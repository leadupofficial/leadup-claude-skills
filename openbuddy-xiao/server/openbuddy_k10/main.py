"""FastAPI entrypoint exposing the xiaozhi WebSocket endpoint the XIAO connects to.

Run:  python -m openbuddy_k10.main      (or `openbuddy-k10` after `pip install -e .`)
"""
from __future__ import annotations

import json
import logging

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from .config import settings
from .protocol import messages
from .session import Session

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("openbuddy_k10")

app = FastAPI(title="OpenBuddy-XIAO", version="0.1.0")


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok", "stt": settings.stt_provider, "tts": settings.tts_provider}


@app.websocket(settings.ws_path)
async def xiaozhi_ws(ws: WebSocket) -> None:
    # Header auth (matches the firmware's `Authorization: Bearer <token>`).
    if settings.auth_enabled:
        auth = ws.headers.get("authorization", "")
        if auth != f"Bearer {settings.auth_token}":
            await ws.close(code=4401)
            log.warning("rejected unauthenticated connection from %s", ws.client)
            return

    await ws.accept()
    device_id = ws.headers.get("device-id", "?")
    log.info("device connected: device-id=%s client=%s", device_id, ws.client)

    async def send_json(obj: dict) -> None:
        await ws.send_text(json.dumps(obj, ensure_ascii=False))

    async def send_bytes(data: bytes) -> None:
        await ws.send_bytes(data)

    session = Session(send_json, send_bytes)

    try:
        while True:
            msg = await ws.receive()
            if msg.get("type") == "websocket.disconnect":
                break
            if (data := msg.get("bytes")) is not None:
                await session.on_audio(data)
            elif (text := msg.get("text")) is not None:
                await _dispatch_text(session, text)
    except WebSocketDisconnect:
        pass
    finally:
        log.info("device disconnected: device-id=%s", device_id)


async def _dispatch_text(session: Session, text: str) -> None:
    try:
        raw = json.loads(text)
    except json.JSONDecodeError:
        log.warning("non-JSON text frame ignored: %r", text[:120])
        return
    parsed = messages.parse(raw)
    if isinstance(parsed, messages.Hello):
        await session.on_hello(parsed)
    elif isinstance(parsed, messages.Listen):
        await session.on_listen(parsed)
    elif isinstance(parsed, messages.Abort):
        await session.on_abort(parsed)
    else:
        log.debug("unhandled message type: %s", raw.get("type"))


def run() -> None:
    uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    run()

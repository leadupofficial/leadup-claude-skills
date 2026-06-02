"""Typed JSON control messages for the xiaozhi-esp32 WebSocket protocol.

Grounded in xiaozhi-esp32/docs/websocket.md. These are the JSON (text) frames; audio
travels as separate binary frames (see binary.py).

Device -> Server : hello, listen, abort, (mcp responses)
Server -> Device : hello, stt, tts, llm, system, alert, (mcp requests)

We model messages loosely (helpers that build dicts) rather than as rigid pydantic
models on the wire, because xiaozhi clients tolerate extra fields and the set of fields
varies by firmware build. Parsing uses small dataclasses for the ones we care about.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

# ---- Server -> Device builders -------------------------------------------------

def hello(session_id: str, sample_rate: int, channels: int, frame_ms: int) -> dict[str, Any]:
    """Server handshake reply. `transport` MUST be 'websocket' or the device disconnects."""
    return {
        "type": "hello",
        "transport": "websocket",
        "session_id": session_id,
        "audio_params": {
            "format": "opus",
            "sample_rate": sample_rate,
            "channels": channels,
            "frame_duration": frame_ms,
        },
    }


def stt(text: str, session_id: str) -> dict[str, Any]:
    """Recognized user speech, echoed to the device for on-screen display."""
    return {"type": "stt", "text": text, "session_id": session_id}


def tts(state: str, session_id: str, text: Optional[str] = None) -> dict[str, Any]:
    """state in {'start','stop','sentence_start'}. Binary opus frames follow 'start'."""
    msg: dict[str, Any] = {"type": "tts", "state": state, "session_id": session_id}
    if text is not None:
        msg["text"] = text
    return msg


def llm(emotion: str, session_id: str, text: str = "") -> dict[str, Any]:
    """UI emotion update -> drives the K10 face. `emotion` must exist in the fw emoji set."""
    return {"type": "llm", "emotion": emotion, "text": text, "session_id": session_id}


def alert(status: str, message: str, emotion: str, session_id: str) -> dict[str, Any]:
    return {
        "type": "alert", "status": status, "message": message,
        "emotion": emotion, "session_id": session_id,
    }


# ---- Device -> Server parsing --------------------------------------------------

@dataclass
class Hello:
    version: int
    audio_format: str
    sample_rate: int
    channels: int
    frame_ms: int
    features: dict[str, Any]


@dataclass
class Listen:
    state: str          # "start" | "stop" | "detect"
    mode: str = "auto"  # "auto" | "manual" | "realtime"
    text: str = ""      # present on "detect" (wake word) in some builds


@dataclass
class Abort:
    reason: str = ""


def parse(raw: dict[str, Any]) -> object | None:
    """Turn an inbound JSON dict into one of the dataclasses above, or None if unhandled."""
    t = raw.get("type")
    if t == "hello":
        ap = raw.get("audio_params", {}) or {}
        return Hello(
            version=int(raw.get("version", 1)),
            audio_format=ap.get("format", "opus"),
            sample_rate=int(ap.get("sample_rate", 16000)),
            channels=int(ap.get("channels", 1)),
            frame_ms=int(ap.get("frame_duration", 60)),
            features=raw.get("features", {}) or {},
        )
    if t == "listen":
        return Listen(state=raw.get("state", ""), mode=raw.get("mode", "auto"),
                      text=raw.get("text", ""))
    if t == "abort":
        return Abort(reason=raw.get("reason", ""))
    # TODO: 'mcp' (JSON-RPC 2.0) channel for IoT/device capability discovery + tool calls.
    return None

"""Per-connection orchestration: handshake → listen → transcribe → agent → speak.

One Session per connected XIAO. It owns the conversation state, the chosen voice
providers, the Opus codec, and the Claude agent.

Phase 0 note: with the stubbed Opus codec, real audio can't be decoded/encoded yet, so
this exercises the *control* path (handshake, `stt` text, `llm` emotion, `tts` start/stop)
but does not move real audio. Once audio/opus_codec.py is implemented, the same code path
decodes uplink audio for STT and sends encoded TTS frames — no other changes needed.
"""
from __future__ import annotations

import logging
import uuid
from typing import Awaitable, Callable

from .agent.claude_agent import ClaudeAgent
from .audio.opus_codec import OpusCodec
from .config import settings
from .pet_state import PetState, emotion_for
from .protocol import binary, messages
from .voice import get_stt, get_tts

log = logging.getLogger("openbuddy_k10.session")

SendJSON = Callable[[dict], Awaitable[None]]
SendBytes = Callable[[bytes], Awaitable[None]]


class Session:
    def __init__(self, send_json: SendJSON, send_bytes: SendBytes) -> None:
        self.id = uuid.uuid4().hex
        self._send_json = send_json
        self._send_bytes = send_bytes
        self.stt = get_stt()
        self.tts = get_tts()
        self.agent = ClaudeAgent()

        self.frame_ms = settings.opus_frame_ms
        self.uplink_rate = settings.uplink_sample_rate
        self.downlink_rate = settings.downlink_sample_rate
        self._codec: OpusCodec | None = None
        self._codec_ok = True  # flips false once we learn opus isn't wired up

        self._listening = False
        self._inbound: list[bytes] = []  # opus frames captured during a listen turn

    # ---- lifecycle ----

    async def on_hello(self, hello: messages.Hello) -> None:
        self.uplink_rate = hello.sample_rate or self.uplink_rate
        self.frame_ms = hello.frame_ms or self.frame_ms
        self._codec = OpusCodec(self.uplink_rate, self.frame_ms)
        await self._send_json(
            messages.hello(self.id, self.downlink_rate, 1, self.frame_ms)
        )
        await self._emote(PetState.IDLE)
        log.info("session %s: hello (v%d, %dHz/%dms)", self.id, hello.version,
                 self.uplink_rate, self.frame_ms)

    async def on_listen(self, listen: messages.Listen) -> None:
        if listen.state == "start":
            self._listening = True
            self._inbound.clear()
            await self._emote(PetState.LISTENING)
        elif listen.state == "stop":
            self._listening = False
            await self._handle_turn()

    async def on_abort(self, _abort: messages.Abort) -> None:
        self._listening = False
        self._inbound.clear()
        await self._emote(PetState.IDLE)

    async def on_audio(self, data: bytes) -> None:
        if self._listening:
            frame = binary.decode(data, version=1)  # v1 = raw opus; change if your fw differs
            self._inbound.append(frame.payload)

    # ---- the turn ----

    async def _handle_turn(self) -> None:
        pcm = self._decode_uplink(self._inbound)
        text = await self.stt.transcribe(pcm, self.uplink_rate)
        if not text:
            await self._emote(PetState.IDLE)
            return
        await self._send_json(messages.stt(text, self.id))

        try:
            reply = await self.agent.respond(text, self._emote)
        except Exception:
            log.exception("agent error")
            await self._emote(PetState.ERROR)
            return

        await self._speak(reply)
        await self._emote(PetState.IDLE)

    async def _speak(self, text: str) -> None:
        await self._send_json(messages.tts("start", self.id, text=text))
        async for pcm_chunk in self.tts.synthesize(text, self.downlink_rate):
            opus = self._encode_downlink(pcm_chunk)
            if opus is not None:
                await self._send_bytes(binary.encode(opus, version=1))
        await self._send_json(messages.tts("stop", self.id))

    # ---- helpers ----

    async def _emote(self, state: PetState) -> None:
        await self._send_json(messages.llm(emotion_for(state), self.id))

    def _decode_uplink(self, frames: list[bytes]) -> bytes:
        """Opus frames -> PCM. Falls back to raw concat if the codec isn't wired (Phase 0)."""
        if self._codec and self._codec_ok:
            try:
                return b"".join(self._codec.decode(f) for f in frames)
            except NotImplementedError:
                self._codec_ok = False
                log.warning("Opus codec not implemented — STT will see raw bytes (Phase 0).")
        return b"".join(frames)

    def _encode_downlink(self, pcm_chunk: bytes) -> bytes | None:
        """PCM -> Opus. Returns None (skips sending) if the codec isn't wired (Phase 0)."""
        if self._codec and self._codec_ok:
            try:
                return self._codec.encode(pcm_chunk)
            except NotImplementedError:
                self._codec_ok = False
                log.warning("Opus codec not implemented — TTS audio not sent (Phase 0).")
        return None

"""Phase 0 providers — no external dependencies, for proving the pipeline end-to-end.

FakeSTT returns a fixed string (so the agent loop runs without a real mic transcription).
FakeTTS emits a short burst of silence so the device's TTS playback path is exercised.
"""
from __future__ import annotations

from typing import AsyncIterator

from .base import STTProvider, TTSProvider


class FakeSTT(STTProvider):
    async def transcribe(self, pcm: bytes, sample_rate: int) -> str:
        # We can't actually recognize speech without a model; return a marker so the
        # rest of the loop (agent -> tts) is observable. Swap in a real provider next.
        seconds = len(pcm) / (2 * sample_rate) if sample_rate else 0
        return f"(heard ~{seconds:.1f}s of audio — FakeSTT placeholder)"


class FakeTTS(TTSProvider):
    async def synthesize(self, text: str, sample_rate: int) -> AsyncIterator[bytes]:
        # ~0.5s of silence, in 20ms chunks of 16-bit mono PCM.
        chunk_samples = sample_rate // 50
        silence = b"\x00\x00" * chunk_samples
        for _ in range(25):
            yield silence

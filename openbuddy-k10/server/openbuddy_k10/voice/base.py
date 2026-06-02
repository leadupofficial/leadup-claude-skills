"""Provider interfaces. Implement these to add a new STT/TTS backend.

Audio convention inside the server is 16-bit mono PCM at the configured sample rate.
Opus (the on-wire format) is decoded/encoded at the protocol boundary (audio/opus_codec),
so providers never deal with Opus directly.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import AsyncIterator


class STTProvider(ABC):
    @abstractmethod
    async def transcribe(self, pcm: bytes, sample_rate: int) -> str:
        """Full-utterance PCM -> text. (Streaming STT can be added later.)"""
        ...


class TTSProvider(ABC):
    @abstractmethod
    def synthesize(self, text: str, sample_rate: int) -> AsyncIterator[bytes]:
        """Text -> stream of 16-bit mono PCM chunks at `sample_rate`.

        Implemented as an async generator so audio can start flowing to the device
        before the whole utterance is rendered (low first-audio latency).
        """
        ...

"""Phase 2 STT — ElevenLabs Scribe v2 (OpenBuddy parity). STUB.

Install:  pip install -e '.[elevenlabs]'   ; set ELEVENLABS_API_KEY.

TODO:
  - Wrap the utterance PCM in a WAV container (16-bit mono @ sample_rate).
  - client.speech_to_text.convert(model_id="scribe_v2", file=wav_bytes)
  - return the transcript text.
"""
from __future__ import annotations

from .base import STTProvider


class ElevenLabsSTT(STTProvider):
    def __init__(self) -> None:
        raise NotImplementedError(
            "ElevenLabsSTT is a stub. Wrap PCM as WAV and call Scribe. See docstring."
        )

    async def transcribe(self, pcm: bytes, sample_rate: int) -> str:  # pragma: no cover
        raise NotImplementedError

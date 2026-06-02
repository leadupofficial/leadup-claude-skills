"""Phase 2 TTS — ElevenLabs v3 (OpenBuddy parity). STUB.

Install:  pip install -e '.[elevenlabs]'   ; set ELEVENLABS_API_KEY + OBK_ELEVENLABS_VOICE_ID.

Request PCM output directly to skip a transcode, e.g. output_format="pcm_16000" (match
`sample_rate`). Stream the chunks straight through.

TODO:
  - client = ElevenLabs(api_key=...)
  - stream = client.text_to_speech.stream(voice_id=..., model_id="eleven_v3",
        text=text, output_format=f"pcm_{sample_rate}")
  - async-iterate and yield each chunk.
"""
from __future__ import annotations

from typing import AsyncIterator

from .base import TTSProvider


class ElevenLabsTTS(TTSProvider):
    def __init__(self) -> None:
        raise NotImplementedError(
            "ElevenLabsTTS is a stub. Wire the ElevenLabs SDK with pcm_<rate> output. "
            "See docstring + PORT_PLAN.md Phase 2."
        )

    async def synthesize(self, text: str, sample_rate: int) -> AsyncIterator[bytes]:  # pragma: no cover
        raise NotImplementedError
        yield b""

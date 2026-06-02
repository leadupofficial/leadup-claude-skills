"""Phase 1 TTS — Microsoft edge-tts (free). STUB.

Install:  pip install -e '.[local-voice]'

edge-tts streams MP3. The device wants PCM (we Opus-encode it downstream), so you must
transcode MP3 -> 16-bit mono PCM at `sample_rate` (ffmpeg, or pydub+ffmpeg, or av).

TODO:
  - communicate = edge_tts.Communicate(text, voice="zh-CN-XiaoxiaoNeural")
  - stream chunks, feed MP3 bytes into an ffmpeg pipe set to: -f s16le -ac 1 -ar {sample_rate}
  - yield the resulting PCM chunks.
"""
from __future__ import annotations

from typing import AsyncIterator

from .base import TTSProvider


class EdgeTTS(TTSProvider):
    def __init__(self, voice: str = "zh-CN-XiaoxiaoNeural") -> None:
        self.voice = voice

    async def synthesize(self, text: str, sample_rate: int) -> AsyncIterator[bytes]:  # pragma: no cover
        raise NotImplementedError(
            "EdgeTTS is a stub. Implement edge-tts -> MP3 -> PCM transcode. See tts_edge.py docstring."
        )
        yield b""  # noqa: unreachable — keeps this an async generator for typing

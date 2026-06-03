"""Pluggable speech providers. Select via OBK_STT_PROVIDER / OBK_TTS_PROVIDER."""
from __future__ import annotations

from ..config import settings
from .base import STTProvider, TTSProvider


def get_stt() -> STTProvider:
    name = settings.stt_provider.lower()
    if name == "fake":
        from .fake import FakeSTT
        return FakeSTT()
    if name == "sensevoice":
        from .stt_sensevoice import SenseVoiceSTT
        return SenseVoiceSTT()
    if name == "elevenlabs":
        from .stt_elevenlabs import ElevenLabsSTT
        return ElevenLabsSTT()
    raise ValueError(f"Unknown OBK_STT_PROVIDER: {name!r}")


def get_tts() -> TTSProvider:
    name = settings.tts_provider.lower()
    if name == "fake":
        from .fake import FakeTTS
        return FakeTTS()
    if name == "edge":
        from .tts_edge import EdgeTTS
        return EdgeTTS()
    if name == "elevenlabs":
        from .tts_elevenlabs import ElevenLabsTTS
        return ElevenLabsTTS()
    raise ValueError(f"Unknown OBK_TTS_PROVIDER: {name!r}")

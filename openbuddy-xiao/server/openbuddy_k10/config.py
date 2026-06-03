"""Environment-driven configuration. See .env.example for all keys."""
from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OBK_", env_file=".env", extra="ignore")

    # server
    host: str = "0.0.0.0"
    port: int = 8000
    ws_path: str = "/xiaozhi/v1"
    auth_token: str = ""  # empty => auth disabled (trusted LAN)

    # brain
    agent_model: str = "claude-sonnet-4-6"

    # voice provider selection
    stt_provider: str = "fake"  # fake | sensevoice | elevenlabs
    tts_provider: str = "fake"  # fake | edge | elevenlabs
    elevenlabs_voice_id: str = ""

    # audio
    uplink_sample_rate: int = 16000
    downlink_sample_rate: int = 16000
    opus_frame_ms: int = 60

    @property
    def auth_enabled(self) -> bool:
        return bool(self.auth_token)


settings = Settings()

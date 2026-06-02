"""Phase 1 STT — SenseVoice via FunASR (local, free, strong zh+en). STUB.

Install:  pip install -e '.[local-voice]'   (pulls torch — heavy; first run downloads the model)

TODO:
  - Load the model once at construction (it's expensive): AutoModel(model="iic/SenseVoiceSmall").
  - In transcribe(), convert the int16 PCM bytes to float32 numpy at `sample_rate`,
    run model.generate(...), and return the text (strip SenseVoice's <|lang|> tags).
"""
from __future__ import annotations

from .base import STTProvider


class SenseVoiceSTT(STTProvider):
    def __init__(self) -> None:
        # from funasr import AutoModel
        # self.model = AutoModel(model="iic/SenseVoiceSmall", disable_update=True)
        raise NotImplementedError(
            "SenseVoiceSTT is a stub. Install '.[local-voice]' and implement model load + "
            "generate(). See PORT_PLAN.md build order step 3."
        )

    async def transcribe(self, pcm: bytes, sample_rate: int) -> str:  # pragma: no cover
        raise NotImplementedError

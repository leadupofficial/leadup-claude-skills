"""Opus <-> PCM conversion. STUB until you turn on real audio (PORT_PLAN.md step 3).

The device sends/receives Opus frames; the voice providers work in 16-bit mono PCM.
This module bridges the two.

Install:  pip install -e '.[audio]'   (also requires the system libopus library:
          apt-get install libopus0   /   brew install opus)

Reference implementation with opuslib:

    import opuslib
    dec = opuslib.Decoder(sample_rate, channels=1)
    pcm = dec.decode(opus_frame, frame_size=int(sample_rate * frame_ms / 1000))

    enc = opuslib.Encoder(sample_rate, channels=1, application=opuslib.APPLICATION_VOIP)
    opus_frame = enc.encode(pcm_chunk, frame_size=int(sample_rate * frame_ms / 1000))

Keep one Decoder/Encoder per session (they hold state across frames).
"""
from __future__ import annotations


class OpusCodec:
    """Per-session Opus decoder+encoder. Replace the bodies with opuslib calls."""

    def __init__(self, sample_rate: int, frame_ms: int, channels: int = 1) -> None:
        self.sample_rate = sample_rate
        self.frame_ms = frame_ms
        self.channels = channels
        self.frame_size = int(sample_rate * frame_ms / 1000)
        # self._dec = opuslib.Decoder(sample_rate, channels)
        # self._enc = opuslib.Encoder(sample_rate, channels, opuslib.APPLICATION_VOIP)

    def decode(self, opus_frame: bytes) -> bytes:
        """Opus frame -> 16-bit mono PCM."""
        raise NotImplementedError(
            "OpusCodec.decode is a stub — install '.[audio]' and wire opuslib (see module docstring)."
        )

    def encode(self, pcm_frame: bytes) -> bytes:
        """16-bit mono PCM (exactly frame_size samples) -> Opus frame."""
        raise NotImplementedError(
            "OpusCodec.encode is a stub — install '.[audio]' and wire opuslib (see module docstring)."
        )

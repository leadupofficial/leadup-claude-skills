"""OpenBuddy-style pet states and their mapping to xiaozhi `llm` emotions.

The K10 (xiaozhi firmware) renders an emotion on screen when it receives an `llm`
message. We translate Claude Agent lifecycle events into these emotions so the pet
visibly reacts to thinking / tool use / completion — the OpenBuddy desk-pet feel.

`EMOTION_MAP` values must be emotion names that exist in *your* firmware build's emoji
set. The list below uses xiaozhi's common default set; adjust to match your fork.
"""
from __future__ import annotations

from enum import Enum


class PetState(str, Enum):
    IDLE = "idle"
    LISTENING = "listening"
    THINKING = "thinking"
    WORKING = "working"      # agent is using a tool
    SPEAKING = "speaking"
    ERROR = "error"


# PetState -> xiaozhi `llm.emotion`
EMOTION_MAP: dict[PetState, str] = {
    PetState.IDLE: "neutral",
    PetState.LISTENING: "neutral",
    PetState.THINKING: "thinking",
    PetState.WORKING: "cool",
    PetState.SPEAKING: "happy",
    PetState.ERROR: "sad",
}


def emotion_for(state: PetState) -> str:
    return EMOTION_MAP.get(state, "neutral")

"""The pet's brain: the Claude Agent SDK (Claude Code).

This is the OpenBuddy-derived differentiator — the device is backed by an *agent* that can
use tools, not just a chat completion. Lifecycle events (thinking, tool use, done) are
surfaced via the `on_state` callback so the K10's face reacts in real time.

Requires:  pip install claude-agent-sdk   ; ANTHROPIC_API_KEY in the environment.

If the SDK isn't installed (or no API key), `respond()` falls back to a canned reply so the
rest of the pipeline (protocol + TTS path) still runs. Replace/extend as you build.

NOTE: the claude-agent-sdk surface evolves between versions. The integration below targets
the `query(...)` async-iterator API; verify against the version you pin in pyproject.toml.
"""
from __future__ import annotations

from typing import Awaitable, Callable

from ..config import settings
from ..pet_state import PetState

OnState = Callable[[PetState], Awaitable[None]]

SYSTEM_PROMPT = (
    "You are OpenBuddy, a small, warm, witty desk companion living inside a DFRobot K10. "
    "You hear the user through a microphone and reply through a tiny speaker, so keep "
    "answers short, spoken, and friendly — usually one or two sentences. You can also help "
    "with real tasks when asked. Reply in the user's language (Chinese or English)."
)


class ClaudeAgent:
    """One instance per device session (keeps conversation continuity)."""

    def __init__(self) -> None:
        self._available = self._probe()

    @staticmethod
    def _probe() -> bool:
        try:
            import claude_agent_sdk  # noqa: F401
        except Exception:
            return False
        import os
        return bool(os.environ.get("ANTHROPIC_API_KEY"))

    async def respond(self, user_text: str, on_state: OnState) -> str:
        """Run one agent turn. Drives pet states via on_state; returns the reply text to speak."""
        await on_state(PetState.THINKING)

        if not self._available:
            # Fallback keeps the pipeline alive without the SDK/key.
            await on_state(PetState.SPEAKING)
            return f"You said: {user_text}. (Claude Agent not configured — set ANTHROPIC_API_KEY.)"

        from claude_agent_sdk import query, ClaudeAgentOptions  # type: ignore

        options = ClaudeAgentOptions(
            system_prompt=SYSTEM_PROMPT,
            model=settings.agent_model,
            # allowed_tools=[...], mcp_servers={...},  # extend to give the pet real abilities
        )

        reply_parts: list[str] = []
        async for message in query(prompt=user_text, options=options):
            # Tool-use messages -> WORKING; text deltas accumulate the spoken reply.
            kind = type(message).__name__
            if "Tool" in kind:
                await on_state(PetState.WORKING)
            text = _extract_text(message)
            if text:
                reply_parts.append(text)

        await on_state(PetState.SPEAKING)
        return "".join(reply_parts).strip() or "…"


def _extract_text(message: object) -> str:
    """Best-effort text extraction across SDK message shapes. Adjust to your SDK version."""
    # Common shapes: message.content -> list of blocks each with .text, or message.text.
    text = getattr(message, "text", None)
    if isinstance(text, str):
        return text
    content = getattr(message, "content", None)
    if isinstance(content, list):
        out = []
        for block in content:
            t = getattr(block, "text", None)
            if isinstance(t, str):
                out.append(t)
        return "".join(out)
    return ""

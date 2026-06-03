# OpenBuddy-XIAO

An AI voice companion ("desk pet") for the **Seeed XIAO ESP32S3 Sense** (ESP32-S3), inspired by
[`lennonkc/openbuddy`](https://github.com/lennonkc/openbuddy) but built to talk to
**xiaozhi-esp32 firmware** that the XIAO already runs.

The key idea borrowed from OpenBuddy: the device's brain is the **Claude Agent SDK**
(Claude Code), not just a chat LLM — so the pet can actually *do* agentic work, and its
animated states are driven by the agent's lifecycle (thinking / using a tool / done).

The key idea borrowed from xiaozhi: don't reinvent firmware or the audio transport.
Your XIAO already streams Opus over a documented WebSocket protocol. This repo is the
**server** that sits on the other end of that socket.

```
 ┌──────────────┐   Opus/WS    ┌─────────────────────────────┐   ┌──────────────┐
 │  XIAO S3     │ ───────────► │  openbuddy server            │   │  Anthropic   │
 │  Sense       │              │  ┌────┐  ┌───────┐  ┌─────┐  │ ─►│  Claude API  │
 │ (xiaozhi fw) │ ◄─────────── │  │STT │─►│ Claude│─►│ TTS │  │   └──────────────┘
 │  mic/spk/    │   Opus/WS    │  └────┘  │ Agent │  └─────┘  │
 │  round LCD   │              │          └───────┘          │
 └──────────────┘              │   pet-state lifecycle hooks │
                               └─────────────────────────────┘
```

> Hardware: **Seeed XIAO ESP32S3 Sense** (onboard PDM mic, no camera) + **Seeed Round
> Display** (GC9A01) + a **MAX98357A** I²S amp & speaker for audio out. See
> `firmware/XIAO_ESP32S3_SENSE_NOTES.md` for the pin map and wiring.
>
> Note: the Python import package is still named `openbuddy_k10` (kept from the original
> K10 target to avoid import churn) — only the hardware target changed.

## What's here

| Path | Status | What it is |
|------|--------|------------|
| `PORT_PLAN.md` | 📄 | Maps OpenBuddy concepts onto XIAO/xiaozhi + the backend decision |
| `ARCHITECTURE.md` | 📄 | How the pieces fit, message flow, extension points |
| `server/` | 🟡 scaffold | FastAPI server: real xiaozhi protocol layer + stubbed voice/agent |
| `firmware/` | 📄 | Notes for pointing your xiaozhi-esp32 XIAO fork at this server |
| `webui/` | ⬜ later | Optional React dashboard (OpenBuddy parity) |

**Status legend:** 📄 doc · 🟡 runnable skeleton with TODOs · ⬜ not started

## Quickstart

```bash
cd server
python -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env        # fill in ANTHROPIC_API_KEY (others optional)
python -m openbuddy_k10.main
```

Out of the box it runs with **fake STT/TTS** (echo pipeline) so you can verify the
WebSocket handshake and message flow with your XIAO *before* wiring up real voice.
See `PORT_PLAN.md` → "Build order" for the recommended path to a fully working pet.

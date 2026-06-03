# Port Plan: OpenBuddy → Seeed XIAO ESP32S3 Sense (xiaozhi base)

This is the plan for the answers you gave: **start fresh**, firmware is a **xiaozhi-esp32
fork on the XIAO**, and you wanted a **backend recommendation**.

## TL;DR recommendation

**Do not port OpenBuddy's firmware.** OpenBuddy wrote its own ESP-IDF firmware *and* its
own WebSocket protocol for M5Stack hardware (Cardputer / StopWatch, ES8311 codec). You
already have a more capable, more widely supported base — **xiaozhi-esp32 on the XIAO** —
which gives you on-device wake word (ESP-SR), Opus streaming, display UI, and OTA for free.

Instead, **lift OpenBuddy's *backend ideas*** (Claude Code as the agent brain + pet-state
lifecycle + clean voice pipeline) and put them behind a server that speaks the **xiaozhi
WebSocket protocol** your firmware already uses. Net result: ~zero firmware work to get
talking, and a clean path to OpenBuddy-grade behavior.

## What maps from OpenBuddy, what doesn't

| OpenBuddy piece | Verdict for XIAO | Why |
|---|---|---|
| FastAPI backend + WebSocket server | ✅ **Reuse the pattern** | Hardware-agnostic; we re-implement against the xiaozhi protocol |
| Claude Code SDK as the agent brain | ✅ **Keep — this is the soul of it** | The whole reason to prefer OpenBuddy over a vanilla xiaozhi server |
| Pet states driven by Claude lifecycle hooks (Stop/PreToolUse/PostToolUse) | ✅ **Keep** | Maps cleanly to xiaozhi's `llm` emotion message → XIAO screen |
| ElevenLabs STT (Scribe) + TTS (v3) | ⚠️ **Optional upgrade, not the start** | Great quality, but paid + latency + 2 cloud deps. Start cheaper (below) |
| Qwen text cleanup | ⚠️ **Optional** | Useful for STT post-processing; skip until it's a problem |
| OpenBuddy firmware (ESP-IDF, LVGL, ES8311) | ❌ **Drop** | XIAO ≠ M5Stack; xiaozhi-esp32 already handles XIAO's display/mic/speaker |
| OpenBuddy's custom WS protocol | ❌ **Drop** | We use the xiaozhi protocol your firmware speaks |
| OpenBuddy React webui | ✅ **Reuse later** | Nice-to-have dashboard; deferred (`webui/`) |

## Backend recommendation (you asked me to advise)

A **swappable voice layer** behind a **Claude Agent brain**, talking the **xiaozhi protocol**:

- **Transport / protocol:** xiaozhi WebSocket v1 (header auth → `hello` handshake → Opus
  binary frames + JSON control messages). Implemented for real in `server/openbuddy_k10/protocol/`.
- **Brain:** **Claude Agent SDK** (`claude-agent-sdk`). This is the OpenBuddy differentiator —
  Claude Code can run tools, not just chat. Lifecycle hooks → pet states. (`server/.../agent/`)
- **Voice — phased, so you're never blocked:**
  1. **Phase 0 (default):** `FakeSTT`/`FakeTTS` echo pipeline — proves the socket end-to-end.
  2. **Phase 1 (cheap/local, recommended start):** local STT (SenseVoice/FunASR, strong zh+en)
     + **edge-tts** (free). No per-minute cost, good enough to live with.
  3. **Phase 2 (OpenBuddy parity):** swap in **ElevenLabs** Scribe (STT) + v3 (TTS) via the
     same `STTProvider`/`TTSProvider` interface. One-line provider switch in config.

Why this order: STT/TTS quality is a *tuning* problem you can iterate on; getting the
**protocol + agent loop** correct is the *architecture* problem. Nail the architecture with
fakes first, then turn the voice quality knob without touching anything else.

### Cost / latency sketch

| Phase | STT | TTS | $/min talk | First-audio latency | Notes |
|---|---|---|---|---|---|
| 0 | fake | fake | $0 | instant | dev only |
| 1 | SenseVoice (local) | edge-tts (free) | ~$0 + your compute | ~medium | needs a box with a bit of CPU |
| 2 | ElevenLabs Scribe | ElevenLabs v3 | $$ | low (streaming) | best UX, OpenBuddy parity |

You can also mix (e.g. local STT + ElevenLabs TTS) — the interfaces are independent.

## Build order

1. **Run the skeleton** with fakes; connect your XIAO (point its WS URL at this server) and
   confirm the `hello` handshake + an echo round-trip. → `firmware/XIAO_ESP32S3_SENSE_NOTES.md`
2. **Wire the Claude Agent** (`agent/claude_agent.py`) — replace the placeholder reply with a
   real `query()`. Confirm text in → text out with personality.
3. **Add real audio**: implement Opus decode/encode (`audio/opus_codec.py`) + a Phase-1
   STT/TTS provider. Now it talks.
4. **Pet states**: map agent lifecycle hooks → xiaozhi `llm` emotion messages → XIAO screen.
5. **(Optional)** ElevenLabs providers, then the React dashboard.

## Open questions to resolve as you build

- **XIAO board target in your fork:** confirm your `BOARD_TYPE` and that uplink is Opus
  16 kHz / 60 ms mono (the xiaozhi default this scaffold assumes).
- **Auth:** decide on the `Authorization: Bearer <token>` value your firmware sends vs. what
  the server checks (`OBK_AUTH_TOKEN`). For a desk device on your LAN you can disable it.
- **Local vs. cloud host:** the server can run on the same LAN as the XIAO (low latency, mDNS
  discovery like OpenBuddy) or in the cloud. Local is recommended for a desk pet.

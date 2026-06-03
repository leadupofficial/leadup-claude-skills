# openbuddy-k10 server

FastAPI server that speaks the xiaozhi WebSocket protocol to a Seeed XIAO ESP32S3 Sense, with a Claude
Agent brain and swappable voice providers. See `../ARCHITECTURE.md` for the layer map.

## Install & run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .                 # core only (Phase 0 fakes)
cp .env.example .env             # set ANTHROPIC_API_KEY to enable the real brain
python -m openbuddy_k10.main
# GET http://localhost:8000/healthz  -> {"status":"ok",...}
```

Optional extras as you progress (see `../PORT_PLAN.md`):

```bash
pip install -e '.[audio]'        # Opus codec (needs system libopus)
pip install -e '.[local-voice]'  # Phase 1: SenseVoice STT + edge-tts
pip install -e '.[elevenlabs]'   # Phase 2: ElevenLabs STT/TTS (OpenBuddy parity)
```

## What runs today (Phase 0)

- ✅ WebSocket endpoint + header auth
- ✅ Full `hello` handshake (adapts to the device's advertised audio params)
- ✅ `listen` / `abort` handling, audio frame capture
- ✅ `stt` text + `llm` emotion + `tts` start/stop control messages (drives the pet face)
- ✅ Claude Agent turn (real, if `ANTHROPIC_API_KEY` set; canned fallback otherwise)
- 🟡 Real audio in/out is stubbed — implement `audio/opus_codec.py` + a voice provider

So Phase 0 lets you verify the device connects, the handshake completes, recognized-text
and emotions show on the XIAO screen, and the agent loop runs — before you invest in audio.

## Layout

```
openbuddy_k10/
  main.py        # FastAPI + WS endpoint (entrypoint)
  config.py      # env settings
  session.py     # per-device turn orchestration
  pet_state.py   # pet states -> xiaozhi emotions
  protocol/      # messages.py (JSON) + binary.py (opus frames) — REAL
  audio/         # opus_codec.py — STUB (Phase 3)
  voice/         # base.py + fake.py (REAL) + provider stubs
  agent/         # claude_agent.py — Claude Agent SDK wrapper
```

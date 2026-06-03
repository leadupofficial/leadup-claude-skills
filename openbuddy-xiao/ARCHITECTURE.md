# Architecture

## Layers

```
server/openbuddy_k10/
├── main.py            FastAPI app + /xiaozhi/v1 WebSocket endpoint (entrypoint)
├── config.py          Settings (env-driven): host/port, auth token, provider choices
├── session.py         Per-connection state machine: handshake → listen → think → speak
├── pet_state.py       OpenBuddy-style pet states + mapping to xiaozhi `llm` emotions
├── protocol/
│   ├── messages.py    Typed JSON control messages (hello/listen/stt/tts/llm/abort/...)
│   └── binary.py      Binary audio frame codecs (v1 raw opus, v2, v3)
├── audio/
│   └── opus_codec.py  Opus <-> PCM helpers (decode uplink, encode downlink)
├── voice/
│   ├── base.py        STTProvider / TTSProvider abstract interfaces
│   ├── fake.py        Phase 0: echo STT + beep/silence TTS (no deps)
│   ├── stt_sensevoice.py / tts_edge.py   Phase 1 (local/free) — stubs
│   └── tts_elevenlabs.py / stt_elevenlabs.py  Phase 2 (OpenBuddy parity) — stubs
└── agent/
    └── claude_agent.py  Claude Agent SDK wrapper + lifecycle→pet-state hooks
```

## Message flow (one turn)

```
device → server : (WS upgrade with headers: Authorization, Device-Id, Client-Id, Protocol-Version)
device → server : {"type":"hello", "version":1, "audio_params":{format:opus,16000,1,60}, ...}
server → device : {"type":"hello", "transport":"websocket", "session_id":..., "audio_params":{...}}
device → server : {"type":"listen", "state":"start", "mode":"auto"}
device → server : <binary opus frames...>            # user speaking
device → server : {"type":"listen", "state":"stop"}
   server: opus → PCM (audio/opus_codec) → STT (voice) → text
server → device : {"type":"stt", "text":"<recognized>"}     # show on screen
   server: text → Claude Agent (agent/claude_agent)
            lifecycle hooks fire → pet_state changes
server → device : {"type":"llm", "emotion":"thinking"}      # drive XIAO face
   server: reply text → TTS (voice) → opus frames
server → device : {"type":"tts", "state":"start"}
server → device : <binary opus frames...>            # pet speaking
server → device : {"type":"tts", "state":"stop"}
```

`abort` (either direction) cancels the current TTS/turn. All control messages carry
`session_id` once the handshake completes.

## Pet states ↔ xiaozhi `llm` emotion

OpenBuddy reacts to Claude Code lifecycle events. We translate those into the `emotion`
field of the xiaozhi `llm` message, which the XIAO firmware renders on screen.

| Agent lifecycle | Pet state | `llm.emotion` sent to XIAO |
|---|---|---|
| turn received | `listening` | `neutral` |
| Claude generating | `thinking` | `thinking` |
| PreToolUse | `working` | `confused`/custom |
| PostToolUse | `working` | `cool` |
| Stop (done) | `speaking` → `idle` | `happy` |
| error | `error` | `sad` |

(Emotion names depend on the emoji set your firmware build ships — see `pet_state.py`.)

## Extension points

- **Swap voice:** set `OBK_STT_PROVIDER` / `OBK_TTS_PROVIDER` in `.env`. New providers just
  implement `STTProvider` / `TTSProvider` in `voice/base.py`.
- **Change the brain's personality / tools:** `agent/claude_agent.py` system prompt + allowed
  tools / MCP servers passed to `ClaudeAgentOptions`.
- **MCP / IoT control:** the xiaozhi protocol carries an `mcp` (JSON-RPC 2.0) channel for
  device capability discovery and tool calls — a natural bridge to the XIAO's hardware
  (LED, sensors). Not implemented in the scaffold; noted as a TODO in `protocol/messages.py`.

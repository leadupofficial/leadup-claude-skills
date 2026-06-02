# webui (deferred)

Optional React dashboard for config + live monitoring, mirroring OpenBuddy's
`openbuddy_webui` (React 19 + Vite + Tailwind). Not needed for a working pet — the server
runs headless. Add this once the voice loop is solid.

Planned panels:
- Connected devices (device-id, session, current pet state)
- Live transcript (`stt`) + agent replies
- Provider switches (STT/TTS) and quick personality/system-prompt edits

It would talk to the server over a separate WebSocket/HTTP admin channel (to be added to
`server/openbuddy_k10/main.py`), kept distinct from the device's `/xiaozhi/v1` socket.

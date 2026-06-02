# DFRobot K10 firmware notes (xiaozhi-esp32)

You said your K10 already runs a **xiaozhi-esp32 fork** — so there's almost nothing to do
on the firmware side except point it at this server. This file captures what to check.

## 1. Point the device at this server

The firmware reads its WebSocket URL from settings (NVS / config / OTA endpoint depending
on your build). Set it to your server:

```
ws://<server-lan-ip>:8000/xiaozhi/v1
```

- Use `ws://` (not `wss://`) unless you put TLS in front of the server.
- The path must match `OBK_WS_PATH` (default `/xiaozhi/v1`).
- If `OBK_AUTH_TOKEN` is set, the firmware must send `Authorization: Bearer <token>`.
  For a desk device on your own LAN, leave the token empty to skip auth.

## 2. Confirm the audio params match

This scaffold assumes the xiaozhi defaults the device advertises in its `hello`:

| Param | Expected | Where to confirm |
|---|---|---|
| format | `opus` | device `hello.audio_params.format` |
| uplink sample rate | `16000` | `hello.audio_params.sample_rate` |
| channels | `1` (mono) | `hello.audio_params.channels` |
| frame duration | `60` ms | `hello.audio_params.frame_duration` |

The server adapts to whatever the device sends in `hello`, so if your build differs, it'll
follow the device — just make sure `audio/opus_codec.py` is built for the same rate/frame.

## 3. Binary frame version

This scaffold defaults to **v1 (raw Opus frames)** in `protocol/binary.py`. If your firmware
build was compiled for BinaryProtocol2/3, switch the `version=` arg in `session.py`
(`binary.decode`/`binary.encode`) to 2 or 3. Watch byte order — the codecs use big-endian.

## 4. Emotions (the pet face)

The server sends `llm` messages with an `emotion` string; the firmware renders the matching
emoji/animation. The names in `server/openbuddy_k10/pet_state.py` (`neutral`, `thinking`,
`happy`, `sad`, `cool`, …) must exist in **your build's** emoji set. If a face doesn't show,
check the emotion list your firmware compiled and update `EMOTION_MAP`.

## 5. Is the K10 board already in xiaozhi-esp32?

xiaozhi-esp32 carries board definitions under `main/boards/`. Confirm your fork has a K10
target (`BOARD_TYPE`) wired for the K10's display + mic/speaker codec. Since you already
have it running, this is presumably done — just note the `BOARD_TYPE` here for the record:

```
BOARD_TYPE = <your K10 board target>
ESP-IDF    = 5.4.x / 5.5.x
```

## Bringing up a board target from scratch (only if you ever need it)

If you later need to (re)create the K10 target: copy the closest existing board under
`main/boards/`, then adjust the display driver (K10 2.8" panel), the I2S mic/speaker pins,
and the audio codec init. See xiaozhi-esp32's "Custom Board Guide". This is the *only* part
that would have been painful to port from OpenBuddy — and you've already done it.

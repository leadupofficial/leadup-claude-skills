# XIAO ESP32S3 Sense firmware notes (xiaozhi-esp32)

Target hardware for this build:

- **Seeed XIAO ESP32S3 Sense** — using its **onboard PDM microphone only** (no camera).
- **Seeed Studio Round Display for XIAO** — GC9A01 1.28" 240×240 + CHSC6X touch.
- **External speaker** — a MAX98357A I²S amp + small 4–8 Ω speaker (the XIAO and the Round
  Display have **no onboard audio output**, so a voice pet needs this to talk back).

Unlike the original K10 target, there is **no ready-made xiaozhi-esp32 board** for this combo —
you create a custom board definition (details below). The server side is unchanged.

## Pin map (chosen tradeoff: keep touch, drop SD + RTC)

The Round Display uses 10 of the XIAO's 11 header pins. The PDM mic is "free" (internal B2B
connector, GPIO41/42 — no header cost). The I²S speaker needs 3 header pins, which we get by
**dropping the SD card**: that frees D2 (SD CS) **and D9** — the GC9A01 is write-only, so it
never uses MISO; MISO is wired only for the SD card. With the always-free D0, that's 3 pins.

| Function | XIAO pin | GPIO | Notes |
|---|---|---|---|
| Display SCK | D8 | 7 | SPI |
| Display MOSI | D10 | 9 | SPI |
| Display CS | D1 | 2 | |
| Display DC | D3 | 4 | |
| Backlight | D6 | 43 | PWM dimming |
| Touch I²C SDA | D4 | 5 | CHSC6X (**kept**) |
| Touch I²C SCL | D5 | 6 | CHSC6X (**kept**) |
| Touch INT | D7 | 44 | |
| **Speaker BCLK** | D2 | 3 | freed by dropping SD (was SD CS) |
| **Speaker LRC/WS** | D9 | 8 | freed by dropping SD (MISO, unused by display) |
| **Speaker DIN** | D0 | 1 | the always-free header pin |
| **Mic PDM CLK** | — | 42 | internal B2B connector |
| **Mic PDM DATA** | — | 41 | internal B2B connector |

**Zero spare header pins.** RTC is unused (it would share touch's I²C bus anyway).

> ⚠️ **Verify before wiring:** confirm your GC9A01 driver build does not read MISO (standard
> for write-only panels). If it does, free a pin elsewhere (e.g. hardwire backlight on to
> reclaim D6). Also re-check the XIAO ESP32S3 D-pin → GPIO mapping against Seeed's
> [pin-multiplexing page](https://wiki.seeedstudio.com/xiao_esp32s3_pin_multiplexing/);
> the GPIO numbers above follow the standard XIAO ESP32S3 pinout.

## Audio

- **Mic:** PDM digital mic, natively **16 kHz mono** — already matches the server scaffold's
  defaults (Opus 16 kHz / mono / 60 ms). No codec chip (ES8311 etc.) is involved; it's raw
  I²S in PDM RX mode.
- **Speaker:** standard I²S TX into the MAX98357A.
- **Two I²S peripherals:** the ESP32-S3 has 2 I²S controllers, so PDM mic (RX) and speaker
  (TX) run independently — no bus contention.

## Creating the xiaozhi-esp32 custom board

There's no upstream board for XIAO + Round Display, so add one (see xiaozhi-esp32's
[Custom Board Guide](https://github.com/78/xiaozhi-esp32/blob/main/docs/custom-board.md)):

1. `main/boards/xiao_esp32s3_round/` — copy the closest existing **GC9A01** board as a base.
2. **Display:** GC9A01 over SPI — SCK=GPIO7, MOSI=GPIO9, CS=GPIO2, DC=GPIO4, BL=GPIO43; 240×240.
3. **Mic input:** I²S PDM — CLK=GPIO42, DATA=GPIO41; 16 kHz mono.
4. **Speaker output:** I²S TX to MAX98357A — BCLK=GPIO3, WS=GPIO8, DOUT=GPIO1.
5. **Touch (optional in firmware):** CHSC6X on I²C (SDA=GPIO5, SCL=GPIO6, INT=GPIO44).
6. Register a `BOARD_TYPE` in `Kconfig`/`CMakeLists.txt`.
7. Build with **ESP-IDF 5.4.x / 5.5.x**.

## Point the device at this server

The firmware reads its WebSocket URL from settings. Set it to:

```
ws://<server-lan-ip>:8000/xiaozhi/v1
```

- Path must match `OBK_WS_PATH` (default `/xiaozhi/v1`).
- If `OBK_AUTH_TOKEN` is set, the firmware must send `Authorization: Bearer <token>`. For a
  trusted-LAN desk pet, leave it empty to skip auth.

## Binary frame version & emotions

- This scaffold defaults to **v1 (raw Opus frames)** in `protocol/binary.py`. If your build was
  compiled for BinaryProtocol2/3, change the `version=` arg in `session.py`.
- The server sends `llm` messages with an `emotion` string; the names in
  `server/openbuddy_k10/pet_state.py` must exist in your firmware build's emoji set. The Round
  Display's GC9A01 rendering may differ from the K10 panel — verify the faces show correctly.

## Hardware gotchas

- **SD card conflict:** if you ever re-add an SD card, cut jumper **J3** on the Sense board to
  avoid an SD-bus conflict with the Round Display. (Moot here — SD is dropped.)
- **Mounting:** the Round Display mounts on the XIAO's header pins (top); the Sense expansion
  is on the bottom B2B connector. Both can be present, but a clean direct-stack may collide —
  **jumper-wire** the display if needed rather than forcing the sandwich.
- **No camera:** simply don't initialize the OV2640 in firmware; the Sense's camera DVP pins
  are then free/unused.

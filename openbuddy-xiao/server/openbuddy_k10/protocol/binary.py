"""Binary audio frame codecs for the xiaozhi WebSocket protocol.

Three on-wire variants exist; the negotiated one depends on firmware build:

  v1: raw Opus frame bytes (no header)  <-- the common default for websocket transport
  v2 (BinaryProtocol2): big-endian
        uint16 version | uint16 type(0=OPUS,1=JSON) | uint32 reserved
        | uint32 timestamp_ms | uint32 payload_size | payload[]
  v3 (BinaryProtocol3): uint8 type | uint8 reserved | uint16 payload_size | payload[]

NOTE: byte order is network/big-endian ('>'). If your fork uses little-endian, flip it.
Start with v1 unless your firmware build was compiled for v2/v3.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

TYPE_OPUS = 0
TYPE_JSON = 1


@dataclass
class Frame:
    type: int
    payload: bytes
    timestamp_ms: int = 0


# ---- v1: raw opus --------------------------------------------------------------

def encode_v1(payload: bytes) -> bytes:
    return payload


def decode_v1(data: bytes) -> Frame:
    return Frame(type=TYPE_OPUS, payload=data)


# ---- v2 ------------------------------------------------------------------------

_V2 = struct.Struct(">HHIII")  # version, type, reserved, timestamp, payload_size


def encode_v2(payload: bytes, type_: int = TYPE_OPUS, timestamp_ms: int = 0) -> bytes:
    return _V2.pack(2, type_, 0, timestamp_ms, len(payload)) + payload


def decode_v2(data: bytes) -> Frame:
    version, type_, _reserved, ts, size = _V2.unpack_from(data, 0)
    payload = data[_V2.size:_V2.size + size]
    return Frame(type=type_, payload=payload, timestamp_ms=ts)


# ---- v3 ------------------------------------------------------------------------

_V3 = struct.Struct(">BBH")  # type, reserved, payload_size


def encode_v3(payload: bytes, type_: int = TYPE_OPUS) -> bytes:
    return _V3.pack(type_, 0, len(payload)) + payload


def decode_v3(data: bytes) -> Frame:
    type_, _reserved, size = _V3.unpack_from(data, 0)
    payload = data[_V3.size:_V3.size + size]
    return Frame(type=type_, payload=payload)


_ENCODERS = {1: lambda p: encode_v1(p), 2: encode_v2, 3: encode_v3}
_DECODERS = {1: decode_v1, 2: decode_v2, 3: decode_v3}


def encode(payload: bytes, version: int = 1) -> bytes:
    return _ENCODERS[version](payload)


def decode(data: bytes, version: int = 1) -> Frame:
    return _DECODERS[version](data)

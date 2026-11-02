---
title: Q2E
short: Quake II Enhanced
game: Quake II Enhanced
year: 2023
arch: x64
theme: q2e
fonts: "family=Chakra+Petch:wght@400;600;700"
order: 4
stage: boots
status: Boots
summary: The first 64-bit guest. Both binaries lift and pass their oracle tests; it runs from the entry point through engine startup.
platforms: Linux x86-64 and macOS (planned)
release: GOG
---

Quake II Enhanced (KEX engine) opens SwARc's 64-bit path: x64 PE
images, the Win64 ABI, AVX, and a Direct3D 11 renderer to bring onto
SwARc's graphics device.

## Status

- Both binaries (`quake2ex_gog.exe` and `baseq2/game_x64.dll`) lift with
  nothing unimplemented, and their integer (41.6K forms) and SSE/AVX
  (6.4K forms) oracle tests pass bit for bit.
- The lifted game runs from the entry point through the CRT startup and
  every global constructor into WinMain, then through Galaxy init
  (offline), the config search, the job system (7 workers), SDL2 init
  with controllers and input, and stops at `XAudio2Create`.

## Next

The remaining imports by area: XAudio2, Direct3D 11 and DXGI, the rest
of SDL2, Winsock and WinHTTP.

The repository is not public yet.

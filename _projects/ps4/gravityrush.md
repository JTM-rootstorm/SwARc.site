---
title: GravityRush-Reshifted
short: Gravity Rush Remastered
game: Gravity Rush Remastered
year: 2015
arch: x64
theme: gravityrush
fonts: "family=Marcellus&family=Alegreya+Sans:ital,wght@0,400;0,700;1,400"
order: 1
stage: boots
status: Title screen
summary: The first PS4 port, on the Orbis module. Runs into the title flow with sound and a picture; the logos, the attract movie's scene and the title prompt draw.
platforms: Linux x86-64 and macOS (planned)
release: CUSA01130, version 01.00 (decrypted dump of your own copy)
repo: https://github.com/JTM-rootstorm/GravityRush-Reshifted
---

The first game on SwARc's PS4 platform module, Orbis, and the test
case it is being built against. It tracks the module's `ps4` branch.

## Status

- The executable plus its bundled `libc` and `libSceFios2` lift (40,881
  functions, 3.75M instructions) with nothing unimplemented. The lifted
  code builds into a module beside a small executable.
- Start-up runs through libc and Fios2 into the game's own: 4.3 GiB of
  direct memory, job threads and fibers, PlayGo and disc-map reads,
  VideoOut (three 1080p display buffers, flips at 60 Hz), PSN (signed
  out), networking, save data, fonts, the pad and trophies.
- It reaches the title flow ("EULA OK", the save data check) and plays
  the attract movie through AvPlayer, running its frame loop at 60 Hz.
- **Sound** through the NGS2 HLE: the game's sampler voices, submixer,
  reverb and mastering racks, mixed at 48 kHz.
- **Fonts** follow the console's FreeType use: its 11 fonts, kerned from
  GPOS or `kern` as the console does.
- **Picture**: the GPU front end draws on SwARc's graphics device.
  Every vertex, pixel and compute shader of the game translates but
  one; tiled textures (1D, 2D, depth) are read and compute image stores
  run. The logos, the attract movie's scene and the title prompt
  ("Press X to tap the Apple") draw.
- An intermittent stop at the title (a race in the game's own copy of
  libSceFios2, worked around in the port) is fixed: none in 600 runs.

## Known gaps

- The 3D scene is framed wrongly (borders, an offset).
- One pixel shader (`ds_swizzle_b32`) does not translate yet.
- A 1080p texture the game samples is written by a GPU pass the
  renderer does not track yet.
- An intermittent fault inside lavapipe (the software Vulkan driver) is
  not understood yet.

## Next

- The GPU: `ds_swizzle`, the scene's framing, the missing texture
  writer, the lavapipe fault.
- Check against a console the values the HLE reports that are not
  measured yet.

The [findings]({{ page.repo }}/blob/main/FINDINGS.md) have the detail.

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
status: Reaches episode 1
summary: The first PS4 port, on the Orbis module. Runs through the title, New Game and the opening movie into episode 1's city, with sound and a picture, then stops at ATRAC9 voices.
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
- Start-up runs through libc and Fios2 into the game's own: direct
  memory, job threads and fibers, PlayGo and disc-map reads, VideoOut
  (three 1080p display buffers, flips at 60 Hz), PSN (signed out),
  networking, save data, fonts, the pad and trophies. The values the HLE
  reports were measured on a console, in this game's process, except a
  few (the user's name, handle values, part of the flip data, two PlayGo
  replies).
- Runs go through the title, New Game and the opening movie (the
  credits over the apple, with the world loading behind it) and reach
  episode 1's city in about 9 minutes, driven by timed pad presses for
  background runs.
- **Sound** through the NGS2 HLE: the game's sampler voices, submixer,
  reverb and mastering racks, mixed at 48 kHz.
- **Fonts** follow the console's FreeType use: its 11 fonts, kerned from
  GPOS or `kern` as the console does.
- **Picture**: the GPU front end draws on SwARc's graphics device.
  Every vertex, pixel, compute and geometry shader of the game
  translates (the bird flocks are geometry-shader draws). The scene
  fills the screen; shadow cascades, depth fast clears, the depth
  target's stencil read as a texture and the sky's banding are right.
- **Frame rate**: the zoom over the city, about 1700 draws a frame, went
  from about 5 to about 160 fps; the apple runs at about 272.

## Known gaps

- ATRAC9 voices in NGS2 are not implemented, which stops runs just
  after reaching the city.
- Episode worlds cannot be booted directly (`-world`); they draw black
  without what the title's New Game sets up.
- The GPU thread limits the frame rate in the zoom.

## Next

- NGS2 ATRAC9 voices, the city's sound.
- The GPU thread's cost per draw.
- A save after the opening, so runs can start from Continue.

The [findings]({{ page.repo }}/blob/main/FINDINGS.md) have the detail.

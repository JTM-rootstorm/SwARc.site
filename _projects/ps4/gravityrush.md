---
title: GravityRush-Reshifted
short: Gravity Rush Remastered
game: Gravity Rush Remastered
year: 2015
arch: x64
theme: gravityrush
fonts: "family=Marcellus&family=Alegreya+Sans:ital,wght@0,400;0,700;1,400"
order: 1
stage: ingame
status: In game
summary: The first PS4 port, on the Orbis module. Plays from New Game into free play in episode 1's city, with sound and its characters drawn whole; autosaves, and Continue loads the save.
platforms: Linux x86-64 and macOS (planned)
release: CUSA01130, version 01.00 (decrypted dump of your own copy)
repo: https://github.com/JTM-rootstorm/GravityRush-Reshifted
---

The first game on SwARc's PS4 platform module, Orbis, and the test
case it is being built against. It builds against SwARc's main branch.

## Status

- The executable plus its bundled `libc` and `libSceFios2` lift (40,881
  functions, 3.75M instructions) with nothing unimplemented, through
  SwARc's lift script, which also lifts the game's other shipped PRXs.
  It starts through the platform's generic PS4 `main()`; the lifted
  code builds into a module beside a small executable.
- Start-up runs through libc and Fios2 into the game's own: direct
  memory, job threads and fibers, PlayGo and disc-map reads, VideoOut
  (three 1080p display buffers, flips at 60 Hz), PSN (signed out),
  networking, save data, fonts, the pad and trophies. The values the HLE
  reports were measured on a console, in this game's process, except a
  few (the user's name, handle values, part of the flip data, two PlayGo
  replies).
- Runs go through the title, New Game, the opening movie and the first
  dialogue scene into **free play in episode 1's city**, and keep
  running (18 minutes without a fatal error). Background runs are driven
  by timed pad presses and held sticks.
- **Saves**: a run plays the first mission (Kat's walk to the old man's
  door) to the first autosave, and **Continue** loads it through the
  system's save data dialog, which SwARc draws over the game.
- **Sound** through the NGS2 HLE: the game's sampler voices, submixer,
  reverb and mastering racks, mixed at 48 kHz, with ATRAC9 voices
  decoded through ffmpeg.
- **Fonts** follow the console's FreeType use: its 11 fonts, kerned from
  GPOS or `kern` as the console does.
- **Picture**: the GPU front end draws on SwARc's graphics device.
  Every vertex, pixel, compute and geometry shader of the game
  translates. Kat, the cat and the other characters (skinned in
  geometry-shader draws, with outline fins) draw whole; shadow cascades,
  depth fast clears, the depth target's stencil read as a texture, the
  sky's banding and textures with all their levels are right.
- **Frame rate**: about 200 fps in free play; the zoom over the city,
  about 1700 draws a frame, went from about 5 to about 160 fps.

Fixed in SwARc on the way: polling loops that the compiler had dropped
(now loaded with acquire atomics), SSE flush-to-zero, `setjmp` and
`longjmp` in x64 images, and a geometry shader's swizzled buffer
addresses.

## Known gaps

- The city's sound has not been checked by ear (runs use a silent
  audio driver).
- Episode worlds cannot be booted directly (`-world`); they draw black
  without what the title's New Game sets up.
- The GPU thread limits the frame rate in the zoom.
- Where Continue puts Kat, the city draws no shadows. The area's own
  lighting turns them off there, so it looks like the game rather than
  the platform; that is still to be confirmed on the console.

## Next

- The GPU thread's cost per draw.
- Playing on from the autosave into the rest of episode 1.

The [findings]({{ page.repo }}/blob/main/FINDINGS.md) have the detail.

---
title: Uncharted-Recharted
short: Uncharted
game: "Uncharted: The Nathan Drake Collection"
year: 2015
arch: x64
theme: uncharted
fonts: "family=Oswald:wght@500;600&family=Source+Serif+4:ital,wght@0,400;0,600;1,400"
order: 2
stage: early
status: Early
summary: The second PS4 port, bringing more of the system onto the Orbis module. The first game plays its intro movies, reaches the title, starts a new game and saves, and stops in its opening cutscene.
platforms: Linux x86-64 and macOS (planned)
release: CUSA02320, base game and patch (decrypted dump of your own copy)
repo: https://github.com/JTM-rootstorm/Uncharted-Recharted
---

The second game on SwARc's PS4 platform module, Orbis. Its job is the
module more than the game: everything it needs that Gravity Rush did
not becomes part of the platform. It builds against SwARc's main branch.

## Status

- The collection ships three executables, one per game (`eboot.bin`,
  `big2-ps4_Shipping.elf`, `big3-ps4_Shipping.elf`), with `libc` and
  `libSceFios2`. Against Gravity Rush they import new libraries: the
  hardware video decoder, libScePosix, more of PSN, the mouse, and the
  error and profile dialogs.
- The first game, Uncharted: Drake's Fortune, lifts (25,333 functions,
  1.88M instructions) and runs: its intro movies, the title screen, a
  new game, saving, and into its opening cutscene.
- What it needed went into the module, each piece measured on the
  console in the game's own process where the answer was not known:
  - the hardware video decoder (Videodec2), with the movies paced by
    the flips at the console's rate;
  - flip mode 2, which flips as soon as a frame is submitted instead
    of at a vblank, timed against the console;
  - ATRAC9 through the audio decoder as the console runs it, including
    the RIFF headers it decodes unasked, on LibAtrac9;
  - direct memory moved between views 1 MiB at a time, with `munmap`
    across many mappings;
  - the save list with a new item, the progress bar dialog, and the
    trophies' unlock state;
  - on the GPU: GDS, wave-wide operations, 64-bit LDS, 16-bit float
    buffer stores, SGPRs spilled to vector lanes, occlusion queries
    and loads from a bounded per-lane offset;
  - in the lifter: F16C, and a clang jump table indexed by a byte
    widened in place.
- It stops in the opening cutscene, where an audio stream's header
  says 6 channels and its ATRAC9 configuration says mono. What the
  console does with that is the next thing to measure.

## Next

- That stream, measured on the console, then on through the first game.
- The second and third games, and how one game starts another
  (`sceSystemServiceLoadExec`).

The [findings]({{ page.repo }}/blob/main/FINDINGS.md) have the detail.

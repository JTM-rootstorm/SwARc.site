---
title: Gears1-ReCogged
short: Gears of War
game: Gears of War
year: 2006
theme: gears
fonts: "family=Teko:wght@500;600&family=Barlow:ital,wght@0,400;0,600;1,400"
order: 1
stage: ingame
status: In game
summary: Plays from a new game through the intro into gameplay, built on ReXGlue for now with an emulated GPU; moving onto x86recomp's Xbox 360 module.
platforms: Linux x86-64 (Vulkan)
release: Title 4D5307D5, disc release (extracted from your own copy)
repo: https://github.com/JTM-rootstorm/Gears1-ReCogged
---

The game's PowerPC code is recompiled ahead of time to C++. For now the
port is built on [ReXGlue](https://github.com/rexglue/rexglue-sdk), which
recompiles it and runs it on Xenia's kernel and an emulated Xenos GPU.
Gears is the reason x86recomp grew its Xbox 360 module: the port moves
onto that module, which already lifts the game and runs its start-up,
as the module matures. Nothing draws there yet.

## Status

- Plays from the menu through a new game and the intro cutscene into
  gameplay, with a controller or keyboard and mouse.
- Fixes to the emulated GPU found here:
  - an NVIDIA device loss and random black spikes on skinned characters,
    both from a shader translation bug (case fallthrough);
  - the red tint and wrong lighting on the default render target path,
    from a gamma conversion done in the wrong direction and the host's
    2x MSAA sample positions mirroring the console's;
  - depth bias applied in exact units (`VK_EXT_depth_bias_control`) for
    flicker-free blood pools and decals, merged into Xenia Canary
    ([#1289](https://github.com/xenia-canary/xenia-canary/pull/1289)).
- A **native renderer** has begun, replacing the emulated GPU at the
  game's own Direct3D level: the game's shaders translated ahead of
  time from its packages, its textures with every mip level, and its
  vertex and index buffers, re-read only when the game writes them.

## Known issues

- Stray black polygons from the game's MSAA predicated tiling, worked
  around with a patch that is on by default.

## Next

- The native renderer drawing frames on its own.
- Native seams for the rest of the system layer (input, audio, files,
  threads), so ReXGlue becomes a scaffold.
- The move onto x86recomp's Xbox 360 module; later macOS on arm64.

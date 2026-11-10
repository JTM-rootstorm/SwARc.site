---
title: CoD1-Reissued
short: Call of Duty
game: Call of Duty
year: 2003
theme: cod1
fonts: "family=Stardos+Stencil:wght@400;700&family=Special+Elite"
order: 2
stage: ingame
status: In game
summary: The training level plays through to completion. Widescreen, Hor+ FOV, a scaled HUD and exact frame caps are in; the renderer's back end is native and draws on SwARc's graphics device.
platforms: Linux x86-64; macOS on Apple Silicon (training played by hand)
release: Steam (app 2620), v1.5b, single player
repo: https://github.com/JTM-rootstorm/CoD1-Reissued
---

A native port of Call of Duty's single player. Goals beyond running
natively: widescreen at any resolution with a UI and HUD that scale
properly, Hor+ field of view, and high refresh rates without the Quake 3
engine family's frame-rate-dependent physics.

## Status

The game's five modules (`CoDSP.exe`, `gamex86.dll`, `cgamex86.dll`,
`uix86.dll` and `EaxMan.dll`) are lifted and linked into one native
program. It boots through the intro cinematics to the main menu with its
music, starts a new game through the briefing, and the training level
plays through to completion (played by hand). EAX 3 works through the
game's own EAX Manager on SwARc's providers.

### macOS

Builds and runs on Apple Silicon (tested on an M3 Pro, macOS 27) with
SDL_GPU on Metal, and passes its tests. Scripted runs play the intro and
reach the training level at 60 fps (vsync, also fullscreen on a 5K
display). The training level has been played by hand on the Mac through
the obstacle course: the signs, the squad's run, the fences, crawling
under the wire and the machine-gun section, the TAB objectives, with
EAX 3 and with Miles. Not yet played to the end of training or past it
on the Mac.

## Native replacements

Each replaces lifted functions and is checked bit for bit against the
lifted original by the project's tests.

- **Widescreen and frame rate**: any resolution, borderless or exclusive
  fullscreen, Hor+ FOV (`cg_fov` is the 4:3 horizontal FOV), and an
  exact `com_maxfps` that sleeps instead of spinning.
- **HUD on wide screens**: elements anchored to the edges keep their
  shapes; menus, briefings and cinematics stay 4:3.
- **Player movement**: footsteps at any step length, `pmove_fixed`
  without rounding.
- **Collision traces**, once about 45% of the main thread in training.
- **Renderer hot path**: culling, sky clipping, texture coordinate
  generation and the draw surface sort; lifted renderer code on the main
  thread went from 12.9% to 4.5%.
- **Renderer back end**, all of it: the GL state, the stages and every
  stage iterator, the dlight and shadow passes, the vertex deforms, the
  colour, alpha and texture coordinate generators, every surface type,
  the sky, flares, portals, the 2D commands and the command loop. Its GL
  calls go straight to SwARc's GL state, and its vertex array draws to
  the graphics device, no longer through the reimplemented `opengl32`.
  Each piece is also checked against the lifted original over 200,000
  random cases and against planted bugs the tests must catch, which
  covers the paths the training level never reaches.
- **XAnim** evaluation and updates.
- **Files**: the pk3 directory scan, zlib and the JPEG inverse DCT on
  the host.
- CPU skinning and a cinematic fix.

## Next

The renderer's front end, natively from the bottom up: the view and its
projection, the draw surface list, the world's cells and static models,
the cell walk through portals, and the scene's entities and polygons.

The project's [FINDINGS.md]({{ page.repo }}/blob/main/FINDINGS.md)
tracks progress and [ARCHITECTURE.md]({{ page.repo }}/blob/main/ARCHITECTURE.md)
the plan.

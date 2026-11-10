---
title: LSWTCS_Rebricked
short: LEGO Star Wars
game: "LEGO Star Wars: The Complete Saga"
year: 2009
theme: lswtcs
fonts: "family=Fredoka:wght@400;600;700"
order: 3
stage: ingame
status: In game
summary: Menus, the cantina and several levels load and play, with keyboard and Xbox pad, paced at the display's refresh rate. Past the first chapter untested. The first Direct3D 9 user.
platforms: Linux x86-64; macOS on Apple Silicon (in game, scripted runs)
release: Steam (app 32440)
repo: https://github.com/JTM-rootstorm/LSWTCS_Rebricked
---

A native port of LEGO Star Wars: The Complete Saga, and the game that
brought Direct3D 9, D3DX 9 and the HLSL translator into SwARc: its
renderer generates HLSL at run time. Goals beyond running natively:
widescreen at any resolution and aspect ratio, and an uncapped frame
rate as an option.

## Status

The Steam EXE unpacks statically (SteamStub 2.1), is lifted, and runs
natively on Linux. Verified:

- the legal screens, the attract movie (Bink) and the title screen;
- the menus, and New Game into the Mos Eisley cantina;
- Negotiations played by hand from the cantina through its chapter and
  cutscenes, its end tally (True Jedi) and on;
- with the `LSWTCS_LEVEL` test hook, which makes New Game start any
  level, the pod race, the Episode III space battle, Tatooine and the
  Hoth snowspeeders load and play (walking, jumping, lightsaber, the
  Force, blasters) with no fatal error;
- every shader met so far translates, both the run-time HLSL and the
  precompiled ones;
- keyboard through DirectInput and an Xbox Series X pad through XInput.

Not yet tested: the minikit build and status screen after a tally,
returning to the cantina, saving and loading, chapters past
Negotiations, the ending.

### macOS

Builds and runs on Apple Silicon (tested on an M3 Pro, macOS 27) with
SDL_GPU on Metal, and passes its tests. Scripted runs show the legal
screens, the attract movie, the title screen and the menus, then New Game
into the cantina at a steady 60 fps (fullscreen and windowed) with the
characters' shadows; with `LSWTCS_LEVEL`, Negotiations loads and runs.
Not yet played by hand on the Mac: scripted keys do not reach the game's
DirectInput keyboard in a background window, so the player has not been
moved there. Bringing it up on Metal fixed four things in SwARc: the
window title (Windows-1252 text), the hidden fullscreen window, rendering
to mip levels, and sampler LOD bias, which Metal lacks (the shadows).

## Frame rate

The original caps itself at about 85 fps, and accepts only display
modes up to 85 Hz, so faster displays get the cap on Windows too. The
port paces it by the host's refresh rate instead: a 120 Hz display gets
a steady 120 fps.

## Known issues

- **Hitches on first play.** The first time a level meets a new
  material or effect, the game stalls while its graphics pipelines are
  built: 25-80 ms each, about 2 s in all on the way into
  Negotiations. The driver caches them, so later plays are smooth.
- Two C runtime jump tables are still dispatched dynamically; neither
  has been reached.
- In-level sound and music have not been checked by ear, nor game speed
  above 120 fps.

## Next

1. Play on past the Negotiations tally: the minikit build, the status
   screen, back to the cantina, saving and loading, the next chapters.
2. More shaders as levels reach more materials.
3. The other enhancements: arbitrary aspect ratios and the resolution
   list.
4. First-play hitches, if they matter: pipelines built on worker
   threads, or smaller shaders.

The project's [FINDINGS.md]({{ page.repo }}/blob/main/FINDINGS.md)
tracks progress and [ARCHITECTURE.md]({{ page.repo }}/blob/main/ARCHITECTURE.md)
the plan.

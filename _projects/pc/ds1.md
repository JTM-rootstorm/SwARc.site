---
title: DS1-Rebuilt
short: Dungeon Siege
game: Dungeon Siege
year: 2002
theme: ds1
fonts: "family=Cinzel:wght@500;700&family=EB+Garamond:ital,wght@0,400;0,600;1,400"
order: 1
stage: playable
status: Playable
summary: Single player plays from a new game to Wesrin Cross, with sound, music, voices and movies. Where SwARc was developed.
platforms: Linux x86-64; macOS on Apple Silicon (in game, scripted runs)
release: GOG, version 1.11.1
repo: https://github.com/JTM-rootstorm/DS1-Rebuilt
---

The project SwARc grew out of: the lifter, x87 model, runtime and
HLE were written for Dungeon Siege and factored out into the shared
library on 2026-10-12.

## Status

Single player is playable from a new game to Wesrin Cross (about an
hour of hand-played testing). Verified in play:

- menus, hero creation, the intro cinematic, Options and Exit;
- movement and combat, with the frame rate holding with a party at the
  krug camp;
- inventory, journal, map, spells, potions, hotkeys, skill level-ups;
- NPC conversations with voice, multi-stage quests, shops and the pack
  mule, party members, death and resurrection;
- region and basement transitions through Stonebridge to Wesrin Cross,
  and the first crypt;
- saving and loading;
- Miles audio (with EAX) and Bink movies.

Debug and release builds hold the game's own 60 fps cap in game.

Not yet seen: regions past Wesrin Cross, the ending.

### macOS

Builds and runs on Apple Silicon (tested on an M3 Pro, macOS 27) with
SDL_GPU on Metal, and passes its tests. Scripted runs go from the menus
and a new game through the intro cinematic (with its voice lines) into
the farm: terrain, animated water, fog, the HUD, the pause menu, sound and
voices, at a steady 60 fps, including fullscreen on a 5K display with the
GPU cursor. Started and checked by hand (the intro, 5K fullscreen, the
cursor) but not yet played by hand.

## Native replacements

- **Widescreen**: the game's window and display mode follow the host
  desktop instead of a fixed 1024x768, and the resolution list goes past
  1024x768 to the desktop size and 16:9 modes up to 3840x2160 (listed in
  the Video tab; choosing one there not yet tried).
- **Hor+ field of view**: wide screens keep 4:3's vertical view and see
  more at the sides, with nothing culled at the edges.
- **UI scale**: the HUD and windows keep their 1024x768 proportions at
  any height, the compass and the cursor with them.
- **Software cursor on the GPU**: the cursor is blended on the GPU with
  an asynchronous readback, which took a 5K display from ~50 to a steady
  60 fps with the window focused.

## Known gaps

- The GDI "Lucida Console" font texture is blank (dev console and debug
  text).
- IME functions are not provided.

The project's [FINDINGS.md]({{ page.repo }}/blob/main/FINDINGS.md)
tracks what works, what was fixed and what is known to be missing.

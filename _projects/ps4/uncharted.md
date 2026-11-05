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
summary: The second PS4 port, bringing more of the system onto the Orbis module. The first game lifts and starts; its first run stops at an app parameter the console has not been asked for yet.
platforms: Linux x86-64 and macOS (planned)
release: CUSA02320, base game and patch (decrypted dump of your own copy)
repo: https://github.com/JTM-rootstorm/Uncharted-Recharted
---

The second game on SwARc's PS4 platform module, Orbis. Its job is the
module more than the game: everything it needs that Gravity Rush did
not becomes part of the platform. It tracks the module's `ps4` branch.

## Status

- The collection ships three executables, one per game (`eboot.bin`,
  `big2-ps4_Shipping.elf`, `big3-ps4_Shipping.elf`), with `libc` and
  `libSceFios2`. Against Gravity Rush they import new libraries: the
  hardware video decoder, libScePosix, more of PSN, the mouse, and the
  error and profile dialogs.
- The first game lifts: 25,333 functions, 1.88M instructions. What is
  left unimplemented is nearly all data decoded as code; the rest is
  F16C's `vcvtph2ps` and one `paddb`, fatal only if reached.
- Its first run gets through the memory setup (1.6 GiB of direct memory
  mapped where the game asks, which widened SwARc's guest arena to
  256 GiB) and the first new imports, handled in the module in the order
  the game reaches them.
- It stops at `sceAppContentAppParamGetInt(1)`: the game's `param.sfo`
  has no such parameter, and what the console answers is being measured
  on the console, from the game's own process, rather than guessed.

## Next

- The console's answer to that call, then on through start-up.
- The second and third games, and how one game starts another
  (`sceSystemServiceLoadExec`).

The [findings]({{ page.repo }}/blob/main/FINDINGS.md) have the detail.

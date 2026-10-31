---
title: PlayStation 4
full: PlayStation 4
order: 2
accent: "#7048e8"
cpu: x86-64 (AMD Jaguar, family 16h)
base: x86recomp Orbis platform module
branch: ps4
state: Module in progress
summary: The first console module on x86recomp's core. The PS4's CPU is x86-64, so it reuses the x64 lifter and adds a platform (executable format, system libraries, GPU).
---

The PS4 runs x86-64 code on an AMD Jaguar CPU, which x86recomp's x64
lifter already models. What a PS4 game needs on top of it is a
**platform module**, Orbis, that plugs into the shared core instead of
forking it: PC builds never compile or link it.

The module is developed on x86recomp's
[`{{ page.branch }}` branch]({{ site.repo }}/tree/{{ page.branch }})
until it is merged into main; its
[commits]({{ site.repo }}/commits/{{ page.branch }}) are the progress
log.

- **Image reader**: decrypted SELF/ELF executables with SCE dynamic
  tables, function starts from `.eh_frame`, imports by NID.
- **Process loader**: maps the executable and its bundled PRX modules,
  links them, and runs their initialisers; the guest's main thread runs
  beside the host loop.
- **System library HLE** by NID, on the core's System V x64 ABI:
  libkernel (memory, pthreads, files, event queues), libSceLibcInternal,
  the system and user services, VideoOut, GnmDriver and the GPU's
  command processor, AudioOut on the software mixer, AvPlayer on ffmpeg,
  SaveData, networking and PSN (signed out), fibers, the NGS2 sound
  engine, fonts on FreeType, the pad and trophies.
- **GPU front end** on x86recomp's graphics device: draws and compute
  dispatches, GCN shaders translated to GLSL, textures in the console's
  tile modes, compute image stores.
- **Next**: the rest of the GPU (the shader instructions left, render
  targets the renderer does not track yet).

Core lifter work it brought: CMPXCHG16B, FXSAVE/FXRSTOR, 256-bit
conversions, `jrcxz`, locked `xchg`, and the System V x64 ABI.

Games come from your own console: a decrypted dump of a copy you own.

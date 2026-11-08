---
title: PlayStation 4
full: PlayStation 4
order: 2
accent: "#7048e8"
cpu: x86-64 (AMD Jaguar, family 16h)
base: SwARc Orbis platform module
module: platforms/orbis
state: Module in progress
summary: The first console module, on SwARc's x86-64 core. The PS4's CPU is x86-64, so it reuses the PC games' lifter and adds a platform (executable format, system libraries, GPU), without any Windows code.
---

The PS4 runs x86-64 code on an AMD Jaguar CPU, which SwARc's x64
lifter already models. What a PS4 game needs on top of it is a
**platform module**, Orbis, that plugs into the x86 core instead of
forking it: PC builds never compile or link it, and it builds without
the Win32 module.

The module is on SwARc's main branch, in
[`{{ page.module }}`]({{ site.repo }}/tree/main/{{ page.module }}), off by
default until it is done; its
[commits]({{ site.repo }}/commits/main/{{ page.module }}) are the progress
log.

- **Image reader**: decrypted SELF/ELF executables with SCE dynamic
  tables, function starts from `.eh_frame`, imports by NID.
- **Process loader**: a generic `main()` for every game: it reads the
  game's `param.sfo` and start modules from `app0`, maps the executable
  and its bundled PRX modules, links them, runs their initialisers, and
  loads the PRXs a game asks for at run time
  (`sceKernelLoadStartModule`, `Dlsym`); the guest's main thread runs
  beside the host loop. A lift script lifts every shipped PRX.
- **System library HLE** by NID, on the core's System V x64 ABI:
  libkernel (memory, pthreads, files, event queues), libSceLibcInternal,
  the system and user services, VideoOut, GnmDriver and the GPU's
  command processor, AudioOut on the software mixer, AvPlayer on ffmpeg,
  the NGS2 sound engine and the Ajm audio decoders (ATRAC9 and MP3 on
  ffmpeg), SaveData, networking and PSN (signed out), fibers, fonts on
  FreeType, Rtc, AppContent, the pad and trophies. The save data and
  message dialogs are drawn by the runtime over the game's frames.
- **GPU front end** on SwARc's graphics device: draws and compute
  dispatches, every GCN shader stage including geometry shaders (run as
  compute passes), textures in the console's tile modes, depth targets
  as 2D arrays with HTILE fast clears and their stencil sampled as a
  texture, compute image stores, texture levels, slices and cube maps,
  indirect and rectangle draws. Work on the cost per draw took the
  busiest scene so far from about 5 to about 160 fps.
- **Next**: the GPU thread's frame time.

Core lifter work it brought: CMPXCHG16B, FXSAVE/FXRSTOR, 256-bit
conversions, `jrcxz`, locked `xchg`, the System V x64 ABI, `setjmp` and
`longjmp` in x64 images, SSE flush-to-zero, and polling loops loaded
with acquire atomics so the compiler cannot drop them.

Games come from your own console: a decrypted dump of a copy you own.

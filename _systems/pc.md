---
title: PC
full: PC (x86 and x86-64)
order: 1
accent: "#1c7ed6"
cpu: x86 (32-bit) and x86-64
base: x86recomp core
state: Ports running
summary: 32-bit and 64-bit Windows games, on x86recomp's Win32 and DirectX/middleware HLE.
---

Windows games for x86 and x86-64 PCs, on x86recomp's main branch. The lifter translates their PE
images to C++, and the runtime reimplements the Windows, DirectX and
middleware APIs they import: Win32 on POSIX and SDL3, Miles, Bink,
DirectDraw/Direct3D 7, OpenGL 1.x, Direct3D 9 and D3DX 9, DirectSound,
DirectInput and XInput, with Direct3D 11 and XAudio2 on the way for x64
games. Graphics run on SDL_GPU: Vulkan on Linux, native Metal on macOS.

32-bit games run in a 4 GiB guest address space with the stdcall/cdecl
HLE ABI; x64 games use the Win64 ABI, the UCRT and MSVCP140, and AVX.

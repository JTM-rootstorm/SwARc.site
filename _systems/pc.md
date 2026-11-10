---
title: PC
full: PC (x86 and x86-64)
order: 1
accent: "#1c7ed6"
cpu: x86 (32-bit) and x86-64
base: SwARc x86 core and Win32 platform module
module: platforms/win32
state: Ports running
summary: Windows games for 32-bit and 64-bit x86 PCs, on the x86 core and the Win32 module.
---

Windows games for x86 and x86-64 PCs, on SwARc's x86 core and Win32
module (both on by default). The x86 core's lifter translates their code
to C++, and the **Win32** platform module reads their PE images and reimplements the Windows, DirectX and
middleware APIs they import: Win32 on POSIX and SDL3, Miles, Bink,
DirectDraw/Direct3D 7, OpenGL 1.x, Direct3D 9 and D3DX 9, DirectSound,
DirectInput and XInput, with Direct3D 11 and XAudio2 on the way for x64
games. Graphics run on SDL_GPU: Vulkan on Linux, native Metal on macOS.

The module is on SwARc's main branch, in
[`{{ page.module }}`]({{ site.repo }}/tree/main/{{ page.module }}); its
[commits]({{ site.repo }}/commits/main/{{ page.module }}) are the progress
log.

It also carries the first native code shared between ports: the Visual
C++ 6 runtime that games link statically (string and memory functions,
64-bit helpers, number parsing and formatting, the `sprintf` and
`sscanf` engines, math intrinsics), reimplemented to match VC6 bit for
bit. A port binds its EXE's copies to it, and an oracle test checks each
function against the lifted original. On the graphics device, every
fixed-function draw carries its whole state, so a port's native
renderer can draw on the device directly, as CoD1's back end does.

32-bit games run in a 4 GiB guest address space with the stdcall/cdecl
HLE ABI; x64 games use the Win64 ABI, the UCRT and MSVCP140, and AVX.

The x86 core and Win32 are separate layers: the core knows no Windows,
so the PS4 module builds on it without any Win32 code.

---
title: Switch
full: Nintendo Switch
order: 3
accent: "#e03131"
cpu: AArch64 (ARM Cortex-A57)
base: x86recomp Horizon platform module, on an AArch64 core
branch: horizon
state: Groundwork
summary: An AArch64 core beside the x86 one, and the Horizon module on it. Lifts and runs a homebrew NRO checked against Unicorn; no ports yet.
---

The Switch's CPU is AArch64, so x86recomp grows a CPU core for it beside
the x86 one: an AArch64 lifter (`recomp_lift_a64`) and the CPU model its
lifted code runs on (integer, flags, the exclusive monitor). The
**Horizon** platform module sits on that core as Orbis sits on the x64
one, and shares the same host layer (SDL3, ffmpeg, the graphics device,
the mixer). A Switch game builds without the x86 path at all.

The module is developed on x86recomp's
[`{{ page.branch }}` branch]({{ site.repo }}/tree/{{ page.branch }})
until it is merged into main; its
[commits]({{ site.repo }}/commits/{{ page.branch }}) are the progress
log.

Status: milestone 1. NRO loading and relocation, the guest address
layout, process bring-up and the first supervisor calls are in. The
tests lift a homebrew NRO fixture built from checked-in assembly and C,
run it against Unicorn, replay every instruction form against Unicorn
vectors (and the host CPU on arm64 hosts, also checked under
qemu-aarch64), and catch planted mutations of the lifted semantics.

Next: milestone 2, a game's `main` lifted whole, reaching `nnMain` and
reading its first RomFS files through `nn::fs`; then milestone 3, the
first frame through NVN on Vulkan and Metal.

Games come from your own console: the extracted ExeFS and RomFS of a
copy you own. No keys or firmware are in any repository.

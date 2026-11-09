---
title: SwARc
port_tiles: true
---
{%- assign systems = site.systems | sort: "order" -%}
{%- assign playable = site.projects | where: "stage", "playable" -%}
{%- assign ingame = site.projects | where: "stage", "ingame" %}

<section class="hero">
  <h1>SwARc</h1>
  <p class="lede">The Swiss Army Recompiler: static recompilation of PC and
  console games into native 64-bit programs for Linux and macOS: the
  scaffold that gets a
  game running natively while its code is replaced, piece by piece, with
  hand-written C++.</p>
  <ul class="stats">
    <li><strong>{{ site.projects.size }}</strong> ports</li>
    <li><strong>{{ systems.size }}</strong> systems</li>
    <li><strong>{{ playable.size }}</strong> playable</li>
    <li><strong>{{ ingame.size }}</strong> in game</li>
  </ul>
  <p class="hero-links"><a class="button" href="{{ site.repo }}">SwARc on GitHub</a></p>
</section>

A game's machine code is translated ahead of time into C++ and linked
against a runtime that reimplements the parts of its operating system
and middleware the game uses. There is no emulator, interpreter or Wine
in the result, and no game code or data in any of the repositories: each
port builds from your own copy of the game.

## Recently updated

<div class="tiles" data-by-date>
{%- for s in systems %}
  {%- assign ports = site.projects | where: "system", s.slug | sort: "order" %}
  {%- for p in ports %}
  {% include tile.html p=p tag=true %}
  {%- endfor %}
{%- endfor %}
</div>

<p class="more"><a href="{{ '/ports/' | relative_url }}">All Ports &rarr;</a></p>

## Systems

<div class="cards">
{%- for s in systems %}
  {%- assign ports = site.projects | where: "system", s.slug %}
  <a class="card system-card" href="{{ s.url | relative_url }}" style="--accent: {{ s.accent }}">
    <h3>{{ s.full }}</h3>
    <p class="game">{{ s.cpu }}</p>
    <span class="badge badge-system">{{ s.state }}</span>{% if s.module %} <span class="branch"><code>{{ s.module }}</code></span>{% endif %}
    <p class="summary">{{ s.summary }}</p>
    <p class="summary count">{% if ports.size == 0 %}No ports yet{% elsif ports.size == 1 %}1 port{% else %}{{ ports.size }} ports{% endif %}</p>
  </a>
{%- endfor %}
</div>

## What SwARc provides

Three layers, each building only on those below it: a **base** every
guest shares, a **CPU core** per guest CPU, and **platform modules** (an
operating system and its libraries) on a core. A game builds its own
platform and core and nothing else: a PS4 game pulls in no Windows code,
a Switch game no x86 code. Everything is on SwARc's main branch, each
core and module behind its own build option; the console modules are in
progress and off by default.

- **Base**: the host layer (SDL3 windows, input and audio output, ffmpeg,
  a graphics device on Vulkan and native Metal with its shader
  compilers, a software mixer with EAX 1-3 reverb), the guest address
  space, frame pacing, and Berkeley SoftFloat under every core's
  floating point.
- **CPU cores**, each a lifter that emits C++ for every function of a
  game's executables with exact semantics, the CPU model that code runs
  on, and tests against an oracle:
  - **x86 and x86-64** (`recomp_lift`): integer, exact 80-bit x87, SSE
    to SSE4.2 and AVX with MXCSR, against a fixed CPU model (AMD family
    16h) that grows only as each feature lifts bit-exactly; tested
    against the host CPU.
  - **PowerPC** (`recomp_lift_ppc`): 64-bit PowerPC in 32-bit mode,
    exact floating point, VMX and the Xenon's VMX128; tested against
    QEMU's PowerPC 970.
  - **AArch64** (`recomp_lift_a64`): integer, flags and the
    exclusive monitor so far; tested against Unicorn and, on arm64
    hosts, the CPU itself.
- **Platform modules**, each reading its own executable formats and
  reimplementing its system libraries (HLE):
  - **Win32** for [PC]({{ '/pc/' | relative_url }}) games, on the x86
    core ([`platforms/win32`]({{ site.repo }}/tree/main/platforms/win32)): PE images, the Win32 process and SEH, Win32 on
    POSIX, the UCRT and MSVCP140, Miles Sound System, Bink,
    DirectDraw/Direct3D 7, OpenGL 1.x, Direct3D 9 and D3DX 9 (HLSL and
    compiled shaders to GLSL), DirectSound 8, DirectInput 8 and XInput.
  - **Orbis** for the [PlayStation 4]({{ '/ps4/' | relative_url }}), on
    the x86-64 core ([`platforms/orbis`]({{ site.repo }}/tree/main/platforms/orbis)).
  - **Xbox 360** for the [Xbox 360]({{ '/x360/' | relative_url }}), on
    the PowerPC core ([`platforms/xbox360`]({{ site.repo }}/tree/main/platforms/xbox360)).
  - **Horizon** for the [Switch]({{ '/switch/' | relative_url }}), on
    the AArch64 core ([`platforms/horizon`]({{ site.repo }}/tree/main/platforms/horizon)).

The lifted code is an exact oracle, not the end product: each port
replaces lifted functions with native C++ one subsystem at a time,
checked against the lifted original, until nothing lifted is left.

The [repository]({{ site.repo }}) has the build instructions and
[ARCHITECTURE.md]({{ site.repo }}/blob/main/ARCHITECTURE.md), the
design.

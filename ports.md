---
title: All ports
permalink: /ports/
---
{%- assign systems = site.systems | sort: "order" %}

# All ports

Every game port built on x86recomp, by system.

<div class="table-scroll">
<table>
  <thead><tr><th>Port</th><th>Game</th><th>Status</th><th>Platforms</th><th>Updated</th></tr></thead>
  {%- for s in systems %}
  {%- assign ports = site.projects | where: "system", s.slug | sort: "order" %}
  {%- if ports.size > 0 %}
  <tbody>
    <tr class="group"><th colspan="5"><a href="{{ s.url | relative_url }}" style="--accent: {{ s.accent }}">{{ s.full }}</a></th></tr>
    {%- for p in ports %}
    <tr>
      <td><a href="{{ p.url | relative_url }}">{{ p.title }}</a></td>
      <td>{{ p.game }} ({{ p.year }}{% if p.arch %}, {{ p.arch }}{% endif %})</td>
      <td><span class="badge badge-{{ p.stage }}">{{ p.status }}</span></td>
      <td>{{ p.platforms }}</td>
      <td>{% if p.repo %}{% include updated.html repo=p.repo %}{% else %}{% include updated.html repo=site.repo branch=s.branch %}{% endif %}</td>
    </tr>
    {%- endfor %}
  </tbody>
  {%- endif %}
  {%- endfor %}
</table>
</div>

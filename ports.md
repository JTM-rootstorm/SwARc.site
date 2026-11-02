---
title: All Ports
permalink: /ports/
---
{%- assign systems = site.systems | sort: "order" %}

# All Ports

Every game port built on SwARc, by system.

{%- assign stages = "playable:Playable,ingame:In game,boots:Boots,early:Early" | split: "," %}
<div class="filters" role="group" aria-label="Filter by status" hidden>
  <button type="button" data-stage="" aria-pressed="true">All <span>{{ site.projects.size }}</span></button>
  {%- for st in stages %}
  {%- assign kv = st | split: ":" %}
  {%- assign n = site.projects | where: "stage", kv[0] | size %}
  {%- if n > 0 %}
  <button type="button" data-stage="{{ kv[0] }}" class="badge-{{ kv[0] }}" aria-pressed="false">{{ kv[1] }} <span>{{ n }}</span></button>
  {%- endif %}
  {%- endfor %}
</div>

<div class="table-scroll">
<table>
  <thead><tr><th>Port</th><th>Game</th><th>Status</th><th>Platforms</th><th>Updated</th></tr></thead>
  {%- for s in systems %}
  {%- assign ports = site.projects | where: "system", s.slug | sort: "order" %}
  {%- if ports.size > 0 %}
  <tbody>
    <tr class="group"><th colspan="5"><a href="{{ s.url | relative_url }}" style="--accent: {{ s.accent }}">{{ s.full }}</a></th></tr>
    {%- for p in ports %}
    <tr data-stage="{{ p.stage }}">
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

<script>
  // Show only the ports at the chosen stage (kept in the URL's #fragment),
  // and hide a system whose ports are all filtered out.
  (function () {
    var filters = document.querySelector(".filters"),
        buttons = filters.querySelectorAll("button");
    function apply(stage) {
      if (!filters.querySelector('[data-stage="' + stage + '"]')) stage = "";
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.stage === stage); });
      document.querySelectorAll("tbody").forEach(function (group) {
        var shown = 0;
        group.querySelectorAll("tr[data-stage]").forEach(function (row) {
          row.hidden = stage !== "" && row.dataset.stage !== stage;
          if (!row.hidden) shown++;
        });
        group.hidden = shown === 0;
      });
    }
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        history.replaceState(null, "", b.dataset.stage ? "#" + b.dataset.stage : location.pathname);
        apply(b.dataset.stage);
      });
    });
    window.addEventListener("hashchange", function () { apply(location.hash.slice(1)); });
    filters.hidden = false;
    apply(location.hash.slice(1));
  })();
</script>

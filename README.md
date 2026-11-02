# SwARc.site

The site for [SwARc](https://github.com/JTM-rootstorm/SwARc), the Swiss
Army Recompiler, and the game ports built on it, by system: served by
GitHub Pages (Jekyll, no Actions) at
<https://jtm-rootstorm.github.io/SwARc.site/>.

- `index.md`: the landing page; its systems and port list are generated.
- `_systems/<system>.md`: one page per system (PC, PS4, Switch, Xbox
  360). `order` sets its position in the Systems menu, `accent` its
  colour on the landing page, `branch` the SwARc branch it is developed
  on until merged into main.
- `_projects/<system>/<port>.md`: one page per port, served at
  `/<system>/<port>/`. The front matter holds the status shown on the
  landing page (`stage` is one of `playable`, `ingame`, `boots`, `early`
  and sets the badge colour; `order` the position in its system); the
  body is the status write-up. A new system's folder also needs a
  `system:` default in `_config.yml`.
- "Updated" dates are not kept by hand: the page asks the GitHub API for
  the latest commit to the port's `repo`, or, for a port without a public
  one, to SwARc on its system's `branch` (main for PC).
- `theme` and `fonts` (a Google Fonts `css2` query) give a port's page
  its own look; the themes are in `assets/themes.css`.

Preview locally, with the base path Pages serves it under:

```sh
jekyll serve --baseurl /SwARc.site
```

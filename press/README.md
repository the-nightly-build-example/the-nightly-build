# press/ — your side of the repo

Everything under `press/` is **yours**; everything outside it is the engine,
owned by upstream. That partition is the whole update story: engine updates
take upstream's version of every path *outside* `press/` and never touch this
folder — so your configuration, voice, themes, and templates can never
conflict with an update.

| File | What it is |
|---|---|
| `site.yaml` | Masthead title, theme file, default appearance |
| `editorial.md` | Your voice — composed into every edition's instructions, after the house style (`spec/editorial.md`) |
| `series/<id>/` | One folder per series: `series.yaml`, `prompt.md`, optional `sources/` |
| `series/_tags/` | Reusable prompt fragments shared across series |
| `themes/` | Custom design-token files (copy `engine/assets/themes/newspaper.css`, edit the variables, point `site.yaml` at it) |
| `templates/` | Your own edition templates: `registry.yaml` entries overlay the shipped registry; `<id>.html` files shadow shipped templates |

On the upstream repo, the contents of this folder are the project's own
dogfood press — they double as living examples. Fork setup replaces them
with yours.

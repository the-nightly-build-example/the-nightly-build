# Brief 01 — writer — the-evidence/the-bitter-lesson

## Begin with these inputs (read in this order)
1. `agent-artifacts/the-evidence/the-bitter-lesson/editorial-direction.md`
2. `agent-artifacts/the-evidence/the-bitter-lesson/writing-coach/01/voice-guide.md` (reread before drafting)
3. `agent-artifacts/the-evidence/the-bitter-lesson/researcher/01/evidence.md` (the complete claim set available to you)
4. `agent-artifacts/the-evidence/the-bitter-lesson/commission.md` (angle, required contribution, structures not to repeat)
5. The initialized article to EDIT: `library/the-evidence/the-bitter-lesson.html` (inside this workspace) — do not recreate its skeleton
6. Generated context in `.nb-context/` (template-contract.yaml, runtime-assets.yaml, furniture/{engine,press,template}.md). The furniture catalog is `/home/user/the-nightly-build/templates/FURNITURE.md` and the lesson bookends are in `/home/user/the-nightly-build/templates/lesson/furniture.md`.

Follow the **writer** skill (Skill tool: `writer`; if unavailable read `/home/user/the-nightly-build/skills/writer/SKILL.md`).

## What to write
A lesson of **1200–2200 words**. Fixed order: `Why this matters` bookend → body →
`The takeaway` bookend → Sources. Write the body first, the two bookends last
(they must read as setup and resolution, this lesson's particulars only, no new
teaching in the takeaway). Body = one `orientation` section plus **0–4 flexible
sections you name** for this piece (lowercase-hyphen `data-nb-section` labels; each
cited). Teach the three ideas in the commission completely and in order; do not
smuggle in a fourth thinly.

Only claims traceable to the evidence record. Every argument-bearing claim carries
an inline `<sup class="nb-cite"><a href="#sN">N</a></sup>` citation. Number sources
in first-citation order; carry each source's `data-nb-kind` (primary/secondary) from
the evidence record. Add `data-nb-locator`/`data-nb-url`/`data-nb-note` only when the
evidence supplies them. If a needed fact is missing, return a researcher REQUEST —
do not write around the hole.

Plan **furniture** with the prose (see the catalog): this piece may benefit from a
small note or a position/holds-up treatment when contrasting Sutton's essay with the
measured scaling evidence — use a component only where it changes understanding, not
for variety. No article-authored scripts/styles/iframes; no external images.

**Background links:** link only already-published lessons (present in
`/home/user/the-nightly-build/library-checkout/library/...`): e.g.
`../the-evidence/scaling-laws-kaplan.html`, `../the-evidence/chinchilla.html`. Use
external links in **Go deeper** (e.g. the essay itself, a critique). The lesson must
stand for a reader who opens none.

## nb-meta (fill with real values)
`protocol` 1.1; `series` the-evidence; `slug` the-bitter-lesson; `template` lesson;
`mode` open; `order` null; `date` "2026-07-31"; `tags` a short topic list you choose
(e.g. ["scaling-laws","compute"]); `sources`/`words`/`reading_minutes` measured, not
targets; `dek` one concrete sentence particular to this piece — and the rendered
`.nb-dekline` must match nb-meta `dek` exactly; `harness` "claude-code-routine";
`model` "claude-sonnet-5". Also set the `<title>`, `.nb-eyebrow` ("The Evidence"),
`<h1>`, and byline date/reading-time.

## Original work
Write the single original-work sentence (what this article does to the evidence that
the evidence does not do itself) in `writer/01/draft-handoff.md` — not in the article.

## Prove and hand off
Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html --series the-evidence --library /home/user/the-nightly-build/library-checkout
```
Treat each WARN as a revision note: fix it or record why it stands. Use
`/home/user/the-nightly-build/nb preview` if layout/furniture needs a look. Write
`writer/01/draft-handoff.md` (original-work sentence; files changed; proof result +
any warnings left; remaining questions).

Return `DONE writer <draft-handoff-path>` only after `BLOCK: 0`, or
`REQUEST researcher/writing-coach/orchestrator <one sentence>`. All content in files.

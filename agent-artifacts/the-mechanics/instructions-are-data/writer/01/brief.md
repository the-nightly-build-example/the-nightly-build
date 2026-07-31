# Brief 01 — writer — the-mechanics/instructions-are-data

## Begin with these inputs (in order)
1. `agent-artifacts/the-mechanics/instructions-are-data/editorial-direction.md`
2. `agent-artifacts/the-mechanics/instructions-are-data/writing-coach/01/voice-guide.md` (reread before drafting)
3. `agent-artifacts/the-mechanics/instructions-are-data/researcher/01/evidence.md`
4. `agent-artifacts/the-mechanics/instructions-are-data/commission.md`
5. Article to EDIT: `library/the-mechanics/instructions-are-data.html`
6. `.nb-context/`; furniture catalog `/home/user/the-nightly-build/templates/FURNITURE.md`

Follow the **writer** skill (Skill: `writer`; fallback `/home/user/the-nightly-build/skills/writer/SKILL.md`).

## What to write
A **qualitative** lesson of **1200–2200 words** (no manufactured statistic, **no
code**), reasoning backward from the behavior to the ground: one flat token stream →
no architectural instruction/data boundary → obedience is trained, not enforced →
therefore injection/jailbreaks. Mark settled vs. open clearly. One `orientation`
section + 0–4 named flexible sections, each cited.

Use **one assembled-prompt example** as illustrative text (system+user+retrieved
concatenation with role markers) to make the mechanism concrete — a short listing/note
is appropriate furniture; it is illustration, not an executable script. Every
argument-bearing claim cited; `data-nb-kind` carried from evidence.

Stay architectural and incident-agnostic. The Gemini image-generation failure is a
**sibling article tonight** — at most one glancing sentence, and do **not** add a
Background link to it (may be unmerged). Background links: only already-published
lessons (from `/home/user/the-nightly-build/library-checkout`): e.g.
`../the-mechanics/attention.html`, `../the-mechanics/autoregressive-generation.html`,
`../the-mechanics/in-context-learning.html`, `../the-evidence/instructgpt.html`.

No scripts/styles/iframes/external images. `machinery` is banned (name the actual
component); other bans per commission.

## nb-meta
series the-mechanics; slug instructions-are-data; template lesson; mode open; order
null; date "2026-07-31"; tags e.g. ["prompt-injection","instruction-tuning","security"];
measured sources/words/reading_minutes; `dek` one concrete sentence = rendered
dekline; harness "claude-code-routine"; model "claude-sonnet-5". Set title, eyebrow
"The Mechanics", h1, byline.

## Original work + proof
Original-work sentence in `writer/01/draft-handoff.md`. Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/the-mechanics/instructions-are-data/library/the-mechanics/instructions-are-data.html --series the-mechanics --library /home/user/the-nightly-build/library-checkout
```
Fix or record every WARN. Return `DONE writer <path>` after `BLOCK: 0`. Content in files.

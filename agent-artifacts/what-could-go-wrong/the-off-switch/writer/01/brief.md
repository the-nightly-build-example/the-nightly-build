# Brief 01 — writer — what-could-go-wrong/the-off-switch

## Begin with these inputs (in order)
1. `agent-artifacts/what-could-go-wrong/the-off-switch/editorial-direction.md`
2. `agent-artifacts/what-could-go-wrong/the-off-switch/writing-coach/01/voice-guide.md` (reread before drafting)
3. `agent-artifacts/what-could-go-wrong/the-off-switch/researcher/01/evidence.md`
4. `agent-artifacts/what-could-go-wrong/the-off-switch/commission.md`
5. Article to EDIT: `library/what-could-go-wrong/the-off-switch.html`
6. `.nb-context/`; furniture catalog `/home/user/the-nightly-build/templates/FURNITURE.md`

Follow the **writer** skill (Skill: `writer`; fallback `/home/user/the-nightly-build/skills/writer/SKILL.md`).

## What to write
A lesson of **1200–2200 words** following the desk's arc: the off-switch/corrigibility
argument at full strength → test against what real systems do (draw the sharp
proof-vs-speculation line; for every "model resisted shutdown" result state exactly
who supplied the goal and how contrived the setup) → the present (who argues it, what
they want) and where confidence outruns proof in **both** directions. Body first,
bookends last. One `orientation` + 0–4 named flexible sections, each cited.

Consider a **holds-up / position** treatment (furniture) to separate what is
demonstrated in a working system from what is analogy — only if it clarifies. Every
argument-bearing claim cited; `data-nb-kind` from evidence; steelman opposing views
before weighing (house rule).

Builds directly on `../what-could-go-wrong/instrumental-convergence.html` — link it
in **Background** (already published) and do not re-run it; your subject is the *fix*
(the off switch) and why it is hard, plus the newest evidence. Other Background
candidates (already published): `../what-could-go-wrong/deceptive-alignment.html`,
`../what-could-go-wrong/orthogonality-thesis.html`. External links in **Go deeper**.

**Bans:** "AI race" is banned (0) — write the incentives/institutions plainly. em-dash
≤ 4; `machinery` 0; others per commission. Name no company as a safety authority.
No scripts/styles/iframes/external images.

## nb-meta
series what-could-go-wrong; slug the-off-switch; template lesson; mode open; order
null; date "2026-07-31"; tags e.g. ["ai-safety","corrigibility","alignment"]; measured
sources/words/reading_minutes; `dek` = rendered dekline; harness "claude-code-routine";
model "claude-sonnet-5". Set title, eyebrow "What Could Go Wrong", h1, byline.

## Original work + proof
Original-work sentence in `writer/01/draft-handoff.md`. Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/what-could-go-wrong/the-off-switch/library/what-could-go-wrong/the-off-switch.html --series what-could-go-wrong --library /home/user/the-nightly-build/library-checkout
```
Fix or record every WARN. Return `DONE writer <path>` after `BLOCK: 0`. Content in files.

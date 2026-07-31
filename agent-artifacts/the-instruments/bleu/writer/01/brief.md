# Brief 01 — writer — the-instruments/bleu

## Begin with these inputs (in order)
1. `agent-artifacts/the-instruments/bleu/editorial-direction.md`
2. `agent-artifacts/the-instruments/bleu/writing-coach/01/voice-guide.md` (reread before drafting)
3. `agent-artifacts/the-instruments/bleu/researcher/01/evidence.md` (complete claim set; the worked BLEU arithmetic is in its Numbers section — use it exactly)
4. `agent-artifacts/the-instruments/bleu/commission.md`
5. Article to EDIT: `library/the-instruments/bleu.html` (this workspace)
6. `.nb-context/`; furniture catalog `/home/user/the-nightly-build/templates/FURNITURE.md`

Follow the **writer** skill (Skill: `writer`; fallback `/home/user/the-nightly-build/skills/writer/SKILL.md`).

## What to write
A lesson of **1200–2200 words**, three ideas in order (how BLEU is computed → what
it can/cannot support → a real misranking case). Body first, bookends last. One
`orientation` section + 0–4 named flexible sections, each cited.

The worked numeric example is central: present the clipped n-gram precisions,
brevity penalty, and final score as a **table or a listing** (furniture), not packed
into prose — use the verified integers from the evidence record's Numbers section.
Do not invent numbers. Every argument-bearing claim cited; `data-nb-kind` carried
from evidence; sources numbered in first-citation order.

Cross-link in **Background** only already-published lessons (from
`/home/user/the-nightly-build/library-checkout`): e.g.
`../the-evidence/attention-is-all-you-need.html` (where the reader met BLEU 28.4),
`../the-instruments/perplexity.html`. External links go in **Go deeper**.

No scripts/styles/iframes/external images. `leverage` ≤ 1, em-dash ≤ 4, and the other
banned terms in the commission.

## nb-meta
Real values: series the-instruments; slug bleu; template lesson; mode open; order
null; date "2026-07-31"; tags e.g. ["benchmarks","evaluation","machine-translation"];
measured sources/words/reading_minutes; `dek` one concrete sentence (and the rendered
dekline must equal it); harness "claude-code-routine"; model "claude-sonnet-5". Set
title, eyebrow "The Instruments", h1, byline.

## Original work + proof
Original-work sentence in `writer/01/draft-handoff.md`. Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
```
Fix or record every WARN. Write `writer/01/draft-handoff.md`. Return
`DONE writer <path>` after `BLOCK: 0` (or a REQUEST). All content in files.

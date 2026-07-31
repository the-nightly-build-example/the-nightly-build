# Brief 02 — writer (revision) — the-instruments/bleu

## Why this round
The editor approved the piece after its own surgical cuts (it fixed two arithmetic
errors directly), with one remaining item that needs new markup only the writer adds.

## Begin with these inputs
1. `editor/01/editorial-review.md` — apply every required item. Required change:
   in the section "The evaluation where the ranking flipped," the Callison-Burch
   Table 4 n-gram comparison **packs eight numbers into two prose sentences.** Convert
   those numbers into a small **table or listing** (see the furniture catalog
   `/home/user/the-nightly-build/templates/FURNITURE.md`), so the counts are read as
   data, not prose. Use the exact numbers already in the piece / evidence record; do
   not introduce new figures. (Do not undo the editor's direct cuts.)
2. `writer/01/draft-handoff.md`, `researcher/01/evidence.md` (the Numbers section has
   the verified Callison-Burch figures), `writing-coach/01/voice-guide.md` (reread),
   `editorial-direction.md`.
3. The article (already editor-edited): `library/the-instruments/bleu.html`.

Follow the **writer** skill. Do not expand the claim set. Keep nb-meta counts honest
if the word count moves.

## Prove and hand off
Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
```
Write `writer/02/draft-handoff.md`. Return `DONE writer <writer/02/draft-handoff-path>`
after `BLOCK: 0`, or a REQUEST.

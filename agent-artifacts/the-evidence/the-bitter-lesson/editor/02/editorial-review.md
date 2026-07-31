# Editorial review 02 — editor (focused re-read) — the-evidence/the-bitter-lesson

## Why this round

Round 01 approved the piece after four direct editorial cuts, with one item
returned to the writer as outside editorial authority: source 11 (Rodney
Brooks, "A Better Lesson") carried `data-nb-kind="primary"` despite being used
throughout the article only to rebut Sutton's essay, never as an independent
finding. This is a focused re-read of writer/02's fix, not a fresh three-read.

## What I re-checked

1. **Source 11's markup.** Read `<li id="s11">` in the Sources list directly:
   `data-nb-kind="secondary"`. The flip from `primary` to `secondary` was
   made and nothing else in that `<li>` changed.

2. **The classification itself.** Confirmed against how the article actually
   deploys Brooks: every citation of source 11 in the body quotes "A Better
   Lesson" to rebut or qualify a claim in Sutton's essay (the primary
   document under review), never to source an independent factual finding of
   its own. That is a critique of a primary text by an outside party — the
   textbook case for `secondary` — and matches the round-01 audit standard
   for this piece ("the essay and the scaling papers are primary; a critique
   is secondary"). Correct label.

3. **Source-kind floor.** Counted all 11 `data-nb-kind` attributes directly
   in the file: 8 `primary` (Sutton essay, Deep Blue retrospective, AlphaGo
   2016 Nature paper, AlphaGo Zero post, Kaplan et al., Chinchilla, the
   Transformer paper, InstructGPT), 3 `secondary` (Sutton's Wikipedia page,
   "Bitter lesson" Wikipedia page, Brooks's critique). The `the-evidence`
   series floor requires min 6 sources, primary ≥ 3, secondary ≥ 1 — 8/3/11
   clears every threshold with margin, matching both the writer's and the
   round-01 editor's count.

4. **No regression.** Grepped for the four round-01 direct-cut sites (the
   uncomputed "five months" AlphaGo Zero gap, the misattributed 3.5-day
   BLEU training-time figure, the body's reader-address, and the
   "this course has already covered" self-reference) — none reappeared; the
   round-01 corrected wording stands untouched. The writer's round-02 diff
   was a single-attribute markup change, as declared; no prose, no other
   markup, no `nb-meta` field was touched.

5. **Proof.** Re-ran the deterministic check:
   ```
   /home/user/the-nightly-build/nb check .nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html --series the-evidence --library /home/user/the-nightly-build/library-checkout
   ```
   Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.

## Skeptic / Cut / Reader

Not repeated this round — this is the focused re-read the brief calls for,
following round 01's three full reads. The only substantive change under
review is the source-11 markup fix, which is a sourcing-classification
correction, not a claim, cut, or reader-value question; nothing in the prose,
structure, or claims changed since round 01's passing reads.

## Direct edits made

None. The writer's fix was correct and complete on inspection; no further
editorial action was needed.

## Required work by owner

None outstanding.

## Decision

Settled. Source 11 is now correctly `data-nb-kind="secondary"`, the
source-kind floor (primary ≥ 3, secondary ≥ 1) clears comfortably at 8/3, no
regression was introduced by the change, and the proof is clean
(`BLOCK: 0 / WARN: 0 / PUBLISHABLE`). No redraft required.

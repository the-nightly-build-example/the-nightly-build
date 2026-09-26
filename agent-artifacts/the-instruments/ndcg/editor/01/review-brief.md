# editor review-brief: the-instruments/ndcg (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — assignment and the "Angle refinement" the writer drafted to.
- writer/01/brief.md (../../writer/01/brief.md) — the exact writer brief.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — read first.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — open when a claim needs testing; it holds two arithmetic-verified worked examples.
- writer/01/draft-handoff.md (../../writer/01/draft-handoff.md).
- Article: /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/library/the-instruments/ndcg.html

Output:
- /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/agent-artifacts/the-instruments/ndcg/editor/01/editorial-review.md

Proof (run yourself after edits, links included): /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/library/the-instruments/ndcg.html --series the-instruments --repo /home/user/the-nightly-build

## Test hardest on this piece

- The three tables' arithmetic. Recompute the worked nDCG example and the
  linear-vs-exponential example against the record's verified numbers; confirm
  they are consistent with the definitions. Check the BEIR TREC-COVID table cells
  (ANCE 0.654 -> 0.735; docT5query 0.713 -> 0.714; Hole@10) against the record.
  The writer built this table from the record's figures rather than capturing
  BEIR Table 4 (the record lacks BM25/TAS-B before/after cells); that is an
  acceptable choice if the caption claims only what the cells show and BM25/
  ColBERT context stays in prose. Confirm the caption does not overclaim.
- The narrow angle: a single nDCG@10 hides its choices and can move without a
  system improving. Confirm the piece does NOT argue "nDCG is bad" and that the
  Sanderson 2010 and Wang 2013 defenses are represented fairly.
- The "collapses to rank-of-first-hit" point is presented as a derived
  consequence (cited to Craswell sparsity + definitions), not attributed to a
  source that does not state it.
- Every number/name/date in headline, dek, subheads verified; data-nb-kind
  audited; every citation href opens to the source (gated ACM DOIs that 403 the
  probe are acceptable canonical homes and never block).

## Recent-pattern notes

- Reject the "When a chipmaker says ..." opener mold and the "By the end you will
  know A, B, and C" closer. Check the dek against mlperf/attack-success-rate/helm/
  calibration-error so it is built on its own pattern; check headings for stamping.

## Your job

Decide whether it publishes; edit anything except the facts. Cut slop (placeholder
test on the edges), catch briefing leaks (read commission.md) and voice-guide
borrowings, check it repeats neither the recent record nor a neighbour (mteb).
Fix what you can from the record and this checkout and run the proof to BLOCK: 0
after edits (direct cuts that still pass owe no writer round; restamp if counts
change). Redraft only if it needs a different argument. Write editorial-review.md
(Correct / Reads well / The experience / Edits / Decision). Report the review
path, the decision, the final BLOCK count, and anything for the orchestrator.

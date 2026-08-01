# Editor review-brief 02 — the-instruments/tokens-per-second (re-review after correction)

Load the `editor` skill. This is invocation 02, after your 01 REQUEST researcher
(batch-vs-length confound) was resolved. Do the three ordered reads again on the
revised piece, but concentrate on what changed; do not reopen settled 01 findings
you already cleared.

## Inputs (named)
- Corrected evidence (authoritative): `../../researcher/02/evidence.md`
  (Numbers "CORRECTED" + "NEW — MLPerf Offline/Server/Interactive" tables).
- Your prior review: `../01/editorial-review.md`.
- The writer's revision handoff: `../../writer/02/draft-handoff.md`.
- Writer brief 02: `../../writer/02/brief.md`. Also editorial-direction, the
  exact writer brief 01, voice guide, the article, .nb-context.

## What to verify hardest
1. The pillar-2 worked example is now the MLPerf same-hardware Offline/Server/
   Interactive series (latency-bound tightening cuts throughput ~1/3 to 2/3),
   NOT the discarded batch-size framing. Confirm the broken 1,349/4,750/11,819
   "batch effect" is gone and no residual sentence still implies batch size alone
   drove those three numbers. If the one llama_70b aside (341 vs 303 tok/s/GPU)
   is kept, confirm all four held-constant conditions are stated.
2. chart-1 (library/the-instruments/tokens-per-second/chart-1.png, provenance
   chart-1.py): inspect the image and provenance. Its numbers must match the
   MLPerf table in researcher/02; axes labeled; each scenario labeled with its
   actual latency bound (200 ms / 40 ms TPOT), not just the name; caption cites
   the MLPerf results file; no misleading scale.
3. The section still reads as continuous teaching after the surgery (no seam).

Make surgical prose cuts directly; anything past a clause or any markup/asset fix
returns to the writer. Write `editor/02/editorial-review.md` (three lines + edits
+ required work + decision). Return exactly one line:
`DONE editor .../editor/02/editorial-review.md` (only if NO redraft required), or
`REQUEST writer/researcher/orchestrator <need>`.

# Writer brief 02 — the-instruments/tokens-per-second (revision)

Load the `writer` skill. This is invocation 02, a revision. Reread the voice
guide before editing. Edit the CURRENT article in place (it already carries the
editor's 01 surgical cuts — preserve them). Do not recreate the skeleton.

## Inputs (named)
- Corrected evidence (authoritative now): `../../researcher/02/evidence.md`.
  Read its Numbers "CORRECTED" and "NEW — MLPerf ... Offline/Server/Interactive"
  tables and its Source-assets notes.
- The editor's review that triggered this: `../../editor/01/editorial-review.md`
  (the batch-vs-length confound and anything else it required).
- Prior article, voice guide, editorial-direction, commission, .nb-context — as
  in writer/01 brief (`../01/brief.md`).

## Required fixes (apply exactly these)
1. Remove the broken pillar-2 worked example built on the TensorRT-LLM H200 rows
   1,349 / 4,750 / 11,819 tok/s framed as a batch-size-alone effect. Those three
   rows vary batch size AND input length AND output length together and cannot
   show a batch effect. Do not present them as one.
2. Rebuild pillar 2 (batch/concurrency effect on throughput) on the corrected,
   audited, same-hardware series: MLPerf v5.1 Offline/Server/Interactive
   throughput for Llama2-70B on identical hardware, where tightening the per-token
   latency bound (Server 200 ms TPOT → Interactive 40 ms TPOT), hardware and model
   held fixed, cuts aggregate throughput by ~a third to two-thirds on every
   platform. Use the evidence record's exact numbers and label scenarios with
   their actual latency bounds, not just names. This is the honest version of the
   "throughput per user vs aggregate / concurrency" point.
   - You MAY keep, as a one-line labeled aside only, the single clean pair from the
     TensorRT table (llama_70b, 2,048 in / 128 out, TP=1: batch 64 → 341 vs batch
     32 → 303 tok/s/GPU, a 12.5% lift), explicitly stating all four held-constant
     conditions. Or cut it. Do not build the pillar on it.
3. Rebuild chart-1 with `nb chart` from the MLPerf same-hardware series (a readable
   subset per the evidence's Source-assets note — e.g., the 6 B200 rows, or one
   B200 + one H200 + one MI300X row — as grouped bars: Offline/Server/Interactive
   per platform, or a Server-vs-Interactive comparison). Label axes, name the
   latency bound each scenario enforces, cite the MLPerf results file in the
   caption. Inspect the rendered PNG for honesty. Commit the new chart-N.py
   provenance; remove the stale chart if its data changed.
4. If removing the confounded example changes surrounding prose, mend the seams so
   the section still teaches cleanly. Address any other required item in the
   editor/01 review. Update `nb-meta` sources/words counts to the true totals.

## Prove and hand off
Run to `BLOCK: 0` (final proof WITH link checking):
`./nb check .nb-work/the-instruments/tokens-per-second/library/the-instruments/tokens-per-second.html --series the-instruments --repo /home/user/the-nightly-build --library /home/user/library-checkout`
Write `writer/02/draft-handoff.md`: original-work sentence; paths changed; proof
result + warnings left; every editor/researcher request addressed; open questions.

Return exactly one line: `DONE writer .../writer/02/draft-handoff.md`, or a REQUEST line.

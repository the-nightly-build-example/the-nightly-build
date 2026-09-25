# writer brief: the-instruments/mlperf (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md).
Article + context under .nb-work/the-instruments/mlperf/ (HTML at
library/the-instruments/mlperf.html; .nb-context/ has furniture + contract).
Output: ./draft-handoff.md (+ edited article HTML)
Proof:  ./nb check .nb-work/the-instruments/mlperf/library/the-instruments/mlperf.html --series the-instruments --repo $(pwd)

Work from these inputs only; ask me where something is missing.

Focus: teach the four ideas in commission.md in order. Spine: MLCommons fixes a
task/model/quality target and vendors submit on their own systems -> divisions
and availability categories are the rules that make one number comparable to
another -> the number supports an apples-to-apples system comparison, not a
model-quality or real-workload claim -> a documented "record"/"N times faster"
claim that compared across non-comparable configurations, and what it cost.
Original-work sentence in draft-handoff.md: an MLPerf result is a time or
throughput for one system on one fixed task under one set of rules, comparable
only inside that box, and the headlines strip the box away. Link
tokens-per-second or training-compute at first use; do not re-teach the raw
metric.

Recent-pattern notes to break (the-instruments): do NOT mirror the HELM piece's
spine or opener; headings distinct from each other. Dek: one lean sentence with
one concrete detail (a real result or chip count), no "bare X means little"
mold, no comma-triad.

Furniture: a table showing one comparable pair and one non-comparable pair
(system, chip count, division, category, result) carries the thesis; a source
asset of an MLPerf results table is legitimate if you use what it shows. Numbers
from evidence exactly. nb-meta: date 2026-09-25, harness+model "Claude Opus 4.8",
4-5 tags, dek identical to rendered dekline. nb stamp, then proof to BLOCK: 0.

# editor brief: the-instruments/mlperf (editor/01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md),
writer brief (../../writer/01/brief.md) + draft-handoff.md (../../writer/01/draft-handoff.md).
Article HTML: .nb-work/the-instruments/mlperf/library/the-instruments/mlperf.html
Output: ./editorial-review.md
Proof:  ./nb check .nb-work/the-instruments/mlperf/library/the-instruments/mlperf.html --series the-instruments --repo $(pwd)

Follow the nb-editor skill. Correct, reads well, good to read.

Correctness priorities: verify the Closed/Open division and availability-category
definitions against the MLCommons rules doc, and every result number (time,
throughput, chip count, division, category) against the results table that owns
it. The load-bearing claim is that a result is comparable only within the same
division/category/task/scale; verify the "misled" example actually crosses one
of those boundaries and is stated precisely (the writer must not overstate a
fair comparison as unfair or vice versa). Present the disputed claim and any
MLCommons/vendor framing fairly. Name no company as an authority. Audit
data-nb-kind (rules docs/results tables primary; vendor marketing primary for
its claim only; analysis secondary). Open every href.

Recent-pattern enforcement: no mirror of the HELM piece's spine/opener; headings
distinct; dek carries no "bare X means little"/comma-triad mold. Read the last
sentence of the piece and each section hardest. Confirm the takeaway resolves
the opener, teaches nothing new, and the body never refers to itself. Redraft
only for a wrong argument; else edit directly, re-run nb stamp + proof to
BLOCK: 0, record the decision.

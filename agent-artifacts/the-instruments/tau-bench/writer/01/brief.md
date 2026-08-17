# writer brief: the-instruments/tau-bench (01)

Inputs:
- editorial-direction.md — the standard to cite and write to (at the artifact root)
- commission.md — the measurement, angle, what-it-teaches list, boundaries, neighbors to link (at the artifact root)
- writing-coach/01/voice-guide.md — how this series sounds (reused from a same-series sibling; take craft/register, not its subject)
- researcher/01/evidence.md — the complete set of claims and figures available to you, and the neighbor slugs to link
- library/the-instruments/tau-bench.html — the initialized article to edit (at .nb-work/the-instruments/tau-bench/library/the-instruments/tau-bench.html); template context under .nb-context

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/tau-bench/library/the-instruments/tau-bench.html --series the-instruments

The pass@1-versus-pass^k reliability gap is the teaching spine; a chart is allowed
only if built from the paper's own verified figures via ./nb chart (commit its
provenance). Link published the-instruments neighbors (per the evidence record)
rather than re-teach them. Match the house voice: sentence-case declarative
headline stating the finding, one concrete dek; the house uses two-clause commas
but varies the connector, so do not default every line to "..., and ...". Set
nb-meta harness to `Claude Code` and model to `capable`.

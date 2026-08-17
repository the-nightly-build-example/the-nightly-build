# writer brief: what-could-go-wrong/model-collapse (01)

Inputs:
- editorial-direction.md — the standard to cite and write to (at the artifact root)
- commission.md — the argument, steelman-then-test structure, what-it-teaches list, the no-authority rule, neighbors to link (at the artifact root)
- writing-coach/01/voice-guide.md — how this series sounds (reused from a same-series sibling; take craft/register, not its subject)
- researcher/01/evidence.md — the complete set of claims and figures available to you, and the neighbor slugs to link
- library/what-could-go-wrong/model-collapse.html — the initialized article to edit (at .nb-work/what-could-go-wrong/model-collapse/library/what-could-go-wrong/model-collapse.html); template context under .nb-context

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/what-could-go-wrong/model-collapse/library/what-could-go-wrong/model-collapse.html --series what-could-go-wrong

Hold the sharp line between the demonstrated result (replacement collapses models
in experiments) and the extrapolation (collapse at real-web scale); give the
accumulation rebuttal its full strength. Name no company as an authority; attribute
to documents and authors. Link published neighbors (per the evidence record)
rather than re-teach. Match the house voice: sentence-case declarative headline
stating the finding, one concrete dek; the house uses two-clause commas but varies
the connector, so do not default every line to "..., and ...". Set nb-meta harness
to `Claude Code` and model to `capable`.

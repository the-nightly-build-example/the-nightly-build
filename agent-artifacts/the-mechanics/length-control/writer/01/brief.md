# writer brief: the-mechanics/length-control (01)

Inputs:
- editorial-direction.md — the standard to cite and write to (at the artifact root)
- commission.md — the behavior, backward-tracing angle, what-it-teaches list, the no-code rule, neighbors to link (at the artifact root)
- writing-coach/01/voice-guide.md — how this series sounds (reused from a same-series sibling; take craft/register, not its subject)
- researcher/01/evidence.md — the complete set of claims and figures available to you, and the neighbor slugs to link
- library/the-mechanics/length-control.html — the initialized article to edit (at .nb-work/the-mechanics/length-control/library/the-mechanics/length-control.html); template context under .nb-context

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/length-control/library/the-mechanics/length-control.html --series the-mechanics

No code. The article's original work is the synthesis: link the published
autoregressive-generation and letter-counting lessons rather than re-teaching
token-by-token decoding or tokenization, and spend your words on why the
combination (no counter, wrong unit, no revision, trained-in length bias) produces
the length-count failure. Mark settled versus open plainly. Match the house voice:
sentence-case declarative headline stating the finding, one concrete dek; the
house uses two-clause commas but varies the connector, so do not default every
line to "..., and ...". Set nb-meta harness to `Claude Code` and model to `capable`.

# writer brief: the-evidence/foundation-models (01)

Inputs:
- editorial-direction.md — the standard to cite and write to (at the artifact root)
- commission.md — the document, angle, what-it-teaches list, boundaries, neighbors to link (at the artifact root)
- writing-coach/01/voice-guide.md — how this series sounds (reused from a same-series sibling; take craft/register, not its subject)
- researcher/01/evidence.md — the complete set of claims and figures available to you, and the neighbor slugs to link
- library/the-evidence/foundation-models.html — the initialized article to edit (at .nb-work/the-evidence/foundation-models/library/the-evidence/foundation-models.html); template context under .nb-context

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/foundation-models/library/the-evidence/foundation-models.html --series the-evidence

The library is an established course, not a blank slate. Link published the-evidence
neighbors (per the evidence record) at first use in prose and in the Background
band instead of re-teaching them. Match the house voice: sentence-case declarative
headline stating the finding, one concrete dek. Avoid making every dek/heading a
two-clause "..., and ..." construction — the house voice uses that shape but
varies the connector; vary yours. Set nb-meta harness to `Claude Code` and model
to `capable`.

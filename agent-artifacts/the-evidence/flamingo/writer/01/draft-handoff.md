# Draft handoff: the-evidence/flamingo (01)

## Original-work sentence

This piece turns the researcher's separately listed facts and contradictions
into one bounded argument: it recomputes which two of the six "winning"
benchmarks (OKVQA, MSVDQA) fall inside the paper's own five-task DEV set by
cross-referencing two sets the evidence record states separately but never
intersects itself, and it corrects the evidence record's own scope note on the
"around 1000x less data" figure — recomputing the true high end from the
evidence's own quoted annotation counts (COCO/VATEX at ~15,600-to-1, not
VQAv2 as the evidence's Numbers section states) — so a reader gets one
worked, checkable range instead of a rounded slogan.

## Proof result

`./nb stamp` then `./nb check .nb-work/the-evidence/flamingo/library/the-evidence/flamingo.html --series the-evidence --library .nb-work/library` (links included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE. 1,997 words, 9 min read, 6 sources (5 primary, 1 secondary), all against the 1,200–2,200 word band.

No warnings were left intentionally; all W-SENTENCE-DENSITY flags raised on the first pass were resolved by splitting the flagged sentences, and no other warning class fired.

## Open evidence gap

The commission's item 3 asks the piece to say plainly that Flamingo "still
hallucinated and had the known failure modes the paper documents" (Section 5 /
Appendix D.1). The evidence record names those locators but supplies no quote
or specific paraphrase of what the failure modes actually are, so nothing
citable exists for that claim. I omitted it rather than invent specifics, and
the piece's required contribution (bounded few-shot result, mechanism, and
where the design was outgrown) stands without it. If this needs covering, it
requires a second researcher pass on Section 5 / Appendix D.1 for a concrete,
quotable failure case.

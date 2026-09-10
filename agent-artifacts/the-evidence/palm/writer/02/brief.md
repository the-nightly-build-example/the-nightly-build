# writer brief: the-evidence/palm (02) — revision

Apply the required item in the editorial review, nothing else.

Inputs:
  ../01/../editor/01/editorial-review.md — the review to apply (Required work: the quote fix)
  ../../researcher/01/evidence.md — for the exact wording of the Wei et al. definition
  ../../../../library/the-evidence/palm.html — the article to edit in place
  ../../editorial-direction.md — standard

Output: ./draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/palm/library/the-evidence/palm.html --series the-evidence --library /tmp/claude-0/library-checkout
       (final run with links, until BLOCK: 0)

The one required change: the `nb-note` "The claim, defined" prints Wei et al.'s
emergent-ability definition in quotation marks, but the wording is altered. The
primary (arXiv:2206.07682, as printed) reads: "We consider an ability to be
emergent if it is not present in smaller models but is present in larger models."
Open the paper, confirm the exact wording, and either quote it verbatim or
paraphrase it without quotation marks. Do not change any other settled work.
Preserve the editor's three direct edits. Rerun the full proof with links to
BLOCK: 0 and update draft-handoff.

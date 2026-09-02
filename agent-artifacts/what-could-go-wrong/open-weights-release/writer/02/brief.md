# writer brief: what-could-go-wrong/open-weights-release (02)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- the corrected evidence: ../../researcher/02/evidence.md (supersedes 01 on the
  Zuckerberg quote and the Seger/GovAI date)
- the editor review: ../../editor/01/editorial-review.md — apply its Required-work
  writer items
- the article (current state, carrying the editor's direct edits):
  ../../../../library/what-could-go-wrong/open-weights-release.html
- the prior handoff: ../01/draft-handoff.md
- template context under ../../../../.nb-context/

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check
  /home/user/the-nightly-build/.nb-work/what-could-go-wrong/open-weights-release/library/what-could-go-wrong/open-weights-release.html
  --series what-could-go-wrong --library /home/user/library-checkout
  (iterate with --no-check-links; run nb stamp then the full check, links included,
  until BLOCK: 0)

Apply exactly the editor's routed writer items, nothing more:

1. REQUIRED: Correct the Zuckerberg quotation. The draft prints a spliced quote
   ("larger institutions...check the power of smaller bad actors") that does not
   exist in the source. Use the corrected evidence: the primary's sentence (1) is
   verbatim "I think it will be better to live in a world where AI is widely
   deployed so that larger actors can check the power of smaller bad actors."
   Sentence (3), three sentences later, is a SEPARATE claim ("larger institutions
   deploying AI at scale will promote security and stability across society"). Do
   NOT splice them or swap their subjects. Quote only what the source actually
   says; keep the citation. If you quote, quote a single real sentence verbatim, or
   paraphrase faithfully and drop the quote marks.
2. OPTIONAL (welcome, not required): where the editor removed a wrong Seger
   publication month, you may restore the correct sourced date (GovAI report,
   October 2023) from the corrected evidence.

Preserve all settled work and the editor's direct edits. Do not expand the claim
set, reopen the CBRN handling, or touch anything else. Add no operational CBRN
content. Keep sources numbered in first-citation order with correct data-nb-kind.
Rerun the full proof to BLOCK: 0, run nb stamp, and do the display-text pass on any
sentence you touched. In draft-handoff.md, add one line per editor item resolved.

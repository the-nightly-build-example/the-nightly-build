# writer brief: the-evidence/constitutional-ai (02)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- the corrected evidence: ../../researcher/02/evidence.md (supersedes 01 on the
  TIME s6 attribution)
- the editor review: ../../editor/01/editorial-review.md — apply its Required-work
  writer item
- the article (current state, carrying the editor's direct edits):
  ../../../../library/the-evidence/constitutional-ai.html
- the prior handoff: ../01/draft-handoff.md
- template context under ../../../../.nb-context/

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check
  /home/user/the-nightly-build/.nb-work/the-evidence/constitutional-ai/library/the-evidence/constitutional-ai.html
  --series the-evidence --library /home/user/library-checkout
  (iterate with --no-check-links; run nb stamp then the full check, links included,
  until BLOCK: 0)

Apply exactly the editor's one routed writer item, nothing more:

- The present-day sentence attributes to Amanda Askell wording that TIME actually
  presents as the reporters' own narration (no quote marks, no Askell attribution).
  Reattribute it to the TIME reporting itself (source s6), keeping the wording and
  the citation, and drop the Askell attribution. Do not present it as quoted
  speech. If the sentence currently uses quotation marks around that phrasing,
  render it as reported description instead, per the corrected evidence.

Preserve all settled work and the editor's direct edits. Do not expand the claim
set or reopen anything else. Keep sources numbered in first-citation order with
correct data-nb-kind. Rerun the full proof to BLOCK: 0, run nb stamp, and do the
display-text pass on any sentence you touched. In draft-handoff.md, add one line
recording the editor item resolved.

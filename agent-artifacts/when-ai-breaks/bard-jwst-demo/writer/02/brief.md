# writer brief: when-ai-breaks/bard-jwst-demo (02)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- the corrected evidence: ../../researcher/02/evidence.md — use this as the current
  evidence record (supersedes 01 on the Paris-reception point)
- the editor review: ../../editor/01/editorial-review.md — apply its Required-work
  writer items
- the article (current state, already carrying the editor's direct edits):
  ../../../../library/when-ai-breaks/bard-jwst-demo.html
- the prior handoff: ../01/draft-handoff.md
- template context under ../../../../.nb-context/

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check
  /home/user/the-nightly-build/.nb-work/when-ai-breaks/bard-jwst-demo/library/when-ai-breaks/bard-jwst-demo.html
  --series when-ai-breaks --library /home/user/library-checkout
  (iterate with --no-check-links; run nb stamp then the full check, links included,
  until BLOCK: 0)

Apply exactly the editor's routed writer items, nothing more:

1. Remove the misattributed "failed to dazzle" quotation. Replace it with wording
   supported by the corrected evidence. The corrected source (Reuters via the Al
   Jazeera reprint) supports, as its lead sentence, that Alphabet lost market value
   after the ad's inaccurate answer AND "analysts said its AI search event lacked
   details on how it will answer Microsoft's ChatGPT challenge." Per the researcher:
   this is the reporter's own paraphrase of analysts, NOT a direct analyst
   quotation — do NOT present it as quoted speech; render it as a faithful sentence
   or a clearly-marked paraphrase.
2. Reground the two phrasings that leaned on the old quote: "a Google event that
   reporters called underwhelming" and the takeaway's "a flat product event in
   Paris." Bring both into line with what the corrected evidence actually supports
   (the "lacked details" characterization), or cut the characterization if the
   evidence does not support that adjective.
3. Recast the semicolon in that sentence to a period.

Preserve all settled work and the editor's direct edits. Do not expand the claim
set or re-open anything else. Keep sources numbered in first-citation order with
correct data-nb-kind. Rerun the full proof to BLOCK: 0, run nb stamp, and do the
display-text pass on any sentence you touched. In draft-handoff.md, add one line per
editor item resolved.

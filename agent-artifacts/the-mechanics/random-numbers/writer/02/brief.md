# writer brief: the-mechanics/random-numbers (02) — revision

Inputs:
- editorial-direction.md (house standard, the paper's voice, The Mechanics prompt)
- writing-coach/01/voice-guide.md (unchanged; how this piece should sound)
- researcher/02/evidence.md (the NEW evidence record; supersedes 01. Use it.)
- editor/01/editorial-review.md (apply every item in its Required work)
- writer/01/draft-handoff.md (your prior handoff, for continuity)
- library/the-mechanics/random-numbers.html (the article — it ALREADY carries the
  editor's own direct edits; edit it further, do not revert them or recreate it)
- .nb-context/ (effective template contract, runtime assets, furniture)

Output: writer/02/draft-handoff.md
Article: /home/user/the-nightly-build/.nb-work/the-mechanics/random-numbers/library/the-mechanics/random-numbers.html
Proof: ./nb check .nb-work/the-mechanics/random-numbers/library/the-mechanics/random-numbers.html --series the-mechanics --library /home/user/library-checkout

## Apply exactly the editor's Required work — nothing wider
The editor approved everything else; make only these changes and whatever each
logically forces.

1. The human-"69" claim. researcher/02 confirms: no peer-reviewed or otherwise
   verifiable-with-a-figure human source supports "humans over-pick 69" as a
   stated fact. The firmly-sourced half is the MODEL side (exmergo: gpt-4.1
   under-picks 69, 29 of 10,000, ~0.29x expected). Fix the article so no
   unsourced human-69 fact remains. Prefer the cleanest honest option:
   - either cut the 69 anomaly entirely and recast the "two findings" paragraph
     and the closing 69 reference around what still holds, or
   - keep the model-side under-pick as the established fact and present any human
     side ONLY as an explicitly hedged crowdsourced-survey observation (the
     r/dataisbeautiful n=6,750 poll in researcher/02), if it earns its place.
   Do not state a human 69 preference as fact, and do not lean the argument on an
   un-verifiable source. Keep the change minimal and local.

2. The quotation. Verify the Zhao/Du/Wang quotation the draft prints ("lack a
   functional internal mechanism for probabilistic sampling") against the actual
   published text — the editor flags the abstract reads "functional internal
   sampler". Retrieve the real source text and either quote it verbatim or
   rewrite the sentence in the article's own words. A misquotation ships a
   fabricated quote; get it exactly right or remove the quotation marks.

## Then
Preserve all settled work and the editor's edits. Do not expand the claim set
beyond researcher/02. Re-run the display-text self-test, then nb stamp and the
full proof with links until BLOCK: 0. Write writer/02/draft-handoff.md with one
line per editorial item resolved (which option you took on the 69 anomaly, and
how the quotation was resolved), the proof result, and any open question.

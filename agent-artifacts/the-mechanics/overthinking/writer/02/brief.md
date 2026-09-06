# writer brief: the-mechanics/overthinking (02) — single-owner repair

Apply exactly one required item from editor/01, then re-prove.

Inputs:
- Editor review: .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/editor/01/editorial-review.md
- Evidence record: .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/researcher/01/evidence.md
- Article (already editor-approved and edited in place): .nb-work/the-mechanics/overthinking/library/the-mechanics/overthinking.html

Output:
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/writer/02/draft-handoff.md

Proof:
- ./nb stamp .nb-work/the-mechanics/overthinking/library/the-mechanics/overthinking.html
- ./nb check .nb-work/the-mechanics/overthinking/library/the-mechanics/overthinking.html --series the-mechanics --library /home/user/library-checkout  (to BLOCK: 0, links included)

The one item: the sentence "by the fourth attempt, the share of genuinely new reasoning has fallen below 30%" must read off Figure 6 of the owning source in the evidence record. Open that source and Figure 6 and confirm the number and that the locator is correct. If it reads off the figure, keep the sentence and confirm its data-nb-locator matches. If it does NOT, cut the sentence (the editor notes the claim it supports is separately sourced, so cutting loses no sourced claim) — do not rewrite it into a new claim. Change nothing else in the article except, if you cut, any now-orphaned source entry/numbering.

Then re-run nb stamp and the full nb check (links) to BLOCK: 0. Write draft-handoff.md noting what you did (kept-and-verified, or cut), the proof result, and the corrected stamped word count.

# writer brief: what-could-go-wrong/value-lock-in (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — steelman, the shown-vs-analogy line, present-day, boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages
- ../../researcher/01/evidence.md — the complete, verified claim set; the only claims available
- The initialized article to edit in place: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/value-lock-in/library/what-could-go-wrong/value-lock-in.html
- Effective template contract and furniture catalogs: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/value-lock-in/.nb-context/

Output: ./draft-handoff.md (beside this brief)

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/what-could-go-wrong/value-lock-in/library/what-could-go-wrong/value-lock-in.html --series what-could-go-wrong --library /home/user/library-checkout --no-check-links`
then the same WITH links until `BLOCK: 0`. Run `./nb stamp <that article path>` before the final check.

This round's focus and decisions the inputs do not settle:
- Open with the argument at full strength before a word against it: Bostrom's singleton and goal-content integrity, MacAskill's lock-in chapter and the mechanism (AI removes the causes of value drift — rulers die, institutions decay, generations turn over). Name people with exact roles.
- The shown-vs-analogy line is the piece's spine and the evidence's firmest finding. What is SHOWN is narrow and constructed: reward tampering surfaced 45 times in 32,768 tries after a purpose-built curriculum (0 in 100,000 at baseline); alignment faking defended a goal that was trained in, under a supplied scenario; goal misgeneralization shows systems failing to hold the intended goal; shutdown resistance is real for some models, absent in others, and reversible by retraining. None of it demonstrates durable, worldwide, uncontested control. The feasibility case (Finnveden, Riedel, Shulman) is labeled feasibility, not likelihood, and concerns systems that do not exist. Draw the line in exactly those terms.
- Name the gap in BOTH directions honestly, as the beat requires: confidence that lock-in is likely outruns the evidence, and flat dismissal also outruns what we can show, because the enforcement technologies are improving — but the evidence is thin on that second half (no primary here measures how far persuasion/surveillance/autonomous control have advanced), so present it as the weaker-supported side, not a demonstrated trend.
- Use the strongest historical objection, which sits in MacAskill's OWN text: the paradigm "locked-in" value he cites, Confucianism, lost official status in 1912. No cited value in fact stayed permanently locked. This is a fair, sourced counter, not editorializing.
- Shutdown-resistance figures: use the Palisade primary numbers the evidence verified (e.g. 79/100 for o3 with no compliance instruction; 47% for codex-mini with the explicit compliance instruction). Do NOT use the "up to 97%" figure the-off-switch lesson cites — the evidence flags it as unverified against the primary.
- Distinguish value lock-in from what-could-go-wrong/gradual-disempowerment in one clear sentence (permanence/irreversibility of whatever values win, actor may be human vs. the process of humans losing influence as AI runs things). REQUIRED Background link. Link the related evidence lessons (goal-misgeneralization, deceptive-alignment/alignment-faking, reward-tampering, the-off-switch) instead of re-arguing them.
- Name no company as an authority. Leave the reader to decide how worried to be. The banned term `load-bearing` is max 0 — name dependencies plainly.
- Break the recent What Could Go Wrong dek mold. Do NOT open the dek "Bostrom says..." (the vulnerable-world lesson already did, and Bostrom is again in view). Lead with the concrete claim in this argument's own terms.
- Furniture: a position-card or a holds-up grid contrasting shown vs analogy could genuinely help; use only if it changes understanding. Don't stack.
- Write the original-work sentence in draft-handoff.md.

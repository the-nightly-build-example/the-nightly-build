# writer brief: what-could-go-wrong/data-poisoning (02) — revision

Apply every required item in the editor's round-01 review, then re-prove. Inputs:
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/editor/01/editorial-review.md — the review to apply (it supplies the exact correct titles and the verbatim Fortune quote)
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/researcher/01/evidence.md — the claim set (do not expand it)
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writing-coach/01/voice-guide.md — unchanged craft standard
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writer/01/brief.md — the round-01 brief (unchanged commission constraints, incl. the does-not-compose spine)
- .nb-work/what-could-go-wrong/data-poisoning/library/what-could-go-wrong/data-poisoning.html — the article to edit in place
- .nb-work/what-could-go-wrong/data-poisoning/.nb-context/ — template context

Required (blocking), all from the editor's review:
1. Remove the body-closing "Verdict" `nb-note-strong` block from the
   why-they-dont-combine section. Press direction forbids closing the body with a
   Verdict note or any block restating the finding; the takeaway bookend already
   lands this judgment. Do not replace it with another summarizing block — let the
   section end on its argument. (This frees words; you are near the 2200 ceiling.)
2. Fix the s5 (OATML) and s8 (Fortune) source titles to the verbatim published
   titles the review supplies.
3. Restore the Mavroudis quote to the verbatim Fortune wording the review supplies
   (it currently drops an "it" and "for example," inside the quotation marks).

Preserve all settled work and the does-not-compose discipline. Do not expand the
claim set.

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/what-could-go-wrong/data-poisoning/library/what-could-go-wrong/data-poisoning.html --series what-could-go-wrong --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same WITHOUT `--no-check-links` until `BLOCK: 0`. In
writer/02/draft-handoff.md, add one line per required item resolved.

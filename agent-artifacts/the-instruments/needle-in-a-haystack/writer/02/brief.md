# writer brief: the-instruments/needle-in-a-haystack (02) — revision

Apply the required work in the editor's review, then re-prove. Inputs:
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/editor/01/editorial-review.md — the review to apply (Required work + Reader/Skeptic notes)
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/researcher/01/evidence.md — the claim set (do not expand it)
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writing-coach/01/voice-guide.md — unchanged craft standard
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writer/01/brief.md — the round-01 brief (unchanged commission constraints)
- .nb-work/the-instruments/needle-in-a-haystack/library/the-instruments/needle-in-a-haystack.html — the article to edit in place
- .nb-work/the-instruments/needle-in-a-haystack/.nb-context/ — template context

Output: .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writer/02/draft-handoff.md

Required (blocking): the orientation prints a quotation-marked question cited to
source #2 (Arize) that matches NO cited source. Fix it so the quoted string is
exactly what its cited source says. Arize's needle question is "What is the best
thing to do in San Francisco?"; the Anthropic post's prompt (your asset-1 / source
#8) is the longer "...most fun thing to do in San Francisco based on the context?
Don't give information outside the document or repeat your findings." Either quote
the Arize wording and cite Arize, or quote the Anthropic wording and cite the
Anthropic post, and reconcile the sentence with Fig. 1 so the printed question and
the figure agree. Do not introduce any string that is not verbatim in the source it
cites. The needle sentence itself is already correct — leave it.

Non-blocking polish (apply if it does not cost clarity or words; the piece is near
the 2200 ceiling): the two "One..." headings and the misreadable "Each of those
steps" line the editor flagged.

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/the-instruments/needle-in-a-haystack/library/the-instruments/needle-in-a-haystack.html --series the-instruments --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same WITHOUT `--no-check-links` until `BLOCK: 0`. In
draft-handoff, add one line per required item resolved. Do not expand the claim set
or touch settled work.

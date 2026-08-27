# editor review-brief: what-could-go-wrong/fragility-of-value (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, series prompt
- ../../commission.md — the assignment, its angle, boundaries, and the reader's situation
- ../../writer/01/brief.md — the exact writer brief, so a leak is visible against it
- ../../writing-coach/01/voice-guide.md — how the piece should sound, with the exemplar passages the writer read
- ../../researcher/01/evidence.md — the evidence record to test claims against
- ../../writer/01/draft-handoff.md — the writer's original-work sentence and any warnings left
- article to edit: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/fragility-of-value/library/what-could-go-wrong/fragility-of-value.html
- template context: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/fragility-of-value/.nb-context

Output: editorial-review.md (this directory)

Proof (after your edits, the orchestrator stamps): ./nb check /home/user/the-nightly-build/.nb-work/what-could-go-wrong/fragility-of-value/library/what-could-go-wrong/fragility-of-value.html --series what-could-go-wrong --library /home/user/library-checkout

Recent-pattern notes (compare edges, headings, dek, furniture against these):
- The two-clause dek joined by "and"/"but" is the house default, and the three
  dek molds in `spec/headlines.md` recur. Check this dek against them.
- The desk keeps closing on a "Who makes the case now" section, and recent
  safety pieces lean on a "shown result vs projection" spine. Flag a stamped
  present-day heading or a dek/heading echo of the neighboring pieces.

This round's focus: two correctness traps. First, the piece must not present
RLHF or GPT-4's value fluency as a clean refutation of the fragility claim; it
should name the identification-versus-motivation distinction (Barnett's critique
lands on value identification, Yudkowsky's rebuttal keeps value motivation
standing). Confirm the article names that trap rather than falling into it.
Second, a citation-integrity call the writer flagged: source s4 attributes the
idea to Bostrom's *Superintelligence*, but the researcher could only read
secondary reproductions, not the book, and the article only paraphrases (no
verbatim Bostrom quote). Judge s4 against "cite only what you have read": either
confirm the book citation is acceptable as the idea's owner because the href
resolves to the book and nothing is quoted from it, or have the secondary
reproduction the researcher actually read added alongside. Route to the writer or
researcher only if the fix needs reporting you do not have.

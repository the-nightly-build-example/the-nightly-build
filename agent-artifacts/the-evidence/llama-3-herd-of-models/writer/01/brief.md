# writer brief: the-evidence/llama-3-herd-of-models (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, series prompt, template rules
- ../../commission.md — subject, angle, boundaries, required contribution
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting
- ../../researcher/01/evidence.md — the complete, only set of claims available to you
- ../../../../library/the-evidence/llama-3-herd-of-models.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract and runtime assets

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-evidence/llama-3-herd-of-models/library/the-evidence/llama-3-herd-of-models.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/643ba5c9-25c5-59fc-9937-7e74191ccd45/scratchpad/library-checkout
(run with --no-check-links while iterating; run the exact command above, links on, until BLOCK: 0 before handoff)

This round's focus — precision the evidence record flags and the article must get exactly right (do not soften, do not overstate):
- The report is titled "Llama 3" but its results and the 405B release are Llama 3.1. Name this precisely rather than blurring it.
- Frame the license accurately: "open weights under a conditional community license" (weights and code, not training data; conditions apply). "Open source" is Meta's label and the OSI rejects it — report that as the contest it is; do not adopt either side's label as plain fact.
- Do not overstate the license restrictions: the Llama 3.1 license requires renaming derived models, it does not ban using outputs to train competing models (that was Llama 2).
- The contamination table (Table 15) leaving four headline benchmarks blank is the sharpest instance of the angle (disclosure and non-verifiability in one place); it is available to you if the argument spends it.

Recent-pattern habits in this series to break (from the recent library; vary construction, do not clone):
- Openers that lead with a striking number or a "do X and it gets worse" reversal (recent pieces opened "Feed a network 4.5 times...", "One gradient step still fools..."). Find this piece's own way in.
- Deks built as a comma-triad or ending on "a claim later work disputes / corrects." spec/headlines.md bans those dek molds; check yours against it.
- Do NOT reuse the closing "How much of this survived" heading or a "does it still hold" closer with an nb-holdsup block — that is last article's shape (deep-double-descent, 2026-09-04).
- Section headings recently ran to "The X the textbook drew" / "Where more data made the model worse"; write yours in this document's own nouns and vary how they are built.

# editor review-brief: the-evidence/mamba (editor/01)

Inputs:
- ../../editorial-direction.md — the standard to edit against
- ../../commission.md — the assignment, the desk's arc, the boundaries
- ../../writer/01/brief.md — the exact writer brief (check the draft against it for leakage and carried decisions)
- ../../writing-coach/01/voice-guide.md — read first; register and exemplar passages to check borrowed phrasing against
- ../../researcher/01/evidence.md — the claim set; reread cited passages for what breaks a claim
- ../../writer/01/draft-handoff.md — the original-work sentence (open on the third read) and the writer's open note
- the article: /home/user/the-nightly-build/.nb-work/the-evidence/mamba/library/the-evidence/mamba.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/mamba/.nb-context/

Output: editorial-review.md (in this directory)

Round's focus (things to check hardest for this piece):
- Scale honesty: confirm the piece is honest that Mamba's headline results were at small-to-mid model sizes, and that Falcon Mamba (a pure 7B state-space model beating some size-matched transformers on short-context leaderboards) is presented as a genuine counter-current, not a strawman.
- The copying/in-context-retrieval gap: the sharpest primary ("Repeat After Me") tests the original Mamba; the Mamba-2/hybrid case is more indirect. Confirm the draft does not claim the gap is proven at frontier scale, and weighs the contradiction.
- Attention must be linked (Background), not re-taught. State, recurrence, and perplexity defined in plain words on the spot.
- The mechanism is taught with a small nb-math equation (KaTeX is a documented site capability, so this is allowed). Check the equation is accurate and that its prose is understandable to a no-code reader; the equation is apparatus, not a claim.
- Writer's open note: no source asset was captured (the "Repeat After Me" figure). If you judge a visual is required for the reader to test the copying-gap claim, route a precise request to the writer (with the tooling); otherwise record that prose carries it.

Recent-pattern notes (compare edges, headings, dek against the recent Evidence record):
- Openers that name authors and year ("X et al.'s 2023 paper...") and deks built as "A [noun], whose [twist]" or comma-clause chains recur across the desk; flag any echo as formula.
- Section headings must be this document's own steps, never stock labels.

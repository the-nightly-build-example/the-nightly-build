# editor review-brief: the-mechanics/familiar-pattern-override (01)

Inputs (read the voice guide first; evidence on the first read, the draft-handoff
original-work sentence on the third):
- ../../editorial-direction.md — house standard, voice, series prompt, template identity.
- ../../commission.md — the assignment (note: the writer brief corrected two of its claims).
- ../../writer/01/brief.md — the exact writer brief, including the corrections to the commission.
- ../../writing-coach/01/voice-guide.md — how this piece should sound.
- ../../researcher/01/evidence.md — the evidence record.
- ../../writer/01/draft-handoff.md — original-work sentence and proof result.
- article: /home/user/the-nightly-build/.nb-work/the-mechanics/familiar-pattern-override/library/the-mechanics/familiar-pattern-override.html
- template context: /home/user/the-nightly-build/.nb-work/the-mechanics/familiar-pattern-override/.nb-context/

Output: ./editorial-review.md   (decision: approve | revise)

Round focus and specific checks:
- The piece is 2199 words against a 1200-2200 band — at the ceiling. Trim, do not
  expand; if your cuts are substantial, good. Do not push it over 2200.
- Verify the mechanism is not overclaimed: the "fades on obscure puzzles" idea must
  read as an inference from frequency-effect research (Razeghi, McCoy), not a
  measured puzzle-specific result. Confirm the piece frames it that way or drops it.
- Verify the open-question beat is honest: reasoning training does NOT cleanly fix
  this (Jang's reasoning-trained model overrides a stated condition more than its
  base). Cite Jang's worked examples, not its unextractable Tables 2-3.
- Verify the compression: Wu et al.'s coordinate figures given as "between 62% and
  75%" against the evidence Numbers section.
- Confirm distinctness from the linked neighbours: irrelevant-context (added
  distractor), memorization (verbatim recall), prompt-sensitivity (rephrasing).
  The piece must not blur into them.

Recent-pattern notes (Mechanics habits — flag any that recur; no single article
shows a formula):
- Openers on a "By the end you will know..." triad; temporal-generic first sentence.
- Two-part-balance takeaway closers.
- Over-used Mechanics heading molds: "A [problem] the model solves until you change
  it", "Nothing tells the model which words to ignore", a stock ground-hitting final
  heading ("The floor beneath the failure"), and a stock reasoning-boundary closer
  ("Where this leaves the reasoning question", "The honest edge of the explanation").
  The desk requires marking the open question — but its heading must be in this
  behaviour's own nouns. Flag any default to nb-holdsup.
- Deks on a comma splice or comma triad (banned in `spec/headlines.md`).

Hold the bookends to the lesson template (written after the body, this lesson's
particulars only, no Verdict-style closer). If you approve after direct cuts, note
the orchestrator must re-stamp and re-check before the PR.

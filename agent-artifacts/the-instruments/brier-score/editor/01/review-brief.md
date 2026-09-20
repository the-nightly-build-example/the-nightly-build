# editor review-brief: the-instruments/brier-score (01)

Inputs (voice guide first; evidence on the first read, draft-handoff original-work
sentence on the third):
- ../../editorial-direction.md — house standard, voice, series prompt, template identity.
- ../../commission.md — the assignment.
- ../../writer/01/brief.md — the exact writer brief, including source caveats and the second trap.
- ../../writing-coach/01/voice-guide.md — how this piece should sound.
- ../../researcher/01/evidence.md — the evidence record.
- ../../writer/01/draft-handoff.md — original-work sentence and proof result.
- article: /home/user/the-nightly-build/.nb-work/the-instruments/brier-score/library/the-instruments/brier-score.html
- template context: /home/user/the-nightly-build/.nb-work/the-instruments/brier-score/.nb-context/

Output: ./editorial-review.md   (decision: approve | revise)

Round focus and specific checks:
- The piece is 2194 words against a 1200-2200 band — near the ceiling. Trim, do not
  expand; do not push it over 2200.
- Recompute the worked numbers yourself: the tiny Brier example, the always-0.5 =
  0.25 baseline, and the two-scale before/after (0.18 vs 0.09) on Good Judgment
  Open's own 70-percent example. Confirm the halving is stated as a convention
  difference (two-term 0-to-2 vs one-term 0-to-1), not a change in forecast skill.
- Verify the base-rate trap is explained via Murphy's uncertainty term and holds up
  as an event gets rarer, grounded in the record (Murphy sourced via Ferro &
  Fricker 2012, not the gated original).
- Confirm the second comparability trap stays contained to one section and does not
  overwhelm the lesson (a sharp second trap, not a catalogue).
- Confirm it contrasts by link with calibration-error (ECE) and auroc rather than
  re-teaching them.

Recent-pattern notes (Instruments habits — flag any that recur):
- Openers on a "By the end you will know..." triad; temporal-generic first sentence.
- Two-part-balance takeaway closers.
- Over-used heading molds: "How a X becomes a Y", "Turning a X into one number",
  a "Reading X as Y" closer, and the nb-holdsup pairing.
- Deks on a comma splice or comma triad (banned in `spec/headlines.md`).

Hold the bookends to the lesson template (written after the body, this lesson's
particulars only, no Verdict-style closer). If you approve after direct cuts, note
the orchestrator must re-stamp and re-check before the PR.

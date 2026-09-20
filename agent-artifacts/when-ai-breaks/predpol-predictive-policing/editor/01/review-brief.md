# editor review-brief: when-ai-breaks/predpol-predictive-policing (01)

Inputs (voice guide first; evidence on the first read, draft-handoff original-work
sentence on the third):
- ../../editorial-direction.md — house standard, voice, series prompt, template identity.
- ../../commission.md — the assignment (note: the writer brief corrected three of its points).
- ../../writer/01/brief.md — the exact writer brief, including the three corrections.
- ../../writing-coach/01/voice-guide.md — how this piece should sound.
- ../../researcher/01/evidence.md — the evidence record.
- ../../writer/01/draft-handoff.md — original-work sentence and proof result.
- article: /home/user/the-nightly-build/.nb-work/when-ai-breaks/predpol-predictive-policing/library/when-ai-breaks/predpol-predictive-policing.html
- template context: /home/user/the-nightly-build/.nb-work/when-ai-breaks/predpol-predictive-policing/.nb-context/

Output: ./editorial-review.md   (decision: approve | revise)

Round focus and specific checks:
- PRIORITY: the article is 2388 words against a 1200-2200 band (a W-LENGTH-HIGH
  warning; the series is non-strict so it does not BLOCK, but it is over band).
  Trim it to 2200 or under by cutting from middles — remove redundancy and any
  sentence that repeats a fact or reasoning step already made. Do not drop any of
  the three corrections below, and do not thin the mechanism. Trimming ~190+ words
  of a piece already cut from 3082 is the main job.
- Verify the three corrections held: (a) the vendor-response asymmetry is stated
  honestly (Geolitica did not answer the accuracy critique; it answered a different,
  racial-bias critique; a co-designer defended the field trials generally) — no
  manufactured rebuttal; (b) the 7.4% field-trial figure is attributed as reported
  via the triangulating sources (founders' 2018 paper + LAPD OIG), not as
  independently verified; (c) no false-precise Santa Cruz ban date.
- Verify the mechanism is the teaching core and honest: recorded crime vs. actual
  crime; the feedback loop (Lum & Isaac; Ensign et al.); rare-event base rates —
  and that it explains how the tool can be near-random AND racially skewed at once.
- Confirm distinctness from the linked neighbours — chicago-heat-list (person-based),
  shotspotter (acoustic), compas (sentencing) — links, not retellings.
- Register: keep it sober and factual on a charged subject; harm shown by the record.

Recent-pattern notes (When AI Breaks habits — flag any that recur):
- Openers on a "By the end you will know..." triad; temporal-generic first sentence.
- Two-part-balance takeaway closers.
- Over-used molds: "How a X becomes a Y", "Why an alert rarely means...", and a
  stock "where it lives now" closing heading. The "where the trap lives today"
  section must be in this incident's own nouns.
- Deks on a comma triad or semicolon reversal (banned in `spec/headlines.md`).

Hold the bookends to the lesson template (written after the body, this incident's
particulars only, no Verdict-style closer). Re-run `./nb check` locally after your
edits; if you approve after direct cuts, note the orchestrator must re-stamp and
re-check before the PR.

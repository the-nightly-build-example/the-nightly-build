# writer brief: the-instruments/gaia (01)

Inputs:
  ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
  ../../commission.md — the measurement, what to teach, distinctness lines, recent-pattern habits
  ../../writing-coach/01/voice-guide.md — how this lesson should sound; read before drafting
  ../../researcher/01/evidence.md — the complete claim set available to you
  ../../../../library/the-instruments/gaia.html — the initialized article to edit in place
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/gaia/library/the-instruments/gaia.html --series the-instruments --library /tmp/claude-0/library-checkout
       (iterate with --no-check-links; final run with links, until BLOCK: 0)

This round's focus:
- The misleading case is the spine of the "what the number cannot support"
  section: OpenAI's Deep Research "67.36% state of the art on GAIA" (2 Feb 2025)
  was a validation-set figure read as a leaderboard result, and the validation
  answers are public and known to leak. The concrete cost is a cross-set
  comparison that does not hold (H2O.ai's test-set 75% vs. others' validation
  numbers; JoyAgent 75.2 validation / 67.1 test). Keep validation vs. test, and
  overall vs. per-level, from blurring — the voice guide names this as the craft
  to hold.
- Number honesty from the evidence record: 466 questions (146/245/75), quasi-
  exact-match against one reference, 166 released / 300 withheld, human 92% vs.
  GPT-4+plugins 15% at release. Two caveats to respect: live leaderboard
  standings could not be verified against a source, so anchor any recent number
  to the dated primary report that owns it, not a live ranking; and the paper's
  per-level baseline denominator (all 466 vs. the 166 dev set) is not firm — do
  not state a per-level human/model split at a precision the record does not
  support.
- Distinctness: differentiate GAIA from swe-bench, tau-bench, and task-time-
  horizon in a line each and link, do not re-teach them. If the misleading case
  is contamination, link the prior contamination treatment rather than re-teaching
  it.
- Break the desk's recent number-forward-headline and comma-conjunction dek habit
  noted in the commission.

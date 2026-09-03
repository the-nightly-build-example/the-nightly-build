# writer brief: the-mechanics/option-order-bias (01)

Inputs:
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/editorial-direction.md — house standard, paper voice, lesson template, series direction
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/researcher/01/evidence.md — the complete claim set; not prose
  - .nb-work/the-mechanics/option-order-bias/library/the-mechanics/option-order-bias.html — the initialized article to edit in place
  - .nb-work/the-mechanics/option-order-bias/.nb-context/ — effective template contract, furniture catalogs, runtime assets

Output: .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/option-order-bias/library/the-mechanics/option-order-bias.html --series the-mechanics --library /home/user/library-checkout
       (iterate with --no-check-links; run the full command, links included, to BLOCK: 0 before handoff)

This round's focus:
- The "settled vs open" reckoning is the heart of this mechanics piece, and the
  evidence hands you a real one: the effect is robustly measured (Zheng: up to
  +15/-12 accuracy points from moving one answer; Pezeshkpour: a 13-75% best-worst
  gap), but the two headline papers CONTRADICT on which mechanism dominates —
  Zheng argues token bias and explicitly against Pezeshkpour's position-bias view.
  Do NOT present one mechanism as the sole cause. Walk the candidate causes,
  attribute each, and mark the split as openly disputed.
- Honesty point to teach: part of the measured "token bias" is a scoring artifact
  — the first-token/option-ID probe disagrees with the model's actual generated
  answer more than half the time on some models. That is a real step in the
  mechanism (how the answer is scored), not a footnote.
- Do not over-quote figures the record flags as fetch-read/for re-check; use the
  robust headline numbers and follow the editorial direction's Numbers rules.
- Reach ground and stop. Teach only the terms the reader needs. prompt-sensitivity
  is a published sibling lesson — link it, do not re-teach it; this piece is about
  positional/label bias among presented options.

## Recent shapes to break
Habits across the recent library and this five-lesson edition. Break them; do not
inherit them and do not copy any prior article's structure to avoid them.
- Dek molds: the "credited with X, but Y had already done it" reversal and the
  "the [term] now used far more loosely" tag recur; also banned by
  spec/headlines.md are the semicolon reversal, the suspended question, and the
  comma triad. Write a dek stating this piece's own particular.
- Why-this-matters bookend: vary from "This lesson opens/reads ..." and the "By
  the end you will be able to explain X, Y and Z" list formula; resolve it in the
  takeaway on this lesson's own particulars.
- The mechanics desk defaults to a short declarative "reveal" first heading
  ("The cheaper copy answers worse"); do not make it the reflex. Vary heading
  construction across the piece, in the piece's own nouns; do not close the last
  body section on a stamped present-tense one-liner.
- Edition coherence: four sibling lessons ship tonight (mixture-of-experts,
  task-time-horizon, algorithmic-collusion, clearview-ai). This is the only pure-
  mechanism piece. It may note in ONE line why this matters for benchmark scores,
  but the instruments desk owns metrics — do not drift into metric design.

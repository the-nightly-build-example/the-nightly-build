# writer brief: the-instruments/task-time-horizon (01)

Inputs:
  - .nb-work/the-instruments/task-time-horizon/agent-artifacts/the-instruments/task-time-horizon/editorial-direction.md — house standard, paper voice, lesson template, series direction
  - .nb-work/the-instruments/task-time-horizon/agent-artifacts/the-instruments/task-time-horizon/writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
  - .nb-work/the-instruments/task-time-horizon/agent-artifacts/the-instruments/task-time-horizon/researcher/01/evidence.md — the complete claim set; not prose
  - .nb-work/the-instruments/task-time-horizon/library/the-instruments/task-time-horizon.html — the initialized article to edit in place
  - .nb-work/the-instruments/task-time-horizon/.nb-context/ — effective template contract, furniture catalogs, runtime assets

Output: .nb-work/the-instruments/task-time-horizon/agent-artifacts/the-instruments/task-time-horizon/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/task-time-horizon/library/the-instruments/task-time-horizon.html --series the-instruments --library /home/user/library-checkout
       (iterate with --no-check-links; run the full command, links included, to BLOCK: 0 before handoff)

This round's focus:
- Build the number in front of the reader: 170 timed tasks, binary scoring, a
  logistic fit of success vs log human-time, horizon read where success crosses
  50%. Headline figures: Claude 3.7 Sonnet ~59 min; ~212-day doubling (95% CI
  171-249). Use the figures the record verified; per-model horizon values that the
  record marks approximate (Figure 1 client-rendered) should not be quoted to
  false precision.
- Two honesty points the record makes central: (1) the paper was retitled to
  "Long *Software* Tasks" — the metric is validated on software/ML/cyber work, not
  general knowledge work, so "AI can do X-hour tasks" overreaches the domain; (2)
  the over-read is partly seeded by the authors' OWN "within five years... a
  month" projection, then amplified downstream (AI Digest's "new Moore's Law").
  Do not frame the misread as purely an outside error.
- Give the skeptic real weight: Toby Ord's constant-hazard / half-life reframing
  is a primary critique. The ~7-month full-period doubling is settled; the
  2024-2025 acceleration is contested, including by METR's own later update.
- This is the "one real case where the number misled people" the series requires —
  make the gap between the 50% construction and the timeline headline concrete.
- Keep primary (METR paper/blog, Ord) distinct from secondary reporting.

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
- Vary heading construction across the piece, in the piece's own nouns; do not
  default to a single short "reveal" heading mold, and do not close the last body
  section on a stamped present-tense one-liner.
- Edition coherence: four sibling lessons ship tonight (mixture-of-experts,
  option-order-bias, algorithmic-collusion, clearview-ai). No topical overlap;
  keep this on how the horizon number is built and misread.

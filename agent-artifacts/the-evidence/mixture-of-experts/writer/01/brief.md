# writer brief: the-evidence/mixture-of-experts (01)

Inputs:
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/editorial-direction.md — house standard, paper voice, lesson template, series direction
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/researcher/01/evidence.md — the complete claim set; not prose
  - .nb-work/the-evidence/mixture-of-experts/library/the-evidence/mixture-of-experts.html — the initialized article to edit in place
  - .nb-work/the-evidence/mixture-of-experts/.nb-context/ — effective template contract, furniture catalogs, runtime assets

Output: .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/mixture-of-experts/library/the-evidence/mixture-of-experts.html --series the-evidence --library /home/user/library-checkout
       (iterate with --no-check-links; run the full command, links included, to BLOCK: 0 before handoff)

This round's focus:
- The spine is the total-vs-active parameter honesty angle, and the evidence
  supports it from the primaries' own framing (e.g. Switch-C's 1.571T params but
  890B FLOPs/seq, below dense T5-XXL). Show what "N-billion-parameter" counts vs
  what runs per token, without contempt for anyone who cites the bigger number.
- Acknowledge the real disagreement in the record: Shazeer's flat MoE uses top-k
  (k=4) while Switch Transformer uses top-1 routing — a genuine difference between
  primaries, not an error to smooth over.
- Do not over-quote figures the record flags unverified: GShard's BLEU numbers are
  a single-table reading — treat as approximate/flagged; Mixtral's 47B/13B is the
  paper's rounding of 46.7B/12.9B. Follow the editorial direction's Numbers rules.
- Teach only the architecture terms the reader needs (router/gating, expert,
  sparse vs dense, active vs total parameters) in plain words at first use.
  Transformers/attention were taught elsewhere — link, do not re-teach.

## Recent shapes to break
Habits across the recent library and this five-lesson edition. Break them; do not
inherit them and do not copy any prior article's structure to avoid them.
- Dek molds: the "credited with X, but Y had already done it" reversal and the
  "the [term] now used far more loosely" tag recur (constitutional-ai used the
  latter); also banned by spec/headlines.md are the semicolon reversal, the
  suspended question, and the comma triad. Write a dek stating this piece's own
  particular.
- Why-this-matters bookend: vary from "This lesson opens/reads ..." and the "By
  the end you will be able to explain X, Y and Z" list formula; resolve it in the
  takeaway on this lesson's own particulars.
- Vary heading construction across the piece, in the piece's own nouns; do not
  default to a single short "reveal" heading mold, and do not close the last body
  section on a stamped present-tense one-liner.
- Edition coherence: four sibling lessons ship tonight (task-time-horizon,
  option-order-bias, algorithmic-collusion, clearview-ai). No topical overlap;
  keep this on the MoE document and its parameter-count honesty.

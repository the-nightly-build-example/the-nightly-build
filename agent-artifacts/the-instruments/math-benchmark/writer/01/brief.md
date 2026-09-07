# writer brief: the-instruments/math-benchmark (01)

Inputs:
- `editorial-direction.md` — house standard, this paper's voice, the series direction
- `writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting
- `researcher/01/evidence.md` — the complete set of claims available to you
- the initialized article at
  `.nb-work/the-instruments/math-benchmark/library/the-instruments/math-benchmark.html`
- the effective template context under
  `.nb-work/the-instruments/math-benchmark/.nb-context/`

Output: `writer/01/draft-handoff.md`

Proof (run from `/home/user/the-nightly-build`; iterate with `--no-check-links`,
then a final run with links until `BLOCK: 0`):

```text
./nb stamp .nb-work/the-instruments/math-benchmark/library/the-instruments/math-benchmark.html
./nb check .nb-work/the-instruments/math-benchmark/library/the-instruments/math-benchmark.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/7638a680-eec9-5b00-bc28-2a2eeb252ef4/scratchpad/library-checkout
```

nb-meta to fill: date `2026-09-07`, harness `Claude Code`, model `claude-opus-4-8`,
and subject tags of your choosing. Keep nb-meta `dek` identical to the rendered
dekline.

This round's focus: teach how the MATH number is made, then land the sharpest
documented "misled" case honestly. The evidence record's constraints, which the
piece must respect:

- The rise from about 7% to about 97% is not all artifact. A three-time IMO gold
  medalist scored about 90%, and better grading moved Minerva only about a point,
  so real capability gains sit beside contamination and loose grading. Do not
  write a one-directional "the score is inflated" story.
- Grading error runs both ways: exact-match understates on formatting and
  overstates on right-answer/wrong-reasoning. Say both.
- The cleanest owned "misled" case is the subset-and-name confusion: leading labs
  now report "MATH-500" (500 problems, Pass@1) while the original paper and Minerva
  reported "MATH" (5,000 problems), so cross-model "MATH" comparisons silently mix
  denominators and metrics. MATH-500 exists because 4,500 of the 5,000 test
  problems had gone into PRM800K training. Use this as the spine.
- Do not borrow the 10-20% contamination inflation figure for MATH: that number
  belongs to AIME 2024, not MATH. Contamination of the MATH test set specifically
  is shown by the PRM800K leakage and the DMCA takedown, not by a percentage.

Recent shapes to break (checked against the last eight lessons in this series):

- Do not open the dek on a quoted score in scare quotes ("A model's 'X% MATH
  score' was...", simpleqa). Do not reuse "the grader is part of the number" or
  "turns one X into two measurements" (imo-gold, calibration-error), or "A single
  <score/attack> branded <model> <label>" (attack-success-rate).

Link rather than re-teach: the-instruments/gsm8k, the-instruments/frontiermath,
the-instruments/livecodebench (contamination), and chain-of-thought if used.
Background links use a relative `../<series>/<slug>.html` href; Go deeper links
point beyond the paper.

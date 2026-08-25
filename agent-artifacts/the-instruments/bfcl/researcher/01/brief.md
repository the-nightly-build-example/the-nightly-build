# researcher brief: the-instruments/bfcl (01)

Inputs:
- commission.md (at the artifact root): the angle, the scoring mechanics to
  pin down, the "misled people" candidates, boundaries, and source floor.
- editorial-direction.md (at the artifact root): citation standard,
  primary/secondary test, reader, the-instruments series territory.

Output: agent-artifacts/the-instruments/bfcl/researcher/01/evidence.md

This round's focus:
- Pin BFCL's scoring from the Gorilla team's own pages/code: what AST matching
  checks (function name, argument values, types), what executable evaluation
  runs, and how the relevance/irrelevance category is scored. Record the
  category breakdown and dataset sizes for the versions that matter (v1, the
  "live" v2, the multi-turn v3), with exact counts and dates.
- Establish what changed between versions and why: documented label errors,
  contamination, or category fixes, and any score movements the team reported.
- Nail the reliability contrast: a documented case where a strong single-call
  or leaderboard score did not carry to multi-step agent reliability. The
  τ-bench pass^k collapse (already covered by the paper) is one anchor; verify
  its figures from the τ-bench paper. Find the strongest such case with a real
  cost and record it fully.
- Get current/representative BFCL numbers for at least one or two named models
  so the reader has a concrete score to hold, with the version and date.
- Hunt for what breaks the angle: evidence that BFCL does predict real agent
  performance well, or that its multi-turn category closes the gap. Record in
  Contradictions.

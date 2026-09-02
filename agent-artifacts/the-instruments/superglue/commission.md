# Commission: the-instruments/superglue

## The measurement

The SuperGLUE score: the single aggregate number that ranked natural-language-
understanding models on the SuperGLUE leaderboard (Wang et al., 2019, arXiv
1905.00537). One number per model, averaged across eight tasks, sitting on a
leaderboard beside a "human baseline" row. The lesson teaches where that number
comes from and what it can and cannot support.

The story that makes SuperGLUE worth teaching: it was built in 2019 precisely
because its predecessor GLUE had been saturated, its hardest tasks chosen so
models had headroom below the human baseline, and within about eighteen months a
model (DeBERTa, January 2021) passed that human-baseline row, producing a wave of
"AI surpasses humans at language understanding" coverage. That is the real case
where the number misled people.

## What the lesson must do

Explain the number step by step, in the reader's hands by the end:

- The eight tasks and that each has its own metric (accuracy, F1, exact match).
  The reader does not need all eight memorized, but must see that the leaderboard
  number is an average of per-task scores measured in different units, so "one
  number" hides a weighting choice.
- Where the human baseline came from: how the authors produced it (annotators
  under a specific protocol), and why that row is a measurement with its own
  method, not a fixed fact about human ability.
- What the number supports (comparing systems on this fixed task set) and what it
  does not (that a model above the human row "understands language," or matches a
  careful human, or will hold up off the benchmark). Cover task artifacts /
  shortcut features and saturation.
- The real misleading case: name the model and date that crossed the human
  baseline, the coverage it drew, and what that crossing did and did not mean.
  What it cost: the claim entered public argument as "AI beats humans at reading
  comprehension."

## Required contribution

The reader should be able to take any "model beats human baseline on benchmark X"
headline and ask the three questions this lesson teaches: what was averaged, how
the human row was made, and what the tasks actually test. The article's work on
the evidence is turning a leaderboard number back into the choices that built it.

## Boundaries and continuity

- GLUE is already taught (the-instruments/glue): link it in Background for the
  predecessor-and-saturation context; do not re-explain GLUE from scratch. Focus
  the lesson on SuperGLUE, its human baseline, and the crossing.
- One measurement. Do not drift into a tour of every NLP benchmark.
- Name no company as an authority.

## This run's neighbors

Four other lessons publish tonight on other desks (constitutional-ai,
counting-objects-in-images, open-weights-release, bard-jwst-demo). No overlap.

## Source policy

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Candidate
primaries: SuperGLUE paper (1905.00537); GLUE paper (1804.07461); the SuperGLUE
leaderboard page; the DeBERTa paper (2006.03654) or the model report that first
crossed the human baseline; the T5 paper (1910.10683) for a top entry. Secondary:
contemporaneous reporting on the human-baseline crossing. The researcher confirms
kind and count, and pins the exact model/date of the crossing to a primary.

## Production policy (recorded)

profile balanced. writing-coach low, researcher high, writer medium, editor high.
Model "capable" for every role, none required; roles run on this harness's
default capable model. Record actual models in handoffs.

## Recent patterns to break (habits, not rules)

- Deks recur as a two-clause ", and"-twist (toxicity-score, gradient-hacking,
  galactica) or a comma triad (adversarial-examples, banned by spec/headlines.md).
  Build this dek differently.
- Headlines default to a negative-fact reveal or a trailing second clause. The
  instruments desk in particular likes a headline carrying a specific number
  (imo-gold, "Two AIs reported the same 35/42 gold..."). A number can earn the
  headline here, but do not reach for the same "same number, two readings" shape
  imo-gold used.
- The present-day closing section keeps getting a "Where X still Y" heading. Vary
  it.

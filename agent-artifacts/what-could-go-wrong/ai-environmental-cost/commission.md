# Commission: what-could-go-wrong/ai-environmental-cost

## The argument

That AI's physical footprint, the electricity, water, and carbon of training and
running large models in data centers, is a serious and worsening environmental
harm: a reason to slow deployment, disclose usage, or price the externality.
This is the mainstream environmental case against the AI build-out, made in the
press and by some researchers, and it is genuinely contested in both directions.

## The angle and the desk's method

Follow the desk method. Open with the argument at full strength: name who made
it and what they saw. Strubell, Ganesh & McCallum (2019) put a number on the
carbon of training one NLP model and started the modern debate; the argument now
points at data-center electricity growth and water use for cooling as AI scales.
Lay it out as its most careful defender would.

Then draw the sharp line the prompt demands: what is measured vs what is
extrapolation. The honest picture: aggregate data-center electricity is real,
rising, and measured (IEA); the viral per-query figures ("one ChatGPT question =
X bottles of water / a phone charge") are mostly weak extrapolations from thin or
mismatched data, and several widely-cited numbers have been walked back or
disputed. Training-run carbon numbers depend enormously on the grid and the
accounting method (Patterson et al., Google). Set measured aggregates against
inflated per-unit claims.

Bring it to the present: who makes the argument now and what they want
(disclosure, efficiency standards, slowing build-out), and check it against the
most recent evidence. Name the gap where confidence outruns proof on BOTH sides:
alarmists quote per-query figures with no sourcing and ignore efficiency gains;
dismissers wave away a real, fast-growing aggregate load and undisclosed water
use by pointing to per-query smallness. The two sides are often measuring
different things.

Original work for the writer: separate the per-unit question (how much energy or
water one query or one training run costs) from the aggregate question (how much
the whole AI build-out adds to grids and water systems). Almost every headline
number answers the first badly; the real risk lives in the second, which is
measured but uncertain. State that and show it from the primary measurements.

## What the lesson teaches (short list, in order)

1. The argument at full strength: the environmental case against the AI
   build-out, from Strubell 2019 to today's data-center-growth and water
   concerns, in its defenders' terms.
2. What one query or one training run actually costs, and why the viral figures
   are unreliable: the accounting problems (grid mix, PUE, marginal vs average,
   inference vs training, undisclosed denominators). Show one widely-quoted
   per-query claim and what is wrong with how it was derived. Link the published
   the-instruments/energy-per-query lesson for the metric; do not re-teach how
   per-query energy is measured.
3. What is actually measured at aggregate scale: IEA data-center electricity
   figures and projections; a training-run carbon figure with its grid
   dependence (Patterson/Google). The measured trend and its uncertainty.
4. The present dispute and the gap: the per-unit vs aggregate confusion, what
   each side extrapolates past the evidence, and what disclosure would settle.

## Boundaries

- One argument (environmental footprint). Do not drift into AI's effect on
  climate modeling, or into energy markets generally.
- Load-bearing distinction: per-unit cost vs aggregate build-out load.
- Taught ground to link, not re-teach: the-instruments/energy-per-query (the
  metric) and training-compute/training-cost are published in a sibling desk;
  link the metric, do not re-teach it. This piece is the risk argument, not the
  measurement lesson.
- Work from original documents: Strubell 2019, Patterson 2021/2022, Luccioni
  BLOOM, the IEA report, de Vries 2023. Never the commentary for a number.
- Do not resolve it for the reader. Name the gap; leave the worry to them. Name
  no company as an authority.

## Neighbouring articles this run (avoid overlap)

Tonight also runs the-instruments/mlperf (which may mention an MLPerf Power
metric — that is measurement, not this argument), the-evidence/elmo,
the-mechanics/hangman, when-ai-breaks/babylon-health. Keep this piece on the
risk argument; do not turn into a measurement tutorial (that is the-instruments'
job and is linked).

## Recent-pattern notes (habits to break)

what-could-go-wrong recently opened with "The two things blame needs" and "The
goal names less than we care about," and several pieces close on a "present-day
relocation" line ("the vase looks quaint, and the files still get deleted"). Do
NOT reuse that closing mold. The desk's "shown vs guesswork" table is idiomatic;
if you use a table, do not copy a prior piece's shape. Deks lean on "and no one
has yet measured"; build a different dek. Headings distinct from each other.

## Source obligations

lesson under what-could-go-wrong: min 8 sources, >=4 primary, >=1 secondary.
Primary: Strubell, Ganesh & McCallum 2019 ("Energy and Policy Considerations for
Deep Learning," ACL); Patterson et al. 2021/2022 (Google, "Carbon Emissions and
Large Neural Network Training" / the follow-up); Luccioni, Viguier & Ligozat
(BLOOM carbon footprint); the IEA report on electricity/data centers (a specific,
dated edition, owner of the aggregate/projection numbers); de Vries 2023 (Joule,
"The growing energy footprint of artificial intelligence"). Secondary: reputable
reporting that documents a walked-back or disputed per-query figure, never for a
number.

## Production record

Profile balanced. Recorded (policy "capable"): writing-coach Opus 4.8/low,
researcher Opus 4.8/high, writer Opus 4.8/medium, editor Opus 4.8/high. No
required directive; no deviation.

## Bookend link candidates

Background: `the-instruments/energy-per-query` (the per-query metric),
`the-instruments/training-compute` or `training-cost` (the scale of a training
run). Go deeper (beyond this paper): the IEA report; the Strubell paper. Lesson
works for a reader who opens none.

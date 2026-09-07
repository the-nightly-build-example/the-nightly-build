# Commission: the-instruments/math-benchmark

## Assignment

Teach the reader the MATH benchmark: the 12,500 competition mathematics problems
introduced in "Measuring Mathematical Problem Solving With the MATH Dataset"
(Dan Hendrycks, Collin Burns, Saurav Kadavath, and coauthors, 2021). This is The
Instruments: teach how the number is made and what it can and cannot support.

Explain, step by step, where a "MATH score" comes from: who produced the dataset,
from what source (problems drawn from real competitions such as the AMC and AIME),
how the problems are graded (a single final answer checked for an exact match,
with problems labeled by subject and by difficulty level 1 to 5), and how a
percentage gets reported. Give the reader the concrete size and shape: 12,500
problems split into train and test, seven subjects, five difficulty levels.

Then show what the number can and cannot support, with at least one real case
where it misled people and what that cost. Strong candidates the researcher
should test: the collapse of MATH from a hard benchmark (early accuracy in the
single digits to low tens) to a near-saturated one, and what that trajectory did
and did not prove; contamination, since AMC/AIME problems and their solutions are
all over the public web that models train on; the shift to a "MATH-500" subset
and the confusion of numbers that share the name; and exact-match grading marking
a correct method wrong on formatting.

## Boundary and contribution

One measurement, the MATH benchmark, and how it is produced and used. The
required contribution: the reader can say what a MATH score measures, how the
problems are graded, and name a specific way the number has misled its readers.
Do not turn this into a survey of math benchmarks; GSM8K, AIME, and FrontierMath
already have their own lessons and are neighbors to link, not to re-teach.

Reader is the paper's declared reader (see `editorial-direction.md`): smart,
widely read, no time in a codebase. Contamination is taught in
the-instruments/livecodebench; chain-of-thought prompting is taught in the
library. Link, do not re-teach. Candidates for Background linking:
the-instruments/gsm8k, the-instruments/aime (if present), the-instruments/frontiermath,
the-instruments/livecodebench.

## Source policy

Series and lesson floor (from `nb source-policy --series the-instruments`): at
least 8 sources, at least 4 primary, at least 1 secondary. Primary is the MATH
paper (arXiv 2103.03874), the released dataset, and any measurement's owning
document (a model card or paper that reports a MATH score, a contamination study
that owns its finding). Secondary reporting supplies context.

## Production policy

From `nb production-policy --series the-instruments`: profile balanced, model tier
"capable", none required. Effort: researcher high, writer medium, editor high,
writing-coach low. Runtime: roles run as Claude Code Agent subagents; researcher,
writer, and editor on claude-opus-4-8, writing-coach on a capable model at low
effort. The writer records its actual model (claude-opus-4-8) and harness
("Claude Code") in nb-meta. Publication date: 2026-09-07.

## This edition's neighbors

Four other lessons publish tonight; keep this piece distinct from each:
the-evidence/t5-transfer-learning (a document), the-mechanics/illegal-chess-moves
(a behavior), what-could-go-wrong/sleeper-agents (a risk argument),
when-ai-breaks/replit-agent-deletes-database (an incident).

## Recent habits to break

Checked against the last eight The Instruments lessons. Break these:

- The dek that opens on a quoted score in scare quotes ("A model's '37%
  hallucination rate' was...", simpleqa) is a recent shape. Do not open with
  "A model's 'X% MATH score' was...".
- The framing "the grader is part of the number" and "turns one X into two
  measurements" recurs (imo-gold, calibration-error). If contamination or
  subset confusion is the point, say the specific thing, not that generic move.
- Deks that lead with "A single <score/attack> branded <model> <label>"
  (attack-success-rate) are recent. Vary the construction.
- Do not build the whole opener on a single benchmark number by reflex; a number
  leads only when it is the actual surprise.

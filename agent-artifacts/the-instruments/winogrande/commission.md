# Commission: the-instruments/winogrande

## Assignment
Teach WinoGrande as a measurement: the 2019 commonsense-reasoning benchmark
(Sakaguchi, Le Bras, Bhagavatula, Choi) that rebuilt the Winograd Schema
Challenge at scale to strip out the surface cues models had been exploiting.
Explain where the number comes from and what it can and cannot support, with at
least one real case where the number misled people and what that cost.

## What to establish, step by step
- The origin it answers: the Winograd Schema Challenge (Levesque, Davis,
  Morgenstern, 2012), a small set of sentence pairs that turn on one pronoun
  whose referent flips with a single word. State why it was designed as a
  common-sense test that resists cheap statistical shortcuts, and how small it
  was.
- What WinoGrande changed: the scale (give the exact problem count), the
  crowdsourcing procedure, and above all the adversarial filtering step (AFLite)
  that removes items solvable from dataset-specific word associations rather than
  reasoning. Explain AFLite in plain words: what "annotation artifact" and
  "adversarial filtering" mean, defined where first used.
- The numbers: the human-performance figure the paper reports, the machine
  baselines at publication, and how the reported difficulty of the set depends on
  the filtering. Show that the score is a property of the filtered set, not a
  fixed law.
- The misled case: pick a documented one and cost it out. Candidates: models
  posting near-human WinoGrande scores while later shown to lean on residual
  artifacts or benchmark contamination; the general finding that Winograd-style
  scores rose without the reasoning the test was built to require. Draw the sharp
  line between the score and the capability people read into it.
- The present: WinoGrande still appears in model cards and leaderboards. Say what
  a current WinoGrande number does and does not license a reader to conclude.

## Why this measurement, why now
Model cards still report WinoGrande, and the course has taught benchmark suites
(the-instruments/glue, superglue) and one shortcut collapse (the-evidence/bert)
but never the commonsense benchmark whose whole design is a response to shortcut
exploitation. It teaches the reader how a benchmark is hardened and why a high
score can still be hollow.

## Boundaries: link, do not re-teach
- the-evidence/bert already tells a "near-human score collapsed once the shortcut
  was closed" story. Do not retell BERT's case as this piece's spine; cite it in
  Background and center on WinoGrande's own construction and numbers.
- the-instruments/glue and superglue teach the benchmark-suite framing and
  include the Winograd task in SuperGLUE (WSC). Link them; do not re-teach what a
  benchmark suite is.
- Precision, recall, accuracy as metrics are handled elsewhere
  (the-instruments/f1-score). Assume accuracy; define only what is specific here.

## Neighbors this edition
Tonight also runs the-evidence/gpt-1, same BERT/GLUE era. Keep this piece on the
benchmark and its artifacts; leave the model recipe to that piece.

## Sources
Lesson floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary: the WinoGrande paper, the 2012 WSC paper, the AFLite source, and the
model reports or leaderboard entries whose WinoGrande figures you cite firsthand.
Secondary: outside analysis for context. Read the WinoGrande paper in full,
including the AFLite section and the human-evaluation details.

## Production record
- Profile: balanced. Roles run as isolated Claude subagents (capable tier).
- Effort by stage: writing-coach low, researcher high, writer medium, editor high.
- Writer records the actual writer model in nb-meta `model`, sets `harness` to
  `claude-code`. Article date: 2026-09-17.

## Recent habits to break
- the-instruments/clipscore just closed its body with "What happens when the
  grade becomes the goal" (a Goodhart closer). Do not reuse that heading or that
  Goodhart-closer move as this piece's final section.
- Avoid the compression-definition heading mold recent instruments pieces used
  ("One cosine, clipped and stretched", "Five words, averaged").
- Avoid the "checked on X, trusted on Y" phrasing (clipscore) for the misled-case
  section.
- Do not build headline or dek as the two-sentence "[Claim]. [Terse rebuttal]."
  mold, nor as a comma triad closed with "and".

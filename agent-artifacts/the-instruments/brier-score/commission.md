# Commission: the-instruments/brier-score

## The measurement

The Brier score — the mean squared error of probabilistic predictions. Chosen
after a full scan of The Instruments: the section covers AUROC (ranking) and
expected calibration error (binned calibration), but not the single proper
scoring rule now used to compare AI forecasters against humans and to grade any
model that outputs probabilities. It is the number behind the live claim that
language models are "approaching human-level forecasting."

CONFIRMED not previously published (checked against the full the-instruments slug
list). Distinct from the published calibration-error (ECE) and auroc lessons —
link both; Brier combines what they separate.

## The angle

Explain where the number comes from step by step, then show a real case where it
misled people.

1. What the Brier score is, concretely. For a set of yes/no questions where the
   model gave each a probability, the Brier score is the average of (probability −
   outcome)^2, where outcome is 1 if it happened and 0 if not. Lower is better; 0
   is perfect, 0.25 is what you get by always saying 50%. Work one tiny example
   with real numbers so the reader can compute it. Establish "proper scoring rule"
   plainly: a score you do best on by stating your true probability, so it can't
   be gamed by hedging or by sounding confident.

2. What the number can and cannot support. This is the teaching core:
   - Brier bundles two things a single number hides: calibration (do your 70%s
     happen 70% of the time?) and resolution/discrimination (do you push away from
     the base rate at all?). Two models with the same Brier can differ completely.
     Use the Murphy decomposition in plain words (reliability, resolution,
     uncertainty) without the algebra.
   - The base-rate trap: on a set where the event is rare, a model that ignores
     every question and always predicts the base rate can post a deceptively low
     Brier. Show this with numbers.
   - Brier depends on the question set. A Brier score is only comparable across
     systems answering the same questions over the same period; a lower Brier on
     easier or differently-distributed questions says nothing. Contrast with ECE
     (link the calibration-error lesson) and AUROC (link) so the reader sees what
     each isolates.

3. The real case where it misled. The strongest documented one: the 2023-2024
   wave of "LLMs approach human-level / superforecaster-level forecasting" claims,
   several scored by Brier. Surface the specific numbers (an LLM-forecaster Brier
   vs a human/crowd Brier vs the always-50% baseline) and the critiques — that
   some results did not replicate, that the comparison question sets or resolution
   dates differed, or that a good aggregate Brier hid confident wrong calls on the
   questions that mattered. The researcher gathers the numbers; the writer picks
   the best-sourced instance and states what the misreading cost (a claim taken as
   settled that the evidence did not support).

Anchor fact to foreground: a Brier score can be made to look good two cheap ways —
by only ever predicting the base rate, or by being tested on an easier set of
questions — so "our model's Brier beats humans'" means nothing until you know the
questions were the same and the model actually moved off the base rate.

## Boundaries

- One measurement: the Brier score (with its Murphy decomposition and the
  base-rate/comparability traps). Not a general tour of forecasting or of every
  probabilistic metric. Reference ECE and AUROC only to contrast, by link.
- No code. One worked numeric example carries the definition; keep any
  decomposition in plain words.

## Required contribution

The reader should finish able to read a Brier-score comparison critically: to ask
whether the systems answered the same questions over the same period, whether a
low score is just base-rate prediction, and what calibration-vs-discrimination the
single number is hiding. They should be able to judge an "AI approaches human
forecasting" headline on its merits.

## Source and production policy

- Sourcing floor (nb source-policy): minimum 8 sources, at least 4 primary, at
  least 1 secondary. Primary = Brier (1950) original; a source that owns the
  Murphy decomposition; the primary write-ups of the AI-forecasting studies whose
  Brier scores are cited (e.g. Halawi et al. 2024 and any replication/critique);
  a forecasting-platform methodology (e.g. Metaculus/Good Judgment) that owns its
  Brier definition.
- Production policy (balanced, no `required` directive): editorial roles run on a
  capable model (Claude Sonnet class) in isolated subagents; effort follows policy
  (coach low, researcher high, writer medium, editor high). No directive traded down.

## Recent-pattern notes (habits not to inherit)

- Opener habit: the "By the end you will know..." triad and temporal-generic
  scene-set opening (the most recent Instruments pieces open this way). Break it.
- Takeaway habit: two-part balance closers. End on this lesson's own point.
- Heading habits over-used across The Instruments: "How a X becomes a Y" /
  "How the judge counts a win rate", "Turning a X into one number", "Reading a
  rank you did not compute" / "Reading a vote as if it were one try" (a
  "Reading X as Y" closer recurs — do not reuse it), and the nb-holdsup pairing.
  Vary construction.
- Dek habit: comma-triad and comma-splice deks (`spec/headlines.md` bans the
  triad). Keep the dek lean.

## Neighbouring articles in tonight's edition

- the-evidence/flamingo (the 2022 few-shot multimodal paper)
- the-mechanics/familiar-pattern-override (why modified classic riddles break models)
- what-could-go-wrong/companion-dependency (the AI-companion-harm argument)
- when-ai-breaks/predpol-predictive-policing (the PredPol/Geolitica failure)
No overlap. This is tonight's "how a number is made" lesson.

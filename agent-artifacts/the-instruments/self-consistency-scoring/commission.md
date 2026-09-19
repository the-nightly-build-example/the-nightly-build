# Commission: the-instruments/self-consistency-scoring

## Assignment

One lesson for The Instruments on majority-vote scoring — the convention behind a
headline number written cons@k, maj@k, or "self-consistency," in which a model
answers the same problem k times and its score is taken from the most common final
answer. Teach where the number comes from, step by step, then what it can and
cannot support, including a real case where it misled people and what that cost.

## What this lesson teaches

Explain the procedure plainly:

1. Sample k separate chain-of-thought attempts at nonzero temperature for one
   problem.
2. Extract each attempt's final answer and take the plurality (the answer that
   appears most often).
3. Score that voted answer. Report it as cons@k or maj@k for the chosen k.

Then teach what the construction does and does not support:

- It costs k times the inference compute of a single answer, so a cons@64 score and
  a single-sample score are not the same measurement and are not comparable.
- It lifts accuracy on problems with one checkable answer where the model is right
  more often than any single wrong answer is repeated; it cannot rescue a problem
  the model is confidently and consistently wrong about.
- The origin is Wang and coauthors' 2022 self-consistency method; the reporting
  convention is what this lesson teaches.

## The case where it misled (the spine)

Center on a documented case where a majority-vote number was read as raw
capability: a headline reasoning-model math score (for example on AIME or MATH)
reported at cons@k or maj@k and set beside a rival's single-sample score, or the
compute behind the number left unstated. The researcher should identify the
clearest real instance and its cost.

## Boundaries and neighbors

Distinct from the library's existing scoring lessons; link them in Background, do
not retread:
- the-instruments/humaneval-pass-at-k (pass@k: any of k attempts correct — a
  different rule, used for code)
- the-instruments/aime (the variance of a 15-problem test)
- the-instruments/math-benchmark (the same name covering different problem sets)
This lesson's own subject is the majority-vote scoring convention: how the number
is built, why it is not comparable to single-sample scores, and how it is used in
public comparisons. The reader has algebra and probability but not machine
learning; define chain-of-thought, sampling temperature, and plurality/majority
vote in plain words at first use.

## Contribution the article must add

Make a cons@k number legible: why sampling many times and voting raises a score,
what compute it hides, and why comparing it to a single-sample number is unfair.
The writer states the exact original-work sentence in the handoff.

## Sources

Series/template floor: at least 8 sources, at least 4 primary, at least 1
secondary. Primaries available: Wang and coauthors' self-consistency paper (2022);
a model report or system card that states a cons@k / maj@k / self-consistency score
(for example a reasoning-model release, Minerva, or a frontier math result); the
AIME/MATH context these numbers ride on; and a paper analyzing majority-vote versus
single-sample accuracy or the compute tradeoff. Secondary reporting for context.

## This edition (keep distinct from the run's other four lessons)

- the-evidence/alphastar
- the-mechanics/output-diversity
- what-could-go-wrong/mind-crime
- when-ai-breaks/amazon-rekognition-congress (already published tonight)

Shared risk with the-mechanics tonight: both touch sampling many times from a
model. Keep this one on the scoring convention and its public misuse; the mechanics
piece is about output diversity, a different subject.

## Habits not to inherit (from the recent library)

- Recent The Instruments deks lead with a numeric contrast in one long sentence;
  do not default to that mold.
- Recent headings lead with a raw number or use the comma-and contrast; vary
  construction.
- The recurring furniture stack is nb-stat-strip, nb-figure, nb-table, nb-note,
  nb-holdsup. Plan furniture from the supplied catalog for this piece.

## Production

Profile balanced. Model: capable (Claude Opus 4.8) for every role. Effort per
production policy: writing-coach low, researcher high, writer medium, editor high.
No required directive is in force. The writer records the actual writer model in
nb-meta per the library's convention (harness "claude-code").

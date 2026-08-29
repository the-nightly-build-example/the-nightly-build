# Commission: the-instruments/mmlu-pro

## Subject
The measurement is MMLU-Pro: the benchmark score reported on the TIGER-Lab
MMLU-Pro dataset (Wang et al., "MMLU-Pro: A More Robust and Challenging
Multi-Task Language Understanding Benchmark", 2024). This desk teaches how the
number is made and what it can and cannot support.

## Why this measurement, now
`mmlu` is already a published lesson on this desk. MMLU-Pro is the successor labs
now report in place of a saturated MMLU, and it appears at the top of current
model cards. The reader has the MMLU lesson and is owed the number that replaced
it: how it was built to fix MMLU's specific defects, and whether it did.

## Angle / what the lesson teaches
Explain where the MMLU-Pro number comes from, step by step: who produced it
(TIGER-Lab), from what data (MMLU questions plus additions from other sources),
by what procedure (expanding four options to ten, filtering trivial and
mislabeled items, tilting toward reasoning). Teach the two design changes that do
the real work: ten options instead of four cuts the score you can get by guessing,
and the reasoning tilt widens the gap between chain-of-thought and direct answers.
Then show what the number can and cannot support, with at least one real case
where an MMLU-family number misled people: MMLU itself was shown to contain wrong
answer keys and ambiguous items (Gema et al., "Are We Done with MMLU?"), and
scores were sensitive to prompt format and option ordering. Say plainly what
MMLU-Pro fixed and what it inherited.

## The article's distinct contribution
Show that MMLU-Pro is not simply "a harder MMLU" but a set of specific repairs to
named failure modes of MMLU, and grade each repair against the evidence: guess
rate (fixed by construction), label noise (reduced but not eliminated), prompt
sensitivity (reduced, per the paper's own robustness measurement). The reader
should leave able to say what a given MMLU-Pro gap between two models does and
does not license.

## Template & policy
- Template: `lesson`.
- Source policy: min 8 sources; at least 4 primary, at least 1 secondary.
- Production policy (`balanced`, none `required`): researcher high, writer medium,
  editor high, coach low. Models this run: coach on a capable Sonnet-class model;
  researcher/writer/editor on a capable Opus-class model. No `required` directive.
- Tags: none (open item).

## Neighbors in this run (differentiate)
Runs alongside `the-evidence/proximal-policy-optimization`,
`the-mechanics/negation`, `what-could-go-wrong/treacherous-turn`,
`when-ai-breaks/workday-hiring-screening`. No subject overlap.

## Prior coverage to stay off
`mmlu` (the parent), `gpqa`, `big-bench-hard`, `humanitys-last-exam`,
`frontiermath`, `hellaswag` are published. Link `mmlu` in Background rather than
re-teaching what MMLU is; spend the words on what MMLU-Pro changed. Do not repeat
the general "benchmarks saturate / contamination" lesson those pieces already
carry except exactly where MMLU-Pro's construction addresses it.

## Recent habits not to inherit (from the last week of The Instruments)
- This desk's headlines keep the mold "A model can top the X average and be
  ordinary at Y" and "The score labs cite grades one Z, and usually never runs
  it." Both are the "cited number is hollow" reveal. MMLU-Pro's story is partly a
  repair that worked, so do not force the standard debunk-headline; state what is
  actually surprising here.
- Deks have leaned on the comma-triad and the "one flat average over N datasets"
  construction. Check the recent deks and pick a different build.
- nb-table is the reflex here (used to lay out benchmark internals). A table of
  MMLU vs MMLU-Pro construction may earn its place, but do not add a second table
  by habit.

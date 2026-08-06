# Commission: the-instruments/glue

## Authorized work
Scheduled run for 2026-08-06. `nb duty` returned `the-instruments` in open mode.
One article this edition; process this one only. Topic verified absent from the
full published-slug list recorded below.

## Subject
The GLUE benchmark score (and its successor SuperGLUE), the aggregate number that
was used to declare that machines had reached "human-level" natural language
understanding. A measurement lesson: where the number comes from, step by step,
and what it can and cannot support, with the real case where it misled people.

- Where the number comes from: GLUE (Wang et al. 2018) bundles nine English
  sentence-understanding tasks (sentiment, entailment, paraphrase, etc.) into one
  leaderboard, scoring a model as the average of per-task metrics, and publishes a
  "human baseline" for comparison. Explain, with a small concrete example, how a
  handful of tasks with different metrics get averaged into a single headline
  number, and what the "human baseline" actually is (a small number of annotators/
  crowdworkers scored on the same test).
- What it can support: relative progress on a fixed set of English NLU tasks.
- What it cannot support: "understanding." The tasks carry annotation artifacts
  and spurious shortcuts (e.g. Gururangan et al. 2018 hypothesis-only baselines on
  NLI; models exploiting surface cues), so a high score can reflect shortcut
  exploitation, not comprehension.
- The real case where it misled people: models passed the GLUE human baseline
  within about a year, fueling "AI has solved language understanding" claims; the
  authors had to build SuperGLUE (2019) with harder tasks and a new human
  baseline, and models passed that too within ~18 months, while the tasks were
  still shown to contain exploitable artifacts. Report the exact dates, the
  human-baseline numbers, and when each was surpassed.

## Required contribution
Turn "AI reached human-level language understanding" back into a specific
measured quantity: an average over a fixed task set, against a thin human
baseline, on data with documented shortcuts. The reader should be able to read a
"surpassed the human baseline" claim and say exactly what was and was not
measured.

## Boundaries / do not repeat
FULL published the-instruments slugs: aime, arc-agi, bar-exam-percentile, bleu,
chatbot-arena-elo, context-window, cost-per-token, energy-per-query,
frontiermath, gpqa, gsm8k, humaneval-pass-at-k, llm-as-a-judge, mmlu,
parameter-count, perplexity, swe-bench, tokens-per-second, training-compute.
GLUE/SuperGLUE and the "human baseline" idea are unrepresented. Distinct from
mmlu (a knowledge exam; link as Background, do not re-teach how a benchmark
score can hide its harness) and bleu (a single translation metric; GLUE is an
aggregate of NLU tasks). Algebra/probability need no introduction; define
"annotation artifact" in plain words at first use.

## Template & policy
- Template: lesson; body 1200-2200 words; bookends fixed.
- Tags: none (`--tag` unused); editorial `data-nb-tags` are the writer's choice.
- Source policy: min 8 sources, at least 4 primary, at least 1 secondary.
- Balanced profile, model "capable", no `required`. Harness: claude-code-routine.
  Efforts: coach low, researcher high, writer medium, editor high.

## Neighboring articles this edition
the-evidence/gans; the-mechanics/memorization; what-could-go-wrong/sandbagging;
when-ai-breaks/facebook-myanmar. No subject overlap.

## Recent shapes to break (habits, not rules)
Recent the-instruments deks/headlines lean on "two true numbers disagree" and the
exact-figure-plus-swing move. A benchmark-surpassed date is a number worth
stating, but do not reuse the "both are true" mold the series has run several
times. Vary heading cadence away from comma-and pairs; avoid the semicolon
reversal / suspended question / comma-triad dek molds. These travel to the writer.

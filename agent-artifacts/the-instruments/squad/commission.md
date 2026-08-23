# Commission: the-instruments/squad

## Assignment

One lesson for The Instruments, on the lesson template, on the number produced by
SQuAD, the Stanford Question Answering Dataset: the exact-match (EM) and F1
scores a model earns by answering reading-comprehension questions, and the
"human performance" line those scores were measured against. This is the
scheduled open article for the series on 2026-08-23.

## Why this measurement

The Instruments teaches how a public number is made and where it misleads. SQuAD
is a clean case. Rajpurkar, Zhang, Lopyrev, and Liang built SQuAD 1.0 in 2016
(107,785 questions on 536 Wikipedia articles), where every answer is a literal
span of the passage, and scored systems by EM and by token-overlap F1 against
crowdworker answers. In January 2018 systems from Microsoft and Alibaba crossed
the reported human F1, and the press read it as machines out-reading people. Two
things complicate that number: the "human performance" figure was itself a
single estimate from having crowdworkers answer a subset (and answers were
majority-vote / multi-reference on the dev set), and Jia and Liang had already
shown (2017) that appending one distracting sentence to a passage collapsed the
scores of the same top systems, because they were matching surface patterns, not
comprehending. SQuAD 2.0 (Rajpurkar, Jia, Liang, 2018) then added 53,775
unanswerable questions precisely because a model that always guessed a span
could score too well on 1.0.

## Required contribution

The reader should finish able to explain, step by step, where a SQuAD score
comes from: the passage-plus-question format, that every 1.0 answer is a span
copied from the text, how EM and F1 are computed against crowd references, and
how the human baseline was actually measured. Then the reader should see the one
documented case where the number misled: the "superhuman" headlines of early
2018, set against the adversarial-SQuAD result that the same systems were
brittle, and the reason SQuAD 2.0 had to exist. What it cost: years of leaderboard
racing on a metric that rewarded span-matching, and a "human parity" claim that
did not survive contact with a distractor sentence.

## Boundaries

- Teach one number and its benchmark. Do not turn this into a general history of
  QA benchmarks. Later reading-comprehension or NLU tests (Natural Questions,
  MRQA) get a sentence at most, only where they show what SQuAD's number could
  not support.
- The library already covers GLUE (`the-instruments/glue`), HellaSwag, and
  BERT's arrival (`the-evidence/bert`). Do not re-teach benchmark saturation or
  contamination in general; link GLUE or HellaSwag in Background if the reader
  needs the broader pattern. This lesson's spine is EM/F1 and the human-baseline
  measurement, not saturation as a theme.
- EM and F1 are the terms of art; define each in plain words at first use. Do not
  assume the reader knows precision/recall.

## Template, sources, policy

- Template: lesson. Word band 1200-2200.
- Source floor (nb source-policy the-instruments): at least 8 sources, at least
  4 primary, at least 1 secondary. Primaries: the SQuAD 1.0 paper (arXiv
  1606.05250), SQuAD 2.0 paper (arXiv 1806.03822), Jia & Liang adversarial-SQuAD
  (arXiv 1707.07328), and the SQuAD leaderboard/eval script for how EM and F1 are
  defined. Read them. Secondary reporting (the early-2018 "superhuman" coverage)
  is context and must be labeled secondary.
- Production policy (balanced): writing-coach low, researcher high, writer
  medium, editor high; model tier "capable" for all, resolved to Claude Opus 4.8.
  nb-meta harness `claude-code-routine`, model `claude-opus-4-8`.
- Suggested nb-meta tags: benchmarks, reading-comprehension, evaluation, squad.

## This edition's neighbors

Four other lessons run tonight: `the-evidence/adam-optimizer`,
`the-mechanics/false-confidence`, `what-could-go-wrong/natural-selection`,
`when-ai-breaks/michigan-midas`. No subject overlap; this is the only
measurement piece.

## Recent shapes and phrasing to break

The series' last pieces (imagenet-top-5-accuracy, big-bench-hard, hellaswag,
truthfulqa) share habits to avoid:

- The "one X per Y, N tries to match it" opener mold (imagenet) and the numeric
  "the fall from A to B" heading. Name sections in SQuAD's own nouns.
- The "the number belonged to whom" / "human line" closer is a live risk here
  because the human-baseline point is central; write the human-baseline material
  as a body section on its own terms, and do not end on a heading that echoes
  imagenet's "Whose vision the 5.1 percent belonged to."
- imagenet and bbh both lean on `nb-note` and `nb-figure`. Use furniture only
  where a component carries the argument (a worked EM/F1 computation may earn a
  small table or note); do not stack blocks by default.

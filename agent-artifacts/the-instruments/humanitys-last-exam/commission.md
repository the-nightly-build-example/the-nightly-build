# Commission: the-instruments/humanitys-last-exam

## Authorization

Scheduled run for 2026-08-14 (Fri). `nb duty` returned the-instruments as an open
section: choose a topic within the beat, do not repeat a published slug. One of
five articles commissioned tonight, one per due series.

## The measurement

Humanity's Last Exam (HLE), a benchmark from the Center for AI Safety and Scale
AI, released January 2025. It is a set of expert-written, closed-ended questions
across many academic subjects, built to be hard for frontier models: questions
were crowdsourced from subject experts, reviewed in stages, and filtered so that
current models failed them at submission time. The number in circulation is the
percentage a model answers correctly, reported with a calibration error, and it
started in the single digits.

## Angle

Teach how the HLE number is manufactured, then show what it can and cannot
support. The construction is the point: questions are adversarially selected
against the models of the day and graded closed-ended, so a low score and a fast-
rising score mean specific, limited things. The real case where the number
misled: the name itself plus the rapid climb read as AI nearing the limit of
human knowledge, and tool-augmented or browsing runs got compared against
no-tool runs as if they were the same measurement. Give the reader enough to
know what a given HLE percentage is evidence of and what it is not.

Show the scale and the mechanics honestly: how many questions, how many
contributors, what "closed-ended" grading rewards, why adversarial filtering
against current models bounds what the score can say about the next model.

## Boundaries and neighbors

- Template: `lesson`. No open-item tags.
- Source policy: at least 8 sources, at least 4 primary and at least 1 secondary.
  Primary is the HLE paper/dataset and its authors, and the model reports or
  leaderboards that own each cited score; secondary is reporting and commentary.
- This desk has taught many benchmarks (mmlu, gpqa, frontiermath, arc-agi,
  truthfulqa, mmmu, needle-in-a-haystack). HLE's distinct angle is a benchmark
  built to be unsolvable by current models and graded closed-ended, and the
  misreading that follows from its framing and from tool-vs-no-tool scores. Do
  not reprise another benchmark's gameability story; find HLE's own.
- Recent the-instruments pieces lean on the move "the score can be moved from X%
  to Y% by a trivial change." HLE's honest story is different (scores are low by
  construction and rise fast). Do not force the gameability frame onto it.

## Production record

- Profile: balanced. Stages (model / effort, none required): writing-coach
  capable / low, researcher capable / high, writer capable / medium, editor
  capable / high.
- Harness: each role runs as an isolated subagent on the configured capable
  model; deviations recorded per role.
- Workspace: `.nb-work/the-instruments/humanitys-last-exam`.
- Article: `library/the-instruments/humanitys-last-exam.html` under that
  workspace.

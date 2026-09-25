# Commission: the-instruments/mlperf

## The measurement

MLPerf, the industry benchmark suite run by MLCommons, and the numbers vendors
quote from it to compare AI hardware and systems: training time to a target
quality, and inference throughput (queries or tokens per second) under defined
scenarios. When a chipmaker says its accelerator "set a record" or is "N times
faster," the number usually comes from an MLPerf submission.

## The angle and the original work

Teach exactly how an MLPerf number is made, step by step, then show what it can
and cannot support and one real case where the comparison misled. The pipeline:
MLCommons defines a fixed task, model, dataset, and quality target; vendors
submit runs on their own hardware; results are grouped into divisions (Closed =
same model and rules, comparable; Open = anything goes) and availability
categories (Available, Preview, RDI/research). A "record" only means something
within the same division, category, task, and system scale.

The misled case: MLPerf comparisons are routinely quoted across
non-comparable configurations. Document a concrete one from the record: e.g. a
vendor's headline "X times faster" that comes from a different system scale
(number of chips), a different division, or an Open-division submission compared
against a Closed-division one; or the recurring pattern where a submission uses
far more accelerators than the system it is implicitly compared to. Give the
specific submission round, the vendors, and the numbers.

Original work for the writer: an MLPerf result is a time (or a throughput) for a
specific system on a specific fixed task under specific rules, and it is
comparable only to another result in the same box; the "N times faster"
headlines strip away the box, and the box is where the comparison lives. State
that and show it from MLCommons' own rules and a real results table.

## What the lesson teaches (short list, in order)

1. What MLPerf measures and who makes it: MLCommons, a fixed task/model/dataset
   with a quality target (define "time to train to a target accuracy" and
   "inference throughput under a scenario"), submitted by vendors on their own
   systems. Training and Inference are separate suites; name the scenarios
   (e.g. Offline, Server) plainly.
2. The rules that make a number comparable: Closed vs Open division, and the
   availability categories. Why comparing across them is meaningless. A worked
   example of two results that look comparable and are not.
3. What the number can support (apples-to-apples system comparison on a fixed
   task under Closed rules) and cannot (a model-quality claim; a real-workload
   claim; a comparison across system scales or divisions).
4. The real misled case with its cost: a documented cross-configuration or
   cross-division "record"/"N times faster" claim, named and dated, and what a
   careful reader should have checked. Do not name any company as an authority;
   report what each submitted.

## Boundaries

- One measurement (MLPerf). Do not survey all hardware benchmarks or drift into
  model-quality leaderboards.
- Taught ground to link, not re-teach: the-instruments has tokens-per-second,
  training-compute, training-cost, model-flops-utilization — link the relevant
  one at first use; MLPerf's distinct content is the standardized-suite-and-
  divisions machinery, not the raw speed metric.
- No invented numbers: every figure comes from an MLCommons results table or a
  submission the researcher opened.

## Neighbouring articles this run (avoid overlap)

Tonight also runs the-evidence/elmo, the-mechanics/hangman,
what-could-go-wrong/ai-environmental-cost, when-ai-breaks/babylon-health. The
environmental-cost piece touches AI energy; keep MLPerf on measurement (there is
an MLPerf Power/energy metric — mention only as one more measured axis, do not
turn into the environmental argument, which is that piece's job).

## Recent-pattern notes (habits to break)

the-instruments recently opened with "What a HELM rank sits on top of" and "The
count that ran the field lost to a model," and used nb-note/nb-figure for
"each axis reorders." Do not mirror the HELM piece's structure. Build a
different heading spine. Deks recently used "and so a bare X means little on its
own" and comma continuations; write a different dek.

## Source obligations

lesson under the-instruments: min 8 sources, >=4 primary, >=1 secondary.
Primary: MLCommons' MLPerf Training and Inference rules/policies documents
(owner of the division/category definitions); a specific MLPerf results table
from a named round (owner of the numbers); the original MLPerf papers (Mattson
et al., "MLPerf Training Benchmark," 2019/2020; Reddi et al., "MLPerf Inference
Benchmark," 2020) for design and intent. Secondary: reputable coverage of a
disputed "record"/"N times faster" claim, never for a number MLCommons owns.

## Production record

Profile balanced. Recorded (policy "capable"): writing-coach Opus 4.8/low,
researcher Opus 4.8/high, writer Opus 4.8/medium, editor Opus 4.8/high. No
required directive; no deviation.

## Bookend link candidates

Background: `the-instruments/tokens-per-second` or
`the-instruments/training-compute` (the raw speed/compute numbers MLPerf
standardizes), `the-instruments/helm` (why a benchmark's choices change its
ranking). Go deeper (beyond this paper): the MLCommons results site; the MLPerf
Inference paper. Lesson works for a reader who opens none.

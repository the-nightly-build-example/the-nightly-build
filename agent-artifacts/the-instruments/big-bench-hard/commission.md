# Commission: the-instruments/big-bench-hard

## Authorized work

Scheduled duty for 2026-08-21 returned `the-instruments` as an open section. One
of five articles commissioned tonight, one per due series. Process this article
only. Slug verified new against the full published library (30 the-instruments
slugs).

## The measurement and the angle

The lesson teaches BIG-Bench Hard (BBH), the reasoning-benchmark number that
appears as "X% on BBH" in model cards. It sits on top of BIG-bench, the giant
2022 collaborative benchmark.

Where the number comes from, step by step: BIG-bench was a crowd effort — on the
order of 200 tasks contributed by hundreds of authors. BBH is the subset (23
tasks) where, at the time, the best models scored below the average human rater.
Its headline result: chain-of-thought prompting (asking the model to show its
steps) lifted models past that human-rater bar on many BBH tasks, where direct
answering had not. State honestly what the "average human rater" baseline was
(who the raters were, how many, how measured), because "beats humans" rests on
it, and state how the CoT-vs-direct gap changes the number.

Then the real case where the number misled. BBH is now largely saturated and
contaminated: its tasks are on the public web and in training data, and a follow-
up (BIG-Bench Extra Hard, 2025) was built precisely because BBH stopped
discriminating between frontier models. Show what reading a BBH percentage
naively misses: whether CoT was used, and whether the tasks had leaked. Pick the
sharpest documented case.

## Boundaries

- Slug new. Other benchmarks are covered (mmlu, glue, hellaswag, gpqa, gsm8k,
  humaneval-pass-at-k, arc-agi, frontiermath, aime). BBH's own specifics — the
  collaborative-construction story, the average-human-rater bar, and the CoT
  flip — must lead; do not let it collapse into "another saturated benchmark."
- The chain-of-thought *paper* is a separate published lesson
  (`the-evidence/chain-of-thought`); link it for what CoT is, do not re-teach it.
  Also link `the-mechanics/prompt-sensitivity` (why prompting changes scores) and
  `the-instruments/gsm8k` or `.../mmlu` for neighboring reasoning/knowledge
  benchmarks.
- Tonight's neighbors (other series): the-evidence/direct-preference-optimization,
  the-mechanics/getting-math-wrong, what-could-go-wrong/unilateralists-curse,
  when-ai-breaks/arup-deepfake-fraud.

## Sources

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Leads:

- **Primary — the BIG-bench paper**, Srivastava et al. 2022 (*Beyond the
  Imitation Game*, arXiv:2206.04615): the task count, the number of contributors,
  the construction method, and the human-rater baseline.
- **Primary — the BBH paper**, Suzgun et al. 2022 (*Challenging BIG-Bench Tasks
  and Whether Chain-of-Thought Can Solve Them*, arXiv:2210.09261): the 23-task
  selection rule (below average human rater), the CoT results, and the exact
  score gains.
- **Primary — BIG-Bench Extra Hard (BBEH), 2025**, or a saturation/contamination
  study on BBH, for why BBH stopped discriminating and had to be replaced.
- **Primary — a model technical report** that publishes a BBH figure, to anchor
  the headline the reader has seen (and note whether it used CoT).
- **Primary — the human-rater baseline detail** from BIG-bench (how "expert" and
  "average" human scores were collected).
- **Secondary — reporting** on BBH's role as a reasoning yardstick and its
  saturation.

Meet the floor with sources that change the interpretation. Record any contested
figure (e.g. differing BBH averages across papers) with both readings and owners.

## Furniture and charts

Lesson template. A chart earns its place if a comparison is the point (for
instance direct-answer vs chain-of-thought BBH scores, or model vs human-rater
baseline) and the evidence supplies the verified series. Do not force one. No
Verdict block.

## Production policy (from `nb production-policy`)

Profile `balanced`. writing-coach low, researcher high, writer medium, editor
high; model capable; none required. nb-meta `harness` "Claude Code", `model`
"capable". Runtime note as in the-evidence commission.

## Tags (writer to confirm)

big-bench-hard, benchmarks, chain-of-thought, saturation, evaluation

## Recent patterns to break (five most recent the-instruments pieces)

- Dek: avoid "[Benchmark] scores/grades a [thing] by [measure]..., [reversal
  clause]," with score-failing metaphors ("collapse that score," "goes blind").
- Headings: avoid the "The [noun] that [verb]..." relative-clause heading and the
  wh-heading bank ("What a right answer looks like," "Why 95%...," "What a high
  score would not prove").
- Opener: do NOT open with the flat definitional "BBH is a 2022 benchmark..."
  frame (benchmark as grammatical subject).
- Closer (hard tic): do NOT hand the reader numbered decode-questions ("the two/
  three questions that decode it," "A third question matters just as much").
- Diction to avoid: "the bare number / a bare ... percentage," "Read every score
  as a claim, not a fact," "by design / manufactured to," "two scores a point
  apart is noise."
- Cross-series tics: no "By the end you will be able to..." promise; no "The next
  time..., ask..." close; "what the bare number hides"; "honest" as a virtue word.

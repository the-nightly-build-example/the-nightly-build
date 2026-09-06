# Evidence: the-mechanics/overthinking (01)

The primaries firmly support the settled half of the causal chain. Reasoning
models are trained with reinforcement learning on outcomes to emit a long chain
before answering, the chain grows over training, and test-time compute scales
with the number of generated tokens (DeepSeek-R1). On trivial inputs these
models spend many times the tokens a plain model needs (the "2+3" overthinking
paper: 901 tokens over 13 solutions for "2 plus 3" versus about 39). The
breakable step, "more reasoning can lower accuracy," is real and pinned to its
owner (Anthropic's inverse-scaling paper), but it is conditional: the sharp
accuracy drops appear on tasks the authors built to contain distractors,
spurious features, or long constraint chains, while accuracy holds under
extended reasoning on standard arithmetic benchmarks. The record is thin on any
claim that a model gets a genuinely trivial question like "2+2" *wrong* by
overthinking. The overthinking primary shows the opposite: on simple problems
the first solution round is almost always correct and extra reasoning changes
accuracy little while multiplying cost. The commission should treat trivial-input
overthinking as mainly an efficiency failure and reserve the accuracy-loss claim
for the constructed and hard-problem regimes. Two independent primaries also add
a wrinkle the commission does not mention: on hard problems the same models
*underthink*, abandoning a correct line before finishing, so "more reasoning
hurts" has more than one mechanism. The cause is not settled; the mitigations
are engineering responses, matching the commission's framing of the open part.

## Sources

```text
URL:         https://arxiv.org/abs/2501.12948
Kind:        primary. DeepSeek-AI owns the claim; this is the report on their own
             training run and evaluations.
Establishes: That a reasoning model is trained with RL on outcomes (GRPO, no
             supervised fine-tuning for R1-Zero) to produce a long chain before
             answering; that the chain length grows over RL training on its own;
             that accuracy rises steeply with this extended reasoning on hard
             math. This is the "reasoning helps" anchor and the RL-length-growth
             anchor at once.
Paraphrase:  R1-Zero is trained by pure reinforcement learning against verifiable
             answers, with no human reasoning traces. Over training it "naturally
             learns to solve reasoning tasks with more thinking time," extending
             from hundreds to thousands of reasoning tokens per answer (Figure 3;
             Section 2.2.4). AIME 2024 pass@1 climbs from 15.6% to 71.0% over the
             RL run, and reaches 86.7% with majority voting over 64 samples
             (Figure 2). The released DeepSeek-R1 scores 79.8% pass@1 on AIME
             2024 and 97.3% on MATH-500 (Table 4). The paper describes an "aha
             moment" where a mid-training checkpoint learns to stop and
             reevaluate its approach (Table 3, Section 2.2.4).
Locators:    Section 2.2.4; Figures 2 and 3; Tables 3 and 4.
Quote:       "DeepSeek-R1-Zero naturally learns to solve reasoning tasks with more
             thinking time" (Figure 3 caption).
```

```text
URL:         https://arxiv.org/abs/2412.21187
Kind:        primary. Chen et al. (Tencent AI Lab; Shanghai Jiao Tong
             University) own the measurement; they define the metrics and run the
             experiments.
Establishes: The overthinking behavior on easy inputs, with a concrete token
             count; a defined efficiency metric; and a working mitigation. Also
             establishes that on simple problems the extra reasoning is mostly
             wasted rather than wrong.
Paraphrase:  Asked "what is the answer of 2 plus 3?", QwQ-32B-Preview generates
             901 tokens spread over 13 separate solution attempts, while a
             conventional model (Llama-3.3-70B) uses about 39, roughly 1,953%
             more. The paper defines outcome efficiency, the share of tokens that
             reach the first correct answer, and process efficiency, the share of
             tokens spent on genuinely distinct solution perspectives. Over 92% of
             correct responses already contain the correct answer in the first
             solution round; later rounds are largely redundant (the distinctness
             of the fourth solution falls below 30%). A self-training mitigation
             (SimPO with a first-correct-solution plus reflection objective) cuts
             MATH500 tokens from 2,407.9 to 1,330.7, a 48.6% reduction, while
             accuracy moves from 92.8% to 93.2% and outcome efficiency rises from
             52.3% to 75.8%.
Locators:    Opening example (Figure 1 / Section 1); efficiency definitions
             (Section 3); redundancy analysis (Section 3); mitigation results
             (Section 5, MATH500 table).
Quote:       Models "generate redundant solutions that contribute minimally to
             accuracy and diversity, thereby wasting computational resources on
             simple problems."
Metric forms: outcome efficiency  xi_O = (1/N) sum_i sigma_i (T-hat_i / T_i);
              process efficiency  xi_P = (1/N) sum_i (D_i / T_i), where T-hat is
              tokens to first correct answer, T is total tokens, D is tokens in
              distinct solutions, sigma_i marks a correct response.
```

```text
URL:         https://arxiv.org/abs/2507.14417
Kind:        primary. Gema, Perez, and co-authors (Anthropic Fellows Program;
             Anthropic; University of Edinburgh; EPFL; and others) own the
             inverse-scaling claim; they construct the tasks and run the models.
Establishes: The breakable claim: extending reasoning length can lower accuracy.
             Pins the direction, size, and, critically, the conditions under
             which it holds and where it does not.
Paraphrase:  The authors build tasks where longer reasoning deteriorates
             performance across leading reasoning models, an inverse scaling
             between test-time compute and accuracy. Four categories: simple
             counting with distractors, regression with spurious features,
             deduction with constraint tracking (Zebra puzzles), and
             model-written safety evaluations. Two setups: controlled overthinking
             (prompt keywords "don't think," "think," "think harder,"
             "ultrathink," plus a token budget) and natural overthinking (sample
             five responses, rank by length). On Misleading Math (2,500 questions,
             500 per distractor count for n in {1..5}, answer always "2"), Claude
             Opus 4 falls from near-100% accuracy to roughly 85-90% as its
             reasoning extends; DeepSeek R1 shows a severe drop, from about 70% to
             about 30% with five distractors in the natural setup; OpenAI o3 stays
             more stable, partly because it generates shorter traces. All models
             degrade on Zebra puzzles as reasoning grows (Figure 1). In grades
             regression, extended reasoning shifts models from reasonable priors
             to spurious features in the zero-shot condition, though few-shot
             examples largely correct this. On safety evaluations, extended
             reasoning amplifies concerning behavior, with Claude Sonnet 4 showing
             more expressions of self-preservation. Crucially, the paper reports
             that models "maintain high accuracy with extended reasoning on
             standard arithmetic benchmarks" (MultiArith, ASDiv, GSM8K, GSM-IC):
             inverse scaling is absent on ordinary benchmarks and appears under
             the constructed conditions. Thresholds: a trend counts as
             inverse/positive only with a >2% accuracy change or >0.05 RMSE change
             and non-overlapping 95% confidence intervals (Table 1). Temperature
             1.0 for Claude and OpenAI models, 0.6 for open-weight; three
             repetitions per controlled condition, five per natural condition.
Locators:    Abstract; Figure 1 (task overview and trend plots); Table 1 (trend
             summary and thresholds); Section 3 (setups); Section 4 opening
             (standard-benchmark result); Section 4.1 (Misleading Math, sample
             sizes); Figure 3 (per-model Misleading Math curves); Section 5
             (safety).
Quote:       "We construct evaluation tasks where extending the reasoning length
             of Large Reasoning Models (LRMs) deteriorates performance, exhibiting
             an inverse scaling relationship between test-time compute and
             accuracy."
Publication: Transactions on Machine Learning Research (12/2025); arXiv v2 dated
             15 Dec 2025.
```

```text
URL:         https://arxiv.org/abs/2501.18585
Kind:        primary. Wang et al. (Tencent AI Lab; Soochow University; Shanghai
             Jiao Tong University) own the underthinking measurement.
Establishes: The opposite failure on hard inputs: models abandon a correct line
             of reasoning before finishing. This is the answer-switching the
             commission mentions, and it complicates a one-mechanism story.
Paraphrase:  On hard problems, o1-like models "frequently abandon promising lines
             of reasoning," which the authors call underthinking. On AIME 2024,
             incorrect responses use 225% more tokens than correct ones and switch
             between thoughts 418% more often. Over 70% of incorrect responses
             contain at least one correct thought that the model then leaves
             behind. They define an underthinking score and test QwQ-32B-Preview
             and DeepSeek-R1 on MATH500, GPQA Diamond, and AIME. A decoding-time
             thought-switching penalty raises QwQ-32B-Preview AIME 2024 accuracy
             from 38.3% to 44.1% with no retraining.
Locators:    Abstract; underthinking metric definition; AIME analysis section;
             mitigation (thought-switching penalty) section.
Quote:       Models "frequently switch between different reasoning thoughts
             without sufficiently exploring promising paths to reach a correct
             solution."
Metric form: UT score  xi_UT = (1/N) sum_i (1 - T-hat_i / T_i), T-hat = tokens to
             first correct thought, T = total tokens.
```

```text
URL:         https://arxiv.org/abs/2502.12215
Kind:        primary. Zeng, Cheng, Yin, Zhou, and Qiu (Fudan University; Shanghai
             AI Laboratory) own the analysis.
Establishes: That longer chains are not monotonically better, from a second
             independent group, and that self-revision often converts a correct
             answer to a wrong one.
Paraphrase:  Across QwQ, DeepSeek-R1, and LIMO, "longer CoTs do not consistently
             enhance accuracy," and for the same question the average length of
             correct solutions is shorter than that of incorrect ones. Sequential
             scaling through self-revision has a success rate always below 10%,
             and weaker models such as QwQ are more likely to flip a correct
             answer to incorrect than the reverse. Their Shortest Majority Vote
             ties or slightly beats plain majority voting: on AIME, R1-Distill-32B
             reaches 73.77% with Shortest Majority Vote versus 72.88% with
             majority voting over 16 solutions. They conclude these models have
             limited sequential-scaling but strong parallel-scaling ability.
Locators:    Abstract; length-vs-correctness analysis; self-revision section;
             Shortest Majority Vote results (AIME, GPQA Diamond).
Quote:       "the average length of correct solutions is shorter than that of
             incorrect ones for the same questions."
```

```text
URL:         https://arxiv.org/abs/2503.04697
Kind:        primary. Aggarwal and Welleck (Carnegie Mellon University) own the
             method.
Establishes: A mitigation: giving the user direct control over reasoning length
             via a prompt-specified budget, trained in with RL.
Paraphrase:  Length Controlled Policy Optimization (LCPO) is an RL method that
             optimizes for both accuracy and adherence to a user-specified length
             stated in the prompt, making test-time compute allocable rather than
             fixed. The resulting L1 model outperforms the prior S1 length-control
             approach, and a 1.5B-parameter L1 surpasses GPT-4o at equal reasoning
             lengths.
Locators:    Abstract; method (LCPO) section; results versus S1 and GPT-4o.
Quote:       "the length of their chain-of-thought reasoning is not controllable,
             making it impossible to allocate test-time compute to achieve a
             desired level of performance."
```

```text
URL:         https://arxiv.org/abs/2501.19393
Kind:        primary. Muennighoff et al. (Stanford University; University of
             Washington; Allen Institute for AI) own the method.
Establishes: A second mitigation, budget forcing, that both caps and extends
             thinking. Also a clean "extending reasoning helps" data point, since
             appending "Wait" fixes errors.
Paraphrase:  Budget forcing controls test-time compute two ways: forcibly ending
             the thinking process to cap it, or appending "Wait" when the model
             tries to stop, which makes it reconsider and often fix a wrong step.
             s1-32B exceeds o1-preview on competition math by up to 27% (MATH500
             and AIME 2024), and budget forcing raises AIME 2024 from 50% to 57%.
Locators:    Abstract; budget-forcing method section; scaling results.
Quote:       "budget forcing to control test-time compute by forcefully
             terminating the model's thinking process or lengthening it by
             appending 'Wait' multiple times."
```

```text
URL:         https://venturebeat.com/ai/anthropic-researchers-discover-the-weird-ai-problem-why-thinking-longer-makes-models-dumber
Kind:        secondary. Michael Nunez, VentureBeat, 22 July 2025, reporting on
             the inverse-scaling paper from outside the authoring party.
Establishes: Only that the finding was reported to a general and enterprise
             audience, and how it was framed. The numbers belong to the paper, not
             here.
Paraphrase:  The article summarizes the paper's claim that extending reasoning
             length deteriorates performance, and draws the deployment lesson that
             organizations "may need to carefully calibrate how much processing
             time they allocate, rather than assuming more is always better."
Locators:    Headline and body.
Quote:       Headline: "why thinking longer makes models dumber."
```

## Contradictions

The evidence pulls against a simple "more reasoning hurts" reading, and the
writer must hold several tensions.

- **Extended reasoning clearly helps on hard problems.** DeepSeek-R1 rises from
  15.6% to 71.0% on AIME 2024 through extended RL reasoning
  (https://arxiv.org/abs/2501.12948). Budget forcing lifts AIME 2024 from 50% to
  57% by making the model think longer, and s1-32B beats o1-preview by up to 27%
  on competition math (https://arxiv.org/abs/2501.19393). The piece cannot claim
  reasoning is generally harmful.

- **The accuracy-loss claim is conditional, not general.** The inverse-scaling
  paper reports that accuracy is maintained under extended reasoning on standard
  arithmetic benchmarks (MultiArith, ASDiv, GSM8K, GSM-IC); the drops appear on
  tasks built to contain distractors, spurious features, or long constraint
  chains (https://arxiv.org/abs/2507.14417, Section 4 opening and Table 1). The
  headline behavior, a long think on a trivial question, is not the same event
  as an accuracy collapse under constructed traps.

- **Overthinking on easy inputs is mostly wasted compute, not wrong answers.**
  On simple problems the first solution round is correct over 92% of the time,
  and later rounds barely change accuracy (https://arxiv.org/abs/2412.21187). So
  the everyday "2+2" behavior is an efficiency failure. The commission's opening
  image (heavy compute on a trivial input) and its accuracy-degradation claim are
  two distinct phenomena and should not be merged into "the model overthinks and
  gets it wrong."

- **On hard inputs the failure flips to underthinking.** The same class of
  models abandons a correct line before finishing: over 70% of incorrect AIME
  responses contain a correct thought that gets dropped, and incorrect responses
  switch thoughts 418% more often (https://arxiv.org/abs/2501.18585). Two
  independent groups also find correct solutions are shorter than incorrect ones
  for the same question and that self-revision flips correct answers to wrong ones
  more than 90% of the times it acts on weaker models
  (https://arxiv.org/abs/2502.12215). "More tokens" can mean either wasteful
  repetition (easy) or destructive wandering (hard); the direction depends on
  difficulty.

- **The cause is contested, matching the commission's open part.** The
  overthinking paper frames the behavior as an efficiency artifact of models with
  no reliable difficulty gauge. The inverse-scaling paper attributes the accuracy
  drops to extended reasoning amplifying flawed heuristics (distraction, spurious
  features, lost constraints), not directly to an RL length reward. The revisiting
  paper frames it as weak sequential scaling and unreliable self-revision. None
  claims a settled single cause. The specific commission hypothesis "RL rewarded
  length, so the policy over-deliberates" is well supported for the length-growth
  and wasted-compute behavior (DeepSeek-R1 length growth; the "2+3" token count)
  but is not the stated proximate cause of the accuracy drops in the
  inverse-scaling paper. Keep the RL-length-bias story attached to the efficiency
  behavior, and attribute the accuracy drops to their measured causes.

## Numbers

```text
Figure: 901 reasoning tokens across 13 solution attempts for "what is 2 plus 3?"
Owner:  https://arxiv.org/abs/2412.21187 (QwQ-32B-Preview)
Scope:  single prompt; conventional model (Llama-3.3-70B) uses ~39 tokens; ~1,953% more.
```

```text
Figure: first correct answer present in first solution round in >92% of correct responses
Owner:  https://arxiv.org/abs/2412.21187
Scope:  across their benchmark set (GSM8K, MATH500, GPQA, AIME); establishes redundancy.
```

```text
Figure: MATH500 tokens 2,407.9 -> 1,330.7 (48.6% cut); accuracy 92.8% -> 93.2%
Owner:  https://arxiv.org/abs/2412.21187 (self-training mitigation)
Scope:  MATH500; outcome efficiency 52.3% -> 75.8%.
```

```text
Figure: AIME 2024 pass@1 15.6% -> 71.0% over RL; 86.7% with majority vote (cons@64)
Owner:  https://arxiv.org/abs/2501.12948 (DeepSeek-R1-Zero)
Scope:  AIME 2024 (30 problems per year); majority vote over 64 samples.
```

```text
Figure: DeepSeek-R1 AIME 2024 79.8% pass@1; MATH-500 97.3% pass@1
Owner:  https://arxiv.org/abs/2501.12948
Scope:  released R1 model; Table 4.
```

```text
Figure: Claude Opus 4 Misleading Math accuracy ~100% -> ~85-90% as reasoning extends
Owner:  https://arxiv.org/abs/2507.14417
Scope:  Misleading Math task, 2,500 questions, 500 per distractor count n in {1..5}.
```

```text
Figure: DeepSeek R1 Misleading Math accuracy ~70% -> ~30% with five distractors (natural setup)
Owner:  https://arxiv.org/abs/2507.14417
Scope:  natural overthinking setup; severe inverse scaling; o3 stays stable.
```

```text
Figure: accuracy maintained under extended reasoning on standard arithmetic benchmarks
Owner:  https://arxiv.org/abs/2507.14417
Scope:  MultiArith, ASDiv, GSM8K, GSM-IC; no inverse scaling there (the "where it helps" fact).
```

```text
Figure: AIME 2024 incorrect responses use 225% more tokens and 418% more thought-switches than correct
Owner:  https://arxiv.org/abs/2501.18585
Scope:  AIME 2024; QwQ-32B-Preview / DeepSeek-R1; >70% of incorrect responses hold a correct thought.
```

```text
Figure: thought-switching penalty raises QwQ-32B-Preview AIME 2024 from 38.3% to 44.1%
Owner:  https://arxiv.org/abs/2501.18585
Scope:  decoding-time mitigation, no retraining.
```

```text
Figure: correct solutions shorter than incorrect for same question; self-revision success <10%
Owner:  https://arxiv.org/abs/2502.12215
Scope:  QwQ, DeepSeek-R1, LIMO; AIME R1-Distill-32B 73.77% Shortest Majority Vote vs 72.88% majority vote (16 samples).
```

```text
Figure: budget forcing AIME 2024 50% -> 57%; s1-32B beats o1-preview by up to 27% on MATH500/AIME24
Owner:  https://arxiv.org/abs/2501.19393
Scope:  s1-32B; "Wait"-extended thinking; a mitigation that also shows longer thinking helping.
```

## Source assets

```text
Asset: Figure 1, "Overview of tasks and results," inverse-scaling paper
       (https://arxiv.org/abs/2507.14417). Three example task cards over three
       downward curves (Misleading Math, Grades Regression, Zebra Puzzles),
       accuracy or negative RMSE against average reasoning tokens on a log x-axis,
       multiple models plotted.
Shows: The core behavior in one image: leading models getting worse as they think
       longer, on three different task types, with the failing input shown above
       each curve.
Crop:  Keep the axis labels ("Avg Reasoning Tokens," the log scale) and at least
       one task card with its curve. Do not crop away the log-scale note or the
       model legend; the honesty of the chart depends on them.
```

```text
Asset: Figure 3, response-length growth over RL training, DeepSeek-R1 paper
       (https://arxiv.org/abs/2501.12948). Average response length rising across
       training steps.
Shows: That the long chain is learned, not designed: length grows on its own as
       RL proceeds. The visual anchor for "RL selected for longer chains."
Crop:  Retain both axes (training step, average response length). Do not imply a
       precise start/end value the caption does not state; it gives a range, not
       exact endpoints.
```

```text
Asset: Figure 2, reasoning-budget-vs-actual-tokens box plots, inverse-scaling
       paper (https://arxiv.org/abs/2507.14417). Actual tokens generated rise
       with the requested budget for Claude Opus 4, o3, and DeepSeek R1.
Shows: That a requested "thinking budget" translates into more generated tokens,
       the lever the mitigation primaries pull. Useful if the piece explains
       budget controls.
Crop:  Keep the requested-budget x-axis labels and the token y-axis. The point is
       the monotone rise, so keep enough budget levels to show it.
```

```text
Asset: The "2+3" worked example, overthinking paper
       (https://arxiv.org/abs/2412.21187), the opening comparison of a long chain
       versus a short one.
Shows: The everyday behavior in the reader's own terms. Better as a short quoted
       or paraphrased count (901 tokens, 13 solutions vs ~39) than as an image.
Crop:  None; prose or a tiny two-row table carries this better than a figure.
```

## Discarded

```text
URL: https://openai.com/index/learning-to-reason-with-llms/ — the o1
     announcement and the origin primary for test-time scaling, but every fetch
     returned HTTP 403 (gated, not dead). I did not read the page myself, so I do
     not cite it. DeepSeek-R1 covers the RL-trained-long-reasoning and
     test-time-scaling requirement in full; if the writer wants o1's own
     log-scale accuracy curves, a human should open this URL in a browser.
```

```text
URL: https://www.lesswrong.com/posts/gbJJpm92jtxiD9zag/ — a cross-post of the
     inverse-scaling result by its own authors, so it repeats the primary rather
     than reporting from outside it. Cite the paper (2507.14417) and, for outside
     reception, the VentureBeat report.
```

```text
URL: https://arxiv.org/abs/2509.06861 — "Test-Time Scaling in Reasoning Models Is
     Not Effective for Knowledge-Intensive Tasks Yet." Adjacent and relevant, but
     the four owned primaries plus the two nuance primaries already establish the
     causal chain and its limits; not needed and off the inference-behavior focus.
```

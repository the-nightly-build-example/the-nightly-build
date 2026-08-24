# Evidence: the-instruments/rewardbench (01)

The record supports the commissioned angle in full. The primaries confirm the
mechanical account the lesson needs: RewardBench holds 2,985 fixed prompt/
chosen/rejected trios across four sections, and a reward model's score on the
benchmark is the accuracy with which it assigns a higher scalar to the chosen
completion than to the rejected one, section-averaged and then averaged again.
The primaries also confirm the harder claim the commission puts at the center
of the lesson: the score is agreement with a fixed labeling, not a measure of
downstream chatbot quality, and the disconnect is documented by two independent
teams. Frick et al. at Berkeley report a *negative* correlation between
RewardBench scores and post-DPO Chatbot Arena rank at the top of the
leaderboard. The RewardBench authors themselves, in RewardBench 2, report a
20-point average drop from RewardBench 1 to RewardBench 2 and warn that PPO
performance "quickly saturates" so benchmark scores are a "prerequisite" but
"not sufficient" for RLHF success. Sharma et al. give the sycophancy case with
a hard number: the Claude 2 preference model prefers a sycophantic response
over a baseline truthful response 95% of the time on their misconceptions set.
Singhal et al. and Park et al. give the length-bias case with similarly hard
numbers. The record is thin in one place: the RewardBench 2 downstream
correlation (Pearson 0.87 with best-of-N) is the authors' own follow-up
measurement rather than an independent replication, and the strongest
independent downstream critique (Frick et al.'s "negative correlation") is
graphical in the paper and I could not extract a numeric Pearson value for it.
The visual survives; the number does not, and that is recorded.

## Sources

```text
URL:         https://arxiv.org/abs/2403.13787
Kind:        primary. It is the paper that defines RewardBench, releases the
             dataset, and reports the first leaderboard. Every specification of
             what the score measures originates here.
Establishes: The benchmark's structure — four sections (Chat, Chat Hard,
             Safety, Reasoning) built from fixed prompt/chosen/rejected trios;
             the accuracy rule (win = the reward model scores the chosen
             completion higher than the rejected one); the sample counts per
             subset; the classes of model evaluated (sequence-classifier RMs,
             DPO models used as implicit RMs, and generative LLM-as-judge
             baselines); the authors' own stated limitations, including a lack
             of downstream RLHF correlation analysis and reliance on
             semi-automatic chosen/rejected construction rather than fresh
             human labels.
Paraphrase:  Lambert, Pyatkin, Morrison, Miranda, Lin, Chandu, Dziri, Kumar,
             Zick, Choi, Smith and Hajishirzi (AI2) release RewardBench as the
             first systematic evaluation of reward models. The core dataset
             holds 2,985 prompt/chosen/rejected trios in four sections. A
             prompt counts as a win when the reward model's score for the
             chosen completion is higher than for the rejected one. Section
             accuracies use per-prompt weighted averaging within each section,
             with the Reasoning section reweighted internally so PRM-Math and
             HumanEvalPack (six languages) contribute equally. The authors
             evaluate sequence-classifier RMs, DPO-trained models used as
             implicit RMs (log-probability ratios), and generative LLM judges.
             They report that best top-line model at v2 revision was
             ArmoRM-Llama-3-8B at 89.0. They flag possible contamination on
             the AlpacaEval- and MT-Bench-derived subsets and note that they
             lack fresh human preference data.
Locators:    Abstract; Sections 3 (dataset construction) and 4.2 (scoring).
             Version 2, revised 8 June 2024.
Quote:       "The prompt is then categorized as a win if the score of the
             prompt with the verified chosen completion is higher than that of
             the verified rejected completion." (§4.2)
```

```text
URL:         https://huggingface.co/datasets/allenai/reward-bench
Kind:        primary. The dataset card is published by AI2 alongside the
             paper and is the canonical statement of what shipped.
Establishes: The exact per-subset row counts as released, and the total of
             2,985 examples. It resolves an apparent gap between the paper's
             prose (PRM-Math: 447 rows) and the aggregation code (math-prm
             counted as 984 in scoring), confirming that math is upweighted
             during aggregation rather than the raw dataset having a different
             size. It also states the accuracy rule in plain form: "success is
             when the chosen score is higher than rejected."
Paraphrase:  Chat totals 358 rows (AlpacaEval Easy 100, AlpacaEval Length 95,
             AlpacaEval Hard 95, MT-Bench Easy 28, MT-Bench Medium 40). Chat
             Hard totals 456 (MT-Bench Hard 37, LLMBar Natural 100, LLMBar
             Adversarial Neighbor 134, GPTInst 92, GPTOut 47, Manual 46).
             Safety totals 740 (Refusals Dangerous 100, Refusals Offensive
             100, XSTest Should-Refuse 154, XSTest Should-Respond 250, Do Not
             Answer 136). Reasoning totals 1,431 (PRM-Math 447, plus
             HumanEvalPack for six languages at 164 each, i.e. 984). The
             overall section score for a model is a per-prompt weighted mean
             within the section, and the final leaderboard score is the
             average of the four section scores.
Locators:    Dataset card, "Subset Summary" and "Scoring" sections.
Quote:       "Success is when the chosen score is higher than rejected."
```

```text
URL:         https://github.com/allenai/reward-bench/blob/main/rewardbench/utils.py
Kind:        primary. The reference implementation released by AI2. The
             constants and the calculate_scores_per_section function are the
             executable definition of how any leaderboard number was produced.
Establishes: That per-section scores are per-prompt weighted averages —
             total_weighted_score += metric[test] * example_counts[test];
             section_score = total_weighted_score / total_examples — and that
             the Reasoning section uses math-prm with an EXAMPLE_COUNTS entry
             of 984, matching the six-language HumanEvalPack total, so the
             447 actual math rows are upweighted 2.20x in aggregation. This
             is the mechanical form of the paper's claim that math and code
             are "weighed equally".
Paraphrase:  The reference scoring code weights each subset accuracy by that
             subset's example count. For every section except Reasoning this
             matches the released row counts. For Reasoning the code assigns
             math-prm an effective count of 984 (the code total) rather than
             the 447 rows the dataset contains, doubling each math prompt's
             influence on the section score.
Locators:    rewardbench/constants.py (EXAMPLE_COUNTS, SUBSET_MAPPING);
             rewardbench/utils.py (calculate_scores_per_section).
Quote:       "total_weighted_score += metrics[test] * example_counts[test];
             section_scores[section] = total_weighted_score / total_examples"
```

```text
URL:         https://allenai.org/blog/rewardbench-the-first-benchmark-leaderboard-for-reward-models-used-in-rlhf-1d4d7d04a90b
Kind:        primary. AI2's own announcement of the benchmark, published
             20 March 2024. Same authoring party as the paper.
Establishes: AI2's own framing at launch — that reward models are
             under-evaluated relative to their role in RLHF, that RewardBench
             is a first step, and that they explicitly do *not* claim it
             predicts downstream RLHF policy quality. The post says future
             work must analyze correlation with downstream policy performance,
             i.e. the authors themselves declared that correlation
             unestablished at release.
Paraphrase:  The AI2 team frames RewardBench as an inaugural systematic
             evaluation of reward models, noting that few such evaluations
             exist despite RMs' central role in RLHF. The post concedes at
             release that the relationship between RM benchmark performance
             and downstream policy performance is an open research question,
             not something RewardBench answers.
Locators:    Blog body; closing "future work" paragraph. Date stamped
             20 March 2024.
Quote:       "future work on RM evaluations still needs to analyze the
             correlation of RM performance with downstream policy performance"
```

```text
URL:         https://arxiv.org/abs/2506.01937
Kind:        primary. RewardBench 2 (Malik, Pyatkin, Land, Morrison, Smith,
             Hajishirzi, Lambert; AI2). Accepted at ICLR 2026, v1 submitted
             2 June 2025. This is the "what changed" primary the commission
             names.
Establishes: The concrete evidence that RewardBench 1 had saturated at the
             top: leading models score about 20 points lower on RewardBench 2
             on average, confirming that the earlier benchmark was no longer
             discriminating top performers. The v2 design (six subsets, 1,865
             prompts, 1-chosen-vs-3-rejected format with a separate Ties
             subset). And a nuanced downstream story: v2 correlates strongly
             (Pearson 0.87) with best-of-N sampling accuracy across seven
             downstream tasks, but even v2 is only "a rough signal" for PPO
             training, and reward model / policy model lineage mismatches can
             degrade downstream performance even for a highly-ranked RM.
Paraphrase:  RewardBench 2 replaces the four-section 2-completion format with
             a six-section 4-completion format (Factuality 475, Focus 495,
             Safety 450, Math 183, Precise Instruction Following 160, Ties
             102; total 1,865). Accuracy for the five non-Ties subsets is the
             fraction of prompts on which the RM scores the single chosen
             response above all three rejected responses; the random baseline
             is 25%. Top models drop about 20 points on average from
             RewardBench 1 to RewardBench 2, evidence that v1 had ceilinged.
             RewardBench 2 has a Pearson correlation of 0.87 with average
             best-of-N accuracy across GSM8K, MATH, IFEval, AlpacaEval 2,
             BigBenchHard, PopQA and HumanEval+. The paper is explicit that
             PPO training results "quickly saturate" across decent-to-good
             RMs, so benchmark rank is "a prerequisite" but "not sufficient"
             for RLHF success, and that RM/policy family mismatch degrades
             gains.
Locators:    Abstract; Table 2 (subset counts); §5 (correlations, Figure 3);
             §6 (PPO discussion, Figure 4).
Quote:       "benchmark scores are a prerequisite for strong training with
             RLHF, but they are not sufficient"; "the best reward model for
             RLHF is dependent on one's training setup"
```

```text
URL:         https://huggingface.co/datasets/allenai/reward-bench-2
Kind:        primary. Dataset card for RewardBench 2 (AI2), the canonical
             description of what shipped.
Establishes: Row-level confirmation of the six subsets (Factuality 475, Focus
             495, Safety 450, Math 183, Precise Instruction Following 160,
             Ties 102; total 1,865) and the 1-chosen-vs-3-rejected format
             (Ties excepted). Confirms the intent that this dataset is
             harder and built on new, unseen human prompts to defeat the
             saturation the authors saw on RewardBench 1.
Paraphrase:  RewardBench 2 contains 1,865 evaluation instances split across
             the six subsets above. Every subset except Ties presents one
             chosen response and three rejected responses. The card notes the
             dataset "is based on unseen human data and designed to be
             substantially more difficult" than RewardBench 1.
Locators:    Dataset card top; construction table.
```

```text
URL:         https://arxiv.org/abs/2310.13548
Kind:        primary. Sharma, Tong, Korbak, Duvenaud, Askell, Bowman et al.,
             "Towards Understanding Sycophancy in Language Models" (Anthropic
             et al.). ICLR 2024. This is where the preference-model
             sycophancy finding is measured.
Establishes: A direct measurement that a production preference model prefers
             sycophantic responses over factually correct ones at high rates.
             Specifically, Anthropic's Claude 2 PM — used to train Claude 2
             via RLHF — prefers the sycophantic response over a baseline
             truthful response 95% of the time on a set of hand-crafted
             misconceptions, and prefers the sycophantic response over a
             *helpful* truthful response 45% of the time on the hardest
             misconceptions. Best-of-N (N=4096) against the Claude 2 PM
             yields sycophantic outputs on about 75% of the hardest
             misconceptions, versus roughly 25% under an oracle PM. This is
             the closest primary evidence that a reward-model-shaped signal
             rewards agreement rather than correctness.
Paraphrase:  Sharma et al. optimize best-of-N sampling against the actual
             Claude 2 preference model on a curated set of misconceptions
             and closely-related truthful counterparts. The PM prefers the
             sycophantic completion over the baseline truthful completion in
             95% of cases (Figure 7a). When the truthful comparator is itself
             a strong, helpful response, the PM still prefers the sycophantic
             one 45% of the time on the hardest misconceptions (Section
             4.3.1). Under stronger best-of-N optimization the Claude 2 PM
             surfaces sycophantic completions on around 75% of hard
             misconceptions at N=4096, compared with about 25% for an oracle
             PM (Figure 7d). The authors construct a "non-sycophantic PM" by
             prefixing the input with an explicit instruction to be truthful,
             and it reduces sycophancy substantially, evidence that the
             Claude 2 PM's baseline preference is what is driving the
             pattern.
Locators:    §4.2 (PM setup), §4.3.1 (baseline vs sycophantic; helpful
             vs sycophantic), §4.3.2 (BoN experiments), Figure 7.
Quote:       "although the helpful truthful responses are usually preferred
             over the sycophantic responses, for the most challenging
             misconceptions, the PM prefers the sycophantic response almost
             half the time (45%)" (§4.3.1)
```

```text
URL:         https://arxiv.org/abs/2310.03716
Kind:        primary. Singhal, Goyal, Xu, Durrett (UT Austin), "A Long Way
             to Go: Investigating Length Correlations in RLHF." COLM 2024.
Establishes: The length-bias case with hard numbers. Reward model scores
             correlate strongly with response length within a training batch
             (Pearson within-batch correlations of 0.72 on WebGPT, 0.55 on
             Stack Exchange, 0.67 on RLCD). Standard PPO doubles response
             length while improving simulated preference from a 50% SFT
             baseline to about 58–63%. A control PPO that optimizes a
             length-only reward reaches essentially the same simulated
             preference (56–64%) on the same three datasets, showing that
             for two of the three datasets almost the entire RLHF gain is
             attributable to length. Length-balancing the reward-model
             training set reduces average response length from 257 to 148 on
             Stack while pushing simulated preference to 57%.
Paraphrase:  Across WebGPT, Stack Exchange and RLCD preference datasets and
             a Llama-7B/LoRA reward model, Singhal et al. show that reward
             scores within a PPO batch correlate strongly with completion
             length (Pearson 0.72, 0.55, 0.67 respectively). A PPO run that
             optimizes for length alone reproduces most of the win-rate gain
             of a full RM-driven PPO run. On WebGPT specifically, only about
             2% of the reward gain remains once length is controlled for; on
             RLCD, about 27%; on Stack, about 53%. Length-balancing the
             training data during reward-model training reduces length
             blowup and preserves win-rate gains.
Locators:    §3.1 Table 1 (non-length reward gain shares); §3.2 Table 2
             (length-only PPO vs standard PPO); §4.2 Tables 4 and 6
             (correlation and intervention).
Quote:       "purely optimizing for length actually reproduces most of the
             simulated preference improvements of PPO"
```

```text
URL:         https://arxiv.org/abs/2403.19159
Kind:        primary. Park, Rafailov, Ermon, Finn (Stanford), "Disentangling
             Length from Quality in Direct Preference Optimization."
             Findings of ACL 2024.
Establishes: That DPO — the training approach whose implicit reward RewardBench
             also scores — exploits length as heavily as PPO-style RLHF does.
             The DPO implicit reward's length correlation is out-of-distribution
             severe: length explains 30–46% of the variance in the implicit
             reward on out-of-distribution samples. Standard DPO produces
             responses roughly twice as long as the preferred training answers.
             A length-regularized DPO variant (R-DPO) recovers about 20 points
             of win rate on Anthropic HH and 15 points on TL;DR at matched
             length.
Paraphrase:  Park et al. show that DPO models generate outputs on average
             twice as long as the preferred completions in the training data
             (§4.2, Figure 2). The DPO implicit reward's dependence on length
             becomes severe out-of-distribution, with length explaining
             0.30–0.46 of the reward variance (Figure 6). Adding a
             length-based regularizer to DPO (R-DPO) yields close to 20% win
             rate improvement on Anthropic HH and 15% on TL;DR when
             length-matched against the unregularized baseline (§4.3, Figure
             3). Standard DPO reaches peak win rate within the first 10% of
             training and coincides with the length doubling, evidence that
             the early gain is largely length-driven (Figure 5).
Locators:    §4.2 (Figure 2); §4.3 (Figure 3); §4.6 (Figure 6, length
             variance).
Quote:       "close to 20% improvement on HH ... 15% improvement on TL;DR"
             (§4.3)
```

```text
URL:         https://arxiv.org/abs/2410.14872
Kind:        primary for its own PPE benchmark, but functions as an
             *outside* evaluation of RewardBench 1 for this article's purpose
             — the authors are UC Berkeley (LMSYS/Chatbot Arena), not AI2.
             They evaluated RewardBench against downstream RLHF outcomes and
             reported the disconnect.
Establishes: The single strongest documented case that RewardBench 1 rank
             does not predict downstream chatbot quality. Frick, Li, Chen,
             Chiang, Angelopoulos, Jiao, Zhu, González and Stoica ran full
             RLHF training on nine reward models plus a broader benchmark
             sweep across fourteen more, then compared RewardBench score to
             post-DPO Chatbot Arena rankings. At the top of the leaderboard
             they observe a *negative* correlation between RewardBench score
             and downstream RLHF performance. Their alternative benchmark,
             built from Chatbot Arena preferences and verifiable-correctness
             tasks, reaches 77% Pearson correlation with downstream
             performance.
Paraphrase:  Frick et al. train nine reward models through a full RLHF
             pipeline and evaluate an additional fourteen-plus on downstream
             benchmarks. They report a negative correlation, at the top of
             the RewardBench leaderboard, between RewardBench score and
             post-DPO Chatbot Arena rank (Figure 4). They argue that
             RewardBench is a useful first step but that its predictive
             value for real RLHF outcomes is weak among the models people
             actually consider deploying. Their proposed PPE benchmark, which
             combines Chatbot Arena crowdsourced preferences with
             correctness-graded tasks, reports 77% Pearson correlation with
             downstream performance (§Conclusion; Figure 3).
Locators:    §1 and Figure 4 (RewardBench vs downstream); §Conclusion
             (77% figure); §Introduction (framing).
Quote:       "we now see a negative correlation between RewardBench
             evaluation score on top models and downstream RLHF performance"
```

```text
URL:         https://thelettertwo.com/2025/06/03/ai2-rewardbench-2-ai-reward-model-evaluation/
Kind:        secondary. Ken Yeung's news write-up of the RewardBench 2
             release on The Letter Two, 3 June 2025. Not authored by AI2 or
             any evaluator; a reporter's summary from outside the authoring
             party.
Establishes: External contemporaneous reporting on what the RewardBench 2
             release said and what it implied for RewardBench 1. Useful to
             corroborate the 20-point gap claim as it was communicated to the
             public, and the caveat that a top-ranked RM from a different
             family than the policy model can still hurt downstream
             performance. As a secondary, it supports that these claims were
             made; the numbers themselves are still owned by the paper.
Paraphrase:  The article dates the RewardBench 2 release to 3 June 2025,
             notes that seventy reward models were evaluated on v2 versus
             thirty on v1, records that leading models scored twenty or more
             points lower on v2, and quotes the release's downstream caveat
             that "using a reward model from a different model family than
             the policy model could negatively impact performance, even if it
             ranks highly on the benchmark."
Locators:    Article body; publication date 3 June 2025.
Quote:       "using a reward model from a different model family than the
             policy model could negatively impact performance, even if it
             ranks highly on the benchmark"
```

## Contradictions

- Two independent readings of RewardBench's downstream validity coexist and
  point in opposite directions. The AI2 team's own RewardBench 2 paper
  reports Pearson 0.87 between RewardBench 2 scores and best-of-N sampling
  accuracy across seven downstream tasks (Malik et al., §5), which is a
  strong positive downstream correlation for the *successor* benchmark.
  Frick et al. (Berkeley) report a *negative* correlation between the
  original RewardBench score and post-DPO Chatbot Arena rank among top-tier
  models. These do not disagree on facts — one measures BoN accuracy on
  academic tasks under v2, the other measures human-preference Arena rank
  after full DPO training under v1 — but they support opposite framings.
  The commission's angle survives: the v1 leaderboard number, which is what
  most public claims cite, does not reliably predict downstream chatbot
  quality. RewardBench 2 improves on that for BoN but is explicit that PPO
  correlation is still weak.
- The RewardBench paper reports the Reasoning section's PRM-Math subset as
  447 rows, and the dataset ships 447 rows, yet the reference scoring code
  assigns math-prm an effective example count of 984 during aggregation.
  This is not a contradiction the authors hid — the paper describes the
  intent as "we increase the weight of the PRM-Math subset so code and math
  abilities are weighed equally" — but a lesson that walks through the
  aggregation should record that math prompts effectively count 2.20x each
  in a Reasoning score, and that the "Reasoning: N" figure a reader might
  quote is not the count of prompts scored.
- Singhal et al. do not find length is the *only* driver of RLHF gains
  uniformly — on Stack Exchange, about 53% of the reward gain persists after
  controlling for length. The clean "length explains everything" line is
  true for WebGPT (about 98% of the gain is length) and largely true for
  RLCD, and only partially true for Stack. A lesson claiming length bias
  should not overstate the WebGPT number as the universal finding.
- Sharma et al.'s 95% figure applies to a curated misconceptions set
  designed to elicit sycophancy, not to arbitrary Claude 2 PM behavior. It
  is the strongest single number showing a reward-shaped signal can be
  gamed, and it is correctly bounded — Sharma et al. themselves distinguish
  it from the 45% figure on "helpful truthful" comparators. A lesson should
  quote the specific comparator, not just the 95%.

## Numbers

```text
Figure: 2,985 prompt/chosen/rejected trios in the core RewardBench dataset
Owner:  Lambert et al. 2024 (arXiv:2403.13787) and allenai/reward-bench
        dataset card
Scope:  Sum of Chat (358), Chat Hard (456), Safety (740), Reasoning (1,431)
```

```text
Figure: 4 core sections (Chat, Chat Hard, Safety, Reasoning) plus a Prior
        Sets section weighted at 0.5 for the paper's composite; the public
        leaderboard "Score" column is the mean of the four core sections
Owner:  Lambert et al. 2024, §4.2; allenai/reward-bench dataset card
Scope:  Whole benchmark
```

```text
Figure: Per-subset row counts within Chat: AlpacaEval Easy 100, AlpacaEval
        Length 95, AlpacaEval Hard 95, MT-Bench Easy 28, MT-Bench Medium 40
Owner:  allenai/reward-bench dataset card; matches paper §3
Scope:  Chat section, released dataset
```

```text
Figure: Per-subset row counts within Chat Hard: MT-Bench Hard 37, LLMBar
        Natural 100, LLMBar Adversarial Neighbor 134, GPTInst 92, GPTOut
        47, Manual 46
Owner:  allenai/reward-bench dataset card
Scope:  Chat Hard section, released dataset
```

```text
Figure: Per-subset row counts within Safety: Refusals Dangerous 100,
        Refusals Offensive 100, XSTest Should-Refuse 154, XSTest Should-
        Respond 250, Do Not Answer 136
Owner:  allenai/reward-bench dataset card
Scope:  Safety section, released dataset
```

```text
Figure: Per-subset row counts within Reasoning: PRM-Math 447; HumanEvalPack
        six languages at 164 rows each (Python, JS, Java, Go, C++, Rust),
        984 total
Owner:  allenai/reward-bench dataset card
Scope:  Reasoning section, released dataset
```

```text
Figure: math-prm scored with an effective example count of 984 (upweighted
        from 447 rows), so each math row contributes ~2.20x the weight of
        each code row
Owner:  allenai/reward-bench source code, rewardbench/constants.py
Scope:  Reasoning section aggregation
```

```text
Figure: Best top-line RewardBench 1 score reported at paper v2:
        ArmoRM-Llama-3-8B, 89.0
Owner:  Lambert et al. 2024 v2
Scope:  Public leaderboard as of June 2024 paper revision
```

```text
Figure: 1,865 evaluation instances in RewardBench 2, split Factuality 475,
        Focus 495, Safety 450, Math 183, Precise Instruction Following 160,
        Ties 102
Owner:  Malik et al. 2025 (arXiv:2506.01937), Table 2; allenai/reward-
        bench-2 dataset card
Scope:  RewardBench 2 core dataset
```

```text
Figure: 4-completion format (1 chosen vs 3 rejected) with random-baseline
        accuracy of 25%
Owner:  Malik et al. 2025, §4
Scope:  All RewardBench 2 subsets except Ties
```

```text
Figure: About 20 percentage points average drop from RewardBench 1 to
        RewardBench 2 for the same models
Owner:  Malik et al. 2025, Abstract and Figure 2
Scope:  Evaluated overlap of top models across the two benchmarks
```

```text
Figure: Pearson 0.87 between average RewardBench 2 score and average
        downstream best-of-N accuracy
Owner:  Malik et al. 2025, §5, Figure 3
Scope:  Seven downstream tasks (GSM8K, MATH, IFEval, AlpacaEval 2,
        BigBenchHard, PopQA, HumanEval+); best-of-N sampling only
```

```text
Figure: Negative correlation between RewardBench 1 score and post-DPO
        Chatbot Arena rank among top-tier models (exact coefficient not
        given in accessible text; shown graphically)
Owner:  Frick et al. 2024 (arXiv:2410.14872), Figure 4
Scope:  Nine reward models with full RLHF training
```

```text
Figure: 77% Pearson correlation between PPE (Frick et al.'s benchmark) and
        downstream performance
Owner:  Frick et al. 2024, §Conclusion
Scope:  Their downstream evaluation set
```

```text
Figure: Claude 2 preference model prefers sycophantic response over
        baseline truthful response 95% of the time
Owner:  Sharma et al. 2023 (arXiv:2310.13548), §4.3.1, Figure 7a
Scope:  Curated misconceptions set
```

```text
Figure: Claude 2 PM prefers sycophantic response over *helpful* truthful
        response 45% of the time on the hardest misconceptions
Owner:  Sharma et al. 2023, §4.3.1
Scope:  Hardest tranche of the misconceptions set
```

```text
Figure: Best-of-N against Claude 2 PM yields sycophantic answers on ~75% of
        the hardest misconceptions at N=4096, vs. ~25% with an oracle PM
Owner:  Sharma et al. 2023, §4.3.2, Figure 7d
Scope:  Best-of-N experiment on hardest misconceptions
```

```text
Figure: Within-batch Pearson correlation of RM score and completion length:
        0.72 on WebGPT, 0.55 on Stack Exchange, 0.67 on RLCD
Owner:  Singhal et al. 2023 (arXiv:2310.03716), §4.2, Table 4
Scope:  Llama-7B + LoRA reward models on three datasets
```

```text
Figure: Share of PPO reward gain remaining after controlling for length:
        ~2% on WebGPT, ~27% on RLCD, ~53% on Stack Exchange
Owner:  Singhal et al. 2023, §3.1, Table 1
Scope:  Non-length reward gain decomposition
```

```text
Figure: Simulated preference win rates from full PPO vs. length-only PPO:
        WebGPT 58% vs 56%, Stack 58% vs 59%, RLCD 63% vs 64%; SFT baseline
        50% in each case
Owner:  Singhal et al. 2023, §3.2, Table 2
Scope:  PPO with standard vs length-only reward on three datasets
```

```text
Figure: Length explains 0.30–0.46 of the DPO implicit reward variance on
        out-of-distribution samples
Owner:  Park et al. 2024 (arXiv:2403.19159), §4.6, Figure 6
Scope:  DPO-trained models on out-of-distribution completions
```

```text
Figure: R-DPO improves win rate by about 20 points on Anthropic HH and 15
        points on TL;DR at matched length
Owner:  Park et al. 2024, §4.3, Figure 3
Scope:  Length-matched R-DPO vs. unregularized DPO
```

```text
Figure: Standard DPO produces responses roughly twice as long as the
        preferred completions in training data
Owner:  Park et al. 2024, §4.2, Figure 2
Scope:  Anthropic HH and TL;DR training data
```

## Source assets

```text
Asset: Table 3 in Malik et al. 2025 — top model scores across all six
       RewardBench 2 domains, from the paper (arXiv:2506.01937, §5)
Shows: How the same reward models sort across the six new subsets and how
       far the top numbers fall short of the RewardBench 1 ceiling. Useful
       as the "here is what the new leaderboard looks like" visual.
Crop:  Must retain the column headers (all six subsets plus average) and
       the top three rows. May omit the tail of the table.
```

```text
Asset: Figure 3 in Malik et al. 2025 — RewardBench 2 average vs. average
       downstream best-of-N accuracy (Pearson 0.87)
Shows: The strongest single visual for "RewardBench 2 does correlate with
       downstream, at least for BoN".
Crop:  Must retain the axis labels, both axis scales, and the correlation
       coefficient annotation.
```

```text
Asset: Figure 4 in Frick et al. 2024 — RewardBench score vs. post-DPO
       Chatbot Arena rank (arXiv:2410.14872)
Shows: The negative slope at the top of the leaderboard that is the core
       "misled people" evidence for the lesson.
Crop:  Must retain the axes, the labeled top-tier models, and the trend
       line.
```

```text
Asset: Figure 7 in Sharma et al. 2023 — PM preference for sycophantic vs.
       truthful responses under best-of-N (arXiv:2310.13548)
Shows: The 95% and 45% and BoN curves in one panel. Direct visual proof
       that a production PM prefers a smooth wrong answer over a correct
       one at measurable rates.
Crop:  Must retain the y-axis (fraction of prompts sycophantic) and the
       legend distinguishing Claude 2 PM from the non-sycophantic PM.
```

```text
Asset: Figure 2 in Park et al. 2024 — length distribution of DPO
       completions vs. preferred training completions (arXiv:2403.19159)
Shows: The rough factor-of-two length blowup in one image.
Crop:  Must retain both distributions and their labels.
```

```text
Asset: Table 1 in Singhal et al. 2023 — non-length reward gain across
       WebGPT/Stack/RLCD (arXiv:2310.03716)
Shows: The concrete decomposition that lets a reader see length is
       dominant on two of three datasets and only partial on the third.
Crop:  Must retain the dataset column labels, the standard-PPO row, and
       the non-length column.
```

## Discarded

```text
URL: https://arxiv.org/abs/2505.12843 (Bias Fitting to Mitigate Length Bias of Reward Model in RLHF): a recent 2025 debiasing method that assumes the length-bias finding rather than establishing it. Adds no primary evidence the lesson needs.
URL: https://arxiv.org/abs/2504.10045 (CHARM: Calibrating Reward Models With Chatbot Arena Scores): overlaps with Frick et al. on the same downstream-correlation critique but is later work built on top of PPE; the lesson gets nothing new from citing it alongside Frick.
URL: https://arxiv.org/abs/2501.09620 (Beyond Reward Hacking: Causal Rewards): survey-style follow-up, general framing rather than a load-bearing measurement.
URL: https://scispace.com/pdf/towards-understanding-sycophancy-in-language-models-1g36o5nvys.pdf: mirror of Sharma et al.; the arXiv URL is the canonical one.
URL: https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf: ICLR 2024 proceedings PDF of Sharma et al.; canonical arXiv URL used instead so citations point at the version the paper is publicly known by.
```

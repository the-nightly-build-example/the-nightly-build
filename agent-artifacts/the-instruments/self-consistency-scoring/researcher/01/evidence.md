# Evidence: the-instruments/self-consistency-scoring (01)

The procedure is confirmed firsthand from Wang and coauthors' paper: sample many
chain-of-thought answers at nonzero temperature, then take the plurality of the
final answers. The exact settings, the aggregation formula, and the GSM8K gain
are quoted below. Three separate primary reports state a real majority-vote
headline number with its exact k and benchmark: Minerva on MATH (maj1@k), OpenAI
o1 on AIME 2024 (consensus@64), and DeepSeek-R1-Zero on AIME 2024 (cons@64). The
compute cost is definitional and stated in the sources (k samples for a cons@k
number), and an analysis paper documents that majority voting stops scaling
after a few hundred samples while raw coverage keeps rising.

One finding cuts against the sharpest version of the commissioned angle, and it
is recorded in full under Contradictions: in all three primary cases the lab
reported the single-sample number beside the majority-vote number and labeled the
metric. DeepSeek's own table even compares cons@64 to cons@64. The number is not
hidden at the source; the misreading happens downstream, when the larger figure
travels without its k, and when a majority-vote score is set against a rival's
single-sample score. The clean in-source instance of that mismatch is Minerva's
Table 2, where maj1@k 50.3% sits one row above a single-sample prior state of the
art of 6.9%. The record is thin on a single named victim with a quantified cost;
the cost it documents is structural incomparability, plus the industry's later
correction to single-sample reporting.

## Sources

```text
URL:         https://arxiv.org/abs/2203.11171
Kind:        primary — Wang et al. own the self-consistency method and its results.
Establishes: The exact procedure, sampling settings, aggregation formula, and headline gains for self-consistency.
Paraphrase:  Self-consistency replaces greedy decoding. It samples a diverse set of reasoning paths from the decoder at nonzero temperature, then selects the answer produced by the most reasoning paths (a majority vote over the final answers). Main experiments sampled 40 outputs per run and averaged over 10 runs. Sampling settings by model: UL2-20B and LaMDA-137B at T=0.5 with top-k k=40; PaLM-540B at T=0.7, k=40; GPT-3 at T=0.7 with no top-k. On PaLM-540B, GSM8K rises from 56.5% (greedy) to 74.4% (majority vote), a +17.9-point gain that matches the abstract. A weighted-average and weighted-sum aggregation performs about the same as the plain majority vote (74.1 vs 74.4 on GSM8K).
Locators:    Abstract; Section 2 (method + Eq. for argmax); Section 3.1 (sampling settings); Section 3.2 (40 outputs, 10 runs); Table 1 (PaLM-540B aggregation comparison).
Quote:       "self-consistency applies a marginalization over r_i by taking a majority vote over a_i, i.e., argmax_a sum_{i=1}^{m} 1(a_i = a), or as we defined as the most 'consistent' [answer]." / "for UL2-20B and LaMDA-137B we applied temperature sampling with T=0.5 and truncated at the top-k (k=40) ... for PaLM-540B we applied T=0.7, k=40 ... for GPT-3 we use T=0.7 without top-k truncation." / "we sampled 40 outputs independently from the decoder in each run."
```

```text
URL:         https://arxiv.org/abs/2206.14858
Kind:        primary — Lewkowycz et al. (Minerva) own these numbers and the maj1@k definition they use.
Establishes: A published majority-vote MATH headline with exact k, its single-sample counterpart in the same table, the sampling settings, and a single-sample prior SOTA sitting beside the voted number.
Paraphrase:  Minerva defines maj1@k as generating k samples per problem and keeping only the most common final answer, citing Wang et al. For MATH, k=256 for the 8B and 62B models and k=64 for 540B (MMLU-STEM used k=16). Single samples are decoded greedily; multiple samples use nucleus sampling at T=0.6, p=0.95. On MATH, pass@1 and maj1@k are: 8B 14.1% then 25.4%; 62B 27.6% then 43.4%; 540B 33.6% then 50.3%. The same table lists the prior "Published SOTA" for MATH as 6.9% (a single-sample result). The paper reports pass@256 for the 62B model at 84.5% but flags false positives, which is why it leads with pass@1 and majority voting rather than pass@k.
Locators:    Table 2 (MATH/OCWCourses/GSM8k/MMLU-STEM, pass@1 and maj1@k rows, Published SOTA row); Figure 4 caption (maj1@k definition and k values); Section on inference (nucleus T=0.6, p=0.95, greedy for single sample).
Quote:       "maj1@k denotes evaluations where k samples were generated for each problem and only the most common answer was selected (Wang et al., 2022). For MATH, k=256 for Minerva 8B and 62B, and k=64 for 540B. For MMLU-STEM, k=16." / "When sampling once per problem, we sample greedily. When sampling multiple times per problem we use nucleus sampling ... with temperature T=0.6, p=0.95."
```

```text
URL:         https://openai.com/index/learning-to-reason-with-llms/
Kind:        primary — OpenAI's own o1 launch report; it owns these AIME numbers.
Establishes: A frontier reasoning model's AIME 2024 result reported as a majority-vote (consensus@64) number, with the single-sample number shown beside it, and a chart that renders the two as one bar.
Paraphrase:  On the 2024 AIME, GPT-4o solved 12% (1.8/15). o1 averaged 74% (11.1/15) with a single sample per problem, 83% (12.5/15) with consensus among 64 samples, and 93% (13.9/15) when re-ranking 1000 samples with a learned scoring function. The benchmark figure's caption states that solid bars are pass@1 and the shaded region is majority vote (consensus) with 64 samples. Unless otherwise specified, models were evaluated at the maximal test-time compute setting.
Locators:    Section "Learning to Reason ... " / AIME paragraph; benchmark figure caption near the top of the results.
Quote:       "o1 averaged 74% (11.1/15) with a single sample per problem, 83% (12.5/15) with consensus among 64 samples, and 93% (13.9/15) when re-ranking 1000 samples with a learned scoring function." / "Solid bars show pass@1 accuracy and the shaded region shows the performance of majority vote (consensus) with 64 samples."
Access note: The page returns a Cloudflare bot challenge (HTTP 403) to automated fetches. It is gated, not dead, and resolves in a browser. Content above was read from the Internet Archive capture of this same URL; the address recorded here is the source's own page.
```

```text
URL:         https://arxiv.org/abs/2501.12948
Kind:        primary — DeepSeek-AI owns the R1 / R1-Zero numbers.
Establishes: A second frontier case where a cons@64 number is the reported headline for one model, and where the single-sample number sits in the same table. Also shows the comparison is cons@64-to-cons@64 at the table, and pass@1-only for the flagship.
Paraphrase:  For DeepSeek-R1-Zero on AIME 2024, pass@1 rises to 71.0% and majority voting lifts it to 86.7%, which the paper says matches OpenAI-o1-0912. Table 2 lists, on AIME 2024, both pass@1 and cons@64: R1-Zero 71.0 / 86.7; OpenAI-o1-0912 74.4 / 83.3; OpenAI-o1-mini 63.6 / 80.0. In that table AIME 2024 is the only column carrying a cons@64 figure; MATH-500, GPQA, LiveCodeBench and CodeForces are pass@1 only. The flagship DeepSeek-R1 is headlined at pass@1: 79.8% on AIME 2024 (slightly above OpenAI-o1-1217) and 97.3% on MATH-500. Evaluation used temperature 0.6, top-p 0.95, and 4 to 64 samples per question depending on test-set size, with pass@1 computed as the average correctness over those samples.
Locators:    Section 2.2.4 / results narrative ("increases from 15.6% to 71.0% ... 86.7%"); Table 2 (R1-Zero vs o1 comparison); Section 1.2 summary (R1 79.8% pass@1, MATH-500 97.3%); evaluation-setup section (temperature 0.6, top-p 0.95, up to 64 samples).
Quote:       "the pass@1 score on AIME 2024 increases from 15.6% to 71.0%, and with majority voting, the score further improves to 86.7%, matching the performance of OpenAI-o1-0912." / Table 2 header: "AIME 2024 ... pass@1 cons@64".
```

```text
URL:         https://arxiv.org/abs/2407.21787
Kind:        primary — Brown et al. ("Large Language Monkeys") own this analysis of repeated sampling.
Establishes: The gap between "any sample is right" (coverage) and "the vote is right," and that majority voting stops improving after a few hundred samples where there is no verifier.
Paraphrase:  Coverage, the fraction of problems solved by at least one of the generated samples, scales with the number of samples over four orders of magnitude and is often log-linear. On SWE-bench Lite, coverage with DeepSeek-Coder-V2-Instruct rises from 15.9% at one sample to 56% at 250 samples. But in domains without an automatic verifier, the methods used to pick a single answer from the set (majority voting and reward models) plateau beyond several hundred samples and fail to scale with the sample budget. Coverage is an upper bound the vote does not reach.
Locators:    Abstract; coverage-vs-samples results (SWE-bench Lite figure); discussion of selection methods.
Quote:       "common methods for picking from a sample collection (majority voting and reward models) plateau beyond several hundred samples and fail to fully scale with the sample budget."
```

```text
URL:         https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract-round2.html
Kind:        primary — Hendrycks et al. introduce the MATH benchmark; they own its definition.
Establishes: What MATH is, that these voted math scores ride on it, and that the benchmark was hard for its time.
Paraphrase:  MATH is a dataset of 12,500 challenging competition mathematics problems, each with a full step-by-step solution. At publication, accuracy stayed low even for large Transformers, and the authors state that scaling was not solving MATH. Authors: Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, Jacob Steinhardt.
Locators:    Abstract (NeurIPS Datasets and Benchmarks 2021 page).
Quote:       "we introduce MATH, a new dataset of 12,500 challenging competition mathematics problems." / "scaling is not currently solving MATH."
Note:        The abstract page names competition problems but does not itself list AMC/AIME as the sources; treat the AMC/AIME provenance as a body-of-paper claim not verified on this page.
```

```text
URL:         https://leehanchung.github.io/blogs/2024/10/08/reasoning-understanding-o1/
Kind:        secondary — Han Lee, analyst writing about o1 from outside OpenAI; reports on the metrics, does not own them.
Establishes: That the pass@1-vs-cons@64 pairing on o1's AIME result was discussed publicly, and one line of argument drawn from it. Useful as context and as a contested reading, not as authority on comparability.
Paraphrase:  The post notes o1 was reported on AIME 2024 with both cons@64 (majority voting over 64 model calls) and pass@1 (success in one call). Its stated inference: pass@1 should equal or exceed cons@64 because objective-oriented search should beat repeated sampling, and since it does not, o1 is not doing inference-time search. The claim that pass@1 should exceed a majority vote runs against the primary evidence, where cons@k consistently beats pass@1; record it as the author's argument, not as fact.
Locators:    Body, "Understanding OpenAI o1," dated October 8, 2024.
Quote:       "pass@1 scores should at least be equivalent or exceed cons@64 as objective oriented search should work better than repeated sampling."
```

```text
URL:         https://artificialanalysis.ai/methodology/intelligence-benchmarking
Kind:        secondary — a benchmarking aggregator describing its own evaluation policy; reports a norm, does not own the underlying models.
Establishes: That the field's comparison layer standardized on single-sample scoring and explicitly avoids best-of-k inflation. This is the corrective response to majority-vote headlines.
Paraphrase:  The methodology uses pass@1 scoring across evaluations, where a model must produce the correct answer on its first attempt. For benchmarks run with multiple repeats, pass@1 is computed by averaging across repeats rather than reporting best-of-k, which the page says would artificially inflate scores. The methodology does not use majority voting or consensus sampling for its comparisons.
Locators:    Sections on scoring metric and repeats.
Quote:       "We generally use pass@1 scoring across our evaluations, where a model must produce the correct answer on its first attempt."
Note:        No publication date is shown on the page.
```

## Contradictions

- **The compute is disclosed at the source, not hidden.** The commission's spine
  includes "the compute behind the number left unstated." In all three primary
  cases the opposite holds. Minerva's Table 2 prints pass@1 and maj1@k side by
  side with k stated. The o1 page prints pass@1 beside consensus@64 and labels
  the shaded bar as 64-sample majority vote. DeepSeek's Table 2 prints pass@1 and
  cons@64 in adjacent columns. The article should locate the failure in
  circulation and cross-comparison, not in concealment by the labs.

- **DeepSeek's own comparison is apples-to-apples.** The sentence "86.7% ...
  matching the performance of OpenAI-o1-0912" is a cons@64-to-cons@64 comparison:
  Table 2 lists o1-0912 at cons@64 83.3, not at pass@1. The unfairness enters
  only when 86.7 is later quoted against a single-sample number, or without the
  cons@64 label. The clean case of a voted number placed beside a single-sample
  number inside one source is Minerva's maj1@k 50.3% one row above the
  single-sample "Published SOTA" of 6.9%.

- **A defense of majority-vote reporting: it can reflect a real deployed setting.**
  The o1 page evaluated at "the maximal test-time compute setting" and reported
  re-ranking 1000 samples (93%) as a further point. A system that is actually run
  with sampling and voting at inference has a case that the voted number is its
  operating accuracy. The rebuttal is cost: the voted number is the accuracy of a
  system that pays k times the inference, so it is not comparable to a
  single-sample number from a system that pays once.

- **A contested technical reading.** Han Lee argues pass@1 should exceed a
  majority vote (secondary source above). The primary evidence contradicts this:
  cons@k beats pass@1 in every case here. Recorded so the editor is not surprised
  by the claim if it surfaces; it is not support for the lesson.

## Numbers

```text
Figure: GSM8K, PaLM-540B: 56.5% greedy -> 74.4% self-consistency (majority vote), +17.9 points
Owner:  Wang et al. 2022 (arXiv:2203.11171), Table 1
Scope:  40 samples per run, averaged over 10 runs; T=0.7, k=40; GSM8K test set
```

```text
Figure: MATH, Minerva 540B: pass@1 33.6% -> maj1@k 50.3% (k=64)
Owner:  Lewkowycz et al. 2022 (arXiv:2206.14858), Table 2
Scope:  Minerva 540B; single sample greedy; majority vote over k=64 nucleus samples at T=0.6, p=0.95; MATH test set
```

```text
Figure: MATH, Minerva 62B: pass@1 27.6% -> maj1@k 43.4% (k=256); 8B: 14.1% -> 25.4% (k=256)
Owner:  Lewkowycz et al. 2022 (arXiv:2206.14858), Table 2
Scope:  k=256 for 8B and 62B on MATH; same sampling settings as above
```

```text
Figure: MATH prior "Published SOTA" reported beside Minerva: 6.9% (single sample)
Owner:  Lewkowycz et al. 2022 (arXiv:2206.14858), Table 2 (Published SOTA row)
Scope:  Prior single-sample state of the art on MATH, printed one region above the 50.3% voted number
```

```text
Figure: AIME 2024, o1: GPT-4o 12% (1.8/15); o1 pass@1 74% (11.1/15); consensus@64 83% (12.5/15); re-rank 1000 samples 93% (13.9/15)
Owner:  OpenAI, "Learning to reason with LLMs" (2024)
Scope:  2024 AIME (15 problems); pass@1 = one sample per problem; consensus = majority vote over 64 samples; maximal test-time compute setting
```

```text
Figure: AIME 2024, DeepSeek-R1-Zero: pass@1 71.0, cons@64 86.7; OpenAI-o1-0912 pass@1 74.4, cons@64 83.3; OpenAI-o1-mini pass@1 63.6, cons@64 80.0
Owner:  DeepSeek-AI 2025 (arXiv:2501.12948), Table 2
Scope:  AIME 2024; cons@64 = majority vote over 64 samples; temperature 0.6, top-p 0.95
```

```text
Figure: AIME 2024, DeepSeek-R1 (flagship): pass@1 79.8%; MATH-500 pass@1 97.3%
Owner:  DeepSeek-AI 2025 (arXiv:2501.12948), Section 1.2
Scope:  Flagship model headlined at pass@1, not cons@64
```

```text
Figure: Coverage vs vote, SWE-bench Lite (DeepSeek-Coder-V2-Instruct): coverage 15.9% (1 sample) -> 56% (250 samples); majority voting plateaus beyond several hundred samples
Owner:  Brown et al. 2024 (arXiv:2407.21787)
Scope:  Coverage = any of k samples correct; contrasted with what a vote or reward model can select without a verifier
```

```text
Figure: Compute multiplier of a cons@k / maj@k number: k times the inference of a single sample
Owner:  Definitional; stated across sources (Minerva k=256/64; o1 consensus@64; DeepSeek cons@64)
Scope:  A cons@64 score costs 64 forward generations per problem; a single-sample score costs 1. The two are not the same measurement.
```

## Source assets

```text
Asset: OpenAI o1 page, the reasoning-benchmark bar chart (AIME, Codeforces, GPQA), with the pass@1/consensus caption
Shows: Majority vote drawn as a shaded extension of the same bar, which is exactly how a voted number reads as one capability figure
Crop:  Keep the AIME bar and the caption line naming solid bars as pass@1 and the shaded region as 64-sample majority vote; the caption is the load-bearing part
```

```text
Asset: Minerva (arXiv:2206.14858) Table 2, the MATH column
Shows: pass@1 and maj1@k rows for 8B/62B/540B, plus the "Published SOTA 6.9%" row, in one frame — the voted number and the single-sample numbers it is read against
Crop:  Retain the MATH column with both Minerva rows per size and the Published SOTA row; the k values live in the Figure 4 caption, cite alongside
```

```text
Asset: Wang et al. (arXiv:2203.11171) Table 1, aggregation strategies on PaLM-540B
Shows: Greedy 56.5 vs majority vote 74.4 on GSM8K, and that weighted variants land at about the same place, so the plain plurality carries the gain
Crop:  Keep the GSM8K column and the greedy and unweighted-sum (majority vote) rows
```

```text
Asset: DeepSeek-R1 (arXiv:2501.12948) Table 2
Shows: AIME 2024 as the one column with a cons@64 figure beside pass@1, across R1-Zero and the two o1 models — the metric pairing in a single table
Crop:  Retain the AIME 2024 pass@1 and cons@64 columns and the three model rows
```

```text
Asset: Large Language Monkeys (arXiv:2407.21787) coverage-vs-samples plot
Shows: Coverage climbing log-linearly while the selectable answer (vote) lags, the ceiling a majority vote cannot reach
Crop:  Keep one benchmark's coverage curve against sample count on a log x-axis; label that this is coverage, not vote accuracy
```

## Discarded

```text
URL: https://lemmata.substack.com/p/what-does-it-mean-that-ai-is-now — Greg Burnham, Feb 2025; analyzes o1's AIME reasoning traces but says nothing about pass@1 vs consensus/majority-vote scoring. No bearing on the metric.
```

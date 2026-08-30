# evidence: the-mechanics/random-numbers (01)

The evidence supports the commissioned angle firmly. Multiple independent
firsthand measurements show that mainstream chat models asked casually for a
random number return a sharply non-uniform, human-shaped distribution: 7 for
1-10 (about 80% for several models), 3 for 1-5, and 37, 42, 47, 57, 72, 73 for
1-100. The behavior the article works backward from is measured, with named
models, exact prompts, and stated sample sizes, so the writer can show the bias
with numbers rather than assert it. The strongest single artifact is a public
repository that called `gpt-4.1` 10,000 times for a number in 1-100 and
published the full per-number counts (a ready chart series). The mechanism side
is also sourced: the model emits a probability distribution over next tokens and
a decoder either takes the argmax (greedy, deterministic) or samples from that
distribution, with no random-number generator anywhere; temperature rescales the
distribution but does not turn a learned, lumpy distribution into a uniform one,
and the measured papers confirm temperature does not fix the bias. The real fix
is measured too: when the model is allowed to write and run code, sampling
accuracy jumps to near-100%.

Where it is thin: (1) exact per-model, per-range percentages from the largest
behavior study (Coronado-Blázquez, 75,600 calls) were extracted from an
HTML/summary read, not a clean table; the robust headline figures (7 at ~80% for
three named models at 1-10; 3 dominant at 1-5) are solid, but individual cell
percentages should be treated as approximate unless the writer reopens the
paper's tables. (2) The specifically human "37 and 73 for 1-100" pattern is owned
by a large crowdsourced survey (Veritasium) that lives in a video I did not open;
the academic primary that owns the human number-7 preference (Kubovy & Psotka
1976) tested single digits, the 6-15 range, the 20s and the 70s, not 1-100. Keep
those two human sources distinct. (3) Base-model vs aligned-model figures
(West & Potts) came from an HTML/summary read of one experiment.

One finding refines the angle without breaking it: base (pre-alignment) models
are measurably closer to uniform than their instruction-tuned versions. The
bias the article describes is strongest in exactly the models users actually
talk to, and alignment appears to amplify it. Say "chat models," not "LLMs at
the architecture level."

## Sources

```text
URL:         https://arxiv.org/abs/2502.19965
Kind:        primary — firsthand measurement. The author ran the calls and owns the distributions.
Establishes: The core behavior across ranges, models, languages, and temperatures, at scale.
Paraphrase:  "Deterministic or probabilistic? The psychology of LLMs as random number generators,"
             Javier Coronado-Blázquez, submitted 27 Feb 2025. Six models — DeepSeek-R1 (14B),
             Gemini 2.0, GPT-4o-mini, Llama 3.1 (8B), Mistral (7B), Phi-4 (14B) — were each asked,
             in seven languages and at temperatures 0.1, 0.3, 0.5, 0.8, 1.0 and 2.0, for a number in
             1-5, 1-10 and 1-100. 100 calls per configuration, 75,600 calls in total. For 1-5, all
             models concentrated on 3. For 1-10, 7 dominated, reaching roughly 80% of answers for
             GPT-4o-mini, Phi-4 and Gemini 2.0, with answers clustered in 4-8 and the extremes 1 and
             10 avoided. For 1-100, a handful of values (e.g. 42, 47, 57, 67, 73) carried most of the
             mass, typically fewer than ten distinct numbers appearing per configuration. Low
             temperature (0.1) collapsed to a single deterministic value; temperature 2.0 added only
             marginal variety and never approached uniform. The author attributes the pattern to
             training text reproducing human cognitive biases; DeepSeek-R1's visible reasoning
             considered proper randomization methods (coin flips, dice) yet its final answers stayed
             biased.
Locators:    Abstract and body (extracted via arxiv.org/html/2502.19965v1; per-cell percentages read
             from summary, treat individual cells as approximate).
Quote:       Prompt used: "Give me a random number between 1 and X. Please only return the number with
             no additional text."
```

```text
URL:         https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100
Kind:        primary — firsthand measurement with published raw data. A blog/repo counts as primary
             for data it measured itself.
Establishes: The 1-100 behavior for one current model, with a full published per-number series and a
             goodness-of-fit test. Best available chart source.
Paraphrase:  Repository by GitHub user "exmergo" (MIT license). OpenAI `gpt-4.1` via the Responses API
             was called 10,000 times at temperature 1.0 with a fixed system prompt requiring a single
             integer in 1-100 and a unique uuid4 per user prompt. The resulting distribution is far
             from uniform: the five most-picked numbers were 47, 57, 72, 37 and 42; 37 and 42 landed
             at about 4.0x their uniform-expected rate and 73 at about 3.4x. A chi-square
             goodness-of-fit test against uniform gave χ² = 15,604, p ≈ 0 (df = 99). Every multiple of
             10 except 10 itself was picked exactly 0 times in 10,000 calls; 10 was picked once. 69
             was UNDER-picked, about 0.29x expected (~29 of an expected ~100); the authors hypothesize
             safety training suppressed it. Raw and processed data are published: data/raw/
             chatgpt_random_results.csv, data/processed/distribution.csv (per-number counts),
             data/processed/stats_summary.csv.
Locators:    README.md; docs/LLM Random Bias Experiment SDD.md; data/processed/distribution.csv.
Quote:       "All multiples of 10, except for 10 itself, were picked exactly 0 times in 10,000 calls."
```

```text
URL:         https://arxiv.org/abs/2601.05414
Kind:        primary — firsthand measurement.
Establishes: That the failure is general to statistical sampling, not just the "pick a number" party
             trick, and that temperature does not systematically fix it.
Paraphrase:  "Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers
             from Statistical Distributions," Minda Zhao, Yilun Du, Mengyu Wang; arXiv:2601.05414v3,
             21 Apr 2026. Eleven models (including GPT-5.2, GPT-4o, Gemini-3-pro, DeepSeek-V3.2,
             Qwen3-32B, Llama-3.3-70B, Llama-4-Scout, Kimi-K2) were asked to draw N=1000 samples from
             15 named distributions (Uniform, Gaussian, Bernoulli, Poisson, and heavier-tailed ones).
             Median pass rate across models was 7%; GPT-4o was best at 40%; several models scored 0%.
             When each sample was requested independently rather than in one batch, 10 of 11 models
             hit 0% and error grew 10-15x, because a batch lets the model self-correct within its own
             context. On a related task — placing the correct answer uniformly across MCQ positions
             A/B/C/D (target 25% each) — GPT-4o produced 12.6 / 46.8 / 35.1 / 5.5 (χ² = 444.5,
             p < .001). A temperature ablation (T ∈ {0.2, 0.5, 1.0, 1.2}) did not systematically
             recover faithful sampling. The authors conclude current LLMs "lack a functional internal
             mechanism for probabilistic sampling" and recommend external numerical libraries.
Locators:    Abstract; results tables (batch/independent/MCQ); Appendix A (temperature ablation).
Quote:       "Current LLMs lack a functional internal mechanism for probabilistic sampling."
```

```text
URL:         https://arxiv.org/abs/2404.09043
Kind:        primary — firsthand measurement. Also the primary for the tool/code fix.
Establishes: Understanding-vs-sampling gap, and that generating and running code produces correct
             sampling where direct answers fail.
Paraphrase:  "Do LLMs Play Dice? Exploring Probability Distribution Sampling in Large Language Models
             for Behavioral Simulation," Jia Gu, Liang Pang, Huawei Shen, Xueqi Cheng (Institute of
             Computing Technology, Chinese Academy of Sciences); arXiv:2404.09043v3. Models including
             GPT-4, GPT-3.5, Claude 2.1, Llama2 and Vicuna were asked to sample from named
             distributions (100 sequences per test, temperature 0.9, KS test at α=0.01). Models could
             identify a distribution when asked (>80% accuracy) but could not sample from it:
             Poisson and Exponential were near-zero pass rates; Normal was best at up to ~50% KS pass;
             no model reached uniform sampling. Crucially, when the models were instead asked to write
             Python code to do the sampling, GPT-3.5, GPT-4 and Claude 2.1 reached "nearly 100%" on
             most explicit distributions. This is direct evidence for question 5 (the real fix is a
             tool/real RNG, not the model's own tokens).
Locators:    Abstract; explicit-distribution results; code-generation results.
Quote:       "LLM agents understand probability distributions, but their performance in sampling
             sequences adhering to probability distributions are limited."
```

```text
URL:         https://arxiv.org/abs/2505.00047
Kind:        primary — firsthand measurement.
Establishes: The nuance/limit: base models are closer to uniform; alignment amplifies the 7 bias.
Paraphrase:  "Base Models Beat Aligned Models at Randomness and Creativity," Peter West, Christopher
             Potts. A Llama-3.1 base model was compared against aligned variants (Llama-Instruct,
             Tulu-DPO, Tulu-SFT, Tulu-Full) at both 8B and 70B, prompted zero-shot to "Generate a
             random integer, uniformly between 0 and 10 (inclusive)," 1,500 successful generations per
             model. Measured by χ² divergence from uniform: at 8B the base model scored 13.9 versus
             aligned models at 52.3 to 129.1; at 70B the base scored 29.2 versus aligned at 18.3 to
             43.6. The paper notes aligned models tend to generate 7 with much higher probability than
             other numbers, "a common human bias," and that this "may begin in the base model and be
             exacerbated by these alignment recipes."
Locators:    Abstract; random-number-generation experiment (read via HTML/summary; treat the exact
             divergence numbers as reported-but-summary-sourced).
Quote:       Aligned models show "a tendency to generate '7' with significantly higher probability than
             other numbers, a common human bias."
```

```text
URL:         https://eric.ed.gov/?id=EJ149623
Kind:        primary — firsthand human experiment. This is the academic owner of the human number-7
             preference (the "training text full of human choices" the lesson invokes).
Establishes: That humans strongly over-choose 7 (and its family) when asked for a "random" number, and
             that the effect is a bid to look spontaneous, not automatic.
Paraphrase:  Michael Kubovy and Joseph Psotka, "The Predominance of Seven and the Apparent Spontaneity
             of Numerical Choices," Journal of Experimental Psychology: Human Perception and
             Performance, 1976, 2(2), 291-294. Asked to report the first digit that comes to mind,
             28.4% of respondents chose 7 — far above the 11% a flat 1-9 choice would give. Follow-up
             conditions: asked for a number 6-15, 17.3% chose 7; when the experimenter named 7 as an
             example, its rate fell to 16.6%; asked for a number in the 20s, 27.7% chose 27; asked for
             one in the 70s, 15.5% chose 77. The authors conclude subjects pick the response that will
             "appear to comply with the request for a spontaneous response."
Locators:    Journal abstract / ERIC record EJ149623 (also psycnet.apa.org/record/1977-00345-001).
Quote:       "When asked to report the first digit that comes to mind, a predominant number (28.4
             percent) of the respondents choose 7."
```

```text
URL:         https://huggingface.co/docs/transformers/generation_strategies
Kind:        primary — the library's own documentation of how it decodes. It owns the claim about what
             its greedy and sampling decoders do.
Establishes: The mechanism, in plain firsthand terms: the model produces a probability distribution
             over the vocabulary; greedy decoding takes the most likely token (argmax, deterministic);
             sampling draws a token at random from that distribution. No RNG "chooses a number" — the
             only randomness is the draw over tokens.
Paraphrase:  Hugging Face Transformers "Generation strategies." Greedy search "selects the next most
             likely token at each step" and is the deterministic default; the reference custom loop
             literally computes next_tokens = torch.argmax(next_token_logits). Sampling (multinomial)
             "randomly selects a token based on the probability distribution over the entire model's
             vocabulary (as opposed to the most likely token, as in greedy search)," so "every token
             with a non-zero probability has a chance to be selected."
Locators:    Sections "Greedy search" and "Sampling"; the custom-loop code example (argmax).
Quote:       "Sampling, or multinomial sampling, randomly selects a token based on the probability
             distribution over the entire model's vocabulary."
```

```text
URL:         https://machinelearningmastery.com/the-statistics-of-token-selection-logits-temperature-and-top-p-walkthrough/
Kind:        secondary — tutorial. Explains the standard temperature math; owns no measurement.
Establishes: The temperature mechanism for question 4: what T<1, T=0 and T>1 do to the token
             distribution.
Paraphrase:  A model's final layer emits a vector of logits, one per vocabulary token; a softmax turns
             them into a probability distribution summing to 1. Temperature is a scaling factor applied
             to the logits before softmax (p_i = exp(z_i/T) / Σ exp(z_j/T)). T<1 "sharpens the
             differences between high- and low-probability tokens," favoring the most likely tokens;
             T=0 reduces softmax to argmax (deterministic, always the top token); T>1 "flattens the
             resulting probabilities, making them more uniform." Flattening moves toward uniform but
             does not reach it: a rescaled non-uniform distribution stays non-uniform, which is why the
             measured studies above find high temperature never uniformizes the answers.
Locators:    Sections on logits→softmax and temperature effects.
Quote:       High temperature "flattens the resulting probabilities, making them more uniform."
```

```text
URL:         https://www.theregister.com/software/2025/06/30/ais-have-a-favorite-number-and-its-not-42/1270950
Kind:        secondary — reports on others' experiments; owns no measurement itself.
Establishes: Context and a second casual-prompt datapoint; ties the trade coverage to the Coronado-
             Blázquez paper.
Paraphrase:  The Register, 30 June 2025, "AIs have a favorite number, and it's not 42." Reports a
             hobby experiment by data scientist Mohd Faraaz (Capco): asked "Guess a number between 1
             and 50," six of seven leading models returned 27 (Grok returned 42). Points to Coronado-
             Blázquez, arXiv:2502.19965, as the systematic study, restating that GPT-4o-mini, Phi-4 and
             Gemini 2.0 chose 7 roughly 80% of the time in 1-10. The Faraaz "27 for 1-50" figure is a
             retelling here; treat it as a secondary datapoint (sample size not stated) unless the
             writer opens Faraaz's own post.
Locators:    Body of the article.
Quote:       —
```

```text
URL:         https://www.youtube.com/watch?v=d6iQrh2TK98
Kind:        secondary — crowdsourced survey reported in a video I did NOT open in full; recorded for
             completeness and traceability, not verified firsthand.
Establishes: The specifically human "37/73 for 1-100" pattern the commission mentions.
Paraphrase:  Veritasium ("Why is this number everywhere?", 2024) reports a survey of roughly 200,000
             people asked to pick a random number; the most common answers in 1-100 were 7, 37, 73 and
             77, and 37 was the single most common when people were asked for a number others would be
             least likely to pick. This is the source that owns the human 1-100 favorites; Kubovy &
             Psotka owns single-digit and small-range human preference but did not test 1-100. If the
             writer needs the human 1-100 figures, cite this and flag it as a crowdsourced survey, or
             lean on Kubovy for the peer-reviewed claim and use the LLM 1-100 data for the rest.
Locators:    Video (not opened); pattern corroborated by IFLScience and The Register coverage.
Quote:       —
```

## Contradictions

- Base vs aligned (West & Potts, arXiv:2505.00047): the bias is NOT a fixed
  property of "language models." Base pre-alignment models are measurably closer
  to uniform (8B: χ² divergence 13.9 vs 52.3-129.1 for aligned). Instruction
  tuning/RLHF appears to amplify the 7 preference. This does not undermine the
  commissioned angle — users interact with aligned chat models, where the bias is
  strong — but the writer must scope the claim to chat/aligned models and can use
  this as the honest "where does the favorite come from" nuance. It also cuts
  against any pure "the model just parrots its human training text" story: if
  base models are flatter, alignment is doing part of the work.

- Not literally "always the mode." The extreme concentration (7 at ~80%, single
  favorites) is measured on the casual prompt "give me a random number." When
  models are instead asked explicitly to "sample N from a Uniform/Normal
  distribution," they do somewhat better and variably (GPT-4o passed 40% of batch
  cases in Bad Dice Players; Normal reached ~50% KS pass in Do LLMs Play Dice).
  The article's behavior is the casual-prompt case, which is the strongly
  concentrated one — but do not overstate it as a universal law across all
  prompting styles.

- The 69 anomaly (exmergo): humans over-pick 69; `gpt-4.1` under-picks it
  (0.29x). This breaks the clean "the model reproduces human number bias" line
  and points to safety/post-training also shaping the output. The repo offers this
  as a hypothesis, not a proven cause. Good honest material for the "what is
  still open" step.

- Reasoning does not rescue it (Coronado-Blázquez): DeepSeek-R1's chain-of-
  thought explicitly considers coin flips and dice, then still outputs a biased
  favorite. Thinking about randomness in tokens is not the same as having a
  random source.

- No mainstream chat model in these sources approaches uniform on the casual
  1-10 prompt. The nearest thing to a counterexample is base models, which most
  users never use directly.

## Numbers

```text
Figure: 7 chosen by ~80% of answers for 1-10 (GPT-4o-mini, Phi-4, Gemini 2.0)
Owner:  Coronado-Blázquez, arXiv:2502.19965
Scope:  range 1-10; 100 calls per (model, language, temperature); 6 models; 7 languages;
        temperatures 0.1-2.0; 75,600 calls total. Per-model exact % approximate from summary read.
```

```text
Figure: 3 is the dominant pick for 1-5 across all six models (~60-80% concentration)
Owner:  Coronado-Blázquez, arXiv:2502.19965
Scope:  range 1-5, same design as above. Concentration figure approximate.
```

```text
Figure: χ² = 15,604, p ≈ 0, df = 99 (gpt-4.1, 1-100, vs uniform)
Owner:  exmergo repository
Scope:  10,000 calls, temperature 1.0, range 1-100.
```

```text
Figure: top picks for 1-100 (gpt-4.1) — 47: 526; 57: 457; 72: 415; 37: 404; 42: 401; 67: 391;
        27: 350; 73: 343; 87: 337
Owner:  exmergo repository (data/processed/distribution.csv)
Scope:  count out of 10,000; uniform expectation ~100 each. 47 ≈ 5.3x, 37 ≈ 4.0x, 42 ≈ 4.0x, 73 ≈ 3.4x.
```

```text
Figure: multiples of 10 picked 0 times (except 10, picked once); 69 picked 29 times (0.29x)
Owner:  exmergo repository (data/processed/distribution.csv)
Scope:  10,000 calls, 1-100. Confirmed against the raw series: 20,30,40,50,60,70,80,90,100 = 0; 10 = 1.
```

```text
Figure: 28.4% of people chose 7 (first digit that comes to mind)
Owner:  Kubovy & Psotka 1976, J. Exp. Psychol. HPP 2(2):291-294
Scope:  single digit choice; further conditions 6-15 → 7 at 17.3%; 20s → 27 at 27.7%; 70s → 77 at 15.5%.
```

```text
Figure: median batch pass rate 7%; GPT-4o best at 40%; independent-request pass rate 0% for 10/11 models
Owner:  Zhao/Du/Wang, arXiv:2601.05414
Scope:  N=1000 samples per distribution, 15 distributions, 11 models.
```

```text
Figure: code-generation sampling reaches "nearly 100%" on most explicit distributions;
        direct sampling near-zero for Poisson/Exponential, ~50% best (Normal)
Owner:  Gu et al., arXiv:2404.09043
Scope:  100 sequences per test, temperature 0.9, KS test α=0.01, GPT-3.5/GPT-4/Claude 2.1.
```

```text
Figure: χ² divergence from uniform — 8B base 13.9 vs aligned 52.3-129.1; 70B base 29.2 vs aligned 18.3-43.6
Owner:  West & Potts, arXiv:2505.00047
Scope:  range 0-10 inclusive, 1,500 generations per model. Summary-sourced; verify against paper tables.
```

Full measured series preserved for a chart (exmergo, gpt-4.1, 10,000 calls,
range 1-100, count per number). Source: data/processed/distribution.csv.

```text
number,count   (uniform expectation = 100)
1,0    2,1    3,2    4,1    5,0    6,0    7,5    8,1    9,2    10,1
11,8   12,56  13,87  14,83  15,4   16,25  17,182 18,42  19,44  20,0
21,7   22,31  23,90  24,48  25,5   26,54  27,350 28,87  29,94  30,0
31,4   32,73  33,13  34,109 35,12  36,146 37,404 38,120 39,45  40,0
41,46  42,401 43,207 44,53  45,18  46,155 47,526 48,81  49,46  50,0
51,9   52,127 53,269 54,196 55,6   56,225 57,457 58,133 59,61  60,0
61,28  62,294 63,286 64,302 65,13  66,12  67,391 68,106 69,29  70,0
71,17  72,415 73,343 74,313 75,12  76,143 77,115 78,93  79,92  80,0
81,13  82,179 83,156 84,267 85,15  86,145 87,337 88,30  89,35  90,0
91,17  92,221 93,84  94,107 95,2   96,23  97,98  98,14  99,1   100,0
```

## Source assets

```text
Asset: The 1-100 frequency series in exmergo's data/processed/distribution.csv (count per number,
       out of 10,000 gpt-4.1 calls), rendered by the repo as a bar chart at viz.exmergo.com.
Shows: The whole shape at once — spikes at 47/57/72/37/42/67/27/73/87, near-empty single digits,
       exact-zero multiples of 10, and the 69 dip. It makes "the choice is biased, not just variable"
       visible in one glance and contrasts against the flat uniform baseline of 100.
Crop:  A chart built per spec/charts.md from this series should keep the full 1-100 axis (the zeros at
       every multiple of 10 are part of the finding) and mark the uniform expectation (100) as a
       reference line. Do not crop to only the tall bars; the empty round numbers carry the argument.
```

```text
Asset: Coronado-Blázquez (arXiv:2502.19965) per-model distribution figures/heatmaps for 1-10 and
       1-100 across temperatures.
Shows: That the concentration on 7 (1-10) and on the prime-ish favorites (1-100) holds across
       different models and does not wash out as temperature rises.
Crop:  If reused, keep the model labels and the temperature axis so the "temperature doesn't fix it"
       point survives; a single-model crop loses the cross-model agreement.
```

```text
Asset: Kubovy & Psotka (1976) table of choice percentages by condition.
Shows: The human baseline the model inherits — 7 at 28.4%, and the parallel 27/77 pulls in shifted
       ranges — in the peer-reviewed source.
Crop:  Values only; the 1976 typesetting is not the point.
```

```text
Asset: West & Potts (arXiv:2505.00047) base-vs-aligned distribution comparison for 0-10.
Shows: The flatter base-model histogram beside the spikier aligned one — the visual form of
       "alignment amplifies the favorite."
Crop:  Keep both distributions in frame; the comparison is the asset.
```

## Discarded

```text
URL: https://medium.com/@aadityaubhat/humans-large-language-models-and-lucky-number-7-... — Medium
     returned HTTP 403; could not read firsthand, so not cited. Its likely primary (Kubovy & Psotka)
     is sourced directly above.
URL: https://medium.com/@hirsch.elad/pick-a-number-between-1-and-50-... — Medium 403; the "27 for
     1-50" claim it and The Register carry is recorded via The Register instead, flagged as secondary.
URL: https://mohdfaraaz.medium.com/llms-and-the-illusion-of-randomness-... — original hobby
     experiment behind The Register piece; Medium is 403-gated and sample size is unstated, so used
     only as the secondary datapoint The Register reports, not as a standalone primary.
URL: https://pasqualepillitteri.it/en/news/2724/... — returned HTTP 502; it reads as secondary
     aggregation of the Coronado/exmergo results anyway, which are cited directly.
URL: https://www.iflscience.com/why-do-many-large-language-models-... — secondary popular coverage;
     redundant with The Register and the primaries; not separately cited.
URL: https://openreview.net/pdf?id=rygGQyrFvH (Holtzman et al. 2020, nucleus sampling) — bot-
     verification wall blocked the body; the temperature/sampling mechanism it would support is
     covered by the Hugging Face docs and the temperature walkthrough, so not cited to avoid citing
     a source I could not open.
URL: arXiv:2604.06543 "The Illusion of Stochasticity in LLMs" and arXiv:2606.05874 — surfaced in
     search with implausible/future identifiers and not opened; excluded as unverified.
```

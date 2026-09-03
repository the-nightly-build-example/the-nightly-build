# Evidence record: option-order bias (researcher/01)

The record supports the lesson's spine firsthand. Two independent studies measure
that a model's choice among fixed multiple-choice options changes when the options
are reordered, and both put concrete figures on the swing: Zheng et al. move a
question's correct answer to each position and see accuracy move by up to 15
points on one model; Pezeshkpour & Hruschka report a best-minus-worst "sensitivity
gap" of roughly 13% to 75% across benchmarks. The candidate causes each have a
primary owner. Position weighting (primacy and recency) is owned by Liu et al. as a
general property of how transformers read a sequence. Priors over answer tokens
are owned by Zhao et al. (common-token bias) and, for the A/B/C/D case
specifically, by Zheng et al. (token bias). Scoring, and how it interacts with the
first two, is owned by Zheng et al.'s protocol description, Robinson & Wingate's
symbol-binding work, two first-token-versus-text studies, and a Hugging Face
engineering post. The record is thin in one important place: the exact split
between token-prior and position causes is not settled, and the two headline
papers openly disagree about which dominates. That disagreement is documented in
Contradictions, not smoothed over. Figures drawn directly from the source PDFs are
marked; a handful read off a rendered page through a fetch tool are flagged so the
writer re-checks them before they carry weight.

## Sources

```text
URL:         https://arxiv.org/abs/2309.03882
Kind:        primary — the paper owns the selection-bias measurement, the
             token-bias claim, and the PriDe method. Authored by the team that ran
             the experiments (Zheng, Zhou, Meng, Zhou, Huang), ICLR 2024.
Establishes: (a) Reordering behavior. Moving a question's golden answer to a fixed
             option position changes accuracy sharply. 0-shot MMLU, Table 1:
             llama-30B goes 53.1 baseline -> 68.2 when the answer is always A
             (+15.2) and -> 41.2 when always D (-11.9). gpt-3.5-turbo goes 67.2 ->
             74.2 at C (+6.9) and -> 60.9 at D (-6.3). vicuna-v1.3-33B +8.8 at C,
             -12.3 at D. (b) A magnitude metric: selection bias is measured as
             RStd, the standard deviation across the recalls of the option IDs
             (higher RStd = more biased). 0-shot MMLU default RStd (Appendix C
             table): gpt-3.5-turbo 5.5, llama-30B 8.5, vicuna-v1.3-13B 10.5,
             falcon-inst-7B 28.7. (c) Cause claim: the bias "arises less from LLMs'
             position bias" and more from "token bias," where the model a priori
             puts more probability mass on specific ID tokens A/B/C/D. Two
             ablations back this: randomly shuffling the options "does not
             obviously change selection bias" (position ruled largely out), while
             removing the option IDs cuts average RStd by 6.4 on MMLU (token
             implicated) at a 2.1-point accuracy cost. (d) PriDe fix: estimate the
             ID prior by permuting option contents over ~5% of samples, subtract it
             from the rest. 0-shot MMLU, alpha=5%: average RStd -7.6, accuracy +1.2.
Paraphrase:  Modern LLMs prefer certain option-ID tokens regardless of content;
             the authors attribute this mainly to a prior over the A/B/C/D tokens
             rather than to option position, and remove it cheaply at inference.
Locators:    Abstract; Section 2.1 (Evaluation), 2.2 (RStd definition), 2.4
             (ablations), Table 1 p.2; PriDe Section 3; Appendix C per-model table
             (the "Default / RemovingIDs / CyclicPerm / PriDe" table). Table 1 and
             the definitions read directly from the PDF; per-model RStd and the
             PriDe delta row read directly from the Appendix C table.
Quote:       "contrary to the common view in previous work ... selection bias
             arises less from LLMs' position bias ... we pinpoint one more salient
             intrinsic cause of selection bias as the model's token bias."
             "for open-source models, we access the output probabilities of option
             ID tokens A/B/C/D/E and use the maximal one as the model prediction.
             For gpt-3.5-turbo, we compare the golden answer with the first
             generated token, with the decoding temperature set to 0."
```

```text
URL:         https://arxiv.org/abs/2308.11483
Kind:        primary — owns the order-sensitivity measurement and the positional
             conjecture. Pezeshkpour & Hruschka (Megagon Labs), Findings of NAACL
             2024.
Establishes: (a) The headline swing. A "sensitivity gap" (best oracle ordering
             minus worst) of "approximately 13% to 75%" zero-shot. Even GPT-4,
             above 90% on some tasks, still shows a 13.1% gap. (b) Table 1, 0-shot,
             best/worst deltas from a vanilla ordering: GPT-4 Abstract Algebra 57.0
             vanilla, -30.0 / +23.0; InstructGPT (text-davinci-003) Abstract
             Algebra 33.0 vanilla, -31.0 / +39.0 (a 70-point span); InstructGPT
             Logical Deduction 64.0, -39.4 / +34.7. GPT-4 is consistently less
             sensitive than InstructGPT. (c) The cause they argue for: positional
             bias interacting with uncertainty. Conjecture 4.1 (verbatim below).
             Supporting checks: sensitivity correlates with error rate; on
             sensitive items the model answers "yes" to "can more than one choice
             be highly probable" over 94% of the time; keeping only the top-2/3
             choices in place barely changes accuracy, which they read as position,
             not content, driving the flips. (d) Amplify/mitigate patterns: putting
             the top-2 choices first-and-last amplifies the bias, placing them
             adjacent mitigates it (Tables 3-4). (e) Fixes: majority vote over 10
             random reorders gives "up to 8 percentage points" improvement;
             Multiple Evidence Calibration (MEC) is unreliable here and
             "consistent[ly] decrease[s]" InstructGPT performance.
Paraphrase:  Option order can swing scores enormously, worst on weaker models and
             harder tasks; the authors trace it to the model favoring positions
             when it is unsure between its top choices, and recommend averaging
             over reorderings.
Locators:    Abstract; Section 3.1 and Table 1 (p.3); Conjecture 4.1 and Section
             4.1 (p.4-5); Tables 3-4 (p.6-7); Section 5 and Table 5 (calibration).
             All read directly from the PDF.
Quote:       Conjecture 4.1: "The sensitivity of LLMs to the order of options in
             multiple-choice questions arises from the interaction of two colluding
             forces: (1) Uncertainty of LLMs regarding the correct answer among the
             top possible choices. And (2) positional bias, leading LLMs to favor
             specific options based on the order they appear in, depending on the
             question."
```

```text
URL:         https://arxiv.org/abs/2307.03172
Kind:        primary — owns the position-weighting mechanism (primacy/recency),
             though for relevant-information location in long context, not MCQ
             option order. Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang;
             TACL 2024.
Establishes: A U-shaped accuracy curve as a function of where the needed
             information sits in the input. Performance is highest when the
             relevant item is at the very start (primacy) or very end (recency) and
             sags in the middle. Multi-document QA: gpt-3.5-turbo's accuracy drops
             "by more than 20%" from best position to the worst (middle) position.
             Table 1 anchors the ceiling: gpt-3.5-turbo oracle 88.3, closed-book
             56.1; claude-1.3 oracle 76.1. Models tested include gpt-3.5-turbo
             (4K/16K), claude-1.3 (and 100K), MPT-30B-Instruct, LongChat-13B-16K,
             with GPT-4 on a subset.
Paraphrase:  A transformer does not weight all sequence positions equally; content
             at the edges is used more reliably than content in the middle. This is
             the general primacy/recency effect the option-position story rests on,
             established here on a different task.
Locators:    Abstract and Figure 1 (p.1); Section 2-3, Table 1 and Figure 5 (p.5).
             Abstract, Figure 1 caption, Table 1, and the ">20%" sentence read
             directly from the PDF.
Quote:       "models are better at using relevant information that occurs at the
             very beginning (primacy bias) or end of its input context (recency
             bias), and performance degrades significantly when models must access
             and use information located in the middle of its input context."
```

```text
URL:         https://arxiv.org/abs/2102.09690
Kind:        primary — owns the "common-token bias" concept and contextual
             calibration. Zhao, Wallace, Feng, Klein, Singh; ICML 2021. Scope is
             few-shot classification prompt order, not MCQ option IDs, so it is the
             origin of the token-prior mechanism rather than a measurement of
             option-order bias.
Establishes: (a) LLM predictions carry three biases: majority-label bias, recency
             bias, and common-token bias, "the inclination to output tokens
             prevalent in the pre-training distribution" (their example: preferring
             "United States" over "Saint Lucia"). (b) Prompt/example ordering alone
             moves sentiment accuracy "from near chance (54%) to near
             state-of-the-art (93%)." (c) The fix that Zheng's PriDe later
             generalizes: estimate the model's prior by feeding a content-free
             input ("N/A") and calibrate so that input scores uniformly across
             answers; this lifts GPT-3/GPT-2 accuracy by "up to 30.0% absolute" and
             cuts variance.
Paraphrase:  Before any option-ID story, LLMs are known to carry priors toward
             particular answer tokens purely from pre-training frequency, and a
             content-free probe can estimate and subtract that prior. This is the
             general form of the A/B/C/D token bias and of PriDe.
Locators:    Abstract; Section 1 and Section 4 (the three biases); Section 5
             (contextual calibration, 30.0% figure). Read directly from the PDF.
Quote:       "they suffer from majority label bias, recency bias, and common token
             bias ... the common token bias leads the model to prefer answers that
             are frequent in its pre-training data."
```

```text
URL:         https://arxiv.org/abs/2404.08382
Kind:        primary — owns the finding that first-token scoring overstates
             selection bias. Wang, Hu, Ma, Roettger, Plank ("Look at the Text",
             2024).
Establishes: Ranking answers by the log-probability of the first token exaggerates
             order sensitivity relative to reading the model's actual generated
             text answer. When the first-token answer and the text answer disagree
             (mismatch rates reported by model: Gemma-7b-Inst 56.8%, Llama2-7b-Chat
             51.4%, Llama2-13b-Chat 35.3%, Mistral-7b-Inst 10.2%), the text answer
             is more robust to option-order changes. Above ~50% mismatch, the plain
             text answer shows less selection bias than PriDe-debiased first-token
             probabilities.
Paraphrase:  Part of the measured "token bias" is an artifact of the scoring probe.
             How much of the A/B/C/D effect survives when you read the words the
             model writes, rather than its first-token distribution, is model- and
             method-dependent. Directly relevant to marking the decomposition as
             unsettled.
Locators:    Abstract; Section 3.3 and Table 4 (mismatch rates and the
             PriDe comparison). Read via the rendered HTML through a fetch tool, not
             the raw PDF — the writer should re-verify the exact percentages before
             quoting them.
Quote:       "text answers are more robust to question perturbations than the first
             token probabilities, when the first token answers mismatch the text
             answers."
```

```text
URL:         https://arxiv.org/abs/2402.14499
Kind:        primary — owns the first-token-vs-text mismatch measurement ("My
             Answer is C: First-Token Probabilities Do Not Match Text Answers in
             Instruction-Tuned Language Models", 2024).
Establishes: First-token probability evaluation is often unfaithful to what the
             instruction-tuned model actually writes. Reported mismatch: Llama2-7b-
             Chat 51.4% on MMLU (dropping toward 9.0% for Mixtral-8x7b), and much
             higher on OpinionQA. Text output is more self-consistent than the
             first-token score for all tested models except Mixtral. Models: Llama2-
             Chat 7/13/70B, Mistral-Instruct v0.1/v0.2, Mixtral-8x7b-Instruct.
Paraphrase:  A second, independent group finds the first-token probe disagrees with
             the model's spoken answer often enough that bias measured through it
             cannot be taken as the model's true choice behavior.
Locators:    Abstract; Section 3 (Models) and Table 4. Read via rendered HTML
             through a fetch tool — re-verify the exact percentages before quoting.
Quote:       "first-token evaluation is not faithful to text output: it often does
             not match the text output's answer."
```

```text
URL:         https://arxiv.org/abs/2210.12353
Kind:        primary — owns "multiple choice symbol binding" (MCSB). Robinson,
             Rytting, Wingate; ICLR 2023.
Establishes: Two ways to score an MCQ. The cloze way conditions on the question
             alone and scores each answer's text; the "natural" way shows the
             question with all lettered options and has the model emit the symbol
             (e.g., "A"). The natural way requires the model to bind each option's
             content to its symbol, an ability the authors name MCSB, and this
             "ability varies greatly by model." Across 20 datasets a high-MCSB model
             does much better with the symbol approach.
Paraphrase:  Whether a model can even be scored by the option letter depends on a
             learned skill that differs by model; the letter-scoring regime where
             option-ID token bias lives is one specific and not universal way to
             pose an MCQ.
Locators:    Abstract; MCSB definition section. Read via the arXiv abstract page
             through a fetch tool; the two-approach framing and "varies greatly by
             model" are from the abstract. Deeper claims not independently read.
Quote:       "The LLM needs what we term multiple choice symbol binding (MCSB)
             ability." (abstract)
```

```text
URL:         https://arxiv.org/abs/2406.03009
Kind:        primary to its own measurements, used here as an independent third
             confirmation. "Unveiling Selection Biases: Exploring Order and Token
             Sensitivity in Large Language Models", Wei, Wu, Huang, Chen (NTU /
             Academia Sinica), 2024.
Establishes: A separate group, zero-shot, frames selection bias as arising from two
             components, option order and token usage, citing both Zheng and
             Pezeshkpour, and quantifies both across several models and tasks. It
             restates the field's two-cause picture (order bias plus common-token
             bias) from outside the two disputing papers.
Paraphrase:  Independent confirmation that the effect is real and that the field
             analyzes it as order-plus-token, useful for the "robustly measured"
             claim. Its own numbers were not extracted here.
Locators:    Abstract and Section 1; the "majority... token bias" recap near
             Section 3. Read via rendered PDF/HTML through a fetch tool; abstract
             and intro read directly, numeric tables not extracted.
Quote:       None extracted verbatim beyond the abstract's framing.
```

```text
URL:         https://huggingface.co/blog/open-llm-leaderboard-mmlu
Kind:        secondary — an engineering explainer reporting, from outside the
             research groups, how MMLU scoring choices change results. Hugging Face
             blog, "What's going on with the Open LLM Leaderboard?"
Establishes: The same MMLU questions scored three ways give different numbers and
             reorder the leaderboard. "Original" compares the probabilities of the
             letters A/B/C/D; "HELM" generates text and reads the letter; "Harness"
             scores the log-probability of the full answer text after the letter.
             LLaMA-65B: 0.636 (Original) vs 0.637 (HELM) vs 0.488 (Harness) on the
             same items.
Paraphrase:  Confirms in plain engineering terms that the scoring probe is a real,
             separable variable: letter-probability, generated-letter, and full-
             text-probability are three different measurements of "the same" answer,
             and they disagree by large margins.
Locators:    Sections describing the three implementations and the comparison
             table. Read via the rendered blog page through a fetch tool; the
             LLaMA-65B figures should be re-checked against the live page.
Quote:       (paraphrased) the three MMLU implementations "are just numbers which
             are not at all comparable."
```

## Contradictions

- Dominant cause, token vs position. Zheng et al. state directly that selection
  bias "arises less from LLMs' position bias" and name token bias as the more
  salient cause, and they cite Pezeshkpour & Hruschka as the "common view" they are
  arguing against. Pezeshkpour & Hruschka's Conjecture 4.1 puts positional bias at
  the center (interacting with uncertainty). The two headline papers reach opposite
  emphases on the same phenomenon. This is the single most important open point for
  the lesson: the effect is settled, the decomposition is not.
- Whether the token effect is partly a measurement artifact. Zheng et al. measure
  token bias through first-token / option-ID probability. Wang et al. (2404.08382)
  and the "My Answer is C" study (2402.14499) show that first-token scoring often
  disagrees with the model's actual text answer (mismatch above 50% on some
  instruction-tuned models), and that the text answer is sometimes more robust than
  PriDe-debiased first-token probabilities. So some of the measured token bias
  belongs to the probe, not only to the model. This does not overturn Zheng's
  ablations (shuffling IDs vs removing IDs), which are internal to one scoring
  method, but it qualifies how much of the headline number transfers to
  generation-time behavior.
- Scope caution, not a contradiction. Liu et al. (primacy/recency) and Zhao et al.
  (common-token bias) are measured on tasks other than short MCQ option ordering.
  They own the mechanisms, not a direct measurement of option-order bias. The
  lesson should present them as the mechanism's origin, and Zheng/Pezeshkpour as the
  option-order measurements, rather than blur the two.

## Numbers

```text
Figure: +15.2 / -11.9 accuracy points (llama-30B, golden answer forced to A vs D)
Owner:  Zheng et al. 2309.03882, Table 1
Scope:  0-shot MMLU, accuracy (%), baseline 53.1; single model, illustrative

Figure: +6.9 / -6.3 accuracy points (gpt-3.5-turbo, golden answer forced to C vs D)
Owner:  Zheng et al. 2309.03882, Table 1
Scope:  0-shot MMLU, accuracy (%), baseline 67.2

Figure: RStd (0-shot MMLU, default): gpt-3.5-turbo 5.5, llama-30B 8.5,
        vicuna-v1.3-13B 10.5, falcon-inst-7B 28.7
Owner:  Zheng et al. 2309.03882, Appendix C per-model table
Scope:  standard deviation of option-ID recalls; higher = more biased; 20 LLMs total

Figure: RemovingIDs ablation: average RStd -6.4, accuracy -2.1 (MMLU)
Owner:  Zheng et al. 2309.03882, Appendix C table, delta-average row
Scope:  0-shot MMLU, averaged over 20 LLMs; token-bias evidence, at an accuracy cost

Figure: PriDe (alpha=5%): average RStd -7.6, accuracy +1.2 (MMLU)
Owner:  Zheng et al. 2309.03882, Appendix C table, delta-average row
Scope:  0-shot MMLU, averaged over 20 LLMs

Figure: sensitivity gap "approximately 13% to 75%"
Owner:  Pezeshkpour & Hruschka 2308.11483, Abstract / Section 3.1
Scope:  best-minus-worst oracle ordering, 0-shot, across five benchmarks

Figure: InstructGPT Abstract Algebra -31.0 / +39.0 (span ~70 points)
Owner:  Pezeshkpour & Hruschka 2308.11483, Table 1
Scope:  0-shot, deltas from vanilla ordering 33.0; text-davinci-003

Figure: GPT-4 still shows a 13.1% gap despite >90% accuracy on some tasks
Owner:  Pezeshkpour & Hruschka 2308.11483, Section 3.1
Scope:  0-shot; shows the effect is not confined to weak models

Figure: majority vote over 10 reorders: "up to 8 percentage points" gain
Owner:  Pezeshkpour & Hruschka 2308.11483, Section 5 / Table 5
Scope:  across GPT-4 and InstructGPT and the five benchmarks

Figure: multi-document QA accuracy drops "more than 20%" best-to-worst position
Owner:  Liu et al. 2307.03172, Section 5 (Table 1 ceilings: gpt-3.5-turbo oracle
        88.3, closed-book 56.1)
Scope:  gpt-3.5-turbo; position of the answer-bearing document; primacy/recency

Figure: sentiment accuracy 54% -> 93% by changing example order alone
Owner:  Zhao et al. 2102.09690, Section 1
Scope:  few-shot classification prompt order; contextual calibration adds up to
        30.0% absolute

Figure: first-token vs text-answer mismatch: Llama2-7b-Chat 51.4% on MMLU;
        Gemma-7b-Inst 56.8%; Mistral-7b-Inst ~10%
Owner:  Wang et al. 2404.08382 (Table 4) and "My Answer is C" 2402.14499 (Table 4)
Scope:  instruction-tuned models; flags the scoring probe as unreliable; read via
        fetch, re-verify exact values

Figure: LLaMA-65B MMLU: 0.636 (Original) / 0.637 (HELM) / 0.488 (Harness)
Owner:  Hugging Face Open LLM Leaderboard MMLU blog
Scope:  same questions, three scoring implementations; ~30% relative swing;
        read via fetch, re-verify
```

## Source assets

```text
Asset: Zheng et al. 2309.03882, Figure 2 (recall-per-ID bars beside the Table 1
       accuracy fluctuation), p.2
Shows: that the accuracy swing when the answer is forced to a position tracks the
       imbalance in how often each option ID is recalled — the visual link between
       "token prior" and "position sensitivity."
Crop:  keep both panels together (the accuracy bars and the A/B/C/D recall bars);
       the argument is the correlation between them, so neither panel stands alone.

Asset: Liu et al. 2307.03172, Figure 1 (the U-shaped accuracy-vs-position curve),
       p.1
Shows: primacy and recency in one picture — high at first and last positions, low
       in the middle. The cleanest single image for the position mechanism.
Crop:  retain the full x-axis from first to last position and the y-axis scale;
       cropping the middle out would destroy the U.

Asset: Pezeshkpour & Hruschka 2308.11483, Figure 1 (GPT-4 flipping "hen house" to
       "outside bedroom window" after a reorder), p.1
Shows: a single worked flip on a real CSQA item — the behavior at the smallest
       scale, one question, one model, one reorder.
Crop:  keep both the original-order and reordered panels and the two answers;
       the point is the changed answer, which needs the before and after.

Asset: Hugging Face Open LLM Leaderboard MMLU blog, the three-implementations
       comparison table (LLaMA-65B row)
Shows: one model, one benchmark, three scoring methods, three different scores.
       Concrete proof that scoring is a separable cause.
Crop:  keep the method labels and at least the LLaMA-65B row; the numbers mean
       nothing without the method names beside them.
```

## Discarded

```text
URL: https://arxiv.org/abs/2605.01846 — position bias in multiple-choice question
     generation, not answering; wrong mechanism and a claimed "no consensus" line
     could not be located in the text, so it is not cited for that point.
URL: https://arxiv.org/abs/2406.07545 — Open-LLM-Leaderboard open-style conversion;
     adjacent topic (moving away from MCQ) but does not own any mechanism the
     lesson needs.
URL: https://arxiv.org/abs/2402.01349 — "LLMs May Perform MCQA by Selecting the
     Least Incorrect Option"; interesting but a different claim (relative ranking),
     read only to confirm it was off-target for the reorder mechanism.
```

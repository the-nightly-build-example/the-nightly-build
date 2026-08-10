# Evidence: the-mechanics/prompt-sensitivity (researcher/01)

The evidence supports every step of the commission's chain with primary measurements. That a trivial formatting change moves accuracy is measured: Sclar et al. (FormatSpread) report a spread of up to 76 accuracy points on LLaMA-2-13B between equivalent formats, and a single worked case where changing a colon to a space moves 1-shot LLaMA-2-7B from 0.043 to 0.826 on one task. That reordering the same few-shot examples moves accuracy is measured: Lu et al. find the same four SST-2 examples score above 85% in some orders and near 50% in others, and a good order for one model correlates 0.05 with a good order for another. The mechanism step (the model conditions on the literal token sequence, with no separate store of "meaning") is supported from three directions: Webson & Pavlick show models keep working when the instruction's meaning is scrambled but swing on the choice of answer tokens; Su et al. trace the delimiter effect to attention heads keying on specific input tokens; Sclar et al. show a format's continuous embedding is separable in a way that tracks its performance spread. The record is thin, and honestly contested, on one point the commission marks open: whether the effect shrinks in the newest frontier models. FormatSpread and Su et al. say it does not shrink with scale or instruction tuning; Hua et al. argue much of the measured spread is an artifact of heuristic scoring and that modern GPT/Gemini models are fairly robust once graded by an LLM judge. The large headline numbers all come from 2021-2023 open models on constrained-output classification, and are generation-dependent. See Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/2310.11324
Kind:        primary. Sclar, Choi, Tsvetkov (University of Washington / Allen Institute for
             AI) and Suhr (UC Berkeley) own the FormatSpread measurements; ICLR 2024.
Establishes: The size of format sensitivity and that it survives scale, more shots, and
             instruction tuning. Models evaluated: LLaMA-2-7B/13B/70B, Falcon-7B,
             Falcon-7B-Instruct, GPT-3.5-Turbo, all autoregressive, on classification and
             some generation tasks from SuperNaturalInstructions.
Paraphrase:  Across "equivalent" formats (same content, different separators/casing/spacing),
             accuracy varies by up to 76 points on LLaMA-2-13B and ~10 points on average
             across 50+ tasks and several models. The median spread across choices of model
             and number of few-shot examples is 7.5 points; 20% of tasks show at least 15
             points of spread for all LLaMA-2 settings (at least 9 for all Falcon settings),
             and several tasks exceed 70 points. On API-gated GPT-3.5-Turbo the spread reaches
             56 points, median 6.4, across 320 formats and 53 tasks. The spread is "not
             eliminated by increasing few-shot examples or model size, nor with instruction
             tuning" (Falcon-7B vs Falcon-7B-Instruct, Fig 2b; 7B vs 13B vs 70B, Fig 2a and
             12; 1- vs 5-shot, Fig 2c). The accuracy landscape over formats is "highly
             non-monotonic," so the best format cannot be found by local search and no single
             atomic feature (separator, casing, enumeration) independently predicts
             performance. Comparison trends between two models are often reversed just by
             choosing different formats, so format performance only weakly correlates between
             models. Mechanism: §4.4, prompt formats are "identifiable transformations of
             prompt embeddings," and the separability of a format's continuous embedding
             correlates with its observed performance spread.
Locators:    Abstract; Overview (the "up to 76 points ... ~10 on average" sentence); §4.1
             Models; §4.2 (median 7.5, the 20%/15-point sentence, the reversal claim); §4.3
             (non-monotonic, atomic features do not independently predict); §4.4 (embeddings);
             Table 1 and Figure 1 (worked examples, below).
Quote:       "with performance differences of up to 76 accuracy points when evaluated using
             LLaMA-2-13B. Sensitivity remains even when increasing model size, the number of
             few-shot examples, or performing instruction tuning."
Quote:       "The space of prompt format accuracy is highly non-monotonic, which makes local
             search algorithms over the space less effective."
```

```text
URL:         https://arxiv.org/abs/2104.08786
Kind:        primary. Lu, Bartolo, Riedel, Stenetorp (University College London) and Moore
             (Mishcon de Reya LLP) own the order-sensitivity measurements; ACL 2022.
Establishes: The size of order sensitivity, that it does not reliably shrink with scale, and
             that a good order is not predictable in advance without labelled data. Models:
             GPT-2 at 0.1B/0.3B/0.8B/1.5B (base/medium/large/XL) and GPT-3 at 2.7B through
             175B.
Paraphrase:  Reordering the same few-shot examples "can make the difference between near
             state-of-the-art and random guess performance." On SST-2 with four examples and
             24 orderings, some permutations reach over 85% accuracy (comparable to supervised
             training) while others sit near 50% (random); GPT2-XL (1.5B) can exceed 90% on a
             good order. Order sensitivity "is present across model sizes (even for the largest
             current models)"; increasing model size "does not guarantee low variance."
             Increasing the number of training examples does not reduce the variance and can
             increase it (Fig 3), so the authors call order sensitivity "likely to be a
             fundamental issue." A good permutation does not transfer between models: the
             permutation-performance correlation between the 175B and the 2.7B model is only
             0.05. In the true few-shot setting there is no labelled development set to pick an
             order, so the authors build an unlabelled "probing set" by sampling from the model
             and rank candidate orders by entropy of the predicted label distribution
             (GlobalE/LocalE), yielding a 13% relative improvement on average across eleven
             text-classification tasks and all model sizes.
Locators:    Abstract; §1 and Figure 1 caption (SST-2, 24 orders, 85% vs ~50%); §2 ("increasing
             model size does not guarantee low variance," the 0.05 correlation); §on adding
             samples (Fig 3, "high level of variance remains ... can even increase"); method
             sections (probing set, entropy, 13%).
Quote:       "some permutations have comparable performance (over 85% accuracy) to supervised
             training for sentiment classification, while others perform close to random
             (around 50%)."
Quote:       "the 175B and 2.7B model only has a correlation of 0.05, this means a good
             permutation for the 2.7B model is in no way guaranteed that it will also yield
             good performance for" another model.
```

```text
URL:         https://arxiv.org/abs/2102.09690
Kind:        primary. Zhao, Wallace, Feng, Klein (UC Berkeley) and Singh (UC Irvine) own the
             instability measurements and the bias analysis; ICML 2021.
Establishes: A second, independent order-sensitivity number, and a candidate mechanism for
             why order (and format) move the score. Models: GPT-3 at 2.7B/13B/175B and GPT-2
             at 1.5B.
Paraphrase:  A prompt has three parts: a format, a set of training examples, and a permutation
             (ordering) of them; each can move accuracy "from near chance to near
             state-of-the-art." Changing only the permutation of the examples in a sentiment
             prompt changes accuracy from near chance (54%) to near state-of-the-art (93%).
             The authors attribute this instability to three biases in how the model reads the
             prompt: majority-label bias (it favours answers that appear often among the
             examples), recency bias (it favours answers that appear near the end of the
             prompt), and common-token bias (it favours answers that were frequent in
             pre-training, e.g. "United States" over "Saint Lucia"). Their contextual
             calibration, which fits a correction so a content-free input ("N/A") predicts
             uniformly, improves accuracy by up to 30.0% absolute and reduces variance, but
             does not remove it.
Locators:    Abstract; §1 (three components; the 54%->93% sentence); §4 (majority-label,
             recency, common-token biases); §5 (contextual calibration, up to 30.0% absolute).
Quote:       "changing the permutation of the training examples in a sentiment analysis prompt
             can change accuracy from near chance (54%) to near state-of-the-art (93%)."
Quote:       "they suffer from majority label bias, recency bias, and common token bias ...
             The majority label and recency biases lead the model to predict training answers
             that appear frequently or near the end of the prompt."
```

```text
URL:         https://arxiv.org/abs/2109.01247
Kind:        primary. Webson & Pavlick (Brown University) own the meaning-vs-surface
             measurements; NAACL 2022.
Establishes: The clearest support for "the model conditions on tokens, not on a stored meaning
             of the prompt." Models: BERT/RoBERTa/ALBERT/T5-LM-adapted, instruction-tuned T0
             (3B, 11B), and GPT-3 175B, on natural language inference (NLI).
Paraphrase:  Testing over 30 hand-written templates and 13 sets of answer ("LM target") words,
             more than 390 prompts in all, they find models "learn just as fast with many
             prompts that are intentionally irrelevant or even pathologically misleading as
             they do with instructively good prompts," and this holds up to GPT-3 175B and for
             instruction-tuned T0. Yet models are "much more sensitive to the choice of the LM
             target words as opposed to the meaning of the instruction templates": swapping
             which token stands for "entailment" (e.g. yes/no vs other tokens) moves results
             more than making the instruction semantically wrong. Instruction tuning makes
             models somewhat more sensitive to instruction semantics, but even T0 performs
             "arguably too well" on pathological prompts. Read together: scrambling the meaning
             is close to a no-op, while changing surface tokens is not, so the model is keying
             on the token strings, not on an extracted meaning.
Locators:    Abstract; §on target words (yes/no categories, "much more sensitive to the choice
             of the LM target words"); results table note ("models do not understand the
             differences between the prompt categories"); §on T0 ("arguably too well ... with
             pathological prompts").
Quote:       "models learn just as fast with many prompts that are intentionally irrelevant or
             even pathologically misleading as they do with instructively 'good' prompts."
Quote:       "models are much more sensitive to the choice of the LM target words as opposed to
             the meaning of the instruction templates."
```

```text
URL:         https://arxiv.org/abs/2510.05152
Kind:        primary. Su, Zhang, Ullrich, Bottou, Ibrahim own the delimiter measurements and
             the attention analysis; 2025 preprint. Confirms the effect in current model
             families and adds a direct token-level mechanism.
Establishes: That the effect persists in 2024-2025 open models and reaches into ranking, plus
             a mechanistic locus. Model families: Llama, Qwen, Gemma.
Paraphrase:  Changing only the single character that separates in-context examples (comma vs
             newline vs semicolon vs hashtag, and so on) changes MMLU accuracy by up to plus or
             minus 23% across leading model families, and one can "put any model in the lead by
             only modifying the single character separating examples." The brittleness "pervades
             topics, model families, and doesn't improve with scale." Probing attention-head
             scores, they find that good delimiters "steer attention towards key tokens in the
             input," and that stating the chosen delimiter in the prompt improves robustness.
Locators:    Abstract (the +/-23% figure, the ranking claim, "doesn't improve with scale," the
             attention finding).
Quote:       "Across leading model families (Llama, Qwen, Gemma), performance on MMLU for
             example can vary by +/-23% depending on the choice of delimiter. In fact, one can
             manipulate model rankings to put any model in the lead by only modifying the
             single character separating examples."
Quote:       "By probing attention head scores, we find that good-performing delimiters steer
             attention towards key tokens in the input."
```

```text
URL:         https://arxiv.org/abs/2509.01790
Kind:        primary, and the main counterweight. Hua, Tang, Gu, Gu, Wong, Qin own these
             re-evaluations; EMNLP 2025. It owns the claim that some measured sensitivity is a
             scoring artifact.
Establishes: That a large part of reported prompt sensitivity, on multiple-choice and
             short-answer benchmarks, disappears when the grader stops using log-likelihood or
             rigid string matching. Models: LLaMA-3.1, Qwen-2, Gemma-2, Ministral, GPT-4o-mini,
             GPT-4.1-mini, Gemini 2.0 Flash (7 total), on ARC-Challenge, GPQA-Diamond,
             OpenbookQA, NarrativeQA, MATH, SimpleQA, with 12 templates.
Paraphrase:  Much prompt sensitivity "stems from heuristic evaluation methods, including
             log-likelihood scoring and rigid answer matching, which often overlook
             semantically correct responses expressed through alternative phrasings." Grading
             the same outputs with an LLM judge collapses the spread: on ARC-Challenge, Gemma-2
             ranges from 0.25 to 0.90 accuracy across templates under heuristic scoring
             (standard deviation 0.28) but varies by only 0.17 under LLM-as-judge (standard
             deviation 0.005). Average Spearman rank correlation across prompts among the
             open-source models rises from 0.30 (heuristic) to 0.92 (LLM-as-judge); on
             NarrativeQA, from 0.40 to 0.87. Their conclusion: "modern LLMs are more robust to
             prompt templates than previously believed, and ... prompt sensitivity may be more
             an artifact of evaluation than a flaw in the models."
Locators:    Abstract and results (the ARC-Challenge/Gemma-2 0.25-0.90 vs 0.17 numbers; the
             0.30->0.92 and 0.40->0.87 rank correlations).
Quote:       "much of the prompt sensitivity stems from heuristic evaluation methods, including
             log-likelihood scoring and rigid answer matching, which often overlook
             semantically correct responses expressed through alternative phrasings."
```

```text
URL:         https://huggingface.co/blog/evaluation-structured-outputs
Kind:        secondary (rigorous explainer, for context). Will Kurt, Remi Louf, Clementine
             Fourrier and the Hugging Face / .txt teams, 30 April 2024. It reports the
             phenomenon and FormatSpread for a general audience, and adds its own small
             demonstration; use it for framing, not as the owner of the core numbers.
Establishes: An accessible restatement of the phenomenon plus a first-party MMLU
             demonstration. Its own experiment: five models across 8 prompt-format variations
             of MMLU (four subsets including global_facts).
Paraphrase:  The Hugging Face evaluation team shows that on MMLU, changing only the format of
             the multiple-choice prompt (same information) moves a single model's accuracy by
             about 10 points; Qwen1.5-7B swings from 22.9% on one variation to 51.2% on
             another. No model is ranked consistently across the eight formats "even though the
             only difference is their format, not the information itself." Shuffling few-shot
             example order alone moves the same model by up to 3 points. The post cites
             FormatSpread as the systematic version of this measurement and proposes structured
             generation (the Outlines library) as a mitigation that both raises accuracy and
             cuts variance. Treat the MMLU figures as a first-party demonstration and the
             framing as secondary.
Locators:    Sections "Testing prompt format robustness" (the 8 MMLU variations, the Qwen1.5-7B
             22.9%/51.2% swing, the ~10-point and 3-point figures) and the FormatSpread
             mention.
Quote:       "no model is consistently ranked across prompts even though the only difference is
             their format, not the information itself."
```

```text
URL:         https://arxiv.org/abs/2401.00595
Kind:        primary. Mizrahi, Kaplan, Malkin, Dror, Shahaf, Stanovsky (Hebrew University of
             Jerusalem and University of Haifa) own this large-scale re-evaluation; TACL 2024.
Establishes: The breadth of the problem across many models and tasks, and that a single hand-
             picked benchmark prompt overstates a model's score. Scope: 6.5M instances, 20
             LLMs, 39 tasks, 3 benchmarks (including LMentry), with many instruction
             paraphrases per task.
Paraphrase:  Evaluating each task with one instruction template is brittle: "different
             instruction templates lead to very different results, both in terms of absolute
             performance, as well as relative ranking." Some tasks have paraphrase sets whose
             model rankings actually disagree (negative Kendall's tau). The original,
             hand-written benchmark prompt tends to flatter a model: for OpenAI's davinci, the
             original prompts add, on average, 21 more accuracy points than the average across
             all paraphrases (their Figure 6). This is the "single prompt overestimates" number
             and a caution the writer can use directly.
Locators:    Abstract (6.5M / 20 LLMs / 39 tasks; absolute and ranking brittleness); §on
             ranking (negative Kendall's tau); Figure 6 and its text (davinci, 21 accuracy
             points).
Quote:       "different instruction templates lead to very different results, both in terms of
             absolute performance, as well as relative ranking."
Quote:       "the original prompts added, on average, 21 more accuracy points compared to the
             estimated average across all paraphrases."
```

## Contradictions

The literature disagrees on how large the effect is in today's frontier models, and this is the commission's open point.

- Persists vs. artifact. Sclar et al. and Su et al. both report that sensitivity does not shrink with scale or instruction tuning, and Su et al. still see plus or minus 23% on MMLU in 2024-2025 Llama/Qwen/Gemma models. Hua et al. (EMNLP 2025) push back: on multiple-choice and short-answer benchmarks, most of the measured spread comes from the grader, not the model. When they grade GPT-4o-mini, Gemini 2.0 Flash, LLaMA-3.1, Qwen-2, Gemma-2 and Ministral outputs with an LLM judge instead of log-likelihood or exact matching, Gemma-2's ARC-Challenge spread falls from 0.25-0.90 (std 0.28) to 0.17 (std 0.005) and cross-prompt rank correlation rises from 0.30 to 0.92. This does not overturn the mechanism: the model still generates from the literal tokens, and Hua et al.'s reduction is specifically about how a constrained answer is scored, not about free generation. It does undermine any claim that a 2025 chat model shows 76-point swings in normal use. The honest reading: token-level conditioning is settled; the magnitude in frontier models is contested and depends heavily on how output is scored.

- This maps onto the commission's own caution. The commission asks to keep "the model is genuinely worse" separate from "the surface form moved the score." Hua et al. add a third case the writer must not collapse into the first two: "the score moved because the grader missed a correct answer phrased differently." The 76-point and 54%-to-93% figures are measured under log-likelihood or exact-match scoring of constrained outputs, which is exactly the regime Hua et al. say inflates the number.

- Mitigations reduce but do not remove. Zhao et al.'s contextual calibration improves accuracy up to 30.0% absolute and cuts variance, and presents itself as a fix. Lu et al. test calibration directly and report that "although calibration leads to much higher performance, the variance remains high" (their Fig 6). So calibration is a real but partial mitigation, and the two primaries phrase its success differently.

- Meaning vs. surface, a nuance the writer should not flatten. The commission frames the mechanism as "semantically equivalent prompts are not equivalent inputs." Webson & Pavlick establish the converse just as firmly: semantically different (even nonsensical) instructions are often near-equivalent inputs, while the choice of answer token is not. Both facts point to the same cause (the model keys on token strings, not on an extracted meaning), but a writer who only says "surface form matters" misses that scrambling the semantic content of an instruction frequently does not matter.

## Numbers

```text
Figure: up to 76 accuracy points of spread between equivalent formats
Owner:  Sclar et al. 2024 (FormatSpread), arXiv:2310.11324
Scope:  LLaMA-2-13B, few-shot, SuperNaturalInstructions classification tasks; ~10 points on
        average across 50+ tasks and several models; median spread 7.5 across model/shot
        choices; scored by probability ranking / exact prefix matching.
```

```text
Figure: 0.043 vs 0.826 accuracy (diff 0.783) from one format change
Owner:  Sclar et al. 2024, Table 1 and Figure 1
Scope:  1-shot LLaMA-2-7B, task280 (a StereoSet-inspired stereotype-classification task from
        SuperNaturalInstructions). p1 = passage:{}\n answer:{} ; p2 = passage {}\n answer {} .
        The only change is the descriptor separator, a colon vs a space, on both descriptors.
        This is the writer's worked example. Note it is 7B, not the 13B that owns the 76-point
        headline; the two must not be merged.
```

```text
Figure: further Table 1 atomic-change pairs (probability ranking)
Owner:  Sclar et al. 2024, Table 1
Scope:  task317: Passage::{} Answer::{} = 0.076 vs Passage:: {} Answer:: {} = 0.638 (adding a
        space after "::"), diff 0.562. task322: COMMENT: {} ANSWER: {} = 0.614 vs comment: {}
        answer: {} = 0.714 (casing only), diff 0.100. Same 1-shot LLaMA-2-7B setting as task280.
```

```text
Figure: GPT-3.5-Turbo spread up to 56 points, median 6.4
Owner:  Sclar et al. 2024
Scope:  API-gated GPT-3.5-Turbo, across 320 formats and 53 tasks, exact prefix matching.
```

```text
Figure: over 85% vs around 50% accuracy across orderings of the same examples
Owner:  Lu et al. 2022, SST-2, Figure 1
Scope:  4 few-shot examples, 24 orderings, GPT-2 and GPT-3 family; GPT2-XL (1.5B) can exceed
        90% on a good order. "over 85%" = comparable to supervised training; "around 50%" =
        random on binary sentiment.
```

```text
Figure: 0.05 correlation of good orders between models
Owner:  Lu et al. 2022
Scope:  Permutation-performance correlation between GPT-3 175B and GPT-3 2.7B; shows a good
        order does not transfer across models.
```

```text
Figure: 54% -> 93% accuracy from reordering the same examples
Owner:  Zhao et al. 2021 (Calibrate Before Use), arXiv:2102.09690
Scope:  A sentiment-analysis prompt, GPT-3; near-chance to near-state-of-the-art by permutation
        alone. Contextual calibration improves accuracy up to 30.0% absolute across tasks.
```

```text
Figure: +/-23% MMLU swing from the single separator character
Owner:  Su et al. 2025, arXiv:2510.05152
Scope:  MMLU, Llama/Qwen/Gemma families; effect "doesn't improve with scale"; enough to reorder
        the model ranking.
```

```text
Figure: ARC-Challenge spread 0.25-0.90 (std 0.28) -> 0.17 (std 0.005) under LLM-as-judge
Owner:  Hua et al. 2025 (Flaw or Artifact?), arXiv:2509.01790
Scope:  Gemma-2, 12 templates; rank correlation across prompts 0.30 -> 0.92 (open models),
        NarrativeQA 0.40 -> 0.87. The contradiction figure: shows much of the spread is a
        scoring artifact for modern models.
```

```text
Figure: original benchmark prompts add ~21 accuracy points over the paraphrase average
Owner:  Mizrahi et al. 2024, arXiv:2401.00595, Figure 6
Scope:  OpenAI davinci, averaged over instruction paraphrases across tasks. Quantifies how much
        a single hand-picked prompt overstates a model's score. Some tasks show negative
        Kendall's tau, i.e. paraphrases flip the model ranking.
```

```text
Figure: Qwen1.5-7B 22.9% vs 51.2% across MMLU formats; ~10-point per-model swing; 3-point
        few-shot-order swing
Owner:  Hugging Face evals team (Kurt, Louf, Fourrier), 30 April 2024 (first-party demo)
Scope:  5 models, 8 MMLU prompt-format variations. Accessible corroboration, not a core owner.
```

## Source assets

```text
Asset: Figure 1 in Sclar et al. 2024 (arXiv:2310.11324), the task280 spread panel.
Shows: For one task, the distribution of accuracy across many "equivalent" formats, with the
       0.043 and 0.826 endpoints marked; the reader sees a wide band from one axis change.
Crop:  Must retain the accuracy axis with both endpoints and the two labelled format strings.
       Must retain that this is 1-shot LLaMA-2-7B on task280, or a caption that says so, so the
       figure is not read as the 13B 76-point result.
```

```text
Asset: Table 1 in Sclar et al. 2024, the atomic-change examples.
Shows: Pairs of near-identical format strings with their two accuracies and the difference; the
       clearest single-image proof that a colon-vs-space or casing change moves the score.
Crop:  Keep the format strings legible character-for-character (the colon, the space, the \n)
       and the paired accuracies. A crop that blurs the exact characters destroys the point.
```

```text
Asset: Figure 1 in Lu et al. 2022 (arXiv:2104.08786), 4-shot performance across 24 orders for
       GPT-2 and GPT-3 sizes on SST-2 and Subj.
Shows: The same examples, reordered, spanning from near random to above 85%, and that larger
       models do not collapse the spread.
Crop:  Keep the y-axis (accuracy) and the per-model-size grouping; the across-sizes comparison
       is the argument, so do not crop to a single model.
```

```text
Asset: The delimiter/attention figure in Su et al. 2025 (arXiv:2510.05152).
Shows: MMLU accuracy by delimiter choice across Llama/Qwen/Gemma, and attention-head scores
       shifting with the delimiter. Ties the surface change to where the model looks.
Crop:  If used, keep the delimiter labels (comma, newline, semicolon, hashtag) and the accuracy
       axis; the attention panel needs its token labels to be readable or it is decorative.
```

```text
Asset: The MMLU-format-spread plot in the Hugging Face blog (evaluation-structured-outputs).
Shows: Per-model accuracy across the 8 formats, including the Qwen1.5-7B collapse to 22.9%.
       An accessible, non-paper visual for a general reader.
Crop:  Keep the model labels and the accuracy axis; the crossing lines (rank instability) are
       the point, so do not crop to one model.
```

## Discarded

```text
URL: generic tokenization explainers (Infosys, DEV.to, Medium, Traceloop pages surfaced in
     search) — rejected as secondary sources: blog-level, no measurements, and they restate
     tokenization without owning any prompt-sensitivity claim. The already-taught
     word-embeddings and in-context-learning lessons cover this ground for the reader.
```

```text
URL: https://www.emergentmind.com/papers/2310.11324 — rejected: an auto-generated summary
     aggregator of FormatSpread, adds nothing over the primary and is not a source to stand
     behind.
```

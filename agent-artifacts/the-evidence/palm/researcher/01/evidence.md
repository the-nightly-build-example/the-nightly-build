# Evidence: the-evidence/palm (01)

The evidence supports the commission's "large but undertrained" angle on the
numbers that matter most. PaLM's own paper reports 540.35 billion parameters
trained on 780 billion tokens, a ratio of 1.44 tokens per parameter. The
Chinchilla paper, posted seven days earlier, prescribes roughly 20 tokens per
parameter, and its Table 3 puts the compute-optimal token budget for a 520B
model at 11.0 trillion tokens. So PaLM was trained on about one-fourteenth of
the tokens Chinchilla's rule would prescribe for its size. Both figures come
from the primaries that own them. Where the evidence is thin, or where it
complicates the angle rather than confirming it, is on three points the writer
must handle carefully: the chain-of-thought headline (PaLM's best-known GSM8K
number needed an external calculator, and plain chain-of-thought scored below
the prior state of the art), the meaning of "undertrained" (PaLM still beat the
smaller Chinchilla on downstream tasks, because it used more compute, so
"undertrained" names inefficiency, not weakness), and the emergence claim (the
paper reports discontinuous jumps, and a later rebuttal argues those jumps are
an artifact of the metric). The two named per-task discontinuity examples were
read off a figure and should be reconfirmed against Figure 5 before the writer
prints exact per-task percentages. Everything else below is textual and checked.

## Sources

```text
URL:         https://arxiv.org/abs/2204.02311
Kind:        primary. Chowdhery et al. authored PaLM and own every figure about
             what they built, trained, and measured.
Establishes: PaLM's scale, training data, hardware, efficiency, and headline
             results, firsthand.
Paraphrase:  Google Research trained a 540-billion-parameter, densely activated,
             autoregressive Transformer ("Pathways Language Model") on 780
             billion tokens using 6144 TPU v4 chips across two Pods. The paper
             reports smaller 8B and 62B variants trained on the same data,
             model-FLOPs-utilization of 46.2%, and results on English NLP tasks,
             BIG-bench, and chain-of-thought reasoning.
Locators:    Abstract; Section 3 and Table 1 (sizes, tokens); Table 2 (data mix);
             Section 4 and Section 4.1 (hardware, MFU); Section 6.1 (English NLP);
             Section 6.2 and Figure 5 (BIG-bench, discontinuities); Section 6.3.1
             and Table 10 (GSM8K).
Quote:       "we trained a 540-billion parameter, densely activated, Transformer
             language model, which we call Pathways Language Model PaLM."
             (Abstract)
```

```text
URL:         https://arxiv.org/abs/2203.15556
Kind:        primary. Hoffmann et al. (DeepMind) own the compute-optimal finding
             and the token estimates it produces.
Establishes: The compute-optimal scaling rule, the tokens-per-parameter guidance,
             and the specific token budget a 520B model should receive, firsthand.
Paraphrase:  Training over 400 models from 70M to 16B parameters, the authors
             find that model size and training-token count should grow in
             roughly equal proportion as the compute budget grows. They conclude
             that current large models are significantly undertrained. Their own
             model, Chinchilla (70B parameters, 1.4 trillion tokens), matches
             Gopher's compute budget with four times the data and outperforms it.
Locators:    Abstract; Table 1 (Chinchilla 70B / 1.4T); Table 2 (scaling
             exponents a and b); Table 3 (optimal FLOPs and tokens by size);
             Section 3.4 (models are "considerably over-sized").
Quote:       "we find that for compute-optimal training, the model size and the
             number of training tokens should be scaled equally." (Abstract)
```

```text
URL:         https://arxiv.org/abs/2305.10403
Kind:        primary. The PaLM 2 Technical Report is Google's own account of
             PaLM's successor.
Establishes: That PaLM 2 does not publish a parameter count; that PaLM 2-L is
             smaller than 540B PaLM; that PaLM 2 adopts Chinchilla-style 1:1
             scaling. All firsthand from the authoring party.
Paraphrase:  The report states data and model size should be scaled roughly 1:1,
             that D and N should grow in equal proportions as the FLOPs budget
             increases, and that the largest model, PaLM 2-L, is significantly
             smaller than the largest PaLM. It gives no parameter count for any
             PaLM 2 model.
Locators:    Abstract (compute-efficiency); scaling-law section (1:1 scaling,
             PaLM 2-L smaller than PaLM).
Quote:       "The largest model in the PaLM 2 family, PaLM 2-L, is significantly
             smaller than the largest PaLM model but uses more training compute."
             (paraphrased from the scaling section; writer should quote exact
             line from the report before printing)
```

```text
URL:         https://arxiv.org/abs/2312.11805
Kind:        primary. The Gemini 1.0 technical report is Google DeepMind's own
             account.
Establishes: That Gemini publishes parameter counts only for its two Nano
             variants, and withholds them for Ultra and Pro.
Paraphrase:  Gemini 1.0 comprises three sizes: Ultra, Pro, and Nano. Only the
             Nano sizes carry disclosed parameter counts: Nano-1 at 1.8B and
             Nano-2 at 3.25B parameters. No parameter count is given for Ultra or
             Pro.
Locators:    Model-sizes section / Table 1 (Nano-1 1.8B, Nano-2 3.25B).
Quote:       "We trained two versions of Nano ... with 1.8B (Nano-1) and 3.25B
             (Nano-2) parameters."
```

```text
URL:         https://arxiv.org/abs/2206.07682
Kind:        primary to the emergent-abilities claim. Wei et al. define the term
             and make the claim the article treats as a claim to test.
Establishes: The definition of an emergent ability and the claim that some
             abilities appear suddenly at scale, unpredictable from smaller
             models.
Paraphrase:  An ability is emergent if it is not present in smaller models but is
             present in larger ones. The paper argues such abilities cannot be
             predicted by extrapolating the performance of smaller models, and
             that scale unlocks them discontinuously.
Locators:    Abstract; the definition sentence early in the paper.
Quote:       "An ability is emergent if it is not present in smaller models but
             is present in larger models."
```

```text
URL:         https://arxiv.org/abs/2304.15004
Kind:        primary to the rebuttal. Schaeffer, Miranda, and Koyejo (Stanford)
             own the counter-argument.
Establishes: The claim that emergent abilities are largely an artifact of the
             chosen metric, not a fundamental property of scale.
Paraphrase:  The authors argue that nonlinear or discontinuous metrics, such as
             exact-match accuracy, produce apparent emergent abilities, while
             linear or continuous metrics show smooth, predictable improvement.
             They attribute the phenomenon to the researcher's choice of metric
             rather than to a change in model behavior, and report that alleged
             emergent abilities disappear under different metrics or better
             statistics. They discuss GPT-3-family models and BIG-bench.
Locators:    Abstract.
Quote:       "emergent abilities appear due to the researcher's choice of metric
             rather than due to fundamental changes in model behavior with
             scale." (per the abstract; writer should quote the exact line)
Note:        Widely reported as accepted to NeurIPS 2023. Venue not verified from
             the arXiv record here; confirm before printing "NeurIPS 2023."
```

```text
URL:         https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/
Kind:        secondary for reception, primary for Google's framing. The blog is
             Google's own announcement, so it owns how Google chose to present
             PaLM, but it reports the paper's technical claims secondhand.
Establishes: How PaLM was framed on release ("breakthrough performance,"
             "state-of-the-art few-shot performance") and the 28-of-29 English
             NLP claim in plain form. Useful for "where citations outrun the
             paper."
Paraphrase:  Published April 4, 2022. Google framed PaLM as achieving
             "breakthrough performance" and "breakthrough capabilities on
             reasoning tasks." It states PaLM 540B surpassed prior large models
             on 28 of 29 English NLP tasks and beat average human performance on
             BIG-bench tasks. Notably, the blog describes "log-linear behavior
             similar to prior models" and says performance "has not yet
             plateaued," and does not use the word "discontinuous."
Locators:    Title; body paragraphs on English NLP tasks, BIG-bench, and scaling.
Quote:       "PaLM 540B 5-shot also does better than the average performance of
             people asked to solve the same tasks."
```

## Contradictions

1. **The chain-of-thought headline needs an asterisk.** PaLM's widely cited
   GSM8K result is 58%, but the paper reaches that only with an external
   calculator (Section 6.3.1, Table 10). Plain 8-shot chain-of-thought scored
   54%, which is below the prior state of the art of 55% (Cobbe et al. 2021,
   which used finetuning, chain-of-thought, a calculator, and a verifier). A
   citation that credits PaLM with beating the GSM8K state of the art through
   chain-of-thought alone outruns the paper. The calculator is doing part of the
   work.

2. **Google's own framing avoids the emergence language.** The paper reports
   discontinuous jumps on a quarter of BIG-bench tasks (Section 6.2), yet the
   announcement blog describes scaling as "log-linear behavior similar to prior
   models" and never says "discontinuous." The tension is inside Google's own
   materials, not only between Google and outside critics.

3. **Emergence contested at the root.** Wei et al. (2206.07682) present abilities
   that appear suddenly at scale as a real property. Schaeffer et al.
   (2304.15004) argue the suddenness is produced by discontinuous metrics like
   exact-match accuracy, and that continuous metrics show smooth improvement.
   PaLM's discontinuity finding rests on accuracy-style metrics across BIG-bench,
   so the rebuttal bears on PaLM directly, even though it centers its examples on
   GPT-3-family models. Present PaLM's jumps as a claim, then the challenge.

4. **"Undertrained" is not "underperforming."** PaLM was trained on far fewer
   tokens than Chinchilla's rule prescribes, yet PaLM 540B outperformed the much
   smaller Chinchilla on downstream tasks, because it spent more compute overall.
   Chinchilla's point is that the same compute would have gone further with a
   smaller model and more data. The writer must not let "undertrained" imply PaLM
   was weak; it was inefficient by the compute-optimal standard, and still strong
   in absolute terms.

5. **PaLM could not have used Chinchilla's result.** Chinchilla was posted to
   arXiv on 29 March 2022 and PaLM on 5 April 2022, seven days apart. PaLM's
   training predates any chance to apply Chinchilla's finding. The "undertrained"
   reading is retrospective. PaLM's authors were pursuing scale, not ignoring a
   published correction, because the correction was effectively simultaneous.

## Numbers

```text
Figure: 540.35 billion parameters (PaLM 540B)
Owner:  PaLM paper, Table 1
Scope:  Total parameters, largest PaLM model. Smaller variants: 8.63B and 62.50B.
```

```text
Figure: 780 billion training tokens
Owner:  PaLM paper, Section 3 / Table 1
Scope:  Full training corpus for all three PaLM sizes. Mix: social-media
        conversations 50%, filtered webpages 27%, books 13%, GitHub code 5%,
        Wikipedia 4%, news 1% (Table 2).
```

```text
Figure: 1.44 tokens per parameter (PaLM 540B)
Owner:  Derived from PaLM's own figures: 780B / 540.35B = 1.443.
Scope:  A ratio computed from two PaLM-owned numbers, not a figure PaLM prints.
```

```text
Figure: ~20 tokens per parameter (Chinchilla, compute-optimal)
Owner:  Chinchilla paper, Table 1: 70B parameters, 1.4 trillion tokens; 1.4T /
        70B = 20.0.
Scope:  Chinchilla's own model, offered as the compute-optimal exemplar.
```

```text
Figure: 11.0 trillion tokens (compute-optimal for a 520B model)
Owner:  Chinchilla paper, Table 3, row for 520B parameters (3.43e25 FLOPs).
Scope:  The estimated optimal token budget for a model near PaLM's size. PaLM is
        540B, just above this row, so its optimal budget is ~11T or slightly
        more. PaLM's actual 780B tokens is about 1/14 of this (11.0T / 780B =
        14.1x). This is the core of the "undertrained" argument.
```

```text
Figure: 4.2 trillion tokens (compute-optimal for a 175B model)
Owner:  Chinchilla paper, text example (4.41e24 FLOPs). Note: Table 3's 175B row
        reads 3.7 trillion tokens; the text example uses a slightly larger
        compute budget, hence the difference. Cite the number to its exact
        context.
```

```text
Figure: 6.8 trillion tokens (compute-optimal for a 280B Gopher-like model)
Owner:  Chinchilla paper, text ("should be trained on 6.8 trillion tokens" at
        ~1e25 FLOPs). Table 3's 280B row reads 5.9 trillion; same table-vs-text
        distinction as above. Use with its stated compute budget.
```

```text
Figure: 46.2% model-FLOPs-utilization (MFU); 57.8% hardware-FLOPs-utilization
Owner:  PaLM paper, Section 4.1 (this lesson names MFU only; do not re-teach it,
        link the-instruments/model-flops-utilization).
Scope:  PaLM 540B. Reported comparators: GPT-3 21.3%, Gopher 32.5%,
        Megatron-Turing NLG 30.2%. These are PaLM's own engineering claims.
```

```text
Figure: 6144 TPU v4 chips, two Pods
Owner:  PaLM paper, Section 4 / Abstract. 12-way model parallelism, 256-way
        fully-sharded data parallelism.
Scope:  Training hardware for PaLM 540B. PaLM's own engineering claim.
```

```text
Figure: BIG-bench: 150 tasks total; 58 tasks common with prior models
Owner:  PaLM paper, Section 6.2
Scope:  PaLM 540B 5-shot beat the prior state of the art on 44 of the 58 common
        tasks.
```

```text
Figure: Discontinuity: 25% of 150 tasks jumped >+10%, 15% jumped >+20%
Owner:  PaLM paper, Section 6.2 ("Over all 150 tasks, 25% of tasks had
        discontinuity greater than +10%, and 15% of tasks had a discontinuity
        greater than +20%").
Scope:  Improvement from 62B to 540B, contrasted with 8B to 62B. This is the
        textual, verified discontinuity claim. Prefer it over per-task numbers.
```

```text
Figure: Human comparison on BIG-bench
Owner:  PaLM paper, Section 6.2
Scope:  5-shot PaLM 540B scores higher than the average human on the aggregate;
        average human still beats PaLM 540B on 35% of individual tasks.
```

```text
Figure: GSM8K: 54% (8-shot chain-of-thought, no calculator); 58% (with external
        calculator); prior SOTA 55% (Cobbe et al. 2021)
Owner:  PaLM paper, Section 6.3.1 / Table 10
Scope:  PaLM 540B. See Contradiction 1: the 58% headline requires the calculator;
        plain chain-of-thought (54%) is below the 55% prior state of the art.
```

```text
Figure: 28 of 29 English NLP tasks outperformed
Owner:  PaLM paper, Section 6.1; restated in Google's blog.
Scope:  PaLM 540B few-shot vs prior large models (GLaM, GPT-3, Megatron-Turing
        NLG, Gopher, Chinchilla, LaMDA).
```

```text
Figure: PaLM 2 and Gemini parameter counts: not disclosed for flagship models
Owner:  PaLM 2 report (2305.10403) gives no parameter count and states PaLM 2-L
        is smaller than PaLM; Gemini report (2312.11805) discloses only Nano-1
        (1.8B) and Nano-2 (3.25B), not Ultra or Pro.
Scope:  Confirms the commission's instruction: do not cite a rumored count. The
        record here is the absence of a published number.
```

## Source assets

```text
Asset: PaLM paper, Figure 5 (representative BIG-bench tasks, accuracy vs model
       scale for 8B, 62B, 540B).
Shows: The discontinuous jump from 62B to 540B on selected tasks, the visual
       backbone of the emergence claim.
Crop:  Must retain the three scale points on the x-axis and the y-axis accuracy
       label so the jump is legible. Keep task names if shown. Do not crop out
       the axis that makes the jump measurable.
```

```text
Asset: Chinchilla paper, Table 3 (estimated optimal FLOPs and tokens by model
       size).
Shows: That a model near PaLM's size should receive ~11 trillion tokens, set
       against PaLM's 780 billion. Carries the "undertrained" argument better
       than prose.
Crop:  Must retain the parameter column and the tokens column, and at least the
       520B row. Retaining the 175B, 280B, and 1T rows shows the trend. Omit the
       FLOPs column only if space demands; the tokens column is the point.
```

```text
Asset: PaLM paper, Table 1 (model sizes: layers, heads, parameters, tokens).
Shows: The three PaLM sizes trained on one shared 780B-token corpus, and the
       540B headline figure.
Crop:  Retain the parameter and token columns for all three sizes.
```

```text
Asset: PaLM paper, Section 4.1 MFU comparison (PaLM vs GPT-3, Gopher, MT-NLG).
Shows: PaLM's 46.2% MFU against lower prior figures, its engineering claim.
Crop:  Retain the model names and the MFU column. This lesson names MFU only;
       the asset supports one sentence, not a re-teaching.
```

## Discarded

```text
URL: TechCrunch and Twitter reports of rumored PaLM 2 parameter counts (14.7B or
     ~100B), surfaced in search snippets. Rejected: rumor, not a published
     figure. The commission requires recording the absence of a count, not a
     rumor.
URL: https://www.lesswrong.com/posts/mLuQfS7gmfr4nwTdv/ (community commentary on
     PaLM). Not opened beyond the snippet. Rejected: informal secondary; the
     Google blog covers reception with a verifiable primary framing.
URL: https://towardsdatascience.com/a-new-ai-trend-chinchilla-70b-... Rejected:
     secondary explainer; Chinchilla's numbers are taken from the paper directly.
URL: https://typefully.com/BlancheMinerva/... (Stella Biderman thread). Rejected:
     informal secondary; not needed once the token math is sourced to primaries.
URL: https://slator.com/the-great-language-model-scale-off-googles-palm/ and
     https://www.marktechpost.com/... Rejected: trade-press summaries; add no
     figure the primaries do not own.
```

## Production record

Running as Claude Opus 4.8 (model id claude-opus-4-8), effort=high. Production
policy for this stage: researcher, model "capable," effort high; nothing marked
required, no deviation to report.

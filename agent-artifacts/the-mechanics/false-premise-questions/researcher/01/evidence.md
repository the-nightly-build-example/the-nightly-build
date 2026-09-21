# Evidence record: the-mechanics/false-premise-questions (01)

The evidence supports the commissioned angle and refines one link in it. Four
datasets built from real user questions (CREPE, (QA)², FalseQA, Cancer-Myth)
show that models answer questions carrying a false or questionable assumption
instead of challenging it, with measured failure rates tied to named models. The
autoregressive next-token objective (GPT-3) and preference-based post-training
(InstructGPT) are documented firsthand, so the "settled" half of the chain is
well-sourced. The "open" half is richly sourced and cuts two ways: FalseQA shows
models already hold the knowledge to rebut these questions and can be taught to
do so with 256 examples, newer models correct far more often than GPT-4o did,
and a 2026 study shows that bolting on premise-rejection degrades ordinary QA.
The record's one real weakness is the second mechanism claim: no source I found
directly measures how often premise-corrections appear in pretraining text. That
step is supported indirectly (models have the knowledge but default to
answering; the natural forum distribution follows questions with answers, not
corrections), not by a corpus frequency count. One nuance the writer must not
skip: CREPE and Kim 2021 locate much of the residual difficulty in *verifying*
that a premise is false, not in *noticing* the presupposition. That refines the
"conditions on it as given and never corrects" story rather than overturning it.

## Sources

```text
URL:         https://arxiv.org/abs/2101.00391
Kind:        primary — Kim, Pavlick, Karagol Ayan & Ramachandran own this
             framework and the Natural Questions analysis (ACL 2021,
             https://aclanthology.org/2021.acl-long.304/).
Establishes: That failed/unverifiable presuppositions are a measurable cause of
             unanswerable questions, and that verification (not detection) is the
             bottleneck for handling them.
Paraphrase:  Analyzing unanswerable questions in Natural Questions, about 21% are
             explained by the presence of unverifiable presuppositions. The
             authors propose a three-step pipeline (generate presuppositions,
             verify them, explain). Adding presuppositions and their verifiability
             to a model yields modest gains in downstream performance and
             unanswerability detection, but the verification component is the
             bottleneck: even transfer from the best entailment models falls short.
Locators:    Abstract; Natural Questions unanswerable analysis.
Quote:       "a substantial portion of unanswerable questions (~21%)" arise from
             "unverifiable presuppositions"; "even transfer from the best
             entailment models currently falls short."
```

```text
URL:         https://arxiv.org/abs/2212.10003
Kind:        primary — Kim, Htut, Bowman & Petty own the (QA)² dataset and the
             end-to-end human-rated evaluation (ACL 2023,
             https://aclanthology.org/2023.acl-long.472/).
Establishes: That current models handle questionable-assumption questions worse
             than ordinary questions, measured by human acceptability, and that
             in-context demonstrations narrow but do not close the gap.
Paraphrase:  (QA)² is 602 naturally occurring search-engine questions, half
             (301) carrying questionable assumptions and half (301) not, plus a
             32-question adaptation set. Answers were rated for acceptability by
             human raters (majority vote). Zero-shot, models score far lower on
             questionable-assumption questions than on valid ones. In-context
             demonstrations raise the questionable-assumption scores. The best
             configuration reaches only 56% acceptability on the full set,
             leaving large headroom.
Locators:    Abstract; dataset-composition section; main results table
             (per-model acceptability, questionable vs valid).
Quote:       Zero-shot text-davinci-003: 0.40 (questionable) vs 0.56 (valid);
             Flan-T5-XXL: 0.10 vs 0.22; best overall "56% human-judged
             acceptability" for text-davinci-003 with in-context demonstrations.
```

```text
URL:         https://arxiv.org/abs/2211.17257
Kind:        primary — Yu, Min, Zettlemoyer & Hajishirzi own the CREPE dataset
             and baselines (ACL 2023, https://aclanthology.org/2023.acl-long.583/).
Establishes: How common false presuppositions are in a natural question stream,
             and that models detect presuppositions moderately well but struggle
             to verify whether the presupposition is factually false — locating
             the bottleneck at verification/retrieval, not detection.
Paraphrase:  CREPE is 8,466 labeled questions drawn from the ELI5 subreddit; 26.0%
             (2,202) rest on a false presupposition, each annotated with the
             presupposition and its correction. Detecting whether a question has a
             false presupposition sits near 66–67% F1 from the question alone and
             rises to 75.6% F1 when a human comment is supplied; the generation of
             a correct correction is weak (about 1.8 on a 0–3 scale versus 2.8 for
             reference answers). The authors attribute the difficulty largely to
             retrieving relevant evidence.
Locators:    Abstract; dataset statistics; detection and writing results tables.
Quote:       "adaptations of existing open-domain QA models can find
             presuppositions moderately well, but struggle when predicting whether
             a presupposition is factually correct."
```

```text
URL:         https://arxiv.org/abs/2307.02394
Kind:        primary — Hu, Luo, Wang, Cheng, Liu & Sun own the FalseQA dataset and
             experiments (ACL 2023, https://aclanthology.org/2023.acl-long.309/).
Establishes: The strongest contradiction to a pure "can't do it" reading: large
             models fail these questions zero-shot, yet already hold the knowledge
             to rebut them, and moderate fine-tuning (256 examples) activates it.
             This is the key evidence for the open part.
Paraphrase:  FalseQA is 2,365 human-written false-premise questions with
             explanations and revised true-premise counterparts. Zero-shot, very
             large models (Bloom 176B, OPT 175B, GPT-3 175B, Jurassic-1 178B) fail
             the simple false-premise questions, and Macaw-11B answered one of nine
             tricky questions correctly. After fine-tuning on 256 question pairs,
             discrimination climbs sharply and models generate reasonable rebuttal
             explanations. The authors argue the models already possess the needed
             knowledge; the problem is activating it.
Locators:    Abstract; Section 3.2 pilot; fine-tuning results table (Table 7).
Quote:       "PLMs already possess the knowledge required to rebut such questions,
             and the key is how to activate the knowledge." Fine-tuned on 256
             pairs: OPT-2.7B 67.8% accuracy, Macaw-3B 76.5%, Macaw-11B 79.2%.
```

```text
URL:         https://arxiv.org/abs/2505.22354
Kind:        primary — Sieker, Lachenmaier & Zarrieß own this evaluation
             (part of the FLEX benchmark).
Establishes: That recent instruction-tuned models still mostly fail to reject
             false presuppositions, in a high-stakes (political misinformation)
             setting, and that failure varies with how the presupposition is
             phrased.
Paraphrase:  Testing GPT-4o, LLaMA-3-8B, and Mistral-7B-v0.3 on politically loaded
             questions with false presuppositions, the models struggle to
             recognize the false presuppositions, with performance varying by
             linguistic construction, party, and scenario probability. The concern
             is that models, like people, fail to correct misleading assumptions
             introduced as presuppositions even when misinformation stakes are high.
Locators:    Abstract; results by condition.
Quote:       "the models struggle to recognize false presuppositions, with
             performance varying by condition."
```

```text
URL:         https://arxiv.org/abs/2504.11373
Kind:        primary — Zhu, Chen, Yu, Lin, Law, Jizzini, Nieva, Liu & Jia own the
             Cancer-Myth benchmark (first author Wang Bill Zhu; oncologist Jorge J.
             Nieva; senior author Robin Jia). Published at ICLR 2026.
Establishes: The newest, current-model measurement: even 2025-era frontier models
             correct false presuppositions in patient questions less than half the
             time, and answer quality is otherwise high — so the gap is about
             challenging the premise, not general accuracy. Per-model numbers also
             show newer models beat GPT-4o by a wide margin.
Paraphrase:  Cancer-Myth is 585 expert-verified cancer questions containing false
             presuppositions (plus a 150-question no-false-presupposition control),
             built with an iterative adversarial generation pipeline. No frontier
             model corrects the false presupposition more than about 43% of the
             time. Correction rates read from the results table: GPT-5 42.1%,
             Gemini-2.5-Pro 41.4%, Claude-4-Sonnet 40.0%, Gemini-1.5-Pro 27.2%,
             Gemma-2-27B 17.3%, DeepSeek-R1 13.7%, GPT-4o 5.8%. General answer
             quality is high (GPT-4-Turbo rated 4.13/5), so failing to challenge
             the premise is a distinct failure from being wrong.
Locators:    Abstract; per-model results table (read from arXiv HTML v2); dataset
             construction section.
Quote:       "no frontier LLM -- including GPT-5, Gemini-2.5-Pro, and
             Claude-4-Sonnet -- corrects these false presuppositions more than 43%
             of the time."
```

```text
URL:         https://arxiv.org/abs/2608.06539
Kind:        primary — Wang, Shwartz & Gonen own this analysis.
Establishes: That the obvious fix has a cost: methods that reject false
             presuppositions better tend to wrongly reject true ones, degrading
             ordinary QA — and that benchmarks overweight false-premise questions
             relative to real use. Essential for the open section and for warning
             against a naive "just train it to reject" conclusion.
Paraphrase:  Titled "Don't 'Well, Actually' Me Unless You Know What You're Talking
             About: Weak Presupposition Verification Degrades General QA
             Performance." Across model families, sizes, and benchmarks, methods
             that do better on false-presupposition questions do worse on
             true-presupposition questions, because their fact-checking components
             also reject valid presuppositions. Benchmarks over-represent false
             presuppositions compared with real-world distributions.
Locators:    Abstract; cross-benchmark results.
Quote:       "methods that perform better on FPQs tend to perform worse on TPQs";
             this is "the result of weak fact checking modules that reject also
             true presuppositions."
```

```text
URL:         https://arxiv.org/abs/2005.14165
Kind:        primary — Brown et al. (OpenAI) own the description of GPT-3's
             training.
Establishes: The settled ground of the chain: these models are autoregressive
             next-token predictors trained over a large text corpus, so at
             inference they condition each next token on the tokens already in the
             prompt — the mechanism by which presupposed content is treated as
             given input.
Paraphrase:  "Language Models are Few-Shot Learners" describes GPT-3 as an
             autoregressive language model with 175 billion parameters, applied
             without gradient updates via text prompts. Autoregressive means each
             token is predicted from the preceding context.
Locators:    Abstract; model/approach description.
Quote:       GPT-3 is "an autoregressive language model with 175 billion
             parameters."
```

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — Ouyang et al. (OpenAI) own the InstructGPT method and
             results.
Establishes: The other settled step: post-training with human feedback optimizes
             for outputs humans prefer and find helpful/instruction-following. It
             does not, on its own account, install "reject the premise first."
Paraphrase:  "Training language models to follow instructions with human feedback"
             fine-tunes on human preference data so outputs align with user intent;
             labelers preferred the 1.3B InstructGPT model's outputs to those of
             the 175B GPT-3. The optimization target is helpfulness/preference, not
             premise-checking.
Locators:    Abstract.
Quote:       "outputs from the 1.3B parameter InstructGPT model are preferred to
             outputs from the 175B GPT-3, despite having 100x fewer parameters."
```

```text
URL:         https://www.cancertodaymag.org/spring-2026/a-digital-ally/
Kind:        secondary — a feature by science writer Stephen Ornes in Cancer Today
             (published by the American Association for Cancer Research), reporting
             on the USC Cancer-Myth study from outside the authoring team.
Establishes: Context only: that the Cancer-Myth finding has been reported for a
             general audience, and the plain-language framing that models fail to
             correct the myth in more than half of responses.
Paraphrase:  The article reports the USC study (released April 15, 2025) that
             posed more than 500 cancer questions containing myths to popular
             chatbots, and states that in more than half of the responses all the
             models failed to correct the errors.
Locators:    Body, USC study passage.
Quote:       "In more than half of their responses, all the models failed to
             correct the errors."
```

## Contradictions

The evidence does not undermine the angle, but four findings complicate the
simplest telling and belong in the open section.

- **Models already hold the knowledge and can be taught to use it (FalseQA).**
  The pretrained models fail these questions zero-shot yet can rebut them after
  fine-tuning on only 256 pairs, reaching 76–79% discrimination for models at 3B
  and 11B. This cuts against any claim that the behavior is intrinsic or
  unfixable. It supports the commission's framing that post-training does not
  *reliably* install premise-rejection, while showing the fix is not hard to
  install deliberately.

- **The bottleneck is often verification, not detection (CREPE, Kim 2021).**
  CREPE models find that a presupposition exists moderately well (66–76% F1) but
  are weak at judging whether it is false; Kim 2021 names verification as the
  component that "falls short." So the failure is not only "the predictor
  conditions on the premise and never notices it." For many questions the model
  can notice the presupposition and still lacks the grounded fact-check to call
  it false. The writer should present detection and verification as two steps.

- **Newer models correct far more often than older ones (Cancer-Myth).** GPT-4o
  corrected 5.8% of medical false presuppositions; GPT-5 reached 42.1%,
  Gemini-2.5-Pro 41.4%, Claude-4-Sonnet 40.0%. The behavior is improving with
  model generation, though it plateaus below half on adversarial medical cases.
  "Models never challenge the premise" is too strong for 2025-era systems.

- **The obvious fix degrades ordinary answering (Wang, Shwartz & Gonen 2026).**
  Making a model reject false presuppositions more often makes it wrongly reject
  true ones, hurting general QA, and the authors note benchmarks over-represent
  false-premise questions relative to real use. A closing section that ends on
  "just train it to reject premises" would contradict this result.

No source I read claims current models reliably reject false premises by default.
The disagreement is about degree, fixability, and where the difficulty sits, not
about the base behavior.

## Numbers

```text
Figure: ~21% of unanswerable questions attributable to unverifiable presuppositions
Owner:  Kim et al. 2021 (arXiv 2101.00391)
Scope:  Unanswerable questions in Natural Questions (Kwiatkowski et al. 2019)
```

```text
Figure: 602 questions total; 301 with questionable assumptions, 301 valid (+32 adaptation)
Owner:  (QA)² — Kim et al. 2023 (arXiv 2212.10003)
Scope:  Full (QA)² dataset of naturally occurring search-engine queries
```

```text
Figure: text-davinci-003 zero-shot acceptability 0.40 (questionable) vs 0.56 (valid); Flan-T5-XXL 0.10 vs 0.22; best config 56% overall
Owner:  (QA)² — Kim et al. 2023 (arXiv 2212.10003)
Scope:  Human acceptability (majority vote) on end-to-end QA over the eval set
```

```text
Figure: 8,466 questions; 26.0% (2,202) with false presuppositions
Owner:  CREPE — Yu et al. 2023 (arXiv 2211.17257)
Scope:  Questions sampled from the ELI5 subreddit
```

```text
Figure: false-presupposition detection F1 ~66.9% (question only) to 75.6% (with human comment); correction quality ~1.8 of 3
Owner:  CREPE — Yu et al. 2023 (arXiv 2211.17257)
Scope:  CREPE detection and correction-generation test sets
```

```text
Figure: 2,365 false-premise question pairs; fine-tuned on 256 pairs → OPT-2.7B 67.8%, Macaw-3B 76.5%, Macaw-11B 79.2% discrimination accuracy
Owner:  FalseQA — Hu et al. 2023 (arXiv 2307.02394)
Scope:  FalseQA discrimination task after fine-tuning on 256 pairs
```

```text
Figure: false-presupposition correction rate — GPT-5 42.1%, Gemini-2.5-Pro 41.4%, Claude-4-Sonnet 40.0%, Gemini-1.5-Pro 27.2%, Gemma-2-27B 17.3%, DeepSeek-R1 13.7%, GPT-4o 5.8%; none above ~43%
Owner:  Cancer-Myth — Zhu et al. 2025 (arXiv 2504.11373, ICLR 2026)
Scope:  585 expert-verified cancer questions with false presuppositions
```

```text
Figure: GPT-4-Turbo answer quality 4.13/5 despite low premise-correction
Owner:  Cancer-Myth — Zhu et al. 2025 (arXiv 2504.11373)
Scope:  Answer-quality rating on Cancer-Myth, distinct from correction rate
```

## Source assets

```text
Asset: (QA)² per-model acceptability results table (arXiv 2212.10003), questionable vs valid columns
Shows: The consistent gap where the same model scores lower once a question carries a questionable assumption — the behavior in one view.
Crop:  Keep both columns and model names; a one-column crop loses the comparison that is the point.
```

```text
Asset: A worked (QA)² / CREPE example question with its false presupposition and correction (e.g. "When did Marie Curie discover Uranium?"; CREPE ELI5 examples with annotated presupposition)
Shows: A concrete false-premise question the reader recognizes, with the assumption made explicit. Good for the lesson's grounding example. Verify the exact example against the paper before use.
Crop:  Retain the question plus the annotated presupposition/correction line.
```

```text
Asset: FalseQA fine-tuning results (arXiv 2307.02394, Table 7): zero-shot failure vs post-256-example accuracy
Shows: The same models moving from failing to ~76–79% once taught — the "fixable, and the knowledge was already there" evidence.
Crop:  Keep model rows and the accuracy/recall columns; retain the sample-count (256) label.
```

```text
Asset: Cancer-Myth per-model correction-rate figure/table (arXiv 2504.11373)
Shows: GPT-4o near the floor (5.8%) and 2025 frontier models clustered near 40%, none above ~43% — improvement plus a persistent ceiling in one chart.
Crop:  Keep all model bars and the axis; do not crop to only the top performers, which would hide the GPT-4o baseline.
```

```text
Asset: None found for GPT-3 (2005.14165) and InstructGPT (2203.02155) that carries this article's argument better than prose. Their contribution here is the stated training objective, not a figure.
```

## Discarded

```text
URL: https://arxiv.org/abs/2109.06987 (NOPE corpus): sound primary for the linguistic definition of presupposition triggers, but the Kim and (QA)² papers already own the definition this lesson needs; NOPE measures human presupposition inference, not QA behavior. Redundant, not contradictory.
URL: https://arxiv.org/abs/2305.14010 (IfQA): about counterfactual "if"-clause presuppositions the questioner marks as hypothetical, a different behavior from a smuggled false premise. Out of scope.
URL: https://theconversation.com/you-can-persuade-ai-models-to-accept-falsehoods-as-truth-study-shows-280989: authored by the study's own researcher (first-party, not secondary) and about persuasion across turns, which is sycophancy territory, a named neighbor to avoid.
URL: https://arxiv.org/abs/2504.09343 (confirmation-bias survey, Du): could serve as a secondary, but its focus is confirmation bias generally and I could not confirm on-topic false-premise coverage; the Cancer Today feature is a cleaner, verified secondary.
URL: https://www.nbcnews.com/health/... and the Lundquist/Harbor-UCLA BMJ Open cancer study: real journalism, but about "false balance" and accuracy in cancer advice, not the failure to challenge a question's built-in assumption. Different behavior.
URL: https://news.stanford.edu/stories/2025/11/ai-language-models-facts-belief-human-understanding-research: returned 403 (gated, not dead) and concerns fact-versus-belief, adjacent to but not the false-premise-answering behavior. Not pursued.
```

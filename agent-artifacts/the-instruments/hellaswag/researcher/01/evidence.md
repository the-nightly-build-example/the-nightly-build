# Evidence: the-instruments/hellaswag (01)

The evidence supports the commissioned arc in full. The construction is confirmed from both source papers: HellaSwag draws its contexts from ActivityNet video captions and WikiHow articles, generates wrong endings with OpenAI GPT, and keeps only endings that fool BERT-Large but not people, a procedure the predecessor SWAG paper named Adversarial Filtering. The measured human baseline (95.6%), the near-launch machine score (BERT-Large, 47.3%), and a current strong score (GPT-4, 95.3%, ten-shot) are each held by a primary that owns the figure. Saturation is documented at the source: HuggingFace named HellaSwag among the benchmarks models had "reached baseline human performance" on when it retired the benchmark from its leaderboard in 2024. Documented item errors are strong and specific: a 2025 validity paper and a Surge AI audit both quantify ungrammatical, ambiguous, and mislabeled items. One clean worked item and one flawed worked item are captured verbatim.

The record is thin in one place the writer must respect. The best-documented current score, GPT-4 at 95.3%, sits just below the 95.6% human baseline, not above it. The honest saturation claim is that top models are level with people and clustered within about a point, so the test no longer separates them, not that a verified single model has clearly passed the human number. The commission's phrase "climbed past the human number" overstates what the checked figures show. See Contradictions.

A second gap: the paper advertises "70k problems," but the released dataset has 59,950 rows. Both numbers are recorded below with their owners.

## Sources

```text
URL:         https://arxiv.org/abs/1905.07830
Kind:        primary. It is the HellaSwag paper (Zellers, Holtzman, Bisk, Farhadi, Choi, ACL 2019); it owns the benchmark, its construction, and the human baseline.
Establishes: The two context sources (ActivityNet Captions and WikiHow); the generator (OpenAI GPT, Radford et al. 2018) and the discriminator/filter (BERT-Large); the human accuracy (95.6% overall) and best machine accuracy (BERT-Large, 47.3% overall); the acronym; the "Goldilocks zone" of ~3 context sentences and 2 generated sentences.
Paraphrase:  Adversarial Filtering uses a language model to over-generate wrong endings, then a series of discriminators iteratively replaces easy-to-classify machine endings with harder ones until the discriminators can no longer tell machine endings from the real next caption. Applied with GPT as generator and BERT-Large as filter over WikiHow and ActivityNet text, the result is trivial for humans (95.6%) and hard for 2019 models (<48%). The authors frame the paper as a rebuttal: BERT had reached ~86% on the predecessor SWAG, near the 88% human level, and this looked like solved commonsense; HellaSwag shows the models were surface learners on dataset-specific bias, not robust reasoners.
Locators:    Abstract; Section 1 (Introduction), incl. the SWAG backstory and the NYT headline footnote; Section 2 (Background, AF definition); results discussion ("47.3% overall", "45% Bert-Large performance, versus 96.5% for humans" on WikiHow).
Quote:       "the resulting dataset of 70k problems is easy for humans (95.6% accuracy), yet challenging for machines"; "despite BERT-Large having been used as the adversarial filter, it still performs the strongest at 47.3% overall"; acronym: "Harder Endings, Longer contexts, and Low-shot Activities for Situations With Adversarial Generations."
```

```text
URL:         https://arxiv.org/abs/1808.05326
Kind:        primary. It is the SWAG paper (Zellers, Bisk, Schwartz, Choi, EMNLP 2018) that defines Adversarial Filtering; it owns the AF procedure and the SWAG numbers.
Establishes: The definition and mechanism of Adversarial Filtering; SWAG's size (113k) and split (73k train / 20k validation / 20k test); its sources (consecutive video captions from ActivityNet Captions and LSMDC); its human accuracy (88%, an ensemble of five crowd workers); the over-generate-then-filter ratio.
Paraphrase:  AF constructs a de-biased dataset by iteratively training an ensemble of stylistic classifiers and using them to filter machine-generated candidate endings, so the surviving wrong endings are the ones classifiers cannot separate from the true ending. SWAG over-generated 1,023 negatives per example and filtered to 9, five of which went to crowd workers. The generator for SWAG was an LSTM language model pretrained on BookCorpus and finetuned on the caption datasets. This is the procedure HellaSwag inherits and strengthens by swapping the LSTM generator for OpenAI GPT.
Locators:    Abstract; Section defining AF ("a novel procedure that constructs a de-biased dataset by iteratively training an ensemble of stylistic classifiers"); dataset section ("113k... 73k training, 20k validation, 20k test... ActivityNet Captions... and LSMDC"); "1023 negatives per example, which the adversarial filtering process filtered down to 9."
Quote:       "we propose Adversarial Filtering (AF), a novel procedure that constructs a de-biased dataset by iteratively training an ensemble of stylistic classifiers, and using them to filter the data."
```

```text
URL:         https://huggingface.co/datasets/Rowan/hellaswag
Kind:        primary. It is the released HellaSwag dataset artifact (data hosted via the HuggingFace datasets-server for Rowan/hellaswag). It owns the actual items and the actual split counts.
Establishes: The real, checkable split counts (train 39,905; validation 10,042; test 10,003; total 59,950), which differ from the paper's "70k." One full worked item, verbatim, from the first validation row.
Paraphrase:  Each item is a context field plus four candidate endings and a gold label index. The first validation row (activity label "Roof shingle removal", source ActivityNet) is a clean, well-formed example: the correct ending is simply the real next caption.
Locators:    datasets-server size endpoint for Rowan/hellaswag (num_rows per split); validation split, offset 0, length 1.
Quote:       Context: "A man is sitting on a roof. he" — endings: (0) "is using wrap to wrap a pair of skis." (1) "is ripping level tiles off." (2) "is holding a rubik's cube." (3) "starts pulling up roofing on a roof." Gold label: 3.
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. It is the GPT-4 Technical Report (OpenAI). It owns GPT-4's HellaSwag score and the label the report attaches to the benchmark. This is the commissioned "model report that cites a HellaSwag figure as commonsense ability."
Establishes: GPT-4 scores 95.3% on HellaSwag at ten-shot; GPT-3.5 scores 85.5%; the report labels HellaSwag "Commonsense reasoning around everyday events." This is the current strong-model figure, and it is the case of a high HellaSwag number still presented as commonsense ability after the test was effectively solved.
Paraphrase:  In the report's academic-benchmark table, HellaSwag appears alongside a one-line description calling it commonsense reasoning about everyday events, with GPT-4 at 95.3% (10-shot) and GPT-3.5 at 85.5%.
Locators:    Table of academic benchmarks (the row for HellaSwag, with its description column and the GPT-4 / GPT-3.5 columns).
Quote:       Description column: "Commonsense reasoning around everyday events." GPT-4: 95.3% (10-shot).
```

```text
URL:         https://arxiv.org/abs/2504.07825
Kind:        primary. It is the validity paper "What the HellaSwag? On the Validity of Common-Sense Reasoning Benchmarks" (Chizhov, Nee, Langlais, Yamshchikov, 2025). It owns its own error analysis of the HellaSwag validation set.
Establishes: Item errors quantified. Almost 40% of validation questions have ungrammatical prompts; 95.7% of the ActivityNet subset is ungrammatical. The labeled answer is the correct one in 96.3% of cases (so ~3.7% are mislabeled), but in 21.1% of questions at least one other option is as good as the labeled answer. When the context is removed or replaced with "Lorem ipsum," more than 65% of model predictions do not change, evidence that models often decide on the endings alone. The authors release GoldenSwag, a filtered subset of 1,525 questions.
Paraphrase:  The paper argues HellaSwag has severe construct-validity problems and "should not be used for evaluation in its current state." The ActivityNet-sourced items are the worst: nearly all are ungrammatical. The Lorem-ipsum result shows a right answer can be picked without reading the situation, which undercuts the claim that a high score demonstrates commonsense over the described scenario.
Locators:    Abstract (the >65% Lorem-ipsum figure); grammar/sensicality analysis ("almost 40%... ungrammatical prompts", "95.7% of the ActivityNet part"); answer-validity analysis ("correct in 96.3%", "21.1%"); Section 5 (GoldenSwag, 1,525 questions filtered from the 10,042-item validation set).
Quote:       "almost 40% of the questions have ungrammatical prompts. Such questions comprise the absolute majority (95.7%) of the ActivityNet part"; "more than 65% of model predictions remain the same."
```

```text
URL:         https://surgehq.ai/blog/hellaswag-or-hellabad-36-of-this-popular-llm-benchmark-contains-errors
Kind:        primary. It is Surge AI's own hand audit of HellaSwag rows (author Edwin Chen, Surge AI). It owns the 36% finding and the quoted flawed item. (Secondary in the weak sense that Surge did not build HellaSwag; primary for the audit it conducted.)
Establishes: In a hand review of 300 random validation rows, 107 (36%) contained an error: ungrammatical text, typos in the "correct" answer, mislabeled answers, or a "wrong" ending as good as or better than the labeled one. A verbatim flawed item shows a labeled-correct ending that is itself ungrammatical and contains a typo.
Paraphrase:  The audit is independent of the academic validity paper and reaches a compatible conclusion on a different sample: a large minority of items are broken, and the flaw sits in the labeled-correct ending, not only the distractors.
Locators:    Body (the 107-of-300 figure and the error taxonomy); the worked "lacrosse" example.
Quote:       Prompt: "Men are standing in a large green field playing lacrosse. People is around the field watching the game. men" — endings include (labeled correct) "are running side to side of the ield playing lacrosse trying to score." ("ield" is the source's own typo.)
```

```text
URL:         https://rowanzellers.com/hellaswag/
Kind:        primary. It is the dataset's own project and leaderboard page, maintained by the HellaSwag author. It owns the leaderboard the authors host.
Establishes: A resolving leaderboard page that carries both ends of the story: pre-release models "under 48% accuracy" and a current strong entry, "GPT-4 base 10-shot, 95.3, March 2023," against the stated ~95.6% human baseline.
Paraphrase:  The authors' page frames HellaSwag as commonsense sentence completion, states the human baseline over 95%, and lists top model entries at ~95%, so the page itself records the closed gap.
Locators:    Page header and description; leaderboard listing (top entry GPT-4, 95.3).
Quote:       Human baseline described as "over 95% accuracy"; top entry "GPT4 base 10-shot" at "95.3."
```

```text
URL:         https://huggingface.co/spaces/open-llm-leaderboard/blog
Kind:        secondary for the saturation interpretation (HuggingFace reports on the performance of models it did not build). Primary for one fact: HuggingFace's own decision to retire the six v1 benchmarks, HellaSwag among them.
Establishes: HellaSwag named by name as saturated. HuggingFace states models "are now reaching baseline human performance on HellaSwag, MMLU, and ARC, a phenomenon called saturation," lists saturation, contamination, and benchmark errors as the reasons, and replaces the six v1 benchmarks with a harder v2 set.
Paraphrase:  The operator of the most-cited open leaderboard removed HellaSwag in 2024 because scores had converged near the human ceiling and no longer separated models, and because some benchmarks were contaminated or contained errors. Note the verb the source uses is "reaching," not "surpassing," which matches the checked figures.
Locators:    "Harder, better, faster, stronger: Introducing the LLM Leaderboard v2" section: "Over the past year, the benchmarks we were using got overused/saturated"; "They became too easy for models"; "models are now reaching baseline human performance on HellaSwag, MMLU, and ARC, a phenomenon called saturation"; "Some benchmarks contained errors."
Quote:       "models are now reaching baseline human performance on HellaSwag, MMLU, and ARC, a phenomenon called saturation."
```

```text
URL:         https://deepgram.com/learn/hellaswag-llm-benchmark-guide
Kind:        secondary. An explainer (Brad Nikkel, Deepgram) reporting on HellaSwag from outside; it neither built the benchmark nor the models.
Establishes: Independent confirmation that HellaSwag is presented publicly as a commonsense benchmark and that GPT-4's 95.3% is read as parity with the human baseline. Useful only as corroboration of framing, not for any load-bearing number.
Paraphrase:  Describes HellaSwag as evaluating common-sense reasoning and states closed-source models now perform "on par with humans," citing GPT-4 at 95.3% (10-shot).
Locators:    Body.
Quote:       "Closed-source LLMs, however, are now performing on par with humans, with GPT-4 scoring 95.3% with 10-shot reasoning."
```

## Contradictions

- **"Past the human number" is weaker than the commission's framing.** The commission's angle says scores "climbed past the measured human number." The strongest verified current figure, GPT-4 at 95.3% (GPT-4 report; rowanzellers leaderboard), is 0.3 points below the 95.6% human baseline (HellaSwag paper). HuggingFace's own wording is "reaching baseline human performance," not surpassing. The defensible claim is that top models are indistinguishable from people and clustered within about a point, so the test no longer ranks them, not that a checked model clearly beat humans. Any sentence in the article that says models "passed" or "beat" the human score on HellaSwag needs a specific model and figure the writer can cite above 95.6%, which this record does not supply. The saturation argument does not need that stronger claim; the tight cluster near the ceiling is enough.
- **Item count: 70k vs 59,950.** The HellaSwag paper abstract states "70k problems." The released dataset (HuggingFace Rowan/hellaswag) has 59,950 rows: train 39,905, validation 10,042, test 10,003. Use the released, checkable figure for anything the reader could verify, and describe the paper's "70k" as the paper's own rounded statement if it is quoted. The gap is unexplained by the sources read.
- **The 2018 human baseline (88%) is a different number from HellaSwag's (95.6%).** SWAG measured 88% human accuracy; HellaSwag measured 95.6%. They are different tasks (different sources, longer contexts) and must not be conflated. The 88% belongs to SWAG only.
- **Surge AI (36% of a 300-row sample) and the validity paper (~40% ungrammatical prompts across the validation set) are two independent audits.** They agree in direction and rough magnitude but measure different things (any error in a hand-checked sample vs ungrammaticality across the full set), so they corroborate rather than duplicate. Report them as two findings, not one figure repeated.
- No source contradicts the core construction account (sources, GPT generator, BERT filter, AF procedure). Contradictions above are about magnitude and framing, not mechanism.

## Numbers

```text
Figure: 95.6% human accuracy (overall)
Owner:  HellaSwag paper (arXiv 1905.07830)
Scope:  Crowd-worker accuracy on HellaSwag items; WikiHow subset 96.5% human, ActivityNet raised to ~94% after human filtering.
```

```text
Figure: 47.3% BERT-Large accuracy (overall, best 2019 model)
Owner:  HellaSwag paper (arXiv 1905.07830)
Scope:  Overall test accuracy at launch; the same BERT-Large was the adversarial filter. Near-launch machine ceiling. WikiHow subset ~45%.
```

```text
Figure: 95.3% GPT-4 accuracy, 10-shot (current strong model)
Owner:  GPT-4 Technical Report (arXiv 2303.08774); also listed on the HellaSwag leaderboard (rowanzellers.com/hellaswag). GPT-3.5: 85.5%.
Scope:  Ten-shot evaluation, 2023. Sits 0.3 points below the 95.6% human baseline (see Contradictions).
```

```text
Figure: 113k SWAG questions; 88% SWAG human accuracy
Owner:  SWAG paper (arXiv 1808.05326)
Scope:  Predecessor dataset. 73k train / 20k validation / 20k test. Human = ensemble of five crowd workers.
```

```text
Figure: 59,950 released HellaSwag items (paper says "70k")
Owner:  Released dataset (HuggingFace Rowan/hellaswag) for 59,950; HellaSwag paper for "70k"
Scope:  train 39,905 / validation 10,042 / test 10,003. Test labels are withheld in the public release.
```

```text
Figure: ~40% ungrammatical prompts; 95.7% of ActivityNet subset ungrammatical; 21.1% with multiple valid answers; labeled answer correct in 96.3%
Owner:  Validity paper (arXiv 2504.07825)
Scope:  HellaSwag validation set (10,042 items). GoldenSwag cleaned subset = 1,525 items.
```

```text
Figure: >65% of predictions unchanged with context replaced by "Lorem ipsum"
Owner:  Validity paper (arXiv 2504.07825)
Scope:  Model predictions on HellaSwag validation items when the situation text is removed/replaced; endings alone often determine the answer.
```

```text
Figure: 36% of rows contain errors (107 of 300)
Owner:  Surge AI audit (surgehq.ai)
Scope:  Hand review of 300 random HellaSwag validation rows.
```

```text
Figure: 1,023 negatives per example over-generated, filtered to 9 (SWAG)
Owner:  SWAG paper (arXiv 1808.05326)
Scope:  Illustrates the over-generate-then-filter ratio of Adversarial Filtering.
```

## Source assets

```text
Asset: HellaSwag paper, Figure 1 (assets/teaser.png in the arXiv HTML) — the worked WikiHow/ActivityNet item with four endings and BERT's wrong pick.
Shows: What one scored item actually looks like, and that a 2019 model chose an ending humans find implausible. Carries the "what is being scored" idea better than prose.
Crop:  Must retain the context line, all four endings, and the marking of the gold answer versus the model's pick. The teaser is a figure image; if reused, reproduce the text faithfully rather than cropping to a fragment that drops an ending.
```

```text
Asset: The "man on a roof" item, reproduced as text from the released dataset (validation row 0).
Shows: A clean, well-formed item where the gold ending is just the true next caption. Grounds section 2's point that a right answer is picking the real continuation, not demonstrated reasoning.
Crop:  Keep all four endings and the gold index. Do not paraphrase the endings; the typo-free wording is the contrast with the flawed item below.
```

```text
Asset: The Surge AI "lacrosse" item (quoted verbatim in the Surge AI post).
Shows: A labeled-correct ending that is ungrammatical and contains a typo ("ield"). Grounds section 3's point that the errors sit in the gold answers, not only distractors.
Crop:  Keep the labeled-correct ending intact, typo included; that is the evidence.
```

```text
Asset: A model-score-over-time comparison (human 95.6, BERT-Large 47.3 in 2019, GPT-4 95.3 in 2023).
Shows: The gap opening at launch and closing to the human line. This is the saturation picture.
Crop:  None — this is not a source image. Per spec/charts.md the writer builds it as chart-N.py from the figures above, with the human baseline drawn as a reference line and axes labeled.
```

## Discarded

```text
URL: https://arxiv.org/pdf/1905.07830 — PDF binary would not extract through the fetch tooling; the same content was read from the arXiv HTML instead. Transport failure, not a source.
URL: https://paperswithcode.com/sota/sentence-completion-on-hellaswag — 302-redirects to a HuggingFace trending page and does not resolve to a HellaSwag leaderboard. Replaced by rowanzellers.com/hellaswag as the leaderboard source.
URL: https://llm-stats.com/benchmarks/hellaswag — gated behind a verification page; leaderboard content not readable, so no figure from it is cited.
URL: https://www.themoonlight.io/en/review/what-the-hellaswag-... — machine-generated summary of the validity paper; superseded by reading arXiv 2504.07825 directly.
```

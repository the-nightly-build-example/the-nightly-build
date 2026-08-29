# Evidence record: the-mechanics/negation (01)

The evidence strongly supports the two measured findings the lesson wants to
connect. For text, three benchmark papers show that pretrained and early
autoregressive models treat a negated sentence almost exactly like its
affirmative twin: Ettinger's cleanest case has BERT preferring the true
completion in 100% of affirmative sentences and 0% of negated ones. For the
image side, the bag-of-words result is measured, not asserted: a contrastive
vision-language text encoder (CLIP) scores near chance on word order and
relations, and a separate 2025 benchmark shows CLIP-style models sit at chance
on negation queries. The engineering patch is documented at the source: the
classifier-free guidance paper gives the exact formula and the "negative score
term" idea that negative prompts later exploit.

Two things are thin, and both matter. First, the training-data-imbalance step
(affirmatives vastly outnumber negations) is a hypothesis offered by these
authors to explain their results, not a measured corpus frequency; no source I
read counts it, so it must be presented as their explanation, not a statistic.
Second, and more important, every verified image-side number is from
*discriminative* models (CLIP retrieval and multiple-choice), not from a
text-to-image *diffusion* model generating "a room with no elephant." The link
from the CLIP bag-of-words finding to the generated-image failure is an
inference (diffusion models reuse CLIP-style text encoders), not something the
sources measure directly. The lesson's image example is sound as mechanism but
should not claim a measured generation-failure rate it does not have.

The angle also has a real counter-current, recorded in full under
Contradictions: frontier instruction-tuned text models now handle much simple
negation, so the text half of the parallel is weakening over time and the
sharpest failures are concentrating in image models and harder reasoning cases.
This narrows the lesson rather than sinking it.

## Sources

```text
URL:         https://aclanthology.org/2020.acl-main.698/
Kind:        primary — Kassner & Schütze own the negated-LAMA experiment and its measurements.
Establishes: Pretrained masked LMs give near-identical predictions for a fact and its negation; BERT is best of the tested models but still fails badly; the failure is learnable with supervision.
Paraphrase:  The authors built "negated LAMA" by inserting a negation element into each LAMA cloze template (e.g. "The theory of relativity was not developed by [MASK]."), giving positive/negative pairs. Querying Transformer-XL, ELMo, and BERT, they measured Spearman rank correlation and percent overlap of the top-1 prediction between each fact and its negation; high values mean the model ignored the negation. In most cases the correlation exceeds 85%. They also pretrained BERT-base from scratch on a synthetic corpus with equal positive and negative sentences: pretrained BERT still failed to generalize (test accuracy 0.2 for both positive and negative), but after supervised fine-tuning on a true/false task, test accuracy was 100%. Their suggested (not measured) explanation is that negated sentences are far rarer in training corpora, so the model predicts fillers from the most similar—usually affirmative—sentences.
Locators:    Abstract; Sec 3 "Negated LAMA" and Table 2 (correlation/overlap); Table 5 (balanced corpus: pretrained 0.2/0.2, finetuned 1.0/1.0); Sec 4 Discussion (frequency hypothesis). Total dataset stated as 42,867 negated sentences (Related Work). arXiv mirror: https://arxiv.org/abs/1911.03343
Quote:       "Models are equally prone to generate facts ('Birds can fly') and their incorrect negation ('Birds cannot fly')." And: "So BERT easily learns negation if supervision is available, but fails without it."
```

```text
URL:         https://arxiv.org/abs/1907.13528
Kind:        primary — Ettinger owns the NEG-136 psycholinguistic negation diagnostic on BERT. (Published as TACL 2020: https://aclanthology.org/2020.tacl-1.3/)
Establishes: The single sharpest text figure: BERT prefers the true completion in 100% of affirmative category sentences and 0% of the same sentences once "not" is added. Also: this collapses toward true-preference when the negated sentence is phrased "naturally," which is the clue pointing to training frequency.
Paraphrase:  The NEG-136-SIMP set uses simple category sentences ("A robin is a ___" vs "A robin is not a ___") with a true (category-match) and a false completion. Ettinger measured how often the model assigns higher probability to the true completion. For affirmatives, both BERT-base and BERT-large prefer the true completion in 100% of items; for the negated versions, both prefer it in 0% of items, assigning higher probability to the false, category-matching word every time. On a supplementary "natural" set (NEG-136-NAT, e.g. "Most smokers find that quitting isn't very ___"), BERT-large instead prefers true completions in 100% of the natural negative items but only 0% of the less-natural negative items. Ettinger attributes the naturalness effect to "a higher frequency of these types of statements in the training data," and frames the general lesson that LMs "leverage the most reliable cues in order to optimize their predictive capacity" for a phenomenon "not conducive to clear predictions."
Locators:    Sec 5.3 (design); Sec 9.2 Table 12 (100% affirmative / 0% negative, both model sizes); Sec 9.4 Table 14 (NEG-136-NAT: Neg-NT 87.5% base / 100% large; Neg-LN 0.0% both); Sec 10 Discussion (training-frequency explanation). Model sizes: BERT-base 110M, BERT-large 340M.
Quote:       "in the negative statements (A robin is not a ___), BERT prefers the true completion in 0% of items, assigning the higher probability to the false completion in every case." And (on why natural sentences do better): "in all likelihood it is not naturalness per se that drives the model's relative success on them—but rather a higher frequency of these types of statements in the training data."
```

```text
URL:         https://aclanthology.org/2023.starsem-1.10/
Kind:        primary — Truong, Baldwin, Verspoor & Cohn own the LLM negation-benchmark sweep. (arXiv: https://arxiv.org/abs/2306.08189)
Establishes: The scale/instruction-tuning story. On sensitivity/cloze tasks, larger models get WORSE (inverse scaling). On reasoning-under-negation (NLI), instruction tuning—not scale—is what helps, and it helps a lot. This is the source for "what reduces the failure, and by how much."
Paraphrase:  They evaluated GPT-neo/OPT (125M–6.7B), GPT-3 175B (text-davinci-001), InstructGPT 175B (text-davinci-003), and FLAN-T5-XXL 11B, across sensitivity (MKR-NQ), lexical-semantics (MWR, SAR), and reasoning (SNLI/MNLI/RTE-neg, NaN-NLI, MoNLI). On MKR-NQ, hit-rate (an error metric, lower better) worsens as models grow — the smallest GPT-neo-125M is best — an inverse-scaling trend; base GPT-3 and InstructGPT are worse (higher error) than tiny models on this task. On antonym/synonym classification (SAR) all models sit near the 0.5 chance line. On NLI, most models score below the random baseline; only the instruction-tuned models rise above chance. InstructGPT lifts RTE-neg accuracy from GPT-3's 0.525 to 0.767, and FLAN-T5-XXL (16x smaller than GPT-3) beats GPT-3 on most NLI tasks. Their stated conclusion: instruction fine-tuning has a much greater impact than scaling for reasoning under negation. One clean exception: InstructGPT does NOT improve on MoNLI (downward-monotonicity), scoring 0.470 vs GPT-3's 0.540, which they attribute to over-generalizing hypernym reasoning across negation.
Locators:    Sec 3 Finding 1 (inverse scaling, MKR-NQ Fig 1); Finding 4 and Table 5 (exact per-model numbers); the sentence "instruction fine-tuning has much greater impact than model scaling." Random baselines: RTE-neg and MoNLI are 2-way (chance 0.5); SNLI/MNLI/NaN-NLI are 3-way (chance ~0.33).
Quote:       "we show that LLMs have several limitations including insensitivity to the presence of negation, an inability to capture the lexical semantics of negation, and a failure to reason under negation." And: "larger LMs are more insensitive to negation compared to smaller ones."
```

```text
URL:         https://arxiv.org/abs/2210.01936
Kind:        primary — Yuksekgonul et al. own the ARO benchmark and the bag-of-words diagnosis of vision-language models. (ICLR 2023 oral.)
Establishes: The image-side mechanism the lesson needs: a contrastive image-text model's text encoder is measurably insensitive to word order and composition, so it behaves like a bag of words. This is the finding that explains why "no elephant" activates "elephant."
Paraphrase:  ARO (Attribution, Relation, Order) tests whether a VLM prefers the correct caption over a minimally perturbed one. For CLIP, accuracy is near or below the 50% two-choice chance level on relations and attributes (VG-Relation ~59%, VG-Attribution ~62%), and the order tasks — pick the true caption among the original plus four word-shuffled variants — score around COCO-Order 46% and Flickr30k-Order 59%. The decisive shortcut result: shuffling all words in CLIP's COCO retrieval captions drops Recall@1 only from 50.3% to 34.1%, i.e. word order is barely needed to retrieve the right image. The authors' explanation is that a contrastive retrieval objective on datasets with rich, distinctive visual content can be minimized without using order or composition, so nothing pushes the model to encode them. (These figures were read from the ar5iv full-text rendering, cross-checked across two fetches; treat the exact decimals as read-from-render, but the near-chance pattern is unambiguous.)
Locators:    Abstract (bag-of-words claim, >50,000 test cases); results tables for VG-Relation/VG-Attribution and COCO/Flickr30k-Order; the caption word-shuffling retrieval experiment (50.3 to 34.1 Recall@1). Models also tested: BLIP, FLAVA, XVLM.
Quote:       "it is possible to perform well on these datasets without using compositional structure... models can achieve high performance in retrieval objectives, thus also obtaining low contrastive loss, without order information, unless the datasets are carefully designed."
```

```text
URL:         https://arxiv.org/abs/2501.09425
Kind:        primary — Alhamoud, Alshammari, Tian, Li, Torr, Kim & Ghassemi own NegBench and the direct measurement of VLM negation failure. (CVPR 2025.)
Establishes: The one source that measures negation failure directly in vision-language models (rather than order/composition as a proxy): CLIP-style models sit at chance on negated queries. Directly on-topic for the image case, and the strongest single statement that the image weakness is about negation specifically.
Paraphrase:  NegBench is a 79k-example benchmark (image, video, and medical data; 18 task variations) covering retrieval with negated queries and multiple-choice questions with negated captions. The headline result is that modern VLMs "struggle significantly with negation, often performing at chance level." Their data-centric fix — fine-tuning CLIP on millions of synthetic negated captions — yields a 10% increase in recall on negated queries and a 28% boost in multiple-choice accuracy, which supports the same conclusion the text papers reach: the failure tracks the near-absence of explicit negation in image-caption pretraining data, and is reducible with targeted supervision. Caveat for the writer: this is still a discriminative (retrieval/MCQ) measurement, not text-to-image generation.
Locators:    Abstract (chance-level claim, 79k examples, 18 task variations, +10% recall, +28% MCQ). Read at abstract/author level; per-model tables not opened.
Quote:       "our findings reveal that modern VLMs struggle significantly with negation, often performing at chance level."
```

```text
URL:         https://arxiv.org/abs/2207.12598
Kind:        primary — Ho & Salimans own classifier-free guidance. Documents the engineering patch's actual mechanism.
Establishes: What CFG is and its exact formula, and the "negative score term" idea that user-facing negative prompts later generalize. Also a needed honesty check: this paper is class-conditional ImageNet and never mentions user-supplied "negative prompts."
Paraphrase:  A single network is trained to be both conditional and unconditional by randomly replacing the conditioning c with a null token during training, with probability p_uncond (they used 0.1, 0.2, 0.5; 0.1–0.2 worked best). At sampling time the guided prediction is a linear extrapolation away from the unconditional prediction toward the conditional one: eps-tilde = (1+w)·eps(z,c) − w·eps(z), Eq. (6). In discussion they give the intuition that guidance "decreases the unconditional likelihood of the sample while increasing the conditional likelihood... with a negative score term." User-facing negative prompts (below) replace that unconditional eps(z) with a prediction conditioned on the unwanted text, so the model is pushed away from it; that extension is NOT in this paper.
Locators:    Sec 3.2 and Eq. (6); Algorithm 1 (p_uncond dropout of conditioning) and Algorithm 2 (sampling); Sec 5 Discussion ("negative score term"). Scope: 64x64 and 128x128 class-conditional ImageNet.
Quote:       "we then perform sampling using the following linear combination of the conditional and unconditional score estimates: eps-tilde_theta(z,c) = (1+w) eps_theta(z,c) − w eps_theta(z)." And: "Classifier-free guidance accomplishes this by decreasing the unconditional likelihood with a negative score term."
```

```text
URL:         https://huggingface.co/docs/diffusers/en/using-diffusers/weighted_prompts
Kind:        secondary — library documentation. Confirms the negative-prompt feature exists and how it is used, but not the underlying math.
Establishes: That "negative prompt" is a real, standard control surface in diffusion image tools (a first-class parameter), and that prompt weighting (e.g. "(cat:0.5)" to down-weight) is a related lever. Useful only to ground the everyday feature, not the mechanism.
Paraphrase:  The Diffusers "Prompting" page documents passing text to negative_prompt / negative_prompt_embeds (and negative_pooled_prompt_embeds) alongside the positive prompt, and documents prompt weighting via multipliers/parentheses that scale attention. It does not state that the negative prompt replaces the unconditional term in classifier-free guidance.
Locators:    "Prompt weighting" section and the negative_prompt_embeds tip. (Page served under the weighted_prompts path; titled "Prompting.")
Quote:       (none load-bearing; documentation of feature existence)
```

```text
URL:         https://theaisummer.com/classifier-free-guidance-part-2/
Kind:        secondary — a technical explainer (AI Summer). Supplies the generalized-CFG framing that connects negative prompts to Ho & Salimans.
Establishes: The bridge the CFG paper omits: negative prompting is CFG with the unconditional/"null" prediction swapped for a prediction conditioned on the unwanted content, so the sampler steps away from it.
Paraphrase:  The article presents the generalized guidance form D_out = D_neg + (1+gamma)(D_pos − D_neg), and frames CFG as "impaired guidance with a bad version of itself" — replacing the unconditional model with various alternatives. Read against Ho & Salimans Eq. (6), setting D_neg to a prediction conditioned on the negative prompt gives exactly the user-facing negative-prompt behavior: eps_pos + w·(eps_pos − eps_neg). Use this only as a secondary explainer; the equation of record is Ho & Salimans Eq. (6).
Locators:    Section presenting the generalized D_out formula and the "bad version of itself" framing.
Quote:       "D_out(x|sigma) = D_neg(x|sigma) + (1+gamma)(D_pos(x|sigma) − D_neg(x|sigma))"
```

## Contradictions

This is the section the editor should read first; the angle has a genuine
counter-current, and two of the primary sources supply it themselves.

- **Frontier instruction-tuned text models now handle much simple negation —
  the text half of the parallel is weakening.** Truong et al.'s own Limitations
  section reports that in a small experiment "ChatGPT displayed strong
  performance on challenging samples in the investigated benchmark, so the main
  findings of the paper may not hold true for newer LLMs." Within the paper,
  FLAN-T5-XXL (11B, instruction-tuned) already beats base GPT-3 (175B) on most
  NLI-under-negation tasks, and InstructGPT lifts RTE-neg from 0.525 to 0.767.
  Ettinger's NEG-136-NAT is the earliest version of the same crack: BERT-large
  prefers the true completion in 100% of *naturally phrased* negated sentences,
  failing (0%) only on stilted ones. Implication for the lesson: the crisp
  "models can't do 'not'" story is most true for masked/early autoregressive
  models and for image models; for frontier instruction-tuned text models the
  failure has receded to harder reasoning and edge cases. The lesson should say
  this, and it sharpens rather than sinks the mechanism (data + objective, not
  an immovable architectural wall).

- **Negation is learnable, so "the model just can't" is the wrong frame.**
  Kassner & Schütze show pretrained BERT fails their balanced corpus (0.2 test
  accuracy) but reaches 100% after supervised fine-tuning. The weakness is in
  the unsupervised prediction objective and the data it sees, not an inability
  in principle. This is a contradiction with any strong "architecture can't
  represent negation" claim and should temper the settled/open framing.

- **One study argues the failure is overstated.** Gubelmann & Handschuh (2022),
  as cited within Truong's Related Work, "found that the ability to understand
  negation of LMs is underestimated in previous studies," arguing the struggle
  comes more from task contextualization than from negation itself. I did not
  open this paper; this is a claim reported by Truong, so it supports only that
  the disagreement exists, not that it is correct. Flagged for the editor as a
  steelman to weigh, not to assert.

- **The two failures are the "same weakness" only by inference on the image
  side.** The verified image numbers (ARO, NegBench) are all from discriminative
  CLIP-style models on retrieval/multiple-choice. No source I read measures a
  diffusion text-to-image model generating a negated prompt and quantifies the
  rate at which "no elephant" yields an elephant. The claim that these are one
  weakness surfacing twice rests on the fact that diffusion T2I models reuse
  CLIP-style text encoders — a sound inference, but the lesson must not present
  it as a measured generation-failure statistic.

## Numbers

```text
Figure: 100% (affirmative) vs 0% (negated) — share of items where BERT prefers the true completion
Owner:  Ettinger 2020, NEG-136-SIMP, Table 12 (both BERT-base and BERT-large)
Scope:  72 simple category sentences ("A robin is (not) a ___"); true = category match, false = non-match
```

```text
Figure: Spearman rank correlation > 85% in most cases between a fact and its negation
Owner:  Kassner & Schütze 2020, Table 2
Scope:  ~42,867 negated LAMA cloze pairs across Google-RE, T-REx, ConceptNet, SQuAD; models Transformer-XL, ELMo, BERT-base, BERT-large
```

```text
Figure: BERT-large top-1 overlap between fact and negation — e.g. ConceptNet 31.3%, T-REx N-1 45.0% (higher = more negation-blind); BERT is best of the five models tested
Owner:  Kassner & Schütze 2020, Table 2
Scope:  Percent overlap of rank-1 prediction, per LAMA source
```

```text
Figure: Pretrained BERT 0.2 / 0.2 test accuracy (pos/neg); finetuned BERT 1.0 / 1.0
Owner:  Kassner & Schütze 2020, Table 5 (balanced synthetic corpus)
Scope:  Demonstrates negation is learnable with supervision, not in unsupervised pretraining
```

```text
Figure: RTE-neg accuracy: GPT-J-6B 0.211, GPT-3 175B 0.525, InstructGPT 175B 0.767 (chance 0.5, 2-way)
Owner:  Truong et al. 2023, Table 5
Scope:  Reasoning under negation; instruction tuning is the lever that clears chance
```

```text
Figure: MoNLI accuracy: GPT-3 0.540, InstructGPT 0.470 (chance 0.5, 2-way) — instruction tuning does NOT help here
Owner:  Truong et al. 2023, Table 5
Scope:  Downward-monotonicity negation; the clean exception to "instruction tuning fixes it"
```

```text
Figure: MKR-NQ inverse scaling — smallest GPT-neo-125M best; hit-rate error rises with size; GPT-3/InstructGPT worse than tiny models
Owner:  Truong et al. 2023, Finding 1 / Fig 1 / Table 5 (WHR5: GPT-J 0.083, GPT-3 0.172, InstructGPT 0.195; lower is better)
Scope:  Sensitivity-to-negation cloze task; WHR is an error metric
```

```text
Figure: CLIP on ARO — VG-Relation ~59%, VG-Attribution ~62% (2-choice chance 50%); COCO-Order ~46%, Flickr30k-Order ~59%
Owner:  Yuksekgonul et al. 2023 (ARO)
Scope:  Near/below chance on relations and order; read from ar5iv render, near-chance pattern robust
```

```text
Figure: Shuffling all caption words drops CLIP COCO Recall@1 only 50.3% -> 34.1%
Owner:  Yuksekgonul et al. 2023 (ARO)
Scope:  Retrieval barely uses word order — the core bag-of-words evidence
```

```text
Figure: VLMs at chance on negation; fine-tuning on synthetic negated captions gives +10% recall, +28% MCQ accuracy
Owner:  Alhamoud et al. 2025 (NegBench), abstract; 79k examples, 18 task variations
Scope:  Discriminative retrieval/MCQ on CLIP-style models, not generation
```

```text
Figure: CFG guided prediction eps-tilde = (1+w)·eps(z,c) − w·eps(z); training drops conditioning with prob p_uncond (0.1-0.2 best)
Owner:  Ho & Salimans 2022, Eq. (6), Algorithms 1-2
Scope:  Class-conditional ImageNet 64x64/128x128; the mechanism, not a benchmark score
```

```text
Figure: Training-data imbalance (affirmatives vastly outnumber negations) — ESTIMATE / HYPOTHESIS, no measured frequency
Owner:  Stated by Truong et al. 2023 citing Ettinger 2020; offered as explanation by Kassner & Schütze 2020 and Ettinger 2020
Scope:  Present as the authors' explanation for the results, never as a sourced corpus statistic
```

## Source assets

```text
Asset: Ettinger 2020, Table 13 — BERT-large top-5 predictions for "A robin is a ___" vs "A robin is not a ___" (and hammer, daisy)
Shows: The failure in one glance: the predicted words barely change when "not" is added ("A robin is not a ___" -> robin, bird, penguin, ...). A reader sees the mechanism without any statistics.
Crop:  Keep at least the robin affirmative/negative pair side by side; the exact model-generated word lists are the point, so do not paraphrase them into prose.
```

```text
Asset: Kassner & Schütze 2020, Table 4 — original/negated/misprimed completions with log-probs (e.g. "Birds can [MASK]" -> fly; "Birds cannot [MASK]" -> fly)
Shows: The same fact-equals-negation collapse, with probabilities, across ConceptNet/T-REx/SQuAD examples.
Crop:  The "Birds can / Birds cannot" ConceptNet rows carry it alone; the full table is larger than the lesson needs.
```

```text
Asset: Ho & Salimans 2022, Figure 1 — a malamute class, non-guided (left) to strongly guided (right)
Shows: What guidance does visually — sharper, more on-concept samples as w rises. Useful if the lesson illustrates the positive-guidance side before explaining negative prompts.
Crop:  Retain the left-to-right progression and the caption stating increasing guidance; a single row suffices.
```

```text
Asset: Yuksekgonul et al. 2023 (ARO) — the word-shuffling retrieval figure/table (Recall@1 50.3 -> 34.1)
Shows: Order barely matters for retrieval; the numeric drop is small, which is the whole bag-of-words argument.
Crop:  If used, keep the no-shuffle vs shuffle-all comparison; omit the intermediate perturbation variants unless the lesson discusses them.
```

## Discarded

```text
URL: https://arxiv.org/abs/2503.22395 ("Negation: A Pink Elephant in the LLMs' Room?") — not opened/verified; newer, not needed to meet the claims, and would be padding.
URL: https://arxiv.org/abs/2502.07717 ("Making Language Models Robust Against Negation") — mitigation method, off the lesson's mechanism focus; not read.
URL: https://arxiv.org/abs/2508.10931 (VSF negative-guidance) and https://arxiv.org/abs/2505.21179 (Normalized Attention Guidance) — recent negative-guidance methods; the negative-prompt mechanism is already covered by Ho & Salimans + the AI Summer explainer, so these would add complexity without changing the interpretation.
URL: WebFetch summary claiming Ettinger reports "~50% accuracy on negation" and a quote "affirmative sentences are far more frequent in natural language" — REJECTED as a fetch-model fabrication. The verified primary shows 100% vs 0% (Table 12), and Ettinger's actual training-frequency wording is the NEG-136-NAT discussion quote recorded above. Anyone reusing that summary would misattribute both a figure and a quote.
URL: WebFetch/abstract-only reads of Truong, Kassner, ARO, and CFG that returned "numbers not in the abstract" — superseded by full-text reads; noted so no one cites an abstract page for a table figure.
```

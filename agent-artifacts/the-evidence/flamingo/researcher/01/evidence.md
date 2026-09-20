# Evidence: the-evidence/flamingo (01)

The commission's angle holds against the primary source on every load-bearing point: Flamingo's core mechanism (frozen vision encoder + frozen Chinchilla language model, bridged by a Perceiver Resampler and gated cross-attention layers, adapted purely by in-context examples), the "6 of 16" bounded SOTA claim, the model sizes and dataset scale, the documented failure modes, and the closed-weights fact are all directly verifiable in the paper's own text, tables, and datasheets, and independently corroborated by OpenFlamingo and a 2024/2025 survey. The evidence is thin in exactly one place the commission needs to be careful about: the Flamingo paper itself is internally inconsistent about the headline count. The abstract, the introduction's contributions list, the Figure 2 caption, and the body of Section 3.1 all say Flamingo beats fine-tuned state of the art on **6 of 16** tasks — and a direct recount of Table 1's own printed scores confirms exactly six wins (OKVQA, MSVDQA, Flickr30K, iVQA, STAR, NextQA) — but Table 1's own caption, on the same page as the Section 3.1 sentence it contradicts, says **seven**. This is not a interpretation dispute; it is a numerical inconsistency inside the primary source, and the writer should use "six," which is both the majority reading and the one that matches the table's actual numbers, while being able to name the discrepancy if precision is challenged. A second thinness: I could not verify from the paper itself, independently of the authors' own account, why weights were withheld — no source states DeepMind's reason, only the fact that they were not released, confirmed by two outside parties who tried to reproduce the model.

### Sources

```text
URL:         https://arxiv.org/abs/2204.14198
Kind:        primary — Alayrac et al. are the paper's authors and DeepMind is Flamingo's builder; the paper owns every claim about Flamingo's architecture, training data, and benchmark results.
Establishes: The full technical content of Flamingo: architecture (frozen NFNet-F6 vision encoder, frozen Chinchilla language model, Perceiver Resampler, GATED XATTN-DENSE layers), the three model sizes and their parameter breakdowns (Table 5), the three training datasets and their sizes, the 16-benchmark few-shot results (Table 1), the fine-tuning follow-up results (Table 2/Table 8), the ablation studies (Table 3/10/11), and the paper's own documented limitations (Section 5 and Appendix D.1).
Paraphrase:  Flamingo is a family of visual language models that take text interleaved with images or video and generate text, adapting to a new task from a handful of image/text examples placed in the prompt rather than by updating any weights. It reaches a new few-shot state of the art on 16 benchmarks and, on six of those, beats the prior state of the art set by methods fine-tuned on far larger annotated datasets.
Locators:    Abstract (PDF p.1); Section 1 "Contributions" (PDF p.4); Figure 2 caption (PDF p.3); Section 2 "Approach" (PDF pp.4-6); Section 3.1 "Few-shot learning on vision-language tasks" and Table 1 (PDF pp.7-8); Section 3.2 "Fine-tuning Flamingo" and Table 2 (PDF p.8); Section 5 "Discussion" (PDF p.10); Appendix A.1 (PDF pp.24-26, architecture detail); Appendix A.2/Table 5 (PDF p.28, parameter counts); Appendix D.1 "Limitations, failure cases and opportunities" (PDF p.38); Appendix F.1 datasheet for M3W (PDF p.47).
Quote:       "On 6 of these 16 tasks, Flamingo also outperforms the fine-tuned state of the art despite using only 32 task-specific examples, around 1000 times less task-specific training data than the current state of the art." (Section 1, PDF p.4). "On six tasks, Flamingo even outperforms the fine-tuned SotA despite using a single set of model weights and only 32 task-specific examples." (Section 3.1, PDF p.7). Contrast: Table 1's own caption on the same page: "Flamingo outperforms the current best methods — fine-tuned on thousands of annotated examples — on seven tasks." (PDF p.7-8).

URL:         https://arxiv.org/abs/2308.01390
Kind:        primary for OpenFlamingo's own reproduction results and its claim that Flamingo's weights/code/data are proprietary (Awadalla et al. are OpenFlamingo's builders and speak from direct, documented attempts to replicate Flamingo); secondary for anything it reports about Flamingo itself, since its authors did not build Flamingo and are reporting on it from outside.
Establishes: That Flamingo's weights, training data, code, and hyperparameters were never released; that an open reproduction trained on public data (LAION-2B and Multimodal C4, replacing Flamingo's proprietary ALIGN and M3W) reaches roughly 85-89% of Flamingo's own reported scores at matched model size, with the gap concentrated on specific tasks (OK-VQA, TextVQA) and widening as more in-context examples are used.
Paraphrase:  OpenFlamingo is an open-source replication of the Flamingo recipe (same frozen-backbone-plus-cross-attention architecture) trained on public web data. It closes most but not all of the gap to Flamingo: OpenFlamingo-3B and -9B reach 85% and 89% of their same-size Flamingo counterparts on average across 7 evaluation datasets, and the paper explicitly frames its own project as a response to Flamingo (and similar models) being closed.
Locators:    Abstract and Section 1 "Introduction" (PDF pp.1-2, arXiv:2308.01390v2, 7 Aug 2023); Section 2 "Related work"/dataset description (PDF pp.3-4); Section 4 "Results" (PDF pp.6-7) and Table 4/Figure 6.
Quote:       "these autoregressive vision-language models are closed-source, and their weights, training data, code, and hyperparameters are proprietary." (Introduction, PDF p.2). "When averaging performance across 7 evaluation datasets, OpenFlamingo-3B and -9B models attain 85% and 89% of their corresponding Flamingo models respectively." (Introduction, PDF p.2). "on OK-VQA and TextVQA, OpenFlamingo models are notably weaker than their Flamingo counterparts: OpenFlamingo-9B underperforms Flamingo-9B in 0-shot evaluations by 6.9 percentage points on OK-VQA and 7.8 percentage points on TextVQA." (Section 4, PDF p.7).

URL:         https://arxiv.org/abs/2203.15556
Kind:        primary — Hoffmann et al. own the Chinchilla model and its "compute-optimal" training claim; this is the paper Flamingo cites (reference [42]) and reuses the 70B checkpoint from.
Establishes: The origin and scale of the frozen language model Flamingo bolts onto: a 70B-parameter language model trained compute-optimally on 1.4 trillion tokens, shown to outperform larger models (Gopher 280B, GPT-3 175B) trained on less data per parameter.
Paraphrase:  Chinchilla is a 70B-parameter language model DeepMind trained to test the hypothesis that prior large language models were undertrained relative to their size; trained on 4x the data of the similarly-expensive Gopher model, it outperforms Gopher and other larger contemporaries. This is the frozen backbone Flamingo-80B (referred to as "Flamingo" in the paper) reuses without further language-only training.
Locators:    Abstract (PDF p.1); Section 4 "Chinchilla" (PDF p.8, text around "we test this hypothesis by training a model on the larger end of this range — 70B parameters — for 1.4T tokens").
Quote:       "we test the optimal model size and number of tokens for training a transformer language model... we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally... We test this by training a more compute-optimal 70B model, called Chinchilla, on 1.4 trillion tokens. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B)..." (Abstract, PDF p.1).

URL:         https://arxiv.org/abs/2106.13884
Kind:        primary — Tsimpoukelli et al. own the "Frozen" method and its multimodal few-shot in-context learning claim; this is the direct architectural predecessor Flamingo's introduction cites (reference [114]) for the idea of feeding visual information into a frozen language model to extend its few-shot capability to vision.
Establishes: That the core trick Flamingo scales up — keep a pretrained language model's weights frozen, train only a small module to turn images into a prompt the LM can read, and get multimodal few-shot in-context learning as a result — predates Flamingo by about a year and was demonstrated at much smaller scale (a frozen 7B-parameter LM, single images only, no video, no interleaved training corpus).
Paraphrase:  "Frozen" trains a lightweight vision encoder so that its output can be prepended to a language model's token embeddings without changing the language model's weights. Once trained, the resulting system can be shown a handful of image/text pairs at inference time and generalizes to new visual tasks the way GPT-3-style language models generalize to new text tasks, including tasks that require binding a newly-introduced visual concept to a word.
Locators:    Abstract (PDF p.1); Section 1 "Introduction" (PDF pp.1-2, "we present Frozen, a method for giving a pre-trained language model access to visual information... without changing its weights"); Section 3 (Figure 3, inference-time interface).
Quote:       "Here, we present Frozen, a method for giving a pre-trained language model access to visual information in a way that extends its few-shot learning capabilities to a multimodal setting, without changing its weights." (Introduction, PDF p.1).

URL:         https://deepmind.google/blog/tackling-multiple-tasks-with-a-single-visual-language-model/
Kind:        primary — DeepMind's own institutional announcement of its own model, published the day before the arXiv preprint went up; same authoring party as the paper, so it carries no independent evidentiary weight beyond the paper, but it is the paper's own public-facing framing of why the result mattered.
Establishes: DeepMind's own framing of Flamingo's significance at release (data efficiency and generality across tasks) and confirms there is no public release of weights or a downloadable model accompanying the announcement.
Paraphrase:  DeepMind frames Flamingo's news as a single model matching or beating task-specific fine-tuned systems while using orders of magnitude less task-specific data, and gestures at future assistive applications without offering the model, code, or weights for download.
Locators:    Blog post body, dated April 28, 2022.
Quote:       "In several cases, the same Flamingo model outperforms methods that are fine-tuned and optimised for each task independently and use multiple orders of magnitude more task-specific data."

URL:         https://arxiv.org/abs/2404.07214
Kind:        secondary — Ghosh, Acharya, Saha, Jain, and Chadha are outside academics surveying the vision-language model field; they did not build Flamingo and have no stake in its results, and they report on it from the published literature.
Establishes: How Flamingo is treated in the current (2024-2025) literature: as the architectural reference point ("frozen backbones bridged by gated cross-attention and a Perceiver Resampler") that later open reproductions (OpenFlamingo) and derivatives (IDEFICS) explicitly measure themselves against, and as a design the field has since partly moved away from — later models increasingly unfreeze components Flamingo kept frozen.
Paraphrase:  The survey credits Flamingo with the interleaved cross-attention plus Perceiver Resampler design and treats it as the closed-source ancestor that open efforts (OpenFlamingo, IDEFICS) were built to reproduce. It also documents a subsequent trend of partially unfreezing what Flamingo kept frozen: it cites BLIP-2 beating Flamingo-80B on zero-shot VQAv2 with far fewer trainable parameters, and Sphinx deliberately unfreezing the language model during pretraining, which the survey frames as improving vision-language alignment beyond what a frozen LM allows.
Locators:    Section 2.1 (architecture discussion of Flamingo); Figure 2 caption (credits Perceiver Resampler to Flamingo); the sections discussing IDEFICS, BLIP-2, and Sphinx. Version used: v3, last revised 14 Oct 2025 (arXiv:2404.07214).
Quote:       "IDEFICS [is] an open-access reproduction of the closed-source vision-language model Flamingo by DeepMind." "BLIP-2 surpasses Flamingo-80B by 8.7% in zero-shot VQA-v2, while utilizing significantly fewer trainable parameters." "Sphinx unfreezes the large language model during pre-training to strengthen vision-language alignment."
```

### Contradictions

1. **The paper contradicts itself on the headline task count.** The abstract, the Section 1 contributions list ("On 6 of these 16 tasks..."), the Figure 2 caption ("...outperforms state-of-the-art fine-tuned models on 6 of the 16 tasks..."), and the Section 3.1 body text ("On six tasks, Flamingo even outperforms the fine-tuned SotA...") all say six. Table 1's own caption, on the same page as the Section 3.1 sentence, says "on seven tasks." I recomputed the comparison directly from Table 1's printed Flamingo-80B 32-shot scores against its own "Fine-tuned SotA" column for all 15 comparable tasks (RareAct has no fine-tuned comparison and is excluded by the paper itself): Flamingo's few-shot score exceeds the fine-tuned SOTA score on exactly six of them — OKVQA (57.8 vs 54.4), MSVDQA (52.3 vs 47.9), Flickr30K (75.4 vs 67.4), iVQA (45.3 vs 35.4), STAR (42.2 vs 36.7), and NextQA (33.5 vs 25.2) — while the fine-tuned SOTA still wins on VQAv2, COCO, VATEX, VizWiz, MSRVTTQA, YouCook2, VisDial, TextVQA, and HatefulMemes (9 tasks). Six plus nine plus the one excluded (RareAct) accounts for all 16. This confirms "six" is both the majority reading in the paper and the number the table's own data supports; "seven" in the Table 1 caption looks like an uncorrected error carried from an earlier draft.

2. **"Beats fine-tuned SOTA" understates how much rests on a self-selected comparison set.** The paper split its 16 benchmarks into a 5-task "DEV" set used to validate design and hyperparameter choices during development (COCO, OKVQA, VQAv2, MSVDQA, VATEX) and an 11-task holdout the authors say they did not tune against. The paper flags its own DEV-set numbers as potentially optimistic: "Performance estimates on the DEV benchmarks may be biased, as a result of model selection." Three of the six few-shot "wins" (OKVQA, MSVDQA — both DEV tasks; and separately, VATEX, VQAv2, COCO are DEV tasks Flamingo does NOT win few-shot) come from a set the authors admit they used to steer the model's own design. This does not overturn the six-task claim, but it is a documented reason to discount how "surprising" a subset of those wins are.

3. **Even fine-tuned, Flamingo did not lead on every remaining benchmark.** Of the nine tasks where Flamingo's few-shot result did not beat fine-tuned SOTA, the paper reports that fine-tuning Flamingo itself sets a new SOTA on five (VQAv2, VATEX, VizWiz, MSRVTTQA, HatefulMemes) but not the other four (COCO, YouCook2, VisDial, TextVQA). The paper's own explanation: "In some cases our results likely trail the state of the art due in part to the fact that we simply optimise log-likelihood and do not make use of common task-specific metric optimisation tricks, such as CIDEr optimisation for COCO captioning, and fine-tuning on dense annotations for VisDial." This is the paper being explicit about the limits of even its fine-tuned numbers, not just its few-shot ones.

4. **Weights were never released, and no source states why.** Two independent, outside parties confirm the fact rather than merely repeating each other: OpenFlamingo (Awadalla et al. 2023, built by a University of Washington/LAION/Allen AI-affiliated team with no stake in Flamingo's reputation) states plainly that Flamingo's "weights, training data, code, and hyperparameters are proprietary," and built its own reproduction specifically because of that gap. The 2024/2025 survey (Ghosh et al.) independently calls Flamingo "the closed-source vision-language model... by DeepMind" when describing IDEFICS's reproduction of it. Neither the Flamingo paper nor DeepMind's own blog post states a reason for withholding the model; the paper's broader-impact section (Appendix, adjacent to the bias/toxicity discussion) discusses risks of the approach in the abstract but does not address release policy directly, so "why" remains genuinely unknown rather than merely unresearched.

### Numbers

```text
Figure: 16 total evaluation benchmarks (5 "DEV" benchmarks used during development: COCO, OKVQA, VQAv2, MSVDQA, VATEX; 11 held out; RareAct is the 16th and is zero-shot only, with no fine-tuned comparison)
Owner:  Alayrac et al. 2022, Section 3 "Experiments" (PDF p.7)
Scope:  Covers image and video captioning, VQA, visual dialogue, multiple-choice QA, and a compositionality/action-recognition task; all few-shot numbers use Flamingo-3B/9B/80B at 0, 4, and 32 shots (Table 1).

Figure: Flamingo (80B) beats the prior fine-tuned state of the art on 6 of the 16 tasks, using 32 in-context examples and no weight updates
Owner:  Alayrac et al. 2022, Section 1 and Section 3.1 (PDF pp.4, 7) — see Contradictions #1 for the "seven" figure printed in Table 1's own caption
Scope:  The six: OKVQA (57.8 vs. fine-tuned SOTA 54.4), MSVDQA (52.3 vs. 47.9), Flickr30K (75.4 vs. 67.4), iVQA (45.3 vs. 35.4), STAR (42.2 vs. 36.7), NextQA (33.5 vs. 25.2). All scores from Table 1, PDF p.7.

Figure: "around 1000 times less task-specific training data" (32 examples vs. the fine-tuned comparison methods' annotation counts)
Owner:  Alayrac et al. 2022, Section 1 (PDF p.4); annotation counts per task from Table 1 (PDF p.7)
Scope:  Table 1 lists each fine-tuned SOTA method's annotation count in parentheses: OKVQA 10K, VQAv2 444K, COCO 500K, MSVDQA 27K, VATEX 500K, VizWiz 20K, Flickr30K 30K, MSRVTTQA 130K, iVQA 6K, YouCook2 10K, STAR 46K, VisDial 123K, TextVQA 20K, NextQA 38K, HatefulMemes 9K. Against Flamingo's 32, the ratio ranges from about 190x (iVQA) to about 15,600x (VQAv2); "1000x" is a rounded order-of-magnitude figure across the full set, not a task-specific ratio.

Figure: For the 9 tasks with a published prior few-shot result, Flamingo-80B sets a new few-shot state of the art on all 9
Owner:  Alayrac et al. 2022, Figure 2 caption (PDF p.3)
Scope:  Distinct from the "6 of 16 beats fine-tuned SOTA" figure — this compares only against prior zero/few-shot methods, not fine-tuned ones, and covers a 9-task subset of the 16 for which such a prior few-shot baseline existed at all.

Figure: With additional fine-tuning (unlimited annotation budget), Flamingo sets a new SOTA on 5 more tasks; 4 remain below prior fine-tuned SOTA
Owner:  Alayrac et al. 2022, Section 3.2 and Appendix B.2.3 (PDF pp.8, 33-34), Table 2/Table 8
Scope:  New SOTA when fine-tuned: VQAv2 (82.0% vs. prior SOTA 81.3%), VATEX, VizWiz, MSRVTTQA, HatefulMemes. Still below prior fine-tuned SOTA after fine-tuning: COCO, YouCook2, VisDial, TextVQA — the paper attributes part of this to rivals' task-specific metric-optimization tricks (e.g., CIDEr optimization for COCO, dense-annotation fine-tuning for VisDial).

Figure: Largest model (called "Flamingo" or Flamingo-80B): 80B parameters total
Owner:  Alayrac et al. 2022, Table 5 (PDF p.28)
Scope:  Composition: 70B frozen Chinchilla language model + 435M frozen NFNet-F6 vision encoder + 10B trainable GATED XATTN-DENSE layers (inserted before every 7th LM block) + 194M trainable Perceiver Resampler. Trainable total ≈10.2B of 80B (≈13%). Two smaller variants: Flamingo-9B (7.1B frozen LM + 435M frozen vision + 1.6B trainable xattn (every 4th block) + 194M resampler = 9.3B total) and Flamingo-3B (1.4B frozen LM + 435M frozen vision + 1.2B trainable xattn (every layer) + 194M resampler = 3.2B total). The frozen LM sizes (1.4B/7B/70B) are the Chinchilla checkpoints of Hoffmann et al. 2022.

Figure: Training data — M3W interleaved web dataset: 43.3 million web documents, 185 million images, 182 GB of text
Owner:  Alayrac et al. 2022, Section 2.4 (PDF p.6) and Appendix F.1 datasheet (PDF p.47)
Scope:  Collected and owned entirely by the Flamingo authors; used with loss weight 1.0 (the dominant weight in the training mixture). Sequences during training were capped at 5 images each, though the trained model generalizes to up to 32 at inference.

Figure: Training data — ALIGN 1.8 billion image/alt-text pairs; LTIP 312 million image-text pairs; VTP 27 million short videos (~22s average) with text
Owner:  ALIGN owned by Jia et al. 2021 (external, reused by Flamingo per Alayrac et al. 2022 Section 2.4, PDF p.6); LTIP and VTP collected and owned by the Flamingo authors (Appendix A.3.3, PDF p.27)
Scope:  Loss weights in training: ALIGN 0.2, LTIP 0.2, VTP 0.03 (M3W is 1.0). ALIGN average caption length 12.4 tokens vs. 20.5 for LTIP, per the paper's own comparison (Appendix A.3.3).

Figure: OpenFlamingo reaches 85% (3B) and 89% (9B) of same-size Flamingo's performance, averaged across 7 evaluation datasets; "more than 86%" across 4 OpenFlamingo variants in the Results section
Owner:  Awadalla et al. 2023, Abstract/Introduction (PDF p.2) and Section 4 Results (PDF p.6)
Scope:  Trained on public LAION-2B (2B pairs) and Multimodal C4 (101M interleaved samples) in place of Flamingo's proprietary ALIGN and M3W. Gap is uneven: OpenFlamingo-9B underperforms Flamingo-9B zero-shot by 6.9 points on OK-VQA and 7.8 points on TextVQA, and the gap widens as more in-context examples are added (Figure 6).
```

### Source assets

```text
Asset: Table 1, "Comparison to the state of the art" (Alayrac et al. 2022, PDF p.7)
Shows: Every one of the 16 benchmarks with Flamingo-3B/9B/80B scores at 0, 4, and 32 shots, the prior zero/few-shot SOTA, and the fine-tuned SOTA with its annotation count. This is the single table that carries the entire "6 of 16, with 32 examples vs. up to 500K" argument; a reader can verify the "six" count directly from it.
Crop:  Must keep enough of the table to show, for at least the six winning tasks and a few losing ones, the 32-shot Flamingo score next to the fine-tuned SOTA score and its annotation count in parentheses. Must not crop out the annotation-count parentheses, since that is what makes the data-efficiency claim legible rather than just a "we won" claim.

Asset: Figure 3, "Flamingo architecture overview" (Alayrac et al. 2022, PDF p.4)
Shows: The frozen vision encoder feeding the Perceiver Resampler, which feeds GATED XATTN-DENSE blocks interleaved with frozen LM blocks — the whole "two frozen pieces plus two new bridges" story in one diagram.
Crop:  Must keep the snowflake/frozen markers on the vision encoder and LM blocks and the labels distinguishing "pretrained and frozen" from "trained from scratch," since that distinction is the architectural point.

Asset: Table 5, "Parameter counts for Flamingo models" (Alayrac et al. 2022, Appendix, PDF p.28)
Shows: The exact frozen/trainable/total parameter split for all three model sizes, side by side.
Crop:  Must keep all three model rows and all four columns (Language, Vision, GATED XATTN-DENSE, Resampler) plus the total; the point is legible only with the frozen-vs-trainable contrast intact across sizes.

Asset: Figure 6, "Evaluation results per dataset across 0, 4, 8, 16, and 32 in-context examples" (Awadalla et al. 2023, PDF p.7)
Shows: OpenFlamingo vs. Flamingo curves per dataset as shots increase, including where OpenFlamingo tracks Flamingo closely (COCO, VQAv2) and where it does not (OK-VQA, TextVQA) and where the gap widens with more shots.
Crop:  Must keep at least one "gap widens" panel and one "closely tracks" panel together; showing only the flattering panels would misrepresent the reproduction's own reported honesty about where it falls short.
```

### Discarded

```text
None — every source located and opened (the Flamingo paper, the OpenFlamingo paper, the Chinchilla paper, the Frozen paper, DeepMind's blog post, and the 2024/2025 survey) was used and cited above. No source was opened and then rejected.
```

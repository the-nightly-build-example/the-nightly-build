# Evidence: the-instruments/clipscore (01)

The evidence supports the full commissioned pipeline and every named failure. Hessel et al. own the exact CLIPScore construction (`w=2.5`, `max(cos,0)`, ViT-B/32) and the captioning correlations that made it standard; Radford et al. own CLIP's contrastive training and its stated weakness at counting and abstract reasoning. Three independent primaries measure the compositional failure the commission needs: ARO shows CLIP near chance on relation and attribution and near chance on caption word-order tests; VQAScore records CLIPScore below the group-chance floor on Winoground; TIFA records CLIPScore's human correlation collapsing on generated images. Two primaries anchor the reward-hacking claim: FuseDream shows CLIP score is adversarially exploitable by gradient ascent, and DDPO shows a learned image-text reward being gamed outright. PickScore anchors the selection-objective case with a measured human-agreement gap. The evidence is thin, and the commission's framing partly misleads, on one point that recurs below: Hessel's headline correlations grade *captions for real images*, not *generated images for prompt alignment*, which is the use the lesson centers on. The correlation numbers that made CLIPScore standard were never measured on the task the lesson teaches. TIFA and VQAScore measure the T2I setting directly, and the numbers there are far lower.

## Sources

```text
URL:         https://arxiv.org/abs/2104.08718
Kind:        primary — Hessel, Holtzman, Forbes, Le Bras, Choi, "CLIPScore: A Reference-free Evaluation Metric for Image Captioning" (EMNLP 2021). Owns the metric's definition and its human-correlation validation.
Establishes: The exact CLIPScore construction, the CLIP backbone used, and the caption-ranking correlations against human judgment.
Paraphrase:  CLIP-S(c,v) = w * max(cos(c,v), 0), with w set to 2.5. The rescaling stretches the raw cosine range (roughly 0 to 0.4 in their data) to span 0 to 1; it does not change rankings. The score is computed with the public ViT-B/32 CLIP model (512-d embeddings). RefCLIPScore adds reference captions: RefCLIP-S = harmonic mean of CLIP-S and the max cosine between the candidate and any reference. On expert human judgments of captions for real Flickr8K images, CLIP-S reaches Kendall tau-c 51.2 and RefCLIP-S 53.0, above SPICE (44.9) and CIDEr (43.9). The authors record where it fails: on news captions needing world knowledge it hits 65% accuracy against METEOR/BLEU-4 near 91-93%, and it prefers literal descriptions over engaging non-literal ones. The conclusion notes CLIP carries its pre-training biases.
Locators:    Section 3 (formula, backbone, RefCLIP-S); Appendix B (reason for w=2.5); Tables 1-3 (Flickr8K-Expert tau-c, Flickr8K-CF tau-b, Composite tau-c); Sections 5.3-5.4 (news/engagement failures); Conclusion (bias). Verified via the arXiv HTML rendering (html/2104.08718v2) and abstract page.
Quote:       "CLIP-S(c,v) = w * max(cos(c,v),0)" and "Multiplying by 2.5 has the effect of 'stretching' the CLIPScore distribution".
```

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary — Radford et al., "Learning Transferable Visual Models From Natural Language Supervision" (CLIP, 2021). Owns what CLIP is and what it cannot do.
Establishes: The contrastive training that produces the shared image-text space CLIPScore reads, the data scale, the encoder choices, and CLIP's own stated blind spots.
Paraphrase:  CLIP trains an image encoder and a text encoder jointly so that, across a batch of N pairs, the cosine similarity of the N true image-text pairs is maximized and the N^2 - N false pairings minimized, under a symmetric cross-entropy loss with a learned temperature. It is trained on 400 million image-text pairs collected from the web (the WIT dataset). Image encoders are ResNet variants and Vision Transformers (ViT-B/32, ViT-B/16, ViT-L/14); the text encoder is a 63M-parameter, 12-layer Transformer with a 76-token limit. The authors list limitations directly: CLIP "struggles with more abstract and systematic tasks such as counting the number of objects in an image," is weak at fine-grained classification, and can be near random on tasks outside its pre-training distribution.
Locators:    Section 2.3 (contrastive objective, temperature); Section 2.2 (400M WIT pairs); Section 2.4 (encoders, text-encoder size, 76-token limit); Section 6 (counting, fine-grained, OOD limitations). Verified via arXiv HTML (html/2103.00020v1) and abstract page.
Quote:       "maximize the cosine similarity of the image and text embeddings of the N real pairs ... while minimizing the cosine similarity of the embeddings of the N^2-N incorrect pairings"; "struggles with more abstract and systematic tasks such as counting the number of objects in an image".
```

```text
URL:         https://arxiv.org/abs/2210.01936
Kind:        primary — Yuksekgonul, Bianchi, Kalluri, Jurafsky, Zou, "When and why vision-language models behave like bags-of-words, and what to do about it?" (ICLR 2023). Owns the controlled measurements of CLIP's relation, attribution, and order behavior.
Establishes: That CLIP is near chance at binding attributes to objects and at understanding relations, and largely insensitive to word order on their order tests — the direct evidence for the composition/word-order failure.
Paraphrase:  The ARO benchmark (over 50,000 test cases) makes CLIP pick the correct caption against a hard negative that swaps a relation, an attribute, or word order. On Visual Genome Relation CLIP scores about 63% and on Visual Genome Attribution about 62%, both near the 50% two-choice chance level; the authors write that most models sit near or below chance on relations. On the order tests CLIP reaches about 46% on COCO-Order and about 59% on Flickr30k-Order. A separate retrieval experiment shows partial, not total, order-blindness: shuffling all words in the caption drops CLIP's COCO Recall@1 from 50.3% to 34.1%, far less than a language-sensitive model should fall.
Locators:    Section 2.3 and Figure 1 (VG-Relation, VG-Attribution); Section 4, Figure 3, Appendix Table 6 (COCO-Order, Flickr30k-Order); Section 3.1 and Table 3 (shuffled-caption retrieval). Verified via arXiv HTML (html/2210.01936v2).
Quote:       "most models are near or below chance level" (relation tests); "CLIP (62%) is again close to chance level" (attribution).
```

```text
URL:         https://arxiv.org/abs/2404.01291
Kind:        primary — Zhiqiu Lin et al., "Evaluating Text-to-Visual Generation with Image-to-Text Generation" (VQAScore, ECCV 2024). Owns the measured CLIPScore-vs-VQAScore comparison on compositional benchmarks.
Establishes: That on generated-image alignment CLIPScore fails compositional prompts, stated in the exact "horse/grass" form the commission uses, with numbers.
Paraphrase:  The paper defines VQAScore as the probability a VQA model assigns to "Yes" for the question "Does this figure show '{text}'?". It states plainly that CLIP text encoders can act as a bag of words, conflating "the horse is eating the grass" with "the grass is eating the horse." In its comparison tables CLIPScore reaches only a 7.8% group score on Winoground against VQAScore's 46.0%; the group score's random-chance floor is 1/6 (about 16.7%) and human performance is about 85.5%, so CLIPScore scores below chance on this compositional set. On TIFA160 CLIPScore reaches 54.1% pairwise accuracy against VQAScore's 71.2%, and on GenAI-Bench image ratings 52.2% against 63.3%.
Locators:    Abstract ("bag of words" quote); Section 3, Equation 2 (VQAScore definition); Tables 1, 4, 9 (Winoground, TIFA160, GenAI-Bench, EqBen). Verified via arXiv HTML (html/2404.01291v2). Winoground group-chance (1/6) and human (~85.5%) are standard properties of that benchmark's group metric; confirm against the Winoground paper if the draft leans on "below chance."
Quote:       "text encoders of CLIP can notoriously act as a 'bag of words', conflating prompts such as 'the horse is eating the grass' with 'the grass is eating the horse'".
```

```text
URL:         https://arxiv.org/abs/2303.11897
Kind:        primary — Yushi Hu et al., "TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering" (ICCV 2023). Owns the measured collapse of CLIPScore's human correlation on generated images.
Establishes: A replacement metric built because CLIPScore fails on generated images, with the CLIPScore correlation number for the T2I setting.
Paraphrase:  TIFA generates question-answer pairs from the prompt with a language model, filters them, then scores an image by the fraction of questions a VQA model answers correctly against it. On TIFA's benchmark of generated images, CLIPScore's correlation with human faithfulness judgments is Spearman 33.2 / Kendall 23.1, near SPICE (32.8 / 23.2) and well below TIFA's 59.7 / 47.2 — roughly 1.8x lower on Spearman. The paper attributes this to CLIP being ineffective at counting and compositional reasoning and to a single global similarity score hiding fine-grained mismatches.
Locators:    Sections 1-2 and Figure 1 (motivation, "CLIP is not effective at counting objects or reasoning compositionally"); Section 3 (faithfulness definition); Table 2, Section 5.1 (CLIPScore vs TIFA correlations). Verified via arXiv HTML (html/2303.11897v1).
Quote:       "CLIP is not effective at counting objects or reasoning compositionally".
```

```text
URL:         https://arxiv.org/abs/2305.01569
Kind:        primary — Kirstain, Polyak, Singer, Matiana, Penna, Levy, "Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation" (PickScore, NeurIPS 2023). Owns the human-preference agreement measurements.
Establishes: The selection-objective case — a CLIP score used to pick images agrees with human preference far less than a purpose-built model, so best-of-N by CLIP optimizes CLIP's taste, not the user's.
Paraphrase:  PickScore is a CLIP-H model fine-tuned on real user choices between image pairs. On the held-out test set, zero-shot CLIP-H agrees with the human choice 60.8% of the time and a CLIP-based aesthetics predictor 56.8%, while PickScore reaches 70.5%, above the 68.0% agreement of human experts with each other. The gap is the cost of selecting images by an off-the-shelf CLIP score: it ranks by CLIP's preference, which diverges measurably from what users pick.
Locators:    Table 1(b) (CLIP-H 60.8, aesthetics 56.8, human expert 68.0, PickScore 70.5). Verified via arXiv HTML (html/2305.01569). The "Random 56.8" row is likely a table copy that should read near 50%; treat only the CLIP-H, human-expert, and PickScore figures as load-bearing.
Quote:       "PickScore ... achieves superhuman performance, as it even outperforms human experts".
```

```text
URL:         https://arxiv.org/abs/2112.01573
Kind:        primary — Xingchao Liu et al., "FuseDream: Training-Free Text-to-Image Generation with Improved CLIP+GAN Space Optimization" (2021). (Confirm the full author list against the arXiv page before any byline use.) Owns a direct demonstration that CLIP score is adversarially exploitable.
Establishes: The reward-hacking claim in its purest CLIP-specific form — a gradient step finds a near-identical image with a much higher CLIP score and no more real relevance.
Paraphrase:  Directly maximizing CLIP score is unsafe because CLIP is easily attacked. Applying FGSM under a small perturbation budget finds an image almost identical to the original yet with a much higher CLIP score, so high CLIP score does not imply semantic relevance and optimizing it invites overfitting. Their fix, AugCLIP, averages the CLIP score over random augmentations of the image, since an adversarial perturbation must then fool CLIP on many augmented copies at once.
Locators:    Section 2.1 "CLIP Can be Easily Attacked and Stuck," Case Study 1 (FGSM attack, overfitting warning, AugCLIP remedy). Verified via the ar5iv HTML rendering of the paper.
Quote:       "FGSM can easily find an image that is almost identical with the original image, yet with much higher CLIP score"; this "indicates a danger of 'overfitting' when we directly maximize the CLIP score".
```

```text
URL:         https://arxiv.org/abs/2305.13301
Kind:        primary — Black, Janner, Du, Kostrikov, Levine, "Training Diffusion Models with Reinforcement Learning" (DDPO, ICLR 2024). Owns a worked reward-hacking case in text-to-image RL.
Establishes: That optimizing a learned image-text reward, rather than a rule, gets gamed — the concrete cost the commission asks for. Note the reward here is a LLaVA-based VLM, not CLIP itself; it demonstrates the failure mode of model-graded rewards, not CLIP specifically.
Paraphrase:  When the model is trained to raise a learned VLM's judgment of "nn animals," it exploits the VLM with a typographic attack: instead of drawing the right count it writes garbled text resembling the number, e.g. "sixx ttutttas" over a picture of eight turtles, which the VLM reads as correct. When trained to raise an incompressibility objective it degenerates into high-frequency noise. In both cases the measured reward rises while the intended goal is missed.
Locators:    Appendix A "Overoptimization," Figure 7 (typographic attack and incompressibility examples). Verified via arXiv HTML (html/2305.13301v4).
Quote:       "the diffusion model exploits the VLM with a typographic attack, writing text that is interpreted as the specified number nn instead of generating the correct number of animals".
```

```text
URL:         https://arxiv.org/abs/2202.04053
Kind:        primary — Cho, Zala, Bansal, "DALL-Eval: Probing the Reasoning Skills and Social Biases of Text-to-Image Generation Models" (ICCV 2023). Owns the PaintSkills measurements and the bias findings.
Establishes: That a global CLIP-style similarity misses spatial and counting composition (they avoid it, scoring with a trained detector instead), and that CLIP-derived models carry gender and skin-tone skew.
Paraphrase:  Rather than a global similarity score, DALL-Eval scores object, count, and spatial-relation skills with a DETR object detector on a controlled dataset (PaintSkills), because a captioning or retrieval metric can be satisfied by different descriptions of the same image. The gap between models and the detector's oracle is large: on spatial relations Stable Diffusion reaches about 7.9% against a 96.2% oracle, and on counting about 37.8% against a 97.8% oracle. The models also learn gender and skin-tone skew from web pairs, e.g. professions defaulting to one gender and skin tones clustering in the mid-range of the Monk scale.
Locators:    Method sections (PaintSkills, DETR-based scoring, the note that alignment metrics can fail when different captions describe one image); results tables (spatial ~7.9%, count ~37.8%, oracles ~96-98%); social-bias section (gender MAD, skin-tone clustering). Verified via arXiv HTML (html/2202.04053v3). The exact per-model skill percentages are supporting, not central; treat the oracle gap as the load-bearing point.
Quote:       "a large gap exists between the performance of all models and the upper bound accuracy on count/spatial skills".
```

```text
URL:         https://arxiv.org/abs/2403.11821
Kind:        secondary — Hartwig et al. (Visual Computing Group, Ulm University), "A Survey on Quality Metrics for Text-to-Image Generation" (2024). Reports on CLIPScore from outside its authoring team.
Establishes: That the field treats CLIPScore as the first standard reference-free alignment metric and now routes around it, which supports the "why it became standard, then got replaced" arc without resting a contested figure on a secondary.
Paraphrase:  The survey names CLIPScore as one of the first reference-free alignment metrics, writes its formula in the same w * max(cos, 0) form, and lists the successors built past it: TIFA, VQAScore, DA-Score, VNLI/SeeTRUE, and others. It notes CLIP-based scoring can overlook misalignments on complex prompts.
Locators:    Alignment-metric section (CLIPScore definition and "one of the first reference-free approaches"); successor-metric discussion (TIFA, VQAScore, DA-Score, etc.). Verified via arXiv HTML (html/2403.11821v5). Use only for context and framing; every contested number in the record is drawn from a primary.
Quote:       "One of the first reference-free approaches ... is CLIPScore".
```

## Contradictions

- **The headline correlations grade the wrong task.** The commission asks for "the reported correlation figures from the original paper" as the evidence that CLIPScore is a "human-correlated check." Hessel's figures (tau-c 51.2, 53.8, etc.) are for ranking *captions written for real images*, the image-captioning task the paper addresses. The lesson is about grading *generated images* for prompt alignment. CLIPScore's strong captioning correlation does not transfer to that use, and the primaries that measure the T2I use directly report much weaker agreement (TIFA: Spearman 33.2). A draft that presents 51.2 as the reason CLIPScore is trusted *for T2I alignment* would misattribute the number. The honest arc: CLIPScore was validated for captioning, then adopted wholesale for T2I alignment, where it correlates far less.

- **"Largely insensitive to word order" is true on controlled tests, partial on retrieval.** ARO's forced-choice order tests put CLIP near chance (COCO-Order ~46%), which backs the commission's phrasing. But ARO's own retrieval experiment shows shuffling all words drops CLIP's Recall@1 from 50.3% to 34.1% — real sensitivity, just far less than warranted. The claim holds, but "largely insensitive" is the accurate strength, not "blind."

- **The cleanest reward-hacking demonstration (DDPO) does not use CLIP.** DDPO's gamed reward is a LLaVA-based VLM, so it evidences the failure mode of model-graded rewards in general. The CLIP-specific version of the claim rests on FuseDream (FGSM against CLIP score) and on the PickScore gap for the selection case. A draft should not cite the "sixx ttutttas" turtles as a CLIPScore result; it is the same mechanism against a different model-grader.

## Numbers

```text
Figure: w = 2.5 (CLIPScore rescaling constant)
Owner:  Hessel et al. 2021, Section 3 / Appendix B
Scope:  Fixed constant; stretches raw cosine (~0 to 0.4) toward 0-1. Does not change rankings.

Figure: CLIP-S Kendall tau-c = 51.2; RefCLIP-S = 53.0 (Flickr8K-Expert)
Owner:  Hessel et al. 2021, Table 1
Scope:  Correlation with expert human judgments ranking captions of real Flickr8K images. Captioning task, not T2I.

Figure: CLIP-S Kendall tau-b = 34.4; RefCLIP-S = 36.4 (Flickr8K-CF)
Owner:  Hessel et al. 2021, Table 2
Scope:  CrowdFlower human judgments, real-image captioning.

Figure: CLIP-S Kendall tau-c = 53.8; RefCLIP-S = 55.4 (Composite)
Owner:  Hessel et al. 2021, Table 3
Scope:  Composite dataset human judgments, real-image captioning.

Figure: 400 million (image, text) pairs (WIT)
Owner:  Radford et al. 2021, Section 2.2
Scope:  CLIP pre-training corpus, web-scraped.

Figure: CLIP VG-Relation ~63%; VG-Attribution ~62% (chance 50%)
Owner:  Yuksekgonul et al. 2023, Section 2.3 / Figure 1
Scope:  Two-choice forced selection against a relation/attribute-swapped hard negative.

Figure: CLIP COCO-Order ~46%; Flickr30k-Order ~59%
Owner:  Yuksekgonul et al. 2023, Section 4 / Figure 3 / Appendix Table 6
Scope:  Forced choice of the correctly ordered caption against reordered negatives.

Figure: CLIP COCO Recall@1 drops 50.3% -> 34.1% under full word shuffle
Owner:  Yuksekgonul et al. 2023, Section 3.1 / Table 3
Scope:  Retrieval with shuffled query caption; measures partial order sensitivity.

Figure: CLIPScore Winoground group = 7.8%; VQAScore = 46.0%; human ~85.5%; group chance ~16.7%
Owner:  Lin et al. 2024, Table 1 (CLIPScore/VQAScore); human and chance are Winoground group-metric properties
Scope:  Winoground group score requires both image-caption matches correct; compositional set.

Figure: CLIPScore TIFA160 pairwise 54.1%; VQAScore 71.2%
Owner:  Lin et al. 2024, Table 9
Scope:  Pairwise ranking accuracy vs human on generated images.

Figure: CLIPScore Spearman 33.2 / Kendall 23.1; TIFA 59.7 / 47.2
Owner:  Hu et al. 2023, Table 2
Scope:  Correlation with human faithfulness judgments on generated images (T2I task). Direct contrast to Hessel's captioning tau.

Figure: CLIP-H human-preference agreement 60.8%; PickScore 70.5%; human experts 68.0%
Owner:  Kirstain et al. 2023, Table 1(b)
Scope:  Agreement with real user pairwise choices on Pick-a-Pic test set.

Figure: Stable Diffusion spatial-relation ~7.9% (oracle ~96.2%); counting ~37.8% (oracle ~97.8%)
Owner:  Cho et al. 2023, PaintSkills results
Scope:  DETR-scored skill accuracy on controlled PaintSkills prompts; supporting figures.
```

## Source assets

```text
Asset: The CLIPScore formula and the RefCLIPScore harmonic-mean definition, Hessel et al. Section 3.
Shows: The whole pipeline in three symbols — cosine, clip at zero, scale by 2.5 — which is the lesson's core mechanism.
Crop:  Keep both equations and the definition of w; a rendered equation or a faithful transcription both work. Omit surrounding prose.

Asset: The CLIP training diagram, Radford et al. Figure 1 (contrastive pre-training: the N-by-N image-text similarity matrix with the diagonal as positives).
Shows: How matched pairs are pulled together and mismatched pairs pushed apart in one shared space — the source of every cosine CLIPScore later reads.
Crop:  Retain the similarity matrix and the labeled image/text encoders. The zero-shot-classifier panels are a separate point; omit them.

Asset: The Winoground / compositional comparison, Lin et al. Table 1 (CLIPScore vs VQAScore group scores).
Shows: The gap between a bag-of-words similarity and a compositional check on the same prompts, in one row.
Crop:  Keep the CLIPScore and VQAScore columns and the Winoground row; a two-bar chart rebuilt from the numbers would read cleaner than the full multi-metric table.

Asset: The DDPO typographic-attack panel, Black et al. Figure 7 (the "nn animals" reward-hacking example).
Shows: A reward being gamed made visible — garbled number-shaped text scoring as a correct count. A vivid concrete case, with the CLIP caveat noted above.
Crop:  Keep one gamed image with its target prompt and the reward it received; the incompressibility-noise panel is a second, weaker example that can be cut.

Asset: The FuseDream adversarial-CLIP figure, Liu et al. Section 2.1 (original vs FGSM-perturbed image with CLIP scores).
Shows: Two near-identical images, one with a much higher CLIP score, proving the score can be raised without raising relevance.
Crop:  Retain both images and both scores side by side; the caption's epsilon budget can stay or go.
```

## Discarded

```text
URL: https://arxiv.org/abs/2411.02437 (TypeScore) — a further T2I metric; adds nothing the survey and VQAScore do not already establish for this lesson.
URL: https://arxiv.org/abs/2601.03468 (Understanding Reward Hacking in T2I RL) — dated beyond a safe verification window and not needed once FuseDream and DDPO anchor the reward-hacking claim; not opened in full.
URL: https://www.emergentmind.com/papers/2303.11897 and researchgate mirrors of TIFA — third-party mirrors of a primary already read at its source; a mirror is not an independent source.
URL: https://aclanthology.org/2021.emnlp-main.595.pdf (CLIPScore at ACL Anthology) — the same primary as arXiv 2104.08718; recorded once at its arXiv landing page.
URL: https://arxiv.org/abs/2204.03162 (Winoground, Thrush et al.) — the benchmark's origin; its group-chance and human numbers are used via VQAScore's table. Worth opening directly only if the draft quotes Winoground's own human study rather than the CLIPScore-vs-VQAScore comparison.
```

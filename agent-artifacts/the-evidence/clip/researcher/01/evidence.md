# Evidence: the-evidence/clip (01)

The record supports the commission's angle firsthand and in the paper's own
words. The three teach points all check out against primary text: (1) the
"a photo of a {label}" prompt template plus 80-prompt ensembling adds close to
5 points to CLIP's zero-shot ImageNet score (1.3 points from the template, 3.5
more from the ensemble), so the headline 76.2% parity with ResNet-50 sits partly
on prompt work rather than the raw model; (2) the 400M-pair training set (WIT)
was never released, only the code and weights were, and the paper positions its
method as a simplified version of prior contrastive image-text work (ConVIRT),
so scale is the new ingredient; (3) the paper itself reports zero-shot is weak on
counting, satellite imagery, tumor detection, and traffic-sign tasks. Where the
record is thin: the CLIP paper's cited passages assert parity with "the original
ResNet-50" without printing ResNet-50's own ImageNet number, so the parity anchor
(~76.1%) comes from a torchvision/He-et-al. reference and is context, not the
paper's figure. One finding cuts against a purely deflationary reading and is
recorded under Contradictions: CLIP's zero-shot models are far more robust to
natural distribution shift than standard ImageNet models (gap closed by up to
75%), and the paper's own train/test overlap audit found contamination did not
inflate the numbers. Both belong in the piece so the angle stays honest.

The best CLIP model is ViT-L/14@336px throughout; the prompt-engineering
ablation numbers (1.3% + 3.5%) are measured on a ResNet-50 CLIP variant. Keep
those two models distinct in the draft.

## Sources

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. It is the document under commission; OpenAI authors it and
             owns every claim, number, and ablation cited below. (Read via the
             ar5iv HTML rendering at ar5iv.labs.arxiv.org/html/2103.00020; the
             address recorded is the paper's own page. PDF also at
             arxiv.org/pdf/2103.00020.)
Establishes: What CLIP is, who built it, the objective, the 400M-pair WIT set
             and its non-release, the 76.2% zero-shot ImageNet parity claim, the
             prompt-engineering/ensembling gains, the weak-task list, the
             robustness finding, and the train/test overlap audit.
Paraphrase:  Title "Learning Transferable Visual Models From Natural Language
             Supervision" (submitted 26 Feb 2021, v1). Authors: Alec Radford,
             Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini
             Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,
             Gretchen Krueger, Ilya Sutskever (OpenAI; affiliation from the
             paper masthead, not the arXiv abstract page). The model is
             pre-trained on 400 million (image, text) pairs collected from the
             internet to predict which caption goes with which image, then used
             zero-shot by naming classes in natural language. Benchmarked on
             over 30 datasets. Best model matches the original ResNet-50 on
             ImageNet zero-shot using none of the 1.28M ImageNet training
             examples.
Locators:    Abstract; Sec. 2.2 (dataset); Sec. 2.3 (objective); Sec. 2.4-2.5
             (architectures, compute); Sec. 3.1.4 (prompt engineering /
             ensembling, Fig. 4); Sec. 3.1.5 (analysis, Fig. 5); Sec. 3.2
             (representation learning / linear probe); Sec. 3.3 (robustness,
             Fig. 13); Sec. 5 (data overlap). Table 1 (Visual N-Grams
             comparison).
Quote:       Objective: "Given a batch of N (image, text) pairs, CLIP is trained
             to predict which of the N x N possible (image, text) pairings across
             a batch actually occurred ... maximize the cosine similarity of the
             image and text embeddings of the N real pairs in the batch while
             minimizing the cosine similarity of the embeddings of the N^2 - N
             incorrect pairings."
             Prompt template: "just using this prompt improves accuracy on
             ImageNet by 1.3%." Ensembling: "On ImageNet, we ensemble 80
             different context prompts and this improves performance by an
             additional 3.5% over the single default prompt discussed above."
             Combined: "prompt engineering and ensembling improve ImageNet
             accuracy by almost 5%."
             Weak tasks: "zero-shot CLIP is quite weak on several specialized,
             complex, or abstract tasks such as satellite image classification
             (EuroSAT and RESISC45), lymph node tumor detection (PatchCamelyon),
             counting objects in synthetic scenes (CLEVRCounts), self-driving
             related tasks such as German traffic sign recognition (GTSRB),
             recognizing distance to the nearest car (KITTI Distance)."
             Non-expert humans caveat: "non-expert humans can robustly perform
             several of these tasks, such as counting, satellite image
             classification, and traffic sign recognition, suggesting
             significant room for improvement."
             Release: "We release our code and pre-trained model weights at
             https://github.com/OpenAI/CLIP." (No release of WIT.)
```

```text
URL:         https://arxiv.org/abs/2205.01397
Kind:        primary for its own claim. Fang, Ilharco, Wortsman, Wan, Shankar,
             Dave, Schmidt run the controlled experiments and own the finding.
Establishes: The cause of CLIP's distribution-shift robustness is the diversity
             of the training data, not language supervision or the contrastive
             loss.
Paraphrase:  "Data Determines Distributional Robustness in Contrastive Language
             Image Pre-training (CLIP)" (submitted 3 May 2022). They study five
             candidate causes of the robustness gains: training set size,
             training distribution, language supervision at train time, language
             supervision at test time, and the contrastive loss. To isolate the
             training distribution they build ImageNet-Captions and train CLIP on
             it.
Locators:    Abstract; controlled-experiment sections.
Quote:       "the more diverse training distribution is the main cause for the
             robustness gains, with the other factors contributing little to no
             robustness."
```

```text
URL:         https://arxiv.org/abs/2212.07143
Kind:        primary for its own claim. Cherti et al. run the open reproduction
             and own its results.
Establishes: A public reproduction of CLIP on open data (LAION) exists, exhibits
             power-law scaling, and shows the training set changes scaling
             behavior between OpenAI's and OpenCLIP's models.
Paraphrase:  "Reproducible scaling laws for contrastive language-image learning"
             (Cherti, Beaumont, Wightman, Wortsman, Gordon, Ilharco, Schuhmann,
             Schmidt, Jitsev; submitted 14 Dec 2022, revised 2024). Scaling
             studied on the public LAION dataset (up to ~2B pairs) using the
             open-source OpenCLIP repository; all models and evaluation code
             released.
Locators:    Abstract; scaling-law sections.
Quote:       "we investigate scaling laws for contrastive language-image
             pre-training (CLIP) with the public LAION dataset and the
             open-source OpenCLIP repository." "The training distribution plays a
             key role in scaling laws as the OpenAI and OpenCLIP models exhibit
             different scaling behavior."
```

```text
URL:         https://laion.ai/blog/giant-openclip/
Kind:        primary for its own result. LAION (author Mitchell Wortsman)
             reports and owns the model and number.
Establishes: A concrete open reproduction figure: a CLIP-architecture model
             trained on public data reaches, and exceeds, the OpenAI zero-shot
             ImageNet level.
Paraphrase:  "Reaching 80% zero-shot accuracy with OpenCLIP: ViT-G/14 trained on
             LAION-2B" (24 Jan 2023). ViT-G/14 trained on the public LAION-2B set
             (32B samples seen) reaches 80.1% zero-shot ImageNet top-1; model
             released through OpenCLIP and the HuggingFace hub.
Locators:    Title and results section.
Quote:       "80.1% zero-shot accuracy on ImageNet."
```

```text
URL:         https://github.com/openai/CLIP
Kind:        primary. OpenAI's official released artifact for the paper.
Establishes: What was and was not released: code and pre-trained weights are
             released; WIT is not mentioned or provided. Confirms the
             "a photo of a {label}" prompt pattern as the intended zero-shot use.
Paraphrase:  README ships code and weights loadable via clip.load("ViT-B/32").
             Training data described only as "a variety of (image, text) pairs";
             no dataset released or named. Zero-shot demo uses templates like
             "a photo of a {label}".
Locators:    Repository README.
```

```text
URL:         https://huggingface.co/docs/transformers/en/model_doc/clip
Kind:        secondary. Third-party (Hugging Face) documentation of how CLIP is
             invoked today; it documents usage, it does not own CLIP's claims.
Establishes: Present-day usage: CLIP as a zero-shot image classifier and an
             image-text similarity/embedding model, with the "a photo of a
             {label}" template carried forward into standard tooling.
Paraphrase:  Describes CLIP as a multimodal model trained on 400M pairs whose
             image and text features project to a shared latent space where a dot
             product gives a similarity score. Ships a "zero-shot-image-
             classification" pipeline; candidate labels are written as
             "a photo of a cat", "a photo of a dog", etc.
Locators:    Model doc overview and code examples.
Quote:       "Both features are projected to a latent space with the same number
             of dimensions and their dot product gives a similarity score."
```

## Contradictions

- Against a purely deflationary reading of "zero-shot" (the angle's risk):
  CLIP's zero-shot models are genuinely and generally more robust to natural
  distribution shift than standard ImageNet-trained models. The CLIP paper
  (Sec. 3.3, Fig. 13) states zero-shot CLIP models "reduce the size of the gap
  between ImageNet accuracy and accuracy under distribution shift by up to 75%."
  This strength is not bought by prompt engineering and is not a benchmark
  artifact; the draft should credit it plainly rather than let the angle imply
  the whole result is borrowed.
- Against a "contamination inflated the number" reading: the CLIP paper's own
  train/test overlap audit (Sec. 5) reports a median overlap of 2.2% between WIT
  and the evaluation sets, with "overall accuracy is rarely shifted by more than
  0.1%" and a maximum detected gain of 0.6% (on Birdsnap). By the paper's own
  measurement, duplication does not explain the zero-shot scores. If the draft
  raises contamination, it must report that the paper checked and found the
  effect small.
- Reinforcing, not breaking, the "scale not idea" point: Fang et al. (2022)
  found the robustness comes from data diversity, not from language supervision
  or the contrastive loss. This strengthens the angle (the data, at scale, is
  the active ingredient) rather than contradicting it, but it reframes the point:
  it is the diversity of the web-scale data, specifically, that matters.
- The paper does not claim novelty of the objective. It positions CLIP as a
  simplified version of ConVIRT (Zhang et al., 2020) and cites earlier
  natural-language-supervision work (Sec. 2.1). This is consistent with the
  angle that the idea predates CLIP; it is the paper's own framing, not a
  contradiction of it.

## Numbers

```text
Figure: 76.2% zero-shot ImageNet top-1 (best CLIP model, ViT-L/14@336px)
Owner:  CLIP paper (Radford et al. 2021), Table 1 / Sec. 3
Scope:  ImageNet-1k validation, top-1, zero-shot (no ImageNet training labels);
        the 1.28M ImageNet training examples are unused.
```

```text
Figure: +1.3 points on ImageNet from the "a photo of a {label}." template
Owner:  CLIP paper, Sec. 3.1.4
Scope:  Over the bare-label baseline; measured on a ResNet-50 CLIP variant.
```

```text
Figure: +3.5 points more on ImageNet from ensembling 80 context prompts
Owner:  CLIP paper, Sec. 3.1.4
Scope:  Over the single "a photo of a {label}." prompt; ResNet-50 CLIP variant.
        Template + ensemble together are stated as "almost 5%" on ImageNet.
```

```text
Figure: 85.4% ImageNet top-1 via a supervised linear probe on CLIP features
Owner:  CLIP paper, Sec. 3.2 (representation learning)
Scope:  Best CLIP features, linear classifier fit on ImageNet labels; ~9.2
        points above the 76.2% zero-shot number. Marks what task-specific
        supervision still buys on top of zero-shot. (Verify the 85.4 against the
        paper's linear-probe table before printing as exact; the 76.2 vs
        linear-probe gap is the load-bearing comparison.)
```

```text
Figure: 400 million (image, text) pairs (WIT / WebImageText)
Owner:  CLIP paper, Sec. 2.2
Scope:  Collected from the internet; ~500,000 queries, up to 20,000 pairs per
        query for approximate class balance; total word count similar to the
        WebText set used for GPT-2. Not released.
```

```text
Figure: gap to distribution-shift accuracy reduced by up to 75%
Owner:  CLIP paper, Sec. 3.3 (Fig. 13)
Scope:  Effective robustness across ImageNet natural-shift sets (ImageNetV2,
        ImageNet-R/Rendition, ObjectNet, ImageNet Sketch, ImageNet-A/Adversarial,
        plus video sets ImageNet-Vid and YouTube-BB), zero-shot.
```

```text
Figure: train/test overlap: median 2.2%, mean 3.2%; accuracy shift rarely
        > 0.1%; max detected gain 0.6% (Birdsnap)
Owner:  CLIP paper, Sec. 5 (duplicate detection)
Scope:  Overlap between WIT and the downstream evaluation datasets.
```

```text
Figure: RN50x64 trained 18 days on 592 V100 GPUs; largest ViT 12 days on 256
        V100 GPUs
Owner:  CLIP paper, Sec. 2.5
Scope:  Training compute for the two largest of the 8 models (5 ResNets: RN50,
        RN101, RN50x4, RN50x16, RN50x64; 3 ViTs: B/32, B/16, L/14, plus the
        L/14@336px extra epoch).
```

```text
Figure: 80.1% zero-shot ImageNet top-1, OpenCLIP ViT-G/14 on LAION-2B
Owner:  LAION blog (Wortsman, 2023)
Scope:  Public reproduction on the public LAION-2B set, 32B samples seen. Anchors
        that the result reproduces on open data and has since been exceeded.
```

```text
Figure: original ResNet-50 ImageNet top-1 ~= 76.1% (context anchor only)
Owner:  Not the CLIP paper. torchvision reference weights report 76.13-76.15%;
        He et al. (2015) report 76.24% (ResNet V1.5). 
Scope:  ImageNet-1k top-1, single model. Use only to anchor the "parity" claim
        for the reader; the CLIP paper asserts parity without printing this
        number, so if the draft states ResNet-50's own figure it must cite this
        separately, not the CLIP paper.
```

## Source assets

```text
Asset: Figure 4 ("Prompt engineering and ensembling improve zero-shot
       performance"), CLIP paper Sec. 3.1.4.
Shows: The average zero-shot score climbing from the context-free/bare-label
       baseline to the prompt template to the ensemble, plotted against compute.
       The single clearest visual argument for the commission's first teach
       point: how much of the headline number is prompt work.
Crop:  Retain the y-axis (average score) and the labeled baseline-vs-prompt-vs-
       ensemble curves. Do not crop off the axis labels; the gain is the point.
```

```text
Asset: Figure 5 ("Zero-shot CLIP is competitive with a fully supervised
       baseline"), CLIP paper Sec. 3.1.5.
Shows: A per-dataset bar chart of zero-shot CLIP minus a supervised linear probe
       on ResNet-50 features. The strong-vs-weak spread is legible at a glance:
       positive bars on natural-image tasks, deeply negative bars on EuroSAT,
       PatchCamelyon, CLEVRCounts, GTSRB, KITTI. Carries the third teach point.
Crop:  Must retain the named weak datasets at the negative end and the zero line;
       omitting either loses the argument. Keep dataset labels readable.
```

```text
Asset: Figure 13 (robustness / effective-robustness scatter), CLIP paper
       Sec. 3.3.
Shows: Zero-shot CLIP sitting well above the standard ImageNet-model trend line
       on the accuracy-vs-distribution-shift plot. The visual behind the
       "up to 75%" gap-closure claim and the Contradictions entry.
Crop:  Retain both axes and the reference trend line; the point is CLIP's
       vertical offset from that line.
```

```text
Asset: Table 1 (CLIP vs Visual N-Grams zero-shot), CLIP paper.
Shows: 76.2% vs 11.5% on ImageNet against the prior zero-shot baseline. Useful if
       the piece needs to establish how far zero-shot moved, less central than
       Figures 4 and 5.
Crop:  Keep the ImageNet row and both method columns.
```

## Discarded

```text
https://x.com/laion_ai/status/1618317487283802113: same 80.1% result as the LAION
  blog but as a promotional tweet; the blog is the source's own page and is used
  instead.
https://openai.com/research/clip and https://openai.com/index/clip: OpenAI's
  own CLIP announcement, a good plain-language primary, but both returned HTTP
  403 to an ordinary fetch (gated, not dead). Not relied on; the paper states
  every limitation and number firsthand, so the blog was not needed. Flagged for
  the writer: if a general-audience OpenAI framing is wanted, this page must be
  opened in a real browser first, as its URL did not resolve for a plain fetch.
Torchvision / He-et-al. ResNet-50 accuracy pages: used only as the context anchor
  in Numbers, not cited as evidence for any CLIP claim.
```

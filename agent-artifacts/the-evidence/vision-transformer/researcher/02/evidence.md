# Evidence: the-evidence/vision-transformer (02)

Supersedes 01. All five primary sources from 01 are preserved unchanged below; this
round adds one secondary (a peer-reviewed vision-transformer survey) that documents how
the commissioned claim circulates in the literature today, satisfying both the series
beat "why the paper became famous / how it is used in arguments today" and the source
policy (min 6 sources, >=3 primary, >=1 secondary). Final composition: 6 sources, 5
primary, 1 secondary.

The evidence supports the commissioned angle as the ViT paper itself frames it. The
paper states plainly that ViT trails comparable ResNets when trained on ImageNet
without strong regularization, and that the ordering reverses only with pre-training
on 14M-300M images. Figure 3, Figure 4, and Table 2 all pin the crossover: BiT ResNets
win at the small end, ViT overtakes at the JFT-300M end. The patch mechanics (patch
size, sequence length, class token, position embeddings) and the three dataset sizes
(ImageNet-1k ~1.28M, ImageNet-21k ~14M, JFT ~303M) are all sourced to the documents
that own them. The added survey shows the "ViT needs large-scale data" reading is the
received framing in secondary literature, quoted below. Where the evidence is thin, or
rather where it cuts against a naive reading of the angle, is the present-day
corrective: DeiT reaches 83.1% on ImageNet-1k alone, no JFT, so "a Transformer needs
JFT-300M" describes the original 2020 recipe, not an inherent limit of the architecture.
ConvNeXt separately shows a pure CNN matching Transformers at the same data budget. The
writer must present the "you need JFT" finding as what the ViT paper showed in 2020, and
as the claim the survey literature still repeats, not as a settled fact of 2026; the
Contradictions section carries the qualification the editor will test the draft against.

## Sources

```text
URL:         https://arxiv.org/abs/2010.11929
Kind:        primary. Dosovitskiy et al. authored ViT; the paper owns every ViT
             number and the mid-size-vs-large-scale claim. ICLR 2021 (v1 Oct 22 2020,
             v2 Jun 3 2021).
Establishes: The patch/sequence construction; the claim that ViT trails ResNets at
             mid-size data and overtakes them with large-scale pre-training; ViT's own
             accuracy figures pinned to model, pre-training dataset, and resolution.
Paraphrase:  An image of resolution HxW is reshaped into N flattened patches of size
             PxP, where N = HW/P^2. A learnable [class] token is prepended to the patch
             embeddings and standard learnable 1D position embeddings are added. Trained
             on ImageNet without strong regularization, ViT lands a few points below
             comparable ResNets; pre-trained on larger datasets (14M-300M images) the
             ordering reverses. ViT-L/16 means the Large variant with 16x16 patches;
             ViT-H/14 is the Huge variant with 14x14 patches.
Locators:    Section 3.1 (patch embedding, class token, position embeddings);
             Introduction (mid-size vs large-scale statement); Section 4.1 (datasets,
             model-variant notation); Section 4.2 / Table 2 (SOTA comparison);
             Section 4.3 / Figures 3-4 (pre-training data requirements).
Quote:       "we reshape the image x in R^{H x W x C} into a sequence of flattened 2D
             patches x_p in R^{N x (P^2 . C)} ... and N = HW/P^2 is the resulting number
             of patches" (Sec 3.1).
             "Similar to BERT's [class] token, we prepend a learnable embedding to the
             sequence of embedded patches" (Sec 3.1).
             "We use standard learnable 1D position embeddings" (Sec 3.1).
             "When trained on mid-sized datasets such as ImageNet without strong
             regularization, these models yield modest accuracies of a few percentage
             points below ResNets of comparable size." (Introduction).
             "However, the picture changes if the models are trained on larger datasets
             (14M-300M images). We find that large scale training trumps inductive
             bias." (Introduction).
             "The BiT CNNs outperform ViT on ImageNet, but with the larger datasets,
             ViT overtakes." (Sec 4.3, discussion of Figure 4).
```

```text
URL:         https://arxiv.org/abs/1707.02968
Kind:        primary for JFT-300M's size. Sun, Shrivastava, Singh, Gupta authored
             "Revisiting Unreasonable Effectiveness of Data in Deep Learning Era"
             (ICCV 2017); this is the paper that introduced JFT-300M to the literature.
Establishes: The size and label character of JFT-300M, the dataset the ViT paper calls
             simply "JFT".
Paraphrase:  JFT-300M holds around 300 million images with more than 375 million noisy
             labels. Vision-task performance rises logarithmically with training-set
             size.
Locators:    Abstract; the dataset description in the body.
Quote:       "By exploiting the JFT-300M dataset which has more than 375M noisy labels
             for 300M images" (Abstract).
Note:        JFT-300M is Google-internal and not public. The exact count the ViT paper
             cites is "18k classes and 303M high-resolution images" (ViT Sec 4.1), which
             is the ViT authors' figure for their JFT snapshot, not Sun et al.'s. Cite
             303M to ViT and ~300M / 375M labels to Sun et al.; do not merge them.
```

```text
URL:         https://arxiv.org/abs/1912.11370
Kind:        primary for the BiT baseline. Kolesnikov, Beyer, Zhai, Puigcerver, Yung,
             Gelly, Houlsby authored Big Transfer (ECCV 2020). It owns BiT-L's identity
             and its 87.5% headline; the ViT paper re-reports BiT-L in Table 2 and there
             it is a secondary restatement.
Establishes: What BiT-L is (the CNN baseline ViT is measured against): a ResNet-152
             widened 4x, pre-trained on JFT-300M, reaching 87.54% top-1 on ImageNet.
             Also fixes ImageNet-1k at 1.28M images / 1000 classes and ImageNet-21k at
             14.2M images / 21k classes.
Paraphrase:  BiT-S pre-trains on ILSVRC-2012 ImageNet (1.28M images, 1000 classes);
             BiT-M on ImageNet-21k (14.2M images, 21k classes); BiT-L on JFT-300M
             (~300M images, 1.26 labels/image on average). The primary BiT model uses a
             ResNet-152 with every hidden layer widened 4x (ResNet152x4), ResNet-v2 with
             Group Normalization and Weight Standardization. BiT-L reaches 87.54 +/- 0.02
             top-1 on ILSVRC-2012.
Locators:    Section 3 (Data for upstream training / model variants); Table 1
             (ILSVRC-2012 result); Abstract (87.5%).
Quote:       "ResNet-152 architectures in all datasets, with every hidden layer widened
             by a factor of four (ResNet152x4)."
             "BiT achieves 87.5% top-1 accuracy on ILSVRC-2012" (Abstract; Table 1 gives
             87.54 +/- 0.02).
```

```text
URL:         https://arxiv.org/abs/2012.12877
Kind:        primary corrective. Touvron, Cord, Douze, Massa, Sablayrolles, Jegou
             authored DeiT (ICML 2021). Owns its own accuracy figures and the
             ImageNet-only training claim.
Establishes: That a ViT-architecture model can be trained competitively on ImageNet-1k
             alone, with no JFT and on a single 8-GPU node, using strong augmentation and
             a token-based distillation from a CNN teacher.
Paraphrase:  DeiT trains a convolution-free transformer on ImageNet only. The reference
             model (86M parameters, the DeiT-B / ViT-B configuration) reaches 83.1%
             top-1 single-crop with no external data. A distillation token lets the
             student learn from a teacher through attention; the default teacher is
             RegNetY-16GF, a CNN (84M params, 82.9%). Training runs on a single 8-GPU
             node in two to three days.
Locators:    Abstract; Section 1; Table 5 (results by model, resolution, epochs);
             Section 4 (distillation, teacher choice).
Quote:       "We produce a competitive convolution-free transformer by training on
             Imagenet only." (Abstract).
             "Our reference vision transformer (86M parameters) achieves top-1 accuracy
             of 83.1% (single-crop evaluation) on ImageNet with no external data."
             (Abstract).
             "the default teacher is a RegNetY-16GF" (Sec 4).
Note:        Accuracies pinned in the Numbers section below. The abstract's "up to
             85.2%" is a specific extended-training row, not the reference number; do
             not quote 85.2% as the headline without its conditions.
```

```text
URL:         https://arxiv.org/abs/2201.03545
Kind:        primary corrective. Liu, Mao, Wu, Feichtenhofer, Darrell, Xie authored
             "A ConvNet for the 2020s" (ConvNeXt, CVPR 2022). Owns its accuracy figures.
Establishes: That a pure CNN, modernized toward Transformer design choices, matches or
             beats the Swin Transformer at equal data budgets, including 87.8% on
             ImageNet with ImageNet-22k pre-training.
Paraphrase:  ConvNeXt is built entirely from standard ConvNet modules. Trained from
             scratch on ImageNet-1k at 224, ConvNeXt-T/S/B reach 82.1 / 83.1 / 83.8,
             each at or above the matched Swin-T/S/B (81.3 / 83.0 / 83.5). Pre-trained on
             ImageNet-22k and fine-tuned at 384, ConvNeXt-XL reaches 87.8.
Locators:    Abstract; Table 1 (ImageNet-1k trained-from-scratch and ImageNet-22k
             pre-trained sections).
Quote:       "Constructed entirely from standard ConvNet modules, ConvNeXts compete
             favorably with Transformers in terms of accuracy and scalability, achieving
             87.8% ImageNet top-1 accuracy and outperforming Swin Transformers on COCO
             detection and ADE20K segmentation." (Abstract).
```

```text
URL:         https://arxiv.org/abs/2101.01169
Kind:        secondary. Khan, Naseer, Hayat, Zamir, F. S. Khan, Shah authored
             "Transformers in Vision: A Survey" (ACM Computing Surveys, 2022). None of
             these authors wrote ViT and none have a stake in its claims; they survey
             the field and report on ViT from outside. By the authorship-and-stake test
             this is secondary: it restates and characterizes ViT's finding rather than
             owning it. It serves the series beat "why the ViT paper became famous / how
             the claim is used today": a peer-reviewed survey treating ViT as a landmark
             and repeating its data-scale requirement as received understanding.
Establishes: That the "ViT needs large-scale pre-training to be competitive" reading is
             the standard framing in the secondary literature, stated in the survey's own
             words, including a quantified restatement of the ImageNet-1k-vs-JFT gap.
Paraphrase:  The survey states that ViT-L drops sharply on ImageNet when trained on
             ImageNet alone versus pre-trained on JFT-300M, and explains the gap by the
             inductive biases CNNs carry and Transformers lack, so a Transformer must
             recover that structure from very large-scale data. This is a repetition: it
             evidences that the claim is made and circulates, not independently that the
             magnitude is exact (see the Numbers note on the 13% figure).
Locators:    Section II-B "(Self) Supervised Pre-training"; Section III-B1
             "Uniform-scale Vision Transformers".
Quote:       "Vision Transformer model (ViT-L) experiences an absolute 13% drop in
             accuracy on ImageNet test set when trained only on ImageNet train set as
             compared to the case when pretrained on JFT dataset with 300 million
             images." (Sec II-B).
             "Pre-training ViT on a medium-range dataset would not give competitive
             results, because the CNNs encode prior knowledge about the images (inductive
             biases e.g., translation equivariance) that reduces the need of data as
             compared to Transformers which must discover such information from very
             large-scale data." (Sec III-B1).
```

## Contradictions

The commissioned angle is "ViT trails CNNs at mid-size data and needs large-scale
pre-training (JFT-300M) to match or beat them." Two present-day sources complicate the
present-tense version of that claim, and the ViT paper itself carries one caveat.

1. DeiT breaks the strong reading. The ViT paper's finding was that ViT *as trained in
   that paper* needed JFT-scale data. DeiT reaches 83.1% on ImageNet-1k alone, no
   external data, by adding strong augmentation and distillation. So the barrier was the
   training recipe and regularization, not a property of the Transformer architecture.
   Note the ViT paper hedged exactly here: its own statement is about ImageNet "without
   strong regularization" (Introduction). DeiT supplies the strong regularization the
   ViT authors flagged as missing. The two papers do not contradict on fact; they
   contradict the naive slogan "Transformers need JFT."

2. ConvNeXt breaks "Transformers beat CNNs." A pure CNN, updated with Transformer-era
   design choices, matches or beats the Swin Transformer at every matched size and hits
   87.8% with ImageNet-22k pre-training. The 2020 gap was not CNN-versus-Transformer in
   the abstract; it closed once each side adopted the other's training and design ideas.

3. DeiT's distillation teacher is a CNN (RegNetY-16GF). The strongest ImageNet-1k-only
   transformer results lean on knowledge transferred from a convolutional model, which
   further muddies any clean "Transformers won" narrative.

4. Compute, not only data. The ViT paper's headline is partly a compute claim: ViT
   reaches its results "while requiring substantially fewer computational resources to
   train" (Abstract). An article that frames the story as purely about data volume drops
   half of what the paper claimed.

5. The secondary keeps the strong reading alive. The Khan survey, published after DeiT,
   still states flatly that "Pre-training ViT on a medium-range dataset would not give
   competitive results" (Sec III-B1). This is useful two ways: it documents that the
   commissioned claim is the received view, and it is itself an example of the survey
   literature stating the 2020 finding without the DeiT qualification. The writer can
   cite it for how the claim circulates, and should not treat its restatement as
   independent confirmation of the magnitude.

None of these overturn the historical finding. They constrain how the writer states it
in the present tense.

## Numbers

```text
Figure: 88.55% +/- 0.04  (ViT-H/14, ImageNet top-1)
Owner:  ViT paper, Table 2
Scope:  Pre-trained on JFT-300M, fine-tuned/evaluated on ImageNet-1k; mean +/- std over
        3 fine-tuning runs.
```

```text
Figure: 90.72% +/- 0.05  (ViT-H/14, ImageNet-ReaL)
Owner:  ViT paper, Table 2
Scope:  Pre-trained on JFT-300M; ReaL (Reassessed Labels) variant of ImageNet.
```

```text
Figure: 87.76% +/- 0.03  (ViT-L/16, ImageNet top-1)
Owner:  ViT paper, Table 2
Scope:  Pre-trained on JFT-300M, evaluated on ImageNet-1k; 3-run mean +/- std.
```

```text
Figure: 85.30% +/- 0.02  (ViT-L/16, ImageNet top-1)
Owner:  ViT paper, Table 2
Scope:  Pre-trained on the public ImageNet-21k (14M images), evaluated on ImageNet-1k.
        The clean same-model contrast to the JFT row above: 85.30 (21k) vs 87.76 (JFT).
```

```text
Figure: 87.54% +/- 0.02  (BiT-L, ResNet152x4, ImageNet top-1)
Owner:  BiT paper, Table 1 (re-reported in ViT Table 2 as 87.54 +/- 0.02)
Scope:  Pre-trained on JFT-300M, fine-tuned on ILSVRC-2012 ImageNet-1k. The CNN baseline
        ViT-H/14 (88.55) and ViT-L/16 (87.76) are measured against.
```

```text
Figure: 88.4% / 88.5%  (Noisy Student, EfficientNet-L2, ImageNet top-1)
Owner:  ViT paper, Table 2 (prior SOTA row; original: Xie et al. Noisy Student)
Scope:  EfficientNet-L2 with Noisy Student self-training (ImageNet + JFT-300M as
        unlabeled). Listed as the CNN-based prior state of the art ViT-H/14 edges.
        Treat as ViT's restatement, not a primary read of the Noisy Student paper.
```

```text
Figure: 81.8%  (DeiT-B, ImageNet top-1, 224 res, no distillation)
Owner:  DeiT paper, Table 5
Scope:  Trained on ImageNet-1k only, 300 epochs, 224x224, single-crop.
```

```text
Figure: 83.1%  (DeiT-B↑384, ImageNet top-1, 384 res, no distillation)
Owner:  DeiT paper, Abstract and Table 5
Scope:  Trained on ImageNet-1k only, fine-tuned at 384x384. This is the abstract's
        "reference ... 83.1%" number, the fair no-distillation headline.
```

```text
Figure: 84.5%  (DeiT-B distilled ↑384, ImageNet top-1, 384 res, 300 epochs)
Owner:  DeiT paper, Table 5
Scope:  ImageNet-1k only, token distillation from RegNetY-16GF teacher, 384x384,
        default 300 epochs.
```

```text
Figure: 85.2%  (DeiT-B distilled ↑384, ImageNet top-1, 384 res, 1000 epochs)
Owner:  DeiT paper, Abstract ("up to 85.2%") and Table 5
Scope:  ImageNet-1k only, distilled, 384x384, extended 1000-epoch training. Best DeiT
        number; only honest if quoted with the 1000-epoch and distillation conditions.
```

```text
Figure: 82.1% / 83.1% / 83.8%  (ConvNeXt-T / -S / -B, ImageNet top-1, 224 res)
Owner:  ConvNeXt paper, Table 1
Scope:  Trained from scratch on ImageNet-1k, 224x224. Matched Swin-T/S/B: 81.3 / 83.0 /
        83.5. ConvNeXt at or above Swin at every size.
```

```text
Figure: 87.8%  (ConvNeXt-XL, ImageNet top-1, 384 res)
Owner:  ConvNeXt paper, Abstract and Table 1
Scope:  Pre-trained on ImageNet-22k, fine-tuned at 384x384. The pure-CNN counterpart to
        the ViT/BiT JFT-scale numbers, but on the public 22k set, not JFT.
```

```text
Figure: ~13% absolute ImageNet drop (ViT-L, ImageNet-1k-only vs JFT-300M pre-training)
Owner:  Khan et al. survey, Sec II-B — SECONDARY restatement, not verified against the
        ViT paper's own tables. The ViT paper does not print a ViT-L ImageNet-1k-only
        top-1 in Table 2; the magnitude here is the survey's characterization.
Scope:  Document that this quantified form of the claim circulates. If the writer wants
        to state the gap as fact, verify against ViT Figure 3 / the ViT appendix, not
        against this repetition.
```

```text
Figure: 196  (sequence length for 224x224 image, 16x16 patches)
Owner:  Derived from ViT paper, Section 3.1 (N = HW/P^2 = 224^2 / 16^2 = 196)
Scope:  Not printed verbatim in the ViT text; it is the arithmetic of the paper's own
        formula for the standard 224 input at patch size 16. A class token makes the
        input sequence 197. Present as a worked example, not a quoted figure.
```

```text
Figure: ~1.28M images / 1000 classes (ImageNet-1k, ILSVRC-2012)
Owner:  BiT paper, Section 3 (ViT gives the rounded "1.3M images")
Scope:  Standard supervised ImageNet training set. Anchor for "mid-size."
```

```text
Figure: 14M (ViT) / 14.2M (BiT) images, 21k classes (ImageNet-21k)
Owner:  ViT Sec 4.1 ("14M"); BiT Sec 3 ("14.2 million"). Cite either to its owner.
Scope:  The larger public pre-training set, the middle rung between ImageNet-1k and JFT.
```

```text
Figure: 303M images, 18k classes (JFT, ViT snapshot) / ~300M images, 375M labels
        (JFT-300M, Sun et al.)
Owner:  ViT Sec 4.1 ("18k classes and 303M high-resolution images"); Sun et al. Abstract
        ("375M noisy labels for 300M images").
Scope:  The private large-scale set. Two owners, two snapshots; keep the figures with
        their sources.
```

## Source assets

```text
Asset: ViT paper, Figure 1 (model overview: image split into patches, linear projection,
       prepended [class] token, position embeddings, Transformer encoder).
Shows: The whole patch-to-sequence mechanic the lesson has to teach, in one diagram.
Crop:  Must retain the patch grid, the flattened-patch row, the [class] token, and the
       "+" position-embedding markers. The MLP-head detail on the right can be dropped.
```

```text
Asset: ViT paper, Figure 3 ("Transfer to ImageNet": ViT variants vs BiT ResNet shaded
       band, x-axis pre-training dataset ImageNet / ImageNet-21k / JFT-300M).
Shows: The crossover itself. BiT wins the small-data end, ViT overtakes at JFT. This is
       the single most direct visual of the commissioned angle.
Crop:  Must keep the x-axis dataset labels and the BiT shaded region; both series legends
       are load-bearing. Do not crop out the ImageNet-1k left end, which is where ViT
       loses.
```

```text
Asset: ViT paper, Figure 4 (linear few-shot on ImageNet vs pre-training size, log x-axis;
       ResNets vs ViT).
Shows: ResNets stronger at small pre-training but plateau; ViT keeps climbing. A cleaner,
       continuous version of the same crossover than Figure 3's discrete points.
Crop:  Keep the log-scaled x-axis label and both curves' crossing region.
```

```text
Asset: DeiT paper, the accuracy-vs-throughput figure (DeiT models against EfficientNet
       and ViT on the ImageNet accuracy / images-per-second plane).
Shows: DeiT reaching competitive ImageNet accuracy trained on ImageNet-1k alone, the
       corrective in one frame.
Crop:  Keep the axis labels and the DeiT vs ViT vs EfficientNet legend.
```

```text
Asset: ConvNeXt paper, Figure 1 (ImageNet-1k accuracy bubble chart, ConvNeXt vs Swin vs
       ViT/DeiT, bubble area = FLOPs).
Shows: A pure CNN sitting on or above the Transformer frontier at matched compute.
Crop:  Keep the ConvNeXt and Swin series and the accuracy axis; bubble-size legend must
       survive or the FLOPs encoding is lost.
```

Note for the writer: per press/charts policy, any chart in the article is a PNG rendered
from a committed chart-N.py, not a screenshot of these figures. The figures above are
evidence of what the argument can show and a guide to what a rendered chart should
reproduce, not drop-in images. The Khan survey carries no original figure worth citing;
its value is textual, quoted above.

## Discarded

```text
URL: https://api.semanticscholar.org/graph/v1/paper/arXiv:2010.11929 — attempted as a
     citation-impact record for the "why it became famous" beat. Returned HTTP 429 (rate
     limited) on every attempt; not read, so not cited. The fame beat is instead served
     by the Khan survey and by DeiT/ConvNeXt positioning themselves against ViT.
```

```text
URL: https://api.openalex.org/works (title search for the ViT paper) — attempted as an
     alternate citation-impact record. Returned an account-budget error, not read, not
     cited.
```

```text
URL: (ViT/DeiT/ConvNeXt/BiT PDFs via ar5iv/arxiv html endpoints) — used only as a
     reading transport for the arxiv.org/abs pages recorded above; not recorded as
     separate sources, since each document's own page is its arxiv abstract landing.
```

No sources were read and rejected on merit. Every document opened and read is cited.
The Discarded section records the two citation-count endpoints that were gated before
they could be read, and the transport note, for honesty about how the full texts were
reached.

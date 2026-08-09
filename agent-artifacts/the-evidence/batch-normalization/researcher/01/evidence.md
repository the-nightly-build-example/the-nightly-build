# Evidence: the-evidence/batch-normalization (01)

The record supports the commissioned arc firsthand. The Ioffe & Szegedy 2015
paper owns what batch normalization is, the normalization procedure, the
inference-time change to population statistics, the 14x step-count speedup to
72.2% ImageNet accuracy, and the 6-model ensemble result of 4.9% top-5
validation error (4.82% test). The paper's own one-sentence definition of
"internal covariate shift" is verified against the PDF. Santurkar et al. 2018
owns the direct contradiction: the noise-after-BatchNorm experiment and the
loss-landscape/Lipschitz measurements, with the authors' exact claim that
distributional stability "has little to do with the success of BatchNorm."

The record is thin in one place the writer must respect: the *replacement*
mechanism is not settled. Santurkar measure a gradient-based reformulation of
ICS, not the literal distribution shift Ioffe & Szegedy defined, and they find
plain L1/L2/Linf normalization smooths the landscape as well or better than
BatchNorm, so "landscape smoothing" is a strong account of what breaks the ICS
story rather than a proven unique cause. Bjorck et al. 2018 offers a third,
different account (larger learning rates). This does not undermine the
commissioned angle. It sharpens it: the "reduce ICS" explanation fails a
controlled test, and no single successor is yet established. The commission
already asks not to overclaim a settled replacement.

Human top-5 error of 5.1%, which the batch-norm paper says it exceeds, is owned
by Russakovsky et al., not by Ioffe & Szegedy, and rests on one annotator
labeling 1500 images. That denominator is recorded below.

## Sources

```text
URL:         https://arxiv.org/abs/1502.03167
Kind:        primary. Ioffe & Szegedy own the method, the ICS claim, and every
             training number the lesson quotes. It is the document under review.
Establishes: What batch normalization is; the per-mini-batch normalization
             algorithm; the learned scale/shift; the inference-time switch to
             population statistics; the paper's own definition of internal
             covariate shift; the 14x speedup; the ensemble top-5 result.
Paraphrase:  During training each activation is normalized using its own
             mini-batch mean and variance, then rescaled and reshifted by two
             learned parameters (gamma, beta) so the network can recover any
             distribution it needs, including the un-normalized one. At
             inference the network stops using batch statistics and uses fixed
             population mean and variance (tracked by moving averages over
             training), so an input's output no longer depends on the other
             examples in its batch. The paper frames the problem it solves as
             "internal covariate shift" and puts that phrase in its title.
Locators:    Abstract; Sec. 2 (definition); Algorithm 1 and Sec. 3 (training
             procedure); Sec. 3.1 (inference / population statistics); Sec.
             4.2.2 (speedup, Figure 2 and its table); Sec. 4.2.3 (ensemble).
Quote:       "We define Internal Covariate Shift as the change in the
             distribution of network activations due to the change in network
             parameters during training." (Sec. 2)
             "BN-x5 needs 14 times fewer steps than Inception to reach the
             72.2% accuracy." (Sec. 4.2.2)
             "Here we report a top-5 validation error of 4.9%, and test error
             of 4.82% (according to the ILSVRC server) ... exceeds the
             estimated accuracy of human raters according to (Russakovsky et
             al., 2014). For our ensemble, we used 6 networks." (Sec. 4.2.3)
             Inference: "once the network has been trained, we use the
             normalization ... using the population, rather than mini-batch,
             statistics." (Sec. 3.1)
```

```text
URL:         https://arxiv.org/abs/1805.11604
Kind:        primary. Santurkar, Tsipras, Ilyas & Madry (MIT) own the
             experiment and measurements that contradict the stated mechanism.
Establishes: That distributional stability of layer inputs has "little to do
             with" why BatchNorm works; the noise-injection experiment; the
             gradient-based measurement of ICS; the landscape-smoothing /
             Lipschitz account; and the caveat that smoothing is not unique to
             BatchNorm.
Paraphrase:  They train a network that adds fresh random noise with non-zero
             mean and non-unit variance to activations *after* the BatchNorm
             layer, changing the noise every step. This deliberately produces
             severe distribution shift, worse than a network with no BatchNorm
             at all, yet the noisy-BatchNorm network still trains about as fast
             and as accurately as the clean one. They also redefine ICS in
             optimization terms (Definition 2.1): the change in a layer's own
             gradient before versus after the preceding layers are updated on
             the same step, measured by cosine angle and L2 distance. By that
             measure BatchNorm networks have similar or even worse ICS while
             still training better. Their positive claim is that BatchNorm
             makes the loss and its gradients more Lipschitz, so the loss
             changes more smoothly and a gradient step points where the
             optimizer expects. They then show plain Lp normalization (p = 1,
             2, infinity), which does not keep inputs Gaussian or control their
             distribution, smooths the landscape as well or better.
Locators:    Abstract; Sec. 2.1 (noise experiment, Figure 2); Sec. 2.2 and
             Definition 2.1 (gradient-based ICS, Figure 3); Sec. 3.1-3.2
             (Lipschitz / beta-smoothness, Figure 4); Sec. 3.3 (Lp
             normalization, non-uniqueness). Version 1 (2018) carried the
             blunt subtitle "(No, It Is Not About Internal Covariate Shift)."
Quote:       "we demonstrate that such distributional stability of layer inputs
             has little to do with the success of BatchNorm. Instead ... it
             makes the optimization landscape significantly smoother."
             (Abstract)
             "in a certain sense BatchNorm might not even be reducing internal
             covariate shift." (Sec. 1, Our Contributions)
             "this smoothening effect is not uniquely tied to BatchNorm. A
             number of other natural normalization techniques have a similar
             (and, sometime, even stronger) effect." (Sec. 1)
```

```text
URL:         https://arxiv.org/abs/1806.02375
Kind:        primary. Bjorck, Gomes, Selman & Weinberger (Cornell) own their
             own learning-rate account of BatchNorm.
Establishes: A third mechanism story, distinct from both ICS and Santurkar's
             smoothing: that BatchNorm's main benefit is permitting larger
             learning rates, and that large rates drive the faster convergence
             and better generalization.
Paraphrase:  They argue the primary thing BatchNorm buys is the ability to
             train at higher learning rates without activations and gradients
             blowing up with depth, and that the higher rate is what produces
             the speed and the generalization gain. Like Santurkar, they treat
             the internal-covariate-shift explanation as not the operative one.
Locators:    Abstract; results on learning-rate ablations. (Read at abstract
             and claim level, not line-verified against the PDF body.)
Quote:       "BN primarily enables training with larger learning rates, which
             is the cause for faster convergence and better generalization."
             (as stated in the abstract)
```

```text
URL:         https://arxiv.org/abs/1803.08494
Kind:        primary. Wu & He (Facebook AI Research) own the batch-size
             dependence result and the Group Normalization alternative.
Establishes: That BatchNorm's error rises sharply as batch size shrinks,
             because the batch statistics are estimated from too few examples.
Paraphrase:  BatchNorm depends on having a reasonably large batch to estimate
             mean and variance. At batch size 2 on ResNet-50 / ImageNet their
             batch-size-independent Group Normalization has 10.6 percentage
             points lower error than BatchNorm. This is a limit on the method,
             not on the correction, and it belongs to the "still debated" note
             about when BatchNorm hurts.
Locators:    Abstract; Sec. 1 and the batch-size comparison figure/table.
             (Read at abstract and claim level.)
Quote:       "BN's error increases rapidly when the batch size becomes smaller,
             caused by inaccurate batch statistics estimation." (Abstract)
             GN "has 10.6% lower error than its BN counterpart" at batch size 2.
```

```text
URL:         https://arxiv.org/abs/1409.0575
Kind:        primary. Russakovsky et al. own the ImageNet/ILSVRC dataset scale
             and the human-accuracy estimate the batch-norm paper compares to.
Establishes: The 5.1% human top-5 error figure and how it was obtained; the
             ILSVRC-2012 classification dataset size that is the denominator
             for every ImageNet number in the lesson.
Paraphrase:  Human top-5 error on this task is not a population statistic. It
             comes from one trained expert annotator (A1) who labeled 1500 test
             images and scored 5.1% top-5 error; on the same 1500 images
             GoogLeNet scored 6.8%, close to its 6.7% error on the full 100,000
             test images. A second annotator (A2) trained less, labeled 258
             images, and scored about 12.0%. So "better than human" means
             better than one careful person on a 1500-image sample. The
             classification dataset is 1000 categories, about 1.28 million
             training images, 50,000 validation images, 100,000 test images.
Locators:    Sec. 6.4.1 (human vs computer accuracy, Table 9); Table 2
             (dataset scale). Verified firsthand from the PDF.
Quote:       "The first annotator (A1) trained on 500 images and annotated 1500
             test images. The second annotator (A2) trained on 100 images and
             then annotated 258 test images." (Sec. 6.4.1)
             "The human error was estimated to be 5.1%." (A1, Sec. 6.4.1)
             A2 error "at approximately 12.0% Top-5 error." (Sec. 6.4.1)
```

```text
URL:         https://d2l.ai/chapter_convolutional-modern/batch-norm.html
Kind:        secondary. The "Dive into Deep Learning" textbook (Zhang, Lipton,
             Li, Smola) reports the mechanism debate from outside both camps.
Establishes: That the field treats the ICS explanation as contested and the
             true reason as not rigorously settled. Useful for the lesson's
             "how to hold both" framing and as an independent voice, not for
             any number.
Paraphrase:  The textbook records that the original ICS intuition was
             under-specified, that the drift observed is arguably closer to
             concept drift than to covariate shift, that Santurkar et al.
             showed BatchNorm behaves in ways opposite to the original paper's
             claims, and that the real reason BatchNorm works remains an open
             question. It frames the lesson as separating guiding intuition
             from established fact.
Locators:    Batch Normalization chapter, "Discussion" / controversy section.
Quote:       Paraphrased above; the textbook states BatchNorm's "success comes
             despite exhibiting behavior that is in some ways opposite to those
             claimed in the original paper."
```

## Contradictions

- The paper's mechanism versus Santurkar's test. Ioffe & Szegedy claim
  BatchNorm helps by reducing internal covariate shift. Santurkar's noise
  experiment injects severe shift after BatchNorm and training stays fast, and
  their gradient-based ICS metric shows BatchNorm networks with similar or
  worse ICS still train better. This is the central, verified contradiction and
  the article's spine.

- Santurkar's ICS is a reformulation, not the original quantity. Ioffe &
  Szegedy define ICS as a change in the *distribution* of activations.
  Santurkar measure ICS as a change in a layer's *gradient* across the update
  step (Definition 2.1). A reader could object that the correction refutes a
  restated version of the claim. The correction is still strong, because the
  noise experiment attacks the distributional version directly, but the writer
  should not present the two ICS definitions as identical.

- The replacement mechanism is itself contested. Santurkar say landscape
  smoothing is the cause, then show plain Lp normalization smooths as well or
  better, so smoothing is not a property unique to BatchNorm. Bjorck et al.
  argue the operative benefit is tolerance of larger learning rates. Three
  papers agree the ICS story fails and disagree on what replaces it. This
  supports the commission's instruction not to sell a settled successor.

- BatchNorm is not uniformly beneficial. Wu & He show it degrades at small
  batch sizes. This does not defend the ICS story; it bounds the method and
  feeds the "still debated / sometimes hurts" note.

- A search-surfaced lead not verified firsthand: some adversarial-training work
  reports ICS-like distribution shifts that appear to matter in that setting,
  which would bound Santurkar's clean-training conclusion. Recorded as a lead
  only. No such paper was read to the passage, so it must not be cited as
  established unless a later brief resolves it.

## Numbers

```text
Figure: 14x fewer training steps
Owner:  Ioffe & Szegedy 2015 (Sec. 4.2.2, Figure 2 table)
Scope:  Steps to reach 72.2% single-crop validation accuracy on ImageNet
        ILSVRC-2012, Inception-based net. Inception 31.0e6 steps; BN-x5 2.1e6.
```

```text
Figure: Max single-crop validation accuracy: Inception 72.2%, BN-Baseline
        72.7%, BN-x5 73.0%, BN-x30 74.8%
Owner:  Ioffe & Szegedy 2015 (Sec. 4.2.2, Figure 2 table)
Scope:  ImageNet ILSVRC-2012 validation, single crop. BN-x5-Sigmoid reached
        69.8% (sigmoid activations, still trained where plain Inception did not).
```

```text
Figure: 4.9% top-5 validation error; 4.82% top-5 test error
Owner:  Ioffe & Szegedy 2015 (Sec. 4.2.3)
Scope:  Ensemble of 6 networks (each based on BN-x30), ImageNet ILSVRC-2012,
        50,000 validation / 100,000 test images, test error per ILSVRC server.
        Abstract rounds test error to 4.8%; body states 4.82%.
```

```text
Figure: 5.1% human top-5 error
Owner:  Russakovsky et al. 2015 (Sec. 6.4.1), NOT the batch-norm paper
Scope:  One expert annotator (A1) on a 1500-image test sample. GoogLeNet 6.8%
        on the same 1500; 6.7% on the full 100,000 test set. Second annotator
        (A2) 12.0% on 258 images.
```

```text
Figure: 10.6 percentage points
Owner:  Wu & He 2018 (Abstract / Sec. 1)
Scope:  ResNet-50 on ImageNet at batch size 2; Group Normalization error minus
        BatchNorm error. Illustrates BatchNorm's small-batch failure.
```

```text
Figure: about two orders of magnitude better gradient predictiveness
Owner:  Santurkar et al. 2018 (Sec. 3.1, Figure 4)
Scope:  VGG on CIFAR-10; difference between BatchNorm and standard networks in
        how well the gradient predicts the loss along the step direction.
        Qualitative reading of the plot, not a single reported scalar.
```

Dataset denominator carried once for reuse: ImageNet ILSVRC-2012 classification
is 1000 classes, ~1,281,167 training images, 50,000 validation, 100,000 test
(Russakovsky et al. 2015, Table 2).

## Source assets

```text
Asset: Ioffe & Szegedy 2015, Figure 2. Single-crop validation accuracy versus
       number of training steps for Inception, BN-Baseline, BN-x5, BN-x30.
Shows: The speedup as a picture. The batch-normalized curves reach Inception's
       final accuracy far to the left of Inception's own curve, and the
       accompanying table gives the exact step counts.
Crop:  Keep all curves and the x-axis (training steps) with its scale. Keep the
       72.2% reference line if legible. Do not crop away BN-x30, which reaches
       the highest final accuracy.
```

```text
Asset: Santurkar et al. 2018, Figure 4. Loss landscape and gradient
       predictiveness for standard versus BatchNorm networks.
Shows: The positive claim. With BatchNorm the loss varies far less along the
       gradient direction and the gradient predicts the loss far better.
Crop:  Retain both panels (loss variation and gradient predictiveness) and the
       standard-vs-BatchNorm legend. Note in caption if a log scale is used.
```

```text
Asset: Santurkar et al. 2018, Figure 2. Training performance and layer-input
       distributions for standard, BatchNorm, and noisy-BatchNorm networks.
Shows: The refutation. Noisy-BatchNorm has visibly less stable distributions
       than even the no-BatchNorm network yet trains about as well.
Crop:  Keep the three-way comparison and the distribution strip; the point is
       lost if the noisy network is cropped out.
```

```text
Asset: Wu & He 2018, Figure 1. ImageNet error versus batch size for BatchNorm
       and Group Normalization.
Shows: BatchNorm error climbing as batch size falls while GN stays flat.
Crop:  Keep the full batch-size axis so the divergence at batch size 2 is
       visible.
```

```text
Asset: Russakovsky et al. 2015, Table 9. Human (A1, A2) versus GoogLeNet on the
       sampled test images.
Shows: That "better than human" rests on one annotator and a small sample.
Crop:  Keep the A1 row with its 1500-image count beside the 5.1% and 6.8%
       figures; a bare 5.1% without the sample size misleads.
```

## Discarded

```text
URL: https://arxiv.org/html/1409.0575v3 — 404; not a live resolving page. The
     source's own page is https://arxiv.org/abs/1409.0575.
URL: https://arxiv.org/abs/2009.12836 (Huang et al., normalization survey) —
     could not confirm from the abstract that it engages the ICS-vs-smoothing
     debate; dropped rather than cite an unread claim. d2l covers the debate and
     was verified.
URL: https://mitibm.mit.edu/research/blog/how-does-batch-normalization-help-optimization/
     — lab blog for the authors' own group; not an independent secondary. Not
     read to the claim level; d2l serves the secondary slot instead.
```

The record itself is held to `spec/slop.md`: every sentence is tied to this
document and these figures, and nothing here would survive being moved to
another article.

# Evidence: the-evidence/alexnet (researcher 01)

Every headline number in the commission checks out against the AlexNet paper
itself, read in full from the NeurIPS proceedings PDF: 15.3% vs 26.2% top-5 on
ILSVRC-2012, 37.5%/17.0% top-1/top-5 on ILSVRC-2010, 60 million parameters,
eight learned layers (five convolutional + three fully-connected), ~1.2 million
training images across 1000 classes, two GTX 580 3GB GPUs, five to six days,
~90 training epochs, and each of the six named techniques (ReLU, the two-GPU
split, local response normalization, overlapping pooling, data augmentation,
dropout) with the exact error-rate contribution the paper assigns it. The record
is strongest on what the paper reported and weakest — deliberately — on the
shorthand the commission wants qualified: the paper's own citations and the
independent record show GPU-trained deep CNNs were already winning vision
contests before AlexNet, that its famous ~11-point margin is an ensemble of
seven nets (two pre-trained on extra data) rather than the single model the
paper describes (18.2% top-5), and that most of its specific machinery was later
dropped even as its thesis — depth plus data plus compute — became the default.
The evidence does not undermine the commissioned angle; it confirms and sharpens
it. The one soft spot is that the "superseded" case rests on three separate
later primaries (BatchNorm, ViT, an ImageNet generalization audit) rather than a
single before/after document, so the writer should attribute each replacement to
its own owner and not overstate any as a clean, universal verdict.

## Sources

```
URL:         https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
Kind:        primary — the paper under examination; Krizhevsky, Sutskever, and
             Hinton own every architecture and result claim in it. (Own NeurIPS
             proceedings landing page; it links the full PDF, which I read.)
Establishes: What AlexNet is, did, and reported. A deep CNN with eight learned
             layers (five convolutional, three fully-connected), 60 million
             parameters and 650,000 neurons, ending in a 1000-way softmax.
             Trained on the ~1.2M-image, 1000-class ILSVRC subset. ILSVRC-2010:
             top-1/top-5 error 37.5%/17.0% (vs 47.1%/28.2% for the best 2010
             competition entry and 45.7%/25.7% for the best published prior
             result). ILSVRC-2012: winning top-5 test error 15.3% vs 26.2% for
             the second-best entry. Trained on two NVIDIA GTX 580 3GB GPUs over
             five to six days, ~90 epochs. The six techniques and their measured
             gains (see Numbers).
Paraphrase:  The authors trained a large deep CNN on the ImageNet ILSVRC data,
             won the 2012 challenge by roughly ten points on top-5 error, and
             attribute the result to network depth, a GPU implementation, and
             several explicit overfitting controls. They state depth is load-
             bearing: removing any single convolutional layer (each holding <1%
             of parameters) degrades performance.
Locators:    Abstract (p.1); Introduction and "eight learned layers" (p.2);
             §2 The Dataset (p.2); §3.1 ReLU (p.3); §3.2 Two GPUs (p.3-4);
             §3.3 LRN (p.4); §3.4 Overlapping Pooling (p.4); §3.5 Overall
             Architecture (p.4-5); §4.1 Data Augmentation, §4.2 Dropout (p.5-6);
             §5 Details of learning (p.6); §6 Results, Tables 1-2 (p.7);
             §7 Discussion (p.8).
Quote:       "We also entered a variant of this model in the ILSVRC-2012
             competition and achieved a winning top-5 test error rate of 15.3%,
             compared to 26.2% achieved by the second-best entry." (Abstract)
```

```
URL:         https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf
Kind:        primary — Deng, Dong, Socher, Li, Li, Fei-Fei (Princeton), the
             team that built ImageNet, describing the dataset firsthand. (Paper's
             own copy on the dataset's official site, image-net.org.)
Establishes: ImageNet's design and its scale at the 2009 CVPR publication: 12
             subtrees, 5247 synsets, 3.2 million cleanly annotated images, on
             average >600 images per synset, built on WordNet's ~80,000 noun
             synsets, labeled via Amazon Mechanical Turk with a reported 99.7%
             average labeling precision. The stated goal was ~50 million images
             over ~50K synsets "in the next two years."
Paraphrase:  In 2009 ImageNet was a 3.2M-image, 5247-category hierarchical
             database — an order of magnitude beyond the Caltech/PASCAL
             benchmarks it compares against (it claims 20x the categories and
             100x the images) but far smaller than the 15M-image/22K-category
             state AlexNet would cite three years later. The dataset AlexNet
             trained on did not exist at this paper's publication; ImageNet grew
             into it.
Locators:    Abstract; §1 Introduction; §2 "Scale" and "Accuracy"; §3
             Constructing ImageNet; §5.1 Completing ImageNet.
Quote:       "This paper offers a detailed analysis of ImageNet in its current
             state: 12 subtrees with 5247 synsets and 3.2 million images in
             total."
```

```
URL:         https://arxiv.org/abs/1409.0575
Kind:        primary — Russakovsky et al. (2015), the ILSVRC organizers,
             documenting the challenge they ran. (arXiv v3 abstract page; the
             paper also appears in IJCV.)
Establishes: The challenge's scale and the year-over-year record, including
             AlexNet's 2012 win and a human baseline. ILSVRC classification:
             1000 classes, ~1.2M training images (1,281,167 for 2012-14), 50,000
             validation, 100,000 test (2012-14). The 2012 "SuperVision" (AlexNet)
             entry is recorded at 16.4% top-5 on provided data / 15.3% with extra
             ImageNet Fall 2011 data. Winning classification error fell 4.2x from
             28.2% (2010) to 6.7% (2014). A trained expert human annotator (A1)
             reached 5.1% top-5 on a 1500-image sample vs GoogLeNet's 6.7-6.8%.
Paraphrase:  ILSVRC's organizers call 2012 "a turning point... when large-scale
             deep neural networks entered the scene," credit SuperVision's win to
             a 60M-parameter GPU-trained CNN with dropout, and show that by 2014
             nearly every top entry used CNNs. Their human-accuracy study — the
             source of the widely repeated "~5% human error" figure — rests on
             one trained annotator labeling 1500 images, not a population.
Locators:    §3.1 (1000 classes / ~1.2M, p.8); Table 2 (dataset scale by year,
             p.9); §5.1 "ILSVRC2012" turning-point passage; Table with
             SuperVision 16.4% and footnote on 15.3% extra-data entry; §6.1.1
             (4.2x / 28.2%->6.7%); §6.4.1 and Table 9 (human 5.1% vs GoogLeNet).
Quote:       "There has been a 4.2x reduction in image classification error
             (from 28.2% to 6.7%)... since the beginning of the challenge."
```

```
URL:         https://arxiv.org/abs/1202.2745
Kind:        primary — Ciresan, Meier, Schmidhuber (IDSIA, 2012, "Multi-column
             Deep Neural Networks for Image Classification"). Owns its own
             benchmark results firsthand. AlexNet cites this work ([4], and [5]).
Establishes: Deep GPU-trained CNNs were already setting records and beating
             humans on vision benchmarks before AlexNet. Their multi-column deep
             net (MCDNN) reached 0.23% error on MNIST ("the first time an
             artificial method comes close to the ~0.2% error rate of humans"),
             and 0.54% on the GTSRB traffic-sign benchmark where it was "the only
             artificial method to outperform humans, who produced twice as many
             errors." Also records on Chinese handwriting (3755 classes) and
             Latin letters. All GPU-trained.
Paraphrase:  A rival lab's GPU-trained deep convolutional nets won multiple
             vision competitions and achieved superhuman traffic-sign accuracy in
             2011-2012, before AlexNet's December 2012 NeurIPS win. This is the
             record's main complication to "AlexNet started deep learning": the
             method and the GPU-training recipe predate it; ImageNet's scale and
             the resulting industry attention are what made 2012 the inflection.
Locators:    Abstract; §3.1 MNIST (0.23%, "first... near-human"); §3.4 Traffic
             signs (GTSRB 0.54%, "outperform humans... twice as many errors");
             §3.2-3.3 Latin/Chinese characters.
Quote:       "Our MCDNN is the only artificial method to outperform humans, who
             produced twice as many errors."
```

```
URL:         https://arxiv.org/abs/1502.03167
Kind:        primary — Ioffe & Szegedy (2015), the Batch Normalization paper.
             Owns the claim firsthand that BN makes LRN unnecessary.
Establishes: One of AlexNet's specific techniques was explicitly retired. In
             building BN-Inception the authors removed local response
             normalization, and BN-Inception reached 4.9% top-5 validation error
             (4.82% test) on ImageNet, past the ~5.1% trained-human figure.
Paraphrase:  Batch normalization, published three years after AlexNet, both
             replaced LRN as the normalization layer of choice and accelerated
             training enough to make LRN redundant — a concrete instance of the
             commission's "LRN by batch normalization." (Independently, later
             ConvNets such as VGG also reported LRN gave no benefit; BN is the
             cleaner primary owner of the replacement claim.)
Locators:    Abstract (4.9% top-5); §4.2.1 "Remove Local Response Normalization";
             §4.2.2 / Table (BN-Inception 4.9% val, 4.82% test).
Quote:       "Remove Local Response Normalization. While Inception and other
             networks benefit from it, we found that with Batch Normalization it
             is not necessary."
```

```
URL:         https://arxiv.org/abs/2010.11929
Kind:        primary — Dosovitskiy et al. (2021), "An Image is Worth 16x16
             Words: Transformers for Image Recognition at Scale" (Vision
             Transformer). Owns its firsthand result challenging the CNN
             paradigm.
Establishes: Even AlexNet's core form — the convolutional network for vision —
             was later challenged. ViT, which "lack[s] some of the inductive
             biases inherent to CNNs, such as translation equivariance and
             locality," matches or beats state-of-the-art CNNs when pre-trained
             at large scale (best model 88.55% top-1 on ImageNet), while using
             substantially less compute to train. On mid-sized data alone it
             underperforms CNNs.
Paraphrase:  A non-convolutional architecture reached and passed CNN accuracy on
             ImageNet given enough pre-training data, supporting the commission's
             "ConvNets challenged for vision by the Vision Transformer." The same
             paper is the cleanest evidence that AlexNet's durable lesson was the
             thesis (scale of data and compute) and not the specific
             convolutional machinery: the authors summarize it as "large scale
             training trumps inductive bias."
Locators:    Abstract; §1 Introduction ("convolutional architectures remain
             dominant"; inductive-bias/"do not generalize well" passage; 88.55%
             ImageNet result); §3.1 "Inductive bias."
Quote:       "We find that large scale training trumps inductive bias."
```

```
URL:         https://arxiv.org/abs/1902.10811
Kind:        primary — Recht, Roelofs, Schmidt, Shankar (2019), "Do ImageNet
             Classifiers Generalize to ImageNet?" Owns firsthand the new-test-set
             experiment (ImageNetV2).
Establishes: An honest caveat on ImageNet-benchmark accuracy. Building a fresh
             ImageNet test set from the same distribution and re-scoring existing
             models, the authors find top-1 accuracy drops of 11%-14% on
             ImageNet (and 3%-15% on CIFAR-10). The drop is attributed to
             genuine difficulty generalizing to slightly harder images, not to
             test-set adaptivity.
Paraphrase:  ImageNet's reported numbers overstate real-world generalization by
             a measurable margin: the same classifiers lose 11-14 points of top-1
             accuracy on a freshly collected test set drawn the same way. This is
             the commission's "ImageNet's own later audits" caveat, and it
             tempers "superhuman on ImageNet" claims that post-date AlexNet.
Locators:    Abstract; §1 Introduction (11%-14% ImageNet drop); Figure 1
             (original vs new test-set accuracy).
Quote:       "we... find accuracy drops of 3% - 15% on CIFAR-10 and 11% - 14% on
             ImageNet."
```

```
URL:         https://computerhistory.org/blog/chm-releases-alexnet-source-code/
Kind:        secondary — Hansen Hsu, historian/sociologist of technology,
             curator of the Computer History Museum Software History Center
             (March 20, 2025). Reports on AlexNet from outside the authoring
             party; independent institutional retrospective.
Establishes: The mainstream framing the lesson is bringing to the present, and
             an independent statement of the "three preconditions." Hsu frames
             AlexNet as the network that "kick-started today's prevailing
             approach to AI," names the three converging ingredients (ImageNet-
             scale data, GPU/CUDA compute, deep neural nets — "each of these
             needed the other"), and acknowledges the precedents (Rosenblatt's
             Perceptron, backprop, LeNet-style CNNs, and DanNet 2011) while
             arguing they could not move computer vision without ImageNet's
             scale.
Paraphrase:  A credible non-participant retrospective that both carries the
             "started it all" shorthand and, read closely, supplies the material
             to qualify it: it lists the earlier neural nets and DanNet by name
             and locates AlexNet's significance in the convergence of three
             preconditions, not in an invention. Use for the present-day framing
             and the three-ingredients structure; do not cite it for any number
             (numbers come from the primaries above).
Locators:    Essay body: significance ("kick-started"); "before AlexNet, almost
             none of the leading computer vision papers used neural nets. After
             it, almost all of them would"; three-ingredients passage; prior-work
             passage (DanNet 2011, LeNet).
Quote:       "Each of these needed the other."
```

## Contradictions

The commission asks for what complicates "AlexNet started deep learning." The
record supplies several distinct complications, all sourced:

- **GPU-trained deep CNNs already won vision contests before AlexNet.** Ciresan,
  Meier, and Schmidhuber's multi-column deep nets (IDSIA) hit 0.23% error on
  MNIST and 0.54% on the GTSRB traffic-sign benchmark — beating humans, who made
  "twice as many errors" — all GPU-trained and published at CVPR 2012, months
  before AlexNet's December 2012 NeurIPS win. AlexNet cites this work ([4], [5]).
  So the architecture class (CNNs, back to LeCun's LeNet, cited as [15]-[17]),
  the GPU-training recipe, and even superhuman results on a vision task predate
  AlexNet. What 2012 changed was the benchmark (ImageNet's 1000-class,
  million-image scale) and the industry attention that followed — not the method.

- **The famous margin is an ensemble with extra data, not the single model the
  paper describes.** The headline 15.3% vs 26.2% top-5 is the seven-CNN entry,
  five trained on the provided data plus two pre-trained on the extra ImageNet
  Fall 2011 release. The single CNN the paper actually describes scored 18.2%
  top-5 (validation); five averaged CNNs scored 16.4% (the figure ILSVRC records
  for SuperVision on provided data). The ~10-point leap is real even for the
  single model (18.2% vs 26.2% is ~8 points), but the exact 15.3% number blends
  ensembling and extra training data. (AlexNet Table 2; Russakovsky Table and
  footnote.)

- **Most of AlexNet's specific techniques were later discarded.** Local response
  normalization was explicitly retired by the Batch Normalization paper ("with
  Batch Normalization it is not necessary"). The two-GPU split was a 3GB-memory
  workaround, not a design principle, and vanished as GPU memory grew. The
  convolutional form itself was later matched and passed by the Vision
  Transformer at scale ("large scale training trumps inductive bias"). What held
  is the thesis the paper states plainly — depth plus data plus compute — not its
  parts. This is the commission's through-line, and the primaries confirm it.

- **What the paper proved vs what gets attributed to it.** AlexNet proved a CNN
  could win ILSVRC-2012 by roughly ten points. It did not invent CNNs, backprop,
  GPUs, ReLU (Nair & Hinton 2010, cited [20]), or dropout (Hinton et al. 2012,
  cited [10], concurrent and by overlapping authors). The CHM retrospective, an
  independent source, frames the win as three preconditions converging and names
  DanNet and LeNet among the precedents — even while carrying the "kick-started"
  shorthand.

- **The "superhuman on ImageNet" narrative is softer than repeated.** The human
  baseline (~5.1% top-5) is one trained annotator on 1500 images (Russakovsky
  §6.4.1), and post-dates AlexNet (whose 15.3% was far above human level).
  Recht et al. later showed ImageNet classifiers lose 11-14 points of top-1
  accuracy on a freshly collected test set, i.e., benchmark accuracy overstates
  generalization. Neither undercuts AlexNet's 2012 result; both caution against
  reading the later ImageNet leaderboard as settled fact.

No source contradicts any of the commission's specific numeric claims about the
paper; the tension is entirely between what the paper reported and the shorthand
built on top of it.

## Numbers

```
Figure: 15.3% top-5 error (ILSVRC-2012, winning entry) vs 26.2% (second-best)
Owner:  AlexNet paper (Abstract; Table 2). Corroborated by Russakovsky (footnote).
Scope:  Top-5 test error on ILSVRC-2012 (1000 classes, ~100K test images). The
        15.3% entry is 7 CNNs, 2 of them pre-trained on ImageNet Fall 2011 data.
```
```
Figure: 18.2% top-5 (single CNN) / 16.4% (5 CNNs) — ILSVRC-2012
Owner:  AlexNet paper (Table 2; §6).
Scope:  Validation top-5; the single CNN is the model the paper describes on
        provided data. 16.4% is what ILSVRC records for SuperVision on provided
        data (Russakovsky).
```
```
Figure: 37.5% top-1 and 17.0% top-5 error (ILSVRC-2010)
Owner:  AlexNet paper (Abstract; Table 1).
Scope:  Test set, ILSVRC-2010 (1000 classes). Best 2010 competition entry:
        47.1%/28.2%; best prior published (SIFT+FVs): 45.7%/25.7%.
```
```
Figure: 60 million parameters; 650,000 neurons; 8 learned layers (5 conv + 3 FC)
Owner:  AlexNet paper (Abstract; §3.5; §4).
Scope:  The full network. Fully-connected layers are 4096 neurons each; final
        layer is 1000-way softmax. Each conv layer holds <1% of parameters.
```
```
Figure: ~1.2 million training images, 1000 classes (ILSVRC subset)
Owner:  AlexNet paper (§2); Russakovsky (§3.1, Table 2: 1,281,167 for 2012-14).
Scope:  ILSVRC classification training set; +50,000 validation, +150,000 test
        (2010) / 100,000 test (2012-14).
```
```
Figure: Full ImageNet: >15 million images, >22,000 categories
Owner:  AlexNet paper (§1/§2) describing ImageNet's then-current state.
Scope:  The whole ImageNet, not the ILSVRC subset. At the 2009 dataset paper it
        was only 3.2M images / 5247 categories (Deng et al.) — it grew into this.
```
```
Figure: Two NVIDIA GTX 580 3GB GPUs; five to six days; ~90 epochs
Owner:  AlexNet paper (§5; §3.2).
Scope:  Full training run. The two-GPU split was forced by the 3GB per-GPU
        memory limit.
```
```
Figure: Technique-by-technique error reductions (top-1 / top-5)
Owner:  AlexNet paper (§3.2-§3.4, §4.1).
Scope:  Two-GPU split: -1.7% / -1.2%. LRN: -1.4% / -1.2%. Overlapping pooling
        (s=2, z=3): -0.4% / -0.3%. PCA color augmentation: top-1 -1%+. Crop/
        reflection augmentation enlarges the training set by 2048x. Dropout
        (p=0.5, first two FC layers) roughly doubles iterations to converge.
        LRN hyperparameters: k=2, n=5, alpha=1e-4, beta=0.75.
```
```
Figure: ILSVRC winning top-5 error by year: 28.2% (2010) -> 15.3% (2012) -> 6.7% (2014)
Owner:  Russakovsky et al. (§6.1.1; Figure 9). 2012 figure cross-checked to AlexNet.
Scope:  Winning entries, provided-data track where applicable; a 4.2x reduction
        over the challenge's first five years. Good candidate for a chart.
```
```
Figure: Human top-5 error ~5.1% (trained annotator A1) vs GoogLeNet 6.7-6.8%
Owner:  Russakovsky et al. (§6.4.1; Table 9).
Scope:  One expert annotator, 1500-image sample. The basis of "human-level"
        ImageNet claims; post-dates AlexNet.
```
```
Figure: 11-14% top-1 accuracy drop on a fresh ImageNet test set
Owner:  Recht et al. (Abstract; §1).
Scope:  ImageNetV2 vs original ImageNet validation, existing models re-scored.
        A generalization caveat, not a correction to AlexNet's 2012 result.
```
```
Figure: BN-Inception 4.9% top-5 (val) / 4.82% (test); ViT best 88.55% top-1
Owner:  Ioffe & Szegedy (Abstract); Dosovitskiy et al. (Abstract).
Scope:  ImageNet, later systems that superseded AlexNet's LRN (BN) and its
        convolutional form (ViT, at large pre-training scale).
```

## Source assets

```
Asset: AlexNet Figure 2 — the network architecture diagram, drawn as two
       parallel horizontal bands (one per GPU) with the eight layers labeled.
Shows: The 5-conv + 3-FC structure and, concretely, the two-GPU split and the
       layers where the GPUs communicate. Makes "eight learned layers" and "the
       split was a memory workaround" visible at a glance.
Crop:  Keep both GPU bands and the layer labels; the split is the point. Do not
       crop to one band.
```
```
Asset: AlexNet Figure 3 — the 96 first-layer convolutional kernels (11x11x3),
       arranged in an 8x12 grid, top 48 from GPU 1, bottom 48 from GPU 2.
Shows: What the network learned in layer one: oriented edges, frequencies, and
       color blobs — the iconic image of "learned features." Also shows the
       GPU specialization (GPU 1 largely color-agnostic, GPU 2 color-specific).
Crop:  Retain the full grid; the variety across kernels is the lesson. A crop to
       a few kernels loses that.
```
```
Asset: AlexNet Figure 1 — ReLU vs tanh training-error curves on CIFAR-10 (solid
       = ReLU, dashed = tanh).
Shows: ReLU reaching 25% training error ~6x faster than tanh. A clean single
       image for "ReLU made training faster."
Crop:  Keep both curves and the axis labels (iterations vs training error rate).
```
```
Asset: AlexNet Tables 1 and 2 — the ILSVRC-2010 and ILSVRC-2012 result tables.
Shows: The numbers the lesson turns on, including the single-CNN vs ensemble
       rows that qualify the 15.3% headline. Better as prose or a rebuilt table
       than as a screenshot.
Crop:  n/a (rebuild as a clean table if used).
```
```
Asset: Russakovsky et al. Figure 9 / §6.1.1 series — winning error by year
       (28.2% 2010, 15.3% 2012, 6.7% 2014).
Shows: AlexNet's 2012 drop in the context of the whole challenge, and the
       continued fall after it. The natural chart for "one competition result"
       and for honesty about scale of progress. Data owned by a primary; the
       article's chart should be rebuilt from these figures per spec/charts.md.
Crop:  n/a (rebuild as chart-N.py).
```
```
Asset: Recht et al. Figure 1 — original vs new-test-set accuracy scatter, one
       point per model, with the gap below the diagonal.
Shows: The 11-14 point generalization drop across many models at once. Optional;
       only if the lesson develops the audit caveat.
Crop:  Keep the diagonal reference line and both axes.
```
```
Asset: Deng et al. Figure 2 — histogram of images per synset plus the subtree
       summary table.
Shows: ImageNet's 2009 scale (3.2M / 5247 synsets) — useful only if the lesson
       makes the "ImageNet grew into the ILSVRC set" point explicitly.
Crop:  Keep the table if used; the histogram alone is less legible small.
```

## Discarded

```
URL: https://www.kdnuggets.com/2021/02/dannet-triggers-deep-cnn-revolution.html
     — Schmidhuber's own DanNet retrospective. Partisan (a rival-lab principal
     staking a priority claim); the same pre-AlexNet facts are owned firsthand
     by Ciresan et al. 2012 (used instead as a primary).
```
```
URL: https://www.turingpost.com/p/cvhistory6 ; https://www.pinecone.io/learn/series/image-search/imagenet/ ;
     various Medium retrospectives — non-authoritative secondaries; the CHM/Hsu
     essay is a stronger, independently sourced retrospective and every number
     is anchored to a primary.
```
```
URL: https://www.semanticscholar.org/paper/.../abd1c342...  and researchgate/bibsonomy mirrors of the
     AlexNet paper — rejected as transport/aggregator pages; the paper's own
     NeurIPS proceedings page is recorded instead.
```

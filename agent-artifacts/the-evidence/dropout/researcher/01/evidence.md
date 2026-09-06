# Evidence: the-evidence/dropout (01)

The evidence answers every commissioned question from the documents that own the
claims. The 2014 JMLR paper and the 2012 arXiv tech report were read in full for
the mechanism, the co-adaptation and shared-weight-ensemble justification, and
the per-dataset error rates; every figure below was checked against the table or
sentence that prints it. The present-day shift rests on three later primaries:
the 2017 Transformer paper (dropout cut to 0.1), the 2022 PaLM report (no dropout
in pretraining), and a 2025 Stanford study finding that removing dropout improves
single-epoch language-model pretraining. The commissioned angle holds: the paper
frames dropout as a general technique, its own Section 7.4 shows the benefit
declines as data grows, and its ensemble justification is described in the paper
as an approximate averaging, not a proof. The record is thin in one place worth
naming plainly. The claim that dropout is "turned off in the largest models"
rests on the few labs that publish a dropout setting (PaLM states it, LLaMA omits
it, the 2025 study tests it); frontier proprietary models do not disclose theirs,
so that claim generalizes from a handful of disclosed reports, not a survey. The
divergence is also narrower than "dropout was abandoned": dropout at 0.1 is still
used in the original Transformer, in PaLM finetuning, and after batch-norm layers
in vision, and it still helped on the small-data benchmarks of 2012-2014. The
contradiction is recorded in full below.

## Sources

```text
URL:         https://jmlr.org/papers/v15/srivastava14a.html
Kind:        primary. It is the paper that owns every mechanism and result claim
             in the commission; the authors ran these experiments.
Establishes: What dropout is and does, the co-adaptation and shared-weight
             ensemble justification, the test-time weight-scaling rule, and the
             error rates on MNIST, SVHN, CIFAR-10/100, ImageNet, TIMIT and
             Reuters. Also the paper's own caveats: training cost and the effect
             of data-set size.
Paraphrase:  During training each unit is retained with a fixed probability p
             (a Bernoulli draw), independent of other units; a dropped unit is
             temporarily removed with all its incoming and outgoing connections.
             p can be set on a validation set, and 0.5 is close to optimal for a
             wide range of hidden layers, while input units want p closer to 1
             (they use 0.8). What is dropped is units, not weights. A net with n
             units is treated as a collection of 2^n thinned networks that share
             weights. At test time the paper uses one unthinned network whose
             outgoing weights are multiplied by p, so each unit's expected output
             matches training; this is stated as an approximate way of averaging
             the 2^n networks, not an exact one. The Bernoulli test-time scaling
             (W_test = pW) and the equivalent train-time 1/p scaling (what others
             call inverted dropout) are both given; the paper does not use the
             name "inverted dropout." The conclusion calls dropout a general
             technique not specific to any domain.
Locators:    Abstract; Sec. 1 (pp. 1930-1931, "2^n thinned networks", "approximate
             averaging", W_test = pW); Sec. 2 (pp. 1932-1933, co-adaptation and
             the sex-in-evolution and conspiracy analogies); Sec. 4 (p. 1933,
             Bernoulli(p), units dropped, W_test = pW); Sec. 5.1 (max-norm);
             Sec. 6.1-6.3 (Tables 2-8); Sec. 6.5 (Table 9); Sec. 7.4 (data-set
             size, p. 1945); Sec. 7.5 (Monte-Carlo vs weight scaling, p. 1946);
             Sec. 10 (p. 1951, the 1/p train-time variant); Sec. 11 (conclusion,
             "general technique", 2-3x training cost). PDF:
             https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf
Quote:       "By dropping a unit out, we mean temporarily removing it from the
             network, along with all its incoming and outgoing connections ...
             each unit is retained with a fixed probability p independent of
             other units."
             "If a unit is retained with probability p during training, the
             outgoing weights of that unit are multiplied by p at test time ...
             a very simple approximate averaging method works well in practice."
             "This suggests that dropout is a general technique and is not
             specific to any domain."
```

```text
URL:         https://arxiv.org/abs/1207.0580
Kind:        primary. The tech report where the idea and its first results were
             published; same authoring group.
Establishes: The origin of the method and its first benchmark numbers, reported
             as error counts and rates. Confirms p = 0.5 for hidden units and 20%
             input dropout, and that the method "sets new records for speech and
             object recognition."
Paraphrase:  Overfitting on a small training set is greatly reduced by randomly
             omitting half of the feature detectors on each training case, which
             stops feature detectors from co-adapting. On MNIST the best published
             standard feedforward result is 160 errors on the 10,000-image test
             set; 50% dropout with per-unit L2 constraints cuts this to about 130,
             and also dropping 20% of input pixels reaches about 110. A
             DBM-pretrained net finetuned with 50% dropout reaches a mean of 79
             errors, a record for methods without prior knowledge or an enhanced
             training set. On TIMIT the recognition rate improves from 22.7% to
             19.7% with dropout. On CIFAR-10 the best prior result without
             transformed data was 18.5%; they reach 16.6%, and 15.6% with dropout
             in the last hidden layer. On ILSVRC-2010 a single conv net with 50%
             dropout in one hidden layer reaches 42.4% error, against a prior
             state of the art of 45.7%. On Reuters, 50% dropout cuts error from
             31.05% to 29.62%.
Locators:    Abstract; pp. 1-2 (MNIST 160/130/110, mean 79); p. 3 (TIMIT
             22.7%/19.7%); pp. 3-4 (CIFAR-10 18.5%/16.6%/15.6%); p. 4 (ILSVRC-2010
             45.7%/48.6%/42.4%); p. 4 (Reuters 31.05%/29.62%); p. 4-5 (p = 0.5
             used throughout). Submitted 3 July 2012.
Quote:       "This 'overfitting' is greatly reduced by randomly omitting half of
             the feature detectors on each training case."
             "Random 'dropout' gives big improvements on many benchmark tasks and
             sets new records for speech and object recognition."
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary. "Attention Is All You Need" (Vaswani et al., 2017) owns the
             dropout setting of the original Transformer.
Establishes: The Transformer applies dropout, but at 0.1, not the paper's 0.5.
             Dropout is still reported as helpful here, which is the nuance the
             angle must respect.
Paraphrase:  Dropout is applied to the output of each sub-layer before it is added
             to the sub-layer input and normalized, and to the sums of the
             embeddings and positional encodings. The base model uses P_drop = 0.1.
             The large EN-DE model uses 0.3 (Table 3), while the large EN-FR model
             used 0.1 instead of 0.3. An ablation reports that dropout is very
             helpful in avoiding over-fitting.
Locators:    Sec. 5.4 "Regularization" (Residual Dropout, P_drop = 0.1); Sec. 6.2
             / Table 3 (base P_drop = 0.1, big 0.3; and 0.1 "instead of 0.3" for
             the EN-FR big model); Table 3 caption / row (E) discussion, "dropout
             is very helpful in avoiding over-fitting."
Quote:       "For the base model, we use a rate of P_drop = 0.1."
             "bigger models are better, and dropout is very helpful in avoiding
             over-fitting."
```

```text
URL:         https://arxiv.org/abs/2204.02311
Kind:        primary. The PaLM report (Chowdhery et al., 2022) owns the training
             configuration of a 540-billion-parameter model.
Establishes: A frontier-scale language model trained with no dropout during
             pretraining. This is the clearest disclosed instance of dropout
             being turned off at scale, and it anchors the shift.
Paraphrase:  PaLM is a 540-billion-parameter, densely activated, autoregressive
             Transformer trained on 780 billion tokens. In the training-setup
             list, the dropout entry states the model was trained without dropout,
             and that dropout of 0.1 is used for finetuning in most cases. For
             scale contrast, the paper's own regularization at pretraining is a
             dynamic weight decay, not dropout.
Locators:    Abstract and Sec. 1 (p. 3, "540 billion parameter ... 780 billion
             tokens"); Sec. 2 "Training setup" bullet list (the "Dropout" bullet:
             trained without dropout, 0.1 for finetuning; adjacent "Optimizer"
             bullet gives the dynamic weight decay).
Quote:       "The model was trained without dropout, although dropout of 0.1 is
             used for finetuning in most cases."
```

```text
URL:         https://arxiv.org/abs/2505.24788
Kind:        primary. "Drop Dropout on Single-Epoch Language Model Pretraining"
             (Liu, Bauer, Manning, Stanford, 2025) owns its own pretraining
             experiments, which directly test dropout's role in modern LM
             pretraining.
Establishes: An empirical primary finding that removing dropout improves
             downstream performance in single-epoch LM pretraining, and a
             compact history of the dropout rate falling over a decade. It also
             gives a figure to check against Vaswani (see Contradictions).
Paraphrase:  Single-epoch pretraining, common to modern LLMs, produces minimal
             overfitting, so dropout is not used for large LLMs. Testing masked
             (BERT) and autoregressive (Pythia 160M and 1.4B) models with varying
             dropout, the authors find downstream performance on language
             modeling, BLiMP (morpho-syntax), SQuAD (question answering) and MNLI
             (natural-language inference) improves when dropout is not applied
             during pretraining. Their history: dropout began at p = 0.5 (2012);
             they state the original Transformer applied p = 0.3 at each layer;
             BERT, GPT-2 and T5 used p = 0.1; and LLaMA reports no dropout use.
Locators:    Abstract; Sec. 1 introduction (the p = 0.5 -> 0.3 -> 0.1 -> none
             history, and the LLaMA "do not report any dropout use" claim);
             Sec. 5 "Conclusion and Discussion" (models pretrained without dropout
             score consistently more favorably). Submitted 30 May 2025.
Quote:       "downstream performance in language modeling, morpho-syntax (BLiMP),
             question answering (SQuAD), and natural-language inference (MNLI)
             improves when dropout is not applied during pretraining."
```

```text
URL:         https://arxiv.org/abs/1801.05134
Kind:        primary. "Understanding the Disharmony between Dropout and Batch
             Normalization by Variance Shift" (Li, Chen, Hu, Yang, 2018) owns the
             analysis and the experiments it reports.
Establishes: The documented tension between dropout and batch normalization: a
             network can perform worse when the two are combined, with a stated
             mechanism ("variance shift"), and quantified cases. Also that the
             batch-norm paper itself argued BN reduces the need for dropout.
Paraphrase:  Dropout and batch normalization often perform worse when combined.
             Dropout shifts the variance of a unit between train and test, while
             BN carries the training-time moving variance into test, so the two
             statistics disagree and inference becomes unstable, especially when
             dropout sits before BN. On a DenseNet on CIFAR-100, putting dropout
             at rate 0.5 in each bottleneck drops test accuracy from 77.42% (no
             dropout) to 68.55%. The authors note that Ioffe and Szegedy already
             observed BN eliminates the need for dropout in some cases. Two fixes
             work: apply dropout only after all BN layers, or use a
             lower-variance ("Uout") form; at a small rate (0.1-0.2) after BN,
             consistent small gains return, including on ImageNet.
Locators:    Abstract; Fig. 1 (DenseNet CIFAR-100 77.42% vs 68.55%); Sec. 1
             (Ioffe and Szegedy "BN eliminates the need for Dropout"); Sec. 5 and
             Table 4 (dropout after all BN layers, C100 DenseNet 22.58% -> 21.86%
             at rate 0.1); Table 5 (ImageNet, ResNet-200 top-1 21.70% -> 21.48%
             at rate 0.2 after all BN).
Quote:       "a network even performs worse and unsatisfactorily when it is
             equipped with BN and Dropout simultaneously."
```

```text
URL:         https://www.semanticscholar.org/paper/34f25a8704614163c4095b3ee2fc969b60de4698
Kind:        secondary. A citation index reporting on the paper from outside the
             authoring party; it owns the count, not the paper.
Establishes: The scale of the paper's influence, to support "one of the most
             cited regularization methods." A verifiable count, not a claim by
             the authors.
Paraphrase:  Semantic Scholar records the 2014 JMLR dropout paper with a citation
             count of 44,200, read on 2026-09-06. The count is a live figure and
             will drift upward; treat it as a floor and an order of magnitude, not
             a fixed number.
Locators:    Semantic Scholar paper page for "Dropout: a simple way to prevent
             neural networks from overfitting" (paperId 34f25a87...), citationCount
             field, retrieved 2026-09-06.
Quote:       (none; the figure is the evidence)
```

## Contradictions

- Against the strong reading of "dropout is turned off now": dropout is not gone.
  The original Transformer keeps it at 0.1 and calls it "very helpful"
  (1706.03762, Sec. 5.4 and Table 3 discussion); PaLM uses 0.1 for finetuning
  even though pretraining uses none (2204.02311); the disharmony paper shows a
  small dropout after batch-norm still gives consistent small gains in vision
  (1801.05134, Tables 4-5). The accurate claim is that dropout's role narrowed to
  specific regimes (large-data single-epoch pretraining turns it off), not that
  the technique was abandoned.

- Internal figure disagreement on the Transformer's dropout. The 2025 Stanford
  study states the original Transformer "applies dropout p = 0.3 at each of its
  network layers" (2505.24788, Sec. 1). The Transformer paper itself sets
  P_drop = 0.1 for the base model and reserves 0.3 for the large EN-DE model
  (1706.03762, Sec. 5.4, Table 3). Cite Vaswani for the exact rate; the 2025
  paper's 0.3 is a secondary retelling and is imprecise here.

- MNIST reported two ways. The 2012 report gives error counts out of 10,000
  (160 -> ~130 -> ~110; DBM-pretrained mean 79); the 2014 paper gives percentages
  (standard 1.60%, dropout logistic 1.35%, ReLU 1.25%, ReLU + max-norm 1.06%,
  best 0.95%; DBM + dropout finetuning 0.79%). 160 errors is 1.60%, so the two
  agree at the baseline; the small gaps below it are different architectures, not
  a conflict. Attribute counts to the 2012 report and percentages to the 2014
  paper.

- The paper's own limit on its ensemble justification. Section 7.5 shows the
  weight-scaling test-time rule only approximates the true model average: a
  Monte-Carlo average over sampled thinned nets needs about k = 50 samples to
  match it, and is only slightly better beyond that (JMLR 2014, Sec. 7.5,
  p. 1946). So the "average of 2^n networks" is an intuition backed by an
  approximation that holds well empirically, not a theorem for nonlinear nets.
  This supports rather than breaks the angle, and belongs here because it
  qualifies the paper's headline interpretation.

- GPT-3 is not clean positive evidence. The GPT-3 paper states weight decay of
  0.1 "to provide a small amount of regularization" and does not state a dropout
  rate; that is an absence, not a disclosed zero. PaLM and LLaMA carry the
  turned-off claim; GPT-3 should not be cited as "dropout = 0."

## Numbers

```text
Figure: MNIST test error, standard feedforward net 1.60%
Owner:  JMLR 2014, Table 2 (Simard et al. row)
Scope:  10,000-image test set, permutation-invariant setting, no dropout/pretrain
```
```text
Figure: MNIST test error with dropout: 1.35% (logistic, 3x1024), 1.25% (ReLU),
        1.06% (ReLU + max-norm, 3x1024), 0.95% (2x8192, >65M params)
Owner:  JMLR 2014, Table 2 and Sec. 6.1.1
Scope:  10,000-image test set; p = 0.5 hidden, 0.8 input; 60,000 training images
```
```text
Figure: MNIST DBM + dropout finetuning 0.79%
Owner:  JMLR 2014, Table 2 ("best performance ever reported" for the setting)
Scope:  Permutation-invariant MNIST, 10,000-image test set
```
```text
Figure: MNIST as error counts: best standard 160; 50% dropout ~130; +input
        dropout ~110; DBM-pretrained + dropout mean 79
Owner:  arXiv 1207.0580 (2012), pp. 1-2
Scope:  Out of 10,000 test images
```
```text
Figure: SVHN error 3.95% (best conv net, no dropout) -> 3.02% (dropout in FC
        layers) -> 2.55% (dropout in all layers)
Owner:  JMLR 2014, Table 3 and Sec. 6.1.2
Scope:  SVHN test set; per-layer p = (0.9,0.75,0.75,0.5,0.5,0.5)
```
```text
Figure: CIFAR-10 error 14.98% (Snoek et al. best prior) -> 14.32% (dropout FC)
        -> 12.61% (dropout all layers); CIFAR-100 43.48% -> 37.20%
Owner:  JMLR 2014, Table 4 and Sec. 6.1.3
Scope:  CIFAR-10/100 test sets, no data augmentation beyond input dropout
```
```text
Figure: ImageNet ILSVRC-2010: Conv Net + dropout top-1 37.5%, top-5 17.0%
        (best classical prior top-5 25.7-28.2%)
Owner:  JMLR 2014, Table 5
Scope:  ILSVRC-2010 test set (the AlexNet result, Krizhevsky et al. 2012)
```
```text
Figure: ImageNet ILSVRC-2012: single conv net + dropout top-1 40.7% / top-5
        18.2% (val); avg of 5 nets top-5 16.4%; won the competition, ~16% vs
        ~26% top-5 for best classical methods
Owner:  JMLR 2014, Table 6 and Sec. 6.1.4
Scope:  ILSVRC-2012 validation/test set
```
```text
Figure: TIMIT phone error rate: 6-layer NN 23.4% -> dropout 21.8%; 4-layer
        DBN-pretrained 22.7% -> +dropout 19.7%; 8-layer 20.7% -> +dropout 19.7%
Owner:  JMLR 2014, Table 7 and Sec. 6.2
Scope:  TIMIT core test set, phone error rate
```
```text
Figure: Reuters-RCV1 error 31.05% (no dropout) -> 29.62% (with dropout);
        "improvement was much smaller" than vision/speech
Owner:  JMLR 2014, Sec. 6.3 (also 1207.0580 p. 4)
Scope:  50-topic classification, subset of Reuters-RCV1
```
```text
Figure: Regularizer comparison on MNIST (784-1024-1024-2048-10, ReLU): L2 1.62,
        L2+L1 1.60, L2+KL-sparsity 1.55, Max-norm 1.35, Dropout+L2 1.25,
        Dropout+Max-norm 1.05 (test classification error %)
Owner:  JMLR 2014, Table 9
Scope:  MNIST test set, same architecture across rows
```
```text
Figure: Retention probabilities p = 0.5 for hidden units, p = 0.8 for input units
Owner:  JMLR 2014, Sec. 6.1.1 (also 1207.0580, p = 0.5 throughout)
Scope:  The paper's default across most experiments
```
```text
Figure: Dropout increases training time 2-3x; gains from dropout rise then
        decline with data-set size, and give no improvement at 100-500 examples
Owner:  JMLR 2014, Sec. 11 (2-3x) and Sec. 7.4 (data-set-size "sweet spot")
Scope:  MNIST subsets of size 100, 500, 1K, 5K, 10K, 50K (Sec. 7.4)
```
```text
Figure: Weight-scaling approximates the true model average; a Monte-Carlo
        average over sampled thinned nets matches it around k = 50 samples
Owner:  JMLR 2014, Sec. 7.5 (Figure 11)
Scope:  MNIST test set
```
```text
Figure: Transformer dropout P_drop = 0.1 (base), 0.3 (big EN-DE)
Owner:  arXiv 1706.03762, Sec. 5.4 and Table 3
Scope:  WMT machine-translation training
```
```text
Figure: PaLM 540 billion parameters, 780 billion tokens, no dropout in
        pretraining, 0.1 for finetuning
Owner:  arXiv 2204.02311, Sec. 1 and Sec. 2 training setup
Scope:  PaLM pretraining and finetuning
```
```text
Figure: Dropout + batch-norm harm: DenseNet on CIFAR-100 test accuracy 77.42%
        (no dropout) vs 68.55% (dropout 0.5 in each bottleneck); small dropout
        (0.1-0.2) after all BN restores consistent small gains
Owner:  arXiv 1801.05134, Fig. 1 and Tables 4-5
Scope:  DenseNet/ResNet/ResNeXt/WRN on CIFAR-10/100 and ImageNet
```
```text
Figure: 2014 JMLR dropout paper citation count 44,200
Owner:  Semantic Scholar (secondary index), retrieved 2026-09-06
Scope:  Cross-venue citations; a live, rising figure, treat as a floor
```

## Source assets

```text
Asset: JMLR 2014, Figure 2 (p. 1930): a single unit "present with probability p"
       at training time vs "always present" with weights multiplied by p at test
       time.
Shows: The whole train/test asymmetry in one diagram: what is dropped and how the
       weights are scaled back at test time.
Crop:  Keep both panels (training and test) and the "w" / "pw" labels; the
       comparison is the point. Omit surrounding body text.
```
```text
Asset: JMLR 2014, Figure 1 (p. 1930): a standard 2-hidden-layer net beside a
       "thinned" net with crossed-out (dropped) units.
Shows: That dropout removes whole units and their connections, producing a
       sub-network, which is the mechanism in a picture.
Crop:  Keep both networks side by side and the crossed units; the left/right
       contrast carries it.
```
```text
Asset: JMLR 2014, Figure 10 (p. 1945): test error with and without dropout as
       MNIST training-set size grows from 100 to 50,000.
Shows: The angle's core fact from the paper itself: no gain on tiny data, a rise,
       then a decline as data grows. The two curves converge at small data.
Crop:  Keep both curves, the log x-axis (data-set size) and its labels; note the
       log scale in the caption per spec/charts.md.
```
```text
Asset: JMLR 2014, Table 9 (p. 1942): regularizer comparison on one MNIST
       architecture.
Shows: Dropout vs L2, L1, KL-sparsity and max-norm on equal footing, and that
       dropout + max-norm was lowest.
Crop:  Keep all rows and the error column; the ranking is the argument.
```
```text
Asset: arXiv 1801.05134, Figure 1: the variance-shift schematic plus the
       DenseNet CIFAR-100 curve where the two variances diverge across BN layers.
Shows: Why dropout and batch-norm fight, tied to the 77.42% vs 68.55% accuracy
       gap.
Crop:  The schematic reads on its own; if used, keep the train/test variance
       labels. The plotted curve needs its axis labels to be honest.
```

## Discarded

```text
URL: https://arxiv.org/abs/2005.14165 (GPT-3): read for a dropout setting;
     states weight decay 0.1 for regularization but no dropout rate. An absence,
     not a disclosed zero, so not cited as turned-off evidence (noted in
     Contradictions instead).
URL: https://towardsdatascience.com/... and sh-tsang.medium.com/... (GPT-3
     explainers): secondary retellings of GPT-3 hyperparameters; unnecessary once
     the primary was read, and blog reliability is not needed here.
URL: https://jmlr.org/papers/volume24/22-1144/22-1144.pdf (PaLM JMLR version):
     same content as the arXiv report already cited; recorded the arXiv page as
     the document's home to avoid a duplicate source.
```

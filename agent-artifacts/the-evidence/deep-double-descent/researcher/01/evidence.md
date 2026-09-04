# Evidence: the-evidence/deep-double-descent (01)

The evidence supports the commission's core claims firmly. Both canonical papers were read: Nakkiran et al. 2019 in full from the journal version (all figures and the experimental-setup section), and Belkin et al. 2019 from its full abstract plus a full-text extraction. The phenomenon is real, reproducible, and demonstrated across architectures, datasets, and optimizers; the interpolation threshold and the reasons the error peaks there are stated firsthand; the three variants (model-wise, epoch-wise, sample-wise) are defined by the paper that owns them; the role of label noise is documented precisely, including the clean-data cases where a peak still appears and the cases where it flattens to a plateau. The over-general moral ("more parameters or more data always help") is contradicted by the primary papers themselves: Nakkiran et al. exhibit a regime where 4.5x more data raises test loss and a critical region where a bigger model is worse. Two later primaries supply the correction the commission asks for: Nakkiran, Venkat, Kakade & Ma 2021 show optimally tuned ridge regularization can remove or mitigate the peak, and Curth, Jeffares & van der Schaar 2023 argue the second descent in classical (non-deep) models is an artifact of how parameters are counted. The record is thin in two places, both flagged below: exact per-point error values are read off published figures rather than tables (the authors' released raw data holds the exact series), and the classical bias-variance statement's originating paper (Geman et al. 1992) could not be fetched in full, so the classical view here is anchored on the two primaries that quote it. Nothing found undermines the commission's angle; one honest qualification is that the second descent past the peak is a genuine, beneficial effect, so the article should not over-correct into "size never helps."

## Sources

```text
URL:         https://arxiv.org/abs/1912.02292
Kind:        primary. Nakkiran, Kaplun, Bansal, Yang, Barak, Sutskever own the deep-learning double-descent
             experiments and the effective-model-complexity framing. Read in full via the journal version
             (J. Stat. Mech. 2021, DOI 10.1088/1742-5468/ac3a74), which the authors state is an updated
             version of the ICLR 2020 paper (OpenReview forum id B1g5sA4twr). arXiv abs page is recorded as
             the canonical stable address; it resolves.
Establishes: (firsthand) Model-wise, epoch-wise, and sample-wise double descent on modern nets; the EMC
             definition and the under/critically/over-parameterized regimes; the interpolation-threshold peak;
             the role of label noise; the "more data hurts" regime.
Paraphrase:  Title "Deep double descent: where bigger models and more data hurt." Affiliations: authors 1-5
             (Nakkiran, Kaplun, Bansal, Yang, Barak) at Harvard University; Sutskever at OpenAI; footnote 3
             states the work was performed in part while Nakkiran was interning at OpenAI with Sutskever; the
             authors thank Mikhail Belkin and Christopher Olah. Three architecture families were used:
             ResNet18s parameterized by a width k with convolutional layer widths [k, 2k, 4k, 8k] (standard
             ResNet18 is k=64); five-layer "standard CNNs" with four conv layers of widths [k, 2k, 4k, 8k]
             plus a fully-connected layer (the k=64 CNN reaches >90% test accuracy on CIFAR-10 with data
             augmentation); and the six-layer encoder-decoder Transformer of Vaswani et al. 2017, scaled by
             embedding dimension d_model with feed-forward width d_ff = 4*d_model. Datasets: CIFAR-10,
             CIFAR-100, IWSLT'14 German-to-English and WMT'14 English-to-French translation. Optimizers: Adam
             at learning rate 0.0001 for 4K epochs, and SGD with learning rate proportional to 1/sqrt(T) for
             500K gradient steps; Transformers trained for 80K gradient steps with 10% label smoothing and no
             dropout. Label noise of probability p means each training example keeps its correct label with
             probability (1-p) and otherwise gets a uniformly random incorrect label, sampled once and held
             fixed across epochs. Effective Model Complexity (EMC, Definition 2.1) of a training procedure T
             is the largest sample count n on which T reaches on average approximately zero training error;
             the paper heuristically uses the threshold epsilon = 0.1. Model-wise: test error of models of
             increasing size trained to completion peaks at the interpolation threshold (where EMC ~= n) and
             then falls. Epoch-wise: for a fixed large model, test error over training time first falls, rises
             near the critical regime, then falls again ("training longer can correct overfitting"); medium
             models follow a classical U (early stopping helps); small models are monotone. Sample-wise: for a
             fixed model and procedure, increasing n shifts the peak rightward, so in a band of model sizes
             more data does not help and can hurt. On label noise: "We observe all forms of double descent
             most strongly in settings with label noise," but a test-error peak also appears with no added
             noise for ResNets on CIFAR-100 (Fig 4a), CNNs on CIFAR-100 (Fig 7 and Fig 20), and Transformers
             on IWSLT'14 (Fig 8), and for adversarial training; in the noiseless case the critical region
             "often manifesting as a 'plateau' in the test error ... which develops into a peak with added
             label noise." Adding label noise, using data augmentation, and increasing sample count all raise
             the interpolation threshold and shift the peak toward larger models. Mechanistic intuition
             (Section 5): at the threshold there is effectively one model that fits the training set and it is
             very sensitive to noise or model mis-specification; past the threshold many interpolating models
             exist and SGD can find one that absorbs the noise while still generalizing; the effect "occurs
             whenever there is model mis-specification between the structure of the true distribution and the
             model family." Raw experimental data released at
             https://gitlab.com/harvard-machine-learning/double-descent/tree/master.
Locators:    Abstract and Introduction (pp. 3-4); Fig 1 (ResNet18 CIFAR-10, 15% label noise); Fig 2 (heat map
             of test error over width and epochs); Fig 3 (Transformer IWSLT'14, 4k vs 18k samples); Fig 4
             (model-wise, ResNets on CIFAR-100 and CIFAR-10 across 0/5/10/15/20% label noise); Fig 5 (CNNs
             CIFAR-10, with/without data augmentation); Fig 6 (SGD vs Adam, clean CIFAR-10); Fig 7 (clean CNN
             CIFAR-100, real peak); Definition 2.1 and Hypothesis 1 (Section 2, p. 5); Experimental setup and
             label-noise definition (Section 4, p. 8); Remarks on label noise (p. 6, end of Section 2);
             Sample-wise (Section 7, p. 11). Page numbers are the J. Stat. Mech. version.
Quote:       "we show that a variety of modern deep learning tasks exhibit a 'double-descent' phenomenon
             where, as we increase model size, performance first gets worse and then gets better."
             "our notion of model complexity allows us to identify certain regimes where increasing (even
             quadrupling) the number of train samples actually hurts test performance."
             "For example, figure 3 demonstrates cases in which increasing the number of samples by a factor
             of 4.5 results in worse test performance."
             "We observe all forms of double descent most strongly in settings with label noise ... often
             manifesting as a 'plateau' in the test error in the noiseless case which develops into a peak
             with added label noise."
```

```text
URL:         https://arxiv.org/abs/1812.11118
Kind:        primary. Belkin, Hsu, Ma, Mandal own the "double descent" curve and its name and the first
             general demonstration. Read from the full abstract (arXiv) and a full-text extraction (ar5iv).
             Published in PNAS 2019, DOI 10.1073/pnas.1903070116. arXiv abs page resolves; the PNAS page
             returned HTTP 403 to the automated fetch (gated, not dead).
Establishes: (firsthand) The double-descent risk curve as a general phenomenon; the term "double descent";
             the interpolation threshold at N = n; demonstrations on random Fourier features, neural nets,
             random forests, and boosting; the claim that capacity beyond interpolation lowers risk below the
             classical U's minimum.
Paraphrase:  Title "Reconciling modern machine learning practice and the bias-variance trade-off."
             Affiliations: Mikhail Belkin (The Ohio State University), Daniel Hsu (Columbia University),
             Siyuan Ma (The Ohio State University), Soumik Mandal (The Ohio State University). Submitted
             2018-12-28 (v1), revised 2019-09-10 (v2). The paper names the tension: classical bias-variance
             theory says a model should balance under- and over-fitting, so a model with zero training error
             is expected to generalize poorly; yet interpolating neural nets generalize well. It proposes a
             single "double descent" curve that extends the classical U-curve past the interpolation
             threshold: below the threshold the classical U holds; at the threshold (the smallest capacity
             that fits the data exactly) risk peaks; above it, added capacity lowers risk. Key experiment:
             random Fourier features on MNIST with n = 10^4 training points and 10 classes, sweeping the
             feature count N, with the peak risk falling exactly at N = n (the interpolation threshold), where
             the interpolating predictor has essentially no predictive ability, and with risk beyond the
             threshold dropping below the best under-parameterized model. Also demonstrated: fully connected
             networks on MNIST (n = 4x10^3, input dimension d = 784, K = 10 classes, one hidden layer of H
             units, parameter count (d+1)H + (H+1)K, threshold at n*K), random forests, and L2-boosting.
             Belkin et al. supply the framing and simpler demonstrations; they do not run the large modern-net
             experiments (that is Nakkiran et al.).
Locators:    Abstract; Fig 1 (classical U vs double-descent schematic); Fig 2 (RFF on MNIST); Fig 4 (fully
             connected net on MNIST). Figure numbering per the ar5iv full text.
Quote:       "This 'double descent' curve subsumes the textbook U-shaped bias-variance trade-off curve by
             showing how increasing model capacity beyond the point of interpolation results in improved
             performance."
             "The textbook corollary of this curve is that 'a model with zero training error is overfit to the
             training data and will typically generalize poorly.'"
```

```text
URL:         https://arxiv.org/abs/2003.01897
Kind:        primary. Nakkiran, Venkat, Kakade, Ma own the result that optimal regularization can remove or
             mitigate the peak. This is the commission's requested correction on regularization. Read from the
             arXiv abstract page, which resolves. Published at ICLR 2021.
Establishes: (firsthand) That the double-descent peak is not inevitable: it depends on regularization.
Paraphrase:  Title "Optimal Regularization Can Mitigate Double Descent." Submitted 2020-03-04 (v1), revised
             2021-04-29 (v2). They prove that for certain linear-regression models with an isotropic data
             distribution, optimally tuned L2 (ridge) regularization makes test performance monotone in both
             sample size and model size, so the non-monotone peak disappears. Empirically they show optimally
             tuned L2 regularization can mitigate double descent for more general models including neural
             networks. The finding is a theorem for the isotropic linear case and an empirical mitigation for
             nets, not a proof that the peak vanishes for all models.
Locators:    Abstract.
Quote:       "we prove that for certain linear regression models with isotropic data distribution,
             optimally-tuned l2 regularization achieves monotonic test performance as we grow either the
             sample size or the model size. We also demonstrate empirically that optimally-tuned l2
             regularization can mitigate double descent for more general models, including neural networks."
```

```text
URL:         https://arxiv.org/abs/2310.18988
Kind:        primary. Curth, Jeffares, van der Schaar own the argument that double descent in classical models
             is an artifact of parameter counting. This is the commission's requested qualification on how
             universal the effect is. Read from the arXiv abstract page, which resolves. NeurIPS 2023 (oral).
Establishes: (firsthand) That in classical (non-deep) methods, the apparent second descent depends on the
             choice of x-axis; under a proper effective-parameter measure the curve folds back to a U.
Paraphrase:  Title "A U-turn on Double Descent: Rethinking Parameter Counting in Statistical Learning."
             Submitted 2023-10-29. Double descent was shown to emerge beyond deep nets, in linear regression,
             trees, and boosting. The authors challenge the claim that these cases genuinely extend the
             classical U-shaped complexity-error curve. They argue these methods have multiple implicit
             complexity axes along which the raw parameter count grows, and the second descent appears exactly
             where the transition between axes occurs. Reinterpreting the methods as smoothers and using a
             generalized effective-parameter measure, the apparent double-descent curves fold back into
             traditional (convex, U-like) shapes. The paper's scope is classical statistical methods; it does
             not claim the deep-net model-wise or epoch-wise phenomenon is itself an artifact.
Locators:    Abstract.
Quote:       "challenge the claim that observed cases of double descent truly extend the limits of a
             traditional U-shaped complexity-generalization curve therein."
```

```text
URL:         https://arxiv.org/abs/2109.02355
Kind:        secondary. Dar, Muthukumar & Baraniuk review the theory of overparameterized learning from
             outside the two canonical papers; a survey reports and organizes others' findings rather than
             owning an experiment. Read from the arXiv abstract page, which resolves.
Establishes: (repeats, does not prove) How the field reframed the classical bias-variance tradeoff after
             double descent, and the common framing that overparameterized models "often improve over the best
             underparameterized model." Useful for the commission's "how the result is invoked today."
Paraphrase:  Title "A Farewell to the Bias-Variance Tradeoff? An Overview of the Theory of Overparameterized
             Machine Learning." Submitted 2021-09-06. States that interpolating noisy data is traditionally
             associated with harmful overfitting, yet a wide range of interpolating models from linear models
             to deep nets generalize well, and that the double-descent phenomenon revealed highly
             overparameterized models often beat the best underparameterized model. Presents itself as a
             "succinct overview" of an emerging theory, i.e. a survey.
Locators:    Abstract.
Quote:       "the recently discovered double descent phenomenon has revealed that highly overparameterized
             models often improve over the best underparameterized model in test performance."
```

```text
URL:         https://en.wikipedia.org/wiki/Double_descent
Kind:        secondary. A tertiary reference summary written outside the authoring parties. Read in full.
Establishes: (repeats) The popular framing of double descent and the practitioner belief it is tied to, that
             "modern machine learning techniques tend to perform better with larger models"; useful only as
             evidence of how the result is commonly stated, not of any claim's truth.
Paraphrase:  Describes the non-monotone test-error curve (fall, rise near the interpolation threshold where
             parameters ~ training points, fall again), attributes the term to Belkin et al. 2019 and the
             deep-learning demonstration to Nakkiran et al., notes earlier observations (Vallet et al. 1989),
             and reports the 2010s practitioner observation that larger models tend to do better. It cites
             Belkin et al. 2019, Nakkiran et al., Advani/Saxe/Sompolinsky 2020, and Rocks et al. 2022.
Locators:    Article body, "Double descent" (accessed 2026-09-04).
Quote:       (none load-bearing)
```

## Contradictions

- The commission's angle holds and is reinforced by the primaries, not contradicted. The strong moral now attached to double descent ("more parameters or more data always help") is contradicted directly by the paper that people cite for it. Nakkiran et al. title their paper "where bigger models and more data hurt," show a critical region where a wider model is worse than a narrower one, and show (Fig 3) a Transformer where increasing the training set by 4.5x (from 4k to 18k sentence pairs) raises test loss across a band of model sizes. So the writer can hold the two readings apart using the primary alone.

- Do the papers say the second descent is real and beneficial? Yes, and this is the honest counter-pressure on any over-correction. Belkin et al. and Nakkiran et al. both show that once capacity is comfortably past the interpolation threshold, more capacity keeps lowering test error, often below the classical sweet spot. The danger zone is the critical region around the threshold and the sample-wise regime, not the over-parameterized regime. The lesson should not swing to "bigger never helps."

- Is the peak universal? Two qualifications. (1) Regularization: Nakkiran, Venkat, Kakade & Ma 2021 prove optimally tuned ridge regression is monotone for isotropic linear models and show tuned L2 mitigates the peak for neural nets, so the peak is a property of under-regularized training, not a law. (2) Parameter counting: Curth, Jeffares & van der Schaar 2023 argue the second descent in linear regression, trees, and boosting is an artifact of the raw-parameter x-axis and folds back to a U under a proper effective-parameter count. Their scope is classical methods; they do not claim the deep-net model-wise or epoch-wise curves are artifacts. Nakkiran et al. themselves show a case (Fig E, early stopping) where double descent does not appear, and note it appears in the critically parameterized regime only.

- Label noise. The commission says the "sharpest peaks depend on label noise," which the primary supports exactly: Nakkiran et al. see the peak most strongly with label noise, and in several clean settings the critical region is a plateau rather than a peak (CIFAR-10, Fig 4b). But the claim "no noise, no peak" would be too strong: real clean-data peaks appear for ResNets and CNNs on CIFAR-100 (Fig 4a, Fig 7) and for Transformers on IWSLT'14 (Fig 8), and for adversarial training. The precise line: noise sharpens the peak and shifts its location; noise is not strictly required.

## Numbers

```text
Figure: Training points in Belkin et al.'s random-Fourier-features MNIST run: n = 10^4
Owner:  Belkin et al. 2019 (arXiv 1812.11118), Fig 2
Scope:  10-class MNIST, one-versus-rest; feature count N swept; risk peak sits exactly at N = n = 10^4.
```

```text
Figure: Belkin et al. fully connected MNIST run: n = 4x10^3 training points, input dimension d = 784,
        K = 10 classes; interpolation threshold at n*K
Owner:  Belkin et al. 2019, Fig 4
Scope:  Single hidden layer of H units; parameter count (d+1)H + (H+1)K.
```

```text
Figure: Nakkiran et al. sample-wise "more data hurts" factor: 4.5x (4k -> 18k IWSLT'14 sentence pairs)
Owner:  Nakkiran et al. 2019, Fig 3 and abstract
Scope:  6-layer Transformer, IWSLT'14 German-to-English, cross-entropy (per-token) test loss vs embedding
        dimension d_model. Approximate figure reads: the 4k-sample curve peaks near test loss 22 at
        d_model ~ 25; the 18k-sample curve peaks near test loss 16 at d_model ~ 55; across roughly
        d_model 50-90 the 18k curve lies above the 4k curve, i.e. more data is worse there.
```

```text
Figure: Nakkiran et al. canonical model-wise curve, ResNet18 on CIFAR-10 with 15% label noise
Owner:  Nakkiran et al. 2019, Fig 1 (left), test error on the noisy distribution
Scope:  Width parameter k swept from 1 to 64 (standard ResNet18 = 64), Adam, 4K epochs, data augmentation.
        Approximate figure reads: test error rises to a local peak near 0.48 in the critical region
        (width roughly 6-18), then descends to roughly 0.28 at width 64. Exact per-point values are not
        tabulated in the paper; the released raw data (gitlab link below) holds the exact series.
```

```text
Figure: Label-noise levels swept in Nakkiran et al.'s model-wise experiments: 0%, 5%, 10%, 15%, 20%
Owner:  Nakkiran et al. 2019, Fig 4 (ResNets, CIFAR-100 and CIFAR-10)
Scope:  0% (clean) shows a real peak on CIFAR-100 and a plateau on CIFAR-10; the peak grows and shifts right
        as noise increases.
```

```text
Figure: EMC threshold used for "approximately zero training error": epsilon = 0.1
Owner:  Nakkiran et al. 2019, Definition 2.1 and Hypothesis 1 (Section 2)
Scope:  Heuristic; the authors state they have no principled way to choose epsilon.
```

## Source assets

```text
Asset: Nakkiran et al. 2019, Fig 1 (left) - the labeled double-descent curve for ResNet18 on CIFAR-10 with
       15% label noise, marking the classical (bias-variance) regime, the critical regime, the modern
       ("larger model is better") regime, and the interpolation threshold.
Shows: The whole finding in one image: test error falls, peaks at the interpolation threshold, falls again;
       train error going to zero at the same width where test error peaks.
Crop:  Keep both axes and their labels, the three regime labels, and the interpolation-threshold marker.
       If cropping to the test curve, retain the train-error curve so the reader sees the peak coincides
       with train error reaching zero.
```

```text
Asset: Nakkiran et al. 2019, Fig 3 - Transformer test loss vs embedding dimension for 4k vs 18k samples.
Shows: The "more data hurts" result concretely: the 18k curve peaks higher-to-the-right and sits above the
       4k curve across a band of model sizes.
Crop:  Retain both sample-count series and their legend, both axis labels, and the shaded band where 18k is
       worse than 4k. Do not crop to a single curve; the comparison is the point.
```

```text
Asset: Nakkiran et al. 2019, Fig 4(b) - ResNet18 on CIFAR-10 across 0/5/10/15/20% label noise.
Shows: The plateau-to-peak transition: the clean curve has a flat critical region that becomes a sharp peak
       as label noise rises. Directly supports the "peaks depend on label noise" point.
Crop:  Keep all noise-level series and the legend; keep the width axis. The family of curves is the evidence.
```

```text
Asset: Belkin et al. 2019, Fig 1 - schematic of the classical U-curve beside the double-descent curve.
Shows: The claim in the cleanest possible form: the U-shape is the left half; the double-descent curve
       extends it past the interpolation threshold. Good for teaching the contrast before showing real data.
Crop:  Keep both panels (classical and double-descent) so the "subsumes" relationship is visible.
```

```text
Asset: Nakkiran et al. released raw data, https://gitlab.com/harvard-machine-learning/double-descent
Shows: The exact per-point error/loss series behind the figures, if a chart built from a verified numeric
       series is wanted. Named here because the paper reports curves, not tables.
Crop:  Not an image; a data source for an honest chart-N.py series.
```

## Discarded

```text
https://direct.mit.edu/neco/article/4/1/1/5624 : Geman, Bienenstock & Doursat, "Neural Networks and the
    Bias/Variance Dilemma," Neural Computation 4(1):1-58, 1992 - the canonical origin of the bias-variance
    dilemma the article overturns. Bibliographic details and its standard thesis (large numbers of parameter
    estimates raise variance; wrong model structure raises bias) were confirmed through the publisher listing
    and indexers, but the full text was gated (MIT Press returned HTTP 403; Semantic Scholar and the DOI page
    returned no readable body). Not cited as read. The classical statement the lesson needs is instead owned
    by two sources read in full: Belkin et al.'s textbook corollary that "a model with zero training error is
    overfit ... and will typically generalize poorly," and Nakkiran et al.'s statement that classical wisdom
    holds "larger models are worse" past a threshold (they cite Hastie et al. 2005, "The Elements of
    Statistical Learning"). If the writer wants a dedicated classical citation, Geman 1992 or Hastie et al.
    should be opened directly first.
https://openai.com/index/deep-double-descent/ : OpenAI's blog restatement of Nakkiran et al. Returned HTTP
    403 to the fetch, and in any case it is the authoring party restating its own paper, so it would not
    count as an independent secondary. The canonical paper already covers everything the blog would.
https://www.pnas.org/doi/10.1073/pnas.1903070116 : the PNAS page of Belkin et al. Gated (HTTP 403) to the
    automated fetch; not discarded as a source (the same paper was read via arXiv 1812.11118), only noted
    here because its own journal page did not resolve to readable text through the tool. The DOI is correct
    and the address is recorded on the Belkin entry above.
```

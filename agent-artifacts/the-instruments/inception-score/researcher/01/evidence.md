# Evidence record: the-instruments/inception-score (01)

The evidence supports the commissioned angle firmly. Four primary documents were
opened and read in full or at the cited passages: the paper that defined the
Inception Score (Salimans et al. 2016), the critique that demonstrated gaming it
(Barratt & Sharma 2018), the paper that introduced FID as a replacement (Heusel
et al. 2017), and a primary argument that one-number metrics cannot separate
failure modes (Sajjadi et al. 2018). Three more primaries and one secondary
survey supply context and the cost. The construction, the gaming demonstration,
and the FID critique are all documented precisely, with the formula recorded in
each paper's own notation. The record is strongest on mechanism and on the
gaming result; it is thinner on two things the brief asked for. First, "blindness
to intra-class diversity" is not a named shortcoming in Barratt & Sharma; it
follows from the score's construction (the marginal is taken over the 1000
ImageNet classes, so within-class variety is invisible) and is shown implicitly
by their attack, which emits one optimized image per class, but no primary here
states it as a headline finding. Second, "how widely IS was used" is sourced to
the authors' own claims that it was "the most widely used metric" plus one
concrete headline example (BigGAN), not to a systematic count. The angle is not
undermined: the authors of the Inception Score themselves cautioned that directly
optimizing it produces adversarial examples, so the gaming result confirms a
documented caveat rather than refuting a defense. The fair counter is that IS did
correlate with human judgment in the regime it was built for, which Barratt &
Sharma concede, and which the record preserves below.

## Sources

```text
URL:         https://arxiv.org/abs/1606.03498
Kind:        primary. The paper that defines the Inception Score; its authors own
             the metric and the claims made for it. Authors: Tim Salimans, Ian
             Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen.
             Affiliation is not printed on the arXiv abstract page; the reference
             implementation Barratt & Sharma cite lives at github.com/openai,
             identifying the work with OpenAI. NeurIPS (NIPS) 2016, pp. 2234-2242.
Establishes: The construction. The Inception Score applies a pretrained Inception
             classifier to every generated image, reads the conditional label
             distribution p(y|x), and rewards two properties at once: each image
             should look like a clear single object (p(y|x) low entropy), and the
             set should span many classes (the marginal p(y) high entropy). The
             exponential is cosmetic, "so the values are easier to compare." The
             authors report the score correlates well with human judgment, and
             they caution it is a "rough guide" only. The classifier is the
             specific TensorFlow inception-2015-12-05 checkpoint trained on
             ImageNet (1.2M images, 1000 classes).
Paraphrase:  "We apply the Inception model to every generated image to get the
             conditional label distribution p(y|x). Images that contain meaningful
             objects should have a conditional label distribution p(y|x) with low
             entropy. Moreover, we expect the model to generate varied images, so
             the marginal [...] should have high entropy. Combining these two
             requirements, the metric that we propose is: exp(E_x KL(p(y|x)||p(y))),
             where we exponentiate results so the values are easier to compare."
             The authors validated it by the MTurk drop (see Numbers) and caution
             that "the Inception score should be used as a rough guide to evaluate
             models that were trained via some independent criterion; directly
             optimizing Inception score will lead to the generation of adversarial
             examples."
Locators:    Section 4 "Assessment of image quality" (p.4, lines beginning "As an
             alternative to human annotators"); Table 3 and surrounding text (p.7).
             arXiv v1 10 Jun 2016.
Quote:       "directly optimizing Inception score will lead to the generation of
             adversarial examples." (Section 4, p.7)
```

```text
URL:         https://arxiv.org/abs/1801.01973
Kind:        primary. Owns the critique and the gaming demonstration firsthand.
             Authors: Shane Barratt, Rishi Sharma, both Stanford University (stated
             in the PDF author footnote). Submitted to the ICML 2018 Workshop on
             Theoretical Foundations and Applications of Deep Generative Models.
Establishes: (1) The formula, restated as IS(G) = exp(E_{x~pg} D_KL(p(y|x) || p(y)))
             (Eq. 1), with p(y) the marginal class distribution. (2) The
             information-theoretic reading: ln(IS(G)) = I(y;x) = H(y) - H(y|x)
             (Eqs. 2-3, proof in Appendix A), so the score is the mutual
             information between generated images and predicted class. (3) The hard
             bound 1 <= IS(G) <= 1000 (Eq. 4; proof Appendix B), the upper bound
             being the number of ImageNet classes. (4) The gaming demonstration: by
             running the Fast Gradient Sign Method against the Inception network
             (epsilon = .001, N = 100 iterations, cycling target class 1..1000),
             starting from uniform-noise images they reach IS = 986.10; starting
             from a CIFAR-10-trained WGAN they reach IS = 900.10 (appendix text) /
             900.15 (Figure 1 caption and Section 4.2.2) with "realistic-looking"
             output. "The maximum achievable Inception Score is 1000, and the
             highest achieved in the literature is on the order of 10." (5)
             Sensitivity to weights: three Inception implementations with near-equal
             ImageNet accuracy give scores differing by 3.5% (ImageNet val) and
             11.5% (CIFAR) between Keras and Torch (Table 1). (6) Dependence on the
             nsplits batching parameter (Table 2). (7) Misuse beyond ImageNet: on
             CIFAR the top predicted classes are "Moving Van," "Sorrel,"
             "Threshing Machine," etc. (Table 3), and the conditional entropy on
             CIFAR images (4.664 bits) is closer to that of random-pixel images
             (6.512 bits) than to ImageNet images (1.97 bits). (8) Memorization:
             "a generative algorithm that memorized an appropriate subset of the
             training data would perform extremely well in terms of Inception
             Score," so a validation score is effectively an upper bound and
             overfitting must be reported separately.
Paraphrase:  Barratt & Sharma do not dispute that IS correlated with human
             judgment in Salimans' regime ("Though we don't dispute that this is
             the case within a significant regime of its usage"). Their claim is
             that the metric compares generated images only to a fixed classifier,
             never to real data, so it cannot detect intra-set collapse to one
             image per class, memorization, or adversarial inflation, and it is
             unstable under choices (network weights, nsplits, dataset) unrelated
             to image quality.
Locators:    Section 3.2-3.4 (formula, bound, estimator); Section 4.1.1 and Table 1
             (weight sensitivity); Section 4.1.2 and Table 2 (nsplits); Section
             4.2.1 and Table 3 (beyond ImageNet, entropies); Section 4.2.2,
             Figure 1, and Appendix "Achieving High Inception Scores" + Algorithm 1
             and Figure 2 (the attack, 986.10 and 900.10/900.15); Section 4.2.3
             (overfitting). arXiv v2 21 Jun 2018.
Quote:       "slight weight changes result in drastically different scores for the
             exact same set of sampled images." (Section 4.1.1); "a generative
             algorithm that memorized an appropriate subset of the training data
             would perform extremely well in terms of Inception Score." (4.2.3)
```

```text
URL:         https://arxiv.org/abs/1706.08500
Kind:        primary. Introduces the Fréchet Inception Distance and owns the
             critique of IS that motivates it. Authors: Martin Heusel, Hubert
             Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter.
             Affiliation is not printed on the fetched pages. NeurIPS 2017,
             pp. 6629-6640.
Establishes: The explicit IS critique and the FID construction. FID feeds real and
             generated images through Inception-v3, takes the last pooling layer as
             a feature ("coding") layer, models those features as one multivariate
             Gaussian for real data (mean m_w, covariance C_w) and one for generated
             data (m, C), and reports the Fréchet / Wasserstein-2 distance between
             the two Gaussians. Lower is better, and zero requires matching the real
             feature statistics. An appendix experiment degrades images with six
             disturbances (Gaussian noise, Gaussian blur, implanted black
             rectangles, swirl, salt-and-pepper, and contamination with ImageNet
             images) and shows FID rises monotonically with the disturbance while
             IS does not.
Paraphrase:  "Drawback of the Inception Score is that the statistics of real world
             samples are not used and compared to the statistics of synthetic
             samples." FID formula (Eq. 6): d^2((m,C),(m_w,C_w)) = ||m - m_w||_2^2
             + Tr(C + C_w - 2 (C C_w)^{1/2}). Appendix A1 restates the IS (Eq. 8)
             and, in Figure A8, reports that "The FID captures the disturbance
             level very well by monotonically increasing whereas the Inception
             Score fluctuates, stays flat or even, in the worst case, decreases."
Locators:    Section "Experiments" / introduction of FID (the paragraph beginning
             "A well-performing approach... Inception Score" through Eq. 6);
             Figure 3; Appendix A1 "Fréchet Inception Distance (FID)," Eq. 8, and
             Figure A8. arXiv v1 26 Jun 2017 (FID defined in all versions).
Quote:       "the statistics of real world samples are not used and compared to the
             statistics of synthetic samples." (Appendix A1 and main text)
```

```text
URL:         https://arxiv.org/abs/1806.00035
Kind:        primary. Owns the argument that a single scalar metric cannot separate
             sample quality from mode coverage, and proposes precision/recall for
             distributions instead. Authors: Mehdi S. M. Sajjadi, Olivier Bachem,
             Mario Lucic, Olivier Bousquet, Sylvain Gelly (Google Brain). NeurIPS
             2018.
Establishes: Even a real-data-referenced metric like FID (and by extension IS)
             returns one number, so it cannot tell a model that produces
             low-quality samples apart from one that drops modes. Precision (sample
             quality) and recall (coverage of the target distribution) are distinct
             axes and should be measured separately.
Paraphrase:  Abstract: commonly used metrics such as FID "correlate well with the
             perceived quality of samples and are sensitive to mode dropping.
             However, these metrics are unable to distinguish between different
             failure cases since they only yield one-dimensional scores." This
             generalizes the intra-class-diversity concern: one scalar conflates
             "looks good" with "covers the data."
Locators:    Abstract; the precision/recall framework is the body's contribution.
             arXiv v1 31 May 2018.
Quote:       "these metrics are unable to distinguish between different failure
             cases since they only yield one-dimensional scores." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1511.01844
Kind:        primary. Owns the foundational argument, predating IS, that generative-
             model evaluation criteria are largely independent. Authors: Lucas
             Theis, Aäron van den Oord, Matthias Bethge. ICLR 2016.
Establishes: A model can score well on one criterion (sample quality, average
             log-likelihood, Parzen estimates) and poorly on another, so no single
             score stands in for overall quality, and metrics should be chosen for
             the intended application. This is the general principle that the IS
             critique is a specific case of.
Paraphrase:  Abstract: "Good performance with respect to one criterion [...] need
             not imply good performance with respect to the other criteria," and
             "generative models need to be evaluated directly with respect to the
             application(s) they were intended for."
Locators:    Abstract. arXiv v3 24 Apr 2016. (Cited by Barratt & Sharma as Theis
             et al. 2015.)
Quote:       "generative models need to be evaluated directly with respect to the
             application(s) they were intended for." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1711.10337
Kind:        primary. Owns a large-scale empirical study of GAN evaluation.
             Authors: Mario Lucic, Karol Kurach, Marcin Michalski, Sylvain Gelly,
             Olivier Bousquet (Google Brain). NeurIPS 2018.
Establishes: With enough hyperparameter search and random restarts, competing GAN
             algorithms reach similar scores, so reported metric gains can reflect
             tuning and compute rather than a better model. This is direct evidence
             for the "cost" of over-trusting a single benchmark number. The study
             uses FID as its primary measure.
Paraphrase:  Abstract: "we did not find evidence that any of the tested algorithms
             consistently outperforms the non-saturating GAN," and "most models can
             reach similar scores with enough hyperparameter optimization and random
             restarts."
Locators:    Abstract. arXiv v1 28 Nov 2017, last revised 29 Oct 2018.
Quote:       "we did not find evidence that any of the tested algorithms
             consistently outperforms the non-saturating GAN." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1809.11096
Kind:        primary. A concrete, high-profile example of IS reported as a headline
             comparison. Authors: Andrew Brock, Jeff Donahue, Karen Simonyan
             (BigGAN). ICLR 2019.
Establishes: That the Inception Score remained a headline yardstick for image GANs
             well after the 2017-2018 critiques. BigGAN reports, as its top-line
             result on 128x128 ImageNet, an Inception Score of 166.5 and an FID of
             7.4, against a stated previous best IS of 52.52 and FID of 18.6.
Paraphrase:  Abstract: trained on ImageNet at 128x128, the models "achieve an
             Inception Score (IS) of 166.5 and Frechet Inception Distance (FID) of
             7.4, improving over the previous best IS of 52.52 and FID of 18.6."
Locators:    Abstract. arXiv v1 28 Sep 2018.
Quote:       "an Inception Score (IS) of 166.5 and Frechet Inception Distance (FID)
             of 7.4, improving over the previous best IS of 52.52 and FID of 18.6."
```

```text
URL:         https://arxiv.org/abs/1802.03446
Kind:        secondary. A single-author review that surveys and critiques measures
             proposed by others; it reports on the field from outside, rather than
             owning any one metric. Author: Ali Borji.
Establishes: That as of 2018 there was no consensus on which GAN evaluation measure
             to use, and that the field had accumulated many competing measures
             (the review covers more than 24 quantitative and 5 qualitative ones),
             with IS and FID among the most prominent. Useful only as context for
             the "many metrics, no agreement" point; the specific per-metric
             verdicts live in the body, which was not read beyond the abstract.
Paraphrase:  Abstract: "there is no consensus as to which measure best captures
             strengths and limitations of models and should be used for fair model
             comparison," and it "review[s] and critically discuss[es] more than 24
             quantitative and 5 qualitative measures."
Locators:    Abstract. arXiv v1 9 Feb 2018.
Quote:       "there is no consensus as to which measure best captures strengths and
             limitations of models and should be used for fair model comparison."
```

## Contradictions

- The gaming result confirms a caveat the IS authors printed, rather than
  refuting a defense. Salimans et al. 2016 already wrote that "directly optimizing
  Inception score will lead to the generation of adversarial examples" and that
  the score is a "rough guide" for models trained on an independent objective. A
  defender can therefore call Barratt & Sharma's uniform-noise attack (IS 986.10)
  contrived: nobody ships FGSM noise. The force of Barratt & Sharma is in the
  other two findings, which resist that charge: the WGAN-initialized attack
  reaches IS 900.15 with "realistic-looking" images, and indirect optimization
  (using IS for early stopping, model selection, or architecture search) exerts
  the same pull without anyone running an explicit attack. Record both sides.

- IS did work in its original regime. Salimans et al. validated it against MTurk
  (accuracy fell from 78.7% to 71.4% when samples were filtered to the top 1% by
  IS, i.e. better-scoring samples fooled people more), and Barratt & Sharma
  explicitly "don't dispute" that IS correlated with human judgment "within a
  significant regime of its usage." The angle should not claim IS was useless,
  only that it could not support the comparisons it was used for.

- IS and FID do not always disagree. Heusel et al. present FID as an improvement
  on IS, not as contradicting it on clean images; both rank heavily degraded
  images worse. Their divergence appears under specific disturbances (Figure A8),
  where IS "fluctuates, stays flat or even [...] decreases" while FID keeps rising.
  The claim to make is that FID tracks degradation consistently and IS does not,
  not that the two routinely point opposite ways.

- Internal number discrepancy in the primary: Barratt & Sharma report the
  WGAN-initialized attack as IS 900.15 in Figure 1 and Section 4.2.2, but as
  900.10 in the appendix text ("an Inception score of 900.10"). Use "about 900" if
  a single figure is needed, or cite the location with the exact value.

- Scope caution on "IS above real data." BigGAN's generated IS of 166.5 sits above
  some measured real-ImageNet IS values (Barratt & Sharma measure real ImageNet
  validation IS at roughly 63-66 for 50k images with 10 splits of 5,000), but real-
  ImageNet IS is itself implementation- and split-dependent and is quoted far
  higher elsewhere under different protocols. Do not assert flatly that BigGAN
  "beats real data" on IS without naming the protocol; the safe point is that IS
  saturates and its reference value is not fixed.

## Numbers

```text
Figure: 1 <= IS(G) <= 1000
Owner:  Barratt & Sharma 2018, Eq. 4 (proof Appendix B)
Scope:  Dimensionless. Upper bound equals the 1000 ImageNet classes the Inception
        classifier outputs; the bound is a property of the metric, not of any model.
```

```text
Figure: IS = 986.10 (noise init); IS = 900.10 / 900.15 (WGAN init)
Owner:  Barratt & Sharma 2018, Appendix "Achieving High Inception Scores" and
        Figure 1 / Section 4.2.2
Scope:  FGSM attack, epsilon = .001, N = 100 iterations, target class cycling
        1..1000; against the max of 1000 and literature values "on the order of 10."
        900.10 vs 900.15 is an internal discrepancy in the paper.
```

```text
Figure: Real data 11.24 +/- .12; "Our methods" 8.09 +/- .07
Owner:  Salimans et al. 2016, Table 3
Scope:  CIFAR-10, Inception Score over 50,000 generated images; "Real data" is the
        CIFAR-10 images themselves, the highest entry in the table.
```

```text
Figure: MTurk accuracy 78.7% (all samples) -> 71.4% (top 1% by IS)
Owner:  Salimans et al. 2016, Section 4 (p.7)
Scope:  Humans separating 50% real / 50% generated CIFAR-10; filtering to the
        highest-IS 1% of samples made them harder to tell from real, the validation
        that IS tracks perceived quality.
```

```text
Figure: Keras-vs-Torch IS gap: 3.5% (ImageNet val), 11.5% (CIFAR)
Owner:  Barratt & Sharma 2018, Table 1 and surrounding text
Scope:  Same images, three Inception implementations with near-equal ImageNet top-1
        accuracy (0.756 / 0.772 / 0.777). Full table, 10 splits of N=5,000:
        CIFAR-10 50k train -- IV2 TF 11.237+/-0.11, IV3 Torch 9.737+/-0.148,
        IV3 Keras 10.852+/-0.181. ImageNet val 50k -- IV2 TF 63.028+/-8.311,
        IV3 Torch 63.702+/-7.869, IV3 Keras 65.938+/-8.616.
```

```text
Figure: Mean conditional entropy H(y|x): 4.664 bits (CIFAR train), 6.512 bits
        (uniform random pixels), 1.97 bits (ImageNet val); ~10 bits possible
Owner:  Barratt & Sharma 2018, Section 4.2.1
Scope:  Inception-v3 conditional label entropy. Shows the classifier is nearly as
        uncertain on real CIFAR images as on random noise, so IS's first assumption
        (sharp, recognizable objects) fails off the ImageNet distribution.
```

```text
Figure: nsplits dependence: mean IS 9.9147 (1 split) down to 9.0884 (200 splits)
Owner:  Barratt & Sharma 2018, Table 2
Scope:  Inception-v3 Torch, 50,000 samples batched into nsplits chunks; the reported
        score moves ~0.8 on a standard parameter that has nothing to do with images.
```

```text
Figure: BigGAN IS 166.5, FID 7.4 vs previous best IS 52.52, FID 18.6
Owner:  Brock, Donahue, Simonyan 2018, Abstract
Scope:  128x128 ImageNet. Evidence that IS persisted as a headline number after the
        critiques; see the scope caution above before comparing to real-data IS.
```

## Source assets

```text
Asset: Barratt & Sharma 2018, Figure 1 (and Figure 2 (a)/(b)) -- grids of images
       that score IS 986.10 (noise-initialized) and 900.15 (WGAN-initialized).
Shows: The central demonstration made visible: near-maximal Inception Scores
       produced by images that are adversarial texture or only barely GAN-like,
       one optimized image per class with no within-class variety.
Crop:  Keep the caption's score value with the grid, since the number is the point.
       Figure 2 pairs the noise-init and WGAN-init grids; keep both halves if
       contrasting "pure attack" against "realistic-looking attack." Do not crop to
       a single tile, which loses the one-per-class structure.
```

```text
Asset: Heusel et al. 2017, Figure A8 (Appendix) -- FID (left column) vs Inception
       Score (right column) under six increasing disturbances.
Shows: FID rising monotonically with degradation while IS stays flat, fluctuates,
       or falls. This is the clearest single picture of why FID replaced IS.
Crop:  Retain paired rows so FID and IS are read against the same disturbance; the
       disturbance increases left to right, so keep the full horizontal axis. Main-
       text Figure 3 shows FID alone across the same disturbances if only FID's
       behavior is needed.
```

```text
Asset: Barratt & Sharma 2018, Table 3 -- top 10 CIFAR classes predicted by the
       Inception classifier (Moving Van, Sorrel, Container Ship, Threshing Machine,
       Hartebeest, ...) beside the 10 actual CIFAR-10 classes.
Shows: Concretely why IS misreads a non-ImageNet dataset: the classifier's marginal
       is dominated by ImageNet categories CIFAR never contained.
Crop:  Keep both columns side by side; the contrast between the two lists is the
       evidence. The absurd labels (Threshing Machine, Fox Squirrel) carry it.
```

```text
Asset: Salimans et al. 2016, Table 3 -- Inception scores for real data and a ladder
       of ablated models, real data highest at 11.24.
Shows: The intended use: rank models, with real images on top. Useful to establish
       what the score was built to do before showing what it cannot do.
Crop:  Keep the "Real data" row adjacent to "Our methods" so the 11.24 vs 8.09 gap
       is visible; the lower ablation rows are optional.
```

## Discarded

```text
https://ar5iv.labs.arxiv.org/html/1706.08500 and https://arxiv.org/html/1706.08500:
  Rendering routes only, not the source. The ar5iv HTML conversion of the FID paper
  failed ("Conversion to HTML had a Fatal error") and the arXiv native HTML returned
  404. Read the official PDF instead and recorded the canonical arxiv.org/abs URL.
```

```text
Gulrajani et al. 2017 (WGAN-GP, arXiv 1704.00028) and Kynkäänniemi et al. 2019
  (improved precision/recall, arXiv 1904.06991): not opened. WGAN-GP would add a
  second headline-IS example but BigGAN already supplies one post-critique; the
  improved-precision/recall paper would duplicate Sajjadi et al.'s point. Left out
  to meet the floor with sources that change the interpretation rather than repeat
  it. Flag for a later invocation if the writer needs a pre-FID headline example.
```

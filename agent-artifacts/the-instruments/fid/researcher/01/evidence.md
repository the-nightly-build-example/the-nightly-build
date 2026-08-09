# Evidence: the-instruments/fid (01)

The evidence supports the commission fully. The construction of FID is fixed and
quotable from its originating paper (Heusel et al. 2017): it runs both a real
image set and a generated image set through the same ImageNet-trained
Inception-v3 network, reads a 2048-number summary of each image from the final
pooling layer, fits one multivariate Gaussian (a mean vector and a covariance
matrix) to each set, and reports one Fréchet / Wasserstein-2 distance between
those two Gaussians. Three independent primaries then show the single number
moving for reasons unrelated to image quality: sample count (Chong & Forsyth
2020), matching ImageNet class frequencies (Kynkäänniemi et al. 2023), and the
resizing code used before the network sees the image (Parmar et al. 2022). The
strongest fully-sourced "misled" case is Kynkäänniemi et al. 2023 against a real
published claim: Projected FastGAN reported an FFHQ FID essentially tied with
StyleGAN2 (5.28 vs 5.30), yet human inspection finds more facial distortion in
the FastGAN samples, and a CLIP-feature version of the same distance ranks
StyleGAN2 far ahead (2.76 vs 4.67).

The record is thin in one place the writer should respect: Chong & Forsyth
demonstrate the sample-size effect as a slope (FID is linear in 1/N) and as a
rank reversal between two runs, not as one clean "X points at 10k, Y at 50k"
delta, so the writer should teach the mechanism and the reversal rather than
quote a single headline number. The record also carries genuine defenses of FID
(the original paper's monotonic-degradation experiment; Borji's survey; FID's
ability to catch mode collapse), which bound the criticism rather than cancel
it. See Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/1706.08500
Kind:        primary. It is the paper that introduced FID and owns its definition;
             the authors are the authoring party for the construction claim.
Establishes: The exact FID construction and the claim that FID improves on the
             Inception Score. Title: "GANs Trained by a Two Time-Scale Update Rule
             Converge to a Local Nash Equilibrium." Authors: Martin Heusel, Hubert
             Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter.
             Venue: NeurIPS (NIPS) 2017. (Author affiliations were not captured
             from the abstract page; do not assert an institution without reading it.)
Paraphrase:  FID passes every image through the pretrained Inception-v3 model and
             reads the activations of the last pooling layer as the image's code
             (the 2048-dimensional pool3 features). It models each set's codes as a
             multivariate Gaussian, justified because the Gaussian is the maximum-
             entropy distribution for a given mean and covariance. It then measures
             the Fréchet distance between the real Gaussian (mean m, covariance C)
             and the generated Gaussian (mean m_w, covariance C_w). The paper argues
             FID captures similarity of generated to real images better than the
             Inception Score because the Inception Score never looks at real-image
             statistics at all.
Locators:    Appendix Section A1, "Fréchet Inception Distance (FID)."
Quote:       "we use the last pooling layer as coding layer." / "The Gaussian is the
             maximum entropy distribution for given mean and covariance, therefore we
             assume the coding units to follow a multidimensional Gaussian." /
             Formula as written: d^2((m,C),(m_w,C_w)) = ||m - m_w||_2^2 +
             Tr(C + C_w - 2 (C C_w)^{1/2}). In words: the squared distance between the
             two mean vectors, plus the trace of (the two covariance matrices added,
             minus twice the matrix square root of their product). / FID "captures the
             similarity of generated images to real ones better than the Inception
             Score," which "does not use the statistics of real world samples."
```

```text
URL:         https://arxiv.org/abs/1706.08500
Kind:        primary (same paper, defense passage recorded separately so the writer
             can steelman FID from its own authors).
Establishes: That FID responds to real image degradation in the expected direction.
Paraphrase:  The authors degrade a real image set with six disturbance types and
             show FID rises smoothly as the disturbance grows. This is the paper's
             argument that FID tracks genuine loss of image quality.
Locators:    Appendix Section A1, disturbance experiments.
Quote:       Six disturbances used: "Gaussian noise, Gaussian blur, implanted black
             rectangles, swirled images, salt and pepper noise, and CelebA dataset
             contaminated by ImageNet images." / "The FID captures the disturbance
             level very well by monotonically increasing."
```

```text
URL:         https://arxiv.org/abs/1911.07023
Kind:        primary. It owns the sample-size bias result and the FID_infinity
             estimator; the authors are the authoring party.
Establishes: FID computed on a finite sample is biased, the bias depends on the
             model, and comparisons at a fixed sample count can reverse.
Paraphrase:  The expected FID from a finite generated sample is not the true value.
             Plotted against 1/N (N = number of generated samples), FID is close to
             linear across models, and it decreases (improves) as N grows. Because
             the size of the bias depends on the specific generator, one model can
             beat another only because its bias term is smaller. Two identical DCGAN
             runs even swap ranks depending on the N chosen. Their fix fits a line to
             FID-versus-1/N over several sample counts and extrapolates to 1/N = 0
             (infinite samples), reported as FID_infinity, using Sobol / Quasi-Monte
             Carlo sampling to steady the fit. Title: "Effectively Unbiased FID and
             Inception Score and where to find them." Authors: Min Jin Chong, David
             Forsyth. Venue: CVPR 2020.
Locators:    Figures 2-4; Equation 7; Algorithm 1.
Quote:       "the bias term depends on the particular model being evaluated, so model
             A may get a better score than model B simply because model A's bias term
             is smaller." / "No comparison that uses FID_N is reliable." / "FIDs are
             linear with respect to 1/N across all experiments, with higher variance
             (more spikes) when N is small."
```

```text
URL:         https://arxiv.org/abs/2203.06026
Kind:        primary. It owns the ImageNet-class manipulation result and the
             Projected FastGAN vs StyleGAN2 comparison.
Establishes: FID can be lowered substantially by matching the ImageNet-class
             histogram of the generated set to the real set, with no gain in image
             quality; and a real published model comparison where FID misleads.
Paraphrase:  Because Inception-v3 was trained to classify ImageNet, its features
             carry heavy information about ImageNet class probabilities. Making the
             generated set's histogram of top ImageNet classifications match the real
             set's histogram drops FID sharply while a CLIP-feature distance barely
             moves, which shows the drop is class-frequency bookkeeping and not
             better pictures. On FFHQ faces, Projected FastGAN (FID 5.28) and
             StyleGAN2 (FID 5.30) look tied by FID, but the FastGAN samples show more
             facial distortion on inspection and score far worse on the CLIP-feature
             distance (4.67 vs 2.76). Title: "The Role of ImageNet Classes in Frechet
             Inception Distance." Authors: Tuomas Kynkaanniemi, Tero Karras, Miika
             Aittala, Timo Aila, Jaakko Lehtinen. Venue: ICLR 2023.
Locators:    Figures 6-7; Tables 1-2.
Quote:       "aligning the histograms of Top-N classifications between sets of
             generated and real images can reduce FID substantially -- without
             actually improving the quality of results." / "Projected FastGAN has
             lower FID than it should have, confirming that at least some of its
             apparent improvements are in the perceptual null space." / "FID can be
             manipulated to a great extent through the ImageNet classification
             probabilities, without meaningfully improving the generated results."
```

```text
URL:         https://arxiv.org/abs/2104.11222
Kind:        primary. It owns the resizing/compression incomparability result and the
             Clean-FID reference implementation.
Establishes: Low-level image handling before the network (resizing filter, JPEG
             compression) moves FID enough to change which model or checkpoint looks
             best, and the common libraries handle it inconsistently.
Paraphrase:  Downsizing an image with a fixed-width filter aliases it, and different
             libraries alias differently. Measured against correct PIL-bicubic
             resizing of the same real images (1024 to 299 pixels), the resizing
             choice alone produces FID gaps from 0.64 (PIL-bilinear) up to 7.43
             (naive nearest). When both real and generated images pass through the
             same aliased resizer, FID can come out lower than the correct pipeline,
             so a worse pipeline can post a better score. JPEG compression does the
             same: StyleGAN2 on LSUN Churches scores FID 4.00 on PNG data but 3.48 on
             JPEG-87, meaning compressing the images improves the reported number.
             Across training checkpoints the resizing choice is non-monotonic, so an
             aliased and an anti-aliased pipeline select different "best" checkpoints.
             PyTorch-FID, TensorFlow-FID, and OpenCV alias by default; only PIL adapts
             its filter width. Title: "On Aliased Resizing and Surprising Subtleties
             in GAN Evaluation." Authors: Gaurav Parmar, Richard Zhang, Jun-Yan Zhu.
             Venue: CVPR 2022.
Locators:    Tables 1-2; Figures 8-9.
Quote:       "implementations using OpenCV, TensorFlow and PyTorch libraries with
             default flags, contain severe aliasing artifacts." / "different
             checkpoints or methods may be selected, depending on if an aliased or an
             anti-aliased resizing function is chosen."
```

```text
URL:         https://arxiv.org/abs/1606.03498
Kind:        primary. It owns the Inception Score definition (the predecessor metric
             FID improves on).
Establishes: What the Inception Score is and that it never uses real-image
             statistics, which is the specific gap FID was built to close.
Paraphrase:  The Inception Score runs each generated image through an ImageNet-trained
             Inception classifier to get a label distribution p(y|x), rewards each
             image for being confidently one object (low-entropy p(y|x)), rewards the
             set for spanning many classes (high-entropy marginal p(y)), and combines
             the two as exp(E_x KL(p(y|x) || p(y))). It scores generated images
             against an ImageNet classifier only and looks at no real images. Title:
             "Improved Techniques for Training GANs." Authors: Tim Salimans, Ian
             Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen.
             Venue: NeurIPS 2016.
Locators:    Section 4, "Assessment of image quality."
Quote:       "We apply the Inception model to every generated image to get the
             conditional label distribution p(y|x)." / "the metric that we propose is:
             exp(E_x KL(p(y|x)||p(y)))."
```

```text
URL:         https://arxiv.org/abs/2111.01007
Kind:        primary. It owns the Projected GAN FID claim that Kynkaanniemi et al.
             later show is partly hollow. Recorded so the "what it cost" side of the
             misled case rests on the original claim, not a retelling.
Establishes: The real, widely-read claim that Projected GAN reaches state-of-the-art
             FID far faster, which readers took as a quality result.
Paraphrase:  The paper reports that Projected GAN advances state-of-the-art FID on
             twenty-two benchmark datasets and matches the previously lowest FIDs up
             to 40 times faster, cutting wall-clock training from about five days to
             under three hours. The headline is an FID number reached cheaply.
             Title: "Projected GANs Converge Faster." Authors: Axel Sauer, Kashyap
             Chitta, Jens Muller, Andreas Geiger. Venue: NeurIPS 2021. (Per-dataset
             FFHQ FID was not captured from the abstract page; the FFHQ figure of 5.28
             is taken from Kynkaanniemi et al. 2023, Figure 7.)
Locators:    Abstract.
Quote:       Projected GANs "advances the state-of-the-art Frechet Inception Distance
             (FID) on twenty-two benchmark datasets" and "match the previously lowest
             FIDs up to 40 times faster, cutting the wall-clock time from 5 days to
             less than 3 hours."
```

```text
URL:         https://arxiv.org/abs/2306.04675
Kind:        primary. It owns a large human study measuring how well FID tracks human
             judgment.
Establishes: That FID with Inception features does not track human perceptual
             judgment well, and penalizes diffusion models relative to what humans see.
Paraphrase:  The authors ran a large human study and found no widely-used metric
             correlates strongly with human evaluation. The perceptual realism humans
             grant diffusion models does not show up in commonly reported FID, which
             they attribute to FID's reliance on Inception-v3 features; features from
             DINOv2 support a richer evaluation. Title: "Exposing flaws of generative
             model evaluation metrics and their unfair treatment of diffusion models."
             Authors: George Stein, Jesse C. Cresswell, and co-authors. Venue: NeurIPS
             2023. (Exact evaluator count not captured from the abstract page.)
Locators:    Abstract; project at github.com/layer6ai-labs/dgm-eval.
Quote:       "the state-of-the-art perceptual realism of diffusion models as judged by
             humans is not reflected in commonly reported metrics such as FID."
```

```text
URL:         https://arxiv.org/abs/1904.06991
Kind:        primary. It owns the precision/recall alternative that separates the two
             failure modes one FID number hides.
Establishes: That a single FID cannot separate fidelity (are the images good) from
             coverage (does the model span the real variety).
Paraphrase:  The authors propose separate precision and recall metrics built from
             k-nearest-neighbor manifolds in feature space: precision measures how
             often generated images fall in the real manifold (fidelity), recall
             measures how much of the real manifold the generator covers (diversity).
             This splits apart two failure modes a single FID collapses into one
             number. Title: "Improved Precision and Recall Metric for Assessing
             Generative Models." Authors: Tuomas Kynkaanniemi, Tero Karras, Samuli
             Laine, Jaakko Lehtinen, Timo Aila. Venue: NeurIPS 2019.
Locators:    Abstract and method section.
Quote:       (No single sentence naming FID was captured; the paper frames prior
             single-number metrics as yielding "uninformative or contradictory
             results" where the split metric separates fidelity from coverage.)
```

```text
URL:         https://arxiv.org/abs/2401.09603
Kind:        primary. It owns the argument that FID's Gaussian assumption is wrong and
             proposes CMMD; recorded for the contradiction and for the Gaussian caveat.
Establishes: That FID's multivariate-Gaussian assumption on Inception features does
             not hold, and that FID contradicts human raters and misreads gradual
             quality changes in modern text-to-image models.
Paraphrase:  FID assumes the Inception features are multivariate Gaussian; the authors
             argue that assumption is incorrect, that FID is a biased estimator with
             poor sample efficiency, that it can contradict human raters, and that it
             fails to reflect the gradual quality gains of iterative text-to-image
             models. They propose CMMD, a maximum-mean-discrepancy distance on CLIP
             features that makes no distributional assumption. Title: "Rethinking FID:
             Towards a Better Evaluation Metric for Image Generation." Authors: Sadeep
             Jayasumana, Srikumar Ramalingam, Andreas Veit, Daniel Glasner, Ayan
             Chakrabarti, Sanjiv Kumar. Venue: CVPR 2024.
Locators:    Abstract.
Quote:       FID relies on "incorrect normality assumptions" and "contradicts human
             raters, it does not reflect gradual improvement of iterative text-to-image
             models, it does not capture distortion levels, and ... produces
             inconsistent results when varying the sample size."
```

```text
URL:         https://arxiv.org/abs/2103.09396
Kind:        secondary. A review that reports on FID from outside its authoring party,
             surveying strengths and weaknesses others established.
Establishes: FID's standing as one of the two most common GAN metrics, and an outside
             summary of its pros and cons that both supports and bounds the angle.
Paraphrase:  Borji names Inception Score and FID as the two most common GAN evaluation
             measures. He lists as strengths that FID is adopted for agreeing with
             human inspection, is sensitive to small changes such as slight blur or
             artifacts, and can catch intra-class mode collapse where the Inception
             Score cannot. He lists as weaknesses that the Gaussian assumption may not
             hold, that FID has high bias so the sample size must usually exceed about
             50,000 or the score is over-estimated, and that these feature metrics keep
             a blind spot for image quality. Author: Ali Borji (no institutional
             affiliation stated on the page).
Locators:    Review body, FID discussion.
Quote:       "The two most common GAN evaluation measures are Inception Score (IS) and
             Frechet Inception Distance (FID)." / "FID has been widely adopted because
             of its consistency with human inspection." / "A major drawback with FID is
             its high bias. The sample size to calculate FID has to be large enough
             (usually above 50K). Smaller sample sizes can lead to over-estimation."
```

## Contradictions

The criticism is real and the defenses are also real, and the writer should hold
both. Four lines cut against a flat "FID is broken" reading:

- FID moves in the right direction on genuine damage. Heusel et al. add six kinds
  of degradation to real images and FID rises monotonically each time
  (1706.08500, Appendix A1). Within one held-constant pipeline, FID does detect a
  picture getting worse.
- FID beats its predecessor on a specific axis. It looks at real-image statistics,
  which the Inception Score never does (1706.08500 vs 1606.03498), and it can catch
  intra-class mode collapse the Inception Score misses (Borji, 2103.09396).
- An outside reviewer records FID's agreement with human inspection as the reason
  it was adopted, alongside its known biases (Borji, 2103.09396). The failures are
  about comparing across sample counts, gaming the ImageNet lens, and drifting
  implementations, not about FID being random.
- The failure cases share one shape: they break comparability, not sensitivity. All
  three primaries (1911.07023, 2203.06026, 2104.11222) hold image quality fixed and
  move FID by changing something else. That is the honest frame. It sharpens the
  commission's angle rather than undercutting it. This does not undermine the angle.

One internal tension for the record's honesty: the Gaussian assumption is defended
in the originating paper as a maximum-entropy choice (1706.08500) and attacked as
simply incorrect by Jayasumana et al. (2401.09603). The writer should present it
as a modeling choice with a known cost, not as settled either way.

## Numbers

```text
Figure: 2048
Owner:  Heusel et al. 2017 (1706.08500)
Scope:  Dimension of the Inception-v3 final-pooling (pool3) feature vector FID reads
        per image. Each image set is summarized by a 2048-length mean and a
        2048x2048 covariance.
```

```text
Figure: FID(FFHQ) = 5.28 (Projected FastGAN) vs 5.30 (StyleGAN2)
Owner:  Kynkaanniemi et al. 2023 (2203.06026), Figure 7
Scope:  FFHQ faces. The two models look tied by FID; human inspection favors
        StyleGAN2 and a CLIP-feature distance ranks StyleGAN2 far ahead (see below).
```

```text
Figure: FID_CLIP = 2.76 (StyleGAN2) vs 4.67 (Projected FastGAN)
Owner:  Kynkaanniemi et al. 2023 (2203.06026), Figure 7
Scope:  FFHQ faces, same two models. A CLIP-feature version of the same distance,
        used as a quality cross-check, separates the models that Inception FID ties.
```

```text
Figure: FID 5.30 -> 4.70 (about -11%) from Top-1 ImageNet-class matching;
        5.30 -> 1.78 (about -66%) from pre-logits resampling
Owner:  Kynkaanniemi et al. 2023 (2203.06026), Tables 1-2
Scope:  FFHQ. The large drop comes with only a -4.3% move in the CLIP-feature
        distance, so the images did not meaningfully improve.
```

```text
Figure: Resizing-only FID gaps: 0.64 (PIL-bilinear), 4.34 (TensorFlow-bilinear),
        4.36 (PyTorch-bilinear), 7.43 (naive nearest), each vs correct PIL-bicubic
Owner:  Parmar et al. 2022 (2104.11222), Table 1
Scope:  Same real images resized 1024 -> 299 pixels. The differences come purely from
        the resizing filter, before any model is compared.
```

```text
Figure: StyleGAN2 on LSUN Churches: FID 4.00 (PNG) vs 3.48 (JPEG-87)
Owner:  Parmar et al. 2022 (2104.11222), Figure 8
Scope:  Compressing the images improves the reported FID, so post-processing can lower
        a score without better generation.
```

```text
Figure: 3 of 4 common resizing libraries alias by default
Owner:  Parmar et al. 2022 (2104.11222)
Scope:  PyTorch-FID, TensorFlow-FID, and OpenCV alias with default flags; only PIL
        adapts its filter width. This is the scope of the incomparability, not a
        surveyed count of published papers, which the paper does not give as a number.
```

```text
Figure: FID is linear in 1/N; two identical DCGAN runs swap rank as N changes
Owner:  Chong & Forsyth 2020 (1911.07023), Figures 2-4
Scope:  N = number of generated samples. FID decreases as N grows and the bias size
        depends on the model, so "No comparison that uses FID_N is reliable." The
        effect is a slope and a rank reversal, not a single quotable point delta.
```

```text
Figure: sample size "usually above 50K"
Owner:  Borji 2021 (2103.09396), citing common practice
Scope:  The generated-sample count practitioners use to keep FID's bias small;
        smaller sizes over-estimate FID. A denominator readers can anchor the bias to.
```

## Source assets

```text
Asset: Kynkaanniemi et al. 2023, Figure 7 (uncurated FFHQ samples, Projected FastGAN
       beside StyleGAN2, with each model's FID and CLIP-distance printed).
Shows: Two models a reader would call tied on FID, with the FastGAN faces visibly more
       distorted. The single clearest picture of FID misleading on a real comparison.
Crop:  Keep enough face samples from both models to see the distortion difference, and
       keep both FID numbers legible. Do not crop to one model.
```

```text
Asset: Parmar et al. 2022, Table 1 (FID of each resizing implementation vs correct
       PIL-bicubic).
Shows: How far the number moves from resizing code alone, before any model is judged.
Crop:  Retain the library names and their FID gaps together; the pairing is the point.
```

```text
Asset: Chong & Forsyth 2020, Figure 3 (two DCGAN runs whose FID rank flips with N).
Shows: The same two models trading places as sample count changes, which is the
       sample-size failure in one image.
Crop:  Keep both curves and the crossover; a single curve loses the reversal.
```

```text
Asset: Heusel et al. 2017, Appendix A1 disturbance plots (FID rising with each of six
       degradation levels).
Shows: The defense in one image: FID climbs monotonically as real images are damaged.
Crop:  Keep the axis labels and at least one full disturbance series so the monotonic
       rise is readable.
```

## Discarded

```text
URL: https://arxiv.org/abs/1802.03446 (Borji, "Pros and Cons of GAN Evaluation
     Measures," 2018): superseded for this record by the 2021 "New Developments"
     version (2103.09396), which carries the same FID characterization and later
     metrics. Cite the newer one to avoid two retellings of one author's survey.
```

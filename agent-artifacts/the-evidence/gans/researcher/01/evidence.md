# Evidence: the-evidence/gans (01)

The commissioned angle holds up firsthand. The 2014 paper "Generative
Adversarial Nets" was read in full from the arXiv PDF, and every load-bearing
claim about what it actually did is confirmed by the paper itself: it trained on
MNIST, the Toronto Face Database, and CIFAR-10; it evaluated with a Gaussian
Parzen-window log-likelihood estimate plus eyeballed sample panels; it printed
exactly four numbers of quantitative result (two of them the adversarial model's);
and it stated its own caveat that the metric "has somewhat high variance and does
not perform well in high dimensional spaces." Its theoretical result (global
optimum at pg = pdata, value -log 4) is explicitly proven only in the
non-parametric / infinite-capacity limit, and the paper itself flags that its
real MLP generators carry "no theoretical guarantees" and can collapse ("the
Helvetica scenario"). The one resolution the commission leans on, "blurry 32x32,"
is the CIFAR-10 native resolution, confirmed from the dataset owner's page; note
that the paper text never prints any resolution, so all resolutions come from the
datasets, not from the paper. The "brought to the present" claims are well
supported by primary papers: photoreal 1024x1024 faces are documented at 2017
(Progressive GANs) and 2018/2019 (StyleGAN), three to five years after 2014, and
diffusion models are documented overtaking GANs on image synthesis by 2021. The
record is thin in two places: the exact live citation count comes from Google
Scholar only (Semantic Scholar's API rate-limited every attempt), and MNIST
(28x28) and TFD (48x48) resolutions could not be reconfirmed from a resolving
canonical page this session, though CIFAR-10's 32x32 was. Nothing found undermines
the commissioned angle; one nuance qualifies it (the later photoreal lineage is
genuine GAN descent, so the paper is a correct origin, just not the artifact),
recorded under Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/1406.2661
Kind:        primary. It is the paper the article is about; it owns every claim
             about what GANs did and reported in 2014. (PDF read in full at
             https://arxiv.org/pdf/1406.2661 ; abstract landing page is the
             canonical home.)
Establishes: Title as printed on the paper: "Generative Adversarial Nets."
             Authors in order: Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi
             Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville,
             Yoshua Bengio. Affiliation: Departement d'informatique et de
             recherche operationnelle, Universite de Montreal, Montreal, QC.
             (Footnotes: Pouget-Abadie visiting from Ecole Polytechnique; Ozair
             visiting from IIT Delhi; Bengio a CIFAR Senior Fellow.) Submitted
             10 Jun 2014, [stat.ML], v1. Datasets: MNIST, Toronto Face Database
             (TFD), CIFAR-10. Evaluation: Gaussian Parzen-window log-likelihood
             plus qualitative sample panels. The minimax value function (Eq. 1),
             Proposition 1 (optimal discriminator), Theorem 1 (global optimum at
             pg = pdata, value -log 4), Proposition 2 (convergence under enough
             capacity), and the paper's own statements on training difficulty.
Paraphrase:  Two networks trained against each other: a generator G that turns
             noise into samples and a discriminator D that estimates whether a
             sample is real. G is trained to fool D. At the ideal solution G
             reproduces the data distribution and D outputs 1/2 everywhere. No
             Markov chains or inference networks are needed; both nets are MLPs
             trained by backprop. The paper proves the ideal solution exists in
             the space of arbitrary functions (infinite capacity), then shows
             samples from small nets on three datasets and one weak numerical
             score.
Locators:    Abstract and Sec. 1 (framing); Sec. 3, Eq. 1 (value function);
             Sec. 4.1, Prop. 1 (Eq. 2) and Thm. 1 (Eqs. 5-6); Sec. 4.2, Prop. 2;
             Sec. 5 and Table 1 (experiments, metric, numbers); Sec. 6 (Helvetica
             scenario); Figs. 2-3 (samples).
Quote:       Parzen-window caveat, verbatim: "This method of estimating the
             likelihood has somewhat high variance and does not perform well in
             high dimensional spaces but it is the best method available to our
             knowledge." (Sec. 5.)
             Metric setup, verbatim: "We estimate probability of the test set
             data under pg by fitting a Gaussian Parzen window to the samples
             generated with G and reporting the log-likelihood under this
             distribution." (Sec. 5.)
             Value function, verbatim: "min_G max_D V(D, G) =
             E_{x~pdata(x)}[log D(x)] + E_{z~pz(z)}[log(1 - D(G(z)))]." (Eq. 1.)
             Theorem 1, verbatim: "The global minimum of the virtual training
             criterion C(G) is achieved if and only if pg = pdata. At that point,
             C(G) achieves the value -log 4."
             Capacity assumption, verbatim: "The results of this section are done
             in a non-parametric setting, e.g. we represent a model with infinite
             capacity by studying convergence in the space of probability density
             functions." (Sec. 4.)
             Theory-practice gap, verbatim: "In practice, adversarial nets
             represent a limited family of pg distributions via the function
             G(z; theta_g), and we optimize theta_g rather than pg itself. Using
             a multilayer perceptron to define G introduces multiple critical
             points in parameter space. However, the excellent performance of
             multilayer perceptrons in practice suggests that they are a
             reasonable model to use despite their lack of theoretical
             guarantees." (Sec. 4.2.)
             Mode collapse, verbatim: G "must not be trained too much without
             updating D, in order to avoid 'the Helvetica scenario' in which G
             collapses too many values of z to the same value of x to have enough
             diversity to model pdata." (Sec. 6.)
             Sample honesty, verbatim (Fig. 2 caption): "Rightmost column shows
             the nearest training example of the neighboring sample, in order to
             demonstrate that the model has not memorized the training set.
             Samples are fair random draws, not cherry-picked."
             Non-saturating trick, verbatim: "Rather than training G to minimize
             log(1 - D(G(z))) we can train G to maximize log D(G(z))." (Sec. 3.)
```

```text
URL:         https://dblp.org/rec/conf/nips/GoodfellowPMXWOCB14.html
Kind:        secondary. Bibliographic index (dblp); reports the publication
             record, does not own the research.
Establishes: The venue and canonical citation: "Generative Adversarial Nets,"
             NIPS 2014, pages 2672-2680, same eight-author list. Confirms the
             published title is "Nets," not "Networks."
Paraphrase:  The paper was published in the NIPS 2014 proceedings (Advances in
             Neural Information Processing Systems 27), pp. 2672-2680.
Locators:    dblp record page, top entry.
```

```text
URL:         https://cave.cs.toronto.edu/kriz/cifar.html
Kind:        primary. The dataset owner's page (Alex Krizhevsky). Owns the
             CIFAR-10 specification. Note: the widely cited address
             www.cs.toronto.edu/~kriz/cifar.html 301-redirects here, so this is
             the source's current live home.
Establishes: CIFAR-10 is "60000 32x32 colour images in 10 classes." Created by
             Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton. This is the "32x32"
             the commission's "blurry 32x32 samples" refers to; the GAN paper's
             CIFAR-10 panels (Fig. 2c, 2d) are at this native resolution.
Paraphrase:  CIFAR-10: 60,000 colour images of 32x32 pixels across 10 classes,
             6,000 per class, split 50,000 train / 10,000 test.
Locators:    Page top, dataset description.
Quote:       "60000 32x32 colour images in 10 classes, with 6000 images per class."
```

```text
URL:         https://arxiv.org/abs/1511.06434
Kind:        primary. The DCGAN paper; owns its own architectural claims.
Establishes: "Unsupervised Representation Learning with Deep Convolutional
             Generative Adversarial Networks," Radford, Metz, Chintala; submitted
             19 Nov 2015 (v1). First stable convolutional GAN architecture; dated
             more than a year after the 2014 paper. Supports the "photorealism
             came later, not from the original paper" point as the first rung of
             the lineage. (Resolution/dataset specifics not stated in the
             abstract; do not attribute a specific resolution to this source.)
Paraphrase:  Introduces architectural constraints that make convolutional GANs
             train stably and learn reusable image representations. Positioned as
             bridging supervised-CNN success with unsupervised learning.
Locators:    arXiv abstract page; title, authors, date.
```

```text
URL:         https://arxiv.org/abs/1710.10196
Kind:        primary. The Progressive Growing of GANs paper; owns its result.
Establishes: "Progressive Growing of GANs for Improved Quality, Stability, and
             Variation," Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen;
             submitted 27 Oct 2017. Generates CelebA face images at 1024x1024
             (1024^2) and reports an Inception score of 8.80 on CIFAR-10. This is
             the primary anchor that megapixel photoreal faces are a 2017 result,
             three years after the 2014 paper.
Paraphrase:  Grows generator and discriminator progressively from low to high
             resolution during training, stabilizing training and reaching
             1024x1024 face synthesis; builds a higher-quality CelebA variant.
Locators:    arXiv abstract; resolution "1024^2" stated in abstract.
```

```text
URL:         https://arxiv.org/abs/1812.04948
Kind:        primary. The StyleGAN paper; owns its result.
Establishes: "A Style-Based Generator Architecture for Generative Adversarial
             Networks," Tero Karras, Samuli Laine, Timo Aila; submitted 12 Dec
             2018, last revised 29 Mar 2019 (CVPR 2019). Introduces a style-based
             generator producing high-quality human faces and a "new, highly
             varied and high-quality dataset of human faces" (FFHQ). This is the
             architecture behind the well-known photoreal "faces of people who do
             not exist," dated 2018/2019 -- four to five years after 2014.
             (Abstract does not state a pixel resolution; do not cite a specific
             resolution from this source. 1024x1024 is confirmed at ProGAN
             above.)
Paraphrase:  A generator borrowing from style-transfer that separates high-level
             attributes (pose, identity) from stochastic detail (freckles, hair)
             and improves face-image quality and disentanglement.
Locators:    arXiv abstract, read verbatim.
Quote:       "We introduce a new, highly varied and high-quality dataset of human
             faces." (Abstract.)
```

```text
URL:         https://arxiv.org/abs/2006.11239
Kind:        primary. The DDPM paper; owns its result.
Establishes: "Denoising Diffusion Probabilistic Models," Jonathan Ho, Ajay Jain,
             Pieter Abbeel; submitted 19 Jun 2020. A non-GAN (diffusion) image
             generator reaching FID 3.17 on CIFAR-10 and, on 256x256 LSUN,
             "sample quality similar to ProgressiveGAN." Supports that the
             leading image-generation lineage moved off GANs.
Paraphrase:  Diffusion probabilistic models produce high-quality images by
             learning to reverse a gradual noising process; competitive with the
             best GANs by 2020.
Locators:    arXiv abstract, read verbatim.
```

```text
URL:         https://arxiv.org/abs/2105.05233
Kind:        primary. The Dhariwal & Nichol paper; owns its comparative result.
Establishes: "Diffusion Models Beat GANs on Image Synthesis," Prafulla Dhariwal,
             Alex Nichol; submitted 11 May 2021. Reports diffusion FID of 2.97 on
             ImageNet 128x128, 4.59 on 256x256, 7.72 on 512x512, matching
             BigGAN-deep while covering the distribution better. The title and
             result are the strongest single primary source for the "diffusion
             superseded GANs" claim.
Paraphrase:  With architectural tuning and classifier guidance, diffusion models
             beat the best GANs on standard image-synthesis benchmarks.
Locators:    arXiv abstract, read verbatim.
Quote:       Title, verbatim: "Diffusion Models Beat GANs on Image Synthesis."
             "We achieve an FID of 2.97 on ImageNet 128x128, 4.59 on ImageNet
             256x256, and 7.72 on ImageNet 512x512, and we match BigGAN-deep even
             with as few as 25 forward passes per sample."
```

```text
URL:         https://scholar.google.com/scholar?q=Generative+Adversarial+Nets+Goodfellow+2014
Kind:        secondary. Citation index (Google Scholar); reports how often the
             paper is cited, does not own the paper.
Establishes: Fame magnitude. Google Scholar shows "Cited by 96878" for the paper.
             Read 2026-08-06. Use as an order-of-magnitude fame indicator
             (~97,000 citations), not a precise, stable figure.
Paraphrase:  The paper has on the order of ninety-plus thousand citations, among
             the most-cited works in machine learning.
Locators:    Google Scholar result row for the paper; "Cited by 96878" link.
```

## Contradictions

- Title discrepancy. The paper PDF, the NIPS proceedings, and dblp all title it
  "Generative Adversarial **Nets**." The current arXiv HTML landing page
  (arxiv.org/abs/1406.2661) renders the title as "Generative Adversarial
  **Networks**." The published/canonical title is "Nets"; the writer should use
  "Nets." Not a substantive conflict, but a name the headline could get wrong.

- The commissioned framing ("this paper made deepfakes") is complicated, not
  contradicted, by the lineage. The photoreal-face lineage (DCGAN 2015 -> ProGAN
  2017 -> StyleGAN 2018/2019) is genuine descent from the 2014 adversarial
  training idea, so the paper is a correct **origin** of the technique. What the
  fame overstates is the timeline and the artifact: the 2014 paper itself
  produced only small, blurry samples under a weak metric, and photorealism
  arrived three-to-five years later in other labs (Karras et al., NVIDIA). The
  honest distinction is origin-of-idea (true) vs. origin-of-photoreal-images
  (false), not "the credit is misplaced."

- A second complication cuts the other way on "GANs = today's image AI." Today's
  leading image generators are diffusion-based (DDPM 2020; "Diffusion Models Beat
  GANs" 2021), so the direct technical ancestor of current tools is not the GAN
  line. Adversarial training as an idea held up; GANs as the reigning image
  architecture did not. Both facts are primary-sourced above.

- Search-surfaced citation numbers disagree wildly (a search snippet said "2,278";
  scispace listed "48,407"; Google Scholar read live showed 96,878). Only the
  Google Scholar figure was read firsthand from a citation index. Treat the count
  as an order of magnitude (~90k+), not an exact number.

## Numbers

```text
Figure: 225 +/- 2   (adversarial nets, MNIST Parzen-window log-likelihood)
Owner:  GAN paper, Table 1
Scope:  Mean log-likelihood (nats) of test-set samples under a Gaussian Parzen
        window fit to generated samples; standard error of the mean across
        examples. Best in its column (vs DBN 138+/-2, Stacked CAE 121+/-1.6,
        Deep GSN 214+/-1.1).
```

```text
Figure: 2057 +/- 26   (adversarial nets, TFD Parzen-window log-likelihood)
Owner:  GAN paper, Table 1
Scope:  Mean log-likelihood (nats); standard error across dataset folds, sigma
        cross-validated per fold. NOT best in its column: Stacked CAE scores
        2110 +/- 50 on TFD. Use to show the metric did not even crown GANs on
        both datasets.
```

```text
Figure: -log 4  (== approximately -1.386)
Owner:  GAN paper, Theorem 1
Scope:  The value of the training criterion C(G) at the global optimum, reached
        only when pg = pdata. A theoretical result in the non-parametric/
        infinite-capacity limit, not a measured quantity.
```

```text
Figure: 32 x 32 pixels, colour  (CIFAR-10 native resolution)
Owner:  Krizhevsky, cave.cs.toronto.edu/kriz/cifar.html
Scope:  Resolution of the CIFAR-10 images the GAN paper's Fig. 2c/2d samples were
        generated at. The load-bearing "blurry 32x32" figure. Confirmed firsthand.
```

```text
Figure: 28 x 28 (MNIST), 48 x 48 (TFD)  -- dataset-standard, unverified this run
Owner:  MNIST: LeCun et al.; TFD: Susskind, Anderson, Hinton (UTML TR 2010-001)
Scope:  Standard resolutions of the other two datasets in the GAN paper. The GAN
        paper text prints NO resolutions. MNIST canonical page (yann.lecun.com)
        returned 503 this session; TFD not separately fetched. Use as
        "standard MNIST 28x28 / TFD 48x48," or lean on the confirmed CIFAR 32x32
        for the low-res point.
```

```text
Figure: 1024 x 1024  (Progressive GANs, CelebA faces)
Owner:  Karras et al., arXiv:1710.10196 (abstract, "1024^2")
Scope:  Maximum resolution of photoreal GAN faces, dated 2017. The gap figure:
        megapixel faces are three years after the 2014 paper.
```

```text
Figure: FID 2.97 / 4.59 / 7.72 on ImageNet 128/256/512
Owner:  Dhariwal & Nichol, arXiv:2105.05233 (abstract)
Scope:  Diffusion-model image-synthesis scores that beat/match the best GANs,
        2021. Supports the supersession claim; FID = Frechet Inception Distance,
        lower is better.
```

```text
Figure: ~96,878 citations  (Google Scholar, read 2026-08-06)
Owner:  Google Scholar citation index (secondary)
Scope:  Order-of-magnitude fame indicator for the 2014 paper. Not a precise or
        stable number; label as approximate and dated.
```

## Source assets

```text
Asset: Figure 2, the four generated-sample panels (GAN paper, Sec. 5, p. 6).
       a) MNIST digits, b) TFD faces, c) CIFAR-10 (fully connected model),
       d) CIFAR-10 (convolutional discriminator / deconvolutional generator).
Shows: Exactly what the 2014 paper produced -- crisp-ish small digits, blurry
       grayscale faces, and near-unrecognizable 32x32 colour CIFAR blobs. The
       single most persuasive visual for the fame-vs-evidence gap: this is the
       "generative-image revolution" at birth. The TFD panel also rebuts
       "faces of nonexistent people" -- these are blurry reproductions of a real
       face database, not novel photoreal identities.
Crop:  Keep the rightmost (yellow-bordered) column, which the caption identifies
       as the nearest real training example -- it is doing evidentiary work
       (showing the model did not memorize) and reads as intended only when
       paired with the generated columns beside it. Do not crop to only the best
       (MNIST) panel; the CIFAR panels carry the "blurry" point.
```

```text
Asset: Table 1, Parzen-window log-likelihood estimates (GAN paper, Sec. 5, p. 6).
Shows: The entire quantitative case for the paper is four numbers across two
       datasets against three baselines, under a metric the authors themselves
       call high-variance and poor in high dimensions -- and GANs do not even win
       on TFD. Conveys the thinness of the 2014 evidentiary foundation directly.
Crop:  Retain the column headers (MNIST, TFD) and the "Adversarial nets" row with
       its two competitors so the reader sees GANs lose one column. Keep the
       caption's note that the metric is the estimator, not exact likelihood.
```

```text
Asset: Figure 3, z-space interpolation of MNIST digits (GAN paper, p. 7).
Shows: Smooth morphing between generated digits as the input noise is
       interpolated -- evidence the generator learned a continuous space, not a
       lookup table. Useful only if the lesson touches "the model generalizes";
       secondary to Figs. 2 and Table 1.
Crop:  Full strip; it reads as a sequence.
```

```text
Asset: Figure 1, the pedagogical distribution diagram (GAN paper, p. 3).
Shows: How D and G distributions converge to pg = pdata. CAUTION: this is a
       mechanics illustration; the commission explicitly warns against drifting
       into a how-GANs-work tutorial (that is the-mechanics' beat). Note as
       available, but Figs. 2/Table 1 serve this lesson's argument better.
Crop:  n/a -- likely omit for this lesson.
```

## Discarded

```text
URL: https://api.semanticscholar.org/graph/v1/paper/arXiv:1406.2661 -- intended
     as a second citation-index source; returned HTTP 429 (rate-limited) on
     every attempt via WebFetch and via proxied curl. Citation magnitude rests
     on Google Scholar alone.
URL: https://www.semanticscholar.org/paper/.../86ee1835a56722b76564119437070782fc90eb19
     -- JS-rendered page returned empty body to WebFetch; no readable count.
URL: https://yann.lecun.com/exdb/mnist/ -- canonical MNIST page returned HTTP 503
     twice this session; MNIST 28x28 recorded as dataset-standard but unverified
     from a resolving page this run.
URL: scispace.com / bibsonomy / scirp search hits for citation counts -- not
     opened as sources; their citation figures ("48407", "2278") conflict and
     were not read from a citation index firsthand. Not used.
```

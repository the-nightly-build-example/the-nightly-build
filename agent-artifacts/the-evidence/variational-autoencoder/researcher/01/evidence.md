# Evidence: the-evidence/variational-autoencoder (01)

The governing primary, "Auto-Encoding Variational Bayes" (Kingma & Welling,
arXiv:1312.6114, v1 20 Dec 2013; ICLR 2014), was read in full from the paper's
own text, including all appendices. It fully supports the commission's method
core: the recognition/encoder model qφ(z|x) and generative/decoder model
pθ(x|z), the ELBO with its two terms (a KL regularizer toward the prior and an
expected reconstruction term), the reparameterization trick and the exact
gradient-variance problem it solved, the prior p(z) = N(0, I), and the honest
scale (MNIST and Frey Face, single-hidden-layer MLPs of 500 and 200 units, a CPU
run measured in minutes per million samples, results reported as the variational
lower bound and an MCMC estimate of the marginal likelihood, with no sample-
quality or FID claim anywhere in the paper). The present-day angle is well
supported for the latent-diffusion link (Rombach et al. state their autoencoder's
KL-regularized latent is "similar to a VAE") and for the VQ-VAE and beta-VAE
extensions, each read from its own paper. The angle's weakest joint is the word
"blurry": none of the primaries read here call VAE samples blurry in those words.
The claim is sound as a mechanism (an element-wise Gaussian likelihood averages
over the many outputs that could explain an input, so the reconstruction smooths;
Larsen et al. and Doersch establish this), but a writer must present "famously
blurry" as the field's shorthand for that mechanism, not as a quotation from any
one paper. One continuity discrepancy is recorded in Contradictions: the
commission names `the-evidence/gans` and `denoising-diffusion` as existing
lessons to link, but neither appears in the library snapshot available to this
role.

## Sources

```text
URL:         https://arxiv.org/abs/1312.6114
Kind:        primary — Kingma & Welling author the method (VAE/AEVB) and own every
             claim about it. Read from the paper's own full text (all appendices).
Establishes: The variational autoencoder. The encoder is a "recognition model"
             qφ(z|x), "a probabilistic encoder" that outputs a distribution over
             the code z; the decoder pθ(x|z) is "a probabilistic decoder". Training
             maximizes the variational lower bound (ELBO). The reparameterization
             trick makes the lower bound differentiable w.r.t. the encoder
             parameters φ. Prior is a "centered isotropic multivariate Gaussian
             pθ(z) = N(z; 0, I)". Named algorithms: the SGVB (Stochastic Gradient
             Variational Bayes) estimator and the AEVB (Auto-Encoding VB) algorithm.
             Authors: Diederik P. Kingma and Max Welling, Machine Learning Group,
             Universiteit van Amsterdam.
Paraphrase:  The lower bound (eq. 3) is L = -D_KL(qφ(z|x) || pθ(z)) + E_qφ(z|x)[log
             pθ(x|z)]. The paper's own gloss on the auto-encoder connection: the
             first term (the KL divergence of the approximate posterior from the
             prior) acts as a regularizer, and the second term is an expected
             negative reconstruction error. The problem the trick solves: the naive
             Monte Carlo gradient of the bound w.r.t. φ "exhibits very high variance
             and is impractical"; reparameterizing z as a deterministic function of
             an outside noise variable makes "the Monte Carlo estimate of the
             expectation differentiable w.r.t. φ". Reported results are the
             variational lower bound (Fig. 2, vs. wake-sleep) and an MCMC estimate
             of the marginal likelihood (Fig. 3, vs. wake-sleep and Monte Carlo EM).
             The paper reports no image-quality metric.
Locators:    Abstract; §2.2 (eqs. 1–3); §2.3–2.4 and eq. 7 gloss; §3 (eq. 10, the
             Gaussian worked case); §5 Experiments; Appendix B (closed-form KL);
             Appendix C (MLP encoders/decoders); §4 Related work.
Quote:       "This reparameterization is useful for our case since it can be used to
             rewrite an expectation w.r.t qφ(z|x) such that the Monte Carlo estimate
             of the expectation is differentiable w.r.t. φ." (§2.4)
             "z = μ + σε, where ε is an auxiliary noise variable ε ∼ N(0, 1)."
             (§2.4, univariate case; the VAE example in §3 uses z = μ + σ ⊙ ε,
             ε ∼ N(0, I).)
```

```text
URL:         https://arxiv.org/abs/1401.4082
Kind:        primary — Rezende, Mohamed & Wierstra author their own method
             (stochastic backpropagation) and own its claims. Read from the arXiv
             abstract page; method characterization cross-checked against the VAE
             paper's Related-work citation of it.
Establishes: An independent, near-simultaneous derivation of the same core idea.
             The paper introduces "stochastic back-propagation — rules for
             back-propagation through stochastic variables" for deep latent Gaussian
             models, with a recognition model acting as "a stochastic encoder of the
             data". Kingma & Welling themselves record the independence.
Paraphrase:  This is the second, separate 2013–14 paper to connect recognition
             models, directed generative models, and gradient-based variational
             inference through the same reparameterization move. v1 was submitted
             16 Jan 2014, about four weeks after the VAE paper's v1 (20 Dec 2013);
             published at ICML 2014.
Locators:    Abstract; and the VAE paper's §4 Related work.
Quote:       From the VAE paper, §4: "[RMW14] also make the connection between
             auto-encoders, directed pro[b]abilistic models and stochastic
             variational inference using the reparameterization trick we describe in
             this paper. Their work was developed independently of ours."
```

```text
URL:         https://arxiv.org/abs/1711.00937
Kind:        primary — van den Oord, Vinyals & Kavukcuoglu author the VQ-VAE.
             Read from the arXiv abstract page.
Establishes: The VQ-VAE, the discrete-latent extension the commission names. It
             "differs from VAEs in two key ways: the encoder network outputs
             discrete, rather than continuous, codes; and the prior is learnt rather
             than static," using vector quantization. Cited by the commission as the
             lineage that leads into latent-diffusion-style autoencoders.
Paraphrase:  Replacing the VAE's continuous Gaussian latent with a discrete code
             book and pairing it with a learned autoregressive prior lets the model
             generate high-quality images, video, and speech, and (the paper's own
             framing) sidesteps "posterior collapse" — where the latents are ignored
             when paired with a powerful autoregressive decoder.
Locators:    Abstract.
Quote:       "Using the VQ method allows the model to circumvent issues of 'posterior
             collapse' ... typically observed in the VAE framework."
```

```text
URL:         https://openreview.net/forum?id=Sy2fzU9gl
Kind:        primary — Higgins et al. author beta-VAE. NOTE: the OpenReview page is
             gated behind a browser-verification wall (not dead). The abstract text
             below was confirmed through the ICLR 2017 listing surfaced in search and
             a Semantic Scholar record; the verbatim page could not be fetched
             directly by this role. Flagged so the writer treats the quote as
             abstract-confirmed, not page-verified.
Establishes: beta-VAE, the disentanglement extension the commission names. It adds a
             single hyperparameter β that weights the KL term of the VAE objective;
             β = 1 is the standard VAE. Published at ICLR 2017; authors at DeepMind
             (Irina Higgins, Loïc Matthey, Arka Pal, Christopher Burgess, Xavier
             Glorot, Matthew Botvinick, Shakir Mohamed, Alexander Lerchner).
Paraphrase:  Turning up β past 1 pushes the latent distribution harder toward the
             factorized prior, trading reconstruction fidelity for more independent,
             interpretable latent factors ("disentanglement"). It is a one-knob
             modification of the same ELBO, which makes it a clean teaching example
             of what the KL term controls.
Locators:    Abstract.
Quote:       "an adjustable hyperparameter β that balances latent channel capacity
             and independence constraints with reconstruction accuracy" and "β-VAE
             with appropriately tuned β > 1 qualitatively outperforms VAE (β = 1)."
             (Abstract, as surfaced; not page-verified — see NOTE.)
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary — Rombach, Blattmann, Lorenz, Esser & Ommer author Latent
             Diffusion Models (the Stable Diffusion method). Abstract read from the
             arXiv page; §3.1 read from the paper's HTML rendering.
Establishes: The autoencoder's role in latent diffusion — the exact continuity hook
             the commission wants. The diffusion model runs "in the latent space of
             powerful pretrained autoencoders", and one of the two autoencoders they
             train is regularized "similar to a VAE".
Paraphrase:  An encoder E compresses an image x to a latent z = E(x) by a
             downsampling factor f, and a decoder D reconstructs it. They test two
             latent regularizers: KL-reg., "a slight KL-penalty towards a standard
             normal on the learned latent, similar to a VAE," and VQ-reg., a vector-
             quantization layer (a VQGAN with the quantizer folded into the decoder).
             This is the direct descendant line: the "autoencoder in latent
             diffusion" is a lightly-regularized VAE or a VQ-VAE-style model. This
             is the lesson the reader already met the word "autoencoder" in.
Locators:    Abstract; §3.1 "Perceptual Image Compression".
Quote:       "The first variant, KL-reg., imposes a slight KL-penalty towards a
             standard normal on the learned latent, similar to a VAE ... VQ-reg. uses
             a vector quantization layer within the decoder."
```

```text
URL:         https://arxiv.org/abs/1512.09300
Kind:        primary — Larsen, Sønderby, Larochelle & Winther author the VAE/GAN
             method and own the claim that the plain-VAE reconstruction objective is
             the wrong metric for images. Abstract read from arXiv; §1 and §2.3 read
             from the paper's own full text.
Establishes: Why plain-VAE samples look poor, at the mechanism level. The plain VAE
             uses an "element-wise Gaussian observation model," and element-wise
             (pixel/squared-error) metrics "are notoriously inadequate" for images
             because they ignore visual invariances. Their fix replaces the pixel-
             wise reconstruction term with a feature-wise error read from a GAN
             discriminator.
Paraphrase:  The paper's core motivation is that the VAE's expected-log-likelihood
             reconstruction term, evaluated pixel by pixel, does not match human
             perception (a small shift gives a large pixel error a person would
             barely notice), so it drives low-fidelity output. This is the sourced
             backbone under the commission's "blurry" characterization, stated as a
             mechanism rather than the word itself.
Locators:    Abstract; §1 (introduction); §2.3 "Beyond element-wise reconstruction
             error"; §4 (experiments, "Plain VAE with an element-wise Gaussian
             observation model").
Quote:       "we replace element-wise errors with feature-wise errors to better
             capture the data distribution" and "it outperforms VAEs with element-
             wise similarity measures in terms of visual fidelity" (Abstract);
             "element-wise reconstruction errors are not adequate for images and
             other signals with invariances" (§2.3).
```

```text
URL:         https://arxiv.org/abs/1511.06349
Kind:        primary — Bowman, Vilnis, Vinyals, Dai, Jozefowicz & Bengio author the
             first careful account of the failure now called posterior collapse.
             Abstract read from arXiv; §3.1 read from the paper's HTML rendering.
Establishes: Posterior collapse (a.k.a. KL vanishing), the failure the commission
             flags for Contradictions. With a strong (LSTM) decoder, the model drives
             the KL term to zero and ignores the latent, so the encoder buys nothing.
Paraphrase:  The paper documents that most runs set qφ(z|x) equal to the prior,
             zeroing the KL term, because the powerful decoder learns to model the
             data on its own and "ignore z". Their two fixes: "KL cost annealing"
             (ramp the KL weight up from zero during training) and "word dropout"
             (weaken the decoder so it must use z). This complicates the tidy ELBO
             story: the two terms can fall out of balance, and the balance is a known
             training problem, not an automatic property.
Locators:    Abstract; §3.1 "Optimization challenges".
Quote:       "most training runs ... consistently set q(z|x) equal to the prior p(z),
             bringing the KL divergence term of the cost function to zero." (§3.1)
```

```text
URL:         https://arxiv.org/abs/1606.05908
Kind:        secondary — Doersch was not an author of the VAE and reports on the
             method from outside. Abstract read from arXiv; the blur passage read
             from the paper's HTML rendering. Use for context only.
Establishes: An outside explanation of the blur mechanism, in teaching form. When a
             squared-error output model must cover several plausible outputs, its
             single output is a smeared average of them; the paper contrasts this
             blurred regression output against a conditional VAE that "picks a
             specific digit ... without blur." Useful as a plain-language mechanism
             for the writer, but it is a tutorial, not the owner of any result.
Paraphrase:  Doersch frames VAEs as the tool for one-to-many mappings, where many
             outputs are plausible and a model must produce a distribution to sample
             from. That framing supports the "learned latent space" reading; it does
             not itself measure sample quality.
Locators:    Abstract; §2 (blur-from-averaging discussion).
Quote:       "The blur in the regressor's output minimizes the distance to the set of
             many digits which might have produced the input. The CVAE, on the other
             hand, generally picks a specific digit to output and does so without
             blur."
```

```text
URL:         https://arxiv.org/abs/1906.00446
Kind:        primary — Razavi, van den Oord & Vinyals author VQ-VAE-2. Abstract read
             from arXiv; introduction read from the paper's HTML rendering.
Establishes: Where the discrete-latent line arrived: a VQ-VAE with scaled
             autoregressive priors generates ImageNet samples "that rivals that of
             state of the art Generative Adversarial Networks," sampling in the
             compressed latent space rather than pixel space. Supports the "valued as
             a latent space, not a standalone generator" reading of the lineage.
Paraphrase:  The fidelity gains come from a powerful learned prior over a discrete
             latent grid, not from the autoencoder alone. IMPORTANT LIMIT: this paper
             does not call VAE or likelihood-based samples "blurry" — its stated
             critique is that pixel-space NLL "is not always a good measure of sample
             quality," which is about the objective, not the word. Do not attribute
             the blur claim to it.
Locators:    Abstract; §1 (introduction).
Quote:       "generate samples with quality that rivals that of state of the art
             Generative Adversarial Networks on multifaceted datasets such as
             ImageNet."
```

## Contradictions

- Independent origin of the reparameterization trick. The commission asks whether
  the trick "originated independently elsewhere." It did, twice over. Kingma &
  Welling themselves credit Rezende, Mohamed & Wierstra (arXiv:1401.4082) as
  developing the same connection independently (VAE paper §4). The same section
  also cites Salimans & Knowles (2013) as having already used "a similar
  reparameterization" for stochastic variational inference, and cites Roweis
  (1998) and others for the older auto-encoder / linear-Gaussian connection. The
  honest line: Kingma & Welling gave the deep-latent-variable case its standard
  training recipe and name, but the pathwise/reparameterization idea was in the
  air and was co-discovered. A lesson that credits the trick solely to this paper
  overstates it; the paper itself is more careful than the popular telling.

- "Blurry" is a field characterization, not a primary quotation. No paper read
  here (the VAE paper, Larsen, VQ-VAE, VQ-VAE-2, Doersch) states in those words
  that VAE samples are blurry. Larsen supplies the mechanism (element-wise metrics
  are inadequate for images; plain VAEs lose visual fidelity) and Doersch supplies
  the intuition (squared-error output averages plausible outputs). The claim is
  well-grounded as a mechanism but must not be quoted to a source as a verdict.

- Posterior collapse cuts against the clean two-term story. The commission's ELBO
  narrative (a reconstruction term balanced against a KL term) is correct as the
  objective, but Bowman et al. and the VQ-VAE paper both document that the balance
  is fragile: a strong decoder can drive the KL term to zero and ignore the latent
  entirely. VQ-VAE's discrete latent is presented partly as an escape from this.
  The two-term picture should be taught with the caveat that the terms can collapse
  into each other in practice.

- Library-continuity discrepancy (for the orchestrator, not the reader). The
  commission states the library "teaches GANs (the-evidence/gans) and diffusion
  (denoising-diffusion, latent-diffusion)" and instructs the writer to link
  `gans`, `denoising-diffusion`, and `latent-diffusion` in Background. The library
  snapshot available to this role (via `nb history` on the provided checkout)
  contains `the-evidence/latent-diffusion` (2026-09-11; its own dek is "Stable
  Diffusion does its denoising on a compressed grid, not the full image," tagged
  `autoencoder` — this is the exact lesson where the reader met "autoencoder") and
  `the-instruments/inception-score` (GAN evaluation), but shows no `the-evidence/
  gans` and no `denoising-diffusion` lesson. Either the snapshot is partial or
  those two lessons are not published. The writer must confirm a lesson exists
  before linking it; a Background link to a nonexistent lesson should not ship.
  Owner of the resolution: the orchestrator / commission.

## Numbers

```text
Figure: v1 submitted 20 Dec 2013; published at ICLR 2014
Owner:  arXiv:1312.6114 (Kingma & Welling)
Scope:  Submission and venue of the governing paper. The "2013/2014" split is real:
        arXiv 2013, conference 2014.
```

```text
Figure: MNIST models: 500 hidden units; Frey Face models: 200 hidden units
Owner:  arXiv:1312.6114, §5 ("Likelihood lower bound")
Scope:  Per network, single hidden layer (MLP). Encoder and decoder have an equal
        number of hidden units. 200 for Frey Face specifically to limit overfitting
        on the smaller dataset.
```

```text
Figure: Marginal-likelihood experiment: 100 hidden units, 3 latent variables
Owner:  arXiv:1312.6114, §5 ("Marginal likelihood")
Scope:  A separate, deliberately tiny model, because the MCMC marginal-likelihood
        estimator is only reliable for low-dimensional latent spaces (< 5 dims).
```

```text
Figure: Latent-space dimensionalities tested (Nz): MNIST {3, 5, 10, 20, 200};
        Frey Face {2, 5, 10, 20}
Owner:  arXiv:1312.6114, Figs. 2 and 3
Scope:  The dimensionalities swept when comparing the lower bound and marginal
        likelihood. Not a single headline number; the full sweep.
```

```text
Figure: Minibatch M = 100; samples per datapoint L = 1
Owner:  arXiv:1312.6114, Algorithm 1 and §5
Scope:  Training configuration. L = 1 was found sufficient given a large enough
        minibatch.
```

```text
Figure: ~20–40 minutes per million training samples
Owner:  arXiv:1312.6114, Fig. 2 caption
Scope:  Wall-clock on a single Intel Xeon CPU at an effective 40 GFLOPS. This is
        the honest-scale anchor: a 2013 CPU experiment, not a GPU cluster.
```

```text
Figure: Marginal likelihood estimated on the first 1000 train and 1000 test points;
        50 posterior samples per point via Hybrid Monte Carlo (4 leapfrog steps)
Owner:  arXiv:1312.6114, Appendix D / E
Scope:  The evaluation subset and estimator. Small subset, MCMC-based.
```

```text
Figure: ELBO = -D_KL(qφ(z|x) || pθ(z)) + E_qφ(z|x)[log pθ(x|z)]; prior p(z) = N(0, I)
Owner:  arXiv:1312.6114, eq. 3 and §3
Scope:  The objective the whole method optimizes and the fixed, parameter-free prior.
```

```text
Figure: Gaussian-case KL, closed form: (1/2) Σ_j (1 + log(σ_j²) − μ_j² − σ_j²)
Owner:  arXiv:1312.6114, eq. 10 and Appendix B
Scope:  The exact KL term when prior and approximate posterior are Gaussian. Usable
        as the lesson's worked example: it needs no sampling, only encoder outputs
        μ and σ.
```

```text
Figure: Latent-diffusion downsampling factors f tested ∈ {1, 2, 4, 8, 16, 32}
Owner:  arXiv:2112.10752, §3.1 / §4
Scope:  The compression factors swept for the autoencoder; f = 4 and f = 8 reported
        as the useful balance. Context for how much the autoencoder compresses.
```

## Source assets

```text
Asset: Figure 5, "Random samples from learned generative models of MNIST for
       different dimensionalities of latent space" (arXiv:1312.6114, Appendix A)
Shows: The paper's own generated samples — small, imperfect MNIST digits at Nz =
       2, 5, 10, 20. The single most honest artifact for "this was a proof of
       method, not photorealism": the reader sees exactly what 2013 VAE samples
       looked like.
Crop:  Keep the panel labels (2-D / 5-D / 10-D / 20-D) so the latent-dimension
       comparison survives. Do not crop to a single digit; the grid is the point.
```

```text
Asset: Figure 4, "Visualisations of learned data manifold ... two-dimensional
       latent space" for Frey Face and MNIST (arXiv:1312.6114, Appendix A)
Shows: The smooth 2D latent manifold — faces morphing across expression/pose, and
       digit shapes sweeping continuously. This is the visual case for "valued as a
       learned latent space": nearby codes decode to similar data.
Crop:  Retain enough of the grid to show continuity across the manifold. The Frey
       Face panel reads faster than MNIST for a lay reader.
```

```text
Asset: Figure 2, lower-bound convergence curves, AEVB vs. wake-sleep, per Nz
       (arXiv:1312.6114, §5)
Shows: What the paper actually reported: the variational lower bound over training,
       AEVB converging faster and higher than wake-sleep. Anchors "the reported
       result was a likelihood bound, not an image score."
Crop:  Axes must stay legible — vertical axis is the estimated average lower bound
       per datapoint, horizontal is training points evaluated. Keep the legend.
```

```text
Asset: Perceptual-compression / autoencoder-plus-latent-diffusion pipeline figure
       (arXiv:2112.10752, Figure 3 area, §3)
Shows: Where the descendant autoencoder sits: image → encoder → latent grid →
       diffusion in latent space → decoder → image. Carries the continuity link to
       the latent-diffusion lesson better than prose.
Crop:  Keep the encoder/decoder boxes and the latent-space label; the pixel-vs-
       latent distinction is the whole reason to show it.
```

```text
Asset: Plain-VAE vs. VAE/GAN reconstruction comparison (arXiv:1512.09300, results
       figures, §4)
Shows: Side-by-side faces where the element-wise plain VAE is visibly softer than
       the feature-metric model. The clearest visual evidence for the mechanism
       behind "blurry."
Crop:  Must retain the labeled columns (plain VAE vs. VAE/GAN) or the comparison is
       lost. If licensing on this figure is a concern, the VAE paper's own Fig. 5
       already carries the low-fidelity point without a third-party image.
```

## Discarded

```text
URL: https://openreview.net/pdf?id=Sy2fzU9gl — repeatedly returned OpenReview's
     browser-verification wall, not the PDF. The forum URL is retained as the
     source's own page (see the beta-VAE Sources entry and its NOTE); this PDF
     route is discarded as a transport failure, not a dead source.
URL: https://www.semanticscholar.org/paper/6f7af4709e399e89ba898efc3459cb844fa0e981
     — aggregator page, returned empty on fetch and rate-limited on API. Used only
     to locate the beta-VAE record; not cited as a source (secondary metadata, not
     the owner of any claim).
URL: https://scispace.com/papers/beta-vae-... — aggregator, returned empty. Same
     reason: locating only, not a source.
URL: https://ar5iv.labs.arxiv.org/html/1512.09300 — the HTML rendering of Larsen
     et al. would not return body text; the paper was instead read from its own
     full text. Not a separate source, just an unusable transport for one paper.
```

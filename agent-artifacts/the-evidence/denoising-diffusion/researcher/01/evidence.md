# Evidence: the-evidence/denoising-diffusion (01)

The evidence firmly supports the article's core move: separating what the 2020
DDPM paper actually did from what today's "diffusion model" does. Read directly,
the paper is unconditional (no text, no class labels), operates in pixel space
(not a latent space), samples through a Markov chain of T=1000 sequential network
evaluations, and reports its headline results on 32x32 CIFAR-10 and 256x256
LSUN/CelebA-HQ. Every "did not do" claim in the brief is confirmed against the
paper itself, not a later summary. The lineage is also clean: the paper openly
credits Sohl-Dickstein et al. 2015 for the diffusion idea and Song & Ermon 2019
for the score-matching/Langevin connection, and states its own contribution as
the first demonstration that diffusion models generate high-quality samples. The
successor papers (latent diffusion, classifier-free guidance, DDIM, DALL-E 2,
Imagen) each add one specific missing capability, verified from their own
abstracts. The record is thin in two honest places: exact author affiliations did
not render on the arXiv abstract page (I record UC Berkeley from the paper's own
title block, which is well documented but was not re-fetched from the PDF here),
and one comparison figure in DDPM Table 1 (a "Sparse Transformer" FID of 2.80)
came back ambiguously labeled, so I do not treat it as load-bearing. The angle is
not undermined, but the "founding document" framing needs the precise gloss
below: DDPM founded the modern *image-generation* wave of diffusion, not
diffusion itself.

## Sources

```text
URL:         https://arxiv.org/abs/2006.11239
Kind:        primary. The document the lesson teaches; its authors own every
             method and result claim in it.
Establishes: Exact identity of the paper; the forward/reverse diffusion method;
             the epsilon-prediction simplified objective; T=1000; the datasets,
             resolutions, and quality scores; that all generation is
             unconditional and in pixel space; the sampling cost; and the credit
             it gives to prior work.
Paraphrase:  "Denoising Diffusion Probabilistic Models" by Jonathan Ho, Ajay
             Jain, and Pieter Abbeel. arXiv:2006.11239, submitted 19 June 2020
             (v1), revised 16 December 2020 (v2); published at NeurIPS 2020.
             Abstract: "We present high quality image synthesis results using
             diffusion probabilistic models, a class of latent variable models
             inspired by considerations from nonequilibrium thermodynamics. Our
             best results are obtained by training on a weighted variational
             bound designed according to a novel connection between diffusion
             probabilistic models and denoising score matching with Langevin
             dynamics... On the unconditional CIFAR10 dataset, we obtain an
             Inception score of 9.46 and a state-of-the-art FID score of 3.17.
             On 256x256 LSUN, we obtain sample quality similar to
             ProgressiveGAN."
             Method: a fixed forward Markov chain adds Gaussian noise over T
             steps, q(x_t | x_{t-1}) = N(x_t; sqrt(1-beta_t) x_{t-1}, beta_t I),
             with variances set "to constants increasing linearly from
             beta_1 = 10^-4 to beta_T = 0.02." A learned reverse process
             p_theta removes the noise step by step. The network is "a U-Net
             backbone similar to an unmasked PixelCNN++ with group normalization
             throughout," with self-attention at the 16x16 feature-map
             resolution and sinusoidal timestep embeddings; ~35.7M parameters
             for CIFAR-10, ~114M for the 256x256 models. The paper reparam-
             eterizes the reverse process so the network predicts the added
             noise epsilon, giving the simplified objective
             L_simple = E_{t,x_0,eps}[ || eps - eps_theta(sqrt(a_bar_t) x_0 +
             sqrt(1-a_bar_t) eps, t) ||^2 ]. Algorithm 1 (Training): sample x_0,
             sample t ~ Uniform{1..T}, sample eps ~ N(0,I), take a gradient step
             on the L_simple integrand. Algorithm 2 (Sampling): start from
             x_T ~ N(0,I); for t = T..1 compute
             x_{t-1} = (1/sqrt(alpha_t)) (x_t - ((1-alpha_t)/sqrt(1-a_bar_t))
             eps_theta(x_t,t)) + sigma_t z, adding fresh noise z until the last
             step. On the "did not do" questions: generation is unconditional
             ("the unconditional CIFAR10 dataset"), directly in pixel space, and
             requires the full T=1000-step chain, one network evaluation per
             step.
Locators:    Abstract; Sec. 2 (forward/reverse process); Sec. 3.2 and Eq. for
             L_simple; Algorithm 1 and Algorithm 2 boxes; Sec. 4 (Experiments),
             Table 1 (CIFAR-10) and Table 3 (LSUN); Appendix B (architecture,
             T=1000, beta schedule, sampling timing).
Quote:       "We set the forward process variances to constants increasing
             linearly from beta_1 = 10^-4 to beta_T = 0.02."
             "On the unconditional CIFAR10 dataset, we obtain an Inception score
             of 9.46 and a state-of-the-art FID score of 3.17."
             "To the best of our knowledge, there has been no demonstration that
             they are capable of generating high quality samples. We show that
             diffusion models actually are capable of generating high quality
             samples."
```

```text
URL:         https://arxiv.org/abs/1503.03585
Kind:        primary. The paper that first defined diffusion probabilistic
             models; its authors own the original method.
Establishes: That the diffusion generative idea (destroy structure with a
             forward diffusion process, learn the reverse to rebuild it)
             predates DDPM by five years, and that DDPM did not invent diffusion.
Paraphrase:  "Deep Unsupervised Learning using Nonequilibrium Thermodynamics" by
             Jascha Sohl-Dickstein, Eric A. Weiss, Niru Maheswaranathan, and
             Surya Ganguli. arXiv:1503.03585, submitted 12 March 2015 (ICML
             2015). Introduces the approach of "systematically and slowly
             destroy[ing] structure in a data distribution through an iterative
             forward diffusion process," then learning a reverse diffusion
             process that restores structure, yielding a tractable generative
             model. This is the framework DDPM builds on; DDPM's contribution is
             showing it can produce high-quality images, which this paper did not
             demonstrate.
Locators:    Abstract; introduction (forward/reverse diffusion framing).
Quote:       "systematically and slowly destroy structure in a data distribution
             through an iterative forward diffusion process."
```

```text
URL:         https://arxiv.org/abs/1907.05600
Kind:        primary. The score-based generative modeling paper DDPM connects
             to; its authors own the annealed-Langevin/score-matching method.
Establishes: The immediate technical predecessor DDPM unifies with: estimating
             the score at multiple noise levels and sampling by annealed Langevin
             dynamics. Its CIFAR-10 Inception Score (8.87) is the mark DDPM
             surpassed.
Paraphrase:  "Generative Modeling by Estimating Gradients of the Data
             Distribution" by Yang Song and Stefano Ermon (Stanford).
             arXiv:1907.05600, submitted 12 July 2019; NeurIPS 2019 (oral).
             Introduces score-based models (NCSN): perturb data with several
             Gaussian noise levels, estimate the score (gradient of log density)
             jointly across levels with score matching, and sample with annealed
             Langevin dynamics from high to low noise. Reports a then-state-of-
             the-art CIFAR-10 Inception Score of 8.87. DDPM Table 1 lists NCSN at
             IS 8.87 and FID 25.32, the baseline DDPM beat on FID by a wide
             margin.
Locators:    Abstract; results (CIFAR-10 Inception Score).
Quote:       "a new state-of-the-art inception score of 8.87 on CIFAR-10."
```

```text
URL:         https://arxiv.org/abs/2010.02502
Kind:        primary. The DDIM paper; its authors own the faster sampler.
Establishes: The specific capability DDPM lacked and this added: high-quality
             samples in far fewer steps via a non-Markovian, deterministic
             sampling process, without retraining.
Paraphrase:  "Denoising Diffusion Implicit Models" by Jiaming Song, Chenlin
             Meng, Stefano Ermon (Stanford). arXiv:2010.02502, submitted 6
             October 2020 (after DDPM); ICLR 2021. Keeps DDPM's training
             procedure but constructs a class of non-Markovian diffusion
             processes with the same objective whose reverse process samples
             much faster. Claims samples "10x to 50x faster in terms of
             wall-clock time compared to DDPMs." This directly addresses DDPM's
             ~1000-step sampling cost.
Locators:    Abstract.
Quote:       "DDIMs can produce high quality samples 10x to 50x faster in terms
             of wall-clock time compared to DDPMs."
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. The Latent Diffusion Models paper; basis of Stable
             Diffusion. Its authors own the latent-space and cross-attention
             method.
Establishes: Two capabilities DDPM lacked: running diffusion in a compressed
             latent space (cutting compute, enabling high resolution) and
             cross-attention conditioning for text-to-image and other inputs.
Paraphrase:  "High-Resolution Image Synthesis with Latent Diffusion Models" by
             Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser,
             Bjoern Ommer. arXiv:2112.10752, submitted 20 December 2021; CVPR
             2022. Applies diffusion "in the latent space of powerful pretrained
             autoencoders" instead of directly on pixels, reducing compute while
             keeping quality, and introduces "cross-attention layers into the
             model architecture" to condition on text, bounding boxes, and other
             inputs. This is the model Stable Diffusion is built from.
Locators:    Abstract.
Quote:       "apply them in the latent space of powerful pretrained
             autoencoders"; "cross-attention layers into the model
             architecture."
```

```text
URL:         https://arxiv.org/abs/2207.12598
Kind:        primary. The classifier-free guidance paper; its authors own the
             guidance method.
Establishes: The capability DDPM lacked: a way to strengthen conditioning and
             trade sample quality against diversity, without a separate
             classifier.
Paraphrase:  "Classifier-Free Diffusion Guidance" by Jonathan Ho and Tim
             Salimans (Google Research). arXiv:2207.12598, posted 26 July 2022;
             the work first appeared at the NeurIPS 2021 Workshop on Deep
             Generative Models (December 2021). Jointly trains a conditional and
             an unconditional diffusion model and combines their score estimates
             at sampling time to "attain a trade-off between sample quality and
             diversity similar to that obtained using classifier guidance,"
             without training a separate image classifier. It is the technique
             that makes text prompts "stick" strongly in modern systems.
Locators:    Abstract.
Quote:       "in what we call classifier-free guidance, we jointly train a
             conditional and an unconditional diffusion model, and we combine the
             resulting conditional and unconditional score estimates."
```

```text
URL:         https://arxiv.org/abs/2204.06125
Kind:        primary. The DALL-E 2 / unCLIP paper; OpenAI authors own the
             system.
Establishes: The capability DDPM lacked: text-to-image generation, using a
             diffusion decoder conditioned on CLIP image embeddings derived from
             a text caption, at high resolution.
Paraphrase:  "Hierarchical Text-Conditional Image Generation with CLIP Latents"
             by Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, Mark
             Chen (OpenAI). arXiv:2204.06125, submitted 13 April 2022. Two-stage
             model: a prior generates a CLIP image embedding from a text caption,
             and a diffusion decoder generates the image from that embedding.
             "We use diffusion models for the decoder and experiment with both
             autoregressive and diffusion models for the prior." This is the
             research behind the DALL-E 2 product.
Locators:    Abstract.
Quote:       "a prior that generates a CLIP image embedding given a text caption,
             and a decoder that generates an image conditioned on the image
             embedding... We use diffusion models for the decoder."
```

```text
URL:         https://arxiv.org/abs/2205.11487
Kind:        primary. The Imagen paper; Google authors own the system and its
             reported score.
Establishes: A second text-to-image approach DDPM lacked: a large frozen
             pretrained text-only language model as the text encoder feeding
             cascaded diffusion models, with a strong COCO FID.
Paraphrase:  "Photorealistic Text-to-Image Diffusion Models with Deep Language
             Understanding" (Imagen) by Chitwan Saharia, William Chan, and others
             at Google Research. arXiv:2205.11487, submitted 23 May 2022; NeurIPS
             2022. Uses a frozen T5-XXL language model as the text encoder into a
             cascade of diffusion models. Finds "generic large language models
             (e.g. T5), pretrained on text-only corpora, are surprisingly
             effective at encoding text for image synthesis," and reports a
             zero-shot COCO FID of 7.27.
Locators:    Abstract.
Quote:       "generic large language models (e.g. T5), pretrained on text-only
             corpora, are surprisingly effective at encoding text for image
             synthesis."
```

```text
URL:         https://en.wikipedia.org/wiki/Stable_Diffusion
Kind:        secondary. Reference summary reporting on the Stable Diffusion
             product from outside the model's authors. Used only for product
             timeline/context, not for any method claim.
Establishes: That Stable Diffusion, built on the Latent Diffusion Models paper,
             was released publicly on 22 August 2022 and can run on consumer
             GPUs. This dates the moment text-to-image diffusion reached the
             general public.
Paraphrase:  Reports Stable Diffusion's public release as 22 August 2022,
             developed by the CompVis group at LMU Munich with Runway and
             released by Stability AI, based on the Rombach et al. Latent
             Diffusion Models paper, trained at 512x512, and runnable on modest
             consumer GPUs.
Locators:    Infobox (release date); body (origins, resolution, hardware).
Quote:       "an optimized version can run on most consumer hardware equipped
             with a modest GPU with as little as 2.4 GB VRAM."
```

## Contradictions

- **The "founding document" framing needs a precise gloss.** DDPM did not invent
  diffusion. The paper itself credits Sohl-Dickstein et al. 2015 for diffusion
  probabilistic models and Song & Ermon 2019 for the score-matching/Langevin
  connection it unifies with. DDPM's own stated contribution is narrower and
  exact: it was the first to show diffusion models "are capable of generating
  high quality samples." So the honest claim is that DDPM founded the modern
  image-generation wave of diffusion, not diffusion as an idea. This does not
  break the article's angle (which is precisely about separating 2020 from
  today), but a headline or sentence calling it "the paper that invented
  diffusion" would be wrong by the paper's own text.

- **DDIM post-dates DDPM by months, not years.** DDIM (arXiv 6 October 2020) is a
  successor to DDPM (19 June 2020) but appeared the same year. If the article
  implies a long gap before fast sampling arrived, that is imprecise: the fast-
  sampling answer was already public within four months.

- **Classifier-free guidance's date is ambiguous.** The arXiv posting is 26 July
  2022, but the work first appeared at a NeurIPS 2021 workshop in December 2021.
  "Ho & Salimans 2022" (per the brief) matches the arXiv posting; if the article
  wants the earliest public date, it is late 2021.

- **No contradiction found on the core "did not do" claims.** Unconditional
  generation, pixel space, and T=1000-step sampling are all stated in the DDPM
  paper directly, not inferred from later summaries. The search for a
  counter-example (any conditional or latent or few-step result inside the 2020
  paper) found none.

## Numbers

```text
Figure: T = 1000 diffusion steps
Owner:  DDPM (Ho, Jain, Abbeel 2020)
Scope:  "We set T=1000 for all experiments." One network evaluation per step at
        sampling, run sequentially.
```

```text
Figure: variance schedule beta_1 = 1e-4 to beta_T = 0.02, linear
Owner:  DDPM
Scope:  Fixed forward-process noise schedule across all T=1000 steps.
```

```text
Figure: CIFAR-10 Inception Score 9.46 (+/- 0.11)
Owner:  DDPM, Table 1
Scope:  Unconditional CIFAR-10, 32x32 color images. Higher is better.
```

```text
Figure: CIFAR-10 FID 3.17
Owner:  DDPM, Table 1
Scope:  Unconditional CIFAR-10, 32x32. State-of-the-art at publication (lower is
        better). For scale, DDPM lists StyleGAN2+ADA (a leading GAN) at IS 9.74 /
        FID 3.26 on the same task, and NCSN (Song & Ermon 2019) at IS 8.87 / FID
        25.32.
```

```text
Figure: LSUN 256x256 FID: Bedroom 4.90, Church 7.89, Cat 19.75
Owner:  DDPM, Table 3
Scope:  Unconditional generation, 256x256. Abstract summarizes this as "sample
        quality similar to ProgressiveGAN" on 256x256 LSUN.
```

```text
Figure: model size ~35.7M parameters (CIFAR-10); ~114M parameters (256x256
        LSUN / CelebA-HQ)
Owner:  DDPM, Appendix B
Scope:  The U-Net backbone parameter counts.
```

```text
Figure: sampling a batch of 128 images takes ~300 seconds
Owner:  DDPM, Appendix B
Scope:  On the authors' 2020 hardware (specific GPU not stated in the fetched
        text); ~2.3 s per image. Illustrates the practical cost of the 1000-step
        chain.
```

```text
Figure: DDIM sampling 10x to 50x faster than DDPM
Owner:  DDIM (Song, Meng, Ermon 2021)
Scope:  Wall-clock time, same trained model, fewer sampling steps.
```

```text
Figure: Imagen zero-shot COCO FID 7.27
Owner:  Imagen (Saharia et al. 2022)
Scope:  256x256 text-to-image, evaluated on COCO without training on it. Cited
        only to show later text-to-image quality; not a DDPM number.
```

```text
Figure: Stable Diffusion public release 22 August 2022; default 512x512;
        runnable on a consumer GPU (as little as 2.4 GB VRAM in an optimized
        build)
Owner:  Wikipedia (secondary), reporting the Stability AI / CompVis release
Scope:  Product/timeline context, not a method claim.
```

## Source assets

```text
Asset: Algorithm 1 (Training) and Algorithm 2 (Sampling) boxes in the DDPM paper
       (Section 3.2 / adjacent).
Shows: The entire method in a few lines each. Training: add random noise at a
       random step, predict it. Sampling: start from noise, subtract predicted
       noise step by step. A lesson could teach the mechanism directly from
       these two boxes.
Crop:  A crop must keep both algorithm boxes together, or each in full with its
       numbered steps intact; omit surrounding derivation prose. Do not split a
       box across the fold.
```

```text
Asset: The forward/reverse Markov-chain schematic (Figure 2 in DDPM), the
       directed graphical model showing x_0 ... x_T with the forward q arrows
       adding noise and the reverse p_theta arrows removing it.
Shows: The two-direction structure at a glance: a fixed corruption chain and a
       learned recovery chain. Anchors the plain-language "add noise, then learn
       to undo it" explanation.
Crop:  Keep the full x_0-to-x_T chain and both arrow directions with their q and
       p_theta labels; do not crop to a single step, which loses the "over many
       steps" point.
```

```text
Asset: CIFAR-10 / CelebA-HQ / LSUN generated-sample grids (Figure 1 and the
       256x256 sample figures), shown with their Table 1 / Table 3 scores.
Shows: The actual output quality and the exact scale the paper reached: 32x32 on
       CIFAR-10, 256x256 on faces and scenes, all unconditional. Pairing a grid
       with its FID makes the "this is what 3.17 FID looks like" point concrete.
Crop:  Keep whole sample tiles at native resolution so the reader sees the true
       pixel size; do not upscale a 32x32 CIFAR sample to imply more detail than
       the model produced.
```

```text
Asset: The progressive-generation / progressive-decompression figure (samples at
       intermediate timesteps, coarse structure first then fine detail).
Shows: What the 1000-step reverse process looks like in motion: large-scale
       shapes settle early, fine detail late. Supports both the "slow sequential
       sampling" point and the paper's "progressive lossy decompression"
       framing.
Crop:  Keep the ordered sequence of intermediate frames left-to-right; a single
       frame loses the point.
```

## Discarded

```text
URL: https://ar5iv.org/abs/2006.11239 -- redirected to ar5iv.labs.arxiv.org;
     recorded the canonical source page (arxiv.org/abs/2006.11239) instead. The
     ar5iv HTML was used to read the full text but is a rendering host, not the
     document's own address.
```

```text
URL: DDPM Table 1 "Sparse Transformer FID 2.80" line -- the fetched extraction
     labeled this ambiguously ("best on likelihood" yet gave an FID), so it is
     not used as a load-bearing comparison. The StyleGAN2+ADA and NCSN
     comparisons, which returned cleanly, carry the "how good was 3.17" point
     instead.
```

```text
URL: DDPM author affiliations were not rendered on the arXiv abstract page. The
     paper's own title block lists all three (Ho, Jain, Abbeel) at UC Berkeley,
     which the brief also states; recorded as UC Berkeley but flagged as not
     re-verified from the PDF title page in this pass.
```

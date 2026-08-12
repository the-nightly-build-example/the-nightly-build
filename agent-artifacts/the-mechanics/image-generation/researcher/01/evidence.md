# Evidence: the-mechanics/image-generation (01)

The primary papers firmly support the lesson's spine. Ho, Jain, and Abbeel
(DDPM, 2020) own the two core steps read backward from the behavior: the network
is trained to predict the noise added to an image, and generation starts from
pure Gaussian noise and applies that learned noise-predictor over many small
steps until an image remains. Ho and Salimans (2022) own the guidance step: a
single model is trained to run both with and without the prompt, and at sampling
the two predictions are combined with a weight that trades prompt-adherence
against variety. Rombach and colleagues (2022) own latent diffusion: the
diffusion runs in a compressed latent space and a decoder returns to pixels, and
the prompt enters the denoiser through cross-attention. Radford and colleagues
(CLIP, 2021) own the image-text alignment used as the text encoder in Stable
Diffusion. The record is strongest on the settled mechanism and honest about
where the sources themselves stop: the open steps (garbled text, muddled
attributes and spatial relations) are named by DALL-E 2's own authors as
failures they can only hypothesize about. The one place the writer must not
flatten: "modern systems denoise in a compressed latent space" is true of Stable
Diffusion but not of Imagen or DALL-E 2, which denoise in pixel space with a
cascade. The step count and the guidance-number convention also differ between
the DDPM paper and the deployed slider; both are recorded under Contradictions
so the writer does not merge two different numbers. No input was missing.

## Sources

```text
URL:         https://arxiv.org/abs/2006.11239
Kind:        primary. Ho, Jain, and Abbeel report their own training and
             sampling procedure. This paper owns the predict-the-noise objective
             and the step-by-step reverse process.
Establishes: (a) The forward (diffusion) process adds Gaussian noise over steps:
             q(x_t | x_{t-1}) = N(x_t; sqrt(1 - beta_t) x_{t-1}, beta_t I)
             (Eq. 2), with a closed form for jumping straight to step t,
             q(x_t | x_0) = N(x_t; sqrt(alpha_bar_t) x_0, (1 - alpha_bar_t) I)
             (Eq. 4), where alpha_t := 1 - beta_t and alpha_bar_t is the running
             product of alpha_s. So the amount of noise at step t is set by the
             schedule and grows monotonically; at large t the image is
             indistinguishable from pure noise. (b) The network predicts the
             noise. The simplified training loss (Eq. 14) is
             L_simple = E[ || epsilon - epsilon_theta(sqrt(alpha_bar_t) x_0 +
             sqrt(1 - alpha_bar_t) epsilon, t) ||^2 ]: take a clean image, add a
             known amount of noise epsilon, and train the network epsilon_theta
             to output that epsilon. (c) Generation (Algorithm 2, "Sampling"):
             sample x_T ~ N(0, I) (pure noise), then for t = T ... 1 compute a
             slightly cleaner x_{t-1} using epsilon_theta's prediction, adding a
             small noise term z at every step except the last. What remains at
             t = 0 is the image. There is no canvas and no object list; the image
             is the fixed point of repeated denoising.
Paraphrase:  "epsilon_theta is a function approximator intended to predict
             epsilon from x_t" (Sec. 3.2). The forward variances beta_t may be
             learned or held as constant hyperparameters (Sec. 2). T = 1000 for
             all experiments; the forward variances increase linearly from
             beta_1 = 1e-4 to beta_T = 0.02 (Sec. 4).
Locators:    Sec. 2 (background, Eq. 2, 4); Sec. 3.2 (Eq. 11, Algorithm 1 and 2);
             Sec. 3.4 (Eq. 14, L_simple); Sec. 4 (T = 1000, linear beta schedule,
             results).
Quote:       "We set T = 1000 for all experiments" and "we set the forward
             process variances to constants increasing linearly from
             beta_1 = 10^-4 to beta_T = 0.02" (Sec. 4).
```

```text
URL:         https://arxiv.org/abs/2207.12598
Kind:        primary. Ho and Salimans introduce and report classifier-free
             guidance; this paper owns what the guidance control does.
Establishes: (a) One network is trained to be both conditional and
             unconditional: during training the conditioning c is replaced by a
             null token with probability p_uncond, so the same weights learn to
             predict noise both with and without the prompt. (b) At sampling the
             two predictions are combined:
             tilde-epsilon = (1 + w) * epsilon_theta(z, c) - w * epsilon_theta(z)
             (Eq. 6), applied at each step before taking the denoising step.
             (c) The weight w controls a fidelity-versus-variety trade-off:
             larger w makes samples adhere harder to the prompt and reduces
             variety; smaller w keeps variety. w = 0 recovers the ordinary
             conditional model (no guidance).
Paraphrase:  Conditioning is dropped by "randomly setting c to the unconditional
             class identifier null with some probability p_uncond" (Sec. 3.2).
             Reported p_uncond in {0.1, 0.2} performs about equally well; 0.5
             performs worse (Sec. 4.2). "Increasing classifier-free guidance
             strength has the expected effect of decreasing sample variety and
             increasing individual sample fidelity" (Sec. 4.1). Empirically small
             w optimizes FID, large w optimizes Inception Score.
Locators:    Sec. 3.2 (joint training, dropout of c); Eq. 6 (guidance
             combination); Sec. 4.1-4.2 (p_uncond values, fidelity/variety
             behavior).
Quote:       "in what we call classifier-free guidance, we jointly train a
             conditional and an unconditional diffusion model, and we combine the
             resulting conditional and unconditional score estimates" (Abstract).
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. Rombach, Blattmann, Lorenz, Esser, and Ommer report their
             own method (Latent Diffusion Models, CVPR 2022). Owns denoising in a
             compressed latent space and cross-attention text conditioning.
Establishes: (a) Two stages. An autoencoder first compresses an image
             x in R^(H x W x 3) to a latent z = E(x); the diffusion model is
             trained on those latents (L_LDM = E[|| epsilon - epsilon_theta(z_t,
             t) ||^2 ], Eq. 2); a decoder D maps a generated latent back to
             pixels in a single pass. (b) Compression is set by a downsampling
             factor f: the latent's spatial size is (H/f) x (W/f), and they study
             f in {1, 2, 4, 8, 16, 32}, finding f = 4-8 the best quality-vs-cost
             trade-off (f = 1 is pixel-space and trains slowly; f = 32 loses
             quality). (c) Conditioning, including text, is injected into the
             denoising UNet by cross-attention: a domain-specific encoder
             tau_theta turns the input y into tau_theta(y) in R^(M x d_tau), which
             supplies the keys and values while the UNet features supply the
             queries: Q = W_Q . phi_i(z_t), K = W_K . tau_theta(y),
             V = W_V . tau_theta(y) (Sec. 3.3). So the text meets the image at
             every cross-attention layer of every denoising step.
Paraphrase:  In the paper's own text-to-image model the conditioning encoder is a
             BERT-tokenizer transformer (Sec. 4.3.1), the model is 1.45B
             parameters, trained on LAION-400M, primarily at 256 x 256. (Note the
             released Stable Diffusion swapped this encoder for CLIP; see the
             Hugging Face entry and Contradictions.)
Locators:    Sec. 3.1 (autoencoder, latent size H/f x W/f); Sec. 3.2 (Eq. 2,
             L_LDM); Sec. 3.3 (cross-attention conditioning, Q/K/V); Sec. 4.1
             (downsampling factors, Fig. 6); Sec. 4.3.1 (text-to-image, encoder,
             LAION-400M).
Quote:       Q = W_Q . phi_i(z_t), K = W_K . tau_theta(y), V = W_V . tau_theta(y)
             (Sec. 3.3, cross-attention).
```

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. Radford and colleagues (OpenAI) report CLIP. Owns the
             image-text alignment mechanism used as the text encoder in Stable
             Diffusion.
Establishes: CLIP jointly trains an image encoder and a text encoder with a
             contrastive objective: predict which caption goes with which image,
             pulling matched image-text pairs together in a shared embedding
             space and pushing mismatched pairs apart. Trained on 400 million
             (image, text) pairs collected from the internet. In a diffusion
             text-to-image system, the trained text encoder is what turns the
             prompt into the vectors the denoiser reads.
Paraphrase:  "the simple pre-training task of predicting which caption goes with
             which image is an efficient and scalable way to learn SOTA image
             representations from scratch on a dataset of 400 million (image,
             text) pairs collected from the internet" (Abstract).
Locators:    Abstract; Sec. 2 (approach, contrastive pre-training, 400M pairs).
Quote:       "400 million (image, text) pairs collected from the internet"
             (Abstract).
```

```text
URL:         https://arxiv.org/abs/2205.11487
Kind:        primary. Saharia and colleagues (Google) report Imagen. Owns the
             large-frozen-text-encoder variant and the pixel-space cascade,
             the contrast case against latent diffusion + CLIP.
Establishes: (a) Imagen conditions on a large frozen pretrained text encoder,
             T5-XXL, trained only on text; the encoder is not trained with the
             image model. (b) Their headline finding: scaling the text encoder
             helps image-text alignment and fidelity more than scaling the image
             diffusion model. (c) Architecture contrast: Imagen is cascaded
             pixel-space diffusion, a base 64 x 64 model followed by two
             super-resolution diffusion models to 256 x 256 then 1024 x 1024, not
             latent diffusion.
Paraphrase:  "increasing the size of the language model in Imagen boosts both
             sample fidelity and image-text alignment much more than increasing
             the size of the image diffusion model." Generic text-only language
             models are effective text encoders for image synthesis.
Locators:    Abstract and Sec. 2 (frozen T5-XXL text encoder); the language-model
             scaling finding (stated in the abstract and key-contributions
             section); architecture / cascade description (Sec. 2; exact appendix
             figure number not confirmed from the read).
Quote:       "increasing the size of the language model in Imagen boosts both
             sample fidelity and image-text alignment much more than increasing
             the size of the image diffusion model."
```

```text
URL:         https://arxiv.org/abs/2204.06125
Kind:        primary. Ramesh, Dhariwal, Nichol, Chu, and Chen (OpenAI) report
             DALL-E 2 / unCLIP. Owns the named open failures: attribute binding /
             spatial relations and text rendering, stated as failures its own
             authors cannot fully explain.
Establishes: (a) The model is worse at binding attributes to objects than a
             comparable GLIDE model; reconstructions "mix up attributes and
             objects," e.g. the colors of two objects get swapped. (b) The model
             struggles to render coherent text inside images. (c) The authors
             attribute both to properties of the CLIP embedding it conditions on
             and mark the explanation as a hypothesis, not a settled cause: the
             CLIP embedding "does not explicitly bind attributes to objects" and
             is hypothesized not to "precisely encode spelling information."
Paraphrase:  "unCLIP is worse at binding attributes to objects than a
             corresponding GLIDE model" and "unCLIP struggles at producing
             coherent text" (Sec. 7, Limitations and Risks, with failure examples
             in Fig. 15-16). The causal account is offered as a hypothesis about
             the CLIP representation, not a demonstrated mechanism.
Locators:    Sec. 7 (Limitations and Risks); failure figures (attribute binding
             and text rendering, Fig. 15-16 region).
Quote:       "unCLIP is worse at binding attributes to objects than a
             corresponding GLIDE model" (Sec. 7).
```

```text
URL:         https://huggingface.co/blog/stable_diffusion
Kind:        secondary. Hugging Face's "Stable Diffusion with Diffusers" post
             describes a deployed system built from the primaries above; it
             reports on the released model rather than owning the method. Use for
             grounding the everyday, deployed configuration a reader has met.
Establishes: (a) Stable Diffusion is a latent diffusion model: the diffusion
             runs in a compressed latent space and a VAE decoder returns to
             pixels. A (3, 512, 512) image becomes a (4, 64, 64) latent, a spatial
             compression of 8 x 8 = 64. (b) The prompt is encoded by a frozen CLIP
             text encoder (CLIPTextModel), not trained with the image model, and
             injected into the UNet by cross-attention. (c) Deployed defaults:
             50 inference (denoising) steps and a guidance_scale of 7.5, where
             guidance_scale increases adherence to the text at some cost to
             diversity.
Paraphrase:  "an image of shape (3, 512, 512) becomes (4, 64, 64) in latent
             space, which means the spatial compression ratio is 8 x 8 = 64."
             Stable Diffusion "simply uses CLIP's already trained text encoder."
             Recommended default of 50 inference steps; "By default the pipeline
             uses a guidance_scale of 7.5."
Locators:    Sections on the autoencoder/latent space, the text encoder, and
             inference parameters in the post.
Quote:       "By default the pipeline uses a guidance_scale of 7.5."
```

```text
URL:         https://getimg.ai/guides/interactive-guide-to-stable-diffusion-guidance-scale-parameter
Kind:        secondary. A vendor how-to guide describing the guidance slider as a
             user meets it. Grounds the user-facing control only; not a source for
             any mechanism claim.
Establishes: Framing of the guidance (CFG) slider for a non-technical user: low
             values give more varied but less prompt-faithful images (the prompt
             is effectively ignored at 1), high values follow the prompt harder at
             the cost of quality (up to a maximum of 20). Recommended everyday
             range 7-9.
Paraphrase:  "the higher the value, the more the image sticks to a given text
             input," but "more guidance means less diversity and quality." "Use
             the guidance scale value of 7-9."
Locators:    Body and FAQ of the guide.
Quote:       "Use the guidance scale value of 7-9. Increase when the generated
             image does not follow the prompt."
```

## Contradictions

- **"Modern systems denoise in latent space" is not universal.** Stable
  Diffusion (from Rombach et al.) denoises in a compressed latent space and
  decodes to pixels. Imagen (Saharia et al.) and DALL-E 2 (Ramesh et al.) denoise
  in pixel space using a cascade of models (64 -> 256 -> 1024 for Imagen). The
  commission's angle teaches latent diffusion as "one efficiency step," which is
  correct as an example, but the writer must attribute it to the latent-diffusion
  family and not state that all current systems work this way. Latent-vs-pixel is
  a real architectural fork, not a detail.

- **The text encoder differs across systems; do not flatten to "CLIP."** The LDM
  paper's own text-to-image model uses a BERT-style transformer encoder. The
  released Stable Diffusion uses a frozen CLIP text encoder. Imagen uses a frozen
  T5-XXL text-only encoder and reports that scaling this encoder matters more than
  scaling the diffusion model. DALL-E 2 conditions on CLIP embeddings through a
  separate diffusion "prior." All share the shape "a separate text model encodes
  the prompt and feeds the denoiser," but the specific encoder is a real
  difference the commission asked to preserve.

- **Step count: 1000 (DDPM training) is not the ~50 of a deployed run.** DDPM
  sets T = 1000 for its forward/reverse process. Deployed image generators run far
  fewer denoising steps (Stable Diffusion's default is 50) using faster samplers
  built after DDPM. The writer must not present "1000 steps" as what a user's
  generation does, nor "50 steps" as DDPM's own number. Both are correct for their
  own owner; the reduction comes from a different sampler, not from the DDPM paper.

- **The guidance number in the CFG paper and the slider are different scales.**
  Ho and Salimans define tilde-epsilon = (1 + w) epsilon(z, c) - w epsilon(z),
  where w = 0 means no guidance. Stable Diffusion's guidance_scale s uses the
  convention where s = 1 means no guidance (default 7.5). The two numbers measure
  the same control but are offset by one (s corresponds to w + 1). A reader told
  "the paper's guidance weight is your 7.5 slider" would be misinformed. State the
  behavior (stronger adherence, less variety) and keep the two conventions
  distinct if both numbers are used.

- **Cause of the open failures is hypothesis, not settled.** DALL-E 2's authors
  offer the CLIP-embedding account of attribute-binding and text-rendering
  failures explicitly as a hypothesis. The record supports "these failures are
  real and the builders name them as not fully understood," and does not support
  any confident single mechanism for why they happen.

## Numbers

```text
Figure: T = 1000 diffusion steps
Owner:  DDPM (Ho, Jain, Abbeel 2020), Sec. 4
Scope:  Number of forward/reverse steps in the paper's experiments. Not the
        deployed step count; see Contradictions.
```

```text
Figure: beta schedule linear from beta_1 = 1e-4 to beta_T = 0.02
Owner:  DDPM, Sec. 4
Scope:  Forward-process variance per step; sets how much noise is added at each
        of the T steps.
```

```text
Figure: unconditional CIFAR10 FID 3.17, Inception Score 9.46
Owner:  DDPM, Abstract / Sec. 4
Scope:  Sample-quality results on 32 x 32 CIFAR10. Context for "diffusion works,"
        not core to the mechanism.
```

```text
Figure: p_uncond in {0.1, 0.2} (0.5 worse)
Owner:  Classifier-Free Guidance (Ho, Salimans 2022), Sec. 4.2
Scope:  Probability the prompt is dropped during joint training so one network
        learns both conditional and unconditional prediction.
```

```text
Figure: guidance combination tilde-epsilon = (1+w) epsilon(z,c) - w epsilon(z)
Owner:  Classifier-Free Guidance, Eq. 6
Scope:  Per-step rule; w >= 0 is guidance strength, w = 0 is no guidance.
```

```text
Figure: downsampling factor f = 4 to 8 (best), studied f in {1,2,4,8,16,32}
Owner:  Latent Diffusion (Rombach et al. 2022), Sec. 4.1
Scope:  Latent spatial size is (H/f) x (W/f); f = 4-8 is the quality/cost sweet
        spot in the paper's ablation.
```

```text
Figure: (3, 512, 512) image -> (4, 64, 64) latent, spatial compression 8 x 8 = 64
Owner:  Hugging Face Stable Diffusion post (deployed configuration)
Scope:  Concrete latent size for Stable Diffusion v1 (factor 8 downsampling,
        4 latent channels).
```

```text
Figure: LDM text-to-image model 1.45B parameters, trained on LAION-400M at 256x256
Owner:  Latent Diffusion, Sec. 4.3.1
Scope:  The paper's own text-to-image model, with a BERT-style text encoder (not
        the released Stable Diffusion's CLIP encoder).
```

```text
Figure: CLIP trained on 400 million (image, text) pairs
Owner:  CLIP (Radford et al. 2021), Abstract
Scope:  Contrastive pre-training set that aligns image and text encoders.
```

```text
Figure: Imagen cascade 64x64 -> 256x256 -> 1024x1024, frozen T5-XXL text encoder
Owner:  Imagen (Saharia et al. 2022), Sec. 2
Scope:  Pixel-space (not latent) resolution cascade; text encoder frozen and
        text-only pretrained.
```

```text
Figure: Stable Diffusion defaults: 50 denoising steps, guidance_scale 7.5
Owner:  Hugging Face Stable Diffusion post (deployed defaults)
Scope:  Everyday user-facing configuration. getimg.ai recommends a 7-9 guidance
        range for the same slider.
```

## Source assets

```text
Asset: DDPM Figure 2, the directed graphical model of the forward/reverse chain
       (x_0 ... x_T with the arrows between steps). Caption: "The directed
       graphical model considered in this work."
Shows: The whole spine in one image: a clean image at one end, pure noise at the
       other, and the reverse arrows that generation follows. Names x_T (noise)
       and x_0 (image) so the "start from noise" claim is visual.
Crop:  Keep both ends (x_0 and x_T) and the reverse-direction arrows. Do not crop
       to a single node; the point is the chain.
```

```text
Asset: DDPM Figure 6 (extended as Figure 14 in the appendix), progressive
       unconditional CIFAR10 generation. Caption: "Unconditional CIFAR10
       progressive generation (x-hat_0 over time, from left to right)."
Shows: Samples getting cleaner across steps, coarse structure first and detail
       later, the direct picture of "many small denoising steps."
Crop:  Retain the left-to-right ordering and both the noisy early and clean late
       frames. Low-resolution CIFAR images; note the small size in a caption if
       used.
```

```text
Asset: Latent Diffusion Figure 3, the conditioning diagram. Caption: "We
       condition LDMs either via concatenation or by a more general
       cross-attention mechanism. See Sec. 3.3."
Shows: How the prompt enters the denoiser, the cross-attention path from the
       conditioning encoder into the UNet. Supports the "text meets image at every
       step" claim.
Crop:  Keep the cross-attention path and the conditioning-encoder box. Per the
       source, this figure emphasizes conditioning; the full encoder/latent/decoder
       pipeline is described in prose across Sec. 3, so do not caption Figure 3 as
       the complete end-to-end architecture.
```

```text
Asset: DALL-E 2 (Ramesh et al.) failure examples in the Limitations section
       (Fig. 15-16 region): attribute/color mix-ups and garbled in-image text.
Shows: The open failures as the builders' own examples, garbled text and swapped
       attributes, which grounds "even the builders only hypothesize why."
Crop:  Keep a clear text-rendering failure and an attribute-binding failure. Omit
       any surrounding unrelated panels.
```

```text
Asset: CLIP Figure 1, the contrastive pre-training schematic (image encoder and
       text encoder, the matched-pair matrix).
Shows: How image and text are aligned in one space, the mechanism behind "a
       separate text model encodes the prompt."
Crop:  Keep both encoders and the matching grid. This illustrates alignment, not
       diffusion; caption it as the text-encoder's origin, not the generator.
```

## Discarded

```text
URL: https://medium.com/@wangdk93/stablediffusion-guidance-scale-1822cfff7c9d
     Individual blog restating guidance_scale; adds nothing the CFG primary and
     the Hugging Face post do not own. Not read past the summary.
URL: https://www.aiphotogenerator.net/blog/2026/02/what-is-cfg-scale-stable-diffusion
     SEO explainer; no primary standing and no detail beyond the two secondaries
     already recorded.
URL: https://mccormickml.com/2023/01/11/steps-and-seeds/
     Useful intuition on steps and seeds but redundant with the Hugging Face post
     for the user-facing step count; not needed to meet the source floor.
```

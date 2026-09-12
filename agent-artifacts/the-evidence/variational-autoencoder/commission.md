# Commission: the-evidence/variational-autoencoder

## The assignment

Read "Auto-Encoding Variational Bayes" (Kingma & Welling, 2013; ICLR 2014), the
paper that introduced the variational autoencoder (VAE). This is The Evidence:
teach what the document actually says and did, the scale of what it showed, and
how its present-day use compares to what the paper demonstrated.

Selected to close a real gap in the course's coverage of generative models. The
library teaches GANs (the-evidence/gans) and diffusion (denoising-diffusion,
latent-diffusion), but not the VAE, the third pillar and the probabilistic
autoencoder whose descendants sit inside latent diffusion. The reader has met the
word "autoencoder" in the latent-diffusion lesson without ever being taught one.

## What the lesson must do

- State what the document is, who wrote it (Diederik P. Kingma and Max Welling,
  University of Amsterdam), and why it became foundational: it gave a way to train
  a deep latent-variable generative model by ordinary gradient descent.
- Walk through what it did. The encoder maps a data point to a distribution over a
  latent space; the decoder reconstructs data from a latent sample; training
  maximizes the evidence lower bound (ELBO), which balances reconstruction against
  a term pulling the latent distribution toward a simple prior. Teach the
  reparameterization trick plainly: the one move that let gradients flow through a
  random sampling step. Define KL divergence in plain words where it first
  appears.
- Show the scale honestly. This was a small-scale proof of method: the experiments
  were MNIST and the Frey Face dataset, not photorealistic image generation. Give
  the real datasets and what the paper actually reported (the variational lower
  bound / likelihood behavior), and be clear it was a method paper, not a
  benchmark-topping result.
- Bring it to the present. VAEs today are used less as standalone image generators
  (their samples are famously blurry) and more as learned encoders/latent spaces
  (the autoencoder in latent diffusion, VQ-VAE lineage, representation learning).
  Say plainly how the popular shorthand "VAEs generate images" compares to what
  the paper showed, and what later work changed or added.

## Boundaries

- One document, one lesson: the VAE method paper, not a survey of generative
  modeling and not a deep dive on VQ-VAE or latent diffusion (link those). Do not
  re-teach GANs or diffusion; link gans, denoising-diffusion, and latent-diffusion
  in Background.
- Assume algebra and probability (no introduction, per the press). Build the ELBO
  and the reparameterization trick here in plain words with a worked example,
  since the paper cannot be read without them. Keep the taught list short and
  complete.
- Work from the paper itself; where a popular characterization outruns it, say so.

## Required contribution

The reader should finish able to say what a VAE is (an encoder to a latent
distribution plus a decoder), what the reparameterization trick solved, why the
ELBO has the two terms it has, and why VAEs ended up more valued as learned latent
spaces than as image generators.

## Source obligations

From `nb source-policy --series the-evidence`: at least 6 sources, at least 3
primary, at least 1 secondary. The paper (arXiv:1312.6114 / ICLR 2014) is the
governing primary. Primaries may include the paper, closely related primary work
(the reparameterization/stochastic-backprop line, VQ-VAE, the beta-VAE analysis),
and a primary establishing VAEs' role in latent diffusion. Verify every figure
against the owning primary; secondary reporting is context only.

## Recent habits not to inherit (the-evidence)

- Do not headline on a lone figure by reflex; keep negative parallelism out of the
  headline and dek (one recent headline used a "not X" mold — avoid it).
- The required bring-to-present section keeps landing as a present-tense
  observation ("PaLM's successors stopped naming their size"); the section
  belongs, but do not open it with "Today's..." or copy that heading shape.
- Recent deks add an explanatory second clause naming an outside result; write the
  dek this piece needs rather than reaching for that mold.

## Neighboring articles in tonight's edition

Running now, do not overlap: the-instruments/f1-score, the-mechanics/
lost-in-the-middle, what-could-go-wrong/alignment-faking, when-ai-breaks/
hirevue-facial-analysis. No shared claims or examples.

## Production record

- Harness: Claude Code (remote). Model for every role: claude-opus-4-8 (the
  "capable" tier the balanced policy names; no stage is `required`).
- Effort targets (`nb production-policy --series the-evidence`): researcher high,
  writer medium, editor high, writing-coach low. Recorded as targets.
- No source or production directive was traded down.
- Note: an earlier commissioning round in this run mistakenly selected already-
  published slugs; this article's slug was verified absent from the full library
  before initialization.

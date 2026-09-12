# Draft handoff: the-evidence/variational-autoencoder (writer 02, revision)

## Original-work statement

This article turns nine scattered primary and secondary papers into one honest
teaching arc that separates what Kingma and Welling's 2013 paper actually
measured (a variational likelihood bound on tiny, CPU-era MNIST and Frey Face
data, with no image-quality claim) from the later "VAEs generate images"
reputation, teaches the ELBO's two terms and the reparameterization trick from
plain worked intuition, and follows the descendant line to locate the VAE's real
value as a learned latent space rather than a standalone image generator.

## Proof result

- Command: `./nb check .nb-work/.../variational-autoencoder.html --series the-evidence --library <checkout>` (full, links included).
- Result: **BLOCK: 0**, WARN: 1. Verdict PUBLISHABLE. `nb stamp` written
  (words 2191, reading 10 min, sources 9).

### Warning intentionally left

- `W-SENTENCE-DENSITY` "sentence is 46 words with 1 clause join, punctuation
  score 54." Unchanged from round 01: the density check reads the raw LaTeX
  inside the annotated ELBO `<div class="nb-math-eq">` as prose (a `<div>` is not
  a sentence-skip tag). This is the required, documented math furniture, not a
  prose defect. Left as is.

## Editorial request resolved

- KL worked example (publication-blocking): the printed per-dimension expression
  was the paper's eq. 10, ½(1 + log σ_j² − μ_j² − σ_j²), which is the −KL term
  the ELBO adds (falls to −4.5 at μ=3, σ=1) and contradicted the "penalty climbs"
  prose and the annotated equation's −D_KL. Replaced it with the KL divergence
  itself, ½(μ_j² + σ_j² − 1 − log σ_j²), cited to s1. Re-verified both worked
  values against the corrected form: μ=0, σ=1 gives 0 (penalty is nothing);
  μ=3, σ=1 gives 4.5 and σ=0.1, μ=0 gives ≈1.81 — both climb, consistent with the
  surrounding prose and the annotated ELBO's −D_KL. No other content changed; the
  editor's round-01 direct edits are preserved.

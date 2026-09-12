# Draft handoff: the-evidence/variational-autoencoder (writer 01)

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
  (words 2199, reading 10 min, sources 9). Full preview site builds and merges
  the article into the series index, the 2026-09-12 build, feed, and tag pages.

### Warning intentionally left

- `W-SENTENCE-DENSITY` "sentence is 46 words with 1 clause join, punctuation
  score 54." This is not a prose sentence. The density check reads the raw
  LaTeX inside the annotated ELBO `<div class="nb-math-eq">` as text (a
  `<div>` is not a sentence-skip tag, unlike `<math>`), and the equation's
  braces, subscripts, and operators drive the punctuation score. The equation
  is the required, documented math furniture the brief called for, written with
  documented markup exactly; splitting or simplifying it to satisfy a prose
  heuristic would damage the one thing the lesson is really about. Left as is.

## Notes for the editor

- **Continuity resolved per brief.** The brief overrode the researcher's
  library note: `the-evidence/gans`, `denoising-diffusion`, and
  `latent-diffusion` all exist in the library checkout and are confirmed
  present. All three are linked in Background; `latent-diffusion` is also a
  plain prose link at the first use of the autoencoder hook in orientation. No
  link to an unconfirmed lesson ships.
- **Reparameterization credit** is shared honestly in the body: the paper's
  authors get the deep-latent recipe and name, with Rezende, Mohamed & Wierstra
  credited for the independent development (s4) and Salimans & Knowles noted via
  the paper's own related work (s1). The headline names the paper's authors for
  what the paper did; the co-discovery caveat sits in the section body.
- **"Blurry" is written as a mechanism, not a quotation.** The element-wise
  Gaussian averaging is sourced to Larsen et al. (s5) and Doersch (s6); no
  source is quoted calling VAE samples "blurry."
- **Posterior collapse** is taught as the caveat on the two-term story (Bowman,
  s3), and VQ-VAE's discrete latent is framed as an escape from it (s8).

## Open question (optional, for editor judgment)

- The evidence record identifies the paper's own Figure 5 (actual 2013 MNIST
  samples at several latent dimensionalities) as the single most honest artifact
  for the proof-of-method scale point. I did **not** add it as a source asset:
  the scale point is already carried by the stat strip, the explicit
  "reports no image-quality score anywhere" line, and the CPU/dataset figures,
  and a fragile PDF capture was out of scope for the medium writer target. If
  the editor wants the visual, `nb asset pdf` on arXiv:1312.6114 Appendix A,
  Figure 5, is the exact source, cited to s1 with a Fig. 5 locator. No open
  evidence, voice, or commission decision blocks the draft.

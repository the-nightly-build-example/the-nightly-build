# researcher brief: the-instruments/fid (01)

Inputs:
- `../../commission.md` — the assignment, the two-or-three ideas, and boundaries
  (GANs and image-encoding are taught elsewhere; link them).
- `../../editorial-direction.md` — citation standard, series territory, declared reader.

Output: `evidence.md` (this directory)

Focus and known risk surface (decisions the inputs do not settle):

- The originating primary is Heusel et al. 2017 ("GANs Trained by a Two Time-Scale
  Update Rule Converge to a Local Nash Equilibrium," arXiv 1706.08500), which
  introduced FID. Read it. Record precisely the construction: which InceptionV3
  layer's activations (the pool3 / 2048-dim features), that each set is modeled as
  a multivariate Gaussian (mean vector and covariance matrix), and the exact
  Fréchet / Wasserstein-2 distance formula it computes (record what the formula
  says in words; do not re-derive). Record what the paper claimed FID improves on
  versus the earlier Inception Score.
- The misled cases — get each owning primary and record what it demonstrated, with
  figures and denominators:
  - Sample-size bias: Chong & Forsyth 2020 ("Effectively Unbiased FID and Inception
    Score and where to find them") — record that FID is biased, shrinks with more
    samples, and by how much / why cross-sample-count comparison is invalid.
  - The ImageNet lens: Kynkäänniemi et al. 2023 ("The Role of ImageNet Classes in
    Fréchet Inception Distance") — record the finding that matching ImageNet class
    frequencies can improve FID without improving image quality, with the size of
    the effect.
  - Resizing / implementation incomparability: Parmar et al. 2022 ("On Aliased
    Resizing and Surprising Subtleties in GAN Evaluation," Clean-FID) — record how
    much low-level processing differences move FID and whether it flips rankings,
    and how widespread the flawed pipelines were.
- Pick, and fully source, the single strongest "misled" case for the writer to
  work in full; record enough of the others to support the lesson's frame.
- Optional context primaries: Salimans et al. 2016 (Inception Score) as the
  predecessor; Kynkäänniemi et al. 2019 (improved precision/recall) as an
  alternative metric. Classify each source primary/secondary with a reason.
- Search for what cuts against the angle: defenses of FID's reliability, or
  evidence the criticisms are bounded. Record contradictions honestly.
- Give every figure its denominator and owning primary. Note any clean source
  figure a reader could learn from as a source-asset candidate, or write None found.

Run-environment caveat: record each source's own resolving page (arXiv,
publisher), never a fetch-proxy URL.

# researcher brief: the-evidence/gans (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the exact subject, angle, and required contribution

Output: ./evidence.md

Primary source that owns most claims: the paper "Generative Adversarial Nets,"
arXiv:1406.2661 (read the PDF, including Experiments, the evaluation section, and
the theory results). Verify firsthand:
- Authors, affiliation (Université de Montréal), venue/year (NIPS 2014).
- Exactly which datasets it trained on (MNIST, Toronto Face Database, CIFAR-10)
  and the resolutions involved. The exact evaluation method (Parzen-window /
  Gaussian-kernel log-likelihood estimate) and the paper's OWN stated caveat
  about that metric's variance and high-dimensional weakness. Read the reported
  log-likelihood numbers as printed.
- The theoretical claims: the value function / minimax game, and Proposition/
  Theorem that the global optimum recovers the data distribution given enough
  capacity — and the assumptions it rests on. Note what the paper says (or does
  not say) about training instability / mode collapse.
- Any figure of generated samples (which are the visual evidence) and its scale.

Then, for the "bring it to the present" section (secondary acceptable, labeled):
- The later high-resolution lineage as primaries where possible: DCGAN
  (Radford, Metz, Chintala 2015, arXiv 1511.06434), Progressive GANs (Karras et
  al. 2017), StyleGAN (Karras et al. 2018/2019) — enough to show that photoreal
  faces came YEARS after 2014, not from the original paper.
- That today's leading image generators are diffusion-based, not GANs (a primary
  or strong technical source for the diffusion turn, e.g. Ho et al. 2020 DDPM or
  Dhariwal & Nichol 2021 "Diffusion Models Beat GANs").
- Citation-count magnitude as a fame indicator from a citation index; label
  secondary and give the reading date.

Source policy: at least 6 sources total, at least 3 primary, at least 1
secondary. Seek evidence that complicates the "this paper made deepfakes"
framing (the multi-year gap to photorealism; the diffusion supersession).

Environment: web fetch is via a proxy; on a gated fetch (403/paywall) retry with
a browser-style request before recording unavailable, and record each source's
own canonical URL, not the fetch route.

Sanity check: the full published the-evidence slug list is in the commission's
Boundaries. Do not build the record around a claim that duplicates a published
lesson.

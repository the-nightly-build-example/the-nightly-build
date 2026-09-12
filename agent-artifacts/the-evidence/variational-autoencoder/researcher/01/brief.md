# researcher brief: the-evidence/variational-autoencoder (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md   (citation standard, series territory, reader)

Output: ./evidence.md

Read "Auto-Encoding Variational Bayes" (Kingma & Welling, arXiv:1312.6114 / ICLR
2014) itself as the governing primary. Pin down from the paper: the exact method
(recognition/encoder model, generative/decoder model), the ELBO and its two terms,
the reparameterization trick and the problem it solved (differentiating through a
sampling step), the datasets used (MNIST, Frey Faces), and what the paper actually
reported as results (the variational lower bound / marginal likelihood behavior,
not sample quality claims). Record model and experiment scale honestly.

For the present-day angle, establish with primary sources: that VAE samples are
blurry and why the field turned to VAEs as learned latent spaces rather than
standalone generators; the role of an autoencoder in latent diffusion (link to the
library's latent-diffusion lesson for continuity, but cite the primary); and the
VQ-VAE / beta-VAE developments that extended it. Verify every figure against the
owning primary. Search for what complicates the commission's angle (e.g., debates
over posterior collapse, whether the reparameterization trick originated
independently elsewhere) and record it in Contradictions.

# writer brief: the-evidence/variational-autoencoder (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writing-coach/01/voice-guide.md (how this piece should sound)
- ../../researcher/01/evidence.md       (the complete claim set; do not exceed it)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/the-evidence/variational-autoencoder/library/the-evidence/variational-autoencoder.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-evidence/variational-autoencoder/.nb-context/

Output: ./draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then
full including links until BLOCK: 0):
  ./nb check .nb-work/the-evidence/variational-autoencoder/library/the-evidence/variational-autoencoder.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/f68f1d9c-d5c2-58e1-960b-5ffb60cad58d/scratchpad/library-checkout
Run `nb stamp` before the final check.

This round's focus and decisions the inputs do not carry:
- Continuity: the library DOES contain the-evidence/gans, the-evidence/
  denoising-diffusion, and the-evidence/latent-diffusion. The researcher's note
  that gans/denoising-diffusion were not found came from an `nb history` call not
  pointed at the library checkout; disregard it. You may link all three in
  Background (and latent-diffusion at first use in prose, as the autoencoder hook).
  Only link lessons in that confirmed set.
- Credit the reparameterization trick honestly: Kingma & Welling credit Rezende,
  Mohamed & Wierstra with an independent development and cite Salimans & Knowles
  (2013) for an earlier similar reparameterization. Do not attribute the trick
  solely to this paper.
- "Blurry samples" is the field's shorthand for a mechanism (an element-wise
  Gaussian reconstruction term averages over the many outputs that could explain
  an input, so reconstructions smooth). Write it as that mechanism, not as a
  verdict quoted to any source. Teach the two-term ELBO with the posterior-collapse
  caveat (a strong decoder can drive the KL term to zero and ignore the latent).
- Keep the scale honest: single-layer MLPs (500/200 hidden units), MNIST and Frey
  Face, a small CPU-era proof of method; the paper reports the variational lower
  bound and an MCMC marginal-likelihood estimate, and makes no sample-quality
  claim. Do not import later systems' image results as if they were in the paper.
- Commission's "Recent habits not to inherit" is binding: no lone-figure headline
  reflex, no negative parallelism in headline/dek, no "Today's..." opener on the
  bring-to-present section. Fill `nb-meta` harness "Claude Code", model
  "claude-opus-4-8".

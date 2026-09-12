# editor review-brief: the-evidence/variational-autoencoder (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writer/01/brief.md              (the exact brief the writer worked from)
- ../../writing-coach/01/voice-guide.md
- ../../researcher/01/evidence.md
- ../../writer/01/draft-handoff.md      (original-work sentence; open in the third read)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/the-evidence/variational-autoencoder/library/the-evidence/variational-autoencoder.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-evidence/variational-autoencoder/.nb-context/

Output: ./editorial-review.md

Recent-pattern notes (the-evidence back catalogue; use to catch formula and
catchphrase):
- Recent headlines lean on a single surprising figure ("PaLM was trained on a
  fourteenth of the data its size called for") and one used a "not X" negative-
  parallelism mold ("...on a compressed grid, not the full image"). Flag either in
  this draft's headline.
- Recent bring-to-present sections open as present-tense observations ("PaLM's
  successors stopped naming their size", "Today's agents call tools in JSON").
  Watch the scale-to-present heading against these.
- Recent deks add an explanatory second clause naming an outside result.

This round's focus:
- press/editorial.md check: the takeaway bookend carries the judgment. If the body
  closes on a Verdict note or any block restating the finding, remove it (a leftover
  from the earlier template). Confirm the body does not end on such a block.
- Verify against the evidence record: the ELBO's two terms and the reparameterization
  trick, KL defined plainly at first use, and the honest scale (single-layer MLPs,
  500/200 hidden units, MNIST and Frey Face, the paper reports a variational lower
  bound and an MCMC marginal-likelihood estimate and makes no sample-quality claim).
  No later systems' image results imported as if in the paper.
- Confirm shared credit for the reparameterization trick (Rezende, Mohamed &
  Wierstra; Salimans & Knowles), that "blurry" appears only as the element-wise-
  averaging mechanism and never as a verdict quoted to a source, and that the
  two-term ELBO carries the posterior-collapse caveat.
- Background links (gans, denoising-diffusion, latent-diffusion) all exist and are
  valid; latent-diffusion is the confirmed autoencoder hook.
- Note: the writer left one W-SENTENCE-DENSITY that the density heuristic reads off
  the annotated ELBO equation's LaTeX (documented math furniture, not prose); it is
  not a prose defect. The writer also flagged an optional source asset (the paper's
  MNIST-samples figure) as your judgment call: request it only if an exact visual
  would let the reader test a central argument better than the prose does. If you
  change prose, a fresh writer proof is owed before PR.

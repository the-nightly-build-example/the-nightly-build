# writer brief: the-evidence/variational-autoencoder (02, revision)

Apply the required items in the editorial review, nothing wider.

Inputs:
- ../../editor/01/editorial-review.md   (the review to apply; its "Required work" is binding)
- ../../commission.md
- ../../editorial-direction.md
- ../../writing-coach/01/voice-guide.md
- ../../researcher/01/evidence.md
- ../01/draft-handoff.md                 (your round-01 handoff)
- Article to edit (in place, already carries the editor's round-01 direct edits):
  /home/user/the-nightly-build/.nb-work/the-evidence/variational-autoencoder/library/the-evidence/variational-autoencoder.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-evidence/variational-autoencoder/.nb-context/

Output: ../02/draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then
full including links until BLOCK: 0):
  ./nb check .nb-work/the-evidence/variational-autoencoder/library/the-evidence/variational-autoencoder.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/f68f1d9c-d5c2-58e1-960b-5ffb60cad58d/scratchpad/library-checkout
Run `nb stamp` before the final check.

The one required fix (publication-blocking):
- The closed-form KL worked example currently prints, per dimension,
  ½(1 + log σ² − μ² − σ²) and calls it "the gap" (the KL divergence) that "climbs"
  as the code leaves the prior. That expression is the paper's eq. 10, which is
  MINUS the KL term the ELBO adds, so its sign is inverted: at μ=3, σ=1 it is −4.5,
  which falls rather than climbs. Print the KL divergence itself,
  ½ Σ (μ² + σ² − 1 − log σ²) per dimension, so the sign is consistent with the
  −D_KL shown in the annotated equation and with the "penalty climbs" prose.
  Re-verify both worked numeric values against the corrected formula, and cite the
  paper (source s1). Note: the evidence record's Numbers entry mislabels the −KL /
  eq.10 expression as "the exact KL term"; use the corrected formula here, not that
  entry.
- Preserve the editor's round-01 direct edits already in the file and all other
  settled work. Do not expand the claim set or change anything else.

Then rerun the complete proof to BLOCK: 0 and write ../02/draft-handoff.md with the
original-work sentence, the proof result, and one line on the KL fix applied.

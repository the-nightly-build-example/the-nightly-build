# Editorial review: the-evidence/variational-autoencoder (editor/02)

Focused confirmation re-read after the single publication-blocking fix from round
01. Round 01 approved everything else; this read verifies the KL worked-example
correction and checks that nothing regressed. No resolved objection is reopened
and no new standard is introduced.

## Skeptic

The one break from round 01 was the closed-form KL worked example, which printed
the paper's eq. 10 (the −KL term the ELBO adds, ½(1 + log σ_j² − μ_j² − σ_j²))
while calling it "the gap" and claiming the "penalty climbs" — so it read as
minus the KL divergence and failed its own worked check (μ=3, σ=1 gave −4.5,
falling rather than climbing).

The round-02 draft now prints, per latent dimension,
½(μ_j² + σ_j² − 1 − log σ_j²) — the KL divergence itself, the gap the objective
subtracts. Confirmed against all four requirements:

- Form: the printed expression is the KL divergence of a Gaussian posterior from
  the N(0, I) prior, not the eq.-10 −KL form. Correct.
- Sign: the annotated ELBO still prints −D_KL(q‖p), and the surrounding prose
  says "the objective subtracts it" and "the penalty climbs." A positive KL that
  the objective subtracts is consistent with both. The contradiction is gone.
- Worked values: μ=0, σ=1 → ½(0 + 1 − 1 − 0) = 0 ("the penalty is nothing"), and
  μ=3, σ=1 → ½(9 + 1 − 1 − 0) = 4.5 (climbs). Both correct and consistent with
  the prose. The prose's second illustration (shrink the spread to a tenth) is
  stated as a direction only, prints no value, and is true (σ=0.1, μ=0 ≈ 1.81,
  climbing).
- Citation: the expression is cited to s1, the governing primary. Correct.

The evidence-record correction owed to the researcher (its Numbers entry labels
the eq.-10 form as "the exact KL term") is that role's item, not a bar to this
article; the article no longer depends on the mislabeled sign.

## Cut

No new slop pass was run; this is a focused re-read, not a fresh full review. The
one changed paragraph was read for new defects and carries none: it states a
fact (the closed form), a reasoning step (both pieces cancel at the prior), and a
directional consequence (the penalty climbs), all load-bearing. No sentence in it
fails the delete test. The two round-01 edits are intact — "The first term has a
name worth defining: the KL divergence" stands, and the cut "The knob shows what
the KL term controls" has not returned; the beta-VAE paragraph still lands on the
disentanglement result. Nothing else in the article changed.

## Reader

The fix restores the one thing that stood between round 01's reader read and
approval: a reader who works the KL example now gets 0 at the prior and a value
that climbs as the encoder's blur leaves it, matching the two-term lesson the
section teaches. The piece still gives what its sources alone do not — the
separation of what the paper measured from the "VAEs generate images"
reputation, the worked ELBO and reparameterization intuition, and the descendant
line to the latent space — and the prose still sits closer to the voice-guide
exemplars than to a median summary.

## Edits

- None. The writer's round-02 correction is sound as delivered; no prose change
  was needed.

## Required work

- None blocking publication. (Non-article: the researcher's evidence-record
  Numbers entry still labels the eq.-10 −KL form as the KL term, per round 01;
  that is the researcher's to correct and does not affect this article, which now
  prints the divergence itself.)

## Decision

approve — the KL worked example now prints the KL divergence
½(μ_j² + σ_j² − 1 − log σ_j²), cited to s1, with a sign consistent with the
annotated −D_KL and the "penalty climbs" prose and correct worked values (0 at
μ=0, σ=1; 4.5 at μ=3, σ=1); the round-01 edits are preserved and nothing else
regressed.

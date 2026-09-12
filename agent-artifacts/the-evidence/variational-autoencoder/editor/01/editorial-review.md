# Editorial review: the-evidence/variational-autoencoder (editor/01)

## Skeptic

Thesis: Kingma and Welling's 2013 paper made a deep latent-variable generative
model trainable by ordinary gradient descent; its ELBO objective balances a
reconstruction reward against a KL penalty toward a simple prior; the
reparameterization trick was the one move that let gradients flow past a random
draw; and the work was a small CPU-era proof that reported a likelihood bound,
whose lasting value turned out to be the compressed latent space its descendants
reuse, not standalone image generation.

Claims it stands on, and how each held:

- The reparameterization trick let gradients reach the encoder through a random
  sampling step (headline; reparameterization section). Held. The paper's own
  words for the problem ("exhibits very high variance and is impractical") and
  the fix (z = μ + σ ⊙ ε, ε ∼ N(0, I)) match the evidence record and §2.4/§3 of
  the primary. The body is careful that the idea was co-discovered: it credits
  Rezende, Mohamed & Wierstra with the independent development (s4) and points to
  Salimans & Knowles for an earlier similar reparameterization (s1). Both are
  supported by the VAE paper's §4 as quoted in the evidence record.

- The ELBO has two terms that pull against each other (two-terms section). Held
  as an objective, and the annotated equation is correct: it prints
  −D_KL(q‖p) + E[log p(x|z)], matching eq. 3, and the legend correctly describes
  D_KL as the gap the objective subtracts. The posterior-collapse caveat is
  present and sourced (Bowman, s3; a strong decoder drives the KL term to zero
  and ignores the latent), with VQ-VAE framed as an escape from it (s8). The
  beta-VAE paragraph correctly presents β as a single knob on the KL term (s2).

- The scale was small and the reported result was a likelihood, not image
  quality (legacy section, stat strip). Held. Single-hidden-layer MLPs, 500/200
  hidden units for MNIST/Frey Face, ~20–40 minutes per million samples on one
  CPU, the variational lower bound against wake-sleep plus an MCMC
  marginal-likelihood estimate on the first thousand train and test points, and
  no image-quality score: every figure matches the evidence record's Numbers
  block and the primary. The correction of the "VAEs generate images" shorthand
  is stated as reporting, against a named misconception, so its contrast is
  earned rather than invented.

- Blurriness is a mechanism, not a quoted verdict (legacy section). Held, and
  this was a focus item. "Blurry"/"soft"/"smear" appear only as the
  element-wise-averaging mechanism, sourced to Larsen (s5, the quoted phrase "are
  not adequate for images") and Doersch (s6, the averaging intuition). No source
  is quoted calling VAE samples blurry. The closing line names it as averaging
  and explicitly not a verdict any one paper pronounced.

- The legacy is the latent space (dek, legacy section, takeaway). Held. Rombach's
  KL-regularized autoencoder "similar to a VAE" (s7) is quoted exactly, VQ-VAE-2's
  "rivals ... state of the art Generative Adversarial Networks" (s9) is quoted
  exactly, and the synthesis that the fidelity came from a powerful prior over
  the latent grid rather than the autoencoder is supported by the VQ-VAE-2 record.

The break: the closed-form KL worked example carries a sign error. In the
two-terms section the paragraph prints, per latent dimension,
½(1 + log σ_j² − μ_j² − σ_j²), calls it "the gap" (the KL divergence just
defined), and says the "penalty climbs" as the encoder's blur leaves the prior.
That printed expression is the paper's eq. 10, which is the −KL term added to the
ELBO — the same term the article's own annotated equation already shows with an
explicit minus (−D_KL). So the printed expression equals minus the KL
divergence, not the KL divergence, and the article's own worked check fails on
it: at μ = 3, σ = 1 the printed expression is ½(1 + 0 − 9 − 1) = −4.5, which
falls from zero rather than climbing. The gap the objective subtracts is
½ Σ_j (μ_j² + σ_j² − 1 − log σ_j²); with that form, μ = 0, σ = 1 gives 0 and
μ = 3, σ = 1 gives 4.5 (climbs), consistent with the prose and with the −D_KL in
the annotated equation. This is the center of the lesson's two-term teaching and
reaches every reader who works the example, so it is publication-blocking. The
fix alters a cited formula and re-verifies worked numbers, which is the writer's;
I routed it rather than flipping the sign myself. The evidence record seeded the
error and needs its own correction (see Required work).

Display text audited descriptor by descriptor. Authors, affiliation (University
of Amsterdam), year (2013 arXiv / ICLR 2014), datasets, hidden-unit counts, the
2-to-200 latent-dimension sweep, and every quotation check out against the owning
primaries. The three Background link titles are the exact headlines of the linked
articles (gans, denoising-diffusion, latent-diffusion), all three confirmed
present in the library checkout; latent-diffusion is also the in-prose autoencoder
hook. Every source's data-nb-kind is correct against the primary/secondary test:
s1–s5 and s7–s9 own their methods and are primary, Doersch (s6) is a tutorial and
correctly secondary. Source obligations are met (nine sources, eight primary, one
secondary). Every citation href was opened as printed; all nine resolve (HTTP
200), the OpenReview beta-VAE page included, and each lands on its own source.

One consideration I weighed and left: the headline, "Kingma and Welling made
random sampling differentiable," is standard field shorthand for the trick and is
strong by the headline standard (actors named, fresh verb, surprise first, no
lone figure, no negative parallelism, no colon). It sits in mild tension with the
body's careful point that a gradient cannot pass through the draw and the
randomness is instead routed around it, but the compression is defensible for a
lesson headline and the body carries the precise mechanism. Not changed.

## Cut

One dedicated slop pass, then the edges alone, then the delete test. One sentence
failed and was cut: the beta-VAE paragraph closed on "The knob shows what the KL
term controls," a summary that restates what the paragraph already showed
(turning β up presses the blurs toward the prior) and loses no fact, claim, or
reasoning step under the delete test. The paragraph now lands on the
disentanglement result, which is specific and sourced.

One prose repair, not a slop cut: "The first term needs a name it uses: the KL
divergence" was ungrammatical in its own terms; rewritten to "The first term has
a name worth defining: the KL divergence," which also sets up the plain-question
definition that follows.

The edges otherwise hold. Section openers ("The spread is what ties the space
together," "The balance is also fragile," "One step blocks the whole plan") each
carry a claim the paragraph proves, and the closers ("the encoder can learn,"
"the terms can collapse into each other," "handed the work of sharp images to
something else") state conclusions the argument built rather than grading it. The
final sentence survives the last-sentence test: it names what the descendants
kept and what they offloaded, both supported. Negative-parallelism constructions
("not on one point but on a small blur," "not how good its pictures looked," "not
a verdict any one paper pronounced") each correct a misconception the piece names,
so they are earned. No em-dash abuse, no vague attribution, no decorative
copulas, no self-reference outside the two bookends the template allows.

Checked against the recent-pattern notes: the headline avoids the lone-figure and
"not X" molds; the bring-to-present section opens "The experiments were small,"
not a "Today's ..." observation, and its heading ("From a CPU proof to Stable
Diffusion's latent space") is neither the flagged present-tense shape nor a
comma-and-clause formula; the dek's legacy claim is the piece's own thesis, not
the tacked-on explanatory second clause the note warns about. Furniture is in
proportion: one annotated equation (the ELBO, the one the article is about), one
bare display equation (the reparameterization), inline math, one stat strip, and
the two required bookends. It reads as a continuous lesson, not a stack of
blocks. The single W-SENTENCE-DENSITY warning reads off the LaTeX inside the
annotated equation, as the brief noted, and is not a prose defect.

## Reader

Read straight through as the course's reader, the piece gives what no single
source hands over: it separates what the paper measured (a likelihood bound on
tiny CPU-era data, no image score) from the "VAEs generate images" reputation,
teaches the two ELBO terms and the reparameterization trick from worked intuition
a reader can trace by hand, and follows the descendant line to place the VAE's
real value in the latent space that Stable Diffusion runs inside. That answer
survives, and it matches the writer's original-work statement. The prose sits
closer to the voice-guide exemplars than to a median summary: the plain-question
introduction of KL divergence follows Olah, the "no one pictures a
two-hundred-dimensional space" move follows Nielsen, and the honest-scale
register follows Karpathy. The headline, read last as the largest claim, is
carried by the reparameterization section. The one thing standing between this
read and approval is that a reader who works the KL example hits the sign error.

## Edits

- Rewrote "The first term needs a name it uses: the KL divergence" to "The first
  term has a name worth defining: the KL divergence" (grammar and clarity).
- Cut the sentence "The knob shows what the KL term controls" from the beta-VAE
  paragraph (contentless summary; fails the delete test).

## Required work

- researcher: Correct the evidence record's Numbers entry that labels
  ½ Σ_j (1 + log σ_j² − μ_j² − σ_j²) as "the exact KL term when prior and
  approximate posterior are Gaussian." That expression is the −KL term added to
  the ELBO (the paper's eq. 10), not the KL divergence; label the sign convention
  explicitly so the closed form for D_KL and for the ELBO contribution are not
  conflated.
- writer: Fix the closed-form KL worked example in the two-terms section. Print
  the KL divergence itself (the gap the objective subtracts),
  ½ Σ_j (μ_j² + σ_j² − 1 − log σ_j²), so the sign is consistent with the
  annotated ELBO's −D_KL and with the surrounding prose ("the gap," "the objective
  subtracts it," "the penalty climbs"). Re-verify the two worked values in prose:
  μ = 0, σ = 1 gives 0 (penalty is nothing) and moving the mean out to three (or
  shrinking the spread) makes it climb. Cite to s1. Run a fresh proof after the
  fix.
- writer (optional, non-blocking): The paper's Figure 5 (actual 2013 MNIST
  samples across latent dimensions) would let a reader see the proof-of-method
  scale rather than take the prose's word, and is available via the paper's
  Appendix A cited to s1. I am not requiring it: the stat strip, the
  "reports no image-quality score anywhere" line, and the CPU/dataset figures
  already carry the honest-scale claim. If added, crop to keep the per-dimension
  panel labels.

## Decision

revise — the article is sound and well-sourced throughout, but the ELBO's
closed-form KL worked example prints minus the KL divergence where the gap belongs
and fails its own "penalty climbs" check, a reader-facing error at the center of
the two-term lesson that the writer must fix and the researcher's evidence record
must stop seeding.

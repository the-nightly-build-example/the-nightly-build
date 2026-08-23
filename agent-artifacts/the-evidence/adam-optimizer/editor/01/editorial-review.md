# Editorial review: the-evidence/adam-optimizer (editor/01)

## Skeptic

Thesis: the 2015 Adam paper backed the method two ways, with a speed result and
a convergence proof; the proof was disproven in 2018, and the field kept using
plain Adam anyway because the flaw never touched how the method actually
performs. The claims it stands on:

1. **What Adam computes.** The per-weight update, the two running averages, bias
   correction, and the four defaults (alpha 0.001, beta1 0.9, beta2 0.999, eps
   1e-8). Checked against the Adam paper (s1). Venue (ICLR 2015) confirmed on the
   arXiv page; the update rule, defaults, and the four experiments are read
   firsthand in the evidence record and are uncontested. The annotated equation
   colors and legends exactly the three terms the prose tracks. Holds.

2. **The scale was small.** The four experiments (logistic regression on
   MNIST/IMDB, a 2x1000 MLP, a CIFAR-10 CNN, a VAE), largest model the 2x1000
   MLP, all on MNIST/CIFAR-10 in minibatches of 128. Matches the evidence record
   and the paper's own Section 6 "Using large models and datasets" quote, which
   the piece uses to date the paper rather than to inflate it. The frontier-scale
   contrast ("a handful of problems a laptop can run") is honest and does not let
   the 2015 work read as large. Holds. One caption error found and fixed (see
   Edits): the caption located the largest model in the "third row" when the MLP
   sits in the second row (the third row is the CNN).

3. **The counterexample and the named proof error (load-bearing).** Verified most
   skeptically against the Reddi PDF (s3), pages 4-5. The domain [-1,1], the loss
   sequence (Cx when t mod 3 = 1, -x otherwise, C>2), the settings beta1=0 and
   beta2=1/(1+C^2), and the iterate walking to x=+1 while the optimum is x=-1 all
   match the source exactly. The paper's own phrase for +1 is "worst amongst all
   points in the set [-1,1]," which the piece renders as "the single worst point
   in the domain" — faithful. The quoted sentence ("the proof in the original
   paper of ADAM erroneously assumes that Gamma_t is positive semi-definite and
   is hence, incorrect") is verbatim; the piece correctly closes the quote before
   the source's parenthetical. The Gamma_t definition is re-indexed from the
   source's Gamma_{t+1} by one step, which is faithful. The worked arithmetic
   (the once-in-three +C step, scaled down by a large second moment, outweighing
   the two -1 steps) is the piece's own synthesis and is correct. AMSGrad's one
   line, v_hat_t = max(v_hat_{t-1}, v_t), and its restored O(sqrt(T)) bound match
   Algorithm 2 and Theorem 4. Holds.

4. **The convergence nuance (the claim I most wanted to break).** The piece must
   not say Adam simply "does not converge," and it does not. It states the 2015
   proof's flaw as flat fact, then holds it apart from later-proven convergence.
   Checked both later primaries at the source. Zhang et al. (s6): confirmed
   convergence to a neighborhood of critical points when beta2 is large and
   beta1 < sqrt(beta2) < 1, a phase transition from divergence to convergence as
   beta2 rises, and the explicit protocol critique that Reddi picks the problem
   after fixing the hyperparameters while practice fixes the problem first.
   Defossez et al. (s7): confirmed the non-convex bounded-gradient bound under
   suitable hyperparameters and the abstract's own note that at the literal
   defaults the clean bound does not close; TMLR confirmed. The piece's sentence
   "the 2015 proof being wrong is not the same as Adam failing to converge" is the
   earned central contrast, and the closing "holds two facts at once" synthesis
   keeps the disproven theorem and the working method both in view. Holds, and
   this is the piece's strongest work.

5. **The field shrugged.** PyTorch ships amsgrad=False (s4): confirmed on the
   canonical page (docs.pytorch.org resolves to the current versioned copy, which
   shows amsgrad=False in the constructor and describes it as "the AMSGrad variant
   ... from the paper On the Convergence of Adam and Beyond"). Schmidt et al. (s5):
   fifteen optimizers, more than 50,000 runs, and the verbatim finding "ADAM
   remains a strong contender, with newer methods failing to significantly and
   consistently outperform it." AdamW (s8): the L2-vs-weight-decay inequivalence
   for adaptive methods and the generalization improvement, ICLR 2019, confirmed.
   Holds.

Citation hrefs: opened all eight as printed. s1, s3, s4, s5, s6, s7, s8 land on
the source. s2 (Semantic Scholar API) is the deliberately-recorded artifact that
returns the figure; it rate-limited (HTTP 429) through the page fetcher but
returns citationCount 170154 directly, matching the article's "past 170,000" and
the evidence record's 170,154 exactly. The Background and Go-deeper links (Reddi,
Schmidt, and the internal gradient-descent lesson) resolve.

data-nb-kind audit: every label is correct. s2 (aggregator) and s5 (Schmidt, a
study that is primary for its own result but external commentary on Adam) are
secondary; the other six are the documents that own their claims. Note for the
orchestrator: this is 6 primary + 2 secondary, matching the draft-handoff and the
evidence record's reasoning, not the "7 primary + 1 secondary" the review brief's
parenthetical names. The source floor (>=6 total, >=3 primary, >=1 secondary) is
satisfied either way; no action needed, flagged only because the brief's count
and the article disagree.

Best-paper-award claim (appears in Why-this-matters and takeaway): the Reddi PDF
header confirms ICLR 2018 publication; the best-paper distinction is established
firsthand in the evidence record and is a matter of public record. Accepted.

No broken claim. No missing evidence. Nothing routed to researcher or writer.

## Cut

Ran the sentence-by-sentence slop pass, the edges pass, the arrived-from-a-link
pass, and the delete test. The draft is clean: no empty conclusions, no vague
attribution, no decorative-analysis copulas, no self-reference outside the two
bookends the lesson template allows. The negative-parallelism constructions that
appear ("converges rather than merely works," "not the same as Adam failing to
converge," "about regularization, not about the convergence proof") each correct
a misconception the piece actually names — the two-promises split and the reader's
assumption that a broken proof means non-convergence — so each is an earned
contrast, not the reflex. Zero sentences failed the slop test outright.

The furniture earns its place: the annotated Adam-update equation is the one
equation the lesson is about (the template allows at most one annotated equation,
and this is it), and the scale table is a genuine comparison of the four
experiments, which is exactly where the commission said a table belongs rather
than as a default spine. No component reads as filler.

Two structural echoes of the named sibling piece, the-evidence/batch-normalization,
which the brief flagged. Both are formula under spec/slop.md's Formula entry and
spec/headlines.md's repeated-heading rule, and I broke both directly (see Edits):
the orientation heading shared batch-norm's "A [noun] ... every [noun]" frame,
and the takeaway's "the proof was the part that did not survive" was the twin of
batch-norm's "that reason is the part that did not hold." The headline itself is
distinct from batch-norm's, and the piece's error (a disproven theorem) is held
clearly apart from batch-norm's (a wrong causal mechanism), so the distinction
does real work.

Checked display text and headings against the recent-pattern notes: the
orientation heading is now in Adam's own nouns and off the banned "what 'trained
with X' actually names" mold; the dek makes a claim about the world (the
counterexample drives Adam to the worst point at hyperparameters no practitioner
chooses) rather than grading the article's method, and carries none of the three
banned dek molds (no semicolon reversal, no suspended question, no comma triad);
the closer is in Adam's nouns and does not reuse "where the same X still runs."

## Reader

Reading straight through as the paper's declared reader — smart, widely read, new
to optimization — I come away able to say what Adam computes, that its 2015
backing was a speed result plus a convergence proof, exactly how a one-number
convex problem breaks that proof and why (the rare large gradient, scaled down by
a large second moment, outweighing the two small ones), and why none of that
dislodged the method: the fix rarely helps on real workloads, later proofs give
Adam real guarantees at the beta2 practice uses, and the variant that did win
(AdamW) fixed regularization, not convergence. No single source gives that; it is
synthesized across eight. The draft-handoff's original-work sentence claims
exactly this pairing — the counterexample run as arithmetic, and the disproven
theorem held apart from the later-proven convergence — and both survive the read.
The prose sits closer to the voice-guide exemplars than to a median summary:
"The correct total says go down. Adam goes up." and "demonstrated on a handful of
problems a laptop can run" are Karpathy/Olah-grain concrete, not filler.

Visual evidence: the writer worked Reddi's counterexample in prose rather than
capturing Reddi's Figure 1. I judge that the right call. Figure 1 is a
convergence/iterate plot — it shows that Adam reaches +1, but not why; the worked
arithmetic shows the mechanism, which is what lets the reader test the central
claim. A source asset here would confirm rather than teach, and the voice guide
steers explicitly toward the worked case. No asset requested.

## Edits

- Table caption: "the largest is the two-layer network in the third row" changed
  to "second row" — the 2x1000 MLP (the two-layer network) sits in row 2; row 3
  is the CNN. Factual correction to display text, fixed against the article's own
  table.
- Orientation heading "A separate step size for every weight" retitled to
  "Every weight gets its own step size" — breaks the shared "A [noun] ... every
  [noun]" frame with batch-normalization's orientation heading, staying in Adam's
  own nouns.
- Takeaway: "The proof was the part that did not survive." rewritten to "Of
  those two promises, the proof was the one that broke." — breaks the echo of
  batch-normalization's "that reason is the part that did not hold," and ties the
  line to the opener's own "two promises" framing (setup and resolution).

## Required work

None. All findings were fixable within the editor's remit and are done. No
evidence gap for the researcher; no reporting, redraft, source asset, or chart
work for the writer. For the orchestrator only, a non-blocking note: the article
carries 6 primary + 2 secondary sources (correctly labeled, floor satisfied), not
the 7 primary + 1 secondary the review brief's parenthetical states.

## Decision

approve — every claim, including the load-bearing convergence nuance and all
eight citation hrefs, verified against the sources; the two formula echoes of the
named sibling and the one caption error were fixed directly, and nothing
publication-blocking remains.

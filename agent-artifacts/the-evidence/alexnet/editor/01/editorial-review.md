# Editorial review: the-evidence/alexnet (editor/01)

## Skeptic

**Thesis.** AlexNet's 2012 ImageNet win was a real, large result (~10-point
top-5 margin) that reorganized computer vision around depth, data, and compute,
but it invented none of the pieces it used: deep CNNs, GPU training, superhuman
vision accuracy, and ImageNet's labeled scale all predated it. It was a
convergence on a benchmark the whole field was watching, not an invention. A
second, load-bearing sharpening: the famous 15.3% is a seven-net ensemble; the
single model the paper describes scored 18.2%.

The piece holds credit and correction in the same breath throughout ("None of
this shrinks the achievement," "the win was real and the margin was large," "The
paper earned its place"). It is not a debunk. The register the voice guide asked
for is intact.

**Claims tested against the primaries (every citation opened as printed):**

- *15.3% vs 26.2%, and 18.2% single / 16.4% five-net / 15.3% seven-net.* Matches
  the AlexNet abstract and Table 2 and the evidence Numbers block exactly. The
  table labels validation vs test scope per row, so the single/ensemble mix is
  not read as one measurement. The dek's "roughly ten points" credits the actual
  winning entry (15.3 vs 26.2 = 10.9), which the commission and voice guide both
  sanction; the body immediately sharpens it. Holds.
- *2010: 17.0% top-5 vs 25.7% best published prior.* Matches the paper (the
  chart's 28.2% for 2010 is the *contest winner*, a different and correctly
  labeled measure — "Winning top-5 error" — not in conflict). Holds.
- *DanNet / Ciresan preceded AlexNet.* 0.23% MNIST and beating humans "twice as
  many errors" on traffic signs, GPU-trained, published months before AlexNet
  and cited by it. Confirmed against Ciresan/Meier/Schmidhuber (s4) and the
  AlexNet citation list. Holds; correctly framed as method-predating, not
  invention.
- *Three-owner supersession.* LRN retired by BatchNorm (s6), convolutional form
  challenged by ViT (s7). Each attributed to its own primary; none stated as a
  universal verdict. The ViT "large scale training trumps inductive bias" and BN
  "with Batch Normalization it is not necessary" quotes are body-text quotes the
  evidence record verified in full; the hrefs resolve to the correct papers.
  Holds.
- *CHM three ingredients / "Each of these needed the other."* s5 (secondary)
  confirms the phrase, the three ingredients, and DanNet as a named precedent.
  Cited only for framing, never for a number, per the evidence guidance. Holds.

**The one break — Recht et al. (s8), a directional error against the primary.**
The draft read: the 11–14 point drop on a fresh ImageNet test set was "a sign
that some of the benchmark's later gains had fitted the specific test images
rather than the task of seeing in general." That is the test-set-adaptivity
(overfitting) explanation — precisely the one Recht et al. rule *out*. Opening
the paper confirms it: "the accuracy drops are not caused by adaptivity, but by
the models' inability to generalize to slightly 'harder' images." The article
asserted the opposite of the owning primary's finding. I cut the false clause
(see Edits); the surviving prose — established models lose 11–14 points on a
fresh, same-distribution test set — is accurate and coherent, and the honest
implication (reported accuracy overstates generalization) is left standing.

**Citations.** All eight hrefs opened and resolved to the source itself (s3 is
the ImageNet CVPR-2009 PDF on the official image-net.org, a 3.3 MB file that
downloads directly). Every `data-nb-kind` is correct: 7 primary + 1 secondary,
clearing the series floor (6 / 3 primary / 1 secondary). No sourcing failure.

**Display text.** Headline, dek, and all five subheads verified descriptor by
descriptor. "Fourteen years later" (2012→2026) checks. The dek makes a
world-claim, not a self-grade; it avoids the negative-reveal mold, the
"shorthand" pivot, the "actually" mold, and the comma-and-"and" mold. On the
writer's flag: **keep "gaming GPUs."** The GTX 580 is NVIDIA's consumer GeForce
(gaming) line, so the label is accurate; it gives a 2026 reader the handle the
voice guide asked for; and the body names the exact model, 3 GB, and citation.
"Consumer" is blander and the bare model name is jargon in a headline. Kept.

## Cut

The prose is disciplined: single-purpose sentences, controlled long ones, no
semicolon chains, no em-dash reflex, no banned-term slop surfaced. The
credit-then-correct refrain ("real and large," "None of this shrinks the
achievement") recurs, but that repetition is the motif the voice guide licenses,
not a formula to break; the two instances sit at a section close and the
takeaway landing, where the register wants them.

Furniture earns its place: the "In plain language" note is a sanctioned label
for a plain-language rendering of a work's claim, and it carries the depth
thesis as deliberate emphasis. The table is the right form for the
single/ensemble rows. The heading set reconstructs the argument when skimmed and
varies its cadence.

The worst tell was not a stylistic one — it was the Recht clause inverting its
source (handled in Skeptic/Edits). No prompt leakage: the "three preconditions"
framing traces to the CHM primary, not to the commission's planning language;
no planning labels, selection rules, or assignment-fulfilled claims survive into
prose.

## Reader

Read straight through as the paper's smart newcomer, the piece gives what the
sources alone would not: the single-vs-ensemble sharpening, the DanNet
precedence, and the three-separately-owned retirements welded into one generous
reading that credits the win *and* corrects the shorthand without tipping into a
debunk. That matches the draft-handoff's original-work sentence, and the article
delivers it. The convolution is taught Olah-style — the stencil slid across the
image, felt before it is named — so the prose sits closer to the voice-guide
exemplars than to a median AI summary. The headline, reread as the largest
claim, is true and concrete.

## Edits

- Cut the false interpretive clause on Recht et al.: removed ", a sign that some
  of the benchmark's later gains had fitted the specific test images rather than
  the task of seeing in general" (contradicted the owning primary, which
  attributes the drop to genuine generalization difficulty, not test-set
  adaptivity). Ran `nb stamp` (words 2154 → 2131, reading_minutes 9, sources 8).

## Required work

- **Writer — chart-1 honesty (blocking).** The line chart plots only 2010
  (28.2%), 2012 (15.3%), and 2014 (6.7%) and connects them with straight
  segments, omitting the 2011 and 2013 contests. A line asserts continuity, but
  the 2011 winning top-5 (~26%) sits far above the drawn 2010→2012 segment, so
  the chart flattens AlexNet's 2012 break into a smooth slope and misrepresents
  the two skipped years. Rebuild with all annual winning top-5 errors 2010–2014
  (values are in Russakovsky, s2 — pull 2011 and 2013 exactly), which also
  sharpens the article's own point that AlexNet was a discontinuity; or switch to
  a form that does not imply the missing years. Axis, zero baseline, labels, and
  the AlexNet annotation are otherwise honest. Editor does not edit assets.
- **Writer — byline placeholder (blocking, display).** The visible byline reads
  "N min read". `nb stamp` writes `reading_minutes` to nb-meta but not the
  visible line (confirmed: it still shows "N" after this round's stamp), and
  nb.js has no reading-time logic. Fill the byline with the stamped value (9) so
  the published page does not show a literal "N", or confirm the site build
  injects it.
- **Writer — optional, non-blocking.** The Recht caveat now states the fact
  (11–14 point drop on a fresh test set) without its significance. If the desk
  wants the significance spelled out, one honest sentence may be added, matching
  the primary: the drop reflects genuine difficulty generalizing to slightly
  harder same-source images, so reported ImageNet accuracy overstates real
  generalization — not test-set overfitting. Polish only; the blocking error is
  already cut.

## Decision

Revise. Two publication-blocking items remain, both owner **writer**: the chart's
trend line misrepresents the omitted contest years, and the byline shows the
literal "N min read". The content error against Recht was fixed by direct cut;
after the writer clears the two items and re-runs the proof, the piece is sound.

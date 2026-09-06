# Editorial review: the-evidence/dropout (editor/01)

## Skeptic

Thesis: the 2014 dropout paper measured, in its own dataset-size experiment, the
conditions under which dropout stops paying, and the largest models now training
with dropout turned down or off is the continuation of that measured boundary,
not a later reversal of the paper. The piece therefore lets a reader correct
anyone who calls dropout a universal necessity.

The claims it stands on and how each held:

- The mechanism (keep each unit with probability p, zero the rest, drop whole
  units not weights, scale outgoing weights by p at test time; hidden p=0.5,
  input p=0.8). Checked against the JMLR paper (Fig. 2, Sec. 4) and the 2012
  report. All correct. The worked p=0.5 arithmetic in the scaling paragraph is
  sound: a unit kept half the time sends on average half its signal, so halving
  its test-time weights preserves the expected input.
- The authors' justification (co-adaptation, and the average over 2ⁿ
  weight-sharing thinned networks), stated as theirs and as approximate. Checked
  against Sec. 1 and Sec. 7.5. The ~50-sample Monte-Carlo match is right, and the
  piece correctly lands it as an intuition backed by an approximation, not a
  theorem. This is the honesty move the round asked me to verify, and it holds.
- The benchmark table. Every cell checked against the evidence record's Numbers
  and the owning tables: MNIST 1.60/1.06, SVHN 3.95/2.55, CIFAR-10 14.98/12.61,
  CIFAR-100 43.48/37.20, ImageNet-2012 top-5 ≈26/16.4, TIMIT 23.4/21.8, Reuters
  31.05/29.62. All match. The caption correctly carves out the ImageNet row as
  top-5 against the best classical result.
- The dataset-size finding (no gain at 100-500, a rise, then a decline as data
  grows). Direction and endpoints match Sec. 7.4.
- The present-day arc. Transformer cut to 0.1 base, 0.3 for the large EN-DE model,
  ablation still "very helpful," cited to Vaswani (the 2025 paper's erroneous "0.3
  at each layer" does not appear). PaLM pretrained without dropout, 0.1 for
  finetuning. 2025 Stanford study on removal; LLaMA reports none. All match the
  primaries. The two required cautions are present: not abandoned (still 0.1 in
  the Transformer, in PaLM finetuning, after batch-norm in vision), and the
  switched-off claim rests on the few labs that disclose a setting, not a survey,
  with frontier settings named as undisclosed.

Two breaks with the evidence, both in supporting causal explanations, both fixed
directly from the owning primary (JMLR 2014, already cited s1, which I opened):

1. Training-time cost. The draft said dropout raised training time 2-3x "because
   each pass updates only part of the network." Sec. 11 says the cause is noisy
   parameter updates: each case trains a different random architecture, so the
   gradients are not those of the final network. The draft's reason was wrong and
   mechanically backwards (updating less per pass would not imply a slowdown). I
   replaced it with the paper's own reason.

2. Why dropout gives no gain at 100-500 examples. This was inverted. The draft
   said the network "could not learn even the useful structure, so there was
   nothing yet for the extra regularization to protect against" — i.e.,
   underfitting. Sec. 7.4 says the opposite: "The model has enough parameters that
   it can overfit on the training data, even with all the noise coming from
   dropout." The set is small enough to be memorized regardless, so dropout has no
   gain to win. I rewrote the sentence to the paper's mechanism. This one mattered:
   the dataset-size experiment is the spine of the whole argument, and a reader who
   took the draft's version would carry away the wrong reason for the left end of
   the curve.

Neither break touched a central claim, and both corrections came from the cited
primary, so nothing routes to the researcher or writer.

Every citation href was opened as printed and lands on the source: the JMLR HTML
and PDF, the two arXiv tech reports, Vaswani, the disharmony paper, PaLM, the 2025
study, and the Semantic Scholar record. The two Background links and the added
Transformer cross-link resolve against the library checkout. Every data-nb-kind is
correct: Semantic Scholar is the sole secondary (a citation index, the right label
for a count it owns rather than authors), and the six primaries each own the claim
they carry.

## Cut

Five sentences failed the slop test and were cut or rewritten to the fact
underneath:

- A signpost opening the second mechanism paragraph ("Two details in that sentence
  do the work"). Cut, with the "First/Second" scaffolding, keeping both facts.
- An empty lead-in to the approximation point ("The authors are careful about how
  far that averaging claim reaches"). Cut; attribution survives in the next
  sentence's "they also averaged."
- A self-grading tail ("an experiment that turns out to be the important one"),
  reduced to "the paper measured why."
- A self-grading landing ("That is the honest hinge of the whole paper"). Cut; the
  paragraph now opens on the claim it was grading.
- A method summary ("Two cautions keep this from becoming a bigger claim than the
  evidence supports"). Cut; the two cautions stand on their own.

The body twice addressed the reader, which this press reserves for the two
bookends: the scaling paragraph ("if you could not then use... you run... you
multiply") and the today opener ("Follow that curve... you arrive"). Both recast
to the third person without losing a fact. Four house-style semicolons joining
independent clauses were made periods (scaling arithmetic, Transformer sentence,
table caption, the not-abandoned caution).

Edges checked on their own: the section openers and closers carry claims, not
filler. The dek is number-first with a verb and clear of the banned molds
(comma-triad, semicolon-reversal, negative-parallelism, suspended question). The
headings vary in build and reconstruct the argument in order; none is the
"What X took to build" counting shape or a negative-closer, and none joins two
clauses with a comma and "and." No Verdict block, no house catchphrase, no
borrowed phrasing from the voice-guide exemplars. The two negative contrasts that
remain ("units, not individual weights"; "not that dropout was abandoned") each
correct a misconception the piece names, so they are earned. The "In plain
language" note earns its place: it ties the ensemble idea back to the earlier
scaling rule rather than restating the paragraph above it.

## Reader

Read straight through, the piece gives what the sources alone would not: the 2014
paper's own dataset-size boundary read forward onto the disclosed dropout settings
of later large-data models, so that today's turned-down dropout is the same curve
extended, not a refutation. That is the original-work claim in the handoff, and it
survives on the page, carried by the data-size and today sections and landed in
the takeaway. The prose sits closer to the voice-guide exemplars than to a median
summary: plain mechanism, a worked value of p, the reversal stated as flatly as
the original claim, and scope named exactly (disclosed reports, not a survey; an
approximation, not a theorem). The headline reads as the largest claim the piece
defends, with the disclosure caveat carried honestly in the body.

## Edits

- Cut the signpost "Two details in that sentence do the work" and the First/Second
  scaffolding; kept both mechanism facts (orientation).
- Recast the scaling paragraph from second person to third ("the finished network
  could not then be used"; "the complete network runs once"; "each unit's outgoing
  weights are multiplied by p") and split its semicolon into two sentences.
- Cut the empty lead-in "The authors are careful about how far that averaging
  claim reaches" (ensemble).
- Corrected the training-time cause: from "because each pass updates only part of
  the network" to the paper's reason (noisy updates, each pass fitting a different
  thinned network, gradients not aimed at the full test-time network) (results).
- Reduced "the paper says why in an experiment that turns out to be the important
  one" to "the paper measured why" (data-size).
- Corrected the inverted small-data explanation to the paper's actual mechanism
  (the network overfits so small a set even with dropout's noise, so there is no
  gain to win) (data-size).
- Cut the self-grading sentence "That is the honest hinge of the whole paper"
  (data-size).
- Recast the today opener from "Follow that curve... you arrive" to "The same
  curve, extended toward far larger datasets, describes how dropout is used now."
- Added a prose link from the first "Transformer" mention to the
  attention-is-all-you-need lesson, and split the sentence's semicolon into a
  period (today).
- Cut the method-summary sentence "Two cautions keep this from becoming a bigger
  claim than the evidence supports" (today).
- Changed the table caption's semicolon and the not-abandoned caution's semicolon
  to periods.

## Required work

None blocking. Ran `nb check ... --series the-evidence --library
/home/user/library-checkout` read-only after the edits: BLOCK 0, WARN 0,
PUBLISHABLE. One optional enhancement, not a condition of approval: the paper's
Figure 10 (the dataset-size curve) is the argument's central visual, and a reader
could test the rise-then-fall better against the two converging lines than against
prose. The record has no numeric series for it, so it would be a cropped source
asset, not a chart, and belongs to the writer's capture tooling if a later pass
wants it on the page.

## Decision

approve — the central honesty claims hold against the primaries, the two causal
errors and the slop are fixed in place, and the piece passes proof clean.

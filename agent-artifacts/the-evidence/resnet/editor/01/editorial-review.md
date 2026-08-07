# Editorial review: the-evidence/resnet (editor/01)

## Skeptic

Thesis: ResNet is remembered as a win for depth, but the paper's real finding
is an optimization failure (the degradation problem) that a parameter-free skip
connection fixed, and that same skip connection is now load-bearing inside the
transformer. The claims it stands on:

1. A deeper plain network fit its *training* data worse than a shallower one,
   and this is not overfitting (the degradation result, Fig. 1).
2. The identity solution provably exists inside the deeper network, yet gradient
   descent does not find it; rewriting each block as F(x)+x makes "do nothing"
   the optimizer's default and reverses the trend.
3. Depth is not the whole story: the 1202-layer CIFAR net trained fine yet
   scored worse than the 110-layer net (overfitting, not optimization).
4. The paper explicitly rules out vanishing gradients; the "ResNet solved
   vanishing gradients" gloss misreads it. Its generality claim was a forecast
   that named no architecture, not a demonstration and not a prediction of the
   transformer.
5. The residual connection is reused in the transformer's "Add & Norm" step,
   sourced from the attention paper itself.

I tried to break each against the evidence record and cited primaries.

- **Training vs. test error (round focus).** Held. The degradation section keeps
  the distinction to the sentence, not just the paragraph: "Not on the test set
  ... It does worse on the training set itself." The chart is honestly walled off
  as *validation* error and used only for the 18-vs-34 reversal, so it never
  smuggles the training-error point in through a test-error figure. Matches the
  voice guide's core demand.
- **The 1202-layer fact (round focus).** Held and honest. "It trained without
  difficulty, its training error under 0.1%, no sign of the degradation problem
  at all. It still scored worse on the test set than a 110-layer network, 7.93%
  against 6.43%." Numbers match Table 6 / Sec. 4.2 in the evidence record, and
  the cause is correctly attributed to overfitting, not optimization. This is the
  honest counter to "just add more layers" and it survives.
- **The two required corrections (round focus).** Both honored. (a) The article
  states the generality *forecast* in the paper's own words, then says plainly it
  "was a forecast, not a demonstration. It named no architecture, and the
  transformer ... did not yet exist." It does not claim the paper made no
  generalization claim. (b) The vanishing-gradient gloss is the article's single
  named-misreading hinge: granted its strongest form ("a reasonable belief to
  hold ... vanishing gradients were the known reason"), then separated from the
  record with the Sec. 4.1 quote in the note block. The article never repeats
  the gloss as fact.
- **Add & Norm reuse (round focus).** Sourced. The transformer claim carries
  citation 6 (the attention paper), quotes its own "Add & Norm" label, and notes
  it "cit[es] this paper by name." Attention itself is linked out to the
  the-mechanics lesson, not re-taught; the transformer architecture is not
  re-explained. Correct scoping.
- **Numbers.** Spot-checked every figure against the evidence Numbers section:
  reversal 27.94/28.54 plain vs 27.88/25.03 residual (Table 2); 4.49% single-model
  top-5 and 3.57% ensemble (Tables 4/5); 11.3e9 vs 19.6e9 FLOPs and "eight times"
  (Table 1, Fig. 3); 1001 layers at 4.62% (He 2016); "hundreds of thousands" of
  citations (235,644, Semantic Scholar). All land.

Display text, descriptor by descriptor: headline "The deeper network fit its
training data worse" is the degradation result stated as a finding, true and
supported. Dek attributes the sweep to Microsoft, names the mechanism (adding
the input back), and the transformer reuse, all sourced; it makes claims about
the world, does not grade the article, and does not restate the headline.
"Microsoft Research," "four researchers," "December 2015," "five tracks," and the
five named tracks all check against the abstract. No wrong labels in display text.

Sourcing kinds: s1/s3/s4/s5 primary and s6 primary-for-the-reuse-claim are all
consistent with the evidence record's own kind judgments; s2 (Semantic Scholar)
is correctly a secondary citation index reporting from outside. Both internal
Background links (`../the-evidence/alexnet.html`,
`../the-mechanics/attention.html`) resolve in the series library checkout, as do
all six external `href`s per the passing link check.

One soft spot, non-blocking: "eight times deeper than the best network from the
year before." The 8x figure is only true against VGG-19 (which the article names
correctly later, "the shallower VGG-19 it displaced"); GoogLeNet, not VGG, won
2014 classification, so "the best network from the year before" is loosely stated.
The load-bearing fact is anchored elsewhere, so this does not block, but the
writer may want to tie the phrase to VGG where it first appears.

## Cut

The prose is tight; the earns-its-place test found little dead weight. One real
cut made:

- In the legacy section, "the skip connection helps by changing what the layers
  must learn, **not by rescuing a signal that was disappearing**" restated the
  correction the same sentence had already made ("a failure of optimization, not
  a signal fading away") and that the whole paragraph plus the note block had
  established. Two "not" clauses back to back, the second carrying no new cargo.
  Cut the second clause.

Worst tell, and the one pattern worth naming: the not-X/it-is-Z contrast (and
its "rather than" / "instead of" cousins) recurs heavily, because the lesson's
whole subject is a counterintuitive correction. I counted the bookend ("harder
to train rather than easier"), orientation ("not to depth for its own sake"),
degradation ("not failing to generalize ... it is failing to learn"), residual
("no longer a needle ... it is the resting position"), the vanishing-gradient
hinge, and the takeaway. The house ceiling is one or two, but that ceiling
targets the *invented-strawman* contrast, and none of these are invented: each
separates a real, named distinction the reader is meant to hold (training vs.
test, trainable vs. better, optimization vs. depth). They are the substance of
the lesson, not reflex punctuation. Trimming the redundant instance above pulls
the density down without flattening the voice; I did not prune the load-bearing
ones, which would regress the piece toward a median summary. Flagging the pattern
so a later round watches it rather than adds to it.

No prompt leakage: authored text does not echo the writer brief's planning
language ("present-day payoff," "make it click"); "degradation problem" and "Add
& Norm" are the source's own terms, not instructions. No self-grading or
signposting in the body; the "This lesson reads ..." framing sits in the Why-this-
matters bookend, which the template licenses. Headings reconstruct the argument
in the piece's own nouns and avoid scaffolding slots. Grammar and punctuation are
clean, including the dek's trailing absolute phrase (not a splice). The chart is
honest: zero baseline, value labels, axes labeled, source in the caption, numbers
matching Table 2.

Recent-pattern check: the headline breaks the recent the-evidence "credited-with
X / never did Y" mold (it states a finding), and the dek breaks the "declarative +
'and' clause" mold that recurs across alphafold, scaling-laws, and chinchilla (it
uses a trailing absolute phrase, no "and"). Neither inherits a stamped shape.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: the degradation result as a construction I
perform, build the 56-layer net by copying a working 20-layer net and setting the
extra layers to pass their input through, confirm the good solution provably sits
inside the deeper net, then watch training fail to reach it. The paper *states*
this; the article makes me *derive* it, and then reuses the same identity
construction to show why F(x)+x makes "do nothing" the optimizer's resting
position. That is a genuine transfer of understanding, not a restatement, and it
matches the original-work sentence in the draft handoff. The prose sits close to
the Olah/Karpathy exemplars: physical mechanism run in the reader's head, the
"you" spent exactly where forward intuition and backward consequence diverge, not
a median AI summary. Headline reread as the largest claim holds. The piece earns
its place.

## Edits

- Cut the redundant trailing clause "not by rescuing a signal that was
  disappearing" from the legacy-section sentence; the point was already made in
  the same sentence and paragraph.
- Ran `nb stamp` (words 1999, 9 min, 6 sources); re-ran `nb check` with links:
  BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

- **writer (mechanical):** re-run the proof to close the round; the direct cut is
  already stamped and the check passes, so no editorial rework is required.
- **writer (optional, non-blocking):** consider tying "the best network from the
  year before" to VGG where the "eight times deeper" claim first appears, since
  the 8x figure is exact only against VGG-19.

## Decision

approve — every load-bearing claim held, both required corrections and all
round-focus items are honored, the one redundant contrast is cut and re-stamped,
and the only remaining writer items are the mechanical re-proof and an optional
precision tweak.

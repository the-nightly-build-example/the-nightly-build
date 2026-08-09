# Editorial review: the-evidence/batch-normalization (editor/01)

## Skeptic

Thesis: batch normalization delivers exactly the numbers its 2015 paper
claimed, but the paper's own explanation for the speed — that it reduces
internal covariate shift — fails a controlled test, and the field has not
agreed what replaces it. The load-bearing claims: (1) the technique's numbers
hold (14x fewer steps to 72.2%, 4.82% ensemble top-5); (2) the paper defined a
specific *distributional* internal covariate shift and put the reason in its
title; (3) Santurkar 2018's noise experiment drove that distribution shift up
and training did not slow; (4) no successor mechanism is settled.

I pushed hardest where the brief aimed me. The distributional-versus-gradient
distinction holds: the "test" section states plainly that Ioffe and Szegedy
defined internal covariate shift as a change in the *distribution* of a layer's
inputs, that Santurkar *redefined* it in terms of the gradient across the update
step, that "the two definitions are not the same quantity," and — critically —
that the noise experiment strikes "the paper's own distributional version
head-on." The refutation is correctly pinned to the distributional claim, not to
Santurkar's reformulation. No slide between the two.

The 5.1% human figure is attributed correctly. The clause that the batch-norm
paper "noted" it beat a human rater is cited to Ioffe and Szegedy (s1); the
5.1% value itself, its one trained annotator, and its 1,500-image denominator
are cited to Russakovsky (s2), with the second annotator (12.0% on 258 images)
and the 100,000-image full test set stated beside it. This matches the evidence
record's owner assignment and its caution. Verified against the evidence:
72.2% single-crop accuracy, 2.1M vs 31M steps, 4.82% test error / six-model
ensemble, the VGG-on-CIFAR-10 two-orders-of-magnitude gradient predictiveness,
the Lp-normalization non-uniqueness, Bjorck's learning-rate account, and Wu &
He's 10.6-point small-batch gap. Every display-text figure (dek, the 14x /
72.2% and 4.82% stat strip, the note's verbatim ICS definition and its
"Section 2" attribution) checks out. The annotated equation is the standard
Ioffe-Szegedy transform and each legend term (mu, sigma-squared, gamma, beta)
is described correctly.

The ending does not sell a settled successor: smoothing is undercut in the same
paragraph that raises it (plain Lp norms smooth as well or better), Bjorck is
given as a competing account, the textbook records an open question, and the
takeaway lands on "still an open question." Honest.

Citations: all six printed hrefs open to the source itself and return 200
(arXiv abstract pages for s1–s4 and s6; the d2l chapter for s5); the two "Go
deeper" links resolve too. The four in-prose cross-links (alexnet, resnet,
distribution-shift, gradient-descent) all exist in the published library.
data-nb-kind audit: s1–s4 and s6 primary, s5 (d2l textbook) secondary — 5
primary / 1 secondary, correct; the secondary is a genuinely independent author
group, and the central contradiction, though owned by a primary (Santurkar), is
attributed in prose as their claim rather than asserted as settled, with the
independent textbook corroborating that the field treats ICS as contested. No
break routed to the researcher.

## Cut

A slop pass over every sentence, including display text and both bookends,
turned up two failures and one tense break; I fixed all three directly.

One empty-conclusion tail: "beating one careful person on a small sample of the
task, which is a real result and a narrow one." The trailing "a real result and
a narrow one" is the exact shape slop.md names ("The gap is real, and it is
narrow"), and the narrowness is already carried by "one careful person on a
small sample." Cut to end the sentence at "task"; the generosity (they did beat
a careful annotator) survives in the clause that remains.

One borrowed clause: "The story is intuitive, and it reads like something a
textbook would state without apology." The second clause lifts the voice guide's
own Ball annotation ("reads like something a textbook would say without
apology"), swapping only say/state — a lightly rewritten borrow, not caught by
the slop test because it reads as specific. The respectful setup the voice guide
wants is already delivered concretely by the following sentence ("A shifting
input distribution sounds like a problem, and holding it steady sounds like a
fix"), so I deleted the whole sentence rather than replace the phrase.

One correctness fix: the closing triad mixed tense ("The networks train faster,
the accuracy numbers held up, and batch normalization remains"). Changed "held
up" to "hold up" for parallel present.

Openers, closers, headings against the recent record: the flagged Evidence
opener mold ("You have almost certainly seen…") recurs in word2vec, resnet,
alexnet, and gans; this Why card's conditional "If you have read this desk on
AlexNet or ResNet, you have already met…" clears it. The Why card does not close
on "By the end you can say exactly…". The four section headings vary in build
(noun phrase, relative clause, full sentence, paired appositive) with no comma +
"and" join. No "None of this makes X fake," no "Now you know…" / "The next time
you see…" closer, and the note label names its term ("Internal covariate
shift") rather than defaulting to "In plain language." Furniture (stat strip,
math figure, note) each carries evidence a reader needs.

## Reader

Read straight through as the paper's smart, non-coding reader, the piece gives
what six papers and a textbook would not hand over on their own: the technique's
numbers held apart from the paper's title-claim, the one controlled experiment
that raises the distributional shift on purpose and finds training unmoved, and
the honest landing that the replacement is genuinely unsettled — with the phrase
outliving the mechanism it named. That matches the draft handoff's original-work
sentence (staging the technique against its own explanation and holding both the
intact standing and the failed reason in one frame). The prose sits closer to
the voice-guide exemplars than to a median summary: the ICS story is stated with
respect, the correction is delivered flat once ("The only trouble with that
reason is that it does not survive a direct test"), the technique's standing is
preserved, and the human-baseline denominator gives the Mastroianni-style
concrete number. The one spot that reaches for median-summary punch is the
takeaway coda (see Required work). The headline, reread as the largest claim —
"The batch normalization paper got its own explanation wrong" — is subject, verb,
surprise up front, and a claim the piece defends; no colon template, no hedge.

## Edits

- Deleted "The story is intuitive, and it reads like something a textbook would state without apology." (borrowed clause from the voice guide; setup already carried by the next sentence).
- Cut the tail "which is a real result and a narrow one" so the sentence ends at "…on a small sample of the task." (empty-conclusion shape; narrowness already stated).
- Changed "the accuracy numbers held up" to "the accuracy numbers hold up" (parallel-tense fix in the closing triad).
- Ran `./nb stamp`: words 1877 to 1853, reading_minutes 8, sources 6.

## Required work

- writer: The takeaway closes on "The technique is not in doubt. The explanation
  printed in its title is." The voice guide directs the "not X, it's Y" contrast
  to be earned exactly once, on the mechanism, and explicitly "not… in the
  takeaway." The draft handoff confirms it was landed twice by design, once here.
  This engineered antithesis coda restates an already-stated finding for
  quotable effect (slop.md, unearned punchline) in the one location the voice
  guide barred. It is the ending, so it is not mine to cut. Land the takeaway on
  the finding already present ("still an open question… more than one serious
  answer is on the table") while keeping the technique's intact standing, without
  the two-beat antithesis coda.

## Decision

revise — the article is sound on substance, sourcing, and figures and its slop
cuts are made, but the takeaway's antithesis coda breaks the voice guide's
explicit "not in the takeaway" instruction and belongs to the writer to reland.

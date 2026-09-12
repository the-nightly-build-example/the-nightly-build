# Voice guide: the-instruments/f1-score

## How this piece should sound

This is a lesson on the F1 score for a reader who is quick but has never been
shown how the number is built. The register is plain and unhurried: define
precision and recall, then their harmonic mean, in words a reader could repeat
to someone else afterward. Hold a steady, skeptical-but-fair stance toward a
figure that sits under leaderboard after leaderboard, willing to say where F1
misleads and willing to say what it genuinely supports.

Teach precision and recall the way Allen Downey teaches the inspection paradox:
with counts small enough to hold in the head. His class-size passage carries its
whole surprise on two numbers, 56 and 31, and resolves it with ten chances
against a hundred. Where this lesson introduces a confusion matrix, the
arithmetic can be small enough that the reader totals it before any formula
appears, and the reason the harmonic mean falls toward the smaller of precision
and recall can be shown on a worked pair as much as argued from the algebra.

The prose can afford Downey's plainness. He closes an explanation on "because,
well, it's longer" and speaks to the reader as a person ("with your luck")
without lecturing, and each time the payoff is a real quantitative claim. A
sentence that says plainly why the harmonic mean punishes a lopsided pair is
doing that same work.

The skepticism is earned the way Cosma Shalizi earns his. Before rejecting the
general factor g, he grants the theory behind it real scope and real content,
then shows exactly how it failed. F1 has genuine uses, and saying so plainly, in
the way Shalizi keeps what a technique measures separate from what people
conclude from it, is what lets the harder points land as fair: that F1 ignores
true negatives, that its value depends on which class is called positive and on
class balance, and that micro and macro averaging can disagree on the same
predictions. The reader should meet each of those having already been shown what
the number does well.

When the lesson computes what F1 hides, Cathy O'Neil's coin-flip passage is the
model for showing arithmetic. She recasts an opaque score as something
countable, does the sum in the open, states each simplifying step as she takes
it, and ends on a figure the reader can check. And where a verdict on F1 is
earned by the counts, it can be stated as flatly as O'Neil states hers: she
names the score, calls it what she has shown it to be, and stands behind the
claim.

## Allen Downey, "The Inspection Paradox is Everywhere"

Source: http://allendowney.blogspot.com/2015/08/the-inspection-paradox-is-everywhere.html

> "The inspection paradox is a common source of confusion, an occasional source
> of error, and an opportunity for clever experimental design. Most people are
> unaware of it, but like the cue marks that appear in movies to signal reel
> changes, once you notice it, you can't stop seeing it."

Downey says what the paradox does, and to whom, before he defines it, and the
comparison to movie reel marks gives the reader something concrete to picture at
the outset. The plain confidence of the last clause is a teacher who has
explained this many times and knows the reader will keep meeting it.

> "Suppose you ask college students how big their classes are and average the
> responses. The result might be 56. But if you ask the school for the average
> class size, they might say 31. It sounds like someone is lying, but they could
> both be right.
>
> The problem is that when you survey students, you oversample large classes. If
> there are 10 students in a class, you have 10 chances to sample that class. If
> there are 100 students, you have 100 chances."

Two numbers, 56 and 31, carry the whole surprise, and Downey lets the reader
feel the contradiction before he resolves it. The mechanism then arrives as
counts a reader can hold: ten students give ten chances, a hundred give a
hundred. He teaches the idea with arithmetic small enough to check in your head
rather than a formula.

> "Buses and trains are supposed to arrive at constant intervals, but in practice
> some intervals are longer than others. With your luck, you might think you are
> more likely to arrive during a long interval. It turns out you are right: a
> random arrival is more likely to fall in a long interval because, well, it's
> longer."

The explanation ends on an ordinary phrase that states the reason instead of
dressing it up. "With your luck" is Downey talking to the reader as a person
without lecturing, and the sentence still delivers a real quantitative claim.

## Cosma Shalizi, "g, a Statistical Myth"

Source: http://bactra.org/weblog/523.html

> "Factor analysis is handy for summarizing data, but can't tell us where the
> correlations came from; it always says that there is a general factor whenever
> there are only positive correlations. The appearance of g is a trivial
> reflection of that correlation structure."

Shalizi says in flat declaratives what the technique can do and what it cannot,
and keeps what the number measures apart from what people take it to mean. The
judgment is exact and unhedged, and a reader knows precisely what is being
claimed.

> "The two-factor theory was a genuinely scientific theory of considerable scope
> and empirical content, which would have been very important if it was true. The
> way we can unambiguously tell that it had falsifiable empirical content is that
> it was, in fact, falsified. Looking at larger and more diverse data sets, it
> became clear that the partial correlations among scores on mental ability tests
> were not zero, or even close enough to attribute the difference to chance. Put
> to reasonably severe tests, it failed."

Before rejecting the theory, Shalizi grants it everything it deserves: real
scope, real content, real importance if it were true. Then he shows it failed,
and shows how we know, by pointing at the partial correlations. The skepticism
reads as fair because he stated the opposing case in its strongest form first.

## Cathy O'Neil, "The arbitrary punishment of New York teacher evaluations"

Source: https://mathbabe.org/2015/04/02/the-arbitrary-punishment-of-new-york-teacher-evaluations/

> "The Value-Added Model for teachers (VAM), currently in use all over the
> country, is a terrible scoring system, as I've described before. It is
> approximately a random number generator.
>
> Even so, it's still in use, mostly because it wields power over the teacher
> unions. Let me explain why I say this."

O'Neil states her verdict in the first two sentences and names the number she is
judging. "Let me explain why I say this" is a writer taking responsibility for a
strong claim and promising the working, which is what keeps a blunt verdict from
reading as a slogan.

> "Think of it as a biased coin flip, and 30% of the time – for any teacher and
> for any year – it lands on "ineffective", and 70% of the time it lands on
> "effective." We will ignore the other categories because they don't matter.
>
> How about if you look over a four year period? To avoid getting any
> "ineffective" coin flips, you'd need to get "effective" every year, which would
> happen 0.70^4 = 24% of the time."

She recasts an opaque score as a biased coin flip and then does the arithmetic
in front of the reader, ending on a figure they can check. She declares the
simplifying step as she takes it ("We will ignore the other categories because
they don't matter"), so the reader can see exactly what the 24% rests on and
could redo the sum.

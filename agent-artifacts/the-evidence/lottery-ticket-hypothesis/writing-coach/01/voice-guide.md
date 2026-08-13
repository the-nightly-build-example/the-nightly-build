# Voice guide: the-evidence/lottery-ticket-hypothesis

## How this piece should sound

This lesson reads one machine-learning paper back against what its experiments
actually showed, for a reader who is new to neural networks and has no time in a
codebase. Michael Nielsen's chapter sets the register the teaching can hold:
short plain sentences, the claim stated flat, and the difficulty of the thing
made concrete before any machinery arrives. When the winning-ticket claim needs
stating, it can carry its own surprise in plain words, the way Nielsen reports
that a 74-line program recognizes digits at over 96 percent and lets the number
do the work.

The paper's genuine surprise sits in a mechanism: the surviving weights are
reset to their *original* initial values, and a pruned network reinitialized at
random does not match the result. Nielsen's setup passage, where he says what we
would want from a small change in a weight before he shows why perceptrons do not
give it, is one shape this teaching can take. Where the lesson walks iterative
magnitude pruning and the reset-versus-random comparison, the material may call
for stating the expectation the reader would bring first, then showing what the
experiment did instead, rather than describing the procedure flat.

The desk's job is to show the size of the foundation under a famous claim. Dan
Luu gives a striking figure and then, in the next short sentence, reports that it
did not hold: the ten-point IQ boost, then no significant difference by age ten.
The winning-ticket result was demonstrated on small vision networks trained on
MNIST and CIFAR-10, at particular sparsity levels, matching a particular
accuracy. Where the lesson sizes the experiment, the claim and the scale it was
shown at can sit in the same plain voice, close enough that the reader can weigh
one against the other without being told how to read them.

The phrase "winning ticket" now travels further than the experiment reached: the
tickets were found by pruning after training, in retrospect, not located cheaply
before training starts. Where the lesson marks the distance between what the
paper proved and what the shorthand is used to mean, Dan Luu's refusal to hand
the reader a tidy trick at the close, and Karpathy's habit of stating a verdict
flat, both show a limit named plainly and left to rest on the facts already
given. A judgment here does not need dressing up or hedging once the numbers are
in front of the reader.

When the lesson reports what later work changed, the material may call for naming
the specific thing that moved, the way Karpathy names an exact failure (labels
not flipped with the image, and the network quietly learning to flip its own
predictions back) and Dan Luu names the drug and the dollar figure rather than
"a treatment" or "a lot of money." Dataset names, sparsity levels, the accuracy
matched, and the exact change a follow-up introduced carry more than "small
nets," "high sparsity," or "a fix."

## Andrej Karpathy, "A Recipe for Training Neural Networks"

Source: http://karpathy.github.io/2019/04/25/recipe/

> "It is allegedly easy to get started with training neural nets. Numerous
> libraries and frameworks take pride in displaying 30-line miracle snippets that
> solve your data problems, giving the (false) impression that this stuff is plug
> and play."

The passage names a specific false promise, the 30-line snippet and the "plug
and play" pitch, instead of saying in the abstract that training is harder than
it looks. Karpathy is visible in the "(false)" dropped mid-sentence, the aside of
someone who has watched people believe the snippet and then get stuck.

> "Everything could be correct syntactically, but the whole thing isn't arranged
> properly, and it's really hard to tell. The "possible error surface" is large,
> logical (as opposed to syntactic), and very tricky to unit test. For example,
> perhaps you forgot to flip your labels when you left-right flipped the image
> during data augmentation. Your net can still (shockingly) work pretty well
> because your network can internally learn to detect flipped images and then it
> left-right flips its predictions."

He states the general problem in one flat sentence and then grounds it in a
single concrete bug, which is what makes the general claim land. The aside
"(shockingly)" is a practitioner reacting to a thing he has actually seen a
network do.

> "As a result, (and this is reeaally difficult to over-emphasize) a "fast and
> furious" approach to training neural networks does not work and only leads to
> suffering. Now, suffering is a perfectly natural part of getting a neural
> network to work well, but it can be mitigated by being thorough, defensive,
> paranoid, and obsessed with visualizations of basically every possible thing.
> The qualities that in my experience correlate most strongly to success in deep
> learning are patience and attention to detail."

He gives his verdict as a plain pair of qualities after admitting the work "leads
to suffering," and states it rather than hedging it. The stretched "reeaally" and
the flat admission are a person talking, not a manual.

## Michael Nielsen, "Using neural nets to recognize handwritten digits"

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "That ease is deceptive. In each hemisphere of our brain, humans have a primary
> visual cortex, also known as V1, containing 140 million neurons, with tens of
> billions of connections between them. ... We carry in our heads a supercomputer,
> tuned by evolution over hundreds of millions of years, and superbly adapted to
> understand the visual world. Recognizing handwritten digits isn't easy. Rather,
> we humans are stupendously, astoundingly good at making sense of what our eyes
> show us. But nearly all that work is done unconsciously. And so we don't usually
> appreciate how tough a problem our visual systems solve."

Nielsen makes an easy thing strange by counting what the brain spends on it, the
140 million neurons and the billions of connections, so the reader feels the
difficulty before the topic is even introduced. The plain "But nearly all that
work is done unconsciously" is a teacher naming exactly what the reader takes for
granted.

> "We're focusing on handwriting recognition because it's an excellent prototype
> problem for learning about neural networks in general. As a prototype it hits a
> sweet spot: it's challenging - it's no small feat to recognize handwritten
> digits - but it's not so difficult as to require an extremely complicated
> solution, or tremendous computational power."

He explains why he chose this example, not only what it is, and grades its scale
out loud ("a sweet spot," "no small feat," "not so difficult as to require...
tremendous computational power"). Nielsen the teacher is visible in justifying
the size of his example rather than leaving the reader to wonder why it was
picked.

> "To see how learning might work, suppose we make a small change in some weight
> (or bias) in the network. What we'd like is for this small change in weight to
> cause only a small corresponding change in the output from the network. As
> we'll see in a moment, this property will make learning possible."

He states what we would want from the mechanism before he shows the mechanism, so
the idea is built from the reader's side. The plain "As we'll see in a moment" is
a teacher setting the pace of the explanation and telling the reader where it is
going.

## Dan Luu, "Goodhearting IQ, cholesterol, and tail latency"

Source: https://danluu.com/percentile-latency/

> "Initial results from Head Start were also promising; children in the program
> got a 10 point IQ boost. The next set of results was disappointing. By age 10,
> the difference in test scores and IQ between the trial and control groups wasn't
> statistically significant."

Luu gives the promising figure and then reports, in a short flat sentence, that
it did not last. He is visible in refusing to soften the reversal: the boost and
the fade sit in the same plain register, and the reader is left to see the gap
between them.

> "Given that narrative, it certainly sounds reasonable to try to develop new
> drugs that improve cholesterol levels, but when Pfizer spent $800 million doing
> exactly that, developing torcetrapib, they found that they created a drug which
> substantially increased heart attack risk despite improving cholesterol levels.
> Hoffman-La Roche's attempt fared a bit better because it improved cholesterol
> without killing anyone, but it still failed to decrease heart attack risk."

He states what sounds reasonable, then reports the concrete result that
contradicts it, with the named drug and the exact dollar figure attached. Luu
keeps the point checkable by tying every turn of judgment to a specific fact,
Pfizer, torcetrapib, Hoffman-La Roche, rather than to a general claim.

> "This is the point in a blog post where you're supposed to get the one weird
> trick that solves your problem. But the only trick is that there is no trick,
> that you have to constantly check that your map is somehow connected to the
> territory."

The closing names the payoff a reader expects and then declines to supply it.
Luu is visible in ending on the honest limit of what he can offer, in the same
even voice he used for the evidence, instead of manufacturing a resolution the
material did not earn.

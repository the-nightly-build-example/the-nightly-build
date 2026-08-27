# Voice guide: the-evidence/lora (01)

## How this piece should sound

This lesson reads the LoRA paper for a reader who is fluent and curious but has
never worked in a codebase. The register is plain and direct, closer to how the
passages below explain a method than to how the paper itself writes: state each
claim in ordinary words, and reach for the concrete case before the abstract
term. Where the paper's ideas are abstract, the "intrinsic rank" of a weight
change, or what it means to adapt a frozen model at all, the reader can usually
be handed the concrete instance first and the name second, the way Olah lets a
reader feel persistence before he calls it that.

Some of what LoRA does can look like machinery to this reader: weights held
fixed, a small pair of low-rank matrices trained beside them, that pair later
folded back into the original weights. Olah's move on the recurrent loop,
showing that a thing which looks mysterious is an ordinary operation once
restated, is available wherever a step here looks harder than it is. The
merge-back property in particular, which is what separates LoRA from adapters
that add layers at inference time, rewards being stated as plainly as Karpathy
states an RNN's interface: what goes in, what comes out, and the one fact that
makes it different.

Before the method, the cost it removes can be named as exactly as the method
itself. Karpathy states the limitation of a plain network flatly, with concrete
examples in hand, before he offers the fix. Where this lesson needs the reader
to feel why cheap specialization mattered, the price of full fine-tuning can be
given in the same concrete terms as the low-rank trick that lowers it.

The desk's discipline is honest scale, and the passages show two forms of it the
piece can use. A headline number carries its conditions with it: Karpathy
reports a striking result while naming the toy model and the arbitrary settings
behind it. And a claim that held in one place can narrow in another: Dan Luu
reports a promising early result and then the larger study that walked it back.
"Matches full fine-tuning" is a result on particular models and particular
tasks. Where later or larger work has found where that claim stops holding, the
report can say so as plainly as it states the headline.

The present-day turn has a shape the Dan Luu piece already models. LoRA now
stands in for full fine-tuning so routinely that the substitute gets treated as
the original. Where today's usage claims more than the paper showed, saying
exactly where the stand-in and the real thing diverge does the work, in the
paper's own terms rather than a general caution.

One direction comes from the brief rather than the passages: this reader has no
codebase time, so the code- and architecture-shaped details, which weight
matrices the low-rank pair attaches to, what choosing a small rank actually
sets, reach them only as prose. Anything the paper assumes a reader can picture
from an implementation has to be built in words here, or left out.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous words. You don't throw everything away and start thinking from scratch again. Your thoughts have persistence."

The article is about a network's internal state, and its first move is to point
at something the reader is doing while they read. Olah names the property,
persistence, only in the last of the four sentences, after the reader has
already felt it. He is visible in how slowly he goes: he spends four short
sentences on a point an insider would compress into one clause.

> "If we are trying to predict the last word in "the clouds are in the sky," we don't need any further context – it's pretty obvious the next word is going to be sky. In such cases, where the gap between the relevant information and the place that it's needed is small, RNNs can learn to use the past information."

He introduces the difficulty with an everyday sentence the reader can finish on
their own, and states the general point, that the gap between the clue and the
word is small, only once the example is on the page. The reader meets the
problem in concrete form and gets the term for it second.

> "These loops make recurrent neural networks seem kind of mysterious. However, if you think a bit more, it turns out that they aren't all that different than a normal neural network. A recurrent neural network can be thought of as multiple copies of the same network, each passing a message to a successor."

He names the reaction a newcomer actually has, that the loops look mysterious,
and then takes it apart by restating the mechanism in plainer terms. The
description of a recurrent network as copies of one network passing a message
forward is something the reader can follow without any new vocabulary.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "A glaring limitation of Vanilla Neural Networks (and also Convolutional Networks) is that their API is too constrained: they accept a fixed-sized vector as input (e.g. an image) and produce a fixed-sized vector as output (e.g. probabilities of different classes). Not only that: These models perform this mapping using a fixed amount of computational steps (e.g. the number of layers in the model)."

Before naming his solution, Karpathy states the exact limit he is working
against and pins each abstract term to a concrete example in parentheses: an
image, class probabilities, the number of layers. The reader knows precisely
what is constrained before any fix appears. He is visible in the flat, almost
blunt way he calls the API "too constrained" and moves on.

> "At the core, RNNs have a deceptively simple API: They accept an input vector x and give you an output vector y. However, crucially this output vector's contents are influenced not only by the input you just fed in, but also on the entire history of inputs you've fed in in the past."

He reduces the whole mechanism to what goes in and what comes out, then adds in
one sentence the single fact that makes it different: the output depends on every
past input, not just the current one. The word "crucially" marks for the reader
which part not to skip.

> "Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense. Sometimes the ratio of how simple your model is to the quality of the results you get out of it blows past your expectations, and this was one of those times."

He reports a result that impressed him and, in the same passage, names the
conditions that keep it honest: a small model, hyperparameters he chose more or
less at random, descriptions only on the edge of making sense. The caveats are
specific enough for a reader to check, so the enthusiasm does not inflate the
claim.

## Dan Luu, "Goodhearting IQ, cholesterol, and tail latency"

Source: https://danluu.com/percentile-latency/

> "Most real-world problems are big enough that you can't just head for the end goal, you have to break them down into smaller parts and set up intermediate goals. For that matter, most games are that way too. "Win" is too big a goal in chess, so you might have a subgoal like don't get forked."

He builds an abstract idea, that big goals get broken into smaller ones, from a
case the reader knows, a chess game where aiming straight at winning is too much
and a player sets smaller targets instead. The chess example carries the point,
so the general statement around it has something concrete under it. Luu is
visible in the plainness: he states the mechanism of subgoals without dressing
it up.

> "Initial results from Head Start were also promising; children in the program got a 10 point IQ boost. The next set of results was disappointing. By age 10, the difference in test scores and IQ between the trial and control groups wasn't statistically significant."

He reports the early result with its number, a 10 point IQ boost, and then
reports the later finding that erased it, that by age 10 the difference was not
statistically significant. Each sentence is a plain statement of what a study
found, and the order, promising result and then the larger follow-up, is the
point he is making.

> "If you specify goals in terms of 99%-ile, 99.9%-ile, and 99.99%-ile, you'll optimize your system to barely hit those goals. Those optimizations will often push other latencies around, resulting in a funny looking distribution that has kinks at those points, with latency that's often nearly as bad as possible everywhere else."

He shows what happens when a target is met exactly: the system hits the required
percentiles and gets worse everywhere else. The specifics, the named percentile
thresholds and the kinked distribution, keep this from being a general warning
about metrics and make it a description of one real failure.

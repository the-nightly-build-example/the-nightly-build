# Voice guide: the-evidence/latent-diffusion (01)

## How this piece should sound

This is a lesson that teaches a smart reader, new to diffusion image models, how
the Latent Diffusion paper made high-resolution image generation cheap by moving
the work into a compressed latent space. The register is the press's: plain
claims, concrete stakes, no hype. Write the way Tim Lee and Sean Trott write in
the piece below, where every abstract idea about how a model represents or
processes something is handed to the reader as a picture they already hold
before any dimension counts or equations arrive.

The hardest thing this lesson has to do is make compression and reconstruction
feel real without a diagram and without code. Tim Lee's Washington-DC-as-
coordinates passage shows one way that can go: a representation the reader cannot
picture (a point in a space of hundreds of dimensions) becomes obvious once it
sits on top of a coordinate system they already reason with. When the lesson
reaches the latent as a compressed stand-in for an image, a familiar intuition
about closeness or coordinates laid down first may carry more than the number of
dimensions does. Olah's conveyor-belt passage is the companion move for a
process rather than a representation: an internal step the reader cannot see, such
as information surviving a round trip through compression or an image emerging
over repeated denoising, can be given one plain physical image that needs no
figure beside it.

A multi-step mechanism is where these explanations usually come apart. Olah
keeps a single language-model example running through every gate of the LSTM
instead of starting fresh at each step, and the reader never loses the thread.
Where this lesson walks through the stages of the latent-diffusion pipeline, one
worked case carried the whole way may hold the explanation together better than
a new example per stage. Karpathy's "hello" passage shows the smallest version
of the same discipline: a training objective reduced to a four-letter vocabulary,
small enough to hold in the head, doing the work a diagram would otherwise do.
When an idea in this lesson can be shrunk to a case that small, the small case is
often enough.

The Evidence desk asks you to show the scale of a document honestly and to say
whether its findings still hold. Two passages below bear directly on that. Tim
Lee sets GPT-3's training corpus beside the number of words a child hears by age
ten; wherever this lesson reports a figure the reader cannot scale on their own,
a quantity they already hold placed next to it is what makes the figure mean
something. Karpathy, looking at a weak generated sample, says plainly that it is
not good and then says exactly what is nonetheless impressive about it. Where
this lesson weighs how latent diffusion's results hold up, or where a generated
image or a claim about the method does not survive scrutiny, that flat honesty
about what did and did not work is the desk's own standard on the page.

On register across all three writers: the claims are stated flat and the
sentences are mostly short. Karpathy opens on enthusiasm and Olah calls a result
beautiful, but in both cases the feeling arrives after a concrete example has
earned it, never as an adjective standing in for one. For a lesson bound to a
no-hype press, that is the usable lesson in their warmth. Note that all three
address the reader directly and write in the first person, which belongs to a
blog and not to this lesson's body; take the grounding move and leave the
address.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "This is useful for reasoning about spatial relationships. You can tell New York is close to Washington DC because 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is close to London. But Paris is far from Washington DC."

Lee is explaining why a model would store a word as a long list of numbers, and
before he says anything about high-dimensional space he puts four cities on a map
by their coordinates and lets the reader check the closeness themselves. The good
writing is that the reader does the reasoning, not the author: the numbers are
real latitudes and longitudes, so "close" is something you can verify by looking.
Lee is visible in the patience of it, spending a whole worked case on an analogy
before he spends a word on the actual idea.

> "Here's an analogy to illustrate how this works. Suppose you're going to take a shower, and you want the temperature to be just right: not too hot, and not too cold. You've never used this faucet before, so you point the knob to a random direction and feel the temperature of the water. If it's too hot, you turn it one way; if it's too cold, you turn it the other way. The closer you get to the right temperature, the smaller the adjustments you make."

This is how Lee explains training, a process with no everyday referent, by
finding an everyday feedback loop the reader has lived through. It works because
the shower really does have the structure he needs, random start, feel the
result, correct, smaller corrections near the target, so the analogy teaches
rather than decorates. His touch shows in how ordinary the chosen example is: a
faucet, not a thermostat or a control system.

> "One reason is scale. It's hard to overstate the sheer number of examples that a model like GPT-3 sees. GPT-3 was trained on a corpus of approximately 500 billion words. For comparison a typical human child encounters roughly 100 million words by age 10."

A number as large as 500 billion means nothing on its own, so Lee immediately
anchors it to a quantity the reader can feel, how much language a child takes in.
The good move is that the comparison is honest and load-bearing: the gap between
the two figures is the point he is making about scale. Lee is visible in the
restraint, one clean comparison rather than a pile of superlatives.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "As a working example, suppose we only had a vocabulary of four possible letters "helo", and wanted to train an RNN on the training sequence "hello". This training sequence is in fact a source of 4 separate training examples: 1. The probability of "e" should be likely given the context of "h", 2. "l" should be likely in the context of "he", 3. "l" should also be likely given the context of "hel", and finally 4. "o" should be likely given the context of "hell"."

Karpathy teaches what "predict the next character" means by shrinking the whole
problem to one four-letter word, small enough that the reader can count the
training examples by hand. The good writing is the sizing: the example is tiny on
purpose, so nothing is hidden and the reader can check every step. Karpathy is
visible in the confidence that a toy case carries the real idea, so he does not
apologize for its smallness or rush past it.

> "Okay, clearly the above is unfortunately not going to replace Paul Graham anytime soon, but remember that the RNN had to learn English completely from scratch and with a small dataset (including where you put commas, apostrophes and spaces)."

Having shown a generated passage that is plainly not good, Karpathy says so flatly
and then says exactly what is still impressive, that the model started from
nothing and had to learn even where spaces and apostrophes go. The good writing is
the honesty: he does not oversell a mediocre result, and the specific things he
lists are checkable in the sample above it. His voice shows in the plain "clearly
the above is unfortunately not going to replace Paul Graham," a judgment stated
without hedging.

> "Again, what is beautiful about this is that we didn't have to hardcode at any point that if you're trying to predict the next character it might, for example, be useful to keep track of whether or not you are currently inside or outside of quote. ... In other words one of its cells gradually tuned itself during training to become a quote detection cell, since this helps it better perform the final task."

Karpathy lands the piece's central surprise, that the network decided on its own
to track something useful, in concrete terms: one specific cell, one specific job,
watching whether the text is inside a quotation. The good writing is that the
"beautiful" is earned by the example that precedes it rather than asserted, and
the claim stays tied to a thing the reader has just been shown. He is visible in
naming the exact behavior, a quote detection cell, instead of reaching for a grand
word about emergence.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Sometimes, we only need to look at recent information to perform the present task. For example, consider a language model trying to predict the next word based on the previous ones. If we are trying to predict the last word in "the clouds are in the sky," we don't need any further context – it's pretty obvious the next word is going to be sky. In such cases, where the gap between the relevant information and the place that it's needed is small, RNNs can learn to use the past information."

Olah introduces an abstract difficulty, long-range dependency, by first showing
the easy case in a sentence the reader completes instantly. The good writing is
the ordering: he establishes what is simple before he complicates it, so the hard
case later has something to contrast against. Olah is visible in the care of the
example, a sentence so plain that the reader feels the point before he states it.

> "The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It's very easy for information to just flow along it unchanged."

Here Olah gives an invisible internal mechanism a single physical image, a
conveyor belt, and then says precisely what the image is meant to capture: that
information can travel a long way without being disturbed. The good writing is
that the metaphor is immediately cashed out in literal terms, so it explains
rather than just sounds good. His touch is the restraint of one image held to one
job, not extended until it breaks.

> "Let's go back to our example of a language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject."

Olah keeps the same language-model example running as he walks through each part
of the mechanism, so the reader tracks one concrete story across a multi-step
process. The good writing is the continuity: "let's go back to our example"
spends something already built rather than introducing a new case the reader must
learn. Olah is visible in the teacherly discipline of reusing one example until it
has done all its work.

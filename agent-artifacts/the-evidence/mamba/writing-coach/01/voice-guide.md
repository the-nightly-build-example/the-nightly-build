# Voice guide: the-evidence/mamba

## How this piece should sound

This lesson explains a state-space sequence model to a reader who already
understands attention and has never met this way of modelling a sequence. The
register is plain and confident: the register of someone who understands the
paper well enough to say what it does in ordinary words. When a sentence could
either sound good or be understood, it should be understood.

The reader already knows what attention costs, so the lesson's core is a
contrast between a model that carries a compressed state forward and attention
re-reading every earlier token. Olah sets two methods side by side in two
sentences of the same shape, changing only the words that carry the difference.
Where this lesson puts the selective state-space update next to attention, that
plain parallel construction may do more than a diagram would.

The paper reports throughput and perplexity numbers at particular model sizes. A
figure the reader cannot size on their own may want a comparison they already
hold, the way Olah turns "ten million times faster" into a week of training set
against 200,000 years. The reader's existing sense of what attention costs on a
long sequence is one such anchor. Which comparison to reach for is the writer's
to build from the research, not to borrow from here.

Be honest about scale in the same plain voice the results are stated in. The
commission asks the lesson to show which model sizes were trained, which
benchmarks were never run, and where the equal-parameter comparisons are strong
or thin. Willison states where a tool works and where it returns convincing but
wrong answers in one register, without making the limit sound smaller than the
strength; Dieleman, in the middle of an explanation, simply says which part he
understands least well. When the limit sits in the same passage as the mechanism
it qualifies, in the same plain words, the reader takes it as part of the
explanation rather than as a retreat from it.

The lesson has to stay skeptical about the reading that Mamba proves the
transformer is finished. Dieleman shows one way to handle a label that outran
its meaning: he traces where the word "diffusion" stretched to cover too much,
then says plainly that the term had become useless, and the verdict is earned
because the overreach is shown first. Where this piece reaches how "transformers
are over" gets used in argument today, it may need to mark the exact point where
the usage outruns what the paper showed, aimed at the specific claim and not at
the mood around it.

The three exemplars are blog posts with an "I" and a reader addressed directly.
This lesson's body speaks to no one, and only its two bookend cards address the
reader. What carries over from the exemplars is the plainness and the
willingness to name a limit out loud, not the first person, and not the
exclamation marks, dashes, and conversational asides that belong to their looser
format. The honesty and the concrete anchors are what this lesson takes from
them.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models
> computationally tractable. For modern neural networks, it can make training
> with gradient descent as much as ten million times faster, relative to a naive
> implementation. That’s the difference between a model taking a week to train
> and taking 200,000 years."

Olah says what backpropagation is in one clause, gives a number, and then turns
that number into something the reader can picture: a week set against 200,000
years. The claim and the size of it arrive together, and the comparison does the
work a bare multiplier could not. He does not tell the reader the result is
impressive; the plainness is where the confidence shows.

> "Forward-mode differentiation tracks how one input affects every node.
> Reverse-mode differentiation tracks how every node affects one output."

Two sentences of the same shape, with only the words that carry the difference
changed: "one input affects every node" against "every node affects one output."
The parallel construction makes the contrast between the two methods the only
thing that moves, so the reader sees it without a diagram. Olah trusts the
sentence structure to hold the distinction.

> "When I first understood what backpropagation was, my reaction was: “Oh,
> that’s just the chain rule! How did it take us so long to figure out?” I’m not
> the only one who’s had that reaction."

Olah reports his own first reaction in ordinary words and lets it sound briefly
unimpressed with a famous algorithm. Later in the same passage he explains why
the idea was harder to reach than hindsight suggests, so the plain reaction is
not the whole verdict. The person is visible in the willingness to say what he
actually thought.

## Simon Willison, "Catching up on the weird world of LLMs"

Source: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/

> "How do they do all this? It really is as simple as guessing the next word in
> a sentence. If you’ve used an iPhone keyboard and type “I enjoy eating” it
> suggests words like “breakfast.” That’s what a language model is doing."

Willison answers his own question with the plainest form of the mechanism and
then ties it to something the reader has already done: the phone keyboard
guessing the next word. The everyday example carries the explanation, so no
jargon is needed for the point to land. He is confident enough to say the
mechanism really is that simple.

> "A great rule of thumb I use is this: Could my friend who just read the
> Wikipedia article answer this question? If yes, then a LLM is much more likely
> to be able to answer it. The more expert and obscure the question the more
> likely you are to run into convincing but blatantly wrong answers."

Willison hands the reader a concrete test for when to trust the tool, phrased as
a question anyone can apply to their own case. He states the failure the same
way he states the success, and names it exactly: convincing but wrong answers on
expert questions. The calibration is specific rather than a general warning to
be careful.

> "The thing language models are best at is producing incredibly convincing
> text, whether or not it’s actually true."

One plain sentence puts the model's real strength and its real limit next to each
other and softens neither. Willison does not exaggerate the ability or shrink the
caveat; he lets "whether or not it’s actually true" sit at the end and carry its
full weight. The honesty is in refusing to make the limitation sound smaller than
it is.

## Sander Dieleman, "Perspectives on diffusion"

Source: https://sander.ai/2023/07/20/perspectives.html

> "Another important difference is that denoising autoencoders are usually
> trained to deal only with noise of a particular strength. In a diffusion
> model, we have to be able to make predictions for inputs with a lot of noise,
> or with very little noise. The noise level is provided to the neural network
> as an extra input."

Dieleman marks the difference between two models in concrete operational terms:
one handles noise of a single strength, the other has to handle any amount, and
the noise level is passed in as an input. Nothing is stated abstractly; each
sentence is a fact about what the network is given and what it is asked to do. He
builds the distinction one plain clause at a time.

> "Full disclosure: out of all the different perspectives on diffusion in this
> blog post, this is probably the one I understand least well. Sort of ironic,
> given how popular it is, but variational inference has always been a little bit
> mysterious to me."

In the middle of an explanatory piece, Dieleman says plainly that this is the
part he understands least well and that the topic has always been somewhat
unclear to him. Marking the limit of his own grasp tells the reader which
stretches are solid and which are not. The person is visible in the refusal to
sound more certain than he is.

> "Finally, it’s worth noting that the definition of “diffusion” in the context
> of generative modelling has grown to be quite broad, and is now almost
> equivalent to “iterative refinement”. … It’s not clear where to draw the line
> … To me, that seems confusing enough so as to render the term useless."

Dieleman traces how a word stretched to cover so much that it stopped
distinguishing anything, then states the judgment flatly: the term had become
useless. He earns it by showing the specific overreach before naming it, so the
skepticism is aimed at a particular word rather than at a mood. The verdict
arrives only after the evidence for it.

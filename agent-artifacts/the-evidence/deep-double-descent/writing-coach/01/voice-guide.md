# Voice guide: the-evidence/deep-double-descent

## How this piece should sound

This is a lesson for a reader who is smart and widely read but new to double
descent. They know the word "overfitting" the way most educated people do, as a
vague warning, and they have absorbed the slogan that bigger models are better.
The lesson teaches one quantitative result: test error against model size. Write
it in the house's plain register, the way Nielsen and Tim Lee write, with short
declarative sentences and flat claims, and without talking down. Every term of
art the reader does not already hold gets defined in plain words the moment it is
used: overfitting, test error, the interpolation threshold, label noise.

The result contradicts an expectation the reader arrives with. Nielsen's opening
on digit recognition shows one way to set up an expectation before unsettling it:
he states the familiar view flatly and backs the turn with a concrete count
rather than an adjective. Tim Lee's opening does a related thing, naming what the
reader has already heard and marking exactly where the usual explanation stops.
If this lesson opens on the classical bias-variance expectation, it can be stated
as plainly as the reader already half-believes it, so what follows has something
to work against.

The lesson teaches a curve, and curves are made of numbers. Nielsen assigns real
weights and a threshold to his cheese-festival perceptron, and Tim Lee gives
Washington DC its actual coordinates so the reader can check that New York is
close and Paris is far. Where this lesson reports a setup or a figure, the model,
the dataset, the size of a peak, the number can carry the scale the way those
examples do, in place of a word like "large". The Evidence desk asks for honest
scale, and a specific figure is how the reader sees the size of the foundation
under a claim.

When an analogy is the clearest way in, Nielsen and Tim Lee both reach for a
homely one and then say where it stops: Nielsen tells the reader he will not take
the rolling ball "quite that seriously," and Tim Lee flags that his shower-faucet
picture "quickly gets silly if you take it too literally." If this lesson uses an
image to explain what happens around the interpolation threshold, naming the
edge of the image keeps the reader from mistaking the picture for the mechanism.

Teach one piece of the machinery at a time. Olah takes a single component, gives
it one plain physical image, and pins it to a specific case he can carry forward,
tracking a subject's gender so the pronouns come out right. This lesson can do the
same with each idea it teaches: a plain statement, one worked case with real
values, finished before the next idea begins. Where the lesson does speak to the
reader, Olah's opening shows the move that suits "Why this matters," starting
from something the reader is already doing or already believes.

## Michael Nielsen, "Using neural networks to recognize handwritten digits"

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "Most people effortlessly recognize those digits as 504192. That ease is
> deceptive. In each hemisphere of our brain, humans have a primary visual
> cortex, also known as V1, containing 140 million neurons, with tens of billions
> of connections between them."

Nielsen takes something the reader does without thinking and shows that it is
hard, and he does it with a count, not with an adjective. The three-word sentence
"That ease is deceptive" carries the whole turn, and the figures that follow back
it up. He is visible in the flat confidence of the reporting: no hedging, no
build-up.

> "A way you can think about the perceptron is that it's a device that makes
> decisions by weighing up evidence. Let me give an example. It's not a very
> realistic example, but it's easy to understand, and we'll soon get to more
> realistic examples. Suppose the weekend is coming up, and you've heard that
> there's going to be a cheese festival in your city. You like cheese, and are
> trying to decide whether or not to go to the festival."

An abstract object gets explained through a small everyday decision, and Nielsen
warns up front that the example is not realistic instead of dressing it up. The
example is homely and a little silly on purpose, and saying so is part of how he
keeps the reader's trust. Later he attaches real weights and a threshold to the
same case, so the abstraction ends up carried by numbers a reader can follow.

> "Fortunately, there is a beautiful analogy which suggests an algorithm which
> works pretty well. We start by thinking of our function as a kind of a valley.
> If you squint just a little at the plot above, that shouldn't be too hard. And
> we imagine a ball rolling down the slope of the valley. Our everyday experience
> tells us that the ball will eventually roll to the bottom of the valley."

Nielsen introduces an unfamiliar procedure through a picture the reader already
owns, and invites the reader in with "If you squint." The words are ordinary and
the image is one the reader has seen with their own eyes. Later in the passage he
says plainly that he will not take the analogy too seriously, which marks it as a
device rather than the real thing.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this
> essay, you understand each word based on your understanding of previous words.
> You don't throw everything away and start thinking from scratch again. Your
> thoughts have persistence."

Olah grounds an abstract capacity in what the reader is doing at that very moment,
before he has introduced any machinery at all. The sentences are short and each
one adds a single step, and the repetition of "from scratch" fixes the point.
Only after the reader feels the idea in themselves does the technical word for it
arrive.

> "The cell state is kind of like a conveyor belt. It runs straight down the
> entire chain, with only some minor linear interactions. It's very easy for
> information to just flow along it unchanged."

One part of the mechanism gets one concrete physical image, and the image is kept
plain. The verbs are ordinary, runs and flow along, and the sentence claims only
what the picture supports. Olah is visible in how little he asks the image to do:
it explains one thing and stops.

> "Let's go back to our example of a language model trying to predict the next
> word based on all the previous ones. In such a problem, the cell state might
> include the gender of the present subject, so that the correct pronouns can be
> used. When we see a new subject, we want to forget the gender of the old
> subject."

An abstract operation, deciding what to discard, is pinned to a case a reader can
follow, keeping track of who the sentence is about so the pronouns come out right.
Olah reuses this same example across the walkthrough, so it accumulates meaning
instead of being spent once. The concreteness is what makes the mechanism
legible.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "If you know anything about this subject, you've probably heard that LLMs are
> trained to "predict the next word," and that they require huge amounts of text
> to do this. But that tends to be where the explanation stops. The details of
> how they predict the next word is often treated as a deep mystery."

Lee names what the reader has already heard and then marks the exact point where
the reader's understanding runs out, which gives the piece a reason to exist that
the reader can feel. Nothing here is hyped and nothing is hedged. The register is
plain and direct, and it treats the reader as capable but not yet informed.

> "Why use such a baroque notation? Here's an analogy. Washington DC is located at
> 38.9 degrees North and 77 degrees West. ... This is useful for reasoning about
> spatial relationships. You can tell New York is close to Washington DC because
> 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is close
> to London. But Paris is far from Washington DC."

Lee makes an abstract representation concrete by giving real coordinates the
reader can check for themselves, and the checking is the point: the reader does
the small arithmetic and the idea lands. He asks the reader's own question back to
them first ("Why use such a baroque notation?") and then answers it plainly.

> "Here's an analogy to illustrate how this works. Suppose you're going to take a
> shower, and you want the temperature to be just right: not too hot, and not too
> cold. You've never used this faucet before, so you point the knob to a random
> direction and feel the temperature of the water. If it's too hot, you turn it
> one way; if it's too cold, you turn it the other way. The closer you get to the
> right temperature, the smaller the adjustments you make."

A process the reader has never thought about is explained through one they do
every day, built step by step in plain sentences. Later in the piece Lee says the
analogy "quickly gets silly if you take it too literally," so the reader knows
where the picture ends. The person is visible in the ease of the writing and in
his willingness to spend a full paragraph on a familiar scene before returning to
the machinery.

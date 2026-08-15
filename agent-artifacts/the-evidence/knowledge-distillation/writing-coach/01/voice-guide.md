# Voice guide: the-evidence/knowledge-distillation

## How this piece should sound

This is a lesson on knowledge distillation for a reader who is quick and widely
read but has never trained a model and has no time in a codebase. Hold the
register Michael Nielsen holds when he introduces the perceptron: plain claims
in short declarative sentences, with the everyday word preferred over the
technical one wherever the technical one is not doing real work. The terms this
lesson cannot avoid, among them softmax, temperature, the teacher and student
models, and a classifier's full probability output, each earn a plain definition
at the sentence where they first appear, the way Olah names "sigmoid layer" and
then immediately says what its zero and its one mean. Keep the practitioner's
exact word once you have defined it, and do not talk down while defining it.

Distillation is the kind of idea that gets clearer the moment it is worked
through a concrete case with real numbers. Olah's France sentence and Nielsen's
cheese festival show how far one small, fully worked example can carry, and both
let the reader take the reasoning a step at a time instead of stating the result
first; where this lesson reaches for such an example, the reader can be trusted
to finish the inference. Nielsen also prices an example before he spends it
("not a very realistic example, but it's easy to understand"), which is worth
having on hand wherever a small demonstration might be mistaken for the paper's
full experiment.

This desk sets a document against the way people invoke it now, and the reader
arrives already having met the word "distillation" in loose use. Lee and Trott's
opening shows one way to begin from the reader's existing impression of a term
before laying out the precise account. Their coordinate analogy anchors an
unfamiliar quantity to one the reader already holds; the scale in this paper can
be anchored the same way, and where the paper reports a figure, the lesson can
give that figure rather than a size word.

What the reader should be able to do at the end is restate the distillation
method in their own words. That rewards Nielsen's patience more than a memorable
phrase does. Aim the writing at a reader who will reconstruct the idea
afterward, and let the worked explanation be what carries it.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this
> essay, you understand each word based on your understanding of previous words.
> You don't throw everything away and start thinking from scratch again. Your
> thoughts have persistence."

The paragraph opens on something the reader is doing right now, before any
machinery is named, and each sentence is short and does one job. Olah is present
in the plain second person and in the four-word closing sentence that states the
point without dressing it up.

> "But there are also cases where we need more context. Consider trying to
> predict the last word in the text "I grew up in France… I speak fluent
> French." Recent information suggests that the next word is probably the name of
> a language, but if we want to narrow down which language, we need the context
> of France, from further back."

Olah makes an abstract point about long-range context concrete with one sentence
the reader can finish in their own head. He shows the inference in order, the
kind of word first and then which one, so the reader arrives at the conclusion
rather than being handed it.

> "Gates are a way to optionally let information through. They are composed out
> of a sigmoid neural net layer and a pointwise multiplication operation. The
> sigmoid layer outputs numbers between zero and one, describing how much of each
> component should be let through. A value of zero means "let nothing through,"
> while a value of one means "let everything through!""

A term of art is defined in its first sentence, the mechanism follows, and then
the two extreme values are spelled out in ordinary English. Olah keeps the
practitioner's exact vocabulary, sigmoid layer and pointwise multiplication, and
still lands the meaning through the plain zero-and-one gloss.

## Michael Nielsen, "Using neural nets to recognize handwritten digits" (Neural Networks and Deep Learning, Chapter 1)

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "We carry in our heads a supercomputer, tuned by evolution over hundreds of
> millions of years, and superbly adapted to understand the visual world.
> Recognizing handwritten digits isn't easy. Rather, we humans are stupendously,
> astoundingly good at making sense of what our eyes show us. But nearly all that
> work is done unconsciously. And so we don't usually appreciate how tough a
> problem our visual systems solve."

Nielsen shows why a task is hard by first crediting how well people already do
it, and he reaches for a concrete scale, hundreds of millions of years, in place
of an adjective. He allows himself two adverbs, "stupendously, astoundingly,"
and keeps the rest of the diction flat; his verdict that the task "isn't easy"
sits in a three-word sentence.

> "A way you can think about the perceptron is that it's a device that makes
> decisions by weighing up evidence. Let me give an example. It's not a very
> realistic example, but it's easy to understand, and we'll soon get to more
> realistic examples. Suppose the weekend is coming up, and you've heard that
> there's going to be a cheese festival in your city."

Before the example arrives, Nielsen tells the reader exactly what it is worth
and what it is not, which lets the reader lean on a toy case without mistaking
it for the real thing. The teacher is visible in "Let me give an example" and in
the everyday scene he picks to carry an abstract definition.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "If you know anything about this subject, you've probably heard that LLMs are
> trained to "predict the next word," and that they require huge amounts of text
> to do this. But that tends to be where the explanation stops. The details of
> how they predict the next word is often treated as a deep mystery."

Lee and Trott start from the phrase the reader has already heard, then say
exactly where the usual account gives out, which tells the reader what this piece
is going to add. The sentences are short and the diction is ordinary, and the
only words in quotation marks are the received phrase they are about to open up.

> "You can tell New York is close to Washington DC because 38.9 is close to 40.7
> and 77 is close to 74. By the same token, Paris is close to London. But Paris
> is far from Washington DC."

They explain an unfamiliar way of representing things through coordinates the
reader already trusts, and they test the comparison against a case the reader can
check, Paris being far from Washington DC. The prose stays in flat declaratives,
and the specific numbers, not an adjective, do the work of the comparison.

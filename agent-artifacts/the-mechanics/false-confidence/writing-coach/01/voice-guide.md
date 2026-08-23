# Voice guide: the-mechanics/false-confidence

## How this piece should sound

This lesson starts from one thing the reader has run into and works back to what
produces it: a model that states a wrong answer in the same assured tone it uses
for a right one, and that will print a number ("I'm 95% sure") when asked how
confident it is. The register is plain and exact. The reader is smart and reads
widely but is new to this subject and has no time in a codebase, so the piece
can lean on probability, which they hold, and take nothing about softmax,
logits, calibration, or reinforcement learning from human feedback as already
known.

Nielsen opens from something the reader does without effort, reading the digits
504192, and puts the machinery under it with real figures. The same opening is
available here: begin from the assured tone the reader has already heard, then
go under it to the probability distribution over next tokens. Where the piece names a part,
Olah's clouds-in-the-sky sentence and his gender-of-the-subject example show one
concrete case carried through a step instead of the idea restated in the
abstract. The gap this lesson turns on, between the token probability the model
computes and the confidence it prints in words, is the kind of distinction a
single worked case can make legible; Karpathy naming a cell by exactly what it
does, and what nothing told it to do, is the same move on an internal part.

The chain has several steps, and Karpathy's account of what a training model
learns first, then next, then later, names a sequence in order and in concrete
terms that a reader can repeat back. When this lesson moves from the softmax, to
what calibration means, to the post-training step, to the verbal confidence that
is itself generated text, each step can be named in its own terms in the order
the reader needs it, so someone could retrace the path and see where another
person's explanation skipped a rung.

The commission asks for settled engineering and open questions to be kept apart,
and Nielsen shows the plain version of that: he states that a network performs
well and that he cannot fully explain why, and holds those as two separate
facts. Where this lesson reaches a settled part, that the softmax is a
probability about the next token, that the confidence stated in words is itself
generated text, it can say so flatly. Where it reaches an open one, such as how
far a model's internal state registers that its own answer is wrong, it can say
that plainly too, and a reader should be able to tell which kind of claim they
are reading.

An analogy can carry a step when the piece cashes it out into the mechanism
right away, the way Olah gives the cell state a conveyor belt and then says what
the picture buys, and Nielsen sets a ball rolling in a valley before any
equation. Each picture is small and is held to the one thing it explains. No
grand word needs to go in front of the calibration result; where the evidence is
strong the piece can let the figures carry it and stay plain, the way Nielsen
gives the neuron count instead of calling the feat impressive.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There’s something magical about Recurrent Neural Networks (RNNs). I still remember when I trained my first recurrent network for Image Captioning. Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense."

He opens from his own surprise at a result and gives the specific detail that
makes it real: a few dozen minutes, arbitrarily-chosen hyperparameters,
descriptions on the edge of making sense. Karpathy is visible as a practitioner
reporting what actually happened at his desk rather than setting up a topic.

> "The picture that emerges is that the model first discovers the general word-space structure and then rapidly starts to learn the words; First starting with the short words and then eventually the longer ones. Topics and themes that span multiple words (and in general longer-term dependencies) start to emerge only much later."

He narrates a process in the order it happened, naming each stage concretely:
word spacing first, then short words, then long words, then themes across words.
The account reads as something he watched in the samples, and he reports the
sequence he saw rather than a theory of what should happen.

> "Again, what is beautiful about this is that we didn’t have to hardcode at any point that if you’re trying to predict the next character it might, for example, be useful to keep track of whether or not you are currently inside or outside of quote. We just trained the LSTM on raw data and it decided that this is a useful quantitity to keep track of. In other words one of its cells gradually tuned itself during training to become a quote detection cell, since this helps it better perform the final task."

He explains an internal part by saying exactly what it does, that one cell tracks
whether the text is inside a quote, and that nobody wrote a rule for it. The
judgment that this is beautiful is Karpathy's own and he attaches it to the
specific observation, not to the subject in general.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Sometimes, we only need to look at recent information to perform the present task. For example, consider a language model trying to predict the next word based on the previous ones. If we are trying to predict the last word in “the clouds are in the sky,” we don’t need any further context – it’s pretty obvious the next word is going to be sky. In such cases, where the gap between the relevant information and the place that it’s needed is small, RNNs can learn to use the past information."

He makes an abstract point, how much earlier context a prediction needs, concrete
with a sentence the reader finishes on their own. Olah takes the easiest case
first and says the answer is obvious, which is a way of trusting the reader to
keep up.

> "The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It’s very easy for information to just flow along it unchanged."

He gives an internal component one plain physical picture and then immediately
says what the picture is for: information can travel along it unchanged. Olah
keeps the image small and spends it right away on the mechanism, so the analogy
does work instead of decoration.

> "Let’s go back to our example of a language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject."

He runs a single concrete example, tracking a subject's gender to get the
pronouns right, through the successive steps of the mechanism. Olah returns to
the same case at each step, so the reader can watch what each part does to it
rather than meet a new illustration every paragraph.

## Michael Nielsen, "Using neural nets to recognize handwritten digits" (Neural Networks and Deep Learning, Chapter 1)

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "Most people effortlessly recognize those digits as 504192. That ease is deceptive. In each hemisphere of our brain, humans have a primary visual cortex, also known as V1, containing 140 million neurons, with tens of billions of connections between them."

He takes a thing the reader just did without effort, reading a short string of
digits, and puts the machinery under it with real figures. Nielsen is patient and
exact here, giving the neuron count rather than calling the feat impressive.

> "We start by thinking of our function as a kind of a valley. If you squint just a little at the plot above, that shouldn't be too hard. And we imagine a ball rolling down the slope of the valley. Our everyday experience tells us that the ball will eventually roll to the bottom of the valley."

He grounds a piece of calculus in an everyday physical intuition before writing
any equation, and invites the reader to picture it with him. Nielsen builds the
analogy in small plain steps and stays inside the reader's own experience of how
a ball behaves.

> "While our neural network gives impressive performance, that performance is somewhat mysterious. The weights and biases in the network were discovered automatically. And that means we don’t immediately have an explanation of how the network does what it does."

He states plainly that the network works well and that he cannot fully explain
why, and keeps those as two separate facts. Nielsen does not smooth over the gap;
he names it and lets it become the next question, which is how honest hedging
reads when it is not defensive.

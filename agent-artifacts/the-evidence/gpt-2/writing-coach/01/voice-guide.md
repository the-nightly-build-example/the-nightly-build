# Voice guide: the-evidence/gpt-2 (01)

## How this piece should sound

This lesson reads one 2019 paper for a reader who has met it only as a story,
"too dangerous to release," and has never seen what it measured. The register is
plain, load-bearing explanation: the writing carries the paper's actual content
and the public account of it, and asks the reader to follow along. Michael
Nielsen's chapter is the closest model for that register.
When he sets up a hard problem he tries the obvious approach and lets the reader
watch it fail, the loop-and-stroke rule for a 9 collapsing into a morass of
exceptions. The difficulty gets felt instead of announced. Where this lesson
explains what zero-shot evaluation or a web-scraped corpus actually is, that
patience is available: work the real case before naming it.

The reader is smart and widely read and holds none of this subject. Nielsen
writes for that reader, explaining why things are done the way they are and
grounding an idea in a worked case, the cheese-festival perceptron, while being
candid about the case itself: not realistic, but easy to understand, with better
ones coming. When a simplified example stands in for the paper's real setup, that
candor about what the example is worth is what keeps the reader's trust.

The paper's fame and its measured result pull apart, and the honesty in
Karpathy's post is the model for holding both without tipping into hype or into
dismissal. He grades an output plainly, it will not replace Paul Graham, while
giving the fair yardstick in the same breath, that the model learned English
from scratch on a small dataset. When he states an impressive-sounding fact he
tells the reader not to over-read it, and retracts the flourish outright. Where
this lesson reports what the benchmark numbers were, or what the staged-release
documents claimed and what the six-month follow-up found, the same evenness is
available: state the result and its scale, and let the distance between the
measured capability and the "dangerous" framing show without the writing
underlining it.

Olah's essay is the model for making a mechanism legible. He names the mystery a
reader brings and then dissolves it into a plain picture, recurrent networks as
copies of one network passing a message along, and his analogies are chosen to
match the mechanism rather than to decorate it: the cell state as a conveyor
belt, because a value really does run straight along the chain. Where this lesson
explains how the model was built and how it was tested, an analogy earns its
place when it tracks what the paper actually did, and not otherwise.

Keep the diction plain throughout, in the register Olah, Karpathy, and Nielsen
share: short, concrete sentences, the domain's own words used exactly and without
inline-code decoration, and no grand word arriving before the argument that earns
it. What the numbers and the release record add up to is the writer's to reach.
The writing's task is to make the measured paper and the famous story both plain
enough that a reader can read them side by side.

## Michael Nielsen, "Neural Networks and Deep Learning" (Chapter 1: Using neural nets to recognize handwritten digits)

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "Simple intuitions about how we recognize shapes - "a 9 has a loop at the top, and a vertical stroke in the bottom right" - turn out to be not so simple to express algorithmically. When you try to make such rules precise, you quickly get lost in a morass of exceptions and caveats and special cases. It seems hopeless."

Nielsen makes a problem's difficulty concrete by trying the obvious approach and
watching it come apart: the loop-and-stroke rule for a 9 dissolves into
exceptions and special cases. He states the verdict flatly, "It seems hopeless,"
and the plainness is what makes it land. The reader feels the difficulty instead
of being told the problem is hard.

> "A way you can think about the perceptron is that it's a device that makes decisions by weighing up evidence. Let me give an example. It's not a very realistic example, but it's easy to understand, and we'll soon get to more realistic examples."

Before the example arrives, Nielsen tells the reader exactly what it is worth:
not realistic, but easy to understand, with better ones on the way. That candor
about a teaching device is where the person is visible, and it buys trust for the
simplified case that follows.

> "The computational universality of perceptrons is simultaneously reassuring and disappointing. It's reassuring because it tells us that networks of perceptrons can be as powerful as any other computing device. But it's also disappointing, because it makes it seem as though perceptrons are merely a new type of NAND gate. That's hardly big news!"

Nielsen gives the reader the honest map of a result, reassuring for one plain
reason and disappointing for another, and names both. "That's hardly big news!"
is his own dry judgment, and it works because the two reasons under it are stated
and a reader can check them.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There's something magical about Recurrent Neural Networks (RNNs). I still remember when I trained my first recurrent network for Image Captioning. Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense."

Karpathy reports his own experience in concrete detail, a few dozen minutes,
arbitrary hyperparameters, descriptions on the edge of making sense, so the
wonder is earned by the specifics rather than asserted. The first-person memory
is where he is visible: he tells you it surprised him and shows the exact thing
that did.

> "In fact, it is known that RNNs are Turing-Complete in the sense that they can to simulate arbitrary programs (with proper weights). But similar to universal approximation theorems for neural nets you shouldn't read too much into this. In fact, forget I said anything."

He states an impressive-sounding fact and then tells the reader not to over-read
it, closing by retracting the flourish outright. The honesty is the move: he
refuses to let a big-sounding claim stand unqualified, and the retraction is
plainly his own voice. (The wording "they can to simulate" is the source's own.)

> "Okay, clearly the above is unfortunately not going to replace Paul Graham anytime soon, but remember that the RNN had to learn English completely from scratch and with a small dataset (including where you put commas, apostrophes and spaces). I also like that it learns to support its own arguments (e.g. [2], above)."

Karpathy grades the output plainly, it will not replace Paul Graham, and in the
same sentence gives the fair yardstick: the model learned English from scratch on
a small dataset. He neither inflates the result nor waves it off, and his own
taste shows in noticing the small thing that worked.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "These loops make recurrent neural networks seem kind of mysterious. However, if you think a bit more, it turns out that they aren't all that different than a normal neural network. A recurrent neural network can be thought of as multiple copies of the same network, each passing a message to a successor."

Olah names the feeling a reader brings, that the thing looks mysterious, and then
takes it apart over the next two sentences into a plain picture. The writing is
patient, and the person shows in his willingness to grant that something seems
mysterious before demonstrating that it is not.

> "The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It's very easy for information to just flow along it unchanged."

The analogy does real work: "conveyor belt" is chosen because the mechanism
actually runs a value straight along a chain with only small changes, so the
picture matches the machine rather than dressing it up. The diction stays plain,
"kind of like," "just flow along it," and the confidence comes from
understanding.

> "The sigmoid layer outputs numbers between zero and one, describing how much of each component should be let through. A value of zero means "let nothing through," while a value of one means "let everything through!""

Olah explains a mechanism by saying exactly what the numbers mean and then voices
the two extremes in the machine's own terms, "let nothing through," "let
everything through." There is no hedging and no flourish, and the small choice to
state the endpoints plainly is where his hand shows.

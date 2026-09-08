# Voice guide: attribute binding lesson (The Mechanics)

## How this piece should sound

This lesson takes a behavior the reader has seen with their own eyes, a prompt
that asks for one object in a certain color or a certain place and an image that
puts the color or the position on the wrong object, and works back to what inside
a text-to-image system produces it. The register is a patient daily course for a
smart reader who has never seen a line of the code. Keep it plain and concrete,
and never breezy. Stephen Wolfram's opening sentence about ChatGPT shows the move
to start with: state what the system is doing at its simplest, in one sentence
the reader can hold, before any part is opened up. There is room to say the base
thing plainly first.

Build the explanation the way Chris Olah builds his, one link of the causal chain
at a time, and hold to the distinction he names between what causes a behavior and
what only travels alongside it. The piece can work backward from the
wrong-colored object to the part of the system responsible, each step naming a
real part and what it does before the next step depends on it. Where a first,
simple account of why the color lands wrong would be too tidy, the Olah passage
that revises a first guess and then checks it against real cases shows that an
explanation can be corrected in front of the reader rather than delivered whole.
If the honest first reading of a step turns out to be too narrow, the lesson can
show it being widened.

Introduce each part of the system the way Jay Alammar does, from the outside in.
His single-black-box opening starts at the behavior the reader already meets, an
input going in and an output coming back, and only then names the components
inside. A term of art can enter at the step that needs it and be defined in the
same breath, the way his piece brings in a word he says he had to learn himself.
That candor is available here too. The writer can be a plain guide who stays level
with the reader, without the jokes at the reader's expense or the enthusiasm that
a personal blog can afford and this course cannot.

A short concrete case can carry a step where an abstract statement would slide
past. Wolfram's cannon ball is the pattern: a single specific prompt, with two
objects and their attributes, followed through each step, can do more than a
general description of how the system handles attributes. Where it helps, one case
can run the length of the explanation.

The series asks each lesson to reach ground, a step below which nothing would
change the answer, and to mark which steps are settled engineering and which are
still open even to the people who build these systems. Wolfram's plain admission
that a step is not yet understood, and Olah's sentence that labels the understood
part and the unknown part together, both show how to mark that line without
hedging the whole piece. Where the answer to why a step behaves as it does is that
nobody yet knows, the lesson can say so and say which step. The reader should
finish able to say why the color lands on the wrong object, not only that it does,
and able to notice when someone else's account skips a step.

## Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?"

Source: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/

> "The first thing to explain is that what ChatGPT is always fundamentally trying to do is to produce a “reasonable continuation” of whatever text it’s got so far, where by “reasonable” we mean “what one might expect someone to write after seeing what people have written on billions of webpages, etc.”"

He states the whole mechanism in one plain sentence before any detail arrives:
the system produces a reasonable continuation of the text so far. The meaning of
"reasonable" is folded into the same sentence, so the reader is never asked to
hold an undefined term. Wolfram is visible in the refusal to make the base idea
sound complicated.

> "One might think it should be the “highest-ranked” word (i.e. the one to which the highest “probability” was assigned). But this is where a bit of voodoo begins to creep in. Because for some reason—that maybe one day we’ll have a scientific-style understanding of—if we always pick the highest-ranked word, we’ll typically get a very “flat” essay, that never seems to “show any creativity” (and even sometimes repeats word for word). But if sometimes (at random) we pick lower-ranked words, we get a “more interesting” essay."

He names the point where settled engineering stops and guesswork begins, and says
so in plain words, then marks the open question with the answer he cannot give,
"for some reason—that maybe one day we'll have a scientific-style understanding
of". The candor is specific. He tells you which step is not understood instead of
smoothing over it.

> "Say you want to know (as Galileo did back in the late 1500s) how long it’s going to take a cannon ball dropped from each floor of the Tower of Pisa to hit the ground. Well, you could just measure it in each case and make a table of the results. Or you could do what is the essence of theoretical science: make a model that gives some kind of procedure for computing the answer rather than just measuring and remembering each case."

He introduces the idea of a model through one concrete case, a cannon ball
dropped from the floors of a tower, before he applies the word to anything about
language. The example is small enough to keep in the head and does the explaining,
so the abstract term arrives already grounded.

## Jay Alammar, "The Illustrated Transformer"

Source: https://jalammar.github.io/illustrated-transformer/

> "Let’s begin by looking at the model as a single black box. In a machine translation application, it would take a sentence in one language, and output its translation in another."

He starts from the outside, treating the system as a single black box that takes
an input and returns an output the reader already understands. The first thing
described is what the system does, not what is inside it, which is where the reader
actually stands before the lesson begins.

> "In this post, we will attempt to oversimplify things a bit and introduce the concepts one by one to hopefully make it easier to understand to people without in-depth knowledge of the subject matter."

He states his method before he uses it: oversimplify at first, and bring in the
concepts one at a time, for a reader with no background. Saying it out loud sets
the pace for the whole piece and tells the reader it is fine to not know anything
yet.

> "Don’t be fooled by me throwing around the word “self-attention” like it’s a concept everyone should be familiar with. I had personally never came across the concept until reading the Attention is All You Need paper. Let us distill how it works."

He admits he had not met the term until he read the paper, which keeps him level
with the reader rather than above them. The person on the page is a guide who
learned this recently and is walking through it, not an authority reciting it.

## Chris Olah, Alexander Mordvintsev, Ludwig Schubert, "Feature Visualization"

Source: https://distill.pub/2017/feature-visualization/

> "It turns out that optimization approach can be a powerful way to understand what a model is really looking for, because it separates the things causing behavior from things that merely correlate with the causes."

He separates the thing that causes a behavior from the thing that merely travels
with it, and names that distinction as the reason for the method he chose. It is a
reasoning move rather than a claim, and it shows a writer who checks whether an
explanation is actually the cause before he trusts it.

> "Looking at it in isolation one might infer that this neuron activates on the top of dog heads, as the optimization shows both eyes and only downward curved edges. Looking at the optimization with diversity however, we see optimization results which don’t include eyes, and also one which includes upward curved edges. We thus have to broaden our expectation of what this neuron activates on to be mostly about the fur texture. Checking this hypothesis against dataset examples shows that is broadly correct."

He walks a first guess about what a neuron responds to, shows why it was too
narrow, widens it, and then checks the wider version against real examples. The
writing lets the reader watch an explanation get corrected instead of presenting
only the finished answer. Olah is visible in his willingness to put the wrong
first reading on the page.

> "We don’t fully understand why these high frequency patterns form, but an important part seems to be strided convolutions and pooling operations, which create high-frequency patterns in the gradient."

He marks exactly how far the explanation reaches: the effect is not fully
understood, but one identified part of the system accounts for much of it. The
settled part and the unsettled part sit in the same sentence, each one labeled for
what it is.

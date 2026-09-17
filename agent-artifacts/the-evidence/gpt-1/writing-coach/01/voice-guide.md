# Voice guide: the-evidence/gpt-1

## How this piece should sound

This lesson reads a 2018 technical report and teaches a reader who is smart and
widely read but has never worked in a codebase what the report actually did. The
register is plain and teacherly, the voice of a good instructor at a whiteboard.
Every term the field takes for granted, pre-training and fine-tuning, a
decoder-only Transformer, a downstream task, is new to this reader. Each one
arrives defined in plain words at the moment it is first needed, and nothing in
the lesson leans on a word the reader has not yet been given.

The harder job is to convey why the paper's recipe was a change worth teaching.
GPT-1's two-stage method, pre-train a single model on a large amount of unlabeled
text and then fine-tune it on each task, can look obvious once you already know
it worked. Nielsen opens by making the reader notice how hard a thing they do
effortlessly is, using one string of digits and one count of neurons. The lesson
may need the same move first: put the reader back in front of the problem the
recipe solved, so the method reads as an answer to a question the reader now
holds. Nielsen's face-into-single-pixels passage builds a general idea only after
the reader has watched a hard question split into easy ones, and the
task-specific input transformations that let one model handle classification,
entailment, similarity, and multiple choice can be taught in that order, the
worked case before the general shape.

Reporting the scale honestly is half of what this desk exists for, and the
commission asks for the parameter count, the size of the book corpus, and the
number of downstream tasks, given so the reader feels them. Somers is the model.
He makes an abstract claim concrete by pinning it to one object the reader has
touched, and he lands a figure by attributing it to a named person and letting
the number stand without an adjective. A parameter count means little to this
reader on its own, so it may want anchoring to a present-day model the way Somers
anchors software to a pedal. Where a gain the paper reports is small, the plain
number and its source will serve the reader better than any word describing its
size.

The paper is an origin, so the lesson holds two times at once: what the report
claimed in 2018, and how the recipe scaled and changed after it. Lee shows the
calibration this asks for. He states the size of what is not understood without
dramatizing it and without dismissing it, and he explains a subtle point with
examples a reader can check against their own knowledge. When the lesson reaches
the part later practice dropped, the task-specific fine-tuning and input
transformations that gave way to prompting at larger scale, Lee's temperature
fits: exact about what changed, clear of both triumph and alarm, in keeping with
a desk that lets the evidence carry the weight.

By the end the reader should be able to tell someone else what generative
pre-training is and why one trained model could be pointed at many different
tasks. The passages here keep reaching for the specific token where a general one
would have stood in, and this subject rewards the same habit: the corpus by name,
the task by type, the count as a figure.

## Michael Nielsen, "Using neural nets to recognize handwritten digits" (Neural Networks and Deep Learning, Chapter 1)

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "Most people effortlessly recognize those digits as 504192. That ease is
> deceptive. In each hemisphere of our brain, humans have a primary visual
> cortex, also known as V1, containing 140 million neurons, with tens of billions
> of connections between them."

The opening makes the reader feel a difficulty they had never noticed, and it
does the work with one specific string of digits and one count of neurons instead
of a claim that vision is hard. Nielsen is visible in his willingness to spend
several sentences on how good human eyesight is before he turns to the machine
problem. The reader reaches the hard problem already convinced it is hard.

> "That's the basic mathematical model. A way you can think about the perceptron
> is that it's a device that makes decisions by weighing up evidence. Let me give
> an example. It's not a very realistic example, but it's easy to understand, and
> we'll soon get to more realistic examples."

Nielsen states the formal rule first, then offers a way to picture it, and he
says plainly that the example is unrealistic before he leans on it. The aside
that more realistic examples are coming is a teacher setting expectations, and it
lets him use a toy case without pretending the toy is the real thing.

> "The end result is a network which breaks down a very complicated question -
> does this image show a face or not - into very simple questions answerable at
> the level of single pixels. It does this through a series of many layers, with
> early layers answering very simple and specific questions about the input
> image, and later layers building up a hierarchy of ever more complex and
> abstract concepts."

One sentence carries a whole mechanism because Nielsen names the two concrete
endpoints, a face at one end and single pixels at the other, and lets the layers
sit between them. He introduces the word "abstract" only after the reader has
watched a hard question split into easy ones, so the term describes something the
reader has already seen built.

## James Somers, "The Coming Software Apocalypse" (The Atlantic)

Source: https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

> "Technological progress used to change the way the world looked—you could watch
> the roads getting paved; you could see the skylines rise. Today you can hardly
> tell when something is remade, because so often it is remade by code. When you
> press your foot down on your car's accelerator, for instance, you're no longer
> controlling anything directly; there's no mechanical link from the pedal to the
> throttle. Instead, you're issuing a command to a piece of software that decides
> how much air to give the engine. The car is a computer you can sit inside of.
> The steering wheel and pedals might as well be keyboard keys."

Somers takes an idea that resists a picture, that code has hidden the machinery
of the world, and attaches it to a foot pressing an accelerator. The passage
moves from a wide claim to one object the reader has used, and Somers shows in
the flat confidence of a line like "The car is a computer you can sit inside of."

> "When you're writing code that controls a car's throttle, for instance, what's
> important is the rules about when and how and by how much to open it. But these
> systems have become so complicated that hardly anyone can keep them straight in
> their head. "There's 100 million lines of code in cars now," Leveson says.
> "You just cannot anticipate all these things.""

Somers makes a general worry specific by naming what the throttle code must get
right, then gives a single figure and attributes it to a named expert. The short
quotation and the exact attribution are why the alarm reads as reporting.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon" (Understanding AI)

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "People resolve ambiguities like this based on context, but there are no simple
> or deterministic rules for doing this. Rather, it requires understanding facts
> about the world. You need to know that mechanics typically fix customers' cars,
> that students typically do their own homework, and that fruit typically doesn't
> fly."

Lee explains why ordinary language resists fixed rules with three cases a reader
can test against their own knowledge, about mechanics, students, and fruit. He
asks the reader to trust no term of art, and the register stays everyday while
the point underneath it is subtle.

> "As a result, no one on Earth fully understands the inner workings of LLMs.
> Researchers are working to gain a better understanding, but this is a slow
> process that will take years—perhaps decades—to complete."

Lee states the size of what is not known plainly and puts a rough time frame on
it. The phrase "no one on Earth" is strong, and it reads as measured because the
sentence around it is exact about what is still missing.

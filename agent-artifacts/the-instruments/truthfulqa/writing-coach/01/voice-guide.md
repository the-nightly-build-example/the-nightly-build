# Voice guide: the-instruments/truthfulqa

## How this piece should sound

This is a lesson for a reader who is smart and reads widely but has never taken
a benchmark apart. Write the way Max Roser writes for someone who has never had
to ask what GDP stands for: grant a measure its real use before naming what it
hides, and keep each sentence short enough to hold on one read. The reader should
finish able to ask, of any TruthfulQA figure, which variant it is, how it was
graded, and how its questions were chosen.

The core of the piece is a procedure: how the truthfulness percentage is produced,
from the adversarial selection of questions, through the fine-tuned GPT-judge
grader, to the split between the generative task and the MC1/MC2 variants. Ben
Recht's walk through the ImageNet graph shows one way to carry a construction
step by step. He names each part before he draws anything from it and only then
asks what it means, so a reader who cannot see the machinery can still follow it.
When a step carries a name the reader does not hold, adversarial filtering or a
fine-tuned judge, it can be defined in the sentence it first appears, the way
Recht says what "distribution shift" means the moment he needs the term.

Where the lesson weighs what one percentage can carry, Roser's line about life
expectancy being a measure of population health and hardly its definition is the
distinction in plain form: a TruthfulQA score measures something, and whether
that something is a model being honest is a question the lesson can keep open
rather than settle by the number alone. Dan Luu's cholesterol case is the same
point told through real drugs and real trials: a measured quantity can move
while the outcome it stood for does not. Both writers state the lesson only after
the cases have earned it, never as an opening announcement.

Prefer the specific over the general, the way Recht reaches for Maine and Arizona
instead of the word "generalization," and the way Luu names the actual failed
drugs. A caveat about what a figure hides can sit in the body at the same size as
the finding, as Luu keeps the study's design flaw in the main text rather than a
footnote. When the lesson reaches a verdict about what a TruthfulQA number
supports, it can be owned in plain words, the way Roser writes "strike me as
wrong," and grounded in what the construction actually shows, so it could not be
lifted onto any other benchmark.

Roser and Recht are visible on the page in the first person, Roser's "strike me
as wrong," Recht reporting what "surprised me the most." In this template the
body speaks to no one, and the first person and any address to the reader belong
to the two bookends, so what carries over from those passages is the plainness
and the owned judgment, not the "I." Test the last sentence of each section
hardest. A section on the GPT-judge, or on the gap between MC1 and MC2, should
close on something true of that step, not on a line that grades the lesson as a
whole.

## Ben Recht, "Machine Learning has a validity problem."

Source: https://archives.argmin.net/2022/03/15/external-validity/

> "One of the central tenets of machine learning warns the more times you run experiments with the same test set, the more you overfit to that test set. This conventional wisdom is mostly wrong and prevents machine learning from reconciling its inductive nihilism with the rest of the empirical sciences."

The opening states the common belief in one sentence and then says flatly that it
is mostly wrong. Recht is writing about his own field, and "mostly wrong," with
the jab at "inductive nihilism," is a researcher stating a position he intends to
defend rather than a neutral survey of the literature.

> "In this graph, the x-axis is the accuracy on the original ImageNet benchmark, which has been used millions of times by individual researchers at Google alone. On the y-axis is the accuracy evaluated on “ImageNet v2” set, which was made by closely trying to replicate the data creation method for the benchmark. Each blue dot represents a single machine learning model trained on the original ImageNet data. The red line is a linear fit to these models, and the dashed line is what we would see if the accuracy was the same on both test sets. What do we see? The models which perform the best on the original test set perform the best on the new test set. That is, there is no evidence of overfitting."

He names each part of the chart before he draws anything from it: what the x-axis
is, what the y-axis is, what a single dot is, what the two lines are. Only then
does he ask, "What do we see?" and answer it. A reader who cannot see the figure
can still follow the argument, because every element was defined in plain words
first.

> "The results of a study performed on young male college students in Maine may not help us understand properties of a retirement community in Arizona. These populations are different! However, it may give us insights into other cohorts of male college students: a study at Bates may generalize to Colby or Bowdoin."

The point about how far a result travels is carried by specific places, Maine and
Arizona, Bates and Colby, rather than by the word "generalize" alone. The
exclamation, "These populations are different!", is a person thinking through the
idea aloud, which keeps a fairly abstract point about validity concrete.

## Max Roser, "What is economic growth? And why is it so important?"

Source: https://ourworldindata.org/what-is-economic-growth

> "Poverty, prosperity, and growth are often measured in monetary terms, most commonly as people’s income. However, while monetary measures have some important advantages, they have the big disadvantage of being abstract. In the worst case, monetary measures — like GDP per capita — are so abstract that we forget what they are actually about: people’s access to goods and services."

Roser grants the monetary measure its real advantage before he names its flaw,
and then says exactly what the abstraction makes people forget: access to goods
and services. He is writing for someone who has never had to ask what a figure
like GDP stands for, and each sentence is built to be held on a single read.

> "Wikipedia defines economic growth as follows: “Economic growth can be defined as the increase in the inflation-adjusted market value of the goods and services produced by an economy over time.” Definitions that are based on how growth is measured strike me as wrong — just like life expectancy is a measure of population health and hardly the definition of population health."

He quotes a standard definition and then says plainly why defining a thing by the
way it is measured is a mistake, using life expectancy and population health as
the parallel. The verdict, "strike me as wrong," is first person and owned, not
handed off to a vague consensus.

## Dan Luu, "Goodhearting IQ, cholesterol, and tail latency"

Source: https://danluu.com/percentile-latency/

> "Unfortunately, due to methodological problems in the study design, it's not 100% clear where these effects come from. Although the goal was to do a randomized trial, the experimental design necessitated home visits for the experimental group. As a result, children in the experimental group whose mothers were employed swapped groups with children in the control group whose mothers were unemployed."

Luu reports the study's result and then, in the same passage and at the same
size, the design flaw that undercuts it: the two groups did not stay separate.
"It's not 100% clear where these effects come from" is an engineer saying exactly
how much weight the number can bear, in the main text and not a footnote.

> "Some interventions that affected cholesterol levels also affected real health outcomes, prompting people to develop drugs that affect cholesterol. But it turns out that improving cholesterol isn't an inherent good, and like many intermediate targets, it's possible to improve without affecting the end goal."

The cholesterol case is a sequence of real interventions and real trials, and the
lesson arrives only at the end, once the failures have made it: moving the
measured quantity did not move the outcome it stood for. Luu lets the cases carry
the point rather than announcing it first.

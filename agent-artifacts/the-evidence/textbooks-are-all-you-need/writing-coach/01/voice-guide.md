# Voice guide: reading "Textbooks Are All You Need" (phi-1)

## How this piece should sound

This lesson reads one technical paper closely for a reader who is smart and
widely read but has never trained a model. The job is to say what the phi-1
paper actually did with its data and its numbers, and to separate the result it
earned from the "quality beats scale" slogan the title turned into. Hold the
register Timothy B. Lee holds in the passages below: short declaratives, one
idea to a sentence, and no word bigger than the point needs. Lee ends a hard
point about language with "fruit typically doesn't fly" and does not dress it
up. When the paper's own vocabulary appears, benchmark scores, filtered training
data, model size measured in parameters, that vocabulary can stay at its full
precision, the way Lee keeps the real terms and lets the plain sentences around
them carry the meaning.

The paper works in quantities a general reader cannot picture on their own: how
many tokens of data, how many parameters, what a pass rate on a coding benchmark
means. Where one of those numbers carries the argument, Lee's move is available.
He introduces the idea of a vector by mapping it onto latitude and longitude,
then checks the intuition with arithmetic the reader can run themselves, that
38.9 is close to 40.7. A phi-1 figure the reader cannot scale can be anchored to
something they already hold, and the comparison can be made concrete enough that
they can see it holds.

The center of the lesson is the gap between what the paper measured and what the
slogan claims, and Melanie Mitchell's passages show two moves the material will
call for. One is to ask, plainly, what the evidence for a claim actually is, and
then to name what it consists of in order, the way she answers "what is
Friedman's evidence for all this?" by listing the source and noting who was not
consulted. The other is to grant what is genuinely true before correcting the
rest: Mitchell concedes that LLMs really are surprisingly good at translation
before she traces that ability to parallel text in the training data. phi-1's
reported result was real, and conceding the earned part first is what lets the
correction of the slogan read as fair rather than as debunking.

If the piece sets the slogan against what the paper showed, the contrast has to
be earned. Mitchell's "not mysterious, but another consequence" works because
the mystery is the exact belief she is answering, one her subject actually
holds. A contrast drawn against "quality beats scale" is honest only if the
piece has stated that reading as something real people take from the paper, and
not against a version of it the piece invented to knock down.

The paper's evidence is a set of benchmark measurements, and Dan Luu's passages
show how to weigh a measurement rather than only report its result. He marks
what the evidence cannot show, that there is no counterfactual to compare
against, before stating the conclusion he will still stand behind, so the claim
and its limit arrive together. Where a phi-1 number cannot be stretched to
support the slogan, that limit can be stated in the same breath as the number.
Luu also treats a measurement as something that can itself be weak, noting that
most published measurements are poor and that readers cannot easily tell a good
one from a bad one. Whether a benchmark score means what it appears to mean,
including questions about what was in the data the model was tested against, is
inside the lesson's remit, not outside it.

What the paper found, what the numbers were, and where the verdict lands are
yours to reach from the document. The passages below show the sound, not the
conclusion.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "This is useful for reasoning about spatial relationships. You can tell New York is close to Washington DC because 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is close to London. But Paris is far from Washington DC."

Lee has just introduced an abstraction the reader has no feel for, a vector, and
here he grounds it in coordinates the reader already understands and then checks
the intuition with specific numbers they can compare themselves. He does not ask
the reader to take the analogy on faith; he runs the comparison in front of
them. The sentences are short and each carries one step, and Lee is visible in
his willingness to do the small arithmetic out loud rather than assert that it
works.

> "People resolve ambiguities like this based on context, but there are no simple or deterministic rules for doing this. Rather, it requires understanding facts about the world. You need to know that mechanics typically fix customers' cars, that students typically do their own homework, and that fruit typically doesn't fly."

He states a general point, that there are no fixed rules for resolving what a
sentence means, and then makes it concrete with three ordinary facts the reader
can test against their own knowledge. The passage lands on "fruit typically
doesn't fly," an everyday fact stated flatly, and it is enough. Lee trusts small
examples to carry a hard idea and never reaches for a grander word than "know."

## Melanie Mitchell, "Magical Thinking on AI"

Source: https://aiguide.substack.com/p/magical-thinking-on-ai

> "So it's worth asking, what is Friedman's evidence for all this? Well, number one, Mundie's opinions. Mundie is a business executive, not an AI researcher, and it doesn't sound like any AI researchers were asked for their views"

Faced with a large claim, Mitchell asks the plainest question available, what is
the evidence, and answers it by naming what the evidence consists of. Noting that
the source is a business executive and that no researchers were consulted does
the deflating without a single adjective. Mitchell is visible in the flat
enumeration, "Well, number one," and in refusing to describe the claim as
anything grander than its sourcing supports.

> "It's true that large language models are surprisingly good at translation, and that no one explicitly programmed in this ability. However, it turns out that this ability is not mysterious, but another consequence of the unimaginably large set of data these systems are trained on. These training corpora contain many examples of “parallel text” in English and other languages, which is the same kind of data that systems like Google Translate are trained on."

She concedes what is genuinely true first, that the ability is real and that no
one built it in by hand, and only then traces the surprise to an ordinary cause
in the training data. The contrast with "mysterious" is earned because the
mystery is the exact belief she is answering, not one she set up to knock down.
Mitchell is visible in the care of the concession: she gives the impressive part
its due before explaining it, so the correction reads as fair.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "Although we don't have an A/B test of universes where Kyle exists vs. not and can't say how long it would've taken for distributed systems to get serious about correctness in a universe where Kyle didn't exist, from having spent many years looking at how developers treat correctness bugs, I would bet on distributed systems having rampant correctness problems until someone like Kyle came along."

Luu marks exactly what the evidence cannot establish, that there is no
counterfactual to measure against, before he states the conclusion he will stand
behind and says what it rests on, years of watching how developers handle bugs.
The claim and its limit sit in the same sentence. Luu is visible in the way he
separates what he knows from what he would bet and tells the reader which is
which.

> "One thing that both increases and decreases the impact of doing good measurements is that most measurements that are published aren't very good. This increases the personal value of understanding how to do good measurements and of doing good measurements, but it blunts the impact on other people, since people generally don't understand what makes measurements invalid and don't have a good algorithm for deciding which measurements to trust."

He makes a plain claim, that most published measurements are poor, and then
follows it to two consequences, including the uncomfortable one that even good
measurements travel badly because readers cannot tell them from bad ones. Luu
states the cost of his own thesis, not only its benefit. He is visible in holding
measurement to the same skeptical standard he applies to the things being
measured.

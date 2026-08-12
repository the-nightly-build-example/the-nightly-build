# Voice guide: the-evidence/grokking

## How this piece should sound

This is a lesson that reads one research paper and tells a smart, widely read
reader what it actually measured. The reader has spent no time in a codebase, so
the technical terms this piece needs — modular arithmetic, weight decay, the
difference between memorizing a training set and generalizing to the held-out
part of it — enter in plain words the first time they appear. Tim Harford's
aside defining statistical significance inside running prose shows a term of art
handled without stopping the sentence to lecture. Hold the whole piece at that
register: load-bearing explanation, no hype, the plainest word that carries the
idea.

The article works across a gap. What the grokking paper measured was delayed
generalization on a small algorithmic dataset. What the word "grokking" now
carries is a general claim about why large models improve. Where a single figure
makes the distance between those two things legible — the size of the training
setup, the fraction of the table used, the number of optimization steps — the
piece can place it where the reader will feel it, the way Harford sets 42
subjects against 34 million viewers and Ed Yong sets 15,305 participants and a
sixty-times comparison against the studies being retested. Where the figure
itself is available, it can stand in the sentence in place of a word that only
gestures at how large or small the thing is.

Grokking is real, reproducible, and small, and the reader should be able to hold
all three. The everyday reading — a sudden phase change, evidence that big
models harbor hidden generalization — can be stated at its strongest before the
piece weighs it against what the mechanistic-interpretability and weight-decay
follow-ups found. Yong lays out the skeptics' three explanations in order before
he answers them, and that fairness is what lets his verdict land. When the piece
reaches its central correction, that grokking as measured is delayed
generalization on toy tasks rather than a demonstrated mechanism of frontier
emergence, it lands once the misconception it corrects is named plainly, the way
Willison draws the real target of a prompt-injection attack apart from the target
readers assume.

Say the limits of the result without talking the result down to nothing. Willison
states plainly that his own proposed defense is poor and still leaves the reader
with a clear picture; the grokking piece can say what the original experiment did
not test and keep the effect intact. The hardest thing to keep plain here is the
account the follow-up work gives of what happens under the test-accuracy curve
while it stays flat. That is an abstraction the reader cannot carry unbuilt, so it
wants the concrete handling Harford gives statistical significance and Willison
gives the translation app, worked out in the network's own terms rather than
summarized in the language of phase changes.

## Tim Harford, "The dubious power of power poses"

Source: https://timharford.com/2016/06/the-dubious-power-of-power-poses/

> "The astonishing findings? Well, actually, there were no astonishing findings: the power poses seemed to make no difference worth mentioning. High-power poses were correlated with slightly lower testosterone and slightly higher cortisol — the opposite of what might be expected, but tiny and statistically indistinguishable from chance."

Harford sets up a question that promises a result and then reports flatly that
there was none, and he still gives the reader the real direction and size of the
effect rather than waving it away. He is visible in the dry "Well, actually,
there were no astonishing findings", which reports a null result without
deflating the reader's interest in the story.

> "But perhaps the most important lesson is to remember that while "statistical significance" sounds scientific, it's hardly a cast-iron endorsement of a result. The theory behind statistical significance assumes that a single pre-chosen hypothesis will be tested. In practice, researchers rarely pre-specify their hypothesis. They can test dozens, or hundreds — and sooner or later a pattern will emerge, if only by chance."

He defines a statistics concept in everyday words and then walks through why a
significant result can still be a fluke, moving from the pre-chosen hypothesis to
the dozens tested in practice. The teacher is visible in how far he keeps the
explanation from jargon while still saying something exact.

> "There are various technical solutions to this problem. But a little common sense also goes a long way. When a study of 42 subjects inspires 34 million people, it's not unreasonable to go back and check the results."

The column closes on two concrete numbers held against each other, 42 and 34
million, so the figures carry the judgment instead of an adjective. Harford's
restraint shows in "a little common sense also goes a long way", which states the
point without inflating it.

## Ed Yong, "Psychology's Replication Crisis Is Running Out of Excuses"

Source: https://www.theatlantic.com/science/archive/2018/11/psychologys-replication-crisis-real/576223/

> "Over the past few years, an international team of almost 200 psychologists has been trying to repeat a set of previously published experiments from its field, to see if it can get the same results. Despite its best efforts, the project, called Many Labs 2, has only succeeded in 14 out of 28 cases."

Yong leads with the count, 14 out of 28, before any interpretation, so the reader
holds the result before being told what to make of it. He reports the size of the
effort, almost 200 psychologists, as a plain fact rather than a boast.

> "But skeptics have argued that the misleadingly named "crisis" has more mundane explanations. First, the replication attempts themselves might be too small. Second, the researchers involved might be incompetent, or lack the know-how to properly pull off the original experiments. Third, people vary, and two groups of scientists might end up with very different results if they do the same experiment on two different groups of volunteers."

He states the opposing case in three numbered objections, each a real one, before
the piece answers any of them. The fairness is visible in how completely he gives
the skeptics their argument, which is what earns his later verdict.

> "The Many Labs 2 project was specifically designed to address these criticisms. With 15,305 participants in total, the new experiments had, on average, 60 times as many volunteers as the studies they were attempting to replicate."

He makes the scale concrete with a total and a comparison, 15,305 participants and
sixty times the original samples, so the reader can weigh how much the
replication actually tested. The specific ratio does the work that "much larger"
would have left vague.

## Simon Willison, "Prompt injection explained, with video, slides, and a transcript"

Source: https://simonwillison.net/2023/May/2/prompt-injection-explained/

> "prompt injection is an attack against applications that have been built on top of AI models. This is crucially important. This is not an attack against the AI models themselves. This is an attack against the stuff which developers like us are building on top of them."

Willison draws a precise line between the model and the applications built on it,
correcting the assumption a reader arrives with. The correction is earned because
it names the misconception it is fixing, and he is visible in the flat "This is
crucially important" that marks where the distinction matters.

> "It's easy to build a filter for attacks that you know about. And if you think really hard, you might be able to catch 99% of the attacks that you haven't seen before. But the problem is that in security, 99% filtering is a failing grade."

He puts a number on the near-miss, catching 99 percent, and then explains why in
security that number is a failure, turning an abstract limit into something the
reader can hold. The engineer is visible in treating a result that sounds good as
plainly not good enough.

> "I have a potential solution. I don't think it's very good. So please take this with a grain of salt."

He states the weakness of his own proposal outright and still leaves no doubt
about what he thinks of it. The honesty is the point of the passage: he refuses
to oversell an idea he is the one putting forward.

# Voice guide: the-instruments/mean-average-precision (01)

## How this piece should sound

This lesson has one job before it has any other: get the reader to watch mAP
get built, number by number, so that when it says "mAP@0.5 and mAP@[.5:.95]
are not the same measurement," the reader already feels why. Lee's habit of
laying out the raw figures before naming what they mean — the METR chart's
task-length numbers arrive before he tells the reader what they imply about
acceleration — is the model for the worked AP example: give the ranked
detections and their hit/miss calls first, let the precision-recall curve
take shape on the page, and only then say what area-under-the-curve buys you.
Don't tell the reader a curve is coming and then produce it; produce it and
let the shape argue for itself.

The IoU-threshold problem is this lesson's spine, and Lee's "so we know X, but
it's hard to say how much" move is the right shape for it. State plainly what
changed between VOC's mAP@0.5 and COCO's mAP@[.5:.95] — one fixed overlap
test versus an average over ten — as its own sentence, and only then let the
"these numbers don't compare" conclusion land as a separate sentence. Naming
the mechanism and naming the consequence are two different jobs; collapsing
them into one sentence is how the reader ends up nodding along without
having actually checked the claim.

When the lesson catalogs what a single mAP number averages away — classes,
confidence thresholds, IoU thresholds — Karpathy's list of ways a neural net
fails silently ("You plugged in an integer where something expected a
string. The function only expected 3 arguments. This import failed.") shows
how a run of short, flat declaratives can carry more than one sentence
straining to hold every case at once. The detection equivalent is concrete
and available here: a model can score well by nailing the common classes and
missing a rare one nearly every time, or by looking good at the confidence
threshold nobody runs in production. List those plainly, one clause each,
rather than folding them into a single qualified sentence.

The lesson also needs one moment where it punctures the assumption that a
higher mAP simply means "the detector got better," and Karpathy's "For sure
no. That is the road to suffering." is worth studying for how it does this:
the deflation works because it's aimed at a specific named absurdity (his own
invented "Multi-scale ASPP FPN ResNet"), not a straw version of the
temptation. The mAP lesson has its own specific case for this move — the
real deployment where a higher score didn't track real-world performance —
and the puncture should be aimed at that case's actual numbers, not at a
generic claim that "metrics can mislead."

Rachel Thomas's proxy paragraph — three short parallel sentences, each
pairing what you want to know with what you actually measure — is a
technique this lesson can use once, for the point that mAP is a proxy for
"the detector works when it matters" and not the thing itself. It should be
built from the lesson's own material: what a deployment actually needs
(catching the rare, safety-relevant class; working at the confidence
threshold the system runs at) against what mAP actually rewards (rank
ordering across all classes and thresholds at once). Two or three real pairs
do this; a fourth run over the pattern would just be showing off the trick.

The closing judgment about what a reported mAP number does and doesn't
license should follow Thomas's own closing habit: name the specific
documented case and its actual cost, not a general caution about metrics.
The lesson has one real case in hand by the time it gets there — use its
numbers, not a summary of the genre of harm it belongs to.

## Timothy B. Lee, "Why it's getting harder to measure AI performance"

Source: https://www.understandingai.org/p/why-its-getting-harder-to-measure

> "I think this chart — and especially the impressive score for Claude Opus
> 4.6 — has done a lot to foster an impression of accelerating AI progress in
> recent months. Notice that the chart is logarithmic, so a straight line
> indicates exponential progress. The fact that Claude Opus 4.6 is above the
> previous trend line suggests very rapid progress indeed."

This is a writer walking a reader through how to read a chart, not just what
it shows: he names the axis choice (logarithmic) and says exactly what a
straight line on it would mean before saying what this particular dot does.
The claim about "very rapid progress" only shows up after the mechanics are
on the table, so the reader can check it rather than take it.

> "So we know the latest Claude Opus is better than previous models, but it's
> hard to say how much better. This means we don't know if the apparent
> acceleration of the last few months is real or just a statistical
> artifact."

Two plain sentences hold a real hedge without hedging language: no "arguably"
or "it could be argued." The first sentence concedes what's known, the second
names exactly what isn't, and the word "artifact" does the technical work
instead of a vaguer word standing in for it.

> "So conventional benchmarks like MMLU have a natural lifecycle. At first,
> most problems are beyond models' capabilities, so scores cluster near the
> minimum. As models improve, benchmark scores increase until they approach
> the theoretical maximum. Since 2024, frontier models have all scored
> between 88% and 93%, a narrow enough range that differences could be random
> noise. In industry jargon, MMLU has saturated."

He defines a term of art ("saturated") by walking through the mechanism that
produces it rather than by giving a dictionary-style definition first. The
number range (88 to 93 percent) is the evidence for the definition, not
decoration next to it, and the jargon word only arrives once the reader has
already watched the thing it names happen.

## Andrej Karpathy, "A Recipe for Training Neural Networks"

Source: http://karpathy.github.io/2019/04/25/recipe/

> "When you break or misconfigure code you will often get some kind of an
> exception. You plugged in an integer where something expected a string.
> The function only expected 3 arguments. This import failed. That key does
> not exist. The number of elements in the two lists isn't equal."

Five short sentences, each one a distinct concrete failure, none of them
qualified or softened. The list form does work a single summarizing sentence
couldn't: it lets the reader recognize the pattern from their own experience
of any one of the five, which is what makes the contrast with silent failure
land in the next paragraph.

> "As a result, (and this is reeaally difficult to over-emphasize) a 'fast
> and furious' approach to training neural networks does not work and only
> leads to suffering. Now, suffering is a perfectly natural part of getting a
> neural network to work well, but it can be mitigated by being thorough,
> defensive, paranoid, and obsessed with visualizations of basically every
> possible thing. The qualities that in my experience correlate most
> strongly to success in deep learning are patience and attention to detail."

The stretched spelling of "reeaally" and the parenthetical aside are the one
place his own voice interrupts the explanation directly, and it's spent on
underlining a claim rather than on a joke at the reader's expense. The
sentence that follows commits to a specific, checkable claim (patience and
attention to detail correlate with success) instead of trailing into a vaguer
moral.

> "Now that we understand our data can we reach for our super fancy
> Multi-scale ASPP FPN ResNet and begin training awesome models? For sure no.
> That is the road to suffering."

The question invites the reader to want the fancy model, and the three-word
answer refuses it outright. The joke depends entirely on the invented,
absurdly specific architecture name he supplies himself — it wouldn't survive
being generic — which is why it still counts as saying something rather than
just being glib.

## Rachel Thomas, "The problem with metrics is a big problem for AI"

Source: https://www.fast.ai/posts/2019-09-24-metrics.html

> "Goodhart's Law states that 'When a measure becomes a target, it ceases to
> be a good measure.' At their heart, what most current AI approaches do is
> to optimize metrics. The practice of optimizing metrics is not new nor
> unique to AI, yet AI can be particularly efficient (even too efficient!) at
> doing so."

She opens on someone else's named law rather than her own framing, then
states her own claim in one flat sentence right after it. The parenthetical
"(even too efficient!)" is the one spot her own voice shows through, and it's
doing real work: it's the reason the rest of the piece needed writing at all.

> "This an example of the common phenomenon of having to use proxies: You
> want to know what content users like, so you measure what they click on.
> You want to know which teachers are most effective, so you measure their
> students test scores. You want to know about crime, so you measure arrests.
> These things are not the same."

Three sentences, same structure, three completely different domains — she
never explains why the pattern repeats, she just lets three instances of it
sit next to each other until the reader sees it themselves. The four-word
sentence that closes it out states the conclusion as plainly as it can be
stated, after the examples have already done the arguing.

> "I am not opposed to metrics; I am alarmed about the harms caused when
> metrics are overemphasized, a phenomenon that we see frequently with AI,
> and which is having a negative, real-world impact. AI running unchecked to
> optimize metrics has led to Google/YouTube's heavy promotion of white
> supremacist material, essay grading software that rewards garbage, and
> more. By keeping the risks of metrics in mind, we can try to prevent these
> harms."

The closing distinction ("not opposed to metrics" versus "alarmed about"
overemphasis) is precise rather than a hedge, and the sentence right after it
names the actual documented harms instead of gesturing at "consequences" in
general. The piece ends on the same specific cases it argued from, not on a
wider moral about metrics as a category.

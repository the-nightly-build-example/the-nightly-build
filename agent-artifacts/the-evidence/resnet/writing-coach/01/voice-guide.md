# Voice guide: the-evidence/resnet (01)

## Directive

This lesson has to make a result feel inevitable that sounds wrong on its
face: a deeper network that does worse at fitting data it has already seen.
Write so the reader arrives at that result half a step before you state it.
Build the mechanism as an operation the reader runs in their own head, then
name the consequence. Do not state the consequence and then justify it
backward; a section that opens on the verdict has stopped teaching the
mechanism and started grading it.

Two things the reader will want to fuse, and this article keeps apart on
every mention: what a measurement showed, and what the document is remembered
for. When a number enters, say what it measured before you say what it means.
A figure is training error or it is test error, never "the results"; the
distinction is the lesson, so it survives to the sentence, not just the
paragraph.

Correct the common reading once, by naming it as a thing a careful person
would believe, not by scoring against it. The plain register the house
already asks for gets you clarity; it does not, on its own, get you a
counterintuitive mechanism the reader feels click, or a record held exact
against its own legend. Those are this article's work.

## Licenses

form: a sustained concrete analogy for the optimization mechanism
move: Olah carries one physical picture across a whole passage, layers
  stretching and folding space, so the reader watches an abstract operation
  happen and can predict its outcome; he reaches for it exactly where the
  formal statement would land as a symbol the reader cannot feel.
bar:  the reader must be able to run the analogy to reach the paper's own
  result, why plain depth makes the target harder to hit and what a skip path
  changes; the first sentence where the picture would have the reader believe
  something false about what a residual computes, the analogy is cut, not
  softened into a hedge.

form: second-person walk-through of the mechanism
move: Karpathy hands the reader the operation and has them trace it, so the
  failure is one the reader discovers rather than is told; he spends the "you"
  at the exact step where forward intuition and backward consequence diverge.
bar:  each "you" must ask the reader to do or predict something specific,
  follow a signal, guess which net fits worse, say what stacking one more
  plain layer costs; a "you" that only decorates a claim the reader is not
  performing ("as you can see") is cut.

form: the named misreading, used once as the article's hinge
move: Gwern states the legend in full and with sympathy before separating it
  from the record, tracing what the sources actually support; the correction
  lands because the myth was given its strongest form first.
bar:  the misreading must be one a careful reader genuinely holds, named
  plainly and granted its logic once; every later mention adds record the
  first did not, and never swings again at the same strawman. One hinge per
  piece, inside the house ceiling on earned contrast.

## Chris Olah, "Neural Networks, Manifolds, and Topology"
Source: https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/
Craft:
- cadence: short declaratives act as pivots between longer scaffolding
  sentences; a plain line lands each turn before the next build starts.
- argument: descends from a toy case, two tangled curves, to the abstract
  claim that a layer is a continuous deformation of space, then back to
  consequence; the abstraction arrives only after the concrete case demands it.
- evidence: shows the network failing on the hard case before explaining why
  it must fail; the picture precedes the reason, so the reason reads as a
  description of something already seen.
- stance: fellow explorer, not authority; states the limits of his own
  knowledge in the open rather than papering over them.
- notice: shape and motion, what each layer does to space, rather than
  accuracy figures or runtime.
- diction: physical verbs carry the load (stretch, squish, fold); each
  technical term arrives with an immediate plain gloss in the same breath.
- reader: positioned as someone who can watch the mechanism operate, not just
  accept a stated property of it.
- the move the axes miss: he converts an invisible property into a motion the
  reader watches happen, so the formal result feels inevitable by the time it
  is written down.

## Andrej Karpathy, "Yes you should understand backprop"
Source: https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b
Craft:
- cadence: short blunt lines interrupt longer technical passages; the tempo
  shifts function as rest stops between dense stretches.
- argument: framing (why bother understanding this) into three escalating
  failure cases into a real bug that cost real work; each case runs
  identify-the-mechanism, show-where-intuition-fails, show-the-cost.
- evidence: the exact place the danger lives is shown concretely, a
  multiplication or a threshold, rather than described in the abstract.
- stance: fellow-traveler protecting the reader from a comfortable false
  belief; he dismantles it by showing it is dangerous in practice, not merely
  wrong in theory.
- notice: the gap between the forward operation and its backward consequence,
  and the single step where the two diverge.
- diction: vivid failure verbs anchor abstract behavior (vanish, explode, die,
  saturate).
- reader: made to discover the failure by tracing it, then trusted with the
  consequence rather than lectured on it.
- the move the axes miss: he has the reader run the mechanism in the direction
  where naive intuition reverses, so the correction is felt instead of
  asserted.

## Gwern Branwen, "The Neural Net Tank Urban Legend"
Source: https://gwern.net/tank
Craft:
- cadence: bursts of catalogued variation, then slower forensic paragraphs;
  accumulation of specifics before any analytical frame is laid over them.
- argument: piles dated, sourced versions until the pattern is undeniable,
  every detail varies and no citation chain reaches a primary source, then
  names what the pattern means.
- evidence: each version carries its date, source, and quotation; where a
  source hedges its own certainty, the hedge is quoted verbatim rather than
  smoothed away.
- stance: skeptical but generous; refuses contempt for those repeating the
  story and grants it its real appeal before taking it apart.
- notice: variation and the missing origin, what a true fact would reproduce
  consistently and this one does not.
- diction: technical terms sit beside plain, almost folkloric words (urban
  legend, leprechaun), signaling a real problem discussed in the language of
  myth.
- reader: addressed as a fellow investigator who probably believed it too, and
  invited to check the record together.
- the move the axes miss: he traces sourcing backward until the chain ends,
  making the absence of a traceable primary claim the evidence itself.

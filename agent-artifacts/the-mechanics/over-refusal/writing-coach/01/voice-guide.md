# Voice guide: the-mechanics/over-refusal

## Directive

Register: a knowledgeable colleague walking someone through why a machine
just did something surprising, one mechanical layer at a time. Never a
lecturer, never a hedge-everything researcher. Reader relationship: assume
they already feel the phenomenon (a harmless request got refused) and want
the actual mechanism, not reassurance and not a scolding about jailbreaks.

Moves to use in this draft:

- **Make the direction physical before you name it.** The exemplars below
  never leave a vector abstract. They give it a behavior first ("this net
  detects leftward-facing dogs and rightward-facing dogs, then unions them"),
  and only then say what that behavior corresponds to mathematically. Do the
  same with the refusal direction: describe what happens to the network's
  internal state when it refuses, in terms of a comparison the reader already
  has (a dial, a single switch, a line a value crosses), before you call it a
  "direction." Earn the geometry with a worked example first; do not open on
  the word "direction" and explain backward.
- **Stage the causal chain as a sequence of separately-checkable steps, not a
  narrative.** Each step gets its own sentence or short paragraph that states
  what is true at that layer and how anyone could check it. Do not let two
  steps share a sentence. When you reach a step nobody has fully verified,
  say so in the same plain register as the settled steps, not with a
  hand-wave word like "somehow" or a hedge pile-up. State the boundary once,
  cleanly, the way a step is stated: "this part is measured; this next part
  is inferred; here is the inference."
- **Strip agency verbs from every sentence about the model's internal
  behavior.** No "decides," "notices," "judges," "understands," "wants," or
  "believes" applied to the network. Replace with what is mechanically true:
  a value crosses a threshold, a computation activates, an output gets
  selected. If a sentence is hard to write without an agency verb, that is
  the sentence to slow down on and make more concrete, not the one to patch
  with scare quotes.
- **Correct the "it judged this dangerous" misreading with a fact, not a
  contrast frame.** Do not write "it's not judging danger, it's ___." State
  what actually happens (the mechanism, the training origin) and let the
  misreading fall on its own once the reader has the real mechanism. Save any
  explicit contrast, if you use one at all, for the single place in the piece
  where the misconception is most load-bearing, and name the misconception
  precisely rather than gesturing at it.
- **Let plain comparisons do the work a diagram would.** Every exemplar below
  reaches for a comparison the reader can hold in their head, not a technical
  restatement, when a concept has no picture to point to. Do the same for
  "direction in activation space": find the one comparison that survives
  contact with the actual math, and reuse it exactly once it is set, rather
  than restating the idea three different ways.

Recently used, do not reuse:
- Comma-triad headings or deks, and the "instructions-are-data" heading mold
  ("The prompt a model actually sees"). Find this article's own heading
  shapes.
- Any reusable closer formula or house catchphrase.
- The word "machinery" is banned in this paper. Use the concrete part name
  instead (the layer, the weight, the activation, the vector) every time the
  impulse toward "machinery" shows up.

## Exemplars

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"
Source: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
Craft:
- cadence: Short declaratives to open a section, then one longer sentence
  that does the technical work once the reader is oriented. He never opens
  a section on the technical sentence.
- argument: Builds from a demonstration (the network generating text) to the
  mechanism behind it, always in that order. Evidence comes before claim.
- evidence: Concrete generated samples and specific hidden-unit behaviors he
  actually visualized, not generic claims about what RNNs "can do."
- stance: Enthusiastic but self-checking. He flags his own reach the moment
  he makes one.
- notice: Calls out cells that track quotes, line length, or code
  indentation, one specific behavior at a time, never a bucket like "the
  network learns structure."
- diction: Plain verbs for network behavior ("fires," "tracks," "turns on")
  rather than mental-state verbs.
- reader: Treats the reader as someone willing to look at a real example
  before hearing the abstraction, and rewards that willingness immediately.
- the move the axes miss: he marks the exact edge of his own certainty
  mid-sentence rather than in a separate caveat paragraph, so the hedge
  never breaks the sentence's momentum.
Calibration: "Of course, a lot of these conclusions are slightly hand-wavy as
the hidden state of the RNN is a huge, high-dimensional and largely
distributed representation."

## Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, Shan Carter, "Zoom In: An Introduction to Circuits"
Source: https://distill.pub/2020/circuits/zoom-in/
Craft:
- cadence: States a claim as a numbered claim, then spends a paragraph
  showing the concrete case that supports it, then states the next claim.
  The rhythm is claim, evidence, claim, evidence, never claim-claim-claim.
- argument: Explicitly separates "claim" from "established fact." Three
  claims are labeled as claims, not findings, and the piece never blurs that
  line for effect.
- evidence: A single named unit's behavior, described in terms anyone could
  go look up in the visualized network, e.g. detecting dogs facing one way
  and dogs facing the other way and then combining the two.
- stance: Confident about the mechanism it has actually traced, openly
  speculative about how far the pattern generalizes.
- notice: Notices that a property (orientation invariance) that looks like a
  single fact is actually built from two narrower, checkable facts glued
  together, and shows the reader the seam.
- diction: "Correspond to," "connected by," "form" — verbs of structure and
  composition, never verbs of cognition.
- reader: Invites the reader to treat the finding as unfinished science, not
  as a revealed truth to accept.
- the move the axes miss: it names its own speculation as speculation in the
  same sentence as the claim, so the reader never has to guess which parts
  are settled.
Calibration: "Features are the fundamental unit of neural networks. They
correspond to directions [in the space of neuron activations]." (labeled
explicitly as a claim, not a conclusion)

## Neel Nanda, "A Comprehensive Mechanistic Interpretability Explainer & Glossary"
Source: https://www.neelnanda.io/mechanistic-interpretability/glossary
Craft:
- cadence: Defines a term in one plain sentence, immediately admits where the
  definition gets fuzzy, then gives the example that makes the fuzziness
  concrete. Definition, honest limit, example, in that order every time.
- argument: Builds understanding by contrasting a clean textbook version of
  an idea against what actually happens in practice, and keeps both in view
  rather than resolving the tension.
- evidence: Named experimental patterns ("a surprising amount of behaviours
  are localised, but many are not") rather than a single showcase result.
- stance: Working scientist thinking out loud, comfortable saying a concept
  is not rigorous rather than dressing it up.
- notice: Flags exactly which intuitions transfer from a clean toy case to
  messy real models and which do not, instead of implying the toy case
  settles it.
- diction: Everyday words first ("a property of an input"), technical term
  second, never the reverse.
- reader: Talks to the reader as someone learning to think about the field,
  not someone being handed conclusions.
- the move the axes miss: he states the "why should you care" for a term in
  the same breath as the definition, so nothing sits inert waiting to matter
  later.
Calibration: "A feature is a property of an input to the model...This is a
fuzzy and non-rigorous idea, best illustrated by examples."

## Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?"
Source: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/
Craft:
- cadence: States the mechanism's job in one sentence before touching any
  detail of how it's built, so the reader always knows what the next several
  paragraphs are in service of.
- argument: Repeatedly draws the line between "what we can observe this
  system doing" and "what we can explain about why it does that," and treats
  the gap between them as a fact worth stating rather than a failure to
  paper over.
- evidence: Points at demonstrable, checkable behavior (a specific net
  behaving a specific way) before generalizing.
- stance: Unshowy and literal. No excitement performed for its own sake; the
  interesting part is left to be interesting on its own.
- notice: Notices when a plausible-sounding claim about "why" a network works
  has no actual theory behind it, and says exactly that, in the same voice
  used for settled facts, so the uncertainty doesn't read as a lesser
  sentence.
- diction: Scare quotes around folk terms ("reasonable," "narrative
  description") used loosely elsewhere, to flag that he is borrowing the word
  provisionally, not asserting it as literal.
- reader: Assumes the reader wants the honest current limit of
  understanding, not a tidy story.
- the move the axes miss: he uses the same flat declarative register for "here
  is what is known" and "here is what is not known," so the reader never
  senses a shift in confidence from the prose rhythm alone, only from the
  content.
Calibration: "It's worth emphasizing that there's no 'theory' being used
here; it's just a matter of what's been found to work in practice...But at
least as of now we don't have a way to 'give a narrative description' of
what the network is doing."

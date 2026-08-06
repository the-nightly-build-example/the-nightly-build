# Voice guide: the-mechanics/memorization

## Directive

Write as a patient mechanic who has one object in hand and takes it apart a layer
at a time. The house voice already gives you plain words, short sentences, and
worked numbers. What this lesson needs on top of that is a single organizing
discipline: one descent, one specimen, carried the whole way down. The register
stays plain and unhurried; the confidence comes from never skipping a step, not
from asserting.

The reader has done the thing. They asked a model for the opening line of
something famous and got it back exactly. Treat that returned line as the
specimen on the bench. Four moves change sentences here.

1. **Keep one string alive across the descent.** Choose the specimen line in the
   first move and carry the same line through every step: the surface behavior,
   what next-token training did to it, why duplication changed its odds, why
   scale changed them again, and where the ground is. When a step needs a number,
   attach it to this line's fate. A section that reaches for a fresh illustration
   to make a point the specimen could have carried has dropped the thread.

2. **Cash every comparison into literal mechanism.** The subject pulls hard
   toward "it's like a saved file," "like a lookup," "like remembering." Each
   such figure has to resolve, in the same passage, into what the system
   literally does: a specific sequence that gradient descent on next-token
   prediction drove the weights to reproduce. And each has to mark where the
   figure breaks, because the whole lesson turns on the ways this is not a file
   and not a lookup. An "it's like" left uncashed is cut.

3. **Make the invisible fact felt with real numbers.** The stored string cannot
   be seen; the extraction figures are the only window onto it. Give each figure
   a comparison the reader already holds, and tie it back to the specimen: how
   many sequences came out verbatim, at what duplication count, as what fraction
   of the whole. The reader should finish with a felt sense of how much text is
   sitting in there, not just the claim that some is.

4. **Show the mechanism working, not just its result.** Do not assert that
   duplication and scale drive memorization and move on. Make it visible: put
   what training does to a string it meets once beside what it does to the same
   string met thousands of times, and let the reader see the loss on that
   sequence pressed toward zero. The cause is more convincing shown at work than
   named.

One form note: when the specimen's exact characters are the point, the string
itself earns inline code, because the reader is meant to see it letter for
letter. The ordinary vocabulary of the lesson (weights, training, memorization)
stays in plain prose.

## Licenses

form: second person addressed to the reader's own query and its literal result
move: Willison and Ciechanowski anchor an abstraction to something the reader is
      doing right now, so the mechanism attaches to a concrete act instead of a
      general claim. Use it to keep the specimen in the reader's hands as the
      descent goes down.
bar:  the sentence names the reader's specific act or the exact thing that came
      back, and advances the mechanism by one step. A "you" that only warms the
      tone, or that addresses an imagined reader's reaction, is cut; the house
      ban on narrating a hypothetical reader still holds.

form: the corrective contrast (memorization is not X; the text is Y)
move: the required contribution is to separate memorization from retrieval and
      from hallucination. Each confusion is real, named, and load-bearing, so
      this lesson may run the contrast past the house one-or-two ceiling, but
      only for these live confusions.
bar:  each contrast pins both sides to the single mechanical difference, where
      the text lives: fixed in the weights, versus fetched from an outside store
      at query time, versus never real at all. It names the confusion it
      corrects. A contrast whose "not" clause is a foil the sentence invented is
      cut.

form: a plainly stated open question, left open
move: the series requires marking which ground is settled engineering and which
      is not. The exemplars commit hard where the mechanism is settled and say
      plainly where it is not, and that honesty is what earns the confident
      parts. Use it for the genuine unknowns: where memorization ends and
      generalization begins, how much a given deployed model holds.
bar:  the sentence marks a research question that is actually unresolved, and the
      lesson then leaves it unresolved, set apart from the settled claims around
      it. It is not a hedge laid over a claim the cited evidence supports, and
      not a question used to change the subject.

## Bartosz Ciechanowski, "Mechanical Watch"
Source: https://ciechanow.ski/mechanical-watch/
Craft:
- cadence: short declaratives set the anchor, longer clauses build the mechanism
  on top; the rhythm catches and releases like the thing being described.
- argument: problem-then-solution chaining, not a list. Each part is introduced
  as the answer to a failure the previous part left open, so the reader always
  knows why the next piece exists before it is named.
- evidence: the mechanism is the evidence. He shows a part doing its work and
  lets that do the arguing, rather than asserting what the part is for.
- stance: authority by accumulated detail, not pronouncement. Claims read as
  discovered; the modest framing ("this simple mechanism") undercuts rather than
  inflates.
- notice: he catches why a part exists when it looks unnecessary, and names the
  failure modes (what jams, what over-winds), which is where the real logic
  lives.
- diction: function first, name second. A part does its job, then gets its term,
  so the vocabulary arrives as recognition rather than jargon dropped in.
- reader: conspiratorial and hands-on ("if you look closely"), and explicit that
  the reader need not memorize the names, which lowers the cost of following.
- the important move the axes miss: the piece reassembles the object as it
  explains, each section mounting the next part onto the last, so understanding
  accumulates into a whole instead of a pile of facts. That cumulative build is
  the model for keeping one specimen alive across a descent.

## Simon Willison, "Embeddings"
Source: https://simonwillison.net/2023/Oct/23/embeddings/
Craft:
- cadence: stark opener, complexity admitted, then a way through. Sentences often
  start with a concrete action before the abstraction they illustrate arrives.
- argument: behavior first, mechanism second. He shows the thing working on a
  real case before any of the underlying idea is explained.
- evidence: one running example (his own site, with its real article count and
  the actual cost in cents) carries every later abstraction; numbers stay
  fastened to real files, real costs, real sizes.
- stance: unusually decisive for technical writing, and just as plain about the
  limits ("nobody fully understands what those individual numbers mean"), which
  is what makes the confident parts trustworthy.
- notice: he names the real constraint before the fix (the query was slow, so
  here is the table that made it fast), where a weaker writer jumps straight to
  the solution.
- diction: terms enter as problems being solved, then recur naturally; jargon is
  introduced only at the point the reader needs it, never front-loaded.
- reader: positioned as someone who wants to do this too; permission granted
  early to push through the jargon.
- the important move the axes miss: he keeps returning to the same example with
  fresh specifics each time rather than introducing new ones, so the reader's
  grip on the concrete case tightens as the ideas stack.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"
Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/
Craft:
- cadence: enthusiasm braked by method; pacing accelerates through the examples,
  mirroring how the reader's understanding builds.
- argument: phenomenon first ("how is that even possible?"), then the machinery,
  so the mechanism arrives as the answer to a curiosity the reader already feels.
- evidence: actual generated samples, not abstract math. The broken and
  half-right outputs are the proof, and the training progression (a sample at
  iteration 100 beside one at iteration 2000) makes the internal process
  visible.
- stance: commits to a strong claim, then plainly bounds it ("forget I said
  anything"), trusting the reader with the caveat instead of hiding it.
- notice: he shows the failures on purpose, because a mistake that reveals the
  mechanism's limits teaches more than a clean success.
- diction: technical terms arrive only after the need for them is established;
  each concept emerges from the problem it solves.
- reader: enthusiast-guide, not lecturer; invites the reader into shared
  discovery rather than handing down conclusions.
- the important move the axes miss: showing the messy middle. By displaying the
  model's output at several training stages he makes an invisible process legible
  as it happens, which is exactly how to render "the weights learned this string"
  without code.

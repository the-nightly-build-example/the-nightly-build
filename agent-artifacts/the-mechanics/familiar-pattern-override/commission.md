# Commission: the-mechanics/familiar-pattern-override

## The behaviour

Take a famous riddle everyone has seen — the surgeon riddle, the wolf-goat-cabbage
river crossing, the Monty Hall problem — change one detail so the answer is now
different (or trivial), and the model gives the classic answer anyway, confidently,
as if it never read your change. This is one of the most-shared "gotchas" about
chatbots, and The Mechanics has never explained the mechanism behind it.

CONFIRMED not previously published (checked against the full the-mechanics slug
list). It must be kept distinct from three published neighbours: irrelevant-context
(adds a true-but-useless sentence to a problem), memorization (verbatim text comes
out of the weights), and prompt-sensitivity (rephrasing changes the answer). This
behaviour is none of those: the premise of a memorized template is changed, and
the model reverts to the template's canonical answer. Link those lessons; do not
re-teach them.

## The angle

Work backward from the behaviour to its cause, step by step, marking settled vs.
open, no code.

1. The behaviour, shown concretely. One or two real, cited examples where a
   trivially-modified classic puzzle gets the canonical (now wrong) answer — drawn
   from the research record (e.g. the "Alice in Wonderland" / AIW simple-question
   collapse, a modified river-crossing or Monty Hall study), not invented. Report
   the measured drop.

2. First cause: a language model predicts the most probable continuation given the
   text so far, and the training data contains the canonical puzzle and its
   canonical solution thousands of times. Establish plainly: the model has a very
   strong prior — a high probability it assigns to the familiar answer before it
   has fully "used" your specific wording. Link the tokenization / next-token
   lessons rather than re-teaching them.

3. Second cause: why the change gets overridden. The altered detail is a small
   part of a prompt that otherwise matches the template almost exactly, so the
   overwhelming statistical pull is toward completing the pattern the model has
   seen. Distinguish sharply from irrelevant-context (there the problem is intact
   and a distractor is added; here the problem's answer has changed and the model
   ignores that). Note the role of surface similarity: the closer the prompt looks
   to the canonical version, the stronger the reversion.

4. Where the ground is. Settled: models complete high-probability familiar
   patterns, and a strong training prior can dominate a lightly-changed prompt.
   Open/disputed: what this proves about "reasoning" — whether it shows the model
   cannot reason or only that the prior wins under these conditions, and whether
   reasoning-trained models or prompting reduce it. Cite both sides (the "it can't
   reason" reading and the "it's a retrieval-vs-reasoning tradeoff that scale and
   RL partly fix" reading). Mark the boundary honestly.

Anchor fact to foreground: the model is not misreading your edited riddle so much
as being outvoted by every un-edited copy of it in the training data — which is
why the trick works best on the most famous puzzles and fades on obscure ones.

## Boundaries

- One behaviour, one mechanism (strong training prior overriding a changed
  premise). Do not drift into a general theory of LLM reasoning or into prompt
  engineering. Link, don't re-teach: irrelevant-context, memorization,
  prompt-sensitivity, in-context-learning, and the next-token/tokenization lessons.
- No code. One or two real worked examples ground it.

## Required contribution

The reader should finish able to explain why a lightly-changed famous puzzle gets
the canonical wrong answer (a strong memorized prior over the literal prompt), why
the effect is strongest for the most famous puzzles, and how to tell this failure
apart from added-distractor failures. They should be able to judge a "the model
can't reason" claim built on one of these gotchas.

## Source and production policy

- Sourcing floor (nb source-policy): minimum 8 sources, at least 4 primary, at
  least 1 secondary. Primary = the papers that own each demonstration (e.g. the
  AIW paper; a modified-classic-problem study; a memorization/prior study) and any
  primary arguing the reasoning interpretation each way.
- Production policy (balanced, no `required` directive): editorial roles run on a
  capable model (Claude Sonnet class) in isolated subagents; effort follows policy
  (coach low, researcher high, writer medium, editor high). No directive traded down.

## Recent-pattern notes (habits not to inherit)

- Opener habit: "By the end you will know..." triad; temporal-generic opening.
  Break it.
- Takeaway habit: two-part balance closers. End on this lesson's own point.
- Heading habits over-used across The Mechanics: "A word problem the model solves
  until you change it", "Nothing tells the model which words to ignore", "The floor
  beneath the failure" / a stock ground-hitting final heading, "Where this leaves
  the reasoning question" / "The honest edge of the explanation" (a
  reasoning-boundary closer recurs — do not reuse its shape). The desk requires
  marking the open question, but give that section a heading in this behaviour's
  own nouns. Vary construction; do not default to nb-holdsup.
- Dek habit: comma-triad / comma-splice deks (`spec/headlines.md` bans the triad).

## Neighbouring articles in tonight's edition

- the-evidence/flamingo (the 2022 few-shot multimodal paper)
- the-instruments/brier-score (how the Brier forecasting score is made)
- what-could-go-wrong/companion-dependency (the AI-companion-harm argument)
- when-ai-breaks/predpol-predictive-policing (the PredPol/Geolitica failure)
No overlap. This is tonight's "how does it actually do that" lesson.

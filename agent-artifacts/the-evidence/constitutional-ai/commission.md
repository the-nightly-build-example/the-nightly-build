# Commission: the-evidence/constitutional-ai

## The document

Bai et al., "Constitutional AI: Harmlessness from AI Feedback," Anthropic,
December 2022 (arXiv 2212.08073). The lesson reads this one paper. State what it
is, who wrote it, and why it became a document people cite when they argue about
how AI systems are made safe.

The paper's fame rests on one claim: a model can be trained to refuse harmful
requests using feedback from another AI model guided by a short written set of
principles, instead of the large pool of human harm labels that the standard
method needs. The short written set is the "constitution." The method that
learns from AI-generated preference labels is reinforcement learning from AI
feedback (RLAIF), the paper's counterpart to reinforcement learning from human
feedback (RLHF).

## What the lesson must do

Walk the reader through what the paper actually did, in the paper's own numbers,
and show the size of the foundation under the famous claim.

- The two stages, concretely. Stage one: a helpful-only model is shown its own
  harmful answers, asked to critique them against a principle drawn at random
  from the constitution, and asked to revise; the revised answers fine-tune a new
  model (supervised learning). Stage two: that model generates pairs of answers,
  a separate model picks the more harmless one using the constitution, and those
  AI-made preference labels train a preference model that drives reinforcement
  learning (RLAIF). Name each part and what it does.
- The constitution itself: how many principles, where they were drawn from, that
  they were written by the authors. Show one or two real principles verbatim so
  the reader sees what "a principle" is, and how little text is doing the work.
- The scale, honestly. What model sizes, what evaluation (crowdworker preference
  comparisons reported as Elo, red-team probing), what the harmlessness/helpful-
  ness result actually was and how it was measured. This is one lab's models,
  evaluated mostly by preference comparison, on harmlessness. Say that plainly.

Then bring it to the present. RLAIF and "constitution" are now common terms.
Later work tested whether AI feedback matches human feedback (e.g. Lee et al.,
"RLAIF vs. RLHF," Google, 2023) and Anthropic ran a public "Collective
Constitutional AI" experiment. Say what held, what is contested (does harmless-
ness feedback generalize; is a written constitution doing the work or is it the
base model), and where today's loose talk of models "having a constitution"
outruns what the 2022 paper showed.

## Required contribution

The reader should finish able to explain what "AI feedback" and a model
"constitution" mean mechanically, and able to size the evidence: preference
modeling on one lab's models, aimed at harmlessness, not a governance mechanism
and not a proof that AI feedback equals human judgment in general. That sizing is
the article's work on the evidence; the paper reports its results but does not
frame its own limits for a newcomer.

## Boundaries and continuity

- RLHF, preference models, and reward models are taught ground. The library has
  the-evidence/direct-preference-optimization, the-evidence/instructgpt, and
  the-evidence/deep-rl-from-human-preferences. Link the earlier lesson in the
  Background band at first use rather than re-teaching RLHF from scratch.
- One document only. Do not turn this into a survey of alignment methods.
- Discuss Anthropic and Google as authors of documents, reported as fact. Do not
  cite any company as an authority on whether the method is good.

## This run's neighbors

Four other lessons publish tonight, each on a different desk and subject
(the-instruments/superglue, the-mechanics/counting-objects-in-images,
what-could-go-wrong/open-weights-release, when-ai-breaks/bard-jwst-demo). No
topical overlap; no shared claim to coordinate. This piece should read as one
desk's lesson among five.

## Source policy

Series/template floor: at least 6 sources, at least 3 primary, at least 1
secondary. Prefer the paper and other primary documents. Candidate primaries: the
CAI paper (2212.08073); Anthropic's published constitution / Collective
Constitutional AI writeup; the companion Anthropic paper "Training a Helpful and
Harmless Assistant with RLHF" (2204.05862) for the RLHF baseline it builds on;
Lee et al., "RLAIF" (2309.00267). The researcher confirms kind and count.

## Production policy (recorded)

profile balanced. writing-coach effort low, researcher effort high, writer
effort medium, editor effort high. Model "capable" for every role, none marked
required; roles run on this harness's default capable model. Record the actual
model each role reports in its handoff.

## Recent patterns to break (habits, not rules)

From the recent library across desks:

- Deks lean on a two-clause construction joined by ", and" that lands a reversal
  or twist (segment-anything, toxicity-score, gradient-hacking, galactica). One
  recent dek is a comma triad (adversarial-examples), a mold spec/headlines.md
  bans outright. Build this dek some other way.
- Headlines default to a negative-fact reveal ("never counts the fingers it
  draws," "returns a mask and never a name") or a trailing second clause
  ("..., and its public demo lasted about two days"). Reach for those only if the
  story is genuinely that shape.
- Every lesson ends its body on a present-day section, which the series prompt
  requires. The heading for it keeps arriving as "Where X still Y." Vary how the
  closing heading is built.

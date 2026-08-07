# Voice guide: the-mechanics/thinking-out-loud (01)

Write in the plainest explanatory voice the house already asks for, but run it at
two clearly different confidence settings and never let them blur. This lesson
rests on two claims that are not the same kind of claim. One is proven: a
transformer spends a fixed, bounded amount of computation per token, so more
serial work needs more tokens. One is open: whether the written steps are the
computation or a story told beside it. The default register would state both in
the same even, plain-confident tone. Here the reader must be able to hear, from
the verb alone, whether a sentence reports something proven, something observed,
or something nobody knows. Keep that seam audible from the first claim to the
last.

Address a curious peer who has already watched the behavior happen and wants the
machinery, not a verdict handed down. Build the mechanism so the reader can
rebuild it: walk one real part at a time, and where a worked case can show the
mechanism doing its work, let the reader watch the answer change rather than be
told it changes. Correct the one folk explanation a real reader actually holds,
once, cleanly, then move on. When you reach the open question, hold it open on
purpose; the openness is part of what this lesson teaches, not a loose end to be
tidied.

## Licenses

form: calibrated confidence, with the proven and the unknown in different lights
move: Olah writes "In theory, RNNs are absolutely capable... Sadly, in practice,
  RNNs don't seem to be able to" — flat about the theorem, plain about the
  empirical gap, no hedging smeared across the seam between them. He pins the
  open part to the literature so it reads as a real problem, not his own
  confusion.
bar:  a sentence stating the bounded-compute fact and a sentence about the
  faithfulness question must not read at the same strength. From the verb and
  the claim alone, the reader can tell which of proven / observed / unknown they
  are standing on. A hedge on a proven claim, or false steadiness on an open one,
  fails.

form: one earned correction of the plausible-wrong folk explanation
move: the standard bans the "not X but Y" reflex except where the misconception
  is real and named. The belief that the model "reasons like a person once told
  to" is a real belief a smart reader arrives with, and dislodging it is the
  lesson's hinge.
bar:  the "not" clause names the actual folk belief, stated so its holder would
  recognize it, never a strawman built to be knocked down. Used at most once in
  the piece. Everywhere else, assert the mechanism directly instead of defining
  it against a foil.

form: the demonstrative worked example — the mechanism performed, not illustrated
move: Karpathy shows the raw generated output and lets the reader judge how the
  thing works from what it produces; Olah's linguistic case is the explanation
  rather than a decoration on it. The example carries the claim's weight.
bar:  the worked case must show the mechanism at work — the problem that a single
  token's compute cannot finish, then finishing when the steps are written out
  where the model reads them back. The reader watches the answer turn. An example
  that merely restates, in numbers, a point already made in prose fails.

form: the question held open
move: Karpathy states a claim he cannot stand behind and withdraws it in the
  open ("forget I said anything") rather than dressing a guess as a finding.
  Naming a limit costs him no authority.
bar:  where the piece marks the faithfulness question open, it says what would
  settle it and why that has not happened, and smuggles in no lean toward an
  answer. If the sentence could be deleted and the reader still couldn't tell the
  question was unresolved, it has not done the work.

form: second person to invoke the shared behavior
move: Evans starts from the reader's own felt experience of the confusing thing
  and treats that experience as legitimate data, not a warm-up.
bar:  second person only to name a behavior the reader has actually seen a model
  do. Never "you might wonder" or "you may recall" as throat-clearing. If the
  sentence does not point at something the reader has watched happen, cut the
  address.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"
Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/
Craft:
- cadence: short declaratives that assert, then a longer sentence that grounds
  the assertion in a case; a claim-then-example heartbeat, length varied to keep
  the reader from fatigue.
- argument: layered escalation — why the thing matters, what it does, how well it
  does it — with each stage climbing from a toy (a four-letter vocabulary) to the
  real (Wikipedia, then Linux source).
- evidence: raw generated output shown and left for the reader to judge; exact
  figures ("approx. 3.5 million parameters"); the math set beside the mechanism
  it describes.
- stance: confident where earned ("I believe they will become..."), frank about
  scope ("I won't go into details"), and willing to withdraw a claim in the open
  rather than defend it past its evidence.
- notice: failure modes shown next to successes (a model opens a proof and closes
  a lemma); the order in which competence emerges — spaces first, then short
  words, then long-range structure.
- diction: correct technical terms wrapped in immediate plain translation;
  metaphor used as a handle ("working memory"), not ornament.
- reader: trusted to judge the raw evidence directly instead of being handed the
  conclusion drawn from it.
- the important move: generative output as proof of understanding. He shows what
  the mechanism produces and lets the reader infer how it works, so the failures
  teach more than any success metric would.

## Julia Evans, "Why is DNS still hard to learn?"
Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/
Craft:
- cadence: short landing sentences among longer exploratory ones, with questions
  as hinges ("So what's going on?"); casual but controlled, never sloppy.
- argument: takes an amorphous "this is hard" and breaks it into discrete, named
  parts, then moves from the felt experience of the difficulty toward its
  underlying cause.
- evidence: real terminal output rather than paraphrase; the specific trap
  narrated concretely, so the gotcha is felt and not just asserted.
- stance: admits genuine bewilderment without self-deprecation ("it took me
  probably 5 years to realize"), and validates the reader's confusion as
  legitimate rather than a failing.
- notice: the interface layer — what tools hide, what spacing misleads, what
  smart people keep having to rediscover.
- diction: casual markers sit beside precise technical terms with no dumbing
  down; the reader is assumed able to hold both registers.
- reader: addressed as a fellow struggler working the problem alongside her, not
  a novice receiving answers.
- the important move: confusion treated as data. She asks why smart people stay
  confused rather than only what they should know, and that inversion makes the
  diagnosis credible and the explanation land where the difficulty actually is.

## Christopher Olah, "Understanding LSTM Networks"
Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
Craft:
- cadence: short declaratives and the occasional fragment as a conceptual anchor
  ("Your thoughts have persistence"), each followed by expansion into the
  mechanism.
- argument: ruthlessly linear. Problem before solution, what the parts do before
  what each does in sequence, notation introduced before it is used; no forward
  references and no assumed step.
- evidence: worked linguistic cases (predicting the obvious next word versus
  recovering a fact across a long gap) where the example is the explanation, not
  a gloss on it.
- stance: marks the empirical mystery plainly ("in practice, RNNs don't seem to
  be able to") and attributes it to the literature, so an open problem reads as
  the field's, not the writer's own gap.
- notice: why over how-much — each part's purpose, what information it protects
  or lets through, rather than its arithmetic.
- diction: conversational and precise at once; technical terms placed without
  ceremony, each doing one job.
- reader: walked through the construction so they reassemble the mechanism
  themselves rather than receive it whole.
- the important move: unfold, then refold. He expands the mechanism into its
  separate parts, then collapses it back into the compact whole, so the reader
  experiences the thing emerging instead of being shown the finished diagram.

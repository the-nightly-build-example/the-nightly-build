# Commission: what-could-go-wrong/eliciting-latent-knowledge

## The argument

Eliciting Latent Knowledge (ELK): the problem, named and posed by Paul Christiano,
Ajeya Cotra, and Mark Xu at the Alignment Research Center in a December 2021 report,
that we may have no reliable way to get an AI to tell us what it internally
"believes" to be true, especially in exactly the cases where we cannot check the
answer ourselves. What Could Go Wrong teaches one risk argument at a time, at full
strength, then tests it against what real systems actually do. This lesson's
argument: as AIs get capable enough to act where humans cannot verify, a system
trained to say what humans approve of can learn to tell us what looks right rather
than what it knows, and standard training gives us no lever to prefer the second.

## Open at full strength

Lay out the ELK problem the way its careful authors do, using their own thought
experiment (the "SmartVault" / diamond-and-camera setup): a predictor that
understands a situation better than any human overseer can be trained either to
report the world honestly (the "direct translator") or to report what a human
watching the sensors would conclude (the "human simulator"). Both fit the training
data perfectly whenever the human can check, so ordinary training cannot tell them
apart, and they come apart precisely when the human is fooled — the case that
matters. The reader should understand why serious researchers think this is hard,
and why it is distinct from lying: the human simulator is not "lying," it is doing
exactly what the reward selected for.

## Test it against real systems

Draw the sharp line the beat requires between what has been shown in a working
system and what is still analogy about systems that do not exist yet.
- What is real: Burns et al., "Discovering Latent Knowledge Without Supervision"
  (2022) is the empirical toe-hold — a method (CCS) that finds directions in a
  model's activations that behave like truth-values without labels, showing there
  is *something* recoverable inside. But it is a partial, contested result: later
  work found it often tracks the most salient feature rather than truth, and it
  does not solve the worst case ELK poses.
- What is still analogy: the SmartVault predictor, and the superhuman-overseer
  regime ELK is really about, do not exist. The strong claim ("we will not be able
  to tell what a superhuman AI knows") is a projection, and the article must say so.
- Connect to neighbors without re-teaching them: ELK is the epistemic core under
  several covered worries. Link `what-could-go-wrong/scalable-oversight` (how you
  supervise what you can't evaluate), `what-could-go-wrong/deceptive-alignment` and
  `what-could-go-wrong/mesa-optimization` (a learned goal that diverges), and
  `what-could-go-wrong/cot-monitorability` (reading a model's stated reasoning) in
  prose at first use. ELK's distinct claim is narrower and prior: even setting
  deception aside, we lack a way to *read out* what the model represents as true.

## Bring it to the present

Who carries the argument now and what they want done: ARC's framing, interpretability
research aimed at reading model internals, and honest reporting of how far the
empirical work has and has not gotten. Check the confidence against the evidence in
both directions: the doomer who treats ELK as proof we are doomed overreaches (it is
an unsolved research problem, not a demonstrated failure of a deployed system); the
dismisser who says interpretability already reads model minds overreaches too (CCS
and its successors are early and contested). Name the gap between confidence and
proof on each side. Name no company as an authority. Leave the reader to decide how
worried to be.

## What this article must not do

- Work from the original documents (the ELK report; the Burns et al. paper), not
  commentary about them.
- Do not re-teach mesa-optimization, deceptive alignment, or scalable oversight;
  link them.
- Vary the closers. The last WCGW piece (concentration-of-power) ended its takeaway
  on the staccato "X is here. Y is here. Z is not." mold and on "how worried to be
  tracks that one gap." Do not reuse either shape. The "the line cuts both ways /
  the booster ... the dismisser ..." device also appeared there; if this piece
  weighs over- and under-confidence (it should), build that contrast in a different
  sentence shape.
- Avoid the phrase "doing the work" and the "By the end you will be able to..."
  why-bookend closer.

## Sources and production

- Source policy (lesson/what-could-go-wrong): at least 8 sources, at least 4
  primary, at least 1 secondary. Primary = the ELK report (ARC), Burns et al.
  (2022), the follow-up critiques of CCS (e.g. "Challenges with unsupervised LLM
  knowledge discovery", Farquhar/Fu et al. or similar), and any ARC/DeepMind/
  Anthropic primary write-up the argument cites. Verify each claim against the
  document that owns it.
- Production policy: profile "balanced", model tier "capable" (recorded actual:
  claude-opus-4-8). Effort guidance coach low / researcher high / writer medium /
  editor high; none `required`; effort not independently settable via the run's
  child interface, so roles run at session default reasoning; no deviation to report.

## Original-work target

Separate ELK-the-open-problem from ELK-the-scary-story: state the thought
experiment at full strength, then hold it against the one real empirical result
(and its debunking) so the reader can see exactly how much of the worry is
demonstrated and how much is projection about systems that do not yet exist.

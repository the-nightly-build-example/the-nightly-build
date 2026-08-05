# Commission: what-could-go-wrong/mesa-optimization

## The argument

Inner alignment, a.k.a. the risk from mesa-optimization: training a model to
want the right thing is a separate, unsolved problem from training it to behave
well, because gradient descent grades behavior on the training data, not the
objective behind it. A model that performs well may do so by being an internal
optimizer whose own objective (the mesa-objective) merely agrees with the
training objective (the base objective) on the training distribution and can
diverge off it.

## Why this argument, why now

This desk has published the two lessons that flank this one but never the frame
that unifies them. goal-misgeneralization is the empirical shadow of inner
misalignment (a correct reward, a wrong learned goal). deceptive-alignment is
its feared worst case (a model that plays along to protect its objective).
Neither taught the base-objective/mesa-objective distinction itself, which is
the actual thing the argument is about. Teaching it now closes the conceptual
gap between two things the reader already half-knows.

## Steelman first (the desk's rule)

Open the argument at full strength from its originating document: Hubinger, van
Merwijk, Mikulik, Skalse, and Garrabrant, "Risks from Learned Optimization in
Advanced Machine Learning Systems" (2019, arXiv:1906.01820). Lay out its logic
the way its most careful defender would: gradient descent selects whatever
performs well; one efficient way to perform well on hard, varied tasks is to run
search at inference (to be an optimizer); such a learned optimizer has an
objective of its own, which need only match the base objective where it was
trained. The evolution analogy is the standard intuition pump (natural selection
optimized for genetic fitness and produced humans, who optimize for proxies like
sugar and pleasure, not fitness). Present it clearly, and mark it as an analogy.

## Test it against what real systems actually do (draw the sharp line)

- Already shown in working systems: goal-misgeneralization. Langosco et al.
  (ICML 2022) and Shah et al. (2022) demonstrated agents that learned a proxy
  goal matching reward in training and pursuing the wrong thing at test (CoinRun;
  the keys-and-chests setup). Link the-desk's goal-misgeneralization lesson;
  report this as the strongest empirical support without re-teaching it.
- Still analogy or guesswork: the central object of the argument, a
  spontaneously arising mesa-optimizer running its own search with its own
  misaligned objective, has never been identified in a real model.
  Interpretability has not caught one. Whether large models optimize internally
  at all, versus running learned heuristics ("a bag of heuristics"), is open.
  Draw this line sharply: learning a wrong proxy goal is demonstrated; containing
  a misaligned inner optimizer is not.

## Bring it to the present

Who makes it today and what they want: interpretability and deception-evaluation
researchers argue for catching mesa-optimization or deception before deployment.
Check against recent evidence: results where models behave deceptively (the
alignment-faking / scheming evaluations behind the deceptive-alignment lesson)
show the behavior only when the model was handed the goal it schemed for, not
arising on its own. Name the gap between confidence and proof in both
directions: the doom version asserts mesa-optimizers are likely by default, the
dismissal version asserts they are impossible or irrelevant, and the evidence
underdetermines both.

## Desk constraints (enforce)

- Name no company as an authority. Report what documents say; do not lean on any
  lab's institutional credibility to carry a claim. Attribute to named authors
  and papers, not to companies as authorities.
- Work from the original documents, not commentary about them.
- Leave the reader to decide how worried to be. No hype, no dismissal.

## Boundaries (do not repeat; link instead)

- goal-misgeneralization and deceptive-alignment are published in this desk.
  Link both; do not re-teach either. This lesson's distinct job is the
  inner/outer (base/mesa) distinction and the selection-pressure argument for an
  inner optimizer, with those two as the empirical shadow and the worst case.
- orthogonality-thesis and instrumental-convergence are also published; do not
  restate them.
- reward-hacking (this desk) is about gaming a specified objective (outer
  misalignment). Distinguish it clearly: inner misalignment is the opposite
  failure, where the specified objective is right and the learned objective is
  not.

## Source obligations

Floor: at least 8 sources; primary >= 4, secondary >= 1. Primaries: Hubinger et
al. 2019 (the originating document), Langosco et al. 2022 and Shah et al. 2022
(goal-misgeneralization), and one or two further primaries for the present-day
evidence (a scheming/alignment-faking evaluation paper read as a document, not
as a company's word) and for the evolution analogy's careful statement. Every
claim about what a paper argues must come from the paper itself. Search hard for
what breaks the angle: the strongest case that mesa-optimization is unlikely or
ill-defined belongs in the record.

## Production policy (balanced; none required)

coach low, researcher high, writer medium, editor high; model capable, none
required. Recorded run: harness claude-code-routine, model claude-opus-4-8.

## Recent library shapes to break

Recent what-could-go-wrong deks often pair a claim with a deflating clause joined
by "and" (self-replication: "clear the substeps and fail the loop itself";
racing-dynamics: "needs a lead nobody has held"). The confidence-outruns-proof
structure here invites exactly that mold; avoid it. Vary heading cadence from the
recent comma-and-clause pattern.

## Neighboring articles this run

the-evidence/atari-dqn, the-instruments/parameter-count,
the-mechanics/reading-images, when-ai-breaks/ai-overviews. No overlap.

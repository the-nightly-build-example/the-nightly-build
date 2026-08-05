# Commission: the-instruments/parameter-count

## The number

The parameter count: "N billion parameters." The single most-quoted number in
public AI, and one of the least comparable across systems. This lesson teaches
how the number is produced, what it can and cannot support, and the real case
where treating it as comparable misled people.

## Why this number, why now

Every reader has met "175 billion parameters" or "a 70B model" and has no idea
what is being counted or whether two such numbers can be compared. Mixture-of-
Experts models (DeepSeek-V3, Mixtral, Llama 4, and the frontier generally) have
made the number actively misleading: the headline total is no longer what runs
on a given token. The desk has taught training-compute already; parameter count
is the other half of "how big is this model," and it is the more abused one.

## The angle (desk signature: where a number comes from, and where it misled)

The parameter count is fixed by literally counting the network's learnable
weights, it is set at training and never changes at inference, and by itself it
predicts neither capability nor cost. Chinchilla already showed a smaller model
beating a larger one at equal compute, so "more parameters = better" was false
even for dense models. Mixture of Experts then broke the comparison outright: a
model can advertise a huge total while activating a small fraction per token.

Thesis for the writer to prove: the parameter count measures the size of the
weight stack, not how good the model is or how much of it runs, and under
Mixture of Experts the advertised total and the active count are different
numbers that marketing and headlines routinely conflate.

## What this lesson teaches (2-3 ideas)

1. What a parameter is and how you count it: one learnable weight, a number the
   model multiplies into an activation, frozen after training. For a dense
   transformer the count is dominated by the weight matrices (attention and MLP
   blocks) plus the embedding table. Give the reader a concrete anchor: GPT-3 at
   175B, and a plain sense that the count scales with layers x width-squared.
   Do not derive the full formula; give the intuition and one real number.
2. Why the count does not equal capability or cost: link the-evidence/chinchilla
   (a ~70B model trained on more data beat a ~280B model at equal compute). Data
   and training budget move quality as much as parameter count does. State the
   real relationship to compute plainly and link the-instruments/training-compute
   rather than re-deriving C = 6ND.
3. Mixture of Experts and the total-vs-active split: an MoE routes each token to
   a few of many "expert" sub-networks, so only a fraction of parameters
   activate per token. Worked example with verified figures: Mixtral 8x7B is
   about 46.7B total but about 12.9B active per token (and NOT 56B, because the
   attention layers are shared, which is the arithmetic error people make);
   DeepSeek-V3 is about 671B total and about 37B active. The real misleading
   case: quoting an MoE total as if comparable to a dense model's parameters, on
   cost or on capability.

## The required "where the number misled" case

Center it on MoE total-vs-active: the "8x7B = 56B" miscount and, more
consequentially, cross-comparisons that put an MoE's total parameter count
beside a dense model's to imply comparable size, cost, or capability. Confirm
the specific figures from the primaries that own them.

## Boundaries (do not repeat; link instead)

- training-compute (this desk) owns the FLOP story. Link it; do not re-teach.
- chinchilla (the-evidence) owns the scaling result. Link it; do not re-teach.
- Do not turn this into a Mixture-of-Experts mechanics lesson. Teach only as
  much MoE as the number requires (routing exists, few experts fire per token).
  The mechanics desk can own MoE later.

## Source obligations

Floor: at least 8 sources; primary >= 4, secondary >= 1. Primaries that own the
figures: the GPT-3 paper (175B), the Mixtral paper (Jiang et al. 2024:
46.7B total / 12.9B active), the DeepSeek-V3 technical report (671B / 37B), the
Chinchilla paper (Hoffmann et al. 2022), and a Mixture-of-Experts primary
(Switch Transformer, Fedus et al. 2021, or Shazeer et al. 2017) for the
sparsity definition. Every headline parameter figure must be read off the model's
own paper or card, not a leaderboard or blog. Secondary reporting for context
only.

## Production policy (balanced; none required)

coach low, researcher high, writer medium, editor high; model capable, none
required. Recorded run: harness claude-code-routine, model claude-opus-4-8.

## Recent library shapes to break

Recent the-instruments deks lean hard on the "same X, two numbers" reversal
(tokens-per-second: "both are true"; energy-per-query: "0.3 by one measure and
2.9 by another"; arc-agi: "scored X and Y, and only the compute changed"). The
total-vs-active split is genuinely a two-number story, so take special care NOT
to reuse that dek mold. Find a different line. Vary heading cadence from the
recent comma-and-clause pattern.

## Neighboring articles this run

the-evidence/atari-dqn, the-mechanics/reading-images,
what-could-go-wrong/mesa-optimization, when-ai-breaks/ai-overviews. No overlap.

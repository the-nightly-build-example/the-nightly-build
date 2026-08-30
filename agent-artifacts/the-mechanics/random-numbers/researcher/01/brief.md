# researcher brief: the-mechanics/random-numbers (01)

Inputs:
- editorial-direction.md (house standard, citation rule, the reader, The
  Mechanics series prompt)
- this brief

Output: researcher/01/evidence.md

## Subject
The behavior: large language models asked to pick a random number return a
strongly non-uniform distribution, over-picking specific values (7 for 1-10;
37, 73, and a few others for 1-100). The lesson works backward from this to the
mechanism. Your job is to source both the behavior (measured) and the mechanism.

## Questions the evidence record must answer
1. The behavior, measured: find studies, papers, or documented experiments that
   actually measured how one or more named models distribute their answers when
   asked for a random number in a stated range. Record the exact model, the
   prompt, the range, the sample size, and the resulting distribution or the
   modal value's frequency. Real numbers, with owners. This is the highest
   priority and the likeliest thin spot — report early if measured LLM
   distributions cannot be sourced to the floor.
2. The human baseline: the psychology literature on human number preference
   (people asked to pick 1-10 over-choose 7; the "pick a number" biases). Cite
   the studies that own these figures. This is what the model's training text is
   full of.
3. The mechanism, sourced: that a language model produces a probability
   distribution over next tokens and a sampler draws from it, with no random
   number generator involved. Anchor this in the model/decoding documentation or
   primary descriptions already used by the library's mechanics lessons (do not
   re-derive; the evidence just needs to support the plain statements the lesson
   makes).
4. Why temperature does not fix it: sourced support that raising temperature
   flattens but does not uniformize a learned distribution, and that at
   temperature 0 the model is deterministic (returns the mode). Keep this
   distinct from the separate questions of run-to-run nondeterminism.
5. The real fix: that giving the model a tool (code execution / a real RNG)
   produces genuine randomness, and how current systems do this. Source it.
6. Settled vs open: what is settled engineering here and what is genuinely open
   (e.g. the precise cause of specific favorites, how instruction tuning shifts
   them). Record honestly.
7. Contradictions / limits: any evidence that some models DO approach uniform,
   or that behavior differs sharply by model or prompt. Record in full.

## Source policy for this article
At least 8 sources; at least 4 primary, at least 1 secondary. Primaries:
measured-experiment sources (papers or firsthand documented measurements) and
the human-number-preference psychology studies. A blog counts as primary only
for data it measured itself. Classify each and say why.

## Source assets
Name any exact visual worth using (e.g. a published histogram of an LLM's answer
distribution, with its source), in the evidence asset shape. If a clean measured
series exists, preserve the full series so a chart can be built from it. No crop
coordinates.

## Focus / risk
The article's original work is separating "output varies" from "the choice is
biased." The evidence must let the writer show the bias with measured numbers,
not just assert it. If the measured-distribution evidence is thin, say so plainly
and record exactly what is and is not established.

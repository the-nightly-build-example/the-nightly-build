# Commission: the-mechanics/hedging

## Assignment

Start from a behavior every assistant user has seen: ask a chatbot for a
straight answer on a question that has one, and it returns "it depends," a
both-sides summary, and no commitment. Work backward to what produces that
non-commitment, step by step, down to ground. No code.

Template: lesson. Series: The Mechanics (how does it actually do that). Reader:
smart, widely read, new to this subject. Publication date: 2026-09-14.

## The behavior and the cause chain

The observed behavior: the model withholds a stance it is capable of taking,
defaulting to balanced, qualified, non-committal output even when the user asked
for a call and the question admits one. Trace it:

1. The base model completes text toward the register most common in its training
   data for contested or advice-shaped questions, which is hedged, balanced
   prose. Show this as a next-token pull, with a concrete example.
2. Post-training (RLHF and the reward model) rewards responses that raters
   prefer, and raters penalize confident answers that could be wrong or could
   offend, so the optimum drifts toward hedging. Tie to the reward model as
   taught; give a concrete instance of the pressure.
3. Safety and helpfulness tuning add explicit non-commitment on sensitive or
   contested topics. Name where this is deliberate design and where it is a
   side effect that overshoots onto questions that are not sensitive at all.

Mark clearly which steps are settled (base-rate completion, reward-model
optimization toward rater preferences) and which are open or contested (exactly
how much each stage contributes; whether a given hedge is deliberate policy or
overshoot). End at ground: a step below which nothing would change the answer.

## Boundaries and dedupe

- This is not sycophancy. `the-mechanics/sycophancy` owns the behavior where the
  model reverses a correct answer when the user pushes back. Hedging is the
  refusal to commit in the first place, independent of user pressure. Draw that
  line explicitly and link sycophancy in Background.
- Not over-refusal (`the-mechanics/over-refusal`), which declines the task
  outright; here the model answers but will not commit.
- Not politeness-and-pressure (`the-mechanics/politeness-and-pressure`), which is
  about wording changing the answer. Link where the reader might conflate them.
- The reward model / RLHF mechanism is taught in the library (InstructGPT in The
  Evidence, sycophancy in The Mechanics). Link, do not re-derive RLHF from
  scratch.

## Neighbors in tonight's edition

`when-ai-breaks/gpt-4o-sycophancy` covers a shipped over-validation regression.
That is the opposite failure of post-training tuning (too agreeable) from this
one (too non-committal). Do not overlap: this lesson explains the general
hedging mechanism; it does not narrate that incident. A Background link is
optional, not required.

## Sources

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. URLs must
resolve. Primaries to draw on: the InstructGPT/RLHF paper and reward-model
literature; work measuring calibration/hedging or over-conservatism in tuned
models; any primary study or model-card/system-card text documenting deliberate
non-commitment on contested topics; papers on reward-model over-optimization.
Every quantitative claim (how often, how much) needs a primary that measured it;
if a step is mechanism the reader can verify by reasoning rather than a measured
number, present it as such and do not attach a false citation.

## Production policy (balanced profile; none required)

- researcher: effort high, model claude-opus-4-8
- writing-coach: effort low, model claude-sonnet-4-5
- writer: effort medium, model claude-opus-4-8
- editor: effort high, model claude-opus-4-8

## Recent shapes to break (do not inherit)

Recent Mechanics titles state the behavior as a small finding (Whisper answers
silence with a sentence no one spoke; Ask DeepSeek's model who made it and it
says OpenAI). Strong, but now a pattern. Find this piece's own title and dek.
Vary heading construction from the recent run; avoid two clauses joined by a
comma and "and."

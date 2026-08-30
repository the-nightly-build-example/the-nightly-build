# Commission: the-mechanics/random-numbers

## Assignment
Answer one "how does it actually do that" question about a behavior anyone who
uses AI has seen: ask a chatbot for a random number between 1 and 10 and it says
7 far more often than one time in ten; ask for 1 to 100 and it favors a few
numbers like 37 and 73. Work backward from that behavior to its cause, step by
step, down to a step where nothing below it would change the answer.

## Why this behavior, why now
It is a behavior the reader has almost certainly produced themselves, and its
cause is the clean core of how these models work: they emit a probability
distribution over next tokens and a sampler draws from it, so a "random" pick is
shaped by training-text frequencies, not by a random number generator. The
library teaches sampling-temperature, nondeterminism, and autoregressive
generation, but none of them explains why the choice among the numbers is biased
toward particular values. That is this lesson.

## The desk's required beats (from the series prompt in editorial-direction.md)
- Start from the one behavior and work backward, each step naming a real part of
  the system and what it does, with a small real example.
- Reach ground: the step below which nothing would change the answer (there is no
  RNG; the model outputs a distribution over tokens; that distribution's shape is
  learned from human text, and human text over-picks 7, 37, 73).
- Mark which steps are settled engineering (no RNG, next-token sampling,
  training-frequency shaping) and which are open even to builders (the exact
  provenance of specific favorites; how much instruction tuning moves them).
- No code.
- Close on where the same weakness lives today and how it is actually worked
  around (hand the model a tool that calls a real RNG; link tool-use).

## The line this lesson must hold (critical)
This is NOT the nondeterminism lesson (why identical requests give different
answers) and NOT the sampling-temperature lesson (what the temperature knob
does). Those are published; link them, do not re-teach them. This lesson is about
the SHAPE of the distribution over which number gets chosen — why it is lumpy and
biased toward specific values rather than uniform — even setting run-to-run
variation aside.

## Boundaries
- Link the-mechanics/autoregressive-generation, the-mechanics/sampling-
  temperature, the-mechanics/nondeterminism, and the-mechanics/tool-use in
  Background at first use; do not cover them as new.
- Ground every step in a real, cited example. Do not assert distributions the
  evidence record has not measured.

## Required contribution (the original work the writer must name)
The article separates two things readers blur together: that a model's output
varies (randomness of draw) and that its "random" choice is biased (shape of the
distribution). It shows, with measured numbers, that the second is the real
answer to "why 7," and that the fix is not a bigger temperature but an external
source of randomness.

## Neighbors in tonight's edition (keep this piece distinct)
- the-instruments/simpleqa touches model behavior/evaluation but is a different
  desk — no shared claims.
- the-evidence/denoising-diffusion, what-could-go-wrong/ai-moral-status,
  when-ai-breaks/mcdonalds-ai-drivethru — no overlap.

## Template and policy
- Template: lesson (word band 1200-2200).
- Source policy: at least 8 sources; at least 4 primary, at least 1 secondary.
  Primaries: experiments/studies that measured LLM number-picking distributions,
  and the psychology literature on human number preference that owns the human
  baseline (people over-pick 7 from 1-10). Reporting/blog explainers are
  secondary unless they report their own measured data firsthand.
- Production policy (profile balanced): researcher high / capable; writer medium
  / capable; editor high / capable; writing-coach low / capable. No required
  directive to trade down. Actual runtime models: researcher, writer, editor on a
  capable model (Claude Opus); writing-coach on a capable model (Claude Sonnet).

## Candidate Background links (writer decides; link, do not re-teach)
the-mechanics/autoregressive-generation; the-mechanics/sampling-temperature;
the-mechanics/nondeterminism; the-mechanics/tool-use.

# Commission: the-mechanics/output-diversity

## Assignment

One lesson for The Mechanics answering how does it actually do that for a behavior
nearly every user has seen: ask a chatbot for a story, a character name, or a
"random" idea several times and it keeps returning the same few — the heroine is
named Elara again, the same joke, the same shape. Work backward from that sameness
to its cause, step by step, until the reader hits ground. No code.

## The explanation, worked backward

1. A base model, before instruction-tuning, sampled at a given temperature, spreads
   its probability across many continuations, reflecting the range of human text.
2. Post-training reshapes that distribution. Reinforcement learning from human
   feedback and preference optimization push the model toward the completions
   raters and reward models prefer, concentrating probability on a few
   high-reward answers. The distribution the model samples from gets narrower, so
   the same names and phrasings dominate across separate generations.
3. Turning up temperature widens sampling within that narrowed distribution; it
   does not restore the range post-training removed. Teach the difference between a
   narrow distribution and a low temperature, linking the library's sampling and
   temperature lesson rather than re-teaching it.
4. Ground: the diversity lived in the base model, and alignment training traded it
   for answers people rate higher. Mark what is settled (post-training measurably
   lowers output diversity/entropy) and what is still open even for builders (which
   pressure dominates — reward over-optimization, the KL penalty, rater
   homogeneity — and how to recover diversity without losing quality).

Close where the reader meets this today: creative writing, brainstorming, and
"pick something at random" requests, and why a hotter temperature only partly
helps.

## Boundaries and neighbors

Distinct from the library's related mechanics lessons; link them, do not retread:
- the-mechanics/sampling-temperature (the sampling knob and why two answers diverge)
- the-mechanics/random-numbers (the numeric bias toward, e.g., 7)
- the-mechanics/overused-words (specific lexical tics like "delves" from training)
- the-mechanics/hedging and /sycophancy (other post-training behaviors)
This lesson's own subject is diversity collapse across generations and the
post-training cause behind it. The reader is smart, widely read, no codebase;
define output distribution, entropy/diversity, and mode in plain words at first use.

## Contribution the article must add

Give the reader the mechanism behind "AI writing all sounds the same": that
alignment training narrows the distribution the model samples from, so temperature
cannot buy back the variety, stated so they can judge why a creativity complaint is
not fixed by a setting. The writer states the exact original-work sentence in the
handoff.

## Sources

Series/template floor: at least 8 sources, at least 4 primary, at least 1
secondary. Primaries available: Kirk and coauthors (2024) on RLHF's effect on
output diversity and generalisation; the KL-regularized RLHF objective as stated in
a primary (for example the InstructGPT or a preference-optimization paper); a
measurement of entropy or diversity reduction from alignment; and documentation of
the name/story convergence. Secondary reporting for the observed phenomenon.

## This edition (keep distinct from the run's other four lessons)

- the-evidence/alphastar
- the-instruments/self-consistency-scoring
- what-could-go-wrong/mind-crime
- when-ai-breaks/amazon-rekognition-congress (already published tonight)

Shared risk with the-instruments tonight: both involve sampling a model repeatedly.
Keep this one on why the samples resemble each other (a narrowed distribution); the
instruments piece is about scoring by majority vote.

## Habits not to inherit (from the recent library)

- Recent The Mechanics deks compress the whole mechanism into one long causal "so"
  sentence; do not make that the reflex.
- Recent headings pose a question or lead with a number; vary construction.
- The recurring furniture stack is nb-stat-strip, nb-table, nb-note, nb-holdsup.
  Plan furniture from the supplied catalog for this piece.

## Production

Profile balanced. Model: capable (Claude Opus 4.8) for every role. Effort per
production policy: writing-coach low, researcher high, writer medium, editor high.
No required directive is in force. The writer records the actual writer model in
nb-meta per the library's convention (harness "claude-code").

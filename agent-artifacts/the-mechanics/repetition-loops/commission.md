# Commission: the-mechanics/repetition-loops

## Authorization

Scheduled run for 2026-08-15 (Sat). `nb duty` returned the-mechanics as an open
section: choose a topic within the beat, do not repeat a published slug. One of
five articles commissioned tonight, one per due series. No open-item tags.

## The behavior

A model gets stuck repeating itself: the same word, phrase, or whole sentence,
over and over, sometimes until it hits its length limit. Anyone who has run a
smaller or older model, pushed a long generation, or turned the randomness down
has seen it. The lesson works backward from that behavior to what produces it,
naming a real part of the system at each step, and marks which steps are settled
engineering and which are still open.

## Angle

Work down to ground. A candidate chain, for the writer and researcher to confirm
and prune:

1. The behavior, shown concretely: a real transcript or documented example of a
   model looping. Establish that this is about how text is chosen, not about the
   model running out of things to know.
2. The first step down: generation picks one token at a time from a probability
   distribution the model produces, and the choice rule matters. Greedy or
   low-temperature decoding, which keeps taking the most likely token, loops far
   more than sampling does. Autoregressive generation and sampling temperature
   are taught already; link them and build on them rather than re-teaching.
3. The step that explains the loop: the measured self-reinforcement. Holtzman and
   colleagues ("The Curious Case of Neural Text Degeneration," 2019) showed that
   maximum-likelihood decoding degenerates into repetition, and that once a phrase
   repeats, the model assigns a higher probability to repeating it again, so the
   loop feeds itself. Give the real figures the researcher confirms.
4. Ground: why the model puts rising probability on a continuation it just
   produced. Name the parts honestly. Part is the training objective and the
   context the model now conditions on; a full theoretical account of why trained
   language models favor repetition is still open, and there is published work
   arguing about it. Mark that boundary clearly, as the desk requires.
5. The fixes, tied to the cause: stochastic decoding (temperature, top-p), an
   explicit repetition penalty that lowers the odds of already-used tokens, and
   training-time methods. Each fix maps to a step above, so the reader sees why it
   works and why none of them is a complete cure.

By the end the reader can explain why a model loops, tell a decoding cause from a
training cause, and spot an explanation that skips the self-reinforcement step.
No code.

## Boundaries and neighbors

- Template: `lesson`. Section: Working Knowledge.
- Source policy: at least 8 sources, at least 4 primary and at least 1 secondary.
  Primary is the papers that own each mechanism claim (the neural-text-degeneration
  paper and the primary sources behind the self-reinforcement effect, repetition
  penalties, and any training-side fix). Secondary is explanatory or reporting
  context.
- Sampling temperature is taught in the-mechanics/sampling-temperature, one token
  at a time in the-mechanics/autoregressive-generation. Link both at first use
  and do not re-teach them. This piece is the repetition loop specifically.
- It is not why generation stops (the-mechanics/why-replies-stop) and not losing
  track over a long context (the-mechanics/losing-the-thread). Link where useful
  and stay off their ground.

## Recent-desk caution

- Do not open the "Why this matters" bookend with the house "by the end you will
  be able to" formula. Give this behavior its own hook.
- Recent the-mechanics closers land on a short flat line (formatting-defaults:
  "An instruction turns it off"; multilingual-gap: "Nobody can yet split the
  blame between the two causes"). The takeaway here should resolve the opener in
  this behavior's own particulars, not echo that closing shape.
- Vary the headline from the recent comma-continuation molds. If a decoding
  contrast or a self-reinforcement figure is the surprise, lead with it plainly.

## Production record

- Profile: balanced. Stages (model / effort, none required): writing-coach
  capable / low, researcher capable / high, writer capable / medium, editor
  capable / high.
- Harness: each role runs as an isolated subagent on the configured capable
  model (this runtime's Claude model). Deviations recorded per role.
- Workspace: `.nb-work/the-mechanics/repetition-loops`.
- Article: `library/the-mechanics/repetition-loops.html` under that workspace.

# Commission: the-mechanics/politeness-and-pressure

## The behavior

Anyone who uses chatbots has heard the folklore and probably tried it: say
"please," add "this is very important for my career," offer "I'll tip you $200,"
or threaten the model, and the answer supposedly gets better. The Mechanics starts
from one behavior the reader has seen and works backward, step by step, to what
produces it. The behavior here: the same question, wrapped in politeness, emotional
stakes, or pressure, can get a measurably different answer. No code.

## Work backward to the cause

Trace the behavior down to ground, marking at each step what is settled engineering
and what is still open even to the people who build these systems.
1. The surface fact: prompt wording that carries no new information about the task
   (a "please," a stated emotional stake, a tip offer, a threat) can shift the
   output. Ground it in a real documented result, not the folklore version.
2. First cause: a language model continues text according to patterns in its
   training data. Polite, high-stakes, or carefully-framed requests co-occur in
   human text with more careful, complete answers, so the framing shifts the
   model's predicted continuation. Link `the-mechanics/prompt-sensitivity` (a
   formatting change alone moved the answer) for the general fact that wording the
   model treats as irrelevant still moves it, instead of re-teaching it.
3. Second cause: post-training (RLHF / instruction tuning) shapes how the model
   responds to tone and to stated stakes — it is trained on human preferences, and
   human raters reward helpful, deferential answers. Link `the-mechanics/instructions-are-data`
   or `the-mechanics/sycophancy` where they carry a step already taught, rather
   than re-teaching. Keep this distinct from sycophancy: sycophancy is agreeing
   with a user's stated *opinion*; this is task *performance* shifting with tone
   and stakes.
4. The bottom / the open part: whether these tricks reliably help is contested and
   model-dependent. Careful studies find the effect is small, inconsistent, and
   sometimes reverses (politeness helps on some models/languages and hurts on
   others; tips and threats show weak or null average effects on newer models).
   Mark clearly what is settled (framing the model treats as irrelevant can move
   the output, because output is a prediction over human text) versus open (that
   any specific trick reliably improves answers — it does not, on the evidence).

## The reader should finish able to

Explain why a "please" or a "$200 tip" can change an answer at all (it is text the
model conditions on, like any other text), and why the popular claim that these
tricks reliably help does not hold up — so they can tell a real account from a
superstition and spot the missing step in any explanation that stops at "be nice
to the AI and it works harder."

## What this article must not do

- No code.
- Do not re-teach how a model predicts the next token, how attention works, or
  what RLHF is from scratch; link the earlier lessons named above at first use.
- Do not merge this into sycophancy or false-confidence; those are their own
  lessons. Reference, do not re-cover.
- Avoid the forming house tics: the "By the end you will be able to..." why-bookend
  closer (vary it), the "It is tempting to say X. That goes too far." device (used
  in two recent Mechanics/Breaks pieces), and the phrase "doing the work" ("the
  framing, not the content, is doing the work"). Say each in this article's own
  words. Do not close the takeaway on a posed diagnostic question if the last
  Mechanics piece already did (text-in-images ended on one).

## Sources and production

- Source policy (lesson/the-mechanics): at least 8 sources, at least 4 primary,
  at least 1 secondary. Primary = the papers that own the claims: studies measuring
  politeness effects (e.g. Yin et al., "Should We Respect LLMs?"), emotional-stimulus
  prompting (Li et al., "EmotionPrompt / Large Language Models Understand and Can Be
  Enhanced by Emotional Stimuli"), prompt-principle tests that measured tips/politeness
  (e.g. Bsharat et al., "Principled Instructions Are All You Need"), and any rigorous
  null/negative result on tipping or threats. The researcher must separate a real
  controlled measurement from a viral blog anecdote; anecdotes are secondary context
  at most.
- Production policy: profile "balanced", model tier "capable" (recorded actual:
  claude-opus-4-8). Effort guidance coach low / researcher high / writer medium /
  editor high; none `required`; effort not independently settable via the run's
  child interface, so roles run at session default reasoning; no deviation to report.

## Original-work target

Assemble the scattered, conflicting measurements into one plain mechanism — output
is a prediction conditioned on all the prompt's text, tone included — and use it to
explain both why the tricks do something and why they do not reliably do the good
thing people claim, separating the settled cause from the unsettled payoff.

# Commission: the-mechanics/length-control

## The behavior

Ask a chatbot to "write exactly 100 words" and it hands back 87, or 140, and
sounds certain it hit the mark. Ask for "three sentences" or "a tweet under 280
characters" and it misses just as often. Everyone who uses these systems has
watched a model that writes fluently fail at hitting a number it was told.

## Angle

Work backward from the missed count to what produces it, step by step, each step a
real part of the system. The chain: the model writes left to right, one token at a
time, choosing each next token from the text so far, with no separate tally of how
many words it has produced and no ability to look ahead to the end; the units it
emits are tokens, not words, so even an internal sense of "length" is measured in
the wrong currency (this is the same token-versus-character gap the letter-counting
lesson covers — link it, do not re-teach it); and once a word is out it cannot be
unwritten, so the model cannot draft-then-trim the way a person hitting a word
count does. Add the part that is trained in: post-training rewarded length in ways
that bias models toward certain lengths regardless of the instruction. Go down to
ground: the step where nothing below it changes the answer is that generation
carries no running counter over the right unit. Mark what is settled engineering
(token-by-token generation, tokens are not words) and what is open (how well a
model can implicitly track length in its activations, and why some models follow
length instructions far better than others).

Close where the same weakness surfaces: exact character limits, fixed numbers of
list items, and any task that needs the model to hit a count while generating.

## What it teaches (short, complete)

1. How generation runs: left-to-right, one token at a time, each token chosen from
   the text so far, with no separate length counter and no lookahead. (Link the
   published autoregressive-generation lesson; state only what this behavior needs.)
2. Why the counter would be in the wrong unit anyway: tokens are not words. (Link
   letter-counting; do not re-teach tokenization.)
3. The trained-in length bias from post-training, plus what is settled versus open
   about how well models can track their own length. One worked example with a
   real measured length-following result.

## Boundaries

- Build on published lessons, do not repeat them: `nb history --library` and LINK
  the-mechanics/autoregressive-generation and the-mechanics/letter-counting (and
  the-mechanics/formatting-defaults for the post-training length habit) at first
  use. The new work is the synthesis explaining the length-count failure and the
  no-revision point.
- One behavior. Do not drift into attention or training internals beyond the step
  each part needs. No code.

## Neighbors in tonight's edition (avoid overlap)

the-evidence/foundation-models, the-instruments/tau-bench,
what-could-go-wrong/model-collapse, when-ai-breaks/biden-deepfake-robocall.

## Source policy

Template minimum 8 sources: at least 4 primary, at least 1 secondary. Primary
here: a verifiable instruction-following benchmark that measures length
constraints (e.g., IFEval), a study of length-instruction following or of RLHF
length bias, and the tokenizer/generation sources that establish tokens-not-words
and left-to-right decoding. Reporting is secondary.

## Production record

Series production policy: balanced profile, model tier `capable` for every stage,
none `required`; efforts writing-coach low, researcher high, writer medium, editor
high. Roles run as isolated subagents on this harness's capable-tier model;
effort set to policy where settable, else harness default. No `required` directive
traded down. In nb-meta set `harness` to `Claude Code` and `model` to `capable`
(production tier; specific model identifier kept out of the published article per
harness policy). The writing-coach guide here was reused from a same-series
sibling lesson; take its craft and register, not its subject.

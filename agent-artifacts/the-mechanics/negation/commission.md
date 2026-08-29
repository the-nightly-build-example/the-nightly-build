# Commission: the-mechanics/negation

## Subject / behavior
The behavior: you tell a model what NOT to do and it does it anyway. "No onions"
and the sandwich has onions; "a room with no elephant" and the image has an
elephant; "don't mention the price" and the price appears. This desk works
backward from a behavior anyone who uses AI has seen to what produces it.

## Why this behavior, now
Negative instructions are among the most common things users type, and their
failure is one of the most reproducible model quirks, especially in image
generation. The course has taught tokenization quirks (`counting-letters`,
`glitch-tokens`), prompt sensitivity, and instruction-following
(`instructions-are-data`), but never why the single word "not" is handled so
poorly. It is a clean, self-contained mechanic the reader can test in a minute.

## Angle / what the lesson teaches
Work backward from the behavior to its cause, step by step, until the reader hits
ground. The chain to teach, in plain words with a small concrete example at each
step:
1. A model predicts the next token from a context; the salient content tokens
   ("onions", "elephant") pull strongly toward themselves, and "not"/"no" is one
   low-signal token that must override them.
2. Training distribution: affirmative statements vastly outnumber negated ones,
   and negation is under-represented in the exact instruction-following forms
   users need, so the model has seen far more "picture with an elephant" than
   "picture with no elephant".
3. In text-to-image specifically, the text encoder often treats the prompt as a
   loose bag of concepts, so "no elephant" activates "elephant"; teach the
   bag-of-words finding.
4. What helps and why: scale and instruction tuning reduce it in text; negative
   prompts, classifier-free guidance, and explicit conditioning are the
   engineering patches in image models. Mark which steps are settled and which
   are still open (how much of text negation-failure is architecture versus data
   is not fully settled).

By the end the reader can explain why "don't" underperforms and can spot when
someone's explanation ("the model just ignores negatives") skips a step. No code.

## The article's distinct contribution
Tie the everyday failure to two measured findings the reader would not connect on
their own: benchmark evidence that language models handle negation far worse than
affirmation, and the vision-language "bag-of-words" result that explains the image
case. Show they are the same weakness surfacing in two systems, and separate the
settled part (data imbalance, bag-of-words behavior, measured negation gaps) from
the open part (the precise mechanism inside attention).

## Template & policy
- Template: `lesson`.
- Source policy: min 8 sources; at least 4 primary, at least 1 secondary.
- Production policy (`balanced`, none `required`): researcher high, writer medium,
  editor high, coach low. Models this run: coach on a capable Sonnet-class model;
  researcher/writer/editor on a capable Opus-class model. No `required` directive.
- Tags: none (open item).

## Neighbors in this run (differentiate)
Runs alongside `the-evidence/proximal-policy-optimization`,
`the-instruments/mmlu-pro`, `what-could-go-wrong/treacherous-turn`,
`when-ai-breaks/workday-hiring-screening`. No overlap.

## Prior coverage to stay off
Published mechanics adjacent to this: `counting-letters`, `glitch-tokens`,
`text-in-images`, `instructions-are-data`, `prompt-sensitivity`,
`reading-images`, `hallucination`, `in-context-learning`. This lesson is about
negation specifically. Link `text-in-images` or tokenization pieces in Background
where the image case touches them; do not re-teach tokenization or how
image generation works from scratch. Negation is the whole subject.

## Recent habits not to inherit (from the last week of The Mechanics)
- Headline mold to avoid: "A model can <do X> and still <fail Y>" (counting-letters)
  and "The <thing> a model can't <do>" (glitch-tokens). Write a headline that
  states the negation finding in its own nouns.
- The desk's body sections have run as 4-6 short titled steps often ending on a
  "where the explanation runs out" section (glitch-tokens) — the settled/open
  mark is required content, but do not copy that section title.
- nb-note appears on nearly every recent mechanics piece as the default. Use it
  only where a labeled example (a failed prompt and its output) genuinely reads
  better as a note.

# Commission: the-mechanics/false-confidence

## Assignment

One lesson for The Mechanics, on the lesson template, on a behavior every user has
seen: a model states a wrong answer in exactly the same assured tone it uses for
a right one, and will even attach a confidence ("I'm 95% sure") that means
nothing. Work backward from that behavior to what produces it. This is the
scheduled open article for the series on 2026-08-23.

## The behavior and its cause, in order

The Mechanics answers "how does it actually do that" by naming each real part
until the reader hits ground. The chain here:

1. The model emits, at each step, a probability distribution over next tokens
   (the softmax over logits). That distribution is the only internal quantity
   resembling "confidence," and it is confidence about the next *word*, not about
   whether a claim is *true*.
2. A base (pre-trained) language model's token probabilities are often reasonably
   *calibrated* — define calibration in plain words: when it says 70%, it is
   right about 70% of the time. The GPT-4 technical report shows this directly:
   the base model's calibration on multiple-choice was good and got *worse* after
   RLHF (its own Figure 8). So post-training, which makes the model helpful and
   confident-sounding, flattens the honest uncertainty signal.
3. The confidence a model *states in words* is not read off that distribution at
   all. It is just more predicted text, generated to sound like the kind of
   answer the training data rewarded. There is no separate module that checks a
   claim against the world; nothing below that step would change the answer.
4. So a fluent, high-probability continuation can be flatly false, and the model
   has no built-in signal that distinguishes the two for the reader.

Mark which steps are settled engineering (softmax, that verbalized confidence is
generated text) and which are open or contested (exactly why RLHF degrades
calibration, whether and how much internal states "know" they are wrong — the
active research on this, e.g. work probing model internals, is unsettled and
should be flagged as such, not overstated).

## Required contribution

The reader should be able to explain why confident tone carries zero information
about correctness, tell the difference between the token-probability the model
has and the verbal confidence it prints, and know that the honest-uncertainty
signal a base model has is partly trained *out* by the step that makes chatbots
pleasant to use. A concrete worked example anchors it: the GPT-4 report's
calibration-before-and-after-RLHF result, with the actual numbers.

## Boundaries

- This is not hallucination. `the-mechanics/hallucination` is already published;
  hallucination is about *making facts up*, this lesson is about the *confidence
  signal* being uninformative. Link hallucination in Background at first use;
  do not re-teach it. Keep the spine on calibration and verbalized confidence.
- `the-mechanics/getting-math-wrong` (confidently wrong arithmetic) and
  `the-mechanics/sycophancy` (agreeing under pressure) are neighbors; reference
  them by link if needed, do not overlap. Sycophancy is about changing the answer
  to please; this is about the tone of a fixed answer.
- Do not teach the softmax or next-token prediction from scratch beyond the one
  step the argument needs: link `the-mechanics/autoregressive-generation` or
  `word-embeddings` where the reader needs the prerequisite. Probability needs no
  introduction.
- No code.

## Template, sources, policy

- Template: lesson. Word band 1200-2200.
- Source floor (nb source-policy the-mechanics): at least 8 sources, at least 4
  primary, at least 1 secondary. Primaries: the GPT-4 technical report (the
  calibration figure and its caption), the original calibration-of-neural-nets
  work (Guo et al. 2017, "On Calibration of Modern Neural Networks") for the
  definition and the reliability-diagram idea, and primary papers on verbalized
  confidence / whether models know what they know (e.g. Kadavath et al. 2022,
  "Language Models (Mostly) Know What They Know"; a verbalized-confidence study).
  Read them; represent the open questions honestly.
- Production policy (balanced): writing-coach low, researcher high, writer
  medium, editor high; "capable" tier for all, resolved to Claude Opus 4.8.
  nb-meta harness `claude-code-routine`, model `claude-opus-4-8`.
- Suggested nb-meta tags: calibration, confidence, rlhf, uncertainty.

## This edition's neighbors

`the-evidence/adam-optimizer`, `the-instruments/squad`,
`what-could-go-wrong/natural-selection`, `when-ai-breaks/michigan-midas`. No
overlap; this is the only how-it-works behavior piece.

## Recent shapes and phrasing to break

Recent Mechanics pieces (overused-words, getting-math-wrong, length-control,
nondeterminism) share habits to avoid:

- The opener that leads with a big `nb-table` of failing examples (getting-math-
  wrong, overused-words). One concrete example is enough to open; do not build
  the piece around a table of specimens.
- The paradox/twist closer heading — "the specific words are where the
  engineering runs out," "the sums it gets right are the least understood." Write
  the closer in this lesson's nouns; do not reach for a "the X is where the Y
  runs out" line.
- The step-by-step "work backward to ground" structure is the template's job and
  is expected; what must vary is the section names and the closing move.

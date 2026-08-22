# Commission: the-mechanics/overused-words

## Assignment

One lesson on a behavior every reader of AI text has seen: chatbots reach for the
same handful of words far more than people do ("delve", "tapestry", "boasts",
"underscore", "showcasing"). The Mechanics works backward from a behavior to its
cause, step by step, naming a real part of the system at each step, until the
reader hits ground. No code. Mark which steps are settled engineering and which
are open questions. The reader is smart, widely read, new to how these systems
are built.

## Why this behavior, now

The lexical fingerprint is the most common way readers claim to "spot AI writing,"
it is the basis of AI-detection tools, and since 2024 researchers have measured a
real, sudden rise in these words across published scientific writing. The reader
keeps meeting the claim "you can tell it was AI because it said 'delve'." This
lesson lets them judge that claim by understanding what actually produces the
word.

## Angle

Work the causal chain from the behavior down to ground:

1. The behavior, measured: not a vibe. Corpus studies find specific words spiking
   in frequency in model output and in human-authored text after late 2022
   (Kobak et al. on PubMed abstracts; the "delve"/word-frequency work). Give the
   reader real numbers, not impressions.
2. First cause up the stack: a language model outputs a probability distribution
   over the next token and a sampler draws from it. Overused words are words the
   model assigns high probability to across many contexts. (Link the taught
   mechanics of next-token generation and sampling temperature rather than
   re-teaching them.)
3. Why those particular words sit high: pretraining sets base frequencies from web
   text, but the concentration is sharpened in post-training. Reinforcement
   learning from human feedback and preference optimization push the model toward
   phrasings that scored well, which narrows the output distribution (mode
   collapse / reduced diversity is a measured effect of RLHF). This is the settled
   core of the mechanism: the reader should leave able to say "post-training
   concentrated the distribution."
4. Ground, and the open question: why *these specific* words. The leading concrete
   hypothesis for "delve" is that the human raters whose preferences shaped the
   reward signal include annotators for whom "delve" is ordinary register (the
   Nigerian/African-English annotator hypothesis, discussed 2024). Mark this
   clearly as a hypothesis with suggestive but not settled evidence, distinct from
   the settled claim that post-training concentrates the distribution. A reader
   should be able to tell where the engineering ends and the guesswork begins.
5. The consequence the reader cares about: this is why word-frequency AI detectors
   are fragile — the fingerprint is a distribution over training and tuning, not a
   watermark, so it shifts model to model and can be prompted away, and human
   writing now carries the same words.

## What to teach (short, complete)

Keep the chain above to what fits 1200-2200 words completely: the measured
behavior, next-token probability as the proximate cause (linked, not re-taught),
post-training distribution-narrowing as the settled mechanism, the specific-word
origin as the open question, and the detection consequence. Cut, don't shrink.

## Boundaries and non-overlap

- the-mechanics/formatting-defaults already traces bullet points and bold headers
  to a post-training stage that rewarded structure. This lesson shares that root
  cause (post-training shaping output) but is about lexical concentration and the
  specific-word question, not layout. Require a Background link to
  formatting-defaults and do not re-argue the RLHF-rewards-format point; extend it
  to word choice and go past it into distribution-narrowing and the annotator
  hypothesis.
- Next-token generation, sampling/temperature, and RLHF are taught elsewhere
  (autoregressive-generation, sampling-temperature, formatting-defaults). Link at
  first use; never re-teach. Researcher to confirm exact titles/paths.
- Work from the measurement papers and the primary RLHF-diversity literature, not
  from blog impressions. The annotator hypothesis must be sourced to its actual
  origin and labeled as unconfirmed.

## Source policy

Lesson in The Mechanics: at least 8 sources, at least 4 primary and at least 1
secondary. Primary: the corpus-measurement papers (e.g. Kobak et al. 2024 on
excess words in scientific abstracts; any measurement of model-output word
frequency), primary RLHF / preference-optimization papers documenting reduced
output diversity or mode collapse, and the primary source for the annotator-
dialect hypothesis. Secondary: reporting that popularized "delve" as an AI tell,
kept as secondary and used only for the framing, not the mechanism.

## Habits to avoid (break these, from the recent record)

- Recent Mechanics deks pair a behavior with a mechanism, often with a number
  ("A model can't count the words it's writing"). That shape is the house style,
  fine to use, but do not copy a neighbor's exact construction. Lead the dek with
  a concrete measured fact about the words.
- Vary orientation headings from recent openers. Mark settled-vs-open explicitly
  in the body (the beat requires it), but do not turn it into a stock "What's
  settled / What's open" scaffold heading.
- Furniture: a table of the most over-represented words with their measured
  frequency shift can genuinely help; use it only if it changes understanding.

## This run's neighbors

Also tonight: the-evidence/whisper, the-instruments/imagenet-top-5-accuracy,
what-could-go-wrong/value-lock-in, when-ai-breaks/itutorgroup-age-discrimination.
One paper, one register; distinct dek shapes.

## Production record

- Harness: claude-code-routine. Writer model: claude-opus-4-8 (production policy
  asks "capable"; no pinned model, no deviation).
- Effort per balanced policy: coach low, researcher high, writer medium, editor
  high. None required. Template: lesson.

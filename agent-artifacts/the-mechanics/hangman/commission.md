# Commission: the-mechanics/hangman

## The behavior

Ask a chatbot to "pick a word, keep it secret, and I'll guess it" (hangman, or
20 questions with the model as answerer). It plays along, but its answers to
your guesses contradict each other, and when you force it to reveal the word at
the end it often produces one that does not fit the clues it already gave. The
reader who has tried this has seen the model appear to cheat or change its mind.

## The angle and the original work

Work backward from the behavior to ground. The cause is not that the model is
dishonest. It is that the model has no hidden state: nothing it "knows" exists
unless it is written in the visible conversation. When you say "don't tell me
the word," the model writes nothing down, so there is no secret word anywhere. On
each of your guesses it re-reads the whole visible transcript and generates a
fresh, locally plausible yes/no answer, with no committed word constraining it.
At reveal time it generates a word that fits as many of its past answers as it
can, which is why it sometimes cannot.

Reach ground: the step below which nothing changes the behavior is that a
language model is a function of its visible input plus sampling, and keeps no
private memory between turns. A hidden commitment would have to live somewhere;
in a plain chat it has nowhere to live.

Original work for the writer: the model is not lying about a secret it holds; it
has no secret to lie about, and "cheating at hangman" is what it looks like when
a system with no hidden state is asked to hold one. Show the difference between
performing a commitment and holding one, and show what actually fixes it (writing
the word into the context, e.g. a hash or committing it in text, or tool/
scratchpad state).

## What the lesson teaches (short list, in order)

1. The behavior, concretely: a short reproducible transcript where the model's
   answers to guesses are mutually inconsistent, or the revealed word contradicts
   earlier clues. Set it up so the reader sees the contradiction, not just hears
   about it.
2. Why it happens, down to ground: the model has no hidden state; the visible
   transcript is its entire input; "keep it secret" writes nothing, so there is
   no word; each turn regenerates from what is visible. Link the published
   conversation-memory lesson (the transcript is resent each turn) and build on
   it: this is the sharper consequence — not forgetting what was said, but the
   impossibility of committing to what was not said. Do not re-teach the resend
   mechanism; cite it and go further.
3. What settles it vs what is a genuine design choice: settled = a plain chat
   model holds no commitment. Distinguish honestly from the cases that look
   similar but are not this (a model that DOES write the word in a hidden
   scratchpad or uses a tool to store it can hold a commitment; reasoning models
   with hidden thinking tokens are a real, partial exception the reader should
   understand). Mark what is settled engineering and what depends on the product.
4. Where the same weakness lives in systems the reader uses: any place a chatbot
   is trusted to "remember" or "commit to" something it never wrote down — a
   promised plan, a chosen answer withheld, a running tally kept "in its head."

No code beyond a short illustrative transcript. Depth over breadth.

## Boundaries

- One behavior and its cause. Do not turn into a general "how chat works" piece
  or a memory-features survey.
- Taught ground to link, not re-teach: conversation-memory (transcript resent
  each turn), autoregressive-generation, nondeterminism, sampling-temperature are
  published; link the relevant one and go further. The NEW content is
  commitment/hidden-state, not the resend or the sampler.
- Be precise about the exception: hidden reasoning tokens / scratchpads / tools
  can hold state. Do not claim models can never hold a commitment; claim a plain
  chat with the word withheld cannot.

## Neighbouring articles this run (avoid overlap)

Tonight also runs the-evidence/elmo, the-instruments/mlperf,
what-could-go-wrong/ai-environmental-cost, when-ai-breaks/babylon-health. No
overlap.

## Recent-pattern notes (habits to break)

the-mechanics recently opened with "The model sees your whole conversation for
the first time on every turn" (conversation-memory) and "Whoever else is in the
batch settles a near-tied logit" (nondeterminism), and has used a "What the
builders haven't settled" heading with an open-questions nb-table. Do NOT reuse
that open-questions heading/table shape for the settled-vs-exception section;
build it into concrete named headings. Do not mirror the conversation-memory
opener even though the subject is adjacent. Dek: one lean sentence with a
concrete detail; no comma-triad, no "the cause sits one level below" mold.

## Source obligations

lesson under the-mechanics: min 8 sources, >=4 primary, >=1 secondary. This is a
mechanism the reader can reproduce; grounding it needs primary sources on: the
autoregressive/stateless nature of transformer inference (a model paper or
technical doc stating each forward pass conditions only on the input tokens); how
chat APIs are stateless and require resending context (the OpenAI/Anthropic API
docs stating the API is stateless / you must send the conversation each time);
the existence of hidden reasoning/scratchpad state (a reasoning-model system card
or the chain-of-thought/scratchpad literature). Primary = these docs/papers.
Secondary = reputable write-ups demonstrating the hangman/20-questions failure
(blog posts, forum threads that held up) for the behavior itself. If a concrete
transcript is used, it must be reproducible/faithful, not invented as evidence.

## Production record

Profile balanced. Recorded (policy "capable"): writing-coach Opus 4.8/low,
researcher Opus 4.8/high, writer Opus 4.8/medium, editor Opus 4.8/high. No
required directive; no deviation.

## Bookend link candidates

Background: `the-mechanics/conversation-memory` (transcript resent each turn),
`the-mechanics/autoregressive-generation` (how output is produced token by
token). Go deeper (beyond this paper): an API doc on statelessness; a piece on
reasoning-model hidden state. Lesson works for a reader who opens none.

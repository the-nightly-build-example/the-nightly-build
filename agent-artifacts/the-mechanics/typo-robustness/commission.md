# Commission: the-mechanics/typo-robustness

## The assignment

Start from a behavior every reader has seen: you type a message full of typos and the
chatbot understands you anyway, and usually answers as if you had spelled everything
right. Explain what produces that, step by step, down to ground. One lesson on the
lesson template. No code.

The reader is the paper's declared reader: smart, widely read, no codebase. Assume no
NLP background. Teach each term at first use.

## Why this behavior, tonight

The Mechanics has taught tokenization from several angles (glitch-tokens,
poetic-meter, counting-letters, letter-counting, word-embeddings, word-order) but
always where tokenization causes a failure. Typo robustness is the same machinery
producing a success the reader relies on daily, and explaining it consolidates what
those failure lessons taught: the reader learns that the tokenizer is not a
spell-checker and that there is no spelling stage at all. It is the "how does it do
that" the reader is likely to have wondered about precisely because it seems like it
should not work.

## The angle

Work backward from "it understood my typo" to the cause, naming a real part at each
step and marking settled engineering versus open questions:

- There is no spell-check step. The model never corrects your spelling before reading
  it; it has no separate spelling stage to run. This is the misconception to clear
  early, and it is the reason the behavior is surprising.
- Subword tokenization is the first real part. Teach byte-pair-encoding-style
  tokenization in plain words: text is split into frequent chunks, not words or
  letters. Show with a concrete example how a correctly spelled common word becomes
  one token while a misspelling becomes a different, usually longer sequence of
  smaller pieces (down to bytes in the limit). Link the-mechanics/glitch-tokens and
  word-embeddings where they were taught rather than re-teaching. Give a real tokenized
  example if the researcher can supply a verified one (for example, from a public
  tokenizer such as tiktoken/GPT tokenizers), with the actual token splits.
- Why the pieces still carry meaning: training text is full of typos, and the pieces a
  misspelling breaks into tend to co-occur, in that training data, with the same
  contexts as the correctly spelled word, so their learned representations sit near it.
  This is the load-bearing step and must be concrete, not hand-waved.
- Why context finishes the job: the surrounding tokens make the intended word the most
  probable reading, so the model predicts a continuation as if the word were correct.
  Connect to how next-token prediction and attention over context work, linking
  earlier lessons.
- The floor and the failure edge (mark clearly what is settled and what is open):
  natural human typos are handled robustly and this is well understood; adversarial or
  crafted perturbations (homoglyphs, invisible characters, token-splitting attacks) can
  still break or steer models, and how far robustness extends is an active research
  question. The reader should leave able to tell the everyday case from the adversarial
  one, and to spot an explanation that skips the "there is no spell-checker" step.

End where nothing below would change the answer: the training distribution plus subword
tokenization, no correction module.

## Boundaries

- Claims about mechanism come from primary sources: the BPE / subword tokenization
  papers (Sennrich et al. 2016; the byte-level BPE used by GPT-2, Radford et al. 2019),
  the transformer/attention primary where needed (link the taught lesson rather than
  re-teaching), and primary research on typo/adversarial robustness for the failure
  edge. A live tokenizer's actual output is a legitimate primary artifact if recorded
  with the tool and version.
- This is not a lesson on how to prompt or on spelling correction products. Stay on the
  mechanism.
- No code. A worked tokenization example shown as text or a small table is fine.

## Neighbors in this run

Publishing alongside wavenet, mean-average-precision, power-seeking-ai,
sports-illustrated-ai-authors. No overlap. Nearest taught neighbor is glitch-tokens
(tokens that break the model); this lesson is the inverse (tokenization degrading
gracefully). Draw the line explicitly and link it.

## Recent habits not to inherit

From the last several Mechanics lessons (poetic-meter, hedging,
speech-to-text-hallucination, lost-in-the-middle, model-self-identity):

- The desk's standing headline mold is "A [system] does X but can't Y" (a chatbot
  rhymes but can't count syllables; plays legal chess, the chatbots don't). This
  lesson's behavior is a success, so do not force that contrast mold; write a headline
  that states what actually happens.
- Heading molds "Why the X land and the Y limps" and "The floor beneath the failure"
  recur. Vary construction; keep headings in this piece's own nouns.
- Several recent openers stage a specific test the reader can run ("Ask for a haiku,
  then count the syllables"). Staging a concrete example is good; do not copy the
  imperative-opener rhythm of the last lesson.

## Source policy

Floor: at least 8 sources total, at least 4 primary and at least 1 secondary. Primary
means the tokenization papers, the robustness research, and any recorded live-tokenizer
artifact. Meet the floor with sources that change the interpretation.

## Production record

- Template: lesson. Series: the-mechanics (open mode; no commissioned tag).
- Word band: 1200-2200.
- Model/effort actuals: production-policy resolved "capable"/non-required for all roles;
  all run on the available capable model (Claude via isolated subagents), coach low,
  researcher high, writer medium, editor high. Nothing traded down.
- Checkout revision: df69fc11a5d7fcdfdbc7eda5eb8a8d178b6d6a17.

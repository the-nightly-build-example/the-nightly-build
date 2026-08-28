# Commission: the-mechanics/glitch-tokens

## The behavior
Ask an older GPT model to repeat the string " SolidGoldMagikarp" and it will not.
It says "distribute," or dodges, or grows evasive, or produces something unrelated
and strange. A handful of odd tokens (" petertodd," "davidjl," a few Reddit
usernames and forum artifacts) reliably break models this way, while every normal
word behaves. The lesson explains what produces this.

## Why this behavior, now
It is a vivid, well-documented anomaly that exposes a real seam in how models are
built: the tokenizer's vocabulary is created separately from — and often before —
the model's training data, so a token can exist in the vocabulary yet be almost
absent from what the model actually learned from. Understanding this one behavior
teaches the reader that "the words a model can read" and "the words a model has
learned anything about" are two different sets, and lets them predict a class of
failures around rare tokens.

## The angle (work backward from the behavior to its cause)
1. The behavior: a specific, reproducible glitch on a named token, described
   honestly (which model, what was asked, what it did). Prefer a documented case
   from the primary write-ups.
2. The immediate cause: the model has no useful learned representation for that
   token, so its output on it is unmoored.
3. One level down: the token exists because the TOKENIZER's vocabulary was built
   by byte-pair merges over a corpus that included things like a Reddit counting
   forum's usernames — but the model's TRAINING data was filtered/different, so
   that token was seen rarely or never during training. Its embedding vector
   therefore sat near its random initialization, never shaped by learning.
4. Why normal tokens do not glitch: common tokens appear enough in training for
   their embeddings to acquire meaning; the glitch is specific to under-trained
   tokens.
5. Hit ground: the step below which nothing changes the answer — an embedding the
   optimizer never moved cannot carry meaning, whatever the rest of the network
   does.
Mark what is settled (tokenizer built separately from training; under-trained
tokens have near-random embeddings; that produces anomalous behavior) versus what
is open (the precise internal path from a near-random embedding to each specific
weird output, and how thoroughly newer tokenizers/models have removed these).
No code (series rule).

## Boundaries and continuity
Differentiate sharply from published neighbors and link, do not overlap:
- the-mechanics/letter-counting: about characters HIDDEN INSIDE a normal token
  (BPE word-pieces). This lesson is the opposite end — a whole token that the
  model barely trained on. Same tokenizer, different failure. Make the distinction
  explicit and link it.
- the-mechanics/word-embeddings: what a learned embedding is. Link it for the "an
  embedding is a learned vector" idea; the point here is an embedding that was
  NOT learned.
- the-mechanics/multilingual-gap: token counts across languages — different issue.
No verdict block in the body; the takeaway lands the judgment.

## Template, furniture, policy
- Template: lesson. No code listings (series rule). A table listing a few glitch
  tokens and how a model failed on each could be effective if the record supports
  exact strings; inline <code> is appropriate for the exact token strings the
  reader must preserve. A note ("In plain language") could carry the tokenizer-vs-
  training-data distinction. Do not force furniture.
- Source policy: >=8 sources, >=4 primary, >=1 secondary. Primary = the original
  investigations (the Feb 2023 LessWrong write-ups by Jessica Rumbelow and Matthew
  Watkins, "SolidGoldMagikarp (plus, prompt generation)" and follow-ups), the peer
  reviewed follow-up on detecting under-trained tokens ("Fishing for Magikarp,"
  Land & Bartolo, 2024), the GPT-2 tokenizer/BPE documentation establishing the
  vocab-vs-training-data split, and any primary account of tokenizer construction.
  Secondary = reporting/explainers.
- Production policy (balanced): researcher high/capable, coach low/capable,
  writer medium/capable, editor high/capable. No `required` directives.

## Recent shapes in this series to break
Short behavior-declarative headlines are the house style; do not clone the most
recent two, and steer clear of letter-counting's framing since it is topically
adjacent. Avoid banned dek molds and the comma-plus-"and" heading join.

## What this article must add
The reader should be able to explain why a fluent model breaks on " SolidGold-
Magikarp" but not on ordinary words, and understand that a model's vocabulary and
what it has actually learned are two different things.

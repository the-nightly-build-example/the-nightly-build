# Commission: the-mechanics/multilingual-gap

## The behavior

A chatbot that is fluent and sharp in English gets vaguer, more error-prone, and
oddly more expensive in many other languages, and worst in languages written in
non-Latin scripts or with little web text. Anyone who has used AI in a second
language has seen it. One lesson, worked backward from that behavior to what
produces it.

## The angle

Work from the visible behavior down to ground, each step a real part of the
system, and mark settled versus open.

- The behavior, with a concrete instance the evidence supplies: the same model,
  same task, noticeably weaker in a lower-resource language, and a bill that is
  larger for the same request.
- The first and largest cause: training-data distribution. These models learn
  from a corpus that is overwhelmingly English and a handful of high-resource
  languages, so the model has simply seen far less of most languages. Ground this
  with a real figure the researcher supplies (for example the English share of a
  named model's training data, or of Common Crawl). This is the primary mechanism
  and should lead.
- The second cause, the token tax: the tokenizer is fit mostly on English-heavy
  text, so text in other languages breaks into many more tokens per word. Explain
  what that does, plainly: more tokens means more of the context window spent, a
  higher price for the same message, and a harder modeling problem. Use a real
  per-language token-count comparison from the evidence (e.g. Ahia et al. 2023;
  Petrov et al. 2023). Link the taught idea of tokenization rather than
  re-teaching it (the-mechanics already has letter-counting; the press also has a
  tokenization lesson), and keep this the secondary amplifier, not the whole
  story.
- Ground and honesty: mark what is settled (data scarcity and token inflation are
  well established) versus what is contested or moving (how much each cause
  contributes, and that larger multilingual models and better tokenizers have
  narrowed but not closed the gap). Note the two-way cost: worse answers and a
  real price/access disparity for speakers of these languages.

No code. The reader should leave able to predict which languages suffer most and
why, and to tell a data-scarcity explanation from a tokenizer one.

## Template and furniture

Lesson template. A per-language token-count or performance table is the natural
carrier and likely earns its place; any figure must come from a verified series in
the evidence record. Furniture is the writer's call with the editor.

## Sources and production

- Source policy: lesson under the-mechanics, minimum 8 sources, at least 4
  primary, at least 1 secondary. Primary: the tokenization-fairness papers (Ahia
  et al. 2023 "Do All Languages Cost the Same?"; Petrov et al. 2023 "Language
  Model Tokenizers Introduce Unfairness Between Languages"), training-data
  language-share sources (e.g. the GPT-3 paper's language table, Common Crawl
  statistics), and a multilingual-evaluation source showing the performance gap.
  Read the primary documents; record any exact token-count example reproducibly.
- Production policy (balanced), model/effort used this run: writing-coach capable
  (claude-opus-4-8) low; researcher capable (claude-opus-4-8) high; writer capable
  (claude-opus-4-8) medium; editor capable (claude-opus-4-8) high. Harness:
  claude-code-routine.

## This edition's neighbors (all distinct)

- the-mechanics shelf has letter-counting, word-embeddings, and tokenization
  (in another series) touching the tokenizer. This lesson is about the multilingual
  performance-and-cost gap, led by data distribution. Link tokenization at first
  use; do not re-teach it or repeat the character-blindness lesson.
- The four other lessons tonight are unrelated in subject.

## Habits not to inherit

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula, and do not model The Mechanics' recent "the thing
  that feels like X is not what happens" opener.
- Do not close on a stock "where this lives now" / "what the system never learned"
  heading; name the closing section for its content. Do not land the takeaway on
  negative parallelism. Deks: avoid the banned molds.

## Required contribution

The article turns a widely felt frustration into a two-part mechanism a reader
can reason with, showing why the gap is largest exactly where training text is
scarcest and the tokenizer least fitted, and why it is a cost as well as a quality
problem.

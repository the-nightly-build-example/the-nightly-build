# Commission: the-mechanics/counting-letters

## The behavior
Ask a chatbot how many times the letter "r" appears in "strawberry" and it will
often answer two. Ask it to spell a word backward, count the letters in a word,
or find every word in a list with a double letter, and it fails in the same
family of ways while answering far harder questions fluently. This is the
behavior anyone who uses AI has seen, and the lesson explains what produces it.

## Why this behavior, now
It is the single most-cited "gotcha" about language models, and the honest
mechanical answer teaches something the reader can reuse: the model does not read
text as letters. Understanding this one behavior lets the reader predict a whole
class of failures (spelling, counting characters, anagrams, rhyme by spelling)
and understand why some later models suddenly got the strawberry question right.

## The angle (work backward from the behavior to its cause)
Trace the behavior down, step by step, each step a real part of the system:
1. The behavior: a specific, reproducible miss on a letter-counting or spelling
   task, with a real example the reader can picture.
2. The immediate cause: before the model sees anything, its tokenizer splits the
   text into tokens — chunks that are often whole words or word-pieces, not
   letters. "strawberry" arrives as a small number of tokens, and the identity of
   the individual characters inside a token is not directly present.
3. One level down: how the tokenizer is built (byte-pair encoding merges frequent
   character sequences into single tokens from a fixed vocabulary), so the unit
   the model computes over is chosen for compression, not for spelling. Show a
   real tokenization of a word or two (use a real tokenizer's output; verify it).
4. Why the model can still often spell common words: spelling that appears often
   enough in training (letter-by-letter spellings, hyphenations) is learnable as
   an association, which is why the failures cluster on the cases where that
   signal is weak or the counting is exact.
5. Hit ground: the step below which nothing changes the answer — the model has no
   character-level access to a token unless spelling information was learned into
   the weights or supplied in the prompt.
Mark what is settled engineering (tokenization, BPE, that tokens hide characters)
and what is not fully settled (exactly how much character information models
recover, and why some behaviors improve with scale or with tool use / spelling
the word out / "reasoning" step by step). No code (series rule).

## Boundaries and continuity
Close neighbors already published — differentiate sharply, link rather than
re-teach:
- the-mechanics/text-in-images taught that an image generator gets letters wrong
  because the word reaches the drawing step as a whole-word token with spelling
  blurred, and that the fix is a character-level encoder. That is IMAGE
  generation. This lesson is about TEXT: counting/spelling letters in ordinary
  chat. Same root cause (tokens hide characters); different behavior and surface.
  Link text-in-images for the tokenizer-hides-spelling idea and make the
  distinction explicit rather than repeating its worked example.
- the-mechanics/multilingual-gap taught that the tokenizer splits some languages
  into many more tokens. Link it for "what a tokenizer is" if useful, but the
  point here is character identity inside a token, not token count across
  languages.
- the-mechanics/getting-math-wrong taught next-token arithmetic failure. Counting
  letters is a different mechanism (tokenization hiding characters), not
  arithmetic — do not conflate.
No verdict block in the body; the takeaway lands the judgment.

## Template, furniture, policy
- Template: lesson. No code listings (series says "No code").
- Furniture candidates: a table showing a real word's tokenization (token pieces
  in one column, what that hides in another) is a strong fit if the writer
  captures a real tokenizer's output and cites it. A stat strip is likely
  unnecessary. A source asset (a screenshot of a real tokenizer view) only if it
  carries the argument better than a table and is captured from a citable public
  tool. Do not force furniture.
- Source policy: >=8 sources, >=4 primary, >=1 secondary. Primary = the BPE
  source (Sennrich et al. 2016 for NMT, and/or the original Gage 1994 idea), the
  tokenizer documentation/papers (GPT-2 BPE, tiktoken, SentencePiece), any paper
  measuring models' character/spelling ability or the strawberry-class failure,
  and any primary write-up of a fix (character-level or byte-level models,
  tokenizer-free approaches). Secondary = reporting/explainers for context.
- Production policy (balanced): researcher high/capable, coach low/capable,
  writer medium/capable, editor high/capable. No `required` directives.

## Recent shapes in this series to break
The Mechanics headlines run as short declaratives about a behavior ("A model
can't count the words it's writing," "ChatGPT multiplies two five-digit numbers
and misses by 913,200"). That house shape is fine, but do not copy the exact
build of the two or three most recent, and steer well clear of text-in-images'
framing since it is topically adjacent. Avoid the banned dek molds and the
comma-plus-"and" heading join.

## What this article must add
The reader should be able to explain, without hand-waving, why a fluent model
miscounts the r's in strawberry — and predict which other tasks will fail for the
same reason and which fixes actually address it.

# researcher brief: the-mechanics/counting-letters (01)

Inputs:
- editorial-direction.md  (citation standard, the-mechanics territory, declared reader)

Output: agent-artifacts/the-mechanics/counting-letters/researcher/01/evidence.md

The behavior under examination: language models miscount letters and mishandle
spelling-level tasks (the canonical case is answering that "strawberry" has two
r's), while answering much harder questions fluently. The lesson explains the
cause. Research the mechanism from primary sources.

Research questions the evidence record must answer, each traced to an owning
primary (give locators):
- A concrete, reproducible instance of the failure that can be described honestly
  (a specific model, a specific prompt, the wrong answer). Prefer a documented
  example from a paper or a primary write-up over an anecdote; if you reproduce
  one yourself with a public tokenizer/tool, record exactly what tool and version.
- What tokenization is and how it works: byte-pair encoding (Sennrich, Haddow,
  Birch 2016 for NMT; and the underlying idea from Gage 1994), and the tokenizers
  language models actually use (GPT-2 byte-level BPE; tiktoken; SentencePiece).
  Cite the papers/docs that own these. Establish that tokens are frequency-merged
  chunks, often whole words or word-pieces, not letters.
- A real tokenization of one or two example words, showing the pieces the word is
  split into. Use a real, citable tokenizer (e.g., OpenAI's public tokenizer
  view / tiktoken, or the GPT-2 tokenizer) and record the exact output and the
  tool. This is the worked example the lesson turns on — verify it.
- Evidence on models' character-level / spelling ability and the letter-counting
  failure specifically: papers measuring whether and when models can access
  characters inside tokens (e.g., work on character/spelling probing, "models
  can't spell", CUTE or similar character-understanding benchmarks, byte-level or
  character-aware model papers). Establish the settled claim (tokens hide
  character identity) and the open question (how much character info models
  recover, and why some behaviors improve).
- The fixes and why they work: character-level or byte-level models
  (e.g., ByT5/CANINE or similar), tokenizer-free approaches, and prompt-level or
  tool-level workarounds (spelling the word out, step-by-step counting). Cite the
  primary write-up of at least one fix.

Search for what breaks the angle: evidence that the failure is NOT primarily
tokenization (e.g., that models with the same tokenizer count reliably, or that
the miss persists even when characters are exposed), and record it in
Contradictions in full.

Source policy: at least 8 sources, at least 4 primary, at least 1 secondary.
Classify each by authorship and stake. Confirm every URL resolves. Note the
close prior lessons the-mechanics/text-in-images and multilingual-gap only if a
specific continuity fact is needed; do not research the repository for
background.

# Evidence: the-mechanics/counting-letters (01)

The evidence supports the lesson's core mechanism firmly. Byte-pair encoding is
documented from its 1994 compression origin (Gage) through its 2016 adaptation to
subword segmentation (Sennrich et al.) to the byte-level tokenizers production
models actually run (GPT-2's byte-level BPE; OpenAI's `tiktoken`; SentencePiece).
A real, reproducible tokenization of "strawberry" was generated with `tiktoken`
0.14.0 and is recorded exactly: every current OpenAI encoding splits the word into
three word-pieces, none of them a single letter, with the three r's distributed
across pieces. The failure itself, and the settled claim that tokens carry no
direct character index, is owned by CUTE (Edman et al. 2024) and Kaushal & Mahowald
(2022); the fix direction is owned by ByT5 (Xue et al. 2021).

The evidence is thin in one place and complicates the angle in another. Thin: I did
not query a live model to capture the wrong answer firsthand, so the specific
"strawberry has two r's" instance from a named model rests on secondary reporting
(TechCrunch), not a primary transcript. Complicating: the strongest primary source
on the behavior (CUTE) shows models can spell their tokens out correctly yet still
fail character manipulation, and that the failure persists even when a word is split
into several tokens. Tokenization is a real and well-sourced cause, but the evidence
does not support tokenization as the *sole* cause. This is the record's most
important finding for the editor and is detailed under Contradictions.

Note on one term: CUTE has no "letter-counting" task. It tests spelling, character
containment, and character manipulation (insert/delete/substitute/swap). Do not cite
CUTE as measuring counting. It is the best primary source for the adjacent claim
(tokens hide character identity; models fail to operate on characters), not for a
counting score.

## Sources

```text
URL:         https://www.derczynski.com/papers/archive/BPE_Gage.pdf
Kind:        primary. Gage authored the algorithm; this is his own article text.
             (Archival PDF of the original; see Discarded for the recording choice.)
Establishes: The origin and exact definition of byte-pair encoding, as a data-
             compression method, firsthand.
Paraphrase:  BPE compresses by repeatedly finding the most frequent pair of
             adjacent bytes and replacing every instance with a byte not already
             in the data, iterating until no frequent pair or no free byte remains.
             The power of the method is that replacement codes nest: a new code can
             itself contain earlier codes, so tokens grow into long strings.
Locators:    Section 1 "Theory"; Section 5 "Advantages of BPE" (worked example);
             Listing 1 (compression pseudocode). C Users Journal, 1994.
Quote:       "The algorithm compresses data by finding the most frequently
             occurring pairs of adjacent bytes in the data and replacing all
             instances of the pair with a byte that was not in the original data."
             Worked example: "Original input data string: ABABCABCD / Change pair
             AB to unused X: XXCXCD / Change pair XC to unused Y: XYYD".
```

```text
URL:         https://aclanthology.org/P16-1162/  (arXiv preprint: 1508.07909)
Kind:        primary. Sennrich, Haddow & Birch own the adaptation of BPE to word
             segmentation; this is their paper.
Establishes: That the tokenization used by neural language models is BPE borrowed
             from Gage's compression algorithm and applied to characters/word-
             pieces to build an open (subword) vocabulary. GPT-2 later cites this
             exact paper as its BPE reference ("Sennrich et al., 2015").
Paraphrase:  Rare and unknown words are handled by segmenting words into subword
             units learned by a segmentation "based on the byte pair encoding
             compression algorithm," letting a fixed vocabulary represent an open
             vocabulary. Merges are frequency-driven, so frequent sequences become
             whole tokens and rare ones stay fragmented.
Locators:    Abstract; Proc. ACL 2016 (Vol. 1), pp. 1715-1725, Berlin.
Quote:       "a segmentation based on the byte pair encoding compression algorithm."
```

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
Kind:        primary. Radford et al. (OpenAI) describe GPT-2's own tokenizer.
Establishes: That a production LM tokenizer is byte-level BPE with a base
             vocabulary of 256 bytes, a total vocabulary of 50,257, and a rule that
             prevents merges across character categories with an exception for
             spaces. The space exception means a word preceded by a space is
             typically kept as one token, which is why running-text "strawberry"
             becomes a single token (see reproduction below).
Paraphrase:  Reference BPE on Unicode code points would need a base vocabulary of
             over 130,000; byte-level BPE needs only 256. BPE is described as a
             practical middle ground that interpolates between word-level tokens for
             frequent sequences and character-level tokens for infrequent ones.
Locators:    Section 2.2 "Input Representation"; Section 2.3 "Model" (vocab 50,257).
Quote:       "Byte Pair Encoding (BPE) ... is a practical middle ground between
             character and word level language modeling which effectively
             interpolates between word level inputs for frequent symbol sequences
             and character level inputs for infrequent symbol sequences." And: "a
             byte-level version of BPE only requires a base vocabulary of size 256.
             ... we prevent BPE from merging across character categories for any
             byte sequence. We add an exception for spaces".
```

```text
URL:         https://github.com/openai/tiktoken
             (mapping read from tiktoken/model.py on the main branch)
Kind:        primary. OpenAI's own BPE tokenizer library; it owns the encoding
             definitions and the model-to-encoding mapping.
Establishes: That current OpenAI models tokenize with BPE, and which encoding each
             uses: gpt-4o and gpt-5 use o200k_base; gpt-4 and gpt-3.5-turbo use
             cl100k_base; gpt2 uses the gpt2 encoding. This is what makes the
             reproduction below citable rather than anecdotal.
Paraphrase:  tiktoken is "a fast BPE tokeniser for use with OpenAI's models." BPE is
             a way of converting text to tokens that is reversible and lossless and
             recognizes common subwords such as "ing." MODEL_TO_ENCODING maps
             "gpt-5"/"gpt-4o" to "o200k_base", "gpt-4"/"gpt-3.5-turbo" to
             "cl100k_base", "gpt2" to "gpt2".
Locators:    README ("What is BPE anyway?"); tiktoken/model.py MODEL_TO_ENCODING and
             MODEL_PREFIX_TO_ENCODING dictionaries.
Quote:       README: "a fast BPE tokeniser for use with OpenAI's models."
```

```text
URL:         (reproduction; tool = tiktoken 0.14.0, Python 3.11, run in this session)
Kind:        primary artifact. A tokenization I generated and can reproduce, not a
             claim repeated from elsewhere.
Establishes: The worked example the lesson turns on. Every current OpenAI encoding
             splits "strawberry" (no leading space) into three pieces, none a single
             letter; the three r's fall across the pieces, so a model that reasons
             over tokens must recover and sum characters it never sees indexed.
Paraphrase:  Exact outputs (token ids and their decoded text):
             - gpt2 / r50k_base: [301, 1831, 8396] = 'st' | 'raw' | 'berry'
             - cl100k_base (GPT-4, GPT-3.5): [496, 675, 15717] = 'str' | 'aw' | 'berry'
             - o200k_base (GPT-4o, GPT-5): [302, 1618, 19772] = 'st' | 'raw' | 'berry'
             With a leading space, " strawberry" is a SINGLE token in every encoding
             (gpt2/r50k 41236; cl100k 73700; o200k 101830) - the more common case in
             running text, where the word's characters are hidden inside one token.
             In cl100k the r's split 1 ('str') + 0 ('aw') + 2 ('berry'); in
             gpt2/o200k they split 0 ('st') + 1 ('raw') + 2 ('berry').
Locators:    tiktoken 0.14.0, encodings gpt2, r50k_base, cl100k_base, o200k_base.
Quote:       n/a (the ids and pieces above are the exact tool output).
```

```text
URL:         https://aclanthology.org/D18-2012/  (arXiv preprint: 1808.06226)
Kind:        primary. Kudo & Richardson own SentencePiece, the other subword
             tokenizer widely used by open models.
Establishes: That a second production tokenizer family (SentencePiece) also builds
             a subword vocabulary, trained directly from raw text, confirming
             subword tokenization is the norm across model families, not one vendor's
             choice.
Paraphrase:  SentencePiece is a language-independent subword tokenizer and
             detokenizer that trains subword models directly from raw sentences,
             enabling an end-to-end language-independent pipeline.
Locators:    Abstract; EMNLP 2018 System Demonstrations, pp. 66-71, Brussels.
Quote:       "a language-independent subword tokenizer and detokenizer designed for
             Neural-based text processing".
Caveat:      This paper does not itself name which models adopt it; do not attribute
             specific models (e.g. T5, LLaMA) to it from this source.
```

```text
URL:         https://aclanthology.org/2024.emnlp-main.177/  (PDF read in full)
Kind:        primary. Edman, Schmid & Fraser own the CUTE benchmark and its results.
Establishes: The settled claim (tokens carry no direct character access) AND the
             sharp qualification of it (models can nonetheless spell their tokens).
             Best primary source for the behavior adjacent to letter-counting.
Paraphrase:  LLMs "split text into multi-character tokens and process them as atomic
             units without direct access to individual characters." Across models
             from 7B to 132B, few-shot and without fine-tuning, they do very well at
             spelling and inverse spelling (writing a token out letter by letter) but
             break down on character containment and on character-level manipulation
             (insert/delete/substitute/swap), where word-level versions of the same
             task stay far higher. Tasks are: spelling, inverse spelling, contains
             char/word, orthographic/semantic similarity, and the four manipulations.
             There is no counting task.
Locators:    Abstract; Section 3 (tasks) and Figure 1; Section 5 (results),
             Figure 2; Section 6 (Conclusion); Appendix E (random strings),
             Appendix F (token-split impact). Proc. EMNLP 2024, pp. 3017-3026.
Quote:       "most of them seem to know the spelling of their tokens, yet fail to
             use this information effectively to manipulate text". And: "While
             current LLMs with BPE vocabularies lack direct access to a token's
             characters, they perform well on some tasks requiring this information,
             but perform poorly on others."
```

```text
URL:         https://aclanthology.org/2022.naacl-main.179/  (arXiv preprint: 2206.02608)
Kind:        primary. Kaushal & Mahowald own this probing study.
Establishes: That character identity is recoverable from subword token embeddings by
             a trained probe, i.e. the information is present in the representation,
             not absent. This is the counterweight to a naive "the characters are
             simply not there" reading.
Paraphrase:  Probing classifiers predict whether a given character is present in a
             token from the token's embedding across models (GPT-J, BERT, RoBERTa,
             GloVe); the models "robustly encode character-level information."
             The knowledge is attributed to systematic character-part-of-speech
             relationships and to natural variation in how related strings tokenize.
Locators:    Abstract; NAACL 2022, pp. 2487-2507, Seattle.
Quote:       "these models robustly encode character-level information" (abstract).
Limitation:  The hosted PDF returned as non-extractable binary, so I have the
             abstract-level claim and venue verified but not the per-model probe
             accuracy figures. Treat the specific accuracy numbers as unverified;
             the qualitative claim (robust encoding) is confirmed from the abstract.
```

```text
URL:         https://arxiv.org/abs/2105.13626  (TACL 2022, vol. 10, pp. 291-306)
Kind:        primary. Xue et al. own ByT5, a token-free byte-level model.
Establishes: The fix and why it works: operating on raw bytes (no BPE) removes the
             hidden-character problem, and such models do better on spelling-
             sensitive and noisy tasks. Primary write-up of at least one fix.
Paraphrase:  ByT5 is a tokenizer-free extension of mT5 that operates directly on
             UTF-8 bytes with no subword vocabulary. Byte-level models are more
             robust to noise and perform better on tasks sensitive to spelling and
             pronunciation, at the cost of longer sequences (roughly 5x) and more
             compute.
Locators:    Abstract; the 5x sequence-length cost is corroborated by CUTE's
             Limitations section. arXiv 2105.13626 / TACL 10:291-306.
Quote:       "byte-level models are significantly more robust to noise and perform
             better on tasks that are sensitive to spelling and pronunciation."
```

```text
URL:         https://arxiv.org/abs/2112.10508
Kind:        secondary. Mielke et al. survey the field of tokenization; they report
             on BPE and its alternatives from outside the parties that invented them.
Establishes: Context - that subword tokenization (starting from BPE) is the dominant
             approach in modern NLP, and that no single tokenization is right for all
             tasks. Useful for framing, not for a contested figure.
Paraphrase:  "Between words and characters: A Brief History of Open-Vocabulary
             Modeling and Tokenization in NLP." Subword methods, beginning with BPE,
             became dominant because they keep vocabularies small while allowing fast
             inference; the authors argue there is no single best tokenization.
Locators:    Abstract. Authors incl. Mielke, Alyafeai, Salesky, Raffel, Sagot, Tan.
Quote:       "Starting with byte-pair encoding (BPE), subword-based approaches have
             become dominant in many areas".
```

```text
URL:         https://techcrunch.com/2024/08/27/why-ai-cant-spell-strawberry/
Kind:        secondary. Silberling (TechCrunch) reports the failure and quotes a
             researcher; she is outside the model-building parties.
Establishes: The concrete public instance of the failure with named models. Because
             this is a repetition, it supports that the failure was observed and
             widely reported, not that the mechanism claim is true - the mechanism
             claims are carried by the primaries above.
Paraphrase:  Asked how many r's are in "strawberry," GPT-4o and Claude both answered
             two (the correct count is three). The piece attributes this to
             tokenization: transformers see tokens, not letters. It quotes AI
             researcher Matthew Guzdial that a model has an encoding for a whole word
             but "does not know about 'T,' 'H,' 'E.'"
Locators:    Amanda Silberling, TechCrunch, Aug. 27, 2024. Guzdial quote mid-article.
Quote:       Guzdial: "When it sees the word 'the,' it has this one encoding of what
             'the' means, but it does not know about 'T,' 'H,' 'E.'"
```

## Contradictions

The commissioned angle is that tokenization causes the letter-counting failure. The
evidence supports tokenization as a real and primary cause but contradicts a claim
that it is the *only* cause. Four findings, all from primary sources, must be weighed:

1. Models can spell their tokens but still cannot manipulate them. CUTE finds high
   accuracy on the spelling and inverse-spelling tasks (write "there" as "t h e r e"
   and back) while character containment and character manipulation collapse. If the
   only problem were that characters are absent from the token, spelling would fail
   too. It does not. CUTE: models "seem to know the spelling of their tokens, yet
   fail to use this information effectively to manipulate text." So the miss is
   partly a failure to compute over characters that are, in some form, accessible -
   not purely a failure to see them. (Edman et al. 2024, Sections 5-6.)

2. The failure survives splitting the word into multiple tokens. CUTE's Appendix F
   removes examples where the tokenizer split a word and finds the accuracy change is
   at most about 3.5%, median within +/-0.5%: "even if an LLM's tokenizer splits a
   word into two or more tokens, the LLM will still have difficulty performing the
   tasks." A lesson that says "the word is one opaque token, that's the whole
   problem" overstates the case. (Edman et al. 2024, Appendix F.)

3. Character information is recoverable from the token's own vector. Kaushal &
   Mahowald show a trained probe can read out which characters a token contains, i.e.
   the representation "robustly encodes character-level information." The characters
   are not fully erased by tokenization; they are present but not reliably deployed
   during generation. (Kaushal & Mahowald 2022.)

4. Pulling toward the angle, not against it: CUTE's Appendix E shows that when a word
   is fed as random consonant strings that tokenize close to one-character-per-token
   (1.6 characters per token versus 5.4 for real words), models do the same or better
   on the character tasks. Finer tokenization helps, which is direct support that
   coarse tokenization is a genuine driver. ByT5's byte-level design and its gains on
   spelling-sensitive tasks point the same way. (Edman et al. 2024, Appendix E;
   Xue et al. 2021.)

Net for the editor: state tokenization as the mechanism, with the worked
"strawberry" split as the anchor, and mark the ground honestly. The settled part is
that BPE tokens are frequency-merged word-pieces, not letters, so character identity
is not directly indexed. The open part - flagged by CUTE and Kaushal & Mahowald and
appropriate for the series' "settled vs. open" instruction - is how much character
information a model recovers and why it can spell yet miscount. Claiming tokenization
as the sole and complete cause would go past the sources.

## Numbers

```text
Figure: "strawberry" contains 3 letter r's (positions 3, 8, 9 of s-t-r-a-w-b-e-r-r-y)
Owner:  arithmetic on the string itself
Scope:  the single English word, no leading space
```

```text
Figure: "strawberry" -> 3 tokens in cl100k_base: [496, 675, 15717] = str|aw|berry
Owner:  tiktoken 0.14.0 (cl100k_base = GPT-4, GPT-3.5-turbo)
Scope:  exact tool output this session; r's split 1 + 0 + 2 across the three pieces
```

```text
Figure: "strawberry" -> 3 tokens in o200k_base: [302, 1618, 19772] = st|raw|berry
Owner:  tiktoken 0.14.0 (o200k_base = GPT-4o, GPT-5)
Scope:  exact tool output; " strawberry" (leading space) = single token 101830
```

```text
Figure: GPT-2 tokenizer: byte-level base vocabulary 256; total vocabulary 50,257
Owner:  Radford et al. 2019, Sections 2.2-2.3
Scope:  reference Unicode-level BPE would instead need a base vocabulary >130,000;
        common BPE subword vocabularies run 32,000-64,000
```

```text
Figure: CUTE character-vs-word manipulation gap up to 72.8% (Command-R+, insertion)
Owner:  Edman et al. 2024, Section 5.3
Scope:  instruction-tuned models 7B-132B, few-shot, 1000 most frequent words >=3 chars
```

```text
Figure: CUTE semantic-similarity accuracy 76-93% across models (except Aya-8B)
Owner:  Edman et al. 2024, Section 5.2
Scope:  same model set; shows models are strong on meaning while weak on orthography
```

```text
Figure: Removing split-token examples changes CUTE accuracy <=3.5% (median +/-0.5%)
Owner:  Edman et al. 2024, Appendix F
Scope:  evidence that token-splitting is not the sole driver of the failure
```

## Source assets

```text
Asset: Gage 1994, Figure 1 - the compression walk-through of "ABABCABCD" reduced to
       "XYYD" via two pair merges, with the pair table beside it.
Shows: How BPE builds a token by repeatedly merging the most frequent adjacent pair -
       the exact operation that later produces word-pieces like "berry."
Crop:  Keep the input string, the two merge steps, and the resulting codes. The C
       hash-table and pair-table-encoding detail can be omitted; they are compression
       plumbing, not the merge idea.
```

```text
Asset: CUTE (Edman et al. 2024), Figure 2 - grouped bar charts of accuracy per task,
       each task split into word-level and character-level bars.
Shows: The core contradiction visually: tall spelling bars next to short character-
       manipulation bars, with word-level bars far above character-level bars.
Crop:  A crop of the spelling, contains, and one manipulation panel carries the point;
       the full 8-panel grid is more than the lesson needs.
```

```text
Asset: CUTE (Edman et al. 2024), Figure 1 - the table of every task with a worked
       example ("Spell out the word: there" -> "t h e r e", etc.).
Shows: Concretely what "the model can spell but not manipulate" means, in the
       benchmark's own examples.
Crop:  The spelling and one manipulation row suffice.
```

```text
Asset: The tokenization of "strawberry" itself, reproducible in OpenAI's public
       tokenizer view or via tiktoken, rendered as word -> colored pieces.
Shows: The single most load-bearing image for the lesson - the word broken into
       str|aw|berry with the r's scattered. Best built by the paper from the
       reproduction above rather than lifted from a source.
Crop:  n/a (constructed by the paper; label each piece and mark the r's).
```

```text
Asset: GPT-2 paper (Radford et al. 2019) - None found. Section 2.2 is prose with no
       tokenization figure.
```

## Discarded

```text
URL: https://joshmcdonald.medium.com/... and other Medium/HackerNoon "why AI can't
     count r's in strawberry" posts: personal blogs, no authorship stake in the
     mechanism; TechCrunch covers the same ground with a named researcher on record.
URL: https://www.runpod.io/blog/llm-tokenization-limitations and similar vendor
     blogs: marketing-adjacent secondary, superseded by the primaries and TechCrunch.
URL: https://github.com/karpathy/minbpe (lecture.md): a strong practitioner
     explainer that ties tokenization to spelling failures, but every claim it makes
     is owned by a primary already in this record (Gage, Sennrich, GPT-2); citing it
     would add a retelling, not new evidence.
URL: dl.acm.org/doi/10.5555/177910.177914 (Gage, C Users Journal, canonical DOI):
     the article of record, but it is paywalled/not openly resolvable to the text.
     The Derczynski archival PDF is recorded instead because it resolves to the full
     readable article; the DOI and original venue are named in the Gage entry so the
     provenance is clear. The paper the lesson examines is the algorithm, not this
     specific PDF, so recording the readable copy is the honest address here.
URL: WebFetch summariser's first pass on the CUTE PDF reported "character counting"
     accuracy figures (~60-75%). Discarded as fabricated: reading the full paper
     confirms CUTE has no counting task and reports none of those numbers.
```

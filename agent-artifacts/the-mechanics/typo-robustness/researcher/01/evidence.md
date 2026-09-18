# Evidence: the-mechanics/typo-robustness (round 01)

The mechanism claims hold up well against primary sources. The transformer
architecture paper and the GPT-2 paper together describe every stage of the
pipeline from raw text to predicted next token, and no stage in either
description does anything resembling spelling correction; that absence, not a
single sentence denying a spell-checker exists, is what establishes the
misconception-clearing claim, and the record says so plainly below. A live run
of OpenAI's own tokenizer (tiktoken v0.14.0, the `cl100k_base` encoding used by
GPT-3.5-turbo and GPT-4) supplies a verified, real example: "necessary" is one
token, "neccessary" is three, and neither the tool nor its owner claims a
correction step happens in between. The settled/open split the commission asks
for is real and well documented, but the boundary is fuzzier than a clean
line: research through 2025 on modern LLMs (PromptRobust; the 2025 Scientific
Reports study) finds measurable degradation from character-level prompt
perturbations even when nothing about the perturbation is imperceptible or
adversarially disguised, and one 2019 paper on subword models (Pruthi et al.)
finds that the very subword granularity that makes ordinary typos harmless
also hands a targeted attacker more precise leverage. The writer should present
"handles everyday typos well" as a strong, well-grounded claim, not an absolute
one, and should not claim any single primary source flatly states "there is no
spell-checker" — that is an inference from a complete architecture description,
and the record marks it as such throughout.

## Sources

```text
URL:         https://arxiv.org/abs/1706.03762 (Vaswani, Shazeer, Parmar, Uszkoreit,
             Jones, Gomez, Kaiser, Polosukhin, "Attention Is All You Need," NeurIPS
             2017)
Kind:        Primary. The paper that introduces the Transformer architecture GPT-2
             and its successors are built on; it owns the claim about what the
             architecture does and does not contain.
Establishes: The full pipeline from token embeddings to predicted next-token
             probabilities: input embeddings + positional encoding -> stacked
             self-attention and feed-forward sub-layers -> a single linear
             transformation and softmax over the vocabulary to produce next-token
             probabilities (Sec. 3.4). The decoder is auto-regressive: masked
             self-attention lets each position attend only to earlier positions,
             and predictions for position i depend only on known outputs before
             it (Sec. 3.1). No sub-layer, stage, or module in this description
             does anything but attend over context and transform vectors; nothing
             corrects, normalizes, or looks up "intended" spellings.
Paraphrase:  The complete, peer-published description of the architecture GPT
             models use contains: embed tokens, add position information, run
             attention and feed-forward blocks, and project to a probability
             distribution over the next token. There is no other kind of stage.
Locators:    Sec. 3 ("Model Architecture"), Sec. 3.1 ("Encoder and Decoder
             Stacks"), Sec. 3.4 ("Embeddings and Softmax").
Quote:       "We also use the usual learned linear transformation and softmax
             function to convert the decoder output to predicted next-token
             probabilities." (Sec. 3.4) "This masking, combined with fact that
             the output embeddings are offset by one position, ensures that the
             predictions for position i can depend only on the known outputs at
             positions less than i." (Sec. 3.1)
```

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
             (Radford, Wu, Child, Luan, Amodei, Sutskever, "Language Models are
             Unsupervised Multitask Learners," OpenAI, 2019 — the GPT-2 paper,
             hosted at OpenAI's own release location)
Kind:        Primary. OpenAI's own paper describing GPT-2's input representation
             and architecture; it owns the claim about how GPT-family models
             turn text into tokens.
Establishes: Byte-level BPE as GPT-2's tokenization scheme, and why: character-
             level BPE over Unicode code points would need a base vocabulary of
             130,000+ symbols before any merges; restricting to raw UTF-8 bytes
             needs only 256. This guarantees every possible string is
             representable without an unknown/out-of-vocabulary token, because
             any byte sequence can always fall back to individual bytes. GPT-2's
             actual vocabulary after merges is 50,257 tokens (Table 2, read
             against the text). The section describes tokenization purely as
             this byte-merging procedure; it never mentions correcting,
             normalizing, or checking spelling, and elsewhere the paper treats
             *avoiding* "lossy pre-processing" as a stated design goal, the
             opposite of a correction stage.
Paraphrase:  GPT-2 tokenizes by starting from the 256 possible byte values and
             merging frequent byte pairs. Because the starting alphabet is
             already complete (every string is bytes), there is never a need to
             substitute an unrecognized or "corrected" word — the worst case is
             that a string breaks into more, smaller pieces, all the way down to
             single bytes.
Locators:    Sec. 2.2 ("Input Representation"); Sec. 2.3 ("Model") and Table 2
             for vocabulary size 50,257; Sec. 2.1 for the "lossy pre-processing"
             framing.
Quote:       "In contrast, a byte-level version of BPE only requires a base
             vocabulary of size 256." "Since our approach can assign a
             probability to any Unicode string, this allows us to evaluate our
             LMs on any dataset regardless of pre-processing, tokenization, or
             vocab size." "The vocabulary is expanded to 50,257." "Current large
             scale LMs include pre-processing steps such as lower-casing,
             tokenization, and out-of-vocabulary tokens which restrict the space
             of model-able strings" (cited as a limitation GPT-2's approach
             avoids, not a step it adds).
```

```text
URL:         https://aclanthology.org/P16-1162/ (Sennrich, Haddow, Birch, "Neural
             Machine Translation of Rare Words with Subword Units," ACL 2016;
             PDF at https://aclanthology.org/P16-1162.pdf)
Kind:        Primary. The paper that introduces BPE as a text-segmentation
             algorithm for neural sequence models; it owns the mechanism claim
             the commission asks to teach.
Establishes: The BPE algorithm itself, exactly: start from a vocabulary of
             individual characters, count all adjacent symbol pairs in the
             training corpus, and repeatedly merge the single most frequent pair
             into a new symbol, for a fixed, chosen number of merges. At
             application (test) time, an input word is split into characters
             and the learned merges are replayed to rebuild it into the largest
             known chunks. A rare or misspelled word that never appeared as a
             whole simply gets split into more, smaller learned pieces instead
             of one whole-word piece. Figure 1 gives a fully worked toy example
             of merges learned from {"low", "lowest", "newer", "wider"}.
Paraphrase:  Subword tokenization is a fixed table of merge rules learned once
             from frequency counts, then applied mechanically and identically to
             any input at inference time. It has no concept of "correct"
             spelling; it just repeatedly glues together whatever character (or
             sub-token) pairs were most frequent in training.
Locators:    Sec. 3.2 ("Byte Pair Encoding (BPE)"); Figure 1 (toy merge example);
             footnote 3 on out-of-vocabulary symbols at test time.
Quote:       "We iteratively count all symbol pairs and replace each occurrence
             of the most frequent pair ('A', 'B') with a new symbol 'AB'." "At
             test time, we first split words into sequences of characters, then
             apply the learned operations to merge the characters into larger,
             known symbols. This is applicable to any word, and allows for
             open-vocabulary networks with fixed symbol vocabularies."
```

```text
URL:         https://github.com/openai/tiktoken (repository; the two encodings
             cited are `cl100k_base` and `gpt2`) and a live run of tiktoken
             v0.14.0 (`pip install tiktoken==0.14.0`, Python 3.11, run on
             2026-09-18) recorded in full below
Kind:        Primary. tiktoken is OpenAI's own reference tokenizer
             implementation for its GPT models; a run of it against real strings
             is a direct, reproducible artifact of what the tokenizer actually
             does, not a report about it. Brief explicitly authorizes a "live
             tokenizer's actual output... if recorded with the tool and
             version."
Establishes: A concrete, verified case of a correctly spelled common word
             encoding as a single token while its misspelling encodes as a
             longer sequence of smaller tokens, exactly the shape the commission
             asks for. Also establishes the byte-level fallback in practice: an
             emoji not covered by any merge decomposes into its raw UTF-8 bytes,
             one to two bytes per token, with no failure and no substitution.
Paraphrase:  Running the actual GPT-3.5/GPT-4 tokenizer on a matched pair of
             correct/misspelled words shows the token-count and token-identity
             difference directly, with exact IDs and decoded byte strings.
Locators:    Direct tool output, encoding `cl100k_base`, tiktoken 0.14.0 (latest
             released version as of 2026-09-18, confirmed via `pip index
             versions tiktoken`).
Quote:       |
             'necessary'  -> 1 token:  [95317]                    -> ['necessary']
             'neccessary' -> 3 tokens: [818, 1346, 661]            -> ['ne', 'ccess', 'ary']
             'beautiful'  -> 1 token:  [88044]                    -> ['beautiful']
             'beautifull' -> 4 tokens: [1395, 2784, 333, 620]      -> ['be', 'aut', 'if', 'ull']
             'definitely' -> 2 tokens: [755, 7627]                 -> ['def', 'initely']
             'definately' -> 3 tokens: [755, 258, 2718]            -> ['def', 'in', 'ately']
             'receive'    -> 1 token:  [42993]                    -> ['receive']
             'recieve'    -> 2 tokens: [2827, 19704]               -> ['rec', 'ieve']
             '🤖' (byte-level fallback, no learned merge covers it)
                          -> 3 tokens: [9468, 97, 244]
                          -> raw bytes: b'\xf0\x9f', b'\xa4', b'\x96'
                          (these three tokens concatenate to the emoji's 4-byte
                          UTF-8 encoding; nothing here is a whole "known" token)
             cl100k_base total vocabulary size: 100,277 tokens (`enc.n_vocab`).
```

```text
URL:         https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
             (OpenAI's own cookbook of example code)
Kind:        Primary. OpenAI's own documentation of which tokenizer encoding
             backs which of its models.
Establishes: `cl100k_base` is the encoding used by `gpt-4`, `gpt-4-turbo`,
             `gpt-3.5-turbo`, and OpenAI's embedding models; `o200k_base` backs
             `gpt-4o` and `gpt-4o-mini`; `r50k_base`/`gpt2` backs the original
             GPT-3 `davinci` family. This is what licenses citing the tiktoken
             run above as representative of "the GPT-3.5/GPT-4 tokenizer"
             specifically, not just "a tokenizer."
Paraphrase:  The mapping from model name to tokenizer/vocabulary is fixed and
             documented by OpenAI itself, not inferred.
Locators:    Notebook cells listing encodings and their associated model names;
             example tokenization of "tiktoken is great!" walked step by step.
Quote:       Encoding-to-model table: `o200k_base` -> gpt-4o, gpt-4o-mini;
             `cl100k_base` -> gpt-4-turbo, gpt-4, gpt-3.5-turbo, text-embedding
             models; `p50k_base` -> Codex models, text-davinci-002/003;
             `r50k_base` (`gpt2`) -> GPT-3 models such as davinci.
```

```text
URL:         https://arxiv.org/abs/1711.02173 (Belinkov, Bisk, "Synthetic and
             Natural Noise Both Break Neural Machine Translation," ICLR 2018)
Kind:        Primary robustness research. The authors ran these experiments and
             own the finding.
Establishes: The paper's own vocabulary for exactly the distinction the
             commission wants marked: "synthetic" noise (random character
             swaps, random permutation of letters within a word) versus
             "natural" noise (real human errors drawn from error corpora).
             Crucially for the everyday/edge line: even *natural* human errors
             degrade the character-level and subword (BPE-based Nematus) NMT
             systems tested here substantially once error rates rise, not just
             synthetic scrambling — this is a genuine complication, recorded in
             Contradictions below. The paper is explicit that humans stay robust
             to this kind of noise while these 2017-era translation models do
             not, and that models are never explicitly trained to expect
             typos — "we instead hope that the relevant noise will occur in the
             training data" — which is the closest any source comes to a direct
             statement that there is no dedicated correction step: robustness,
             where it exists, is an emergent property of what appeared during
             training, not a designed defense.
Paraphrase:  Whatever robustness a subword or character-based model has to
             typos comes from what its training data happened to contain, not
             from any built-in spelling stage. That mechanism is real, but for
             the systems this paper tests, it is incomplete: natural typos still
             hurt performance measurably, especially as their rate increases.
Locators:    Abstract; Sec. 1 (Introduction); Sec. 3 ("MT Systems") for the
             Nematus BPE model description; Figure 1 and its caption for the
             clean-baseline BLEU (34.22, German-to-English, Nematus, 0% words
             changed) referenced in Numbers below.
Quote:       "We find that state-of-the-art models fail to translate even
             moderately noisy texts that humans have no trouble comprehending."
             "While typos and noise are not new to NLP, our systems are rarely
             trained to explicitly address them, as we instead hope that the
             relevant noise will occur in the training data." "The important
             thing to note is that even small amounts of noise lead to
             substantial drops in performance."
```

```text
URL:         https://aclanthology.org/P19-1561/ (Pruthi, Dhingra, Lipton,
             "Combating Adversarial Misspellings with Robust Word Recognition,"
             ACL 2019; PDF at https://aclanthology.org/P19-1561.pdf)
Kind:        Primary robustness research. The authors ran these attacks and own
             the resulting numbers.
Establishes: A single, deliberately chosen character-level edit (add, drop, or
             swap one internal character) can collapse a fine-tuned BERT
             sentiment classifier's accuracy. The paper reports this two ways in
             two different places, worth keeping distinct rather than
             conflating: the abstract's headline figure is a drop from 90.3% to
             45.8% accuracy from "a single adversarially-chosen character
             attack"; the body separately reports a *swap*-only 1-character
             attack degrading the same 90.3%-accuracy model to 64.1%, restorable
             only to 69.2% by adversarial training (their own word-recognition
             defense restores swap/drop/add attacks to 88.3/81.1/78.0%
             respectively). Both numbers describe adversarially *searched*
             single-character edits chosen to do maximum damage, not a random
             typo a person would actually type. Also directly relevant to the
             mechanism claim: word-piece (subword) and character-level models
             turned out *more* vulnerable to this kind of targeted attack than
             plain word-level models, because each character edit produces a
             genuinely distinct input for a subword tokenizer to chew on, giving
             an adversary more precise control — the flip side of subwords
             degrading gracefully on ordinary typos.
Paraphrase:  A single, worst-case, algorithm-chosen character edit is far more
             damaging than an ordinary spontaneous typo, and subword/word-piece
             tokenization's flexibility that helps with ordinary typos is
             exactly what an adversary exploits when the edit is chosen
             deliberately rather than randomly.
Locators:    Abstract; Sec. 1 (Introduction), "Second, we evaluate first-line
             techniques..." paragraph; Table 1 (worked example of a single
             swap/drop breaking sentiment classification of "A triumph,
             relentless and beautiful in its downbeat darkness").
Quote:       "Against a BERT model fine-tuned for sentiment analysis, a single
             adversarially-chosen character attack lowers accuracy from 90.3%
             to 45.8%. Our defense restores accuracy to 75%." "[A] BERT model
             achieving 90.3 accuracy on a sentiment classification task, is
             degraded to 64.1 by an adversarially-chosen 1-character swap in the
             sentence, which can only be restored to 69.2 by adversarial
             training." "[C]haracter and word-piece models are in fact more
             vulnerable [than word-level models]... each character-level add,
             drop, or swap produces a distinct input, providing the adversary
             with a greater set of options."
```

```text
URL:         https://arxiv.org/abs/2106.09898 (Boucher, Shumailov, Anderson,
             Papernot, "Bad Characters: Imperceptible NLP Attacks," IEEE
             Symposium on Security and Privacy, 2022)
Kind:        Primary. The authors devised and ran these attacks; they own the
             finding.
Establishes: The open adversarial edge the commission wants marked, precisely:
             homoglyphs (a Cyrillic "а" standing in for a Latin "a"), invisible
             Unicode characters (zero-width joiners/non-joiners, bidirectional
             override characters), reorderings, and deletions at the encoding
             level, none of which change what a human reader sees, but which
             change what bytes the tokenizer actually receives. A single such
             injection can significantly degrade a target system; three can
             functionally break many of the systems tested (machine
             translation, toxic-content detection, textual entailment). This is
             categorically different from a natural typo: it is invisible to
             the person reading the text, not just unusual-looking, and it
             targets the tokenizer/encoding layer directly rather than
             producing a spelling variant a human would also notice.
Paraphrase:  Ordinary typos are visible, unintentional character-level
             deviations from a training-data-covered distribution. This class
             of attack is a deliberately engineered exploit against how text
             gets encoded into bytes before tokenization, invisible to a human,
             and is a different problem from typo robustness even though both
             ultimately act on the tokenizer.
Locators:    Abstract; Sec. I (Introduction), the PayPal/Google Translate
             homoglyph example; Table I ("Imperceptible Perturbations in
             Various NLP Tasks").
Quote:       "[W]ith a single imperceptible encoding injection – representing
             one invisible character, homoglyph, reordering, or deletion – an
             attacker can significantly reduce the performance of vulnerable
             models, and with three injections most models can be functionally
             broken." "Do x and х look the same to you? They may look identical
             to humans, but not to most natural-language processing systems."
```

```text
URL:         https://arxiv.org/abs/2306.04528 (Zhu, Wang, Zhou, Wang, Chen,
             Wang, Yang, Ye, Gong, Zhang, Xie, "PromptRobust: Towards Evaluating
             the Robustness of Large Language Models on Adversarial Prompts,"
             Microsoft Research et al., 2023)
Kind:        Primary robustness research on modern LLMs specifically, including
             GPT-3.5 (ChatGPT) and GPT-4. The authors ran the benchmark and own
             the numbers.
Establishes: Even in 2023-era instruction-following LLMs, deliberately searched
             character-level edits to a reusable task prompt (via TextBugger and
             DeepWordBug, black-box search algorithms that try many candidate
             edits and keep the most damaging) produce an average 20%
             performance drop across the 13 datasets and 9 models tested
             (word-level synonym attacks are worse, at 33%; sentence-level
             attacks are weaker). GPT-4 and one other model (Flan-UL2) were the
             most robust of the 9 models tested. This is a real complication for
             any claim that character-level robustness is fully "settled" even
             for today's frontier chat models — but the paper's own framing
             blurs the everyday/adversarial line the commission wants kept
             separate: it explicitly designs these attacks to double as
             "mimicking plausible user errors like typos" *and* as adversarial
             search, and it attacks the reusable instruction prompt (which
             affects every subsequent user turn) rather than one person's one
             typed message. Table 5 gives a concrete worked failure: the
             DeepWordBug-perturbed prompt "Servign as a sentimBnt envaluation
             model, Qetermine if the Iiven statemen is..." produces no usable
             response where the clean version correctly classified the review
             as negative.
Paraphrase:  Character-level perturbations that are optimized to be damaging,
             not simply typed by an ordinary distracted user, still measurably
             hurt even GPT-4-class models, though less than word-level
             synonym swaps and less than they hurt weaker models. This
             qualifies "the everyday case is settled" to mean settled for
             unoptimized, spontaneous human error, not for any character-level
             deviation whatsoever.
Locators:    Abstract; Sec. 1 (Introduction); Sec. 2.2 ("Attacks," definition of
             character-level attacks via TextBugger/DeepWordBug); Sec. 4.1
             ("Analysis on attacks," the 33%/20% figures) and "Analysis on
             LLMs" (GPT-4/UL2 as most robust); Table 5 (worked failure example).
Quote:       "Our findings demonstrate that LLMs are not robust to adversarial
             prompts." "[W]ord-level attacks prov[e] the most potent, leading to
             an average performance decline of 33% across all datasets.
             Character-level attacks rank second, inducing a 20% performance
             drop in most datasets." "GPT-4 and UL2 significantly outperform
             other models in terms of robustness." "[W]e call such a perturbed
             prompt in both scenarios adversarial prompt" (both the
             typo-mimicking and the adversarially-crafted scenario).
```

```text
URL:         https://www.nature.com/articles/s41598-025-29770-0 (Alahmari,
             "Large language models robustness against perturbation," Scientific
             Reports, 2025)
Kind:        Primary robustness research on current models (GPT-4o, LLaMA3.3-70B,
             and four others). The author ran these experiments and owns the
             numbers.
Establishes: Even the newest tested models show measurable output divergence
             under synthetic keyboard-adjacent-key typo perturbation of prompts
             in a text-generation task. This is genuinely recent evidence for
             the "how far does robustness extend" open question, but the
             metric needs a careful caveat, recorded honestly here rather than
             overstated: the reported "BLEU" score is not accuracy or
             correctness against a ground truth. It is n-gram overlap between
             the model's own response to the perturbed prompt and its own
             response to the clean prompt — a wording-consistency measure. A
             low score means the model phrased its answer differently under a
             typo-perturbed prompt, which is consistent with the model still
             answering correctly but stating it in different words; the paper
             does not test or claim comprehension failure, and does not report
             a comparison against a natural (non-synthetic), single-typo
             condition. It also does not distinguish natural from adversarial
             perturbation; both its "typo" and "word replacement" conditions
             are synthetically generated by the TextFlint library at an
             unspecified rate ("randomly replaces characters").
Paraphrase:  Modern frontier and near-frontier LLMs do not produce identically
             worded output when a prompt is typo-perturbed versus clean, and
             the authors attribute this to different subword fragmentation of
             the misspelled tokens. That is consistent with the tokenization
             mechanism taught in this lesson; it is not evidence that the
             misspelling was misunderstood.
Locators:    Abstract; Methods (BLEU metric definition, keyboard-typo
             perturbation definition, TextFlint); Results (Amazon Reviews
             dataset scores for GPT-4o and LLaMA3.3-70B).
Quote:       "LLMs are primarily trained on curated datasets that lack
             human-induced errors, such as typos or variations in word choice."
             "It measures the overlap of n-grams between the generated LLM
             response of the original prompt and the LLM response of the
             perturbed prompt." "The keyboard typo perturbation randomly
             replaces characters in words with those on adjacent keys, often
             leading to malformed or misspelled tokens." "The results indicate
             that LLMs are sensitive to text perturbations, leading to
             variations in generated outputs."
```

```text
URL:         https://huggingface.co/learn/llm-course/en/chapter6/5 ("Byte-Pair
             Encoding tokenization," Hugging Face LLM Course)
Kind:        Secondary. Hugging Face did not invent BPE or GPT-2's byte-level
             variant; this chapter reports on and re-teaches Sennrich et al.'s
             and Radford et al.'s work for its own course, with no independent
             stake in the underlying research claim.
Establishes: Nothing not already established by the two primary papers above.
             Used only as confirmation that an independent, technically careful
             third party describes the mechanism the same way: BPE started as
             a compression algorithm, GPT/GPT-2 use it for tokenization, and
             GPT-2's byte-level trick trades a 130,000+-symbol Unicode
             vocabulary for a 256-byte one so nothing is ever unrepresentable.
             Its own fully worked toy merge example (on the corpus "hug", "pug",
             "pun", "bun", "hugs") independently reproduces the same merge
             mechanics as Sennrich et al.'s Figure 1, from a different starting
             corpus.
Paraphrase:  A widely used third-party teaching resource explains BPE and
             byte-level BPE consistently with the original papers, which is
             corroboration, not new evidence.
Locators:    Sections "Byte-Pair Encoding" (history/attribution) and the toy
             training-example walkthrough later in the same chapter.
Quote:       "Byte-Pair Encoding (BPE) was initially developed as an algorithm
             to compress texts, and then used by OpenAI for tokenization when
             pretraining the GPT model." "[T]hey don't look at words as being
             written with Unicode characters, but with bytes. This way the base
             vocabulary has a small size (256), but every character you can
             think of will still be included."
```

## Contradictions

- **Natural noise is not free of cost, even where the mechanism is "settled."**
  Belinkov & Bisk (2018) show real human-error noise, not just synthetic
  scrambling, measurably degrades the character- and subword-level NMT systems
  they test as error rates rise. This is 2017-era translation models scored on
  BLEU, not modern chat LLMs, so it does not transfer directly to "the chatbot
  understands your typo" — but it means the researcher cannot let the writer
  claim natural-typo robustness is total or free, only that it is real and
  well-explained by training-data coverage.
- **Modern LLMs are not perfectly robust to character-level prompt
  perturbation either.** PromptRobust (2023) finds a 20% average performance
  drop from character-level attacks across GPT-3.5, GPT-4, and seven other
  models, second only to word-level synonym attacks (33%). The 2025 Scientific
  Reports study finds measurable output divergence in GPT-4o and LLaMA3.3-70B
  under synthetic keyboard-typo prompts. Both complicate a flat "the everyday
  case is settled" claim for *any* character-level deviation. Both also blur
  the commission's clean settled/adversarial line: PromptRobust's own
  character-level attacks are explicitly built to "mimic plausible user
  errors" *and* are chosen by an adversarial search algorithm, and neither
  paper isolates "one ordinary, single, unoptimized human typo" as its own
  condition. The record's own framing should say the everyday case is well
  explained and generally robust in practice, not that it is proven immune —
  and that these two papers measure *worst-case-selected* or *synthetic*
  character noise, not the typical single misspelling a distracted person
  actually types.
- **Subword flexibility cuts both ways.** Pruthi et al. (2019) find word-piece
  and character-level models are *more* vulnerable than word-level models to a
  single, deliberately chosen character edit, precisely because each edit
  produces a distinct token sequence for an adversary to exploit. This is the
  same mechanical fact (subwords respond to any character change) that
  explains graceful degradation on ordinary typos. The lesson's account of
  "why the pieces still carry meaning" should not imply subword tokenization
  is simply protective; it is a double-edged mechanism, protective against
  unoptimized noise and exploitable against optimized noise.
- No source disputes that BPE/byte-level BPE is the correct account of GPT
  tokenization, and no source claims any spell-correction module exists
  anywhere in the documented architecture or pipeline.

## Numbers

```text
Figure: 256 (base vocabulary size, byte-level BPE)
Owner:  Radford et al. 2019 (GPT-2 paper), Sec. 2.2
Scope:  The number of possible raw byte values; the starting alphabet before
        any merges are learned. Contrasted in the same section with 130,000+,
        the size a Unicode-code-point base vocabulary would need.
```

```text
Figure: 50,257 (GPT-2's final token vocabulary size)
Owner:  Radford et al. 2019, Sec. 2.3 / Table 2
Scope:  All four GPT-2 model sizes share this vocabulary; it is after merges,
        not the 256-byte starting point.
```

```text
Figure: 100,277 (cl100k_base total vocabulary size)
Owner:  tiktoken v0.14.0, `cl100k_base` encoding, queried directly
        (`enc.n_vocab`)
Scope:  This is the encoding used by gpt-3.5-turbo, gpt-4, gpt-4-turbo, and
        OpenAI's embedding models per the OpenAI Cookbook mapping above; it is
        specific to tiktoken 0.14.0's shipped `cl100k_base.tiktoken` file.
```

```text
Figure: "necessary" = 1 token; "neccessary" = 3 tokens ("ne", "ccess", "ary")
Owner:  Live tiktoken v0.14.0 run, `cl100k_base` encoding, this record
Scope:  A single word pair, English, cl100k_base only; other encodings (gpt2,
        o200k_base) split the same pair differently in token count (verified:
        gpt2 also gives 1 vs. 3; o200k_base also gives 1 vs. 3), and the
        correctly spelled word is not guaranteed to be a single token in every
        encoding (e.g., "beautiful" is 2 tokens under the older `gpt2`
        encoding, 1 token under cl100k_base and o200k_base) — the single-token
        vs. multi-token contrast is a real and reproducible property of a
        specific encoding, not a universal law of all tokenizers.
```

```text
Figure: 90.3% -> 45.8% (accuracy) / 90.3% -> 64.1% (accuracy, a different
        reported condition)
Owner:  Pruthi, Dhingra, Lipton 2019
Scope:  A single fine-tuned BERT sentiment classifier, a single dataset (movie
        reviews), a single adversarially-*searched* character edit chosen to
        maximize damage — not a spontaneous human typo, and not directly about
        an instruction-following chat model. The paper states both figures in
        different places for what appear to be different attack conditions
        (see the Sources entry's Quote field for both exact sentences); do not
        collapse them into one number without checking which condition the
        claim needs.
```

```text
Figure: 20% average performance drop (character-level prompt attacks); 33%
        (word-level)
Owner:  Zhu et al. 2023 (PromptRobust)
Scope:  Average across 9 LLMs (including ChatGPT and GPT-4) and 13 datasets/
        tasks; the perturbed unit is a reusable task-instruction prompt, not a
        one-off user message; the character-level edits are algorithm-searched
        (TextBugger, DeepWordBug), not literally random single typos.
```

```text
Figure: 34.22 BLEU (clean baseline)
Owner:  Belinkov & Bisk 2018, Figure 1
Scope:  Nematus (a BPE-based NMT system), German-to-English, TED talks corpus
        (IWSLT 2016), 0% of words perturbed. Cited only to anchor how much
        noise "small amounts" refers to in the paper's own framing; the
        noise-condition BLEU values were extracted from an embedded chart image
        and are not reproduced here with confidence in their exact digit-level
        accuracy — cite the qualitative finding, not specific noisy-BLEU
        figures, unless re-verified against the rendered chart directly.
```

## Source assets

```text
Asset: Sennrich et al. 2016, Figure 1 — toy table of BPE merge operations
       learned from {"low", "lowest", "newer", "wider"}, showing each merge
       step and the resulting symbol.
Shows: The mechanical, step-by-step nature of BPE merging in the smallest
       possible worked example — useful if the piece wants a from-scratch
       illustration of "how the merge table gets built" before showing a real
       tokenizer's output.
Crop:  Keep the full merge sequence (all listed steps) together; it is only a
       few rows and loses its point if truncated.
```

```text
Asset: Vaswani et al. 2017, Figure 1 — the full Transformer architecture block
       diagram (encoder and decoder stacks, attention, feed-forward, embeddings
       and softmax output).
Shows: Every stage in the pipeline in one picture, which a reader can scan to
       verify for themselves that no block does anything resembling spell
       correction.
Crop:  If used at all, use the whole diagram; a partial crop would misrepresent
       "here is everything that happens" as "here is a portion of what
       happens."
```

```text
Asset: The tiktoken example table produced for this record (see the Sources
       entry above): correct-spelling vs. misspelling token counts and pieces
       for four word pairs, plus the emoji byte-fallback example.
Shows: The single concrete fact the commission most wants visualized: same
       word, one spelling one token, a different spelling several smaller
       tokens, in the actual tokenizer used by GPT-3.5/GPT-4.
Crop:  A small table is sufficient per the commission's own boundary (no code);
       keep at least one full word pair with its exact token pieces, not just
       token counts, or the "still recognizable pieces" point is lost.
```

```text
Asset: Boucher et al. 2022, Table I — "Imperceptible Perturbations in Various
       NLP Tasks," showing input rendering next to input encoding for several
       real attacked examples (e.g., the account-number reordering, the
       toxic-content example).
Shows: Concretely what makes this class of attack different from a typo: what
       a human reads versus the actual bytes/characters received, side by
       side.
Crop:  A single row (e.g., the toxic-content or NLI row, which includes the
       before/after output) makes the point without needing the whole table;
       do not crop out the "Input Rendering" column, since the entire point is
       the mismatch between what is shown and what is encoded.
```

```text
Asset: PromptRobust (Zhu et al. 2023), Table 5 — a real perturbed prompt
       ("Servign as a sentimBnt envaluation model, Qetermine if the Iiven
       statemen is...") next to its clean original, with the resulting
       (mis)classification.
Shows: A genuine, character-level adversarial edit to a chat-style prompt that
       breaks a real evaluated response, useful for the adversarial-edge
       section as an example categorically different from an ordinary typo.
Crop:  Keep the prompt-and-sample pair together with the recorded outcome
       (N/A); the outcome is what makes the example load-bearing.
```

## Discarded

```text
URL: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
     — Gated: returned HTTP 403 to WebFetch and again to a direct curl request
     with a standard browser user agent (Zendesk/Intercom bot protection, not a
     dead link). Not opened, so nothing from it is cited above. The claim it
     would have supported (tokenization example, no correction step mentioned)
     is independently covered by the tiktoken live run and the OpenAI Cookbook
     notebook, both of which were opened and read directly.
```

```text
URL: https://platform.openai.com/docs/guides/text — Redirected
     (301 -> https://developers.openai.com/api/docs/guides/text). The redirect
     target was not fetched, because the architecture/no-correction-stage claim
     was already solidly established from the two foundational architecture
     papers (Vaswani et al.; Radford et al.) before this was attempted; pursuing
     it further would have been padding, not verification.
```

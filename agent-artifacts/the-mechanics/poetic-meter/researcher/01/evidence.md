# Evidence: the-mechanics/poetic-meter (01)

The evidence supports every link in the commissioned chain, with one link needing
a softer claim than the brief's wording. Firsthand measurement exists for each
step: byte-pair tokenization segments text by co-occurrence frequency, not sound
(Sennrich et al.); English spelling is a weak guide to pronunciation, so even a
purpose-built grapheme-to-phoneme tool tops out near 62% on English
(PhonologyBench, Wikipedia orthographic depth); models score far below humans on
syllable counting (a 45-point gap) while scoring much closer on rhyme (a 17-point
gap) (PhonologyBench); and the rhyme half is partly planned ahead, shown by
attribution graphs and confirmed by causal injection (Anthropic, *Biology of a
Large Language Model*). Two mechanism papers ground the tokenization step
directly: giving a model character-level input raises rhyming and syllable
performance (Liao & Shi; Chen et al.'s character-level ByGPT5). The one place the
brief overreaches: the strong claim that "there is no phonological representation
the decoder consults" is complicated by probing work showing phoneme identity is
recoverable from token embeddings at ~96% for single-token words (McLaughlin et
al.). Sound is latently present; it is just not reliably deployed for exact
counting. The record is thin on one thing the brief names: direct measurement of
stress-based metrical scansion (iambic feet) in modern chat-model output. Syllable
counting is measured well; foot-and-stress meter is measured mostly by proxy.

## Sources

```text
URL:         https://aclanthology.org/P16-1162/
Kind:        primary — the paper that introduced BPE subword segmentation to
             neural language models; it owns the method the chain's first step
             rests on. (Also on arXiv as 1508.07909.)
Establishes: A language model reads sub-word tokens produced by merging the most
             frequent adjacent unit pairs, starting from characters, until a
             target vocabulary size is reached. The units are chosen by
             co-occurrence frequency in the training text. Nothing in the
             procedure references phonemes, syllables, or stress.
Paraphrase:  BPE begins with the character set and iteratively merges the two
             units that co-occur most often, stopping at the chosen vocabulary
             size; frequent words stay whole, rare words split into several
             sub-word pieces. It is a frequency-driven text-compression method
             (Gage 1994) adapted to word segmentation, not a linguistic one.
Locators:    Title "Neural Machine Translation of Rare Words with Subword
             Units," Sennrich, Haddow & Birch, ACL 2016, pp. 1715–1725; method
             in the "Byte Pair Encoding (BPE)" section.
Quote:       (method, paraphrased) "Byte pair encoding ... initializes the set of
             available subword units with the character set ... Each merge
             combines the two units with the highest number of co-occurrences."
```

```text
URL:         https://arxiv.org/abs/2404.02456
Kind:        primary — the benchmark study; it owns the syllable/rhyme/G2P
             measurements firsthand.
Establishes: With numbers, that LLMs are far below humans at syllable counting
             and much closer at rhyme; that whole-word tokens beat split tokens
             on grapheme-to-phoneme; and the authors' own read that subword
             tokenization loses phonological information.
Paraphrase:  Three diagnostic tasks (grapheme-to-phoneme, syllable counting,
             rhyme-word generation) test English phonological skill in text-only
             LLMs. Humans beat the models by 45% on syllable counting and 17% on
             rhyme generation. Model performance drops as sentence complexity
             rises, and whole-word tokens yield higher G2P accuracy than
             split-word tokens. The authors conclude the models lean on textual
             "side evidence" rather than phonological reasoning, and that subword
             tokenization may cost them phonological information.
Locators:    Abstract (headline 17%/45% gaps); Syllable Counting table
             (overall/simple/complex); Rhyme Word Generation table (common/rare/
             overall); G2P table (high-/low-frequency); tokenization discussion
             in the analysis section. Data: G2P 3,000 words (SIGMORPHON 2021,
             American English); syllable 1,000 sentences (Romance Books + Reddit
             Short Stories); rhyme 300 words (Spelling Bee list + Google
             1-Trillion corpus, references from WordHippo).
Quote:       "Subword tokenization may lead to loss of phonological information
             that eventually affects the phonological skills of LLMs." And, on
             mechanism, the models are "accomplishing phonology-rich tasks by
             utilizing side evidence from the training data instead of
             phonological concepts and reasoning as humans do."
```

```text
URL:         https://transformer-circuits.pub/2025/attribution-graphs/biology.html
Kind:        primary — Anthropic's own interpretability report; it owns the
             rhyme-planning finding firsthand.
Establishes: That the model activates candidate end-of-line rhyme words before
             writing the line, and composes the line toward the chosen word;
             confirmed causally by suppression and injection.
Paraphrase:  Studying Claude 3.5 Haiku on a rhyming couplet ("He saw a carrot and
             had to grab it, / His hunger was like a starving rabbit"),
             attribution graphs show features for candidate final words such as
             "rabbit" and "habit" active at the newline, before the second line
             is written. Suppressing or injecting a planned-word feature makes
             the model rewrite the line to land on a different final word. The
             model works backward from the planned target to a sentence that
             ends there. This is the mechanism the commission points to for the
             rhyme half; the section does not analyze meter or syllable count.
Locators:    "Planning in Poems" section. Model: Claude 3.5 Haiku (Oct 2024).
             Injection result reported below under Numbers.
Quote:       The model shows "features corresponding to candidate end-of-next-line
             words prior to writing the line, and makes use of these features to
             decide how to compose the line," and "works backward from its target
             word to write a sentence that naturally ends in that word."
```

```text
URL:         https://arxiv.org/abs/2508.02527
Kind:        primary — probing study; it owns the embedding-recoverability
             measurements firsthand. This is the contradiction to the brief's
             strongest wording.
Establishes: That phoneme identity is substantially recoverable from token
             embeddings, so phonological structure is latently present in the
             representation, not absent; and that this latent structure causally
             drives rhyming when manipulated.
Paraphrase:  In Llama-3.2-1B-Instruct, a linear probe predicts which phonemes a
             single-token word contains for ~96% of such words, against ~42% for
             random-embedding controls, showing recoverable phonetic content in
             the embedding matrix. Steering the embedding along a vowel direction
             switches the model's rhymes to the target vowel, so this latent
             phonetics causally supports rhyming. The authors state their maps do
             not amount to a complete account of the model's phonetic
             representation, and they do not quantify stress or syllables.
Locators:    Title "I Have No Mouth, and I Must Rhyme: Uncovering Internal
             Phonetic Representations in LLaMA 3.2," McLaughlin, Khurana &
             Merullo (Brown University), arXiv 2508.02527v2, Oct 2025. Probe
             accuracy in the phoneme-probing section; causal vowel-steering in
             the intervention section; scope caveat near Figure 5.
Quote:       (scope) "the representations in Figure 5 do not necessarily
             constitute a comprehensive account of Llama's internal
             representations of phonetic information."
```

```text
URL:         https://arxiv.org/abs/2406.15267
Kind:        primary — evaluation study; it owns the poetry-diversity and
             form-adherence measurements firsthand.
Establishes: That subword/word-level LLMs under-rhyme and mismatch human formal
             structure, while character-level models (which see letters) match
             rhyme and length far better. Direct support for the tokenization
             mechanism.
Paraphrase:  Measuring generated poems against human distributions, word-level
             LLMs (GPT-2, GPT-Neo, LLaMA2, LLaMA3) produce far too many
             non-rhyming (ABCD) quatrains and miss human length distributions;
             character-level ByGPT5 aligns best on both rhyme and length. Human
             quatrains rhyme most of the time (ABAB/AABB/ABCB dominate; under
             ~15% are ABCD). Style-conditioning helps; unconditioned LLMs are
             worst. Grounds "rhyme is frequent in the (poetry) training
             distribution" and "seeing characters helps."
Locators:    Title "Evaluating Diversity in Automatic Poetry Generation," Chen,
             Gröner, Zarrieß & Eger, 2024. Rhyme-scheme distribution + KL
             results; length histogram-intersection scores; model list in setup.
Quote:       "Current automatic poetry systems are considerably underdiverse
             along multiple dimensions — they often do not rhyme sufficiently,
             are semantically too uniform and even do not match the length
             distribution of human poetry."
```

```text
URL:         https://arxiv.org/abs/2604.17105
Kind:        primary — mechanism study; it owns the tokenization-alignment
             measurements firsthand.
Establishes: That subword tokenization is either too coarse for local
             phonological features or misaligned with phonological boundaries,
             and that character-level input measurably raises phonological-task
             performance.
Paraphrase:  Inserting character-level delimiters raises rhyming-awareness
             accuracy across models (GPT-2 66.1%→77.2%, BERT 68.3%→73.4%,
             Llama-3.1-8B 79.0%→84.0% at the 40%-depth layer). A
             Syllable-Tokenization Alignment Distance shows words whose token
             splits align with syllable boundaries are handled better on G2P and
             syllable counting than misaligned words. Ties BPE directly to lost
             phonological/syllabic structure and shows the loss is partly
             recoverable with finer-grained input.
Locators:    Title "How Tokenization Limits Phonological Knowledge Representation
             in Language Models and How to Improve Them," Liao & Shi, 2026.
             Rhyming-awareness delimiter results; STAD analysis section.
Quote:       "Subword tokenization methods such as Byte Pair Encoding ... are
             often either too coarse to capture local phonological features or
             misaligned with phonological boundaries."
```

```text
URL:         https://www.technologyreview.com/2025/03/27/1113916/anthropic-can-now-track-the-bizarre-inner-workings-of-a-large-language-model
Kind:        secondary — MIT Technology Review reporting on the Anthropic study
             from outside Anthropic; useful for accessible context and for the
             researcher's on-record surprise, not for the primary claim.
Establishes: Independent, plain-language confirmation that the finding was read
             as counter to token-by-token generation, and a direct quote of the
             lead researcher.
Paraphrase:  The article recounts the carrot/rabbit couplet and reports that
             Claude had settled on "rabbit" while processing "grab it," then
             wrote toward that ending; it frames this as against the assumption
             that models pick one word at a time.
Locators:    Will Douglas Heaven, MIT Technology Review, 27 March 2025.
Quote:       Researcher Josh Batson: "The planning thing in poems blew me away."
             The finding "goes against the common assumption that large language
             models always work by picking one word at a time in sequence."
```

```text
URL:         https://en.wikipedia.org/wiki/Orthographic_depth
Kind:        secondary — reference overview; context for the linguistics premise
             that English spelling is an unreliable guide to sound.
Establishes: That English is a "deep" orthography, lacking consistent
             letter-to-sound correspondence, which is why spelling statistics are
             a poor proxy for pronunciation.
Paraphrase:  A deep orthography lacks a consistent one-to-one mapping between
             graphemes and phonemes; English is unusual for combining deep
             orthography with many letters having multiple sounds (e.g. "ea" in
             "beat" vs "head," with no visual cue which is meant). Cites Catts et
             al. (2024), Annals of Dyslexia.
Locators:    "Orthographic depth" article, opening definition and the
             English-specific paragraph.
Quote:       Deep orthographies "do not have a consistent one-to-one
             correspondence between sounds (phonemes) and the letters or
             characters (graphemes) that represent them."
```

## Contradictions

- **The brief's ground claim is too strong as literally worded.** The commission
  says to end on "there is no phonological or metrical representation the decoder
  consults." McLaughlin et al. (2508.02527) show the opposite for phonemes: a
  linear probe recovers a single-token word's phonemes ~96% of the time from the
  embedding, and steering that embedding changes which words the model rhymes.
  Phonological structure is latently *in* the representation. The defensible
  version of the chain is that sound is present but unreliable and not deployed
  for exact counting — not that it is absent. The article should make this the
  "settled vs open" boundary, not paper over it.

- **The failure is not uniform across models — a live "why some scan better"
  case.** On PhonologyBench syllable counting, Claude-3-Sonnet scores 55.3%
  overall while GPT-4 scores 23.3% and GPT-3.5-Turbo 19.6% (human 90.0%). Same
  task, same text-only input, a >30-point spread between two strong closed
  models. This is direct evidence that meter/syllable failure is not a fixed
  architectural fact, and it is exactly the open question the commission flags.
  No source I read explains the spread.

- **Seeing characters helps, which cuts against "sound is simply unavailable to
  a text model."** Both Chen et al. (character-level ByGPT5 best on rhyme/length)
  and Liao & Shi (character delimiters raise rhyming-awareness accuracy by
  5–11 points) show the bottleneck is the *tokenization*, not the text medium.
  A text model with finer-grained input recovers some of the lost structure.
  This supports the tokenization step while undercutting any framing that a
  text-only model can never access sound.

- **Rhyme is not uniformly "gotten right."** The commission contrasts rhyme
  success with meter failure. PhonologyBench qualifies the rhyme half: GPT-4
  rhymes common words 69.1% but rare words 46.1% (humans 86.4% / 60.4%), and
  weaker models fall to single digits on rare words (Mistral 8.3%). Rhyme
  success tracks word frequency, consistent with leaning on training-text
  statistics, but it is still well short of human and far from "solved." Frame
  rhyme as *relatively* better, with numbers, not as reliable.

## Numbers

```text
Figure: 45 percentage points (human − model syllable-counting gap)
Owner:  PhonologyBench (arXiv 2404.02456), abstract + syllable table
Scope:  English syllable counting; human baseline 90.0% overall
```

```text
Figure: Syllable counting overall accuracy — Claude-3-Sonnet 55.3%, GPT-4 23.3%,
        GPT-3.5-Turbo 19.6%, LLaMA-2-13B-Chat 6.9%, Mistral-7B-Instruct 6.8%,
        Mixtral-8x7B-Instruct 6.6%; human 90.0%
Owner:  PhonologyBench (arXiv 2404.02456), Syllable Counting table
Scope:  1,000 sentences (Romance Books + Reddit Short Stories); "overall" column.
        Verified directly against the table (Sonnet 55.3 vs GPT-4 23.3
        cross-checked). Simple/complex splits also given (GPT-4 24.2/15.3).
```

```text
Figure: 17 percentage points (human − model rhyme-generation gap)
Owner:  PhonologyBench (arXiv 2404.02456), abstract + rhyme table
Scope:  Rhyme-word generation; human overall 74.6%, GPT-4 overall 57.6%
```

```text
Figure: Rhyme-word generation — GPT-4 common 69.1% / rare 46.1% / overall 57.6%;
        human common 86.4% / rare 60.4% / overall 74.6%; Mistral-7B rare 8.3%
Owner:  PhonologyBench (arXiv 2404.02456), Rhyme Word Generation table
Scope:  300 words (Spelling Bee list + Google 1-Trillion). Shows rhyme success
        falling with word rarity. Lower confidence on the exact non-GPT-4,
        non-Sonnet cells (extracted from HTML tables, not all re-verified).
```

```text
Figure: Grapheme-to-phoneme accuracy — dedicated G2P library baseline 62.4%
        (high-freq) / 52.8% (low-freq); best LLM (Claude-3-Sonnet) 52.7% / 40.2%
Owner:  PhonologyBench (arXiv 2404.02456), G2P table
Scope:  3,000 words (SIGMORPHON 2021, American English). Even a purpose-built
        tool stays near 62% on English — the quantitative face of "spelling is an
        unreliable guide to sound." Per-model G2P cells: lower confidence,
        extracted from HTML, not all re-verified.
```

```text
Figure: ~96% vs ~42% (probe recovers single-token-word phonemes vs random-
        embedding control)
Owner:  McLaughlin et al. (arXiv 2508.02527), phoneme-probing section
Scope:  Llama-3.2-1B-Instruct token embeddings; single-token words. The
        measure of latent phonology — the "open question" figure.
```

```text
Figure: 70% (line ends on the injected planned rhyme word after feature
        injection, across 25 poems)
Owner:  Anthropic, Biology of a Large Language Model, Planning in Poems section
Scope:  Claude 3.5 Haiku; causal confirmation that the planned end-word steers
        the whole line.
```

```text
Figure: Rhyming-awareness accuracy gains from character delimiters —
        GPT-2 66.1%→77.2%, BERT 68.3%→73.4%, Llama-3.1-8B 79.0%→84.0%
        (at ~40%-depth layer)
Owner:  Liao & Shi (arXiv 2604.17105), rhyming-awareness results
Scope:  Character-level input recovers phonological signal BPE tokens obscure.
```

```text
Figure: Human quatrains — under ~15% non-rhyming (ABCD); ABAB/AABB/ABCB dominate
Owner:  Chen et al. (arXiv 2406.15267), rhyme-scheme distribution
Scope:  Human poetry corpora (English + German). Grounds "rhyme is frequent in
        the training distribution."
```

## Source assets

```text
Asset: The couplet attribution graph in "Planning in Poems" (Biology of a Large
       Language Model), showing "rabbit"/"habit" candidate-word features active
       at the line break before the second line is generated.
Shows: The single clearest picture in the whole chain — the model holding a
       rhyme target ahead of the words that lead to it.
Crop:  Must retain the planned-word feature nodes and the newline position they
       sit at; may omit the wider graph's unrelated branches. Interactive
       figure; a still would need to preserve the labels.
```

```text
Asset: PhonologyBench syllable-counting results table (arXiv 2404.02456).
Shows: The human-vs-model gap and the Claude-Sonnet/GPT-4 spread in one view —
       the metrical-failure evidence and the "some models scan better" open
       question together.
Crop:  Must keep the human baseline row and at least Claude-3-Sonnet and GPT-4;
       keep the "overall" column labeled.
```

```text
Asset: PhonologyBench G2P table with the dedicated-library baseline row (2404.02456).
Shows: That even a purpose-built grapheme-to-phoneme tool only reaches ~62% on
       English — spelling-to-sound is hard for anything, not just LLMs.
Crop:  Must retain the baseline (G2P library) row beside the LLM rows.
```

```text
Asset: McLaughlin et al. phoneme-probe figure / vowel-direction geometry (2508.02527).
Shows: Phonetic structure sitting inside the embedding space — the visual form of
       "sound is latently present."
Crop:  Keep the probe-accuracy comparison (recovered vs random control) legible.
```

Beyond these, None found that would beat prose for the tokenization step itself
(a merge table is better told than shown at this reader level).

## Discarded

```text
https://ceur-ws.org/Vol-3834/paper122.pdf: "Does ChatGPT Have a Poetic Style?" —
  likely relevant (GPT-3.5/GPT-4 across 24 poetic forms) but the PDF returned only
  binary/compressed data on fetch and no HTML mirror was found; could not read the
  passages, so not cited. Unresolved access failure.
https://aclanthology.org/2026.wildre-1.1/ (MetricalARGS): metrical-poetry LLM
  taxonomy, but its worked example is Telugu meter, not English iambic/syllabic
  form; off the commission's English behavior, so not relied on.
https://arxiv.org/pdf/2411.13100 (Song Form-aware lyric generation): syllable-count
  control for song lyrics via a specialized system, not a measurement of a general
  chat model's failure; adjacent, not on-chain.
https://arxiv.org/pdf/2502.19064 and https://arxiv.org/pdf/2606.30556: LLMs as
  poetry *evaluators/judges*, not producers of meter; different question.
https://arxiv.org/pdf/2205.12206 (PoeLM), Deep-speare: purpose-built
  meter/rhyme-controllable models. They show meter needs explicit modeling, which
  supports the angle, but they are systems papers, not measurements of the plain
  behavior; held in reserve, not cited, to avoid conflating a special-purpose model
  with the chat model the lesson is about.
```

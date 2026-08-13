# Evidence: the-mechanics/multilingual-gap (01)

The evidence supports the commissioned two-part mechanism and the order the
commission asks for. A named model is measurably weaker on the same task in
lower-resource languages: GPT-4 scores 85.5% on MMLU in English and 62.0% on the
same translated questions in Telugu (OpenAI GPT-4 report, Figure 5). The lead
cause, data distribution, has a firsthand figure: GPT-3's training data is 93%
English by word count (Brown et al. 2020, §3.3), and the raw web it is drawn
from is about 41% English by Common Crawl's own count. The amplifier, the token
tax, is documented by two primaries (Ahia et al. 2023; Petrov et al. 2023) and
reproduced here from a real tokenizer: the same sentence of the Universal
Declaration of Human Rights costs 33 tokens in English and 512 in Burmese under
cl100k_base, a 15.5x inflation that matches Petrov's reported ceiling. The
evidence is thin in three places, and the writer should not paper over them.
First, the 93% figure belongs to GPT-3 (2020); no current frontier model
discloses its per-language mix, so the lead mechanism rests on a dated proxy plus
the raw-web figure. Second, the split between the two causes is correlational and
unquantified: MEGA (Ahuja et al. 2023) finds both data size and tokenizer
fertility correlate with performance, that the two correlate with each other, and
that neither explains every task. Third, the performance gap is measured on
machine-translated benchmarks, so part of it reflects translation quality rather
than the model. Each of these is set out under Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/2005.14165
Kind:        primary. Brown et al. 2020, the GPT-3 paper, owns the description of
             GPT-3's own training data.
Establishes: The lead-cause figure: the model's training corpus is
             overwhelmingly English, stated firsthand by its builders.
Paraphrase:  GPT-3 was trained on 300 billion tokens drawn mostly from filtered
             Common Crawl, plus WebText2, two book corpora, and English
             Wikipedia. The paper states the training data is still primarily
             English, 93% by word count, with 7% other languages documented in
             the supplemental material. Weighting was set by hand, not by dataset
             size, so Common Crawl (60% of the mix) was seen less than once while
             Wikipedia was seen 3.4 times.
Locators:    §3.3 (Translation) for the 93% figure; Table 2.2 and §2.2 for the
             dataset mix.
Quote:       "Although GPT-3's training data is still primarily English (93% by
             word count), it also includes 7% of text in other languages."
```

```text
URL:         https://commoncrawl.github.io/cc-crawl-statistics/plots/languages
Kind:        primary. Common Crawl's own published statistics for its own crawl.
Establishes: A current, model-independent anchor for how English-skewed the raw
             web text is before any model curates it.
Paraphrase:  In the CC-MAIN-2026-30 crawl, English is the primary language of
             40.58% of documents, far ahead of any other. The next languages are
             Russian 6.82%, German 5.99%, Japanese 5.32%, French 4.80%, Spanish
             4.64%, Chinese 4.43%. Language is assigned by the CLD2 detector, one
             primary language per document.
Locators:    Languages plot, crawl CC-MAIN-2026-30; methodology note on CLD2.
Quote:       (none needed; figures are the evidence)
```

```text
URL:         https://arxiv.org/abs/2305.13707
Kind:        primary. Ahia et al. 2023, "Do All Languages Cost the Same?", owns
             its own measurements of token counts, cost, and utility across
             languages on OpenAI's API.
Establishes: The token tax as both a cost and a utility problem, measured on a
             named model (gpt-3.5-turbo) across 22 languages.
Paraphrase:  Across 22 typologically diverse languages on ChatGPT (gpt-3.5-turbo)
             and BLOOMZ, Latin-script languages use substantially fewer tokens
             for the same information; languages with their own script, such as
             Telugu and Georgian, need up to 5x more tokens. Because OpenAI bills
             per token, this becomes a price gap: on the XLSUM task, prompting
             plus generation costs up to 4x more in Telugu and Amharic than in
             English, and close to 5x for mid-resource Indic non-Latin languages.
             The heavy fragmentation also cuts utility: with a 4096-token limit,
             fewer in-context examples fit, and more test inputs overflow the
             context window, which lowers in-context-learning performance in the
             affected languages. The paper frames this as a socio-economic
             disparity because the overcharged speakers tend to live where the
             API is least affordable.
Locators:    Abstract; §2 (RQ1-RQ4); §3.1 (models); §4.1 (up to 5x tokens); §4.2
             (up to 4x cost, 5x for a user in Andhra Pradesh); §4.3 (utility).
Quote:       "a user in Andhra Pradesh might have to pay 5x more than an English
             user in the US would pay for an equivalent use of the model."
```

```text
URL:         https://arxiv.org/abs/2305.15425
Kind:        primary. Petrov et al. 2023, "Language Model Tokenizers Introduce
             Unfairness Between Languages", owns its tokenization-premium
             measurements on the FLORES-200 parallel corpus.
Establishes: The exact token-inflation multipliers on the current GPT-3.5/GPT-4
             tokenizer, and that even multilingual tokenizers keep a large gap.
Paraphrase:  On FLORES-200, the premium is the ratio of a language's token count
             to English for the same sentence. The cl100k_base tokenizer used by
             ChatGPT and GPT-4 uses about 1.6x more tokens for Italian, 2.6x for
             Bulgarian, and 3x for Arabic; for Shan, spoken in Myanmar, up to 15x.
             Portuguese is closest to parity yet still needs about 50% more tokens
             than English. A concrete case: the Shan word for "you" becomes 9
             tokens under cl100k_base because its consonant and three diacritics
             are four separate codepoints, while English "you" is one token.
             The gap survives multilingual training: BLOOM's tokenizer still shows
             a 12.06x premium for Shan and 7.36x for Dzongkha (Table 4). The
             consequences: users of some languages pay at least 2.5x more, wait up
             to about 2x longer, and fit an order of magnitude less text in a
             fixed context window.
Locators:    Abstract; §1 (1.6x/2.6x/3x/15x); §4.1 and Table 1 (Portuguese ~50%,
             Shan "you" = 9 tokens); Table 4 (multilingual tokenizers); §1 items
             1-3 (cost >=2.5x, latency ~2x, context).
Quote:       "The same text translated into different languages can have
             drastically different tokenization lengths, with differences up to 15
             times in some cases."
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. OpenAI GPT-4 Technical Report, owns GPT-4's own benchmark
             results.
Establishes: The concrete performance instance: one model, one task, weaker in
             lower-resource languages, with figures.
Paraphrase:  OpenAI translated MMLU (57-subject multiple choice) into many
             languages with Azure Translate and ran GPT-4 3-shot. English scores
             85.5%. Scores fall roughly with resource level and script: Spanish
             84.0%, French 83.6%, Russian 82.7%, Arabic 80.0%, Japanese 79.9%,
             Korean 77.0%, then low-resource and non-Latin languages lower still,
             Bengali 73.2%, Thai 71.8%, Marathi 66.7%, Telugu 62.0%. The report's
             own framing is that GPT-4 in most of these languages beats the prior
             best models' English scores (GPT-3.5 70.1%, PaLM 69.3%, Chinchilla
             67.0%), so it presents the same data as progress. Both readings come
             from one chart.
Locators:    §3 and Figure 5 (cross-language MMLU); Appendix F (Azure Translate
             method and caveats).
Quote:       "some translations preserve proper nouns in English, as per
             translation conventions, which may aid performance" and translations
             are "in some cases losing subtle information which may hurt
             performance."
```

```text
URL:         https://aclanthology.org/2023.emnlp-main.258/
Kind:        primary. Ahuja et al. 2023, "MEGA: Multilingual Evaluation of
             Generative AI", owns its own cross-language evaluation and its
             analysis of what drives the gap.
Establishes: The two causes measured side by side, the strongest evidence on the
             contested relative-contribution question, and that GPT-4 narrows but
             does not close the gap.
Paraphrase:  Across 16 datasets and up to 70 languages, MEGA finds a consistent
             gap between English and non-English, worst for low-resource non-Latin
             languages, where fine-tuned smaller models still beat GPT-4. It
             measures both proposed causes. Tokenizer fertility (sub-words per
             word; higher is worse) for OpenAI models reaches about 10 for
             Malayalam and Tamil, so the tokenizer is nearly byte-level there, and
             fertility correlates negatively and significantly with performance.
             Pre-training data size (using GPT-3's disclosed per-language counts as
             a proxy for the closed models) correlates positively with performance
             on four tasks. The two factors are themselves correlated, but data
             size explains cases fertility cannot: GPT-3.5 scores 72.1% in French
             versus 67.0% in Japanese on PAWS-X despite near-equal tokenizer
             fertility, which lines up with 3.5B French versus 214M Japanese tokens
             in GPT-3's data. GPT-4 bridges the gap "to some extent" but the
             discrepancy remains. For many low-resource languages, translating the
             input to English first is hard to beat.
Locators:    Abstract; §3.3 "Factors Explaining Performance Trends" (tokenizer
             fertility, Figures 4-5; data-size analysis and the French/Japanese
             example); §6 (conclusion).
Quote:       "we do see that using pre-training data we are able to explain some
             trends that are not explained by tokenizer fertility alone."
```

```text
URL:         (reproduced in this record; method below)
Kind:        primary. A firsthand token-count comparison produced here with a real
             tokenizer, not a repetition of a paper's number.
Establishes: A reproducible per-language token inflation on the current
             GPT-3.5/GPT-4 tokenizer, independent of the cited papers.
Paraphrase:  Article 1 of the Universal Declaration of Human Rights, taken in each
             language from the Unicode UDHR data (github.com/unicode-org/udhr),
             was encoded with tiktoken's cl100k_base (the ChatGPT and GPT-4
             tokenizer, 100,277-token vocabulary). English is the baseline at 33
             tokens. The same paragraph costs 1.3x in Spanish and German, about
             1.5x in French and Chinese, 2.2x in Russian, 2.7x in Arabic, 5.5x in
             Hindi, 8.5x in Telugu, 9.2x in Amharic, and 15.5x in Burmese. The
             ceiling matches Petrov's reported "up to 15 times". Characters per
             token fall from 5.15 in English to 0.34 in Amharic, so the tokenizer
             is close to per-byte on the scripts it was least fitted to. Full
             series under Numbers; the input strings are recorded so the count can
             be rerun.
Locators:    Method: tiktoken 0.13.0, encoding cl100k_base; input = UDHR Article 1
             per language; whitespace collapsed; count = len(enc.encode(text)).
Quote:       (none; the counts are the evidence)
```

```text
URL:         https://arxiv.org/abs/2510.12389
Kind:        primary. Teklehaymanot and Nejdl 2025, "Tokenization Disparities as
             Infrastructure Bias", owns its own cross-language token measurements.
Establishes: That the token tax persists into 2025 across a wide language set,
             evidence that the amplifier is settled and current.
Paraphrase:  Using tiktoken across more than 200 languages, the study reports that
             non-Latin and morphologically complex languages incur 3-5x higher
             relative tokenization cost than English. It is a single cross-section,
             not a comparison across tokenizer versions, so it shows persistence
             but not a trend over time.
Locators:    Abstract; methods (tiktoken, RTC and TPS metrics).
Quote:       "non-Latin and morphologically complex languages incur significantly
             greater token inflation, often 3-5 times higher RTC ratios."
```

```text
URL:         https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/tokenization-other-languages/
Kind:        secondary. A developer-education page reporting the token tax from
             outside the research; it repeats the pattern and links Petrov 2023.
Establishes: Only that the finding has reached practitioner-facing material. It
             owns no measurement.
Paraphrase:  The page states that a sentence that is 4-5 tokens in English can be
             15-20 or more in Hindi, Thai, or Burmese, describes 3-8x as common for
             non-Latin scripts, and points readers to Petrov et al. 2023. Its
             multipliers are given as general patterns, not sourced figures.
Locators:    Body and "Further reading".
Quote:       (none; a repetition, not a source of fact)
```

## Contradictions

- **The token inflation is not purely a data-share artifact.** The commission
  wants data distribution to lead and the tokenizer to amplify. Ahia et al. warn
  the mapping is looser than that: they hypothesize the token disparity comes from
  training-data imbalance but add that this "is not always the case, but it could
  also be dependent on linguistic features or properties of language scripts"
  (§2, RQ1). A writer who says English's data share directly sets every language's
  token count overstates what the primary claims.

- **The split between the two causes is unquantified and correlational.** MEGA
  measures both and refuses to rank them: tokenizer fertility and pre-training
  data size each correlate with performance, they correlate with each other, and
  they "correlate well with only a subset of the tasks and what we are measuring
  is the correlation which might not imply causation." The French-versus-Japanese
  case shows data explaining variance the tokenizer cannot, which supports putting
  data first, but no source gives a clean percentage to either cause.

- **The gap is narrowing, and the same numbers can be read as progress.** The
  GPT-4 report presents its cross-language MMLU chart as GPT-4 beating older
  models' English scores in most languages. The within-model gap (85.5% English
  to 62.0% Telugu) and MEGA's finding that fine-tuned models still beat GPT-4 in
  low-resource non-Latin languages both stand, but the honest statement is that
  larger multilingual models close much of the gap without closing it, not that
  nothing has improved.

- **The performance gap is measured through machine translation.** GPT-4's
  multilingual MMLU questions were translated by Azure Translate; the report says
  translations sometimes lose information "which may hurt performance" and
  sometimes keep English proper nouns "which may aid performance." MEGA finds that
  for many low-resource languages, translating the input to English first is hard
  to beat. So part of the measured gap is benchmark translation quality, not the
  model reasoning in the language. The gap is real; its exact size on any one
  benchmark is not a clean model-capability reading.

- **The premium is a property of the tokenizer's training, not of the script.**
  Petrov's Table 3 shows MuRIL, a tokenizer trained for Indian languages, encodes
  Telugu at 1.21x English and most Indic languages within 1.06-1.26x, against the
  5x-plus those same languages pay under English-centric tokenizers. This
  undercuts any claim that non-Latin scripts are inherently expensive; the cost
  tracks what the tokenizer was fit on.

- **The lead figure is dated and belongs to an older model.** The 93% English
  figure is GPT-3 (2020). No current frontier model publishes its per-language
  mix; MEGA itself falls back to GPT-3's distribution as a proxy for GPT-3.5 and
  GPT-4. Common Crawl's 40.58% is current but describes the raw web, not any
  model's curated training set. The jump from ~41% (raw web) to 93% (GPT-3's mix)
  is itself a finding: English-favoring quality filters and the English book,
  WebText, and Wikipedia additions concentrate English well above its web share.

## Numbers

```text
Figure: 93% English by word count (7% other languages)
Owner:  Brown et al. 2020 (GPT-3), §3.3
Scope:  GPT-3's full training corpus, by word count. 300B training tokens total.
```

```text
Figure: English 40.58% of documents (next: Russian 6.82, German 5.99, Japanese
        5.32, French 4.80, Spanish 4.64, Chinese 4.43)
Owner:  Common Crawl language statistics
Scope:  Crawl CC-MAIN-2026-30; primary language per document by CLD2 detector.
```

```text
Figure: GPT-4 3-shot MMLU accuracy, English 85.5% down to Telugu 62.0%
Owner:  OpenAI GPT-4 Technical Report, Figure 5
Scope:  Same MMLU questions machine-translated to each language via Azure
        Translate. Full series: English 85.5, Italian 84.1, Afrikaans 84.1,
        Spanish 84.0, German 83.7, French 83.6, Indonesian 83.1, Russian 82.7,
        Polish 82.1, Ukrainian 81.9, Greek 81.4, Latvian 80.9, Mandarin 80.1,
        Arabic 80.0, Turkish 80.0, Japanese 79.9, Swahili 78.5, Welsh 77.5,
        Korean 77.0, Icelandic 76.5, Bengali 73.2, Urdu 72.6, Nepali 72.2,
        Thai 71.8, Punjabi 71.4, Marathi 66.7, Telugu 62.0. Reference English
        baselines: GPT-3.5 70.1, PaLM 69.3, Chinchilla 67.0, random 25.0.
```

```text
Figure: Up to 5x more tokens for the same information (Telugu, Georgian)
Owner:  Ahia et al. 2023, §4.1
Scope:  22 languages on ChatGPT (gpt-3.5-turbo), relative to English.
```

```text
Figure: Up to 4x cost for prompt+generation (Telugu, Amharic); ~5x for a Telugu
        user versus an English user
Owner:  Ahia et al. 2023, §4.2 (XLSUM)
Scope:  Per-token API billing on gpt-3.5-turbo, relative to English.
```

```text
Figure: cl100k_base premium: Italian 1.6x, Bulgarian 2.6x, Arabic 3x, Shan up to
        15x; Portuguese (closest) still ~1.5x
Owner:  Petrov et al. 2023, §1 and §4.1
Scope:  FLORES-200 parallel sentences, tokens relative to English, ChatGPT/GPT-4
        tokenizer.
```

```text
Figure: Multilingual tokenizers still far from parity: BLOOM Shan 12.06x,
        Dzongkha 7.36x
Owner:  Petrov et al. 2023, Table 4
Scope:  FLORES-200, relative to English, tokenizers built for multilingual use.
```

```text
Figure: Cost >= 2.5x, latency ~2x, context capacity > order of magnitude, for the
        worst-served languages
Owner:  Petrov et al. 2023, §1 (implications 1-3)
Scope:  Consequences of the token premium for commercial API users.
```

```text
Figure: MuRIL encodes Telugu at 1.21x English (Indic languages 1.06-1.26x)
Owner:  Petrov et al. 2023, Table 3
Scope:  FLORES-200, tokenizer trained for 16 Indian languages plus English.
        Contrast with 5x-plus under English-centric tokenizers.
```

```text
Figure: OpenAI tokenizer fertility ~10 sub-words/word for Malayalam and Tamil;
        GPT-3.5 PAWS-X French 72.1% vs Japanese 67.0% (3.5B vs 214M pretrain
        tokens)
Owner:  Ahuja et al. 2023 (MEGA)
Scope:  OpenAI models across MEGA's task suite; data counts from GPT-3's disclosed
        per-language distribution used as a proxy.
```

```text
Figure: Reproduced cl100k_base token counts, UDHR Article 1, English = 33 tokens
Owner:  This record (tiktoken 0.13.0, cl100k_base)
Scope:  One parallel paragraph per language, tokens and multiplier vs English,
        characters per token:
          English (Latin)        33 tokens   1.00x   5.15 char/tok
          Spanish (Latin)        44          1.33x   3.89
          German (Latin)         44          1.33x   3.73
          French (Latin)         50          1.52x   3.72
          Chinese simpl. (Han)   50          1.52x   0.86
          Russian (Cyrillic)     74          2.24x   2.16
          Korean (Hangul)        85          2.58x   1.02
          Arabic (Arabic)        88          2.67x   1.32
          Japanese (Kana/Kanji)  93          2.82x   0.91
          Hindi (Devanagari)    182          5.52x   1.04
          Telugu (Telugu)       281          8.52x   0.55
          Amharic (Ge'ez)       305          9.24x   0.34
          Burmese (Myanmar)     512         15.52x   0.51
        Reproduce: fetch udhr_<key>.xml from github.com/unicode-org/udhr, take the
        <article number="1"> paragraph text, and run
        tiktoken.get_encoding('cl100k_base').encode(text). Keys: eng, spa, deu_1996,
        fra, cmn_hans, rus, kor, arb, jpn, hin, tel, amh, mya.
```

```text
Figure: 3-5x higher relative tokenization cost, non-Latin/complex languages, 2025
Owner:  Teklehaymanot and Nejdl 2025
Scope:  tiktoken across 200+ languages; a single cross-section, no time trend.
```

## Source assets

```text
Asset: GPT-4 Technical Report, Figure 5, "GPT-4 3-shot accuracy on MMLU across
       languages" (the horizontal bar ranking English at 85.5% down to Telugu
       62.0%, with the older-model English baselines marked).
Shows: The performance gap as one ordered picture: same model, same questions,
       accuracy sliding down as languages get lower-resource and non-Latin, with
       the old English scores drawn in so the reader sees both the gap and the
       progress at once.
Crop:  Must keep the English bar, the low-resource tail (through Telugu), and the
       reference baselines. A crop that drops the baselines loses the "narrows but
       does not close" reading. Note the machine-translation caveat in any caption.
```

```text
Asset: Petrov et al. 2023, the tokenized Shan word "you" rendered as 9 colored
       token pieces against English "you" as one token (§4.1).
Shows: Why a rare script fragments: one written character split into consonant
       plus three diacritics, each its own codepoint, each its own token. It makes
       the token tax concrete at the level of a single word.
Crop:  Keep both the Shan word with its token boundaries and the English "you"
       beside it; the comparison is the point.
```

```text
Asset: A chart built from this record's reproduced token counts (Numbers section),
       English 33 to Burmese 512 for the same UDHR paragraph. Would be rendered by
       the article's own chart-N.py per spec/charts.md, not lifted from a source.
Shows: The token multiplier climbing with script distance from English, from a
       tokenizer the reader can run themselves, with the input text disclosed.
Crop:  Label the y-axis as tokens for one fixed paragraph; caption the tokenizer
       (cl100k_base) and the text (UDHR Article 1); order languages by count.
```

```text
Asset: Common Crawl languages plot (English ~41% bar towering over the rest).
Shows: The raw-web starting point before any model curates, so the reader sees
       the skew is upstream of training choices.
Crop:  Keep English plus the next several bars so the scale of the lead is legible;
       note the crawl id (CC-MAIN-2026-30) and CLD2 method in the caption.
```

## Discarded

```text
URL: https://kathane.substack.com/p/not-speaking-english-to-chatgpt-costs — blog
     restatement of the token tax; no firsthand measurement, primaries cover it.
URL: https://medium.com/@programmerraja/how-your-llm-costs-5x-more-... — Medium
     explainer; secondary to Ahia/Petrov, adds no verifiable figure of its own.
URL: https://www.magd.dev/blog/the-token-inequality-... — personal blog; same
     ground as the primaries with no independent data.
URL: https://dl.acm.org/doi/10.5555/3666122.3667730 — the ACM/NeurIPS record for
     Petrov et al.; same paper as the arXiv page already cited, not a new source.
URL: https://huggingface.co/papers/2305.15425 — listing page for Petrov et al.,
     not the paper itself.
```

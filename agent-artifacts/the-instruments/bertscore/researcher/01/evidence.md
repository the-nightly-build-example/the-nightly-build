# Evidence: the-instruments/bertscore (01)

The evidence fully supports the commission's recipe and its "what it cannot
support" half. The originating paper (Zhang et al., ICLR 2020) and the metric's
own repository document each gear: contextual token embeddings, greedy cosine
matching, precision/recall/F1, optional idf weighting, and the baseline
rescaling that is explicitly readability-only and "does not affect the ranking
ability and human correlation." The non-comparability point is well sourced: the
repository states scores change with the encoder, the layer, the library
version, and even the tokenizer implementation, and it asks users to publish a
hash string recording all of these. There are two concrete, documented cases
where the number misled, each owned by its study: Hanna and Bojar (2021) show
BERTScore rates lexically similar but incorrect translations too high and is
weakest on function-word errors, and Sun et al. (2022) show it inherits the
encoder's social bias, scoring one gender-swapped candidate 31 points above
another. Contradictions are real and recorded: Kocmi et al. (2021) rank
BERTScore below every learned metric on MT system ranking, and SummEval (Fabbri
et al., 2021) finds its F1 correlates near zero with human judgments of summary
factual consistency, below ROUGE-1.

The record is thin in three places, stated plainly so the writer does not
overclaim. First, the paper reports its human-correlation advantage across dozens
of appendix tables rather than one summary figure, and its strongest numbers are
system-level correlations computed over few systems per language pair, so "higher
by how much" has no single clean answer. Second, the later studies that qualify
BERTScore are each on modest samples (Hanna and Bojar's accuracies on small
filtered sets; SummEval's system-level correlations over 16 systems; Sun et al.'s
bias averages), so treat their exact decimals as indicative, not precise. Third,
the authors ask users to report a version hash, but I found no study measuring
whether papers actually do; the compliance claim in research direction 3 cannot
be sourced and should be cut or stated as unknown.

## Sources

```text
URL:         https://arxiv.org/abs/1904.09675
Kind:        primary. The paper that defines and owns the metric (ICLR 2020).
             Authors: Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
             Weinberger, Yoav Artzi (Cornell University). Read via full HTML.
Establishes: The complete recipe and the paper's own claims and caveats.
             - Token representation: contextual embeddings (default English:
               24-layer RoBERTa-large; Chinese: BERT-chinese; other languages:
               cased multilingual BERT); different vectors for the same word
               depending on surrounding context.
             - Similarity: cosine similarity of a reference token and a
               candidate token; with pre-normalized vectors this reduces to the
               inner product.
             - Greedy matching: "each token is matched to the most similar token
               in the other sentence." Recall matches each reference token to its
               best candidate token; precision does the reverse; F1 is their
               harmonic mean. Formulas: R = (1/|x|) Σ_i max_j x_i·x̂_j ;
               P = (1/|x̂|) Σ_j max_i x_i·x̂_j ; F = 2PR/(P+R).
             - idf weighting: optional; idf computed from the reference sentences
               of the test set, plus-one smoothed; weights the max-similarity
               terms. Same idf for every system on a test set.
             - Baseline rescaling: X̂ = (X − b)/(1 − b), where b is the average
               BERTScore on ~1M random candidate-reference pairs drawn from
               Common Crawl monolingual data (near-zero overlap). Puts scores
               "typically between 0 and 1." Quote below.
             - Scope of evaluation: outputs of 363 machine-translation and
               image-captioning systems; main MT corpus WMT18 (149 systems, 14
               language pairs); COCO 2015 captioning (12 systems).
             - Claims: stronger system- and segment-level correlation with human
               judgment than BLEU and other metrics; strong model-selection
               performance; on captioning, surpasses SPICE among task-agnostic
               metrics but is beaten by LEIC, a trained metric that also sees the
               image. idf "at times provides small benefit, but in other cases
               does not help"; they proceed without idf and recommend F1.
             - No single configuration dominates: "there is no one configuration
               of BERTScore that clearly outperforms all others." Multilingual
               BERT "has less stable performance on low-resource languages."
             - Robustness: on PAWS-QQP adversarial paraphrases (word swaps), most
               metrics fall "almost down to chance," while BERTScore "drops only
               slightly."
             - Cost: the WMT18 en-de test set (2,998 sentences) takes 15.6 sec vs
               5.4 sec for SacreBLEU.
Paraphrase:  BERTScore encodes each token of candidate and reference with a
             pretrained Transformer encoder, greedily pairs each token with its
             most cosine-similar token in the other sentence, and averages those
             similarities into precision, recall, and F1; idf reweighting and a
             linear baseline rescaling are both optional add-ons, the latter
             purely for readability.
Locators:    Sec. 3 (Token Representation, Similarity Measure, BERTScore,
             Importance Weighting, Baseline Rescaling); Sec. 4 (Experimental
             Setup); Sec. 5 (Results, Tables 1-6); Sec. 6 (Robustness); Sec. 7
             (Discussion). Abstract.
Quote:       "This method does not affect the ranking ability and human
             correlation of BERTScore, and is intended solely to increase the
             score readability." (Sec. 3, Baseline Rescaling)
```

```text
URL:         https://github.com/Tiiiger/bert_score
Kind:        primary. The authors' own reference implementation and
             documentation (README). Owns the versioning/hash behavior and the
             default-model facts.
Establishes: - Supports "about 130 models"; default English encoder is
               roberta-large; the authors now recommend microsoft/
               deberta-xlarge-mnli for best correlation. Different model = a
               different measurement.
             - Output carries a hash code, e.g.
               "roberta-large_L17_no-idf_version=0.3.0(hug_trans=2.3.0)"; the
               rescaled variant appends "-rescaled".
             - Concrete rescaling effect on one example pair: raw
               P/R/F1 = 0.957378 / 0.961325 / 0.959333 becomes rescaled
               0.747044 / 0.770484 / 0.759045.
             - Fast vs slow tokenizer changes the number (see below).
             - Limitation: sentences longer than 510 word-piece tokens are
               truncated; BERTScore "is undefined between sentences longer than
               510."
             - idf is optional and "when the set of reference sentences become
               too small, the idf score would become inaccurate/invalid."
Paraphrase:  Two BERTScore numbers are the same measurement only when the model,
             layer, idf setting, library version, and tokenizer match; the
             library prints a hash of that configuration and the authors ask
             users to report it, borrowing the practice from sacreBLEU.
Locators:    README sections: intro, "Practical Tips," "Default Behavior /
             Default Model," CLI usage example.
Quote:       "Report the hash code ... in your paper so that people know what
             setting you use. This is inspired by sacreBLEU. Changes in
             huggingface's transformers version may also affect the score."
             And, on fast tokenizers: "you will get different scores because of
             the difference in the tokenizer implementations."
```

```text
URL:         https://github.com/Tiiiger/bert_score/blob/master/journal/rescale_baseline.md
Kind:        primary. Authors' own write-up of the rescaling, signed "Tianyi,
             Varsha, and Felix."
Establishes: - Raw RoBERTa-large scores sit in a narrow band; "computed with the
               large RoBERTa model often is between 0.85 and 0.95."
             - Concrete corpus-level effect: "the average BERTScore (computed
               with RoBERTa-large, layer17) on the WMT18 De-EN translation
               evaluation dataset drops from 0.9311 to 0.5758" after rescaling.
             - Rescaling "does not affect BERTScore's correlation with human
               judgment"; baseline is the average score over ~500K randomly
               paired sentences per language/model.
Paraphrase:  Rescaling stretches raw scores that cluster near 0.9 down toward a
             0-to-1 range, turning a 0.93 average into 0.58, without changing any
             ranking or correlation.
Locators:    Whole document (journal/rescale_baseline.md).
Quote:       "the average BERTScore (computed with RoBERTa-large, layer17) on the
             WMT18 De-EN translation evaluation dataset drops from 0.9311 to
             0.5758."
```

```text
URL:         https://aclanthology.org/2021.wmt-1.59/
Kind:        primary. Owns its failure-mode findings and figures. "A Fine-Grained
             Analysis of BERTScore," Michael Hanna and Ondřej Bojar (Charles
             University), WMT 2021, pp. 507-517. Used the original authors'
             BERTScore implementation with default baseline rescaling (English,
             roberta-large).
Establishes: A documented case where BERTScore misleads in its core job: ranking
             a correct translation above an incorrect one.
             - Central finding: "BERTScore fails to assign low scores when a bad
               candidate sentence has high lexical overlap with the reference in
               terms of content words," and is "less sensitive to smaller errors,
               especially if the candidate is lexically or stylistically similar
               to the reference."
             - TQ-AutoTest, condition (ii) accuracy (does the correct pair beat
               the bad translation?): average 75.5%, but function words 42.9% and
               punctuation 40.0%. BLEU on the same test scored 36.2%.
             - TQ-AutoTest mean F1 for correct translation pairs: 0.815 average,
               but the "function word" category falls to 0.712.
             - PE2rr, "hard" setting (post-edited MT as the reference, so the bad
               candidate overlaps it heavily): BERTScore is "at or below chance
               in all categories except sentences with an untranslated word."
             - Grammatical Error Correction (Table 5): a sentence with 5
               remaining errors still scores 0.812, versus 0.821 error-free and
               0.842 for an alternate reference — a very narrow band.
             - Concrete example (tag questions): reference "You're crazy, aren't
               you?", good alternate "You're crazy, right?", bad candidates
               "You're crazy, or?" and "You're crazy, are not you?" — errors in
               function words that BERTScore struggles to penalize.
             - Context notes: BERTScore was not included even in the WMT20
               metrics shared task; and Kocmi et al. (2021) found its performance
               "middle-of-the-road, though better than BLEU," recommending COMET.
Paraphrase:  BERTScore reliably catches obvious content-word errors but misses
             subtle, meaning-changing edits when the wrong sentence still looks
             like the reference, so it is better at separating very different
             systems than near-neighbors or two outputs of one system.
Locators:    Abstract; Sec. 5.1 (Tables 1-2); Sec. 5.2 (Table 4, Fig. 4); Sec.
             5.3 (Table 5); Sec. 6 (Discussion); Sec. 7 (Related Work).
Quote:       "We find that BERTScore fails to assign low scores when a bad
             candidate sentence has high lexical overlap with the reference in
             terms of content words." (Sec. 8, Conclusion)
```

```text
URL:         https://aclanthology.org/2022.emnlp-main.245/
Kind:        primary. Owns the bias measurements. "BERTScore is Unfair: On Social
             Bias in Language Model-Based Metrics for Text Generation," Tianxiang
             Sun, Junliang He, Xipeng Qiu, Xuanjing Huang (Fudan University),
             EMNLP 2022, pp. 3726-3739. Tests BERTScore F-score with its default
             encoder (matching-based paradigm). (arXiv: 2210.07626.)
Establishes: A documented case of the encoder's blind spot reaching the score.
             - Core claim: "popular PLM-based metrics exhibit significantly higher
               social bias than traditional metrics on 6 sensitive attributes,
               namely race, gender, religion, physical appearance, age, and
               socioeconomic status."
             - Method: paired candidates identical except for a demographic term;
               a fair metric should score them the same. Bias = the score gap.
             - Concrete worked example (Table 1, scores normalized to [0,100]):
               reference "The carpenter made a desk for the clerk because the
               clerk needed a desk"; candidate with "she" scores 38.87 and with
               "he" scores 70.14 — a BERTScore gap of 31.27 from a single pronoun.
             - Aggregate: for gender, PLM-based metrics show score differences of
               roughly 7 to 21, while traditional metrics (BLEU, ROUGE, METEOR)
               stay near or below 3 (Fig. 4). BERTScore's average gender-bias gap
               is about 7.
Paraphrase:  Because BERTScore reads similarity out of a pretrained encoder, it
             reproduces that encoder's social stereotypes, giving otherwise
             identical candidates different scores when only a demographic word
             changes — far more so than n-gram metrics.
Locators:    Abstract; Sec. 1 (Table 1); Sec. 3 (paradigms, Table 2); Sec. 4
             (Fig. 4).
Quote:       "we demonstrate that popular PLM-based metrics exhibit significantly
             higher social bias than traditional metrics on 6 sensitive
             attributes."
```

```text
URL:         https://aclanthology.org/2021.wmt-1.57/
Kind:        primary. Owns the cross-metric ranking comparison. "To Ship or Not
             to Ship: An Extensive Evaluation of Automatic Metrics for Machine
             Translation," Tom Kocmi, Christian Federmann, Roman Grundkiewicz,
             Marcin Junczys-Dowmunt, Hitokazu Matsushita, Arul Menezes
             (Microsoft), WMT 2021.
Establishes: The main contradiction to a simple "BERTScore is the good semantic
             metric" reading: it trails every learned metric.
             - Pairwise accuracy at ranking system pairs, full set (n = 1,717
               system pairs, aggregated across language pairs): COMET 96.5,
               COMET-src 95.3, Prism 94.5, BLEURT 93.8, ESIM 92.9, BERTScore 92.2,
               ChrF 89.5, TER 89.2, CharacTER 88.6, BLEU 88.2, Prism-src 85.3.
             - Recommendation: use a pretrained metric as the main metric,
               specifically COMET; use a string metric like ChrF only for
               unsupported languages; "Do not use BLEU."
Paraphrase:  Across a large human-judged MT comparison, BERTScore ranks in the
             middle: clearly above BLEU and other overlap metrics, and clearly
             below the trained metrics COMET and BLEURT, which the authors
             recommend instead.
Locators:    Sec. 1 (best-practice list); Sec. 5 results (Table 3, "Everything"
             column, n=1717); Sec. 6 (Discussion).
Quote:       "Use a pretrained metric as the main automatic metric; we recommend
             COMET. ... Do not use BLEU, it is inferior to other metrics."
```

```text
URL:         https://aclanthology.org/2021.tacl-1.24/
Kind:        primary. Owns its summarization correlation table. "SummEval:
             Re-evaluating Summarization Evaluation," Alexander R. Fabbri,
             Wojciech Kryściński, Bryan McCann, Caiming Xiong, Richard Socher,
             Dragomir Radev, TACL vol. 9, 2021. (arXiv: 2007.12626.)
Establishes: A second contradiction: on summarization, BERTScore's F1 correlates
             worse with human judgment than cheap ROUGE on some dimensions.
             - Setup: 16 summarization-model outputs on 100 CNN/DailyMail
               articles, judged by 3 experts on coherence, consistency, fluency,
               relevance; Table 2 is system-level Kendall's tau using 11
               reference summaries (n = 16 systems, so noisy).
             - BertScore-f tau: coherence 0.2059, consistency 0.0441, fluency
               0.2435, relevance 0.4265.
             - ROUGE-1 tau: consistency 0.5294; ROUGE-2 consistency 0.5882 — both
               far above BERTScore-F1 on factual consistency.
             - The recall variant behaves very differently: BertScore-r
               consistency tau is 0.6618 while BertScore-p is -0.1912, so the F1
               that people report (0.0441) hides a strong recall and a negative
               precision.
Paraphrase:  When human annotators rated summary quality, the reported BERTScore
             F1 tracked their factual-consistency judgments barely at all and
             below ROUGE, and the precision and recall halves pulled in opposite
             directions.
Locators:    Abstract; Sec. 3.1 (metric list); Sec. 3 (Table 2, system-level).
Quote:       Table 2, BertScore-f consistency = 0.0441 vs ROUGE-1 consistency =
             0.5294.
```

```text
URL:         https://huggingface.co/spaces/evaluate-metric/bertscore
Kind:        secondary. Hugging Face's metric card in the `evaluate` library:
             documents and repeats the metric from outside the authoring party.
             Used for adoption and to corroborate the configuration caveats.
Establishes: - Adoption: BERTScore ships as a standard metric in Hugging Face's
               `evaluate` (and `datasets`) collections, the common route by which
               it is reported alongside BLEU and ROUGE.
             - Repeats the caveat that correlation "depends on the model and
               language pair selected," and that output includes a hashcode.
             - Repeats a paper figure worth flagging: model-selection accuracies
               (Hits@1) on WMT18 hybrid systems "ranged from 0.004 for en<->tr to
               0.824 for en<->de" — see Numbers, verified against the paper.
Paraphrase:  A widely used evaluation library packages BERTScore as a default
             metric and passes along the authors' warnings that the score depends
             on model and language and comes with a configuration hash.
Locators:    Metric card sections "How to use," "Values from popular papers,"
             "Limitations and bias."
Quote:       "BERTScore correlates well with human judgment on sentence-level and
             system-level evaluation, but this depends on the model and language
             pair selected."
```

## Contradictions

The evidence does not undermine the commissioned angle; it sharpens its second
half. Three tensions are worth the writer's attention.

- **"Semantic beats overlap" is not always true.** SummEval finds BERTScore-F1
  correlating 0.0441 with expert factual-consistency judgments of summaries,
  below ROUGE-1 (0.5294) and ROUGE-2 (0.5882). On this task the cheaper n-gram
  metric wins. The paper's advantage was demonstrated on machine translation and
  captioning, not summarization consistency, so the "closer by meaning" story has
  a documented exception. (Sources: aclanthology.org/2021.tacl-1.24;
  arxiv.org/abs/1904.09675.)

- **BERTScore is outperformed by learned metrics, not just cheaper ones.** Kocmi
  et al. place BERTScore (92.2%) below COMET (96.5%), COMET-src (95.3%), Prism
  (94.5%), BLEURT (93.8%), and ESIM (92.9%) on MT system ranking, and recommend
  COMET. This is consistent with, not contrary to, the paper — but it corrects any
  impression that BERTScore is the state of the art. (Source:
  aclanthology.org/2021.wmt-1.57.)

- **The paper's robustness claim and the later failure findings pull against each
  other.** Zhang et al. show BERTScore is more robust than rivals on PAWS word
  swaps; Hanna and Bojar show it fails to penalize lexically similar but incorrect
  translations, especially function-word errors, dropping to at-or-below chance in
  their hard setting. Both can be true — PAWS swaps reorder content words, which
  BERTScore catches, while function-word and small edits are what it misses — but a
  writer should not cite the robustness result as a general claim.
  (Sources: arxiv.org/abs/1904.09675; aclanthology.org/2021.wmt-1.59.)

Minor internal tension: the paper reports idf weighting as inconsistent ("at
times provides small benefit, but in other cases does not help") and proceeds
without it, while the repository suggests idf "may correlate better" but warns it
becomes invalid on small reference sets. Present idf as optional and situational,
not as a default improvement.

## Numbers

```text
Figure: R = (1/|x|) Σ_i max_j x_i·x̂_j ; P = (1/|x̂|) Σ_j max_i x_i·x̂_j ;
        F1 = 2PR/(P+R), over pre-normalized token embeddings (cosine = dot product)
Owner:  Zhang et al. 2020 (arxiv.org/abs/1904.09675), Sec. 3
Scope:  per candidate-reference sentence pair; greedy token matching
```

```text
Figure: baseline rescaling X̂ = (X − b)/(1 − b)
Owner:  Zhang et al. 2020, Sec. 3
Scope:  b = mean BERTScore over ~1M random sentence pairs per language/model
        (Common Crawl); rescaling changes readability only, not ranking/correlation
```

```text
Figure: 0.9311 → 0.5758 (average F, RoBERTa-large layer 17, after rescaling)
Owner:  bert_score repo journal (github.com/Tiiiger/bert_score, rescale_baseline.md)
Scope:  average over the WMT18 De-EN translation evaluation dataset
```

```text
Figure: raw F1 0.959333 → rescaled 0.759045 (one example pair, roberta-large L17)
Owner:  bert_score repo README (github.com/Tiiiger/bert_score)
Scope:  single candidate/reference pair, English, no-idf, version 0.3.0
```

```text
Figure: raw RoBERTa-large scores "often between 0.85 and 0.95"
Owner:  bert_score repo journal
Scope:  qualitative range of raw (un-rescaled) F on typical inputs
```

```text
Figure: version hash "roberta-large_L17_no-idf_version=0.3.0(hug_trans=2.3.0)"
Owner:  bert_score repo README
Scope:  identifies model, layer, idf setting, library version; "-rescaled" appended
        when rescaled; ~130 supported models; default English encoder roberta-large
```

```text
Figure: model-selection accuracy (Hits@1) F_BERT+idf: de→en 0.824, tr→en 0.004
Owner:  Zhang et al. 2020, Table 3 (verified in source text)
Scope:  WMT18, 10K hybrid super-sampled systems, averaged over 100K samples;
        left number is to-English. Plain F_BERT tr→en = 0.142 (to-English).
        Shows reliability varies enormously by language pair.
```

```text
Figure: 2,998 sentences scored in 15.6 sec (BERTScore) vs 5.4 sec (SacreBLEU)
Owner:  Zhang et al. 2020, Sec. 5
Scope:  WMT18 en-de test set, single run
```

```text
Figure: condition-(ii) accuracy: 75.5% average; function words 42.9%; punctuation
        40.0%; BLEU on same task 36.2%
Owner:  Hanna & Bojar 2021 (aclanthology.org/2021.wmt-1.59), Table 2
Scope:  TQ-AutoTest, filtered examples with two good + one/two bad translations;
        English target, default roberta-large with baseline rescaling
```

```text
Figure: mean F1 for correct translation pairs 0.815 average; function word 0.712
Owner:  Hanna & Bojar 2021, Table 1
Scope:  TQ-AutoTest, per linguistic-phenomenon category
```

```text
Figure: sentence with 5 remaining errors scores F1 0.812 (vs 0.821 error-free,
        0.842 alternate reference)
Owner:  Hanna & Bojar 2021, Table 5
Scope:  Grammatical Error Correction data; means across examples
```

```text
Figure: BERTScore gender gap 70.14 (he) vs 38.87 (she) = 31.27 on one pair
Owner:  Sun et al. 2022 (aclanthology.org/2022.emnlp-main.245), Table 1
Scope:  scores normalized to [0,100]; reference "The carpenter made a desk for the
        clerk because the clerk needed a desk"; candidates differ only in pronoun
```

```text
Figure: average gender-bias gap ~7 (BERTScore); PLM-based metrics 7-21, traditional
        metrics <~3
Owner:  Sun et al. 2022, Fig. 4
Scope:  across the gender dataset of paired stereotype/anti-stereotype candidates
```

```text
Figure: MT system-pair ranking accuracy: COMET 96.5, COMET-src 95.3, Prism 94.5,
        BLEURT 93.8, ESIM 92.9, BERTScore 92.2, ChrF 89.5, TER 89.2,
        CharacTER 88.6, BLEU 88.2, Prism-src 85.3
Owner:  Kocmi et al. 2021 (aclanthology.org/2021.wmt-1.57), Table 3, "Everything"
Scope:  n = 1,717 system pairs, aggregated across language pairs; percentages
```

```text
Figure: SummEval system-level Kendall tau — BertScore-f: coherence 0.2059,
        consistency 0.0441, fluency 0.2435, relevance 0.4265; ROUGE-1 consistency
        0.5294; ROUGE-2 consistency 0.5882; BertScore-r consistency 0.6618;
        BertScore-p consistency −0.1912
Owner:  Fabbri et al. 2021 (aclanthology.org/2021.tacl-1.24), Table 2
Scope:  16 CNN/DailyMail summarization systems, expert annotations, 11 references;
        small n, treat as indicative
```

## Source assets

```text
Asset: Figure 1 (the R_BERT computation diagram) in Zhang et al. 2020, Sec. 3
Shows: reference and candidate tokens, the pairwise cosine-similarity matrix, the
       greedy match highlighted, and where optional idf weights enter — the whole
       mechanism in one picture
Crop:  must retain the token-to-token similarity grid and the highlighted greedy
       matches; may omit the idf-weight column if the lesson defers idf
```

```text
Asset: the before/after similarity-matrix images in the repo journal
       (journal/static/before.png and after.png; produced by `bert-score-show`)
Shows: how rescaling redraws the same token-similarity matrix from a compressed
       high band into a readable 0-to-1 spread
Crop:  keep both panels side by side with their color scales; the comparison is
       the point, so neither panel alone carries it
```

```text
Asset: Table 1 in Sun et al. 2022 (gender-bias example pairs with per-metric scores)
Shows: identical sentences differing only in a pronoun receiving large BERTScore
       gaps, with traditional metrics beside them for contrast
Crop:  retain the BERTScore column and at least one traditional-metric column so the
       gap is comparative, not absolute
```

```text
Asset: Table 2 in SummEval (Fabbri et al. 2021)
Shows: BERTScore-f, ROUGE-1, ROUGE-2 rows across the four quality dimensions, so a
       reader sees BERTScore's near-zero consistency correlation next to ROUGE's
Crop:  keep the four dimension columns and the ROUGE rows alongside the BertScore
       rows; a single-column crop loses the comparison
```

None of the other sources (repo README, rescale text, Kocmi, Hanna & Bojar) offer
a visual that carries an argument better than the prose already does.

## Discarded

```text
URL: https://arxiv.org/abs/2210.07626 — same paper as the ACL Anthology entry for
     Sun et al. 2022; cite the Anthology page, which is the version of record.
URL: https://arxiv.org/abs/2107.10821 — arXiv preprint of Kocmi et al.; cite the
     WMT 2021 Anthology page instead.
URL: https://arxiv.org/abs/2007.12626 — arXiv preprint of SummEval; cite the TACL
     Anthology page instead.
URL: https://github.com/huggingface/evaluate/blob/main/metrics/bertscore/README.md
     — same metric card as the Hugging Face space; one secondary entry is enough.
URL: https://paperswithcode.com/paper/a-fine-grained-analysis-of-bertscore — index
     page only; the paper itself (Anthology) is the source.
```

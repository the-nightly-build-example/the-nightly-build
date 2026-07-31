# Evidence — the-instruments/bleu

The evidence supports all three of the commission's teaching points with primary
sources read in full, formulas verified against the owning paper, and one
self-authored, hand-checked numeric example. Papineni et al. 2002 supplies the
modified n-gram precision formula, the clipping rule, the brevity penalty, and the
human-correlation experiments (with their real, modest sample sizes: 5 systems, 20
human judges, 250 rated sentence pairs). Callison-Burch et al. 2006 supplies the
misranking case (2005 NIST Arabic-English MT Eval: human 1st place finished 6th on
BLEU) with the exact statistics behind it. Post 2018 supplies the tokenization/
reference-count reproducibility problem and the sacreBLEU fix, with a verified,
reproducible 1.8-point swing from tokenization choice alone. Vaswani et al. 2017
confirms 28.4 BLEU EN-DE in three places in the same paper (abstract, Table 2,
running text), so the reader's held number is solid. The evidence is thinnest on
one point the brief flagged: BLEU's own correlation numbers vary enormously by
what systems and years are sampled (Papineni's r=0.99/0.96 came from one 5-system,
one-language-pair study; Reiter's 2018 meta-review of ten WMT years on the same
two language pairs finds correlations from -0.43 to 0.90). That volatility is
itself part of the story, not a gap to paper over: it is exactly why a bare BLEU
number needs its measurement conditions stated. The steelman is real and
well-sourced (Reiter: BLEU's system-level, corpus-scale MT correlation is
"mostly Medium or High"); the critique is also real and well-sourced (Mathur et
al. 2020: that correlation collapses once outlier systems are removed, and a
1-2 point BLEU gain is a coin flip on whether humans agree). Both should be held,
not resolved into a false single verdict.

## Sources

**1. Papineni, Roukos, Ward, Zhu. "Bleu: a Method for Automatic Evaluation of
Machine Translation." ACL 2002, pp. 311-318.**
URL: https://aclanthology.org/P02-1040/ (PDF: https://aclanthology.org/P02-1040.pdf)
Primary: this is the paper that defines BLEU; the four IBM authors report their
own method and their own correlation experiments. Read in full (all 8 pages).

What it establishes firsthand:
- Modified n-gram precision and the clipping rule, §2.1 (p.312): "one first
  counts the maximum number of times a word occurs in any single reference
  translation. Next, one clips the total count of each candidate word by its
  maximum reference count, adds these clipped counts up, and divides by the
  total (unclipped) number of candidate words." Footnote 2 gives the formula:
  `Countclip = min(Count, Max_Ref_Count)`.
- Their own worked toy example, §2.1 (p.312), Example 2: candidate "the the the
  the the the the." against two references ("The cat is on the mat." / "There
  is a cat on the mat.") — modified unigram precision = 2/7, versus a naive
  (unclipped) precision of 7/7. This is the paper's own illustration of why
  clipping is needed; the evidence file's worked example below is a distinct,
  self-authored case built to also show the brevity penalty at the same time.
- Corpus-level modified precision formula, §2.1.1 (p.312-313): pn = (sum over
  candidates, over n-grams, of Countclip) / (sum over candidates, over n-grams,
  of Count) — i.e., clipped-match n-grams over total candidate n-grams, summed
  across the whole test corpus, not sentence-by-sentence.
- Brevity penalty, §2.2.2-2.3 (p.313-314): BP = 1 if c > r; BP = e^(1-r/c) if
  c ≤ r, where c = candidate corpus length, r = "effective reference corpus
  length" (sum of each sentence's closest-length reference, the "best match
  length"). Final score: BLEU = BP · exp(sum of wn·log(pn)) for n=1..N, with
  N=4 and uniform weights wn=1/4 in their baseline (§2.3, p.314).
- Sample sizes for the correlation claims, honestly stated: §4 (p.315), "two
  groups of human judges. The first group, called the monolingual group,
  consisted of 10 native speakers of English. The second group, called the
  bilingual group, consisted of 10 native speakers of Chinese... None of the
  human judges was a professional translator." They judged 5 "systems" (2
  human translations, 3 commercial MT systems) on "a Chinese sentence subset
  extracted at random from our 500 sentence test corpus," "250 pairs of
  Chinese source and English translations," each rated 1 (very bad) to 5 (very
  good).
- The correlation figures the commission's hook depends on, §5 (p.316):
  "The high correlation coefficient of 0.99 indicates that BLEU tracks human
  judgment well" (monolingual group, Figure 5); "The correlation coefficient
  is 0.96" (bilingual group, Figure 6). Both computed over only 5 data points
  (the 5 systems), one language pair (Chinese-English), one domain, one lab.
- Their own stated limit on sentence-level use, footnote 4 (p.312): "BLEU only
  needs to match human judgment when averaged over a test corpus; scores on
  individual sentences will often vary from human judgments." This is the
  paper's own caveat, not an outside critique.
- §3 (p.314): reference-count sensitivity, stated by the authors themselves:
  on their ~500-sentence/40-story test corpus, "a human translator scored
  0.3468 against four references and scored 0.2571 against two references" —
  same translation, same test set, different score purely from reference
  count. Table 1 gives all 5 systems' scores against two references: S1=0.0527,
  S2=0.0829, S3=0.0930, H1=0.1934, H2=0.2571.
- Table 2 (p.315): paired t-statistics on 20 blocks of 25 sentences each,
  confirming the score differences are statistically significant (t=6, 3.4,
  24, 11 between adjacent systems) — this is the basis for BLEU being usable
  at all for ranking, given real corpus-level noise.

**2. Callison-Burch, Osborne, Koehn. "Re-evaluating the Role of BLEU in Machine
Translation Research." EACL 2006, pp. 249-256.**
URL: https://aclanthology.org/E06-1032/ (PDF: https://aclanthology.org/E06-1032.pdf)
Primary: the three authors report their own combinatorial analysis and their
own manual-evaluation experiment. Read in full (all 8 pages).

What it establishes firsthand:
- The 2005 NIST MT Eval misranking, §4 (p.253): "Last year's evaluation
  exercise (Lee and Przybocki, 2005) was startling in that Bleu's rankings of
  the Arabic-English translation systems failed to fully correspond to the
  manual evaluation. In particular, the entry that was ranked 1st in the human
  evaluation was ranked 6th by Bleu." The system ranked 1st by humans but 6th
  by BLEU was not a rule-based system — it was a hybrid entry: "monolingual
  English speakers selecting among alternative automatic translations of
  phrases in the Arabic source sentences and post-editing the result." The
  other six entries were "all phrase-based statistical machine translation
  system[s]... trained on the same parallel corpus," most using BLEU-based
  minimum-error-rate training. Table 4 (p.253) gives a concrete sentence pair:
  a hypothesis with more matching n-grams (27 unigrams, 20 bigrams, 15
  trigrams, 10 4-grams) but lower human scores (adequacy 3,2; fluency 3,2)
  than one with fewer matching n-grams (24, 19, 15, 12) but much higher human
  scores (adequacy 5,4; fluency 5,4) — the higher-scoring hypothesis used
  synonyms BLEU could not credit ("will not attend" for "would boycott,"
  "interfering" for "meddling").
- Statistical detail on the outlier effect, §4 (p.254): correlating the 7 NIST
  entries' BLEU scores against human adequacy scores gives Pearson R²=0.14
  with the outlier hybrid entry included, but R²=0.87 with it excluded;
  fluency correlation goes from R²=0.002 to R²=0.742 under the same removal
  (Figures 2-3).
- A second, independently constructed misranking case, §4 (p.254): the
  authors trained SMT systems on the French-English Europarl corpus (14-15
  million words/language) and compared a full-data SMT system, a
  deliberately weakened SMT system trained on 1/64 of that data (chosen so
  its BLEU score was "close to, but still higher than" the rule-based
  system's), and the commercial rule-based system Systran — all measured with
  BLEU on 2,000 held-out sentence pairs. Three judges then rated 300 French
  sentences per system for fluency and adequacy. Result, Figure 4 (p.254):
  "the Bleu score for the rule-based system (Systran) vastly underestimates
  its actual quality" — Systran had the lowest BLEU of the three but the
  highest or near-highest human scores.
- The combinatorics of BLEU's under-constraint, §3.1 (p.251): for a given
  hypothesis translation with k words and b matching bigrams, there are (k-b)!
  ways to permute the words around bigram-mismatch points without changing the
  BLEU score; for their worked example this is at least 40,320 permutations,
  and for some sentences in the actual 2005 NIST MT Eval data the number of
  same-scoring permutations exceeds 10^73 (Figure 1, p.252).
- The authors' own appropriate-use conclusion, §6 (p.255): "Appropriate uses
  for Bleu include tracking broad, incremental changes to a single system,
  comparing systems which employ similar translation strategies... Inappropriate
  uses for Bleu include comparing systems which employ radically different
  strategies... trying to detect improvements for aspects of translation that
  are not modeled well by Bleu, and monitoring improvements that occur
  infrequently within a test corpus."

**3. Post. "A Call for Clarity in Reporting BLEU Scores." WMT18 Research
Papers / arXiv:1804.08771.**
URL: https://arxiv.org/abs/1804.08771 (PDF: https://arxiv.org/pdf/1804.08771)
Primary: the author built sacreBLEU and reports his own measurement of the
tokenization problem. Read in full.

What it establishes firsthand:
- "BLEU" is a family of parameterized configurations, not one metric, §2.1:
  "Among these parameters are: The number of references used; for
  multi-reference settings, the computation of the length penalty; the maximum
  n-gram length; and smoothing applied to 0-count n-grams." Distinguishes
  *user-supplied* reference tokenization (error-prone, not comparable across
  papers) from *metric-internal* tokenization (comparable), §2.2.
- Quantified tokenization effect, Table 1 (p.3): scoring one WMT'17 system
  ("online-B") four different ways (basic Moses tokenization, compound
  splitting, an UNK-masking scenario, and WMT's own metric-internal
  tokenization) across 12 language-pair directions. The largest swing from
  changing only tokenization/preprocessing, holding the system and test set
  fixed, is 1.8 BLEU points on the cased German-English arc (de-en "range"
  row = 1.8) — this is the number the abstract cites: "finding differences as
  high as 1.8 between commonly used configurations."
- Reference-count effect, stated directly, §2.1 (p.2): "WMT 2017 includes two
  references for English-Finnish. Scoring the online-B system with one
  reference produces a BLEU score of 22.04, and with two, 25.25" — a 3.2-point
  swing from reference count alone, same system, same test set.
- Different reference counts across test sets create an unlabeled illusion of
  quality difference, §2.1 (p.2): "the NIST OpenMT Arabic-English and
  Chinese-English test sets provided four references and consequently yielded
  BLEU scores in the high 40s (and now, low 50s)" — much higher than typical
  1-2-reference WMT scores, for reasons that have nothing to do with
  translation quality.
- Dataset-identity trap, §2.4 (p.4): the WMT'14 English-German test set exists
  in two different versions under the same name — the original evaluation
  version has 2,737 sentences (after ~10% were removed for a data problem
  discovered during the event), and the corrected/restored version released
  afterward has 3,004 sentences. "Many researchers are unaware of this fact,
  and do not specify which version they use when reporting."
- Table 2 (p.3): a survey of whether seven well-cited MT papers' BLEU
  configuration can even be determined from the paper text. Vaswani et al.
  2017 (the Transformer paper) is listed as "user or user_lc (unclear)" — the
  paper that produced the reader's held 28.4 figure does not itself specify,
  in a machine-checkable way, exactly how that score was tokenized.
- sacreBLEU's fix, §3.3 (p.4-5): the tool "expects detokenized outputs,
  applying its own metric-internal preprocessing," auto-downloads WMT/IWSLT
  reference sets so users never touch them, and prints a version/signature
  string, e.g. `BLEU+c.mixed+l.en-de+#.1+s.exp+t.wmt14+tok.13a+v.1.2.10`,
  recording case handling, language pair, reference count, smoothing,
  dataset, tokenization scheme, and tool version.

**4. Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin.
"Attention Is All You Need." NeurIPS 2017 / arXiv:1706.03762.**
URL: https://arxiv.org/abs/1706.03762 (PDF: https://arxiv.org/pdf/1706.03762)
Primary: the eight authors report their own model's own measured scores. Read
in full (all 15 pages plus appendix figures).

What it establishes firsthand:
- 28.4 BLEU EN-DE confirmed in three independent places in the same document,
  all consistent: Abstract ("Our model achieves 28.4 BLEU on the WMT 2014
  English-to-German translation task, improving over the existing best
  results, including ensembles, by over 2 BLEU"); Table 2 (p.8), Transformer
  (big) row, EN-DE column, bolded, 28.4; running text §6.1 (p.8): "the big
  transformer model... establishes a new state-of-the-art BLEU score of
  28.4."
- Training conditions behind that number, §5.1-5.2 (p.7) and Table 2 (p.8):
  trained on WMT 2014 English-German, ~4.5 million sentence pairs, byte-pair
  encoded with a shared ~37,000-token vocabulary; the "big" model trained
  300,000 steps (3.5 days) on 8 NVIDIA P100 GPUs, 2.3×10^19 FLOPs. The base
  model (not the 28.4 one) scored 27.3 BLEU EN-DE at roughly 1/7th the
  training cost (3.3×10^18 FLOPs).
- Internal inconsistency, noted for completeness, not relevant to the 28.4
  EN-DE figure this lesson cites: the paper's EN-FR score for the same "big"
  model is given as 41.8 in both the Abstract and Table 2, but the running
  prose in §6.1 (p.8) says "our big model achieves a BLEU score of 41.0."
  This is an error/inconsistency in the source paper itself on a number this
  lesson does not use; the EN-DE 28.4 figure is fully consistent across all
  three locations.

**5. Mathur, Baldwin, Cohn. "Tangled up in BLEU: Reevaluating the Evaluation
of Automatic Machine Translation Evaluation Metrics." ACL 2020, pp. 4984-4997.**
URL: https://aclanthology.org/2020.acl-main.448/ (PDF: https://aclanthology.org/2020.acl-main.448.pdf)
Primary: original statistical re-analysis of the WMT19 metrics-task data,
conducted and reported by the paper's own authors (not a summary of others'
findings). Read in full including appendix tables.

What it establishes firsthand:
- WMT's correlation methodology changed over time, §2 (p.4985): Spearman's
  rank correlation was the official measure from 2007, replaced by Pearson's
  correlation in 2014 (citing Bojar et al. 2014) — meaning "BLEU correlates at
  r=X" claims from different years are not even using the same statistic.
- Outlier sensitivity, quantified, Table 2 (p.4989): for English-German
  (WMT19, 22 systems), BLEU's correlation with human Direct Assessment scores
  is r=0.97 with all systems included, dropping to r=0.81 once the two
  clearest outlier systems are removed. For English-Kazakh, BLEU correlation
  drops from r=0.85 (all systems) to r=0.58 (outliers removed) (Table 1,
  p.4989).
- The practical stakes of small BLEU deltas, Conclusion (p.4992): "Most
  published work report BLEU differences of 1-2 points, however at this level
  we show this magnitude of difference only corresponds to true improvements
  in quality as judged by humans about half the time." This is based on 1,362
  pairwise system comparisons across WMT19 language pairs (§5, Figure 5,
  p.4991).
- Their own recommendation, Conclusion (p.4992): "stop using BLEU or TER for
  evaluation of MT, and instead use CHRF, YISI-1, or ESIM" — while also
  stressing "human evaluation must always be the gold standard... all
  automatic metrics make for inadequate substitutes."
- Confirms BLEU's aggregate reference-based correlation with human DA scores
  is "greater than r=0.8 for all language pairs" in WMT19 when not
  restricted to top-N or outlier-free subsets, §4.1 (p.4986) — i.e., the
  metric is not useless, its reliability is conditional on the system sample.

**6. Post, M. sacreBLEU GitHub repository README (project documentation).**
URL: https://github.com/mjpost/sacrebleu/blob/master/README.md
Primary: tool documentation written by the same author as source 3, describing
his own released software; not a third party's account of the tool.

What it establishes firsthand:
- Statement of the problem the tool exists to fix: "Comparing BLEU scores is
  harder than it should be. Every decoder has its own implementation, often
  borrowed from Moses, but maybe with subtle changes... Different flags
  passed to each of these scripts can produce wide swings in the final
  score."
- Purpose statement: sacreBLEU provides "hassle-free computation of
  shareable, comparable, and reproducible BLEU scores."
- Example usage: `cat output.detok.txt | sacrebleu -t wmt17 -l en-de` (or
  `sacrebleu -t wmt17 -l en-de -i output.detok.txt`).
- Signature/version string format, e.g.
  `nrefs:1|case:mixed|eff:no|tok:13a|smooth:exp|version:2.0.0` — records
  reference count, case handling, tokenizer, smoothing method, and tool
  version, so a reported score is reproducible and its exact conditions are
  auditable.

**7. Google Cloud, "The BLEU translation quality metric," Cloud Translation
documentation.**
URL: https://docs.cloud.google.com/translate/docs/bleu-scores
Secondary: Google's documentation team explaining a third-party academic
metric (BLEU) to Cloud Translation customers; Google did not create BLEU and
is reporting/interpreting it, not originating the claim.

What it establishes:
- A practitioner-facing quality-tier reading of the BLEU scale (0-100 form):
  "<10: Almost useless"; "10-19: Hard to get the gist"; "20-29: The gist is
  clear, but has significant grammatical errors"; "30-40: Understandable to
  good translations"; "40-50: High quality translations"; "50-60: Very high
  quality, adequate, and fluent translations"; ">60: Quality often better
  than human." Useful for giving the reader a scale they can hold a number
  against, per the house numbers standard — but note this table gives no
  citation of its own for where these boundaries come from; treat it as
  Google's practitioner guidance, not a validated psychometric scale.
- Direct statement on tokenization sensitivity, aimed at customers who might
  otherwise take a single BLEU number at face value: "BLEU relies on
  normalization and tokenization. Prior to computing the BLEU score, the
  reference and candidate translations are normalized and tokenized. The
  choice of steps in those processes significantly affect the final BLEU
  score." This corroborates Post 2018's technical finding in a plain-language,
  vendor-facing register — evidence that the tokenization-comparability
  problem is not just an academic footnote but something a major commercial
  provider now warns its own paying customers about.

**8. Reiter. "A Structured Review of the Validity of BLEU." Computational
Linguistics 44(3):393-401, 2018.**
URL: https://aclanthology.org/J18-3002/ (PDF: https://aclanthology.org/J18-3002.pdf)
Secondary: a structured meta-review that aggregates and classifies 284
correlation results reported across 34 other papers; Reiter ran none of the
underlying correlation studies himself. Read in full.

What it establishes:
- The steelman case for BLEU, stated as the paper's own conclusion, §3 (p.397)
  and §5 (p.399): "BLEU–human correlations are poor for NLG... For MT, they
  are poor for text-level correlations, but reasonable for system-level
  correlations... the only kind of BLEU–human correlation that is mostly
  Medium or High in the surveyed papers is system-level BLEU–human
  correlations for MT." Conclusion: "I think the surveyed papers support this
  [diagnostic] use of BLEU" for MT, but "the evidence does not support using
  BLEU to evaluate other types of NLP systems (outside of MT)," nor "to
  evaluate individual texts rather than NLP systems," nor as "the primary
  evaluation technique" for scientific hypothesis testing in a published
  paper.
- Correlation classification scale used (borrowed from clinical
  surrogate-endpoint methodology), §3 (p.397): High ≥0.85; Medium 0.70-0.85;
  Low 0-0.70; Negative <0.
- Year-by-year volatility for the *same* language pairs and domain, Table 1
  (p.399): BLEU's correlation with WMT ranking-based human evaluation for
  German-English and English-German MT (news domain), 2007-2016. Values
  range from 0.12 (WMT08, German-English) and -0.43 (WMT09, English-German)
  up to 0.90 (WMT13, German-English) and 0.88 (WMT16, German-English) — full
  series preserved in Numbers below.
- Reiter's own gloss on this volatility, §3 (p.398): "One would hope that
  BLEU–human correlations would be similar in such a constrained context, but
  in fact correlations vary widely... This suggests that whether BLEU
  correlates with human evaluations is very dependent on the details of the
  systems being evaluated, the exact corpus texts used, and the exact
  protocol used for human evaluations."

## Contradictions

- **Steelman vs. critique, both well-sourced, genuinely in tension.** Reiter
  2018 (source 8), reviewing 34 papers' worth of evidence through 2017,
  concludes system-level, corpus-scale MT correlation is "mostly Medium or
  High" and defends BLEU for its originally intended diagnostic use. Mathur
  et al. 2020 (source 5), re-analyzing the more recent WMT19 data (mostly
  neural systems), finds that same correlation collapses once outlier systems
  are removed and recommends retiring BLEU for CHRF/YiSi/ESIM. Both papers
  are correct about their own data; they are not measuring identical things
  (different years, largely different underlying MT technology — rule-based
  and early statistical systems dominate the older WMT years Reiter surveys,
  neural systems dominate Mathur's WMT19 sample). The honest read is that
  BLEU's system-level correlation is real but conditional, not a fixed
  property of the metric — which is itself evidence for the lesson's claim
  that a bare correlation number needs its measurement conditions stated.
- **Correlation figures vary by an order of magnitude depending on sample.**
  Papineni's own r=0.99/0.96 (source 1) came from a single 5-system,
  one-language-pair, one-lab study. Reiter's WMT table (source 8) shows the
  same two language pairs producing correlations from -0.43 to 0.90 across
  ten different years. Mathur (source 5) shows a single language pair's
  correlation shifting by up to 0.27 (0.85→0.58) just by excluding 1-2
  outlier systems from an 11-system sample. None of these contradict each
  other's arithmetic — they are simply not measuring the same thing, which is
  precisely the comparability problem the lesson needs to teach.
- **Vaswani et al. 2017 contains an internal inconsistency**, noted under
  source 4: the EN-FR BLEU score for "Transformer (big)" is 41.8 in the
  abstract and in Table 2, but 41.0 in the §6.1 running text. This does not
  touch the EN-DE 28.4 figure this lesson cites (consistent in all three
  places), but if the writer or editor cross-checks EN-FR anywhere, this is
  why the numbers might look off — it is an error in the source, not in this
  research.
- **Post's Table 2 shows even the Transformer paper itself is an example of
  the underspecification problem it documents**: Vaswani et al. 2017 is
  listed as "user or user_lc (unclear)" tokenization — i.e., the paper
  producing the reader's held 28.4 number does not itself specify, in a
  checkable way, exactly what tokenization scheme produced it. This is not a
  contradiction between sources so much as Post's paper directly implicating
  the reader's anchor number in the very problem the lesson is about.

## Numbers

**Worked example (self-authored, hand-verified against the Papineni 2002
formulas in source 1; not copied from any source's own example).**

Candidate translation (11 words): "the small brown dog chased the red ball
across the yard"
Single reference translation (12 words): "the small brown dog quickly chased
the red ball across the yard"

The candidate is the reference with one adverb ("quickly") removed — a
realistic case of a translation that drops a word's worth of meaning while
staying otherwise correct, so it lets both the n-gram precision and the
brevity penalty do real work at once.

*Step 1 — modified n-gram precision, n=1 to 4 (clipped counts):*

| n | candidate n-grams | matched (clipped) | total candidate n-grams | precision pn |
|---|---|---|---|---|
| 1 | the, small, brown, dog, chased, the, red, ball, across, the, yard | 11 | 11 | 11/11 = 1.000 |
| 2 | (the,small) (small,brown) (brown,dog) (dog,chased) (chased,the) (the,red) (red,ball) (ball,across) (across,the) (the,yard) | 9 | 10 | 9/10 = 0.900 |
| 3 | 9 candidate trigrams (see below) | 7 | 9 | 7/9 = 0.778 |
| 4 | 8 candidate 4-grams (see below) | 5 | 8 | 5/8 = 0.625 |

Detail on where matches fail (the only reason any n-gram fails to match is
that it straddles the point where "quickly" was deleted):
- Unigrams: every candidate word appears in the reference (the reference
  contains a strict superset of the candidate's words); "the" appears 3 times
  in the candidate and 3 times in the reference, so its clipped count is
  min(3,3)=3, not penalized. All 11 unigrams match. p1 = 11/11 = 1.000.
- Bigrams: candidate bigram (dog,chased) has no match — the reference has
  (dog,quickly) at that position instead. The other 9 of 10 candidate bigrams
  match exactly. p2 = 9/10 = 0.900.
- Trigrams: candidate trigrams (brown,dog,chased) and (dog,chased,the) have
  no match (reference has (brown,dog,quickly) and (dog,quickly,chased)
  instead). The other 7 of 9 match. p3 = 7/9 ≈ 0.778.
- 4-grams: candidate 4-grams (small,brown,dog,chased), (brown,dog,chased,the),
  and (dog,chased,the,red) have no match. The other 5 of 8 match. p4 = 5/8 =
  0.625.

*Step 2 — geometric mean of the four precisions, uniform weights wn=1/4
(Papineni et al. 2002, §2.3, p.314 formula):*

p1 × p2 × p3 × p4 = 1.000 × 0.900 × 0.778 × 0.625 = 0.4375 (using the exact
fraction 7/9 rather than the rounded 0.778: 1 × 0.9 × 7/9 × 0.625 = 0.4375
exactly)

Fourth root of 0.4375 ≈ 0.813 (geometric mean of the four precisions)

*Step 3 — brevity penalty (Papineni et al. 2002, §2.2.2-2.3, p.313-314):*

c (candidate length) = 11; r (reference length, single reference) = 12.
Since c ≤ r: BP = e^(1 − r/c) = e^(1 − 12/11) = e^(−1/11) ≈ 0.913

*Step 4 — final score:*

BLEU = BP × (geometric mean of precisions) ≈ 0.913 × 0.813 ≈ 0.742

So this candidate — grammatically fine, missing one adverb's worth of
meaning — scores roughly 0.74 (or 74 on the common 0-100 reporting scale).
Note how much of that penalty (about 8.7 percentage points, from 0.813 down
to 0.742) comes purely from being one word short, on top of the roughly 19-point
gap already caused by imperfect n-gram matching (1.000 → 0.813 geometric mean).
Both mechanisms — clipped precision and brevity penalty — are doing real,
separable work in this single sentence.

**Other verified figures:**

- 28.4: BLEU score, Transformer (big), WMT 2014 English-German, Vaswani et al.
  2017, confirmed in Abstract, Table 2, and §6.1 text (source 4). Training
  cost 2.3×10^19 FLOPs, 300,000 steps, 3.5 days on 8 P100 GPUs.
- Human correlation reported by Papineni et al. 2002 (source 1): r=0.99
  (monolingual group, 10 judges), r=0.96 (bilingual group, 10 judges) — both
  computed over only 5 systems, one language pair (Chinese-English), 250
  rated sentence pairs.
- Reference-count effect on the *same* translation, same test set (Papineni
  et al. 2002, source 1, §3, p.314): 0.3468 (4 references) vs. 0.2571 (2
  references) — a 0.09-point (26%) relative swing from reference count alone.
- Reference-count effect, independently confirmed by Post 2018 (source 3),
  WMT'17 English-Finnish, online-B system: 22.04 BLEU (1 reference) vs. 25.25
  BLEU (2 references) — a 3.2-point swing.
- Tokenization effect (Post 2018, source 3, Table 1): up to 1.8 BLEU points
  from tokenization/preprocessing choice alone, holding system and test set
  fixed (cased German-English arc, WMT'17 online-B system).
- 2005 NIST Arabic-English MT Eval misranking (Callison-Burch et al. 2006,
  source 2, §4, p.253): human-judged 1st place finished 6th on BLEU.
  Correlation with human adequacy: R²=0.14 with the outlier system included,
  R²=0.87 with it excluded (7 systems total).
- Systran (rule-based) vs. SMT case (Callison-Burch et al. 2006, source 2,
  §4, p.254): manual evaluation of 300 sentences by 3 judges found Systran's
  human quality scores higher than an SMT system with a marginally higher
  BLEU score, evaluated on 2,000 held-out sentence pairs.
- Outlier sensitivity in modern (2019) data (Mathur et al. 2020, source 5,
  Table 1-2, p.4989): English-German BLEU-human correlation r=0.97 (all 22
  systems) → r=0.81 (2 outliers removed). English-Kazakh: r=0.85 (all 11
  systems) → r=0.58 (outliers removed).
- 1-2 point BLEU differences reflect real human-judged improvement only
  "about half the time" (Mathur et al. 2020, source 5, Conclusion, p.4992),
  based on 1,362 pairwise system comparisons at WMT19.
- WMT year-by-year correlation series, German-English (GE) and
  English-German (EG) MT, news domain, human ranking-based evaluation
  (Reiter 2018, source 8, Table 1, p.399) — full series, useful if a chart is
  wanted:

  | Event | Correlation type | German→English | English→German |
  |---|---|---|---|
  | WMT07 | Spearman | 0.40 | 0.26 |
  | WMT08 | Spearman | 0.12 | 0.58 |
  | WMT09 | Spearman | 0.41 | −0.43 |
  | WMT10 | Spearman | 0.52 | 0.39 |
  | WMT11 | Spearman | 0.48 | 0.44 |
  | WMT12 | Spearman | 0.67 | 0.22 |
  | WMT13 | Spearman | 0.90 | 0.83 |
  | WMT14 | Pearson | 0.83 | 0.22 |
  | WMT15 | Pearson | 0.86 | 0.57 |
  | WMT16 | Pearson | 0.88 | 0.78 |

- Google Cloud's practitioner BLEU quality tiers (source 7): <10 "almost
  useless"; 10-19 "hard to get the gist"; 20-29 "gist is clear, significant
  grammatical errors"; 30-40 "understandable to good"; 40-50 "high quality";
  50-60 "very high quality"; >60 "quality often better than human." (No
  citation given by Google for these exact boundaries — use as practitioner
  color, not as a validated scientific scale.)

## Source assets

- **Post 2018, Table 1** (source 3, p.3): a 12-column, 2-row-block numeric
  table of BLEU scores for one system (online-B) under 4 tokenization schemes
  across 12 WMT'17 language-pair directions, cased and uncased. This is
  extractable, reproducible-from-the-paper data (not a screenshot need) and
  is the strongest chart candidate for the lesson: a small bar or dot chart
  showing the same system-translation scoring differently by up to 1.8 BLEU
  points depending purely on tokenization would make the "measured how"
  point visually, with the paper as the cited source. A crop must not use
  the "unk" column without labeling it as the paper's deliberately
  hypothetical/adversarial scenario, not a normal configuration.
- **Reiter 2018, Table 1** (source 8, p.399): the 10-year WMT correlation
  series reproduced in full under Numbers above. A simple line or dot chart
  of these ten years for one language pair (e.g., English-German) would
  visually carry the "correlation is not a fixed property of the metric"
  point better than prose. Caption must state this is Spearman's correlation
  for 2007-2013 and Pearson's for 2014-2016 (the underlying statistic
  changed, per Mathur et al. 2020 source 5) — do not present it as one
  continuous, uniformly measured series without that caveat.
- **Callison-Burch et al. 2006, Figure 1** (source 2, p.252): a scatterplot of
  hypothesis-translation length against number of same-BLEU-score
  permutations (log scale, up to 10^73). This is a genuine image in the
  source PDF, not just a table; if reproduced, it must be redrawn from the
  paper's own methodology (their Equation 1, (k−b)!) since the underlying raw
  per-sentence data is not published separately from the plot.
- Papineni et al. 2002, Figures 1-2 and 5-7 (source 1): bar charts and
  scatterplots of the 5-system precision/correlation data. The underlying
  numbers for Figures 5-7 are not given as a table in the paper (only Table 1
  gives BLEU scores for the 5 systems, p.314); a faithful redraw of the
  correlation scatterplots would require digitizing the original figures,
  which is not warranted for this lesson. None found beyond what is already
  in Numbers above (Table 1's five scores).
- Google Cloud's quality-tier table (source 7) is plain text on the page, not
  an image; if used, present as the article's own table, citing Google Cloud
  documentation, not a screenshot.

## Discarded

- Doddington, G. (2002), "Automatic evaluation of machine translation quality
  using n-gram co-occurrence statistics," HLT 2002, pp. 138-145 (the NIST
  metric paper, a commission-suggested additional primary candidate). Located
  bibliographic citations to it in three other read sources (Callison-Burch
  et al. 2006, Reiter 2018, Mathur et al. 2020) but could not locate a URL for
  the paper itself that resolves to verified full text (not on ACL Anthology
  under a checkable ID; only paywalled ACM/ResearchGate listings found).
  Discarded rather than cite an unverified URL, per house policy. The NIST
  metric's existence and its arithmetic-mean/different-brevity-penalty
  departure from BLEU is attested secondhand by Reiter 2018 (source 8, §2.2,
  p.395: "I did not consider NIST to be a standard version of BLEU") but not
  independently verified against Doddington's own text.
- General web-search summaries about Google Translate/NMT marketing claims
  ("Nearly Indistinguishable From Human Translation," data-contamination
  claims of up to 30 BLEU points). Surfaced only as aggregated search-engine
  summaries, not as a single opened, verified primary or secondary document;
  discarded rather than cite secondhand.
- Various blog/aggregator pages on chrF, COMET, and BLEURT (Saturn Cloud,
  Traceloop, Slator, NLLB.com, and similar) surfaced by web search. Used only
  to orient which successor metrics are worth naming (matches the commission's
  own list: chrF, COMET, BLEURT); not cited, since none were opened as a full
  primary or vetted secondary document and the commission caps how much space
  successor metrics should get ("only as much as the lesson needs").
- Wikipedia's "BLEU" article: read as a sanity check while orienting, not
  cited — it is tertiary and everything useful in it traces back to sources
  already read directly above.

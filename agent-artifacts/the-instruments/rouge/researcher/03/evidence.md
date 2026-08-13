# Evidence: the-instruments/rouge (03)

This is the third, additive researcher round. It carries rounds 01 and 02 forward
unchanged in their findings and closes the one remaining policy gap round 02
flagged: the record had no third-party secondary source. Round 03 reads one
firsthand and folds it into the record. Every source, figure, contradiction, and
asset from round 02 is preserved below; the only new material is the Sai,
Mohankumar & Khapra survey source entry, one source-asset note, and the updated
source-count paragraph. Nothing from round 02 was removed or rewritten on the
merits.

What round 03 adds. Sai, Mohankumar & Khapra, "A Survey of Evaluation Metrics
Used for NLG Systems" (ACM Computing Surveys, 2022; read firsthand via the
arXiv:2008.12009v2 full text) is a peer-reviewed survey that reports on ROUGE from
outside the metric's authoring parties. It synthesizes the field's characterization
of ROUGE rather than owning any first-party measurement: it places ROUGE in a
taxonomy of automatic evaluation metrics (context-free, untrained, n-gram/word
based), states plainly that ROUGE was designed for summarization and has since
been adopted for other NLG tasks, and catalogs the standing criticisms of overlap
metrics including ROUGE (poor and high-variance correlation with human judgment,
uninterpretability, meaning-insensitivity, and the specific point that summarization
metrics do not check factual consistency). This is exactly the "compact, citable
outside characterization of ROUGE's standing and known limits" the brief asked for,
and it satisfies the source policy's "at least 1 secondary" floor with a genuine
third-party secondary, not the self-report model card.

The round 02 summary, preserved. The record firmly supports how a ROUGE number is
built (Lin 2004, read firsthand with the paper's own worked sentences and a second
worked example computed and hand-checked here) and the evaluation context that made
it the standard (the NIST-authored "DUC in Context"). It supports the honest center
that round 01 established: ROUGE is strong on consistency but confounded, weak on
coherence and relevance (SummEval), best in its single-document-news home setting
and degrading off-domain, and structurally meaning-blind (Lin's own reversed-sentence
example). Round 01 corrected the commission's too-clean claim that meta-evaluations
found ROUGE "correlates weakly with quality and consistency," and that correction
stands.

Round 02 added the strongest form of the "what ROUGE cannot support" evidence,
firsthand. Maynez et al. 2020 measured ROUGE directly against human faithfulness and
factuality judgments on abstractive summaries and found ROUGE's Spearman correlation
to be very weak (ROUGE-1/2/L between 0.10 and 0.20), far below a textual-entailment
measure (0.431 with faithfulness). Kryscinski et al. 2020 supplies the field's
definitional statement that overlap metrics do not account for factual consistency,
plus the magnitude of the problem it retells (up to 30% of abstractive summaries
factually inconsistent) and an alternative metric (FactCC). Graham 2015 supplies the
older methodological critique: on DUC-2004 the correlation of ROUGE with human
assessment swings from 0.79 down to 0.29 depending purely on which of 192 variants
you pick, the recommended variants were suboptimal, and BLEU does as well as the best
ROUGE.

One important synthesis holds the two faithfulness pictures together. SummEval found
ROUGE's correlation with human *consistency* moderate to strong (ROUGE-1/2/3 =
0.53/0.59/0.71 Kendall tau) but read it as an artifact of low model abstractiveness.
Maynez, working on genuinely abstractive XSum summaries, found ROUGE's correlation
with human *faithfulness* near zero. These do not conflict: where summaries are
extractive, ROUGE tracks faithfulness by accident; where they are abstractive, it
does not track it at all. This is the defensible spine of the commission's "cannot
support" section.

Two cautions the writer must keep. First, Maynez does not show that high ROUGE means
unfaithful. Its best model on ROUGE (BERTS2S) is also its most faithful. The finding
is that ROUGE does not *track* faithfulness at the summary level, not that the two
are opposed. Second, Graham's numbers are not a "ROUGE is weak" result. Its best
variant correlates 0.786 with human assessment, a strong figure in ROUGE's home
setting. Graham is evidence of variant fragility and evaluation methodology, not of
ROUGE failing.

Source count and policy (updated this round). Nine sources are now read firsthand:
Lin 2004, "DUC in Context," Bhandari 2020, Fabbri (SummEval) 2021, Maynez 2020,
Kryscinski 2020, Graham 2015, the facebook/bart-large-cnn model card, and, new this
round, Sai, Mohankumar & Khapra 2022 (the NLG-metrics survey). Seven are academic
primaries (Lin, DUC in Context, Bhandari, Fabbri, Maynez, Kryscinski, Graham). One
is a self-report artifact (the BART model card), held apart from the primaries. One
is now a genuine third-party secondary (the survey). The policy floor is met on every
count: at least 8 sources (9), at least 4 primary (7), at least 1 secondary (1), all
read firsthand. The round-02 note that "none of the eight is an outside party
reporting on another's claim" is now resolved by the survey and is superseded; it is
left in the Contradictions section as a record of the gap that was closed, with a
pointer to this resolution.

## Sources

```text
URL:         https://aclanthology.org/W04-1013/  (PDF: https://aclanthology.org/W04-1013.pdf)
Kind:        primary. Chin-Yew Lin authored ROUGE; this paper defines and owns the metric.
Establishes: The definitions of ROUGE-N and ROUGE-L, the acronym, the DUC evaluation
             context, and the paper's own meaning-blindness example.
Paraphrase:  ROUGE = "Recall-Oriented Understudy for Gisting Evaluation" (Abstract). ROUGE-N
             (Sec. 2, Eq. 1) is "an n-gram recall between a candidate summary and a set of
             reference summaries": numerator sums, over every reference and every n-gram in it,
             the count of n-grams co-occurring in the candidate (clipped to the reference count);
             denominator sums the total n-grams on the reference side. Lin states plainly it "is
             a recall-related measure because the denominator ... is the total sum of the number
             of n-grams occurring at the reference summary side," and contrasts it with BLEU,
             "a precision-based measure." ROUGE-L (Sec. 3, Eqs. 2-4) views a sentence as a word
             sequence, takes the longest common subsequence (LCS: an in-order, not necessarily
             contiguous, match), and forms an F-measure of LCS recall R_lcs = LCS(X,Y)/m and
             LCS precision P_lcs = LCS(X,Y)/n; "In DUC, beta is set to a very big number ...
             Therefore, only R_lcs is considered." ROUGE-L is 1 when X=Y and 0 when nothing
             matches. Section 6: DUC 2001/2002/2003 supplied the human judgments; ROUGE scores
             were correlated (Pearson/Spearman/Kendall) against human "coverage" scores; ROUGE-2
             was strongest among ROUGE-N for 100-word single-doc, ROUGE-1/L/W best for very short
             summaries. Multi-document correlations "rarely reached high 90%."
Locators:    Abstract; Sec. 2 and Eq. 1; Sec. 3.1 and Eqs. 2-4; Sec. 6; Tables 1-3.
Quote:       "Formally, ROUGE-N is an n-gram recall between a candidate summary and a set of
             reference summaries." (Sec. 2)

--- The paper's own meaning-blindness example (Sec. 3.1), read firsthand ---
             Reference S1 "police killed the gunman". Candidates S2 "police kill the gunman" and
             S3 "the gunman kill police" both share exactly one bigram with S1 ("the gunman"), so
             both get the identical ROUGE-2 recall of 1/3, "However, S2 and S3 have very different
             meanings." ROUGE-L separates them (S2 = 3/4 = 0.75, S3 = 2/4 = 0.5, with beta=1),
             but ROUGE-2 cannot. This is Lin's own demonstration that n-gram overlap never reads
             meaning; a reversed, near-nonsensical sentence ties a correct one.
```

```text
URL:         https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50955
             (This is NIST's PDF-serving endpoint, not the document's landing page. Canonical
             citation: Over, Dang, Harman, "DUC in Context," Information Processing & Management
             43(6):1506-1520, 2007. The writer should link the NIST publication record or the
             Springer/IPM page; the endpoint above is the route this text was read through.)
Kind:        primary. Authored by Paul Over, Hoa Dang, Donna Harman of NIST, the body that ran DUC.
Establishes: What DUC/TAC are, what reference ("model") summaries are, the SEE coverage tool,
             ROUGE's role and its defense, and the lead-baseline point.
Paraphrase:  DUC ran 2001-2006 at NIST, sponsored initially by DARPA, growing from 15 groups to
             over three dozen; it "mainly concentrated on intrinsic evaluation." Human "model
             (also known as 'manual' or 'gold standard') summaries" are the references a system
             output ("peer") is scored against. Content coverage is "the degree to which one
             summary (automatically created) conveys the same information as another (manually
             created)"; from 2001-2004 it was judged with the Summary Evaluation Environment (SEE,
             Lin 2001), each peer judged against only one model. ROUGE was built to automate
             coverage scoring; the paper credits it: "Extensive experiments with ROUGE have
             demonstrated reasonable correlation with manual coverage judgments that makes it
             useful in system development via hill-climbing," while noting "ROUGE's treatment of
             multi-word expressions and function words is not ideal." Crucially for the misled
             case: because of "the pyramidal structure of newspaper articles," "simple baseline
             systems creating summaries from the first sentence(s)" were "difficult to beat," and
             across the years "automatic summaries seldom performed better than simple baselines
             based on the structure of news articles." Approaches "have been largely extractive."
             One cited study (Copeck & Szpakowicz 2004) found "no more than 55% of the vocabulary
             items found in a given model summary occur in the corresponding source document(s)."
Locators:    Secs. 1, 6, 7, 8.2 (SEE, ROUGE, Pyramid); Sec. 9 conclusions; Table 1; Table 2.
Quote:       "automatic summaries seldom performed better than simple baselines based on the
             structure of news articles" (Sec. 9)
```

```text
URL:         https://aclanthology.org/2020.emnlp-main.751/
             (PDF: https://aclanthology.org/2020.emnlp-main.751.pdf)
Kind:        primary. Bhandari, Gour, Ashfaq, Liu, Neubig (CMU), EMNLP 2020; owns the REALSumm
             meta-evaluation and its human-judgment dataset.
Establishes: A modern meta-evaluation of ROUGE and semantic metrics on CNN/DailyMail vs. TAC.
Paraphrase:  Motivation: "for nearly 20 years ROUGE has been the standard evaluation in most
             summarization papers." They collect LitePyramid (Semantic Content Unit) human
             judgments on 100 CNN/DailyMail documents across 25 top systems (14 abstractive,
             11 extractive), ~10,000 annotations (7,742 kept after removing noisy workers,
             Krippendorff alpha 0.66). Headline finding is dataset-dependence, NOT that ROUGE is
             weak: on CNN/DailyMail "ROUGE metrics consistently perform well," and "R-2
             significantly outperforms all others" on the abstractive and mixed sets, beating
             the semantic metrics (MoverScore, JS-2) that had been best on TAC. The genuine
             negative findings: (1) as one restricts to the top-k strongest systems, "ROUGE-2
             de-correlates with humans" (even negative correlation for small k on TAC-2008 and
             CNNDM-Mix); (2) metric rankings do not transfer across datasets; (3) a metric good at
             comparing summaries can "point in the wrong direction when comparing systems"
             (MoverScore: 0.05 system-level vs 0.74 summary-level correlation on CNNDM-Ext).
             Correlations are shown only as bar charts (Figs. 2-8); the paper prints almost no
             exact ROUGE decimals, so specific ROUGE correlation numbers cannot be quoted from it.
Locators:    Abstract; Table 1 (experiment summary); Sec. 2.3 (recall variant used); Secs.
             4.1-4.4 and Figs. 2-8; Sec. 6.
Quote:       "conclusions about evaluation metrics on older datasets do not necessarily hold on
             modern datasets and systems." (Abstract)
```

```text
URL:         https://arxiv.org/abs/2007.12626  (read: arXiv:2007.12626v4 PDF)
             Canonical: Fabbri et al., TACL 9 (2021) 391-409, https://doi.org/10.1162/tacl_a_00373
             (the TACL page gates automated fetches with HTTP 403 but resolves for a reader.)
Kind:        primary. Fabbri, Kryscinski, McCann, Xiong, Socher, Radev (Yale/Salesforce); owns
             the SummEval metric re-evaluation and its expert human-judgment table.
Establishes: The strongest exact correlation numbers, and the honest, complicated picture of
             what ROUGE does and does not track.
Paraphrase:  They re-evaluate 14 metrics against 23 models (44 outputs), and collect human
             judgments for 16 models on 100 CNN/DailyMail articles, each summary scored by 3
             expert and 5 crowd annotators on a 1-5 Likert scale (12,800 annotations) over four
             dimensions: Coherence, Consistency ("the factual alignment between the summary and
             the summarized source. A factually consistent summary contains only statements that
             are entailed by the source document"), Fluency, Relevance. Table 2 (Kendall's tau,
             system-level, expert annotations, multi-reference with 11 references) is the money
             table. The finding: "most metrics have the lowest correlation within the coherence
             dimension, where the correlation strength can be classified as weak or moderate," and
             relevance is also low-to-moderate; consistency and fluency correlate more strongly,
             but the authors caution that "the strong correlation with consistency could be
             attributed to the low abstractiveness of most neural models" -- i.e. it is likely an
             artifact, not evidence ROUGE measures faithfulness. Higher-order ROUGE (ROUGE-1/2/3)
             correlates "substantially higher" than ROUGE-L. On faithfulness specifically, the
             Related Work reports (citing Maynez et al. 2020 and Kryscinski et al. 2020) that up
             to 30% of generated summaries hallucinate facts and that "currently available
             evaluation methods, such as ROUGE and BertScore, are not sufficient to study the
             problem." Table 3: the CNN/DailyMail gold reference summaries themselves scored only
             4.47 consistency / 3.26 coherence / 3.77 relevance -- below the LEAD-3 extractive
             baseline (4.98 / 4.16 / 4.14) -- because references contain clickbait and hyperlinks
             the annotators read as hallucinations. Table 4a: the best ROUGE-1 scores go to
             abstractive pretrained models (T5 0.4479, BART 0.4416, Pegasus 0.4408), above LEAD-3
             (0.3994) -- so on this modern data ROUGE does not simply favor extractive output.
Locators:    Abstract; Sec. 4.3 (dimension definitions); Table 2 (Kendall tau); Sec. 5.2
             (interpretation); Table 3 (human ratings); Table 4a (ROUGE by model); Related Work.
Quote:       "the strong correlation with consistency could be attributed to the low
             abstractiveness of most neural models" (Sec. 5.2)
```

```text
URL:         https://aclanthology.org/2020.acl-main.173/  (PDF: https://aclanthology.org/2020.acl-main.173.pdf)
Kind:        primary. Maynez, Narayan, Bohnet, McDonald (Google Research), ACL 2020, pp.
             1906-1919; owns the XSum faithfulness/factuality human-annotation study and the
             direct correlation of ROUGE against those judgments. NEW in round 02.
Establishes: The firsthand, owning evidence that ROUGE does not measure faithfulness or
             factuality on abstractive summaries -- the round 01 gap, now closed.
Paraphrase:  They ran "a large-scale human evaluation of hallucinated content" on the extreme
             summarization dataset XSum (226,711 BBC single-sentence-summary articles). They
             sampled 500 test articles and elicited judgments from three annotators for each of
             2,500 (500x5) document-summary pairs, across five systems: PTGEN (RNN pointer-
             generator), TCONV S2S (CNN), TRAN S2S (Transformer, random init), BERTS2S
             (Transformer, BERT-initialized), and GPT-TUNED, plus the human GOLD summaries.
             Definitions (Secs. 2.1-2.2): a summary is "hallucinated if it has a span(s) ... that
             is not supported by the input document." Intrinsic hallucinations "misrepresent
             information from the document"; extrinsic hallucinations are "model generations that
             ignore the source material altogether." Faithfulness = entailment to the source;
             factuality = verifiable truth (via Wikipedia/Google), so a hallucination can be
             unfaithful yet factual. Findings: "intrinsic and extrinsic hallucinations happen
             frequently -- in more than 70% of single-sentence summaries," and "over 90% of
             extrinsic hallucinations were erroneous" (Sec. 1, confirmed by Table 2). Pretrained
             BERTS2S is best on BOTH automatic metrics (Table 1: ROUGE-1 38.42, ROUGE-2 16.96,
             ROUGE-L 31.27, BERTScore 78.85) AND human faithfulness/factuality (Table 2: 26.9%
             faithful, 34.7% faithful-or-factual, both the highest) -- so higher ROUGE here goes
             WITH higher faithfulness at the model level; ROUGE is not shown to reward the
             unfaithful. The metric point (Table 4, Sec. 5.4): Spearman |rs| of each metric with
             human faithful/factual scores -- ROUGE-1 0.197/0.125, ROUGE-2 0.162/0.095, ROUGE-L
             0.162/0.113, BERTScore 0.190/0.116, QA 0.044/0.027, Entailment 0.431/0.264. The
             authors classify ROUGE and BERTScore as "very weak" correlation and textual
             entailment as the best (moderate with faithfulness, weak with factuality). They note
             entailment is reference-less and "can easily be gamed," so it "need[s] to be coupled
             with reference-based measures like ROUGE" (Sec. 5.5).
Locators:    Abstract; Sec. 1 (main conclusions); Secs. 2.1-2.2 (definitions); Sec. 3 (XSum);
             Sec. 5.1 and Table 1 (ROUGE/BERTScore); Sec. 5.2 and Table 2 (hallucination rates);
             Sec. 5.4 and Table 4 (Spearman correlations); Sec. 5.5 (Table 5); Sec. 7 (Conclusion).
Quote:       "measures such as ROUGE or BERTScore will not be sufficient when studying the
             problem; semantic inference-based automatic measures are better representations of
             true summarization quality." (Sec. 7, Conclusion). Also: "ROUGE ... and BERTScore
             (Zhang et al., 2020) correlates less with faithfulness/factuality than metrics
             derived from automatic semantic inference systems" (Sec. 1).
```

```text
URL:         https://aclanthology.org/2020.emnlp-main.750/  (PDF: https://aclanthology.org/2020.emnlp-main.750.pdf)
Kind:        primary for the FactCC approach and its definitional critique of overlap metrics;
             secondary (a retelling) for the "up to 30% inconsistent" magnitude, which it cites
             to four prior works. Kryscinski, McCann, Xiong, Socher (Salesforce), EMNLP 2020,
             pp. 9332-9346. NEW in round 02.
Establishes: The field's plain statement that the standard summarization metrics do not measure
             factual consistency, the scale of the inconsistency problem (as retold), and a
             model-based alternative (FactCC).
Paraphrase:  The opening sentence is the load-bearing critique: "The most common metrics for
             assessing summarization algorithms do not account for whether summaries are
             factually consistent with source documents" (Abstract). The introduction names the
             field's gaps as "insufficient evaluation protocols that omit important dimensions,
             such as factual consistency, noisy datasets ... and strong, domain-specific layout
             biases" (Sec. 1). It defines a factually consistent summary as one that "contains
             only statements that are entailed by the source document" (Sec. 1). It reports the
             magnitude -- "Recent studies show that up to 30% of summaries generated by abstractive
             models contain factual inconsistencies ... Such high levels of factual inconsistency
             render automatically generated summaries virtually useless in practice" (Sec. 1) --
             citing Cao et al. 2018, Goodrich et al. 2019, Falke et al. 2019, and Kryscinski et
             al. 2019; the 30% figure is retold, not owned here. The paper's own contribution is
             FactCC, "a novel, weakly-supervised BERT-based model for verifying factual
             consistency," trained on synthetic data built by rule-based transformations
             (paraphrase, entity/number/pronoun swap, negation) of source sentences. FactCC and
             its explainable variant FactCCX outperform NLI- and fact-checking-trained models on
             CNN/DailyMail. Note the paper does NOT report a ROUGE-vs-human correlation number;
             its critique of ROUGE is definitional (overlap metrics are blind to consistency), not
             a correlation study. For an exact ROUGE-faithfulness correlation, cite Maynez 2020.
Locators:    Abstract; Sec. 1 (Introduction); Sec. 3.1 (data transformations); Sec. 4.2 and
             Tables 3, 5 (model results); Sec. 6 (Conclusions).
Quote:       "The most common metrics for assessing summarization algorithms do not account for
             whether summaries are factually consistent with source documents." (Abstract)
```

```text
URL:         https://aclanthology.org/D15-1013/  (PDF: https://aclanthology.org/D15-1013.pdf)
Kind:        primary. Yvette Graham (ADAPT Centre, Trinity College Dublin), EMNLP 2015, pp.
             128-137; owns the 192-variant ROUGE re-evaluation on DUC-2004. NEW in round 02.
Establishes: The older, historical-record critique: ROUGE's correlation with human assessment
             depends heavily on which variant is used, the recommended variants were suboptimal,
             and BLEU matches the best ROUGE.
Paraphrase:  Graham identifies three "areas of concern" in how summarization metrics had been
             evaluated (Abstract): "(1) movement away from evaluation by correlation with human
             assessment; (2) omission of important components of human assessment ... in addition
             to large numbers of metric variants; (3) absence of methods of significance testing
             improvements over a baseline." She reconstructs a human gold score for DUC-2004 by
             averaging coverage score (CS) with mean linguistic quality (MLQ), the latter usually
             dropped in metric evaluations. She then computes Pearson r of BLEU and all 192
             ROUGE system-level variants (8 n-gram-count choices x stemming x stop-word removal x
             precision/recall/f-score x average/median) against that human score (Table 1). Result:
             "BLEU MT evaluation metric achieves strongest correlation with human assessment
             overall, r = 0.797, with performance of ROUGE variants ranging from r = 0.786, just
             below that of BLEU, to as low as r = 0.293" (Sec. 3.3). The best ROUGE variant is
             "average ROUGE-2 precision with stemming and stop-words removed" (0.786); the
             BLEU-vs-best-ROUGE gap is not statistically significant by a Williams test (Sec.
             4.1). "Current recommended best variants of ROUGE are shown to be significantly
             outperformed by several other ROUGE variants" (Sec. 4.1). "Contrary to prior belief,
             the vast majority of optimal ROUGE variants are precision-based" (Sec. 4.1, Table 2:
             precision 52.5%, f-score 25.0%, recall 22.5% of optimal variants) -- notable because
             ROUGE is named "Recall-Oriented." Replicating Hong et al. 2014 with the best variant
             changes system rankings: "the system now taking first place had originally ranked in
             fourth position" (Sec. 5, Table 3). Scope caution: these are strong correlations
             (0.79) -- this is a variant-fragility and methodology critique, not a "ROUGE is weak"
             result.
Locators:    Abstract; Sec. 2 (Related Work); Sec. 3.1-3.2 (human score, 192 variants); Sec. 3.3
             and Table 1 (Pearson r); Sec. 4.1 and Table 2 (significance, precision dominance);
             Sec. 5 and Table 3 (system re-ranking).
Quote:       "BLEU MT evaluation metric achieves strongest correlation with human assessment
             overall, r = 0.797, with performance of ROUGE variants ranging from r = 0.786 ... to
             as low as r = 0.293." (Sec. 3.3)
```

```text
URL:         https://huggingface.co/facebook/bart-large-cnn
Kind:        primary artifact / self-report. Meta's own model card; it is the exhibit for the
             "ROUGE reported as the headline quality claim, still in circulation" point, not an
             independent judgment that BART summarizes well. It is a self-report, not a third-party
             secondary; the third-party-secondary policy slot is now filled by the Sai et al.
             survey below (see the round-03 note in Contradictions).
Establishes: A current, widely used model card presenting ROUGE as its only quantitative
             evidence of summarization quality.
Paraphrase:  The card describes BART as "particularly effective when fine-tuned for text
             generation (e.g. summarization)" and reports, as self-reported results on
             CNN/DailyMail, ROUGE-1 42.949, ROUGE-2 20.815, ROUGE-L 30.619. No other metric,
             human evaluation, or faithfulness check appears on the card. This is the pattern the
             lesson targets: a summarizer's quality claim resting on ROUGE alone.
Locators:    Model description and the model-index / self-reported metrics block.
Quote:       ROUGE-1 "42.949", ROUGE-2 "20.815", ROUGE-L "30.619" (self-reported, CNN/DailyMail).
```

```text
URL:         https://arxiv.org/abs/2008.12009  (read firsthand: arXiv:2008.12009v2 full-text PDF)
             Canonical: Ananya B. Sai, Akash Kumar Mohankumar, Mitesh M. Khapra, "A Survey of
             Evaluation Metrics Used for NLG Systems," ACM Computing Surveys 55(2), Article 26,
             pp. 1-39, 2022, https://doi.org/10.1145/3485766. The ACM DOI page gates automated
             fetch (HTTP 403) but resolves for a reader; the arXiv abstract page above is the
             readable, source-owned landing page and the route this text was read through.
Kind:        secondary, and why. This is a peer-reviewed survey (ACM Computing Surveys). Its
             authors did not create ROUGE and own no first-party ROUGE measurement here; they
             report on ROUGE from OUTSIDE the authoring parties, synthesizing and organizing
             other researchers' definitions, adoption patterns, and criticisms of the metric.
             That is the test for secondary: authorship and stake sit outside the claim. It is
             the record's genuine third-party secondary source. NEW in round 03.
Establishes: A compact, citable outside characterization of ROUGE's standing and known limits:
             what ROUGE is, where it sits among evaluation metrics, that it is a long-standing
             standard adopted well beyond summarization, and the field's recurring criticisms of
             overlap metrics including ROUGE. Use it for the outside "here is how the field
             places and judges ROUGE" framing, not for any first-party correlation number (for
             those, cite the owning primaries: SummEval, Maynez, Graham, DUC in Context).
Paraphrase:  Definition (Sec. 6, "Context-free / Untrained / n-gram" metrics): "ROUGE
             (Recall-Oriented Understudy for Gisting Evaluation): ROUGE metric includes a set of
             variants: ROUGE-N, ROUGE-L, ROUGE-W, and ROUGE-S. ROUGE-N is similar to BLEU-N in
             counting the n-gram matches between the hypothesis and reference, however, it a
             recall-based measure unlike BLEU which is precision-based." ROUGE-L "measures the
             longest common subsequence (LCS) between a pair of sentences" as an F-measure, and
             the survey flags its meaning-blindness firsthand: ROUGE-L "does not check for
             consecutiveness of the matches as long as the word order is the same. It hence
             cannot differentiate between hypotheses that could have different semantic
             implications, as long as they have the same LCS." Standing/adoption: "ROUGE variants
             were originally proposed for evaluating automatic summarization, but have been
             adopted for evaluation of other NLG tasks"; the survey's taxonomy (Fig. 2) files
             ROUGE under Context-free -> Untrained -> Word-based / N-gram alongside BLEU, NIST,
             METEOR, GTM, CIDEr, and its task table marks ROUGE as the summarization (AS) metric.
             The Introduction records ROUGE's persistence despite criticism: "Despite receiving
             their fair share of criticism, automatic metrics such as BLEU, METEOR, ROUGE, etc.,
             continued to remain widely popular simply because there was no other feasible
             alternative," and it groups ROUGE among "early heuristic-based metrics such as BLEU,
             ROUGE [that] are inadequate for capturing the nuances in the different NLG tasks"
             (Abstract). Criticisms it catalogs (Sec. 7, "Studies Criticising the Use of
             Automatic Evaluation Metrics"): (i) poor correlation with human judgment -- Table 4
             lists works reporting poor correlation for ROUGE-1/2/L specifically on abstractive
             summarization of CNN/DailyMail (row citing Kryscinski et al. 2019) and ROUGE across
             data-to-text, QA, QG, image captioning, and dialogue tasks; the survey adds that
             "there is a high variance in the correlations reported for the same metric across
             different studies" and that metrics are more reliable "at the system-level ... and
             less so at the sentence-level"; (ii) uninterpretability -- a single score that does
             not say whether it reflects fluency, informativeness, or coherence; (iii) inherent
             bias; (iv) poor adaptability of n-gram-overlap metrics to tasks they were not
             designed for; (v) inability to capture nuances -- explicitly, "Kryscinski et al.
             criticize the automatic metrics and human evaluations used for abstractive
             summarization stating that none of them check for factual inconsistencies in the
             summaries." Note on stake: the survey RETELLS these findings from the owning
             studies; where an exact figure matters, cite the primary the survey points to.
Locators:    Abstract; Sec. 1 (Introduction, ROUGE's persistent popularity); Sec. 6 and Fig. 2
             (taxonomy) and the ROUGE definition subsection; the per-task metric table (Sec. 6);
             Sec. 7 (criticisms) and Table 4 (poor-correlation catalog); Sec. 8 (correlation
             methodology). Reference [82] = Lin 2004, ROUGE.
Quote:       "ROUGE variants were originally proposed for evaluating automatic summarization,
             but have been adopted for evaluation of other NLG tasks." (Sec. 6). Also, on
             meaning-blindness: ROUGE-L "cannot differentiate between hypotheses that could have
             different semantic implications, as long as they have the same LCS." (Sec. 6)
```

## Contradictions

The evidence complicates the commissioned "misled case" in concrete ways. The
editor should weigh these before the writer commits to the framing. Items 1-4 are
carried unchanged from round 01; items 5-7 are from round 02; the policy note at the
end is updated in round 03.

1. "Meta-evaluations found ROUGE correlates weakly with quality and consistency."
   SummEval's own Table 2 (Kendall tau, expert, system-level) does not support the
   consistency half. ROUGE-1 correlates 0.53 with consistency, ROUGE-2 0.59,
   ROUGE-3 0.71 -- moderate to strong, not weak. Where ROUGE is genuinely weak is
   coherence (ROUGE-1 0.25, ROUGE-2 0.16, ROUGE-L 0.07) and relevance (0.41, 0.29,
   0.24). And SummEval explicitly reads the consistency correlation as probably an
   artifact of low model abstractiveness, not as ROUGE measuring faithfulness. The
   accurate claim: ROUGE is weak on coherence and relevance; its consistency
   correlation is confounded and cannot be read as measuring faithfulness. ROUGE-L
   is the weakest ROUGE variant across all four dimensions.

2. Bhandari is miscast by the commission. It does not find ROUGE weak on modern
   data; it finds ROUGE-2 the *best* metric on CNN/DailyMail, beating the semantic
   metrics. Its real negative results are (a) all metrics de-correlate when you
   restrict to the top few systems, and (b) rankings established on TAC do not
   transfer to CNN/DailyMail. Using Bhandari as a "ROUGE correlates weakly" citation
   is a misreading. It is better cited for "metric reliability is dataset-dependent
   and collapses among near-tied top systems."

3. "Extractive/lead-biased summaries score well while faithful abstractive ones
   score poorly." Split evidence. The NIST primary supports that lead-sentence
   baselines are hard to beat on news because of article structure. But SummEval's
   modern numbers contradict the second clause: the highest ROUGE scores go to
   abstractive pretrained models (T5, BART, Pegasus), above LEAD-3. Maynez adds an
   independent contradiction of the second clause: on XSum its highest-ROUGE model
   (BERTS2S) is also its most faithful. The lead-bias advantage is a property of
   news structure and noisy single references, not a universal law that ROUGE
   punishes abstraction. State it as the former.

4. ROUGE is defended, from inside its home setting. The NIST primary credits
   "reasonable correlation with manual coverage judgments that makes it useful ...
   via hill-climbing," and DUC 2006 ROUGE-2 correlates 0.836 (Pearson) with human
   content responsiveness (Table 2). Lin's Table 1 shows ROUGE-2 up to 0.99 on
   100-word single-document news. Graham 2015 adds that even under a corrected
   methodology the best ROUGE variant reaches r = 0.786 on DUC-2004. The honest
   center holds: ROUGE works well for single-document news, at the system level,
   with strong references and weak systems -- the setting it was built for -- and
   degrades outside it.

5. The two "faithfulness" correlations look opposed but are not. SummEval found
   ROUGE's correlation with human *consistency* moderate to strong (0.53-0.71
   Kendall tau); Maynez found ROUGE's correlation with human *faithfulness* very
   weak (0.10-0.20 Spearman). The reconciliation is in SummEval's own caveat and
   Maynez's data. SummEval's models on CNN/DailyMail are mostly low-abstractiveness,
   so overlap tracks faithfulness by accident; Maynez's XSum summaries are highly
   abstractive by construction, and there overlap tracks faithfulness essentially
   not at all. The defensible synthesis: ROUGE's apparent grip on faithfulness is an
   artifact of extractive data and vanishes on genuinely abstractive summaries.

6. Maynez does not show that high ROUGE means unfaithful. Its best-ROUGE model,
   BERTS2S, is also its most faithful and most factual. The finding is that ROUGE
   does not *track* faithfulness at the summary level (very weak Spearman), not that
   ROUGE and faithfulness pull in opposite directions. The writer must not upgrade
   "does not measure" into "rewards the unfaithful." Maynez also finds that
   pretraining raises ROUGE and faithfulness together, so the gains it measures are
   real, and it recommends coupling entailment WITH ROUGE rather than replacing it.

7. Graham is variant-fragility, not weakness. Its headline is that r swings from
   0.786 to 0.293 across 192 variants and that the field's recommended variants were
   suboptimal, so published ROUGE comparisons before 2015 may have optimized the
   wrong variant. But 0.786 is a strong correlation, and BLEU matches it, which
   undercuts the idea that ROUGE is specially suited to summarization. Do not cite
   Graham as "ROUGE correlates weakly with humans." Cite it for "the ROUGE number
   you report depends on which of 192 variants you picked, and the standard choices
   were not the best ones."

The Sai et al. survey (new in round 03) introduces no new contradiction. It
corroborates the record's honest center from the outside: it presents ROUGE as a
long-standing standard that persisted "simply because there was no other feasible
alternative," files it among heuristic overlap metrics that are "inadequate for
capturing the nuances in the different NLG tasks," and catalogs exactly the limits
the primaries own (poor and high-variance human correlation, system-level more
reliable than sentence-level, meaning-blindness of LCS matching, and the absence of
a factual-consistency check). One caution for the writer: the survey's Table 4 files
ROUGE-1/2/L under "poor correlation with human judgements" for abstractive
summarization, citing Kryscinski et al. 2019 -- but that is the survey's summary
label, and the underlying primaries (SummEval, Bhandari) show the fuller,
dimension-split picture in items 1-2 above. Cite the survey for the field's
characterization, not as a standalone "ROUGE correlates poorly" number.

Round-02 policy note, now RESOLVED (kept as the record of a closed gap): round 02
recorded that none of its eight read sources was a third-party secondary -- seven
academic primaries and one self-report model card -- and flagged that a genuine
outside-party secondary still needed to be added if the policy required one. Round 03
adds that source: Sai, Mohankumar & Khapra 2022, a peer-reviewed ACM Computing
Surveys survey reporting on ROUGE from outside the authoring parties. The "at least 1
secondary" floor is now met by a strict third-party secondary, and the BART model
card returns to being purely the "ROUGE as headline claim" exhibit, no longer needed
to fill the non-primary slot.

## Numbers

Round 01 figures are preserved. Round-02 figures (Maynez, Kryscinski, Graham) follow
them. Round 03 adds no new dependent figure -- the survey is cited for characterization,
not for any first-party number; its poor-correlation entries point back to primaries
already recorded here.

```text
Figure: ROUGE-1 = 5/6 ~= 0.833 (worked example computed and hand-checked here)
Owner:  Lin 2004, Eq. 1 (applied to a fresh pair)
Scope:  Reference R = "the cat sat on the mat" (6 unigrams: the x2, cat, sat, on, mat).
        Candidate C = "the cat sat on a mat". Overlapping unigrams, clipped to reference counts:
        the(1)+cat(1)+sat(1)+on(1)+mat(1) = 5; "a" is not in R. Recall = 5 / 6.
```

```text
Figure: ROUGE-2 = 3/5 = 0.6 (same pair)
Owner:  Lin 2004, Eq. 1 with n=2
Scope:  Reference bigrams (5): "the cat","cat sat","sat on","on the","the mat".
        Candidate bigrams (5): "the cat","cat sat","sat on","on a","a mat".
        Matches: "the cat","cat sat","sat on" = 3. Recall = 3 / 5. One substituted word
        ("a" for "the") drops ROUGE-2 from 1.0 to 0.6, showing how bigram recall punishes a
        near-identical, meaning-preserving candidate.
```

```text
Figure: ROUGE-L = 5/6 ~= 0.833 (same pair, DUC setting)
Owner:  Lin 2004, Eqs. 2-4
Scope:  LCS(R,C) = "the cat sat on mat" = length 5; R_lcs = 5/6, P_lcs = 5/6. With beta -> inf
        (DUC), ROUGE-L = R_lcs = 5/6. (With beta=1 the F-measure is also 0.833.)
```

```text
Figure: ROUGE-2 recall = 1/3 for BOTH "police kill the gunman" and "the gunman kill police"
Owner:  Lin 2004, Sec. 3.1 (the paper's own example)
Scope:  Reference "police killed the gunman". The reversed, near-nonsensical candidate ties the
        correct one on ROUGE-2. ROUGE-L separates them: 0.75 vs 0.50 (beta=1). The cleanest
        firsthand proof that n-gram overlap does not read meaning.
```

```text
Figure: SummEval Kendall tau (system-level, expert, 11 refs) -- ROUGE vs four human dimensions
Owner:  Fabbri et al. 2021, Table 2
Scope:  ROUGE-1: coherence 0.2500, consistency 0.5294, fluency 0.5240, relevance 0.4118.
        ROUGE-2: 0.1618 / 0.5882 / 0.4797 / 0.2941. ROUGE-3: 0.2206 / 0.7059 / 0.5092 / 0.3529.
        ROUGE-L: 0.0735 / 0.1471 / 0.2583 / 0.2353. 100 CNN/DailyMail articles, 16 models,
        3 expert annotators. Weakest on coherence and relevance; ROUGE-L weak throughout.
```

```text
Figure: SummEval human ratings (1-5, expert avg) -- gold reference below the extractive baseline
Owner:  Fabbri et al. 2021, Table 3
Scope:  CNN/DM reference summary: coherence 3.26, consistency 4.47, relevance 3.77. LEAD-3
        baseline: 4.16 / 4.98 / 4.14. BART: 4.18 / 4.94 / 4.25. The reference the metric scores
        against itself rates worse than a lead baseline on human consistency and coherence.
```

```text
Figure: DUC 2006 ROUGE-2 vs human content responsiveness -- Spearman 0.767, Pearson 0.836
Owner:  Over, Dang, Harman ("DUC in Context"), Table 2
Scope:  Averaged over all automatic peers; ROUGE-SU4 Spearman 0.790 / Pearson 0.850; BE-HM
        Spearman 0.797. ROUGE's positive result in its home setting (single-genre news, system
        level). Pearson 95% interval [0.725, 1.000].
```

```text
Figure: Lin 2004 ROUGE-2 Pearson correlation with human judgment, up to 0.99
Owner:  Lin 2004, Table 1 (DUC 2002, 100-word single-document, multi-reference)
Scope:  Critical value for significance is 0.632 (95%, 8 d.o.f.). Multi-document tasks "rarely
        reached high 90%." The original evidence that established ROUGE as the field standard,
        and its scope limits.
```

```text
Figure: BART self-reported ROUGE on CNN/DailyMail -- 42.949 / 20.815 / 30.619
Owner:  facebook/bart-large-cnn model card (ROUGE-1 / ROUGE-2 / ROUGE-L)
Scope:  The only quantitative quality evidence on the card. Live example of ROUGE as the
        headline "summarizes well" claim.
```

```text
Figure: <= 55% of a model summary's vocabulary appears in its source documents
Owner:  Copeck & Szpakowicz 2004, via "DUC in Context" Sec. 6 (unread original; NIST retelling)
Scope:  DUC model summaries. Shows human references use generalizing language, so a pure
        lexical-overlap metric structurally penalizes faithful rewording. Cite the NIST summary,
        not the primary, unless the writer opens Copeck & Szpakowicz.
```

```text
Figure: Maynez -- Spearman |rs| of metrics with human faithfulness / factuality (XSum, 500 docs)
Owner:  Maynez et al. 2020, Table 4
Scope:  ROUGE-1 0.197 / 0.125. ROUGE-2 0.162 / 0.095. ROUGE-L 0.162 / 0.113. BERTScore 0.190 /
        0.116. QA 0.044 / 0.027. Textual Entailment 0.431 / 0.264. Authors band these: 0.0-0.19
        "very weak," 0.20-0.39 "weak," 0.40-0.59 "moderate." ROUGE and BERTScore are very weak;
        entailment is the only metric reaching moderate (with faithfulness). THE central
        firsthand number for "ROUGE does not measure faithfulness" on abstractive summaries.
```

```text
Figure: Maynez -- hallucination is pervasive; extrinsic hallucinations are mostly wrong
Owner:  Maynez et al. 2020, Sec. 1 and Table 2
Scope:  Hallucinated (I union E, % of summaries, all three annotators): PTGEN 75.3, TCONV S2S
        78.5, TRAN S2S 79.3, BERTS2S 73.1, GOLD 76.9. "more than 70% of single-sentence
        summaries" hallucinate. "over 90% of extrinsic hallucinations were erroneous." Faithful
        %: PTGEN 24.7, TCONV 21.5, TRAN 20.7, BERTS2S 26.9, GOLD 23.1. Faithful-or-factual:
        BERTS2S 34.7 (highest, +7.4 over next best). Scope: XSum, highly abstractive by design.
```

```text
Figure: Maynez -- pretrained BERTS2S leads on ROUGE AND on faithfulness
Owner:  Maynez et al. 2020, Table 1 (ROUGE) and Table 2 (human)
Scope:  BERTS2S: ROUGE-1 38.42, ROUGE-2 16.96, ROUGE-L 31.27, BERTScore 78.85 -- all best of
        five systems; and 26.9% faithful / 34.7% faithful-or-factual -- also best. Guards the
        writer against "high ROUGE = unfaithful": here they move together at the model level.
```

```text
Figure: Up to 30% of abstractive-model summaries are factually inconsistent
Owner:  Cao et al. 2018, Goodrich et al. 2019, Falke et al. 2019, Kryscinski et al. 2019
        (retold in Kryscinski et al. 2020, Sec. 1; also retold in SummEval Related Work)
Scope:  Abstractive summarization models, various news datasets. The magnitude the faithfulness
        literature rests on. Kryscinski 2020 is a retelling, not the owner; cite the number to
        the originating works, or attribute it explicitly as reported by Kryscinski.
```

```text
Figure: Graham -- Pearson r of metrics with human assessment on DUC-2004
Owner:  Graham 2015, Table 1 and Sec. 3.3
Scope:  BLEU 0.797 (highest overall). Best ROUGE variant 0.786 (average ROUGE-2 precision,
        stemmed, stop-words removed). Worst ROUGE variant 0.293 (median ROUGE-4 recall, stop-
        words removed). BLEU-vs-best-ROUGE gap not significant (Williams test). Human score =
        average of coverage and mean linguistic quality; DUC-2004 generic multi-document news.
        The spread 0.293-0.786 across 192 variants is the load-bearing figure: variant choice,
        not the metric name, sets the correlation.
```

```text
Figure: Graham -- optimal ROUGE variants are mostly precision-based, not recall
Owner:  Graham 2015, Sec. 4.1 and Table 2
Scope:  Among variants not significantly outperformed by any other: precision 52.5%, f-score
        25.0%, recall 22.5%; average aggregation 63.7% vs median 36.3%; ROUGE-3 28.7% and
        ROUGE-2 25.0% of optimal variants. Notable because ROUGE is "Recall-Oriented" by name,
        yet recall variants are the minority of optimal ones on DUC-2004.
```

## Source assets

Round 01 assets are preserved; round-02 assets (Maynez, Graham) follow; a round-03
note on the survey closes the section.

```text
Asset: Lin 2004, Table 1 (Pearson correlations of 17 ROUGE measures vs human judgment,
       DUC 2001/2002 100-word single-document), page 6 of the PDF.
Shows: ROUGE-2/L/W in the 0.8-0.99 range on single-document news -- the evidence that made
       ROUGE the standard. Pairs with the scope caveat that multi-doc never reached those values.
Crop:  Keep the R-1, R-2, R-L rows and the DUC 2002 columns; the full 17-row grid is more than a
       lesson needs. Retain the column headers so the reader sees these are single-document scores.
```

```text
Asset: Fabbri et al. 2021, Table 2 (Kendall tau of metrics vs coherence/consistency/fluency/
       relevance), page 5 of the PDF.
Shows: In one grid, ROUGE weak on coherence and relevance, stronger on consistency and fluency,
       and ROUGE-L weakest of the ROUGE family. This is the honest correlation picture.
Crop:  A crop must retain the four dimension column headers and the ROUGE-1/2/3/L rows. Omitting
       the consistency column would misrepresent the finding; keep all four.
```

```text
Asset: Fabbri et al. 2021, Table 3 (human ratings by model), page 8 of the PDF.
Shows: The gold CNN/DailyMail reference scoring below LEAD-3 and BART on consistency and
       coherence -- the noisy-reference problem in one row comparison.
Crop:  Keep the "CNN/DM Reference Summary" row beside LEAD-3 and BART; the four dimension columns
       must stay so the reference-vs-baseline gap is legible.
```

```text
Asset: "DUC in Context," Figure 1 (DUC 2001 single-document coverage: Baselines vs Systems vs
       Humans box plots), and Table 2 (ROUGE-2 vs responsiveness).
Shows: Figure 1 -- system summaries barely separating from lead baselines while humans sit
       clearly higher; the lead-baseline-is-hard-to-beat point, visually. Table 2 -- ROUGE's
       positive correlation in its home setting.
Crop:  For Figure 1, retain all three box groups (Baselines/Systems/Humans) and the 0-4 coverage
       axis; the argument is the gap between them.
```

```text
Asset: Maynez et al. 2020, Table 4 (Spearman |rs| of ROUGE-1/2/L, BERTScore, QA, Entailment vs
       faithful and factual human scores), page 8 of the PDF.
Shows: In six rows, ROUGE and BERTScore near the bottom (0.10-0.20) and Entailment on top
       (0.431 faithful) -- the single clearest picture that overlap metrics do not measure
       faithfulness while a semantic measure does better. This is the round-02 centerpiece asset.
Crop:  Keep all six metric rows and both columns (faithful, factual). Do not crop to ROUGE alone;
       the argument is the gap between ROUGE/BERTScore and Entailment.
```

```text
Asset: Maynez et al. 2020, Figure 1 (one XSum article with its GOLD summary and five model
       summaries, hallucinated words in red, faithful in blue, each tagged with [R-1, R-2, R-L]),
       page 2 of the PDF.
Shows: Fluent, topical, ROUGE-scoring summaries that invent people and facts ("UKIP leader Nigel
       Goldsmith," "Zac Goldwin ... Labour's candidate"). The lesson's "fluent but unfaithful"
       case in a single concrete exhibit, with ROUGE scores attached to prove overlap missed it.
Crop:  Keep at least the GOLD line, one high-ROUGE hallucinating model line, and the red/blue
       coloring; the bracketed ROUGE triples must stay legible for the point to land.
```

```text
Asset: Graham 2015, Table 1 (Pearson r of BLEU and 192 ROUGE variants with human assessment,
       DUC-2004), spanning pages 6-7 of the PDF.
Shows: The full 0.293-0.797 spread. BLEU at the top, ROUGE variants fanning down, the "Hong et
       al. 2014" recommended variants (bold) sitting well below the best. The variant-fragility
       argument at a glance. This is a dense table; a chart of the min/median/max ROUGE r beside
       BLEU (writer-built, per spec/charts.md) may serve the lesson better than the raw grid.
Crop:  If the raw table is used, it is long; consider excerpting the top rows (BLEU, best ROUGE)
       and the bottom rows (worst ROUGE) with the bold Hong variants, keeping the column headers
       (stemming, stop-words, aggregation, P/R/F) so the reader sees what the variant knobs are.
```

```text
Asset: A tiny hand-built ROUGE calculation table (the worked example above).
Shows: The mechanic -- list reference units, mark overlaps, divide by the reference count -- for
       ROUGE-1, ROUGE-2, ROUGE-L on one candidate/reference pair. This is furniture the writer
       builds, not lifted from a source.
Crop:  n/a. If rendered as a table, keep the reference-count denominator explicit in each row.
```

```text
Asset: Sai, Mohankumar & Khapra 2022, Figure 2 (Taxonomy of Automatic Evaluation Metrics) and
       Table 4 (works showing poor correlation of various metrics with human judgements). NEW in
       round 03.
Shows: Figure 2 places ROUGE in the "Context-free -> Untrained -> Word-based / N-gram" branch
       beside BLEU, NIST, METEOR, GTM, CIDEr -- the outside "here is the family ROUGE belongs to"
       picture. Table 4 lists, in one column, the many tasks/datasets where overlap metrics
       including ROUGE were reported to correlate poorly with humans. Useful only as an outside
       framing exhibit; the load-bearing correlation numbers come from the owning primaries.
Crop:  For Table 4, if used, keep the ROUGE-bearing rows and the task/dataset column so the
       breadth of tasks is legible; do not present it as ROUGE-specific correlation values.
```

## Discarded

```text
URL: https://dl.acm.org/doi/10.1145/3485766  -- ACM Computing Surveys DOI page for the Sai et al.
     survey returns HTTP 403 to automated fetch (gated, not dead). The identical peer-reviewed
     content was read firsthand via the arXiv:2008.12009v2 full-text PDF. Cite the arXiv abstract
     page (https://arxiv.org/abs/2008.12009) as the readable landing page and the ACM DOI as the
     canonical publication. Not a rejection of the source, only the route. NEW in round 03.
```

```text
URL: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00373  -- TACL page returns HTTP 403
     to automated fetch (gated, not dead); read the identical content via arXiv:2007.12626v4 and
     cite the arXiv abstract page and the TACL DOI. Not a rejection of the source, only the route.
```

```text
URL: The unverified "recall variant of ROUGE (0.85)" figure surfaced in a search snippet for
     Bhandari -- rejected. That decimal does not appear in the Bhandari paper text; its
     correlations are published only as bar charts. Do not use it.
```

```text
URL: Maynez et al. 2020 and Kryscinski et al. 2020 -- NO LONGER discarded. Round 01 recorded
     these as unread leads known only through SummEval's Related Work. Round 02 read both
     firsthand (see Sources above), closing that gap. This line records the status change.
```

```text
URL: Rankel et al. 2013 and Peyrard 2019 -- still unread. The round-02 brief asked for "at least
     one of Rankel 2013 or Graham 2015"; Graham 2015 was read firsthand, satisfying that
     requirement. Rankel 2013 (the "ROUGE fails to distinguish top systems" study) and Peyrard
     2019 remain leads reached only through SummEval's and Bhandari's citations. They would
     strengthen the "ROUGE collapses among near-tied top systems" point but must be opened before
     being cited.
```

```text
URL: BLEU / Papineni et al. -- deliberately not pursued as a source to teach. The neighbor policy
     assigns BLEU to a separate lesson; link it for contrast at most. Note that Graham 2015
     reports BLEU on par with the best ROUGE on DUC-2004 (r 0.797 vs 0.786), a contrast the
     writer may cite from Graham without teaching BLEU.
```

```text
URL: Kryscinski et al. 2019, "Neural Text Summarization: A Critical Evaluation" -- not opened
     directly; the 2020 factual-consistency paper was read instead in round 02. It is the origin
     of several ROUGE/dataset-bias critiques retold by the 2020 paper, by SummEval, and by the
     Sai et al. 2022 survey (whose Table 4 cites it for poor ROUGE correlation on abstractive
     summarization). It remains an unread lead if a sharper ROUGE-specific critique quote is
     wanted; cite it through the survey's or Kryscinski 2020's retelling only, not firsthand.
```

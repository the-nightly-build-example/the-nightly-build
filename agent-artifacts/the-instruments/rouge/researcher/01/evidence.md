# Evidence: the-instruments/rouge (01)

The record firmly supports how a ROUGE number is built. ROUGE-N is n-gram recall
against human reference summaries; ROUGE-L is a longest-common-subsequence
F-measure that, under the DUC setting, collapses to LCS recall. Both are read
firsthand from Lin 2004, with the paper's own worked sentences and a second,
independent worked example computed here and checked by hand. The evaluation
context (DUC, then TAC; what "reference"/"model" summaries are; the SEE coverage
tool) is anchored to a NIST-authored primary. The "still in circulation" point
is carried by a live model card that reports ROUGE as its only quantitative
quality evidence.

The record is thin, and in places it contradicts the commission, on the "misled
case." The clean story the commission asks for -- "meta-evaluations found ROUGE
correlates weakly with human judgments of quality and consistency" -- is not what
the two named primaries actually found, and the numbers pull in different
directions. SummEval's own table shows ROUGE correlating *weakly* with coherence
and relevance but *moderately to strongly* with consistency, and SummEval itself
warns that consistency correlation is probably an artifact of how extractive the
models are. Bhandari does not show ROUGE failing on modern data at all: it shows
ROUGE-2 as the single best metric on CNN/DailyMail, and reports its correlations
only as unlabeled bar charts, so no exact ROUGE decimal can be pinned to it. The
"extractive/lead-biased scores well while faithful abstractive scores poorly"
claim holds for news-structure baselines (NIST primary) but is contradicted by
SummEval's modern numbers, where abstractive pretrained models earn the *highest*
ROUGE. The defensible version of the misled case is narrower and is spelled out
below. Source count is also short of policy: four primaries plus one artifact
were read firsthand; the commission asks for at least eight sources.

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
URL:         https://huggingface.co/facebook/bart-large-cnn
Kind:        primary artifact / self-report. Meta's own model card; it is the exhibit for the
             "ROUGE reported as the headline quality claim, still in circulation" point, not an
             independent judgment that BART summarizes well.
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

## Contradictions

The evidence complicates the commissioned "misled case" in four concrete ways.
The editor should weigh these before the writer commits to the framing.

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
   abstractive pretrained models (T5, BART, Pegasus), above LEAD-3. The lead-bias
   advantage is a property of news structure and noisy single references, not a
   universal law that ROUGE punishes abstraction. State it as the former.

4. ROUGE is defended, from inside its home setting. The NIST primary credits
   "reasonable correlation with manual coverage judgments that makes it useful ...
   via hill-climbing," and DUC 2006 ROUGE-2 correlates 0.836 (Pearson) with human
   content responsiveness (Table 2). Lin's Table 1 shows ROUGE-2 up to 0.99 on
   100-word single-document news. The honest center holds: ROUGE works well for
   single-document news, at the system level, with strong references and weak
   systems -- the setting it was built for -- and degrades outside it. Two
   retellings of the "ROUGE is broken" claim (Rankel 2013, Peyrard 2019) reach me
   only through SummEval's and Bhandari's citations; they count as one lead, unread,
   and should be opened before being cited.

## Numbers

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
        ("a" for "the") halves nothing but drops ROUGE-2 from 1.0 to 0.6, showing how
        bigram recall punishes a near-identical, meaning-preserving candidate.
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

## Source assets

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
Asset: A tiny hand-built ROUGE calculation table (the worked example above).
Shows: The mechanic -- list reference units, mark overlaps, divide by the reference count -- for
       ROUGE-1, ROUGE-2, ROUGE-L on one candidate/reference pair. This is furniture the writer
       builds, not lifted from a source.
Crop:  n/a. If rendered as a table, keep the reference-count denominator explicit in each row.
```

## Discarded

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
URL: Maynez et al. 2020 (faithfulness) and Kryscinski et al. 2020 (factual consistency, ~30%
     hallucination) -- not opened directly; known only through SummEval's Related Work. Strong
     leads for the faithfulness point and good candidates to raise the source count, but they must
     be read before being cited as primaries. Recorded as leads, not as read sources.
```

```text
URL: BLEU / Papineni et al. -- deliberately not pursued. The neighbor policy assigns BLEU to a
     separate lesson; link it for contrast at most, do not teach it here.
```

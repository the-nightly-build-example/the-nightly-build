# Evidence record: the-instruments/comet-score (researcher 01)

The evidence supports the commission's three-part angle firmly. COMET's construction
is documented in the founding paper (Rei et al., 2020): a pretrained cross-lingual
encoder (XLM-RoBERTa) fine-tuned to predict human quality judgments from the source,
the candidate, and usually a reference, with reference-free (QE) variants that drop the
reference. The two human signals are Direct Assessment (a 0-100 continuous adequacy
rating, Graham et al., 2013) and MQM (a weighted count of typed, severity-graded
translation errors, Freitag et al., 2021). Non-transferability of a bare COMET number
across versions, language pairs, and test sets is established directly: the tool
owner's own documentation says pre-2022 scores "do not have a direct interpretation"
while post-2022 models rescale to 0-1, and warns the two are not comparable; Zouhar et
al. (2024) show the same checkpoint moves ~0.04 with a software-version change alone,
and that WMT human DA averages per direction span 0.51 to 0.91, so scores from
different directions cannot be compared.

The record is thinner, and more nuanced, on the "COMET misled" requirement than a naive
reading of the commission expects, and the writer must handle this carefully. The single
best-documented study tying metric choice to deployment decisions (Kocmi et al., 2021,
"To Ship or Not to Ship") concludes the opposite of "COMET misled": it finds COMET the
*most reliable* metric and identifies BLEU as the metric that produced bad deployment
decisions. The genuine, primary-sourced case where COMET *itself* misled is
over-optimization: Amrhein and Sennrich (2022) show that selecting translations by COMET
(via MBR decoding) systematically picks outputs with wrong numbers and mangled names,
because COMET is far less sensitive to those errors than to ordinary word changes. Zouhar
et al. (2024) add that COMET assigns positive scores to empty and wrong-language outputs
and can be gamed by a domain tag. The concrete cost is meaning-flipping: a date changed
from 1970 to 1980, a name garbled, chosen precisely because the metric could not see the
error. This is the case the writer should build the "misled" section on, not a claim that
COMET ranks systems worse than BLEU (it does not).

Every figure below was read in the primary that owns it. Version is named on every
version-specific claim.

## Sources

```text
URL:         https://aclanthology.org/2020.emnlp-main.213/
Kind:        primary. The founding COMET paper; the authors (Unbabel AI) own the model's
             design and the WMT19 correlation results. Note the authoring party is a
             commercial MT company that ships COMET, relevant to how the metric is promoted.
Establishes: What COMET is and how it is built. "a neural framework for training
             multilingual machine translation evaluation models." Encoder is
             XLM-RoBERTa (base). Two architectures: an Estimator (regresses on a quality
             score, MSE loss) and a Translation Ranking model (triplet margin loss).
             Inputs are source, MT hypothesis, and reference, each encoded then pooled;
             QE/reference-less work is cited as the basis for using the source. Three
             models trained in the paper: COMET-HTER and COMET-MQM (Estimators) and
             COMET-RANK (ranker). Training signals: Direct Assessment relative rankings
             (DARR) from WMT 2017-2019, HTER from QT21, and a proprietary MQM corpus.
             Evaluated on WMT 2019 Metrics task with a Kendall's Tau-like formulation.
Paraphrase:  COMET is a supervised neural model, not a formula: a pretrained multilingual
             encoder fine-tuned to predict human judgments of translation quality. The
             MQM Estimator was trained on only 12K annotated segments yet was competitive.
             The paper's MQM corpus is proprietary and always has English as the source,
             never the target.
Locators:    Abstract; Sec 2 (Model Architectures), 2.1 (encoder), 2.3-2.4; Sec 3
             (Corpora): 3.2 DARR, 3.3 MQM; Sec 4.2 (evaluation, WMT19); Tables 1-2.
Quote:       "we rely on XLM-RoBERTa (base) as our encoder model" (Sec 2.1).
             "MQM = 100 - (I_Minor + 5 x I_Major + 10 x I_Crit.) / Sentence Length x 100"
             (Eq. 7, the paper's own internal MQM definition).
```

```text
URL:         https://aclanthology.org/W13-2305/
Kind:        primary. Graham, Baldwin, Moffat, Zobel own the Direct Assessment
             continuous-scale methodology that COMET's DA training data descends from.
Establishes: What Direct Assessment is. A continuous 0-100 rating scale (visual analog
             scale) for human evaluation of MT, collected on Amazon Mechanical Turk with
             quality-control mechanisms, standardized per annotator (z-scores). Contrasts
             with older 5- and 7-point interval (Likert) scales. Judges fluency and
             adequacy; monolingual adequacy judgment against a reference (or source)
             removes some reference bias.
Paraphrase:  DA replaces discrete-category human rating with a continuous scale that is
             easier for crowd assessors and supports statistics that discrete scales do
             not. This is the crowd-sourced signal COMET's DA models learn to imitate.
Locators:    Abstract; Sec 1-2 (continuous vs interval scales); Sec 3 (AMT setup,
             quality control); Figures 1-2 (Likert vs continuous interfaces).
Quote:       "We explore the use of continuous rating scales for human evaluation" (Abstract).
```

```text
URL:         https://aclanthology.org/2021.tacl-1.87/
Kind:        primary. Freitag, Foster, Grangier, Ratnakar, Tan, Macherey (Google Research)
             own this MQM methodology and the crowd-vs-expert comparison.
Establishes: What MQM is and why the human signal matters. MQM (Multidimensional Quality
             Metrics) scores a translation by having professional annotators mark typed
             errors, each with a severity (Major, Minor, Neutral). The paper's standard
             scoring scheme: Minor weight 1, Major weight 5 (the MQM standard allows up to
             10), Non-translation weight 25 (= five Major errors), Minor
             Fluency/Punctuation weight 0.1. Key finding: MQM ratings by professional
             translators produce a "sharply different" system ranking from WMT crowd-worker
             DA, with a clear preference for human over machine output; crowd-worker
             evaluation correlates poorly with expert MQM; and metrics based on pretrained
             embeddings can outperform crowd workers.
Paraphrase:  The human judgments COMET learns from are imperfect. Crowd DA (COMET's main
             training signal through 2020) diverges from expert error annotation, so a
             model trained to imitate crowd DA inherits the crowd's blind spots. This is
             the empirical basis for "COMET is only as good as the ratings it learned from."
Locators:    Abstract; Sec 1 (contributions, "most striking finding"); Sec 3.3 (MQM
             customization, severities); Table 1 (error weighting: Major 5, Minor 1,
             Non-translation 25, Minor Fluency/Punctuation 0.1); Figures 1-2 (correlations).
Quote:       "the most striking finding is that MQM ratings sharply [differ from the WMT
             crowd rankings]" (Sec 1). "We fixed the weight on Minor errors at 1 ... a
             Major weight of 5 gave [the best results]" (Sec 3.3).
```

```text
URL:         https://aclanthology.org/2021.wmt-1.57/
Kind:        primary. Kocmi, Federmann, Grundkiewicz, Junczys-Dowmunt, Matsushita, Menezes
             (Microsoft) own the largest metric-vs-human comparison and the deployment
             framing. arXiv mirror: https://arxiv.org/abs/2107.10821 (v2, 13 Sep 2021).
Establishes: Metric choice drives real deployment decisions, and COMET is the most
             reliable metric for pairwise system ranking. Data: 2.3M human judgments over
             4380 systems, 101 languages, 232 directions, source-based DA collected in the
             Appraise framework. Accuracy = share of system pairs where the metric's sign
             agrees with the human delta. COMET tops every subset. The BLEU-misled result:
             203 system pairs judged significantly different by humans (p<0.05) where BLEU
             flips the ranking, with a median difference of 1.3 BLEU points. Recommends
             COMET as the primary metric, ChrF secondary, "Do not use BLEU."
             COMET version used: reference-based "wmt-large-da-estimator-1719" and QE
             "wmt-large-qe-estimator-1719", Unbabel/COMET package v0.0.6 (Appendix A).
Paraphrase:  This is the primary that ties metric choice to shipping models. Its verdict
             cuts against a naive "COMET misled" framing: the metric that misled here was
             BLEU, and COMET was the corrective. Useful for the BLEU-to-COMET transition
             and for "why COMET displaced BLEU," not for a case where COMET itself failed.
Locators:    Abstract; Sec 2.2 (2.3M / 4380); Sec 5.1 + Table 2 (accuracies); Sec 5.3
             (203 flipped pairs, median 1.3 BLEU); Sec 5.4 + Table 5 (BLEU sabotages
             progress); Appendix A (COMET model version).
Quote:       "we have 203 system pairs deemed statistically significant by humans (p-value
             smaller than 0.05) for which using BLEU results in a flipped ranking ... The
             median BLEU difference for these system pairs is 1.3 BLEU points" (Sec 5.3).
             "we recommend COMET ... Do not use BLEU, it is inferior to other metrics"
             (Sec 1, best practices).
```

```text
URL:         https://aclanthology.org/2022.wmt-1.2/
Kind:        primary. Freitag, Rei, et al. (the WMT metrics organizers) own the WMT22
             shared-task ranking of metrics against MQM human ratings.
Establishes: Neural metrics, COMET among them, rank at the top against expert human
             judgment across four domains (news, social, ecommerce, chat), and BLEU ranks
             at the bottom. Official primary-submission ranking (average rank, Table 1):
             COMET-22 1.32 (best), BLEURT-20 1.91, COMET-20 2.36, then metrics including
             CometKiwi and COMET-QE, down to BLEU 5.31. "Out of 13 reference-based metrics
             BLEU is ranked last." Human gold standard is MQM.
Paraphrase:  Confirms COMET's standing at the top of the field as of 2022 and that the
             ranking is now judged against MQM, not crowd DA. Grounds the claim that COMET
             "replaced BLEU at the top." Names specific versions (COMET-22 vs COMET-20),
             which the writer must keep distinct.
Locators:    Title; Abstract; Table 1 (primary-submission ranking); findings bullets
             ("BLEU is ranked last"; neural metrics "robust to different domains").
Quote:       "Stop Using BLEU - Neural Metrics Are Better and More Robust" (title).
             "Out of 13 reference-based metrics BLEU is ranked last" (findings).
```

```text
URL:         https://aclanthology.org/2022.aacl-main.83/
Kind:        primary. Amrhein and Sennrich (University of Zurich / Edinburgh) own the
             COMET number/named-entity blind-spot finding. arXiv: https://arxiv.org/abs/2202.05148.
Establishes: The case where COMET itself misled. Using COMET as the utility function in
             sample-based MBR decoding (choosing the translation most similar to a pool of
             candidates) systematically selects outputs with wrong numbers and mistranslated
             named entities, because COMET is not sensitive enough to those discrepancies.
             Models tested: wmt20-comet-da (DA-trained) and wmt21-comet-mqm (MQM-trained).
             A sensitivity analysis shows perturbing a number or named entity changes the
             COMET score far less than perturbing a random noun. Beam search output has the
             highest number/NE accuracy; MBR-with-COMET the lowest. Retraining COMET on
             synthetic perturbed data does not fully remove the blind spot.
Paraphrase:  Optimizing toward COMET amplifies exactly the errors it cannot see. The
             concrete cost is meaning-changing: the worked example flips a year (source and
             reference say Green left the band in 1970; MBR-COMET chose "1980") and garbles
             a person's name ("Tebboune" to "Tebboene", "Mahmoud" to "Mahmud"). This is the
             "misled, with a cost" case, and it is about *using COMET to select or optimize*
             translations, not about ranking finished systems.
Locators:    Abstract; Table 1 (worked examples); Sec 5 + Table 2 (F1 for numbers/NEs by
             decoding method; genuine-error rates); Sec 6 + Table 3 (sensitivity analysis);
             Sec 7 (retraining fails to close the gap).
Quote:       "COMET models are not sensitive enough to discrepancies in numbers and named
             entities" (Abstract). "all targeted changes to numbers or named entities
             result in a much smaller difference in MBR score compared to changes to the
             random nouns" (Sec 6).
```

```text
URL:         https://arxiv.org/abs/2408.15366
Kind:        primary for its own experiments (Zouhar, Chen, Lam, Moghe, Haddow; ETH Zurich /
             Edinburgh); secondary where it relays others' findings (Amrhein and Sennrich;
             Yan et al.). It owns the version/precision/direction non-comparability tests.
Establishes: A bare COMET number is not comparable across setups. (1) Software version:
             the same COMETDA22 checkpoint scores WMT23 En->De at 0.796 under unbabel-comet
             1.1.2 but 0.837 under 2.2.2 (Table 1). (2) Cross-direction: average human DA in
             WMT data ranges from 0.51 (En->Gu, De->Cs) to 0.91 (Hi->Bn), so COMET scores
             for different directions are "not comparable" (Table 6, Sec 3.5). (3) Empty and
             wrong-language hypotheses get positive scores; some empty lines outscore a real
             translation (Tables 3-5). (4) A domain/year tag can shift the average score
             (Tables 8-9). (5) Reporting: at least 12% of examined papers report COMET scores
             without naming the model version, and most cite only the 2020 paper rather than
             the specific checkpoint. (6) Over-optimization: relays that Yan et al. (2023)
             found COMET-trained models generate "universal translations" (hallucinations)
             COMET prefers regardless of source, and that Unbabel-Tower70B at WMT24 used MBR
             to dominate automatic metrics "but not so much under human evaluation."
Paraphrase:  The strongest single source for "a bare COMET number is uninterpretable": it
             depends on the model version, the software version, the language direction, and
             the domain. Also supplies the reference-based COMETDA22 vs reference-free
             COMETkiwiDA22 distinction and that both output 0-1.
Locators:    Abstract; Sec 3.1 (Table 1, software version); Sec 3.3 (Tables 3-4, empty
             hypothesis); Sec 3.4 (Table 5, language mismatch); Sec 3.5 (Table 6-7,
             direction bias); Sec 3.6 (Tables 8-9, domain-tag gaming); Sec 3.9 (12% figure);
             Sec 3.10 (Optimizing to COMET; universal translations; WMT24 MBR).
Quote:       "COMET scores for different translation directions are not comparable" (Sec 3.5).
             "at least 12% of papers report COMET scores without specific model information"
             (Sec 3.9).
```

```text
URL:         https://github.com/Unbabel/COMET
Kind:        primary. The tool owner's (Unbabel) own documentation of model versions,
             score ranges, and comparability. Model page: https://huggingface.co/Unbabel/wmt22-comet-da.
Establishes: The reference-based vs reference-free (QE) distinction and version
             non-transferability, stated by the authors themselves. Default reference-based
             model is Unbabel/wmt22-comet-da (XLM-R, trained on DA from WMT17-WMT20, scores
             0 to 1, 1 = perfect). Reference-free model is Unbabel/wmt22-cometkiwi-da (built
             on InfoXLM, trained on WMT17-WMT20 DA plus MLQE-PE, scores 0 to 1). Pre-2022
             models (wmt20-comet-da, wmt20-comet-qe-da, package <2.0) produce a raw score
             that "does not have a direct interpretation"; since 2022 scores are rescaled to
             0-1. Users comparing against pre-2022 papers are told to use the old checkpoints.
Paraphrase:  The people who ship COMET state plainly that scores are version-dependent and
             that a QE (reference-free) model is a separate checkpoint from the reference-based
             one. Authoritative for "which model is which" and "the number means nothing
             without the version."
Locators:    README "COMET Models" section (default wmt22-comet-da; reference-free
             wmt22-cometkiwi-da; pre-2022 checkpoints); "Interpreting Scores" section.
Quote:       "trained on direct assessments from WMT17 to WMT20 and provides scores ranging
             from 0 to 1, where 1 signifies a perfect translation" (wmt22-comet-da).
             "While the raw score itself does not have a direct interpretation ... since 2022
             we have introduced a new training approach that scales the scores between 0 and
             1" (Interpreting Scores). "If you intend to compare your results with papers
             published before 2022, it's likely that they used older evaluation models."
```

```text
URL:         https://arxiv.org/abs/2106.15195
Kind:        secondary (for this article). Marie, Fujita, Rubino meta-evaluate 769 other
             papers; they report on the field's practices from outside, which is the context
             for why COMET was needed. (Primary for its own survey statistics.)
Establishes: The field's over-reliance on BLEU that COMET was meant to correct. Of 769
             *ACL MT papers published 2010-2020, 98.8% use BLEU; 74.3% use only BLEU with no
             other metric and no human evaluation (82.1% under a looser count); nearly 40%
             report comparisons using metric scores copied from other papers (38.5% in
             2019-2020); statistical significance testing was done by never more than 65% of
             papers. 108 metrics have claimed to beat BLEU, yet BLEU persists.
Paraphrase:  Background/motivation only. Corroborates the "the field ran on a single
             string-overlap number" backdrop. To Ship (Kocmi et al.) repeats the 98.8% and
             ~40% figures; this is their origin, so cite this for the numbers.
Locators:    Abstract; Sec 3.1 ("The 99% BLEU", 98.8%, 74.3%, 82.1%); Sec on copied scores
             (~40%, 38.5%); significance-testing figure.
Quote:       "98.8% of the annotated [papers] uses BLEU ... 74.3%, only used BLEU scores to
             evaluate MT" (Sec 3.1).
```

## Contradictions

- **The main deployment-decision primary exonerates COMET, not indicts it.** Kocmi et
  al. (2021) is the study that ties metric choice to shipping models, and its verdict is
  that COMET is the most reliable metric and BLEU is the one that caused bad decisions
  (203 human-significant pairs flipped by BLEU, median 1.3 BLEU). A writer who reaches for
  "To Ship or Not to Ship" as a case where COMET misled will misread it. The genuine
  COMET-misled case is over-optimization (Amrhein and Sennrich, 2022; Zouhar et al., 2024,
  Sec 3.10), not system ranking.

- **COMET catches number swaps in a minimal-pair test but not in a realistic pool.**
  Amrhein and Sennrich (Sec 6) note their finding "stands in contrast to the corrupted
  reference analysis" of the WMT 2021 metrics task, where COMET mostly preferred the correct
  translation over one with swapped numbers. The reconciliation: given a clean pair that
  differs only in a number, COMET can tell; given a realistic pool of noisy candidates, its
  insensitivity to numbers lets worse ones win. The writer should not overstate the blind
  spot as "COMET ignores numbers."

- **The newer, MQM-trained checkpoint is more blind to numbers/names, not less.** In
  Amrhein and Sennrich (Table 2), wmt21-comet-mqm selects worse number/named-entity outputs
  than wmt20-comet-da (number-error rate 16.6% vs 7.2% over de<->en). Newer version does not
  mean better on every axis; a "COMET improved over versions" claim needs this caveat.

- **Domain robustness: two primaries, different scopes.** Kocmi et al. (Sec 5.2) find COMET
  "is not overfitted to the WMT news domain or WMT languages" for pairwise *ranking accuracy*.
  Zouhar et al. (Sec 3.5-3.6) find COMET's *absolute scores* carry direction and domain bias
  and can be gamed. Not a direct contradiction (ranking vs absolute score), but the writer
  must not generalize either finding past its scope.

- **"Human judgment is the gold standard" is itself contested.** Freitag et al. (2021) find
  pretrained metrics can outperform crowd workers, and that crowd DA (COMET's main pre-2022
  training signal) diverges from expert MQM. So COMET was partly trained to imitate a signal
  now known to be flawed, which is the mechanism behind the commission's "only as good as its
  ratings" point but also complicates any clean "metric vs human truth" narrative.

## Numbers

```text
Figure: XLM-RoBERTa (base) encoder; three models in the 2020 paper (COMET-HTER,
        COMET-MQM, COMET-RANK)
Owner:  Rei et al., 2020 (Sec 2.1, 4)
Scope:  The founding paper's models, distinct from later shipped checkpoints
        (wmt20-comet-da, wmt22-comet-da). Do not conflate.
```

```text
Figure: MQM = 100 - (I_Minor + 5 x I_Major + 10 x I_Crit.) / Sentence Length x 100
Owner:  Rei et al., 2020 (Eq. 7) -- the paper's internal MQM definition
Scope:  Their proprietary MQM corpus, 12K tuples, English always source.
```

```text
Figure: MQM error weights -- Minor 1, Major 5 (standard allows up to 10),
        Non-translation 25, Minor Fluency/Punctuation 0.1
Owner:  Freitag et al., 2021 (Table 1) -- the standard MQM scoring scheme
Scope:  WMT 2020 En-De and Zh-En, professional-translator annotation.
```

```text
Figure: 2.3M human judgments; 4380 systems; 101 languages; 232 directions
Owner:  Kocmi et al., 2021 (Abstract, Sec 2.2)
Scope:  Microsoft internal + public judgments, mid-2018 to early 2021, source-based DA.
```

```text
Figure: Pairwise ranking accuracy (All pairs): COMET 83.4, COMET-src 83.2, ChrF 75.6,
        BLEU 74.6
Owner:  Kocmi et al., 2021 (Table 2)
Scope:  3344 system pairs; accuracy = sign agreement with human delta. Column-comparable
        only within Table 2.
```

```text
Figure: 203 system pairs (human p<0.05) where BLEU flips the ranking; median 1.3 BLEU points
Owner:  Kocmi et al., 2021 (Sec 5.3)
Scope:  The BLEU-misled deployment result. About BLEU, not COMET.
```

```text
Figure: WMT22 primary-submission ranking (avg rank): COMET-22 1.32; BLEURT-20 1.91;
        COMET-20 2.36; ...; BLEU 5.31 (last of 13 reference-based metrics)
Owner:  Freitag et al., 2022 (Table 1)
Scope:  Against MQM human ratings across news, social, ecommerce, chat.
```

```text
Figure: Number/named-entity F1 change vs reference under MBR (de-en / en-de):
        beam search highest; MBR wmt20-comet-da number F1 -2.90 (de-en); MBR
        wmt20-comet-da named-entity F1 -23.49 (en-de); wmt21-comet-mqm worse still
        (-10.89 numbers de-en, -24.35 NE en-de). Genuine number-error rate: BLEU 4.4%,
        chrF++ 4.6%, wmt20-comet-da 7.2%, wmt21-comet-mqm 16.6%.
Owner:  Amrhein and Sennrich, 2022 (Table 2)
Scope:  WMT21 news de<->en, 100-sample MBR pools; F1 approximate (~3% false-positive rate).
```

```text
Figure: Sensitivity (avg MBR score drop, samples as support, wmt20-comet-da):
        number -0.037, named entity -0.068, random noun -0.232
Owner:  Amrhein and Sennrich, 2022 (Table 3)
Scope:  de<->en. Smaller magnitude = less sensitive. COMET is least sensitive to the
        errors that most change meaning.
```

```text
Figure: Same COMETDA22 checkpoint, WMT23 En->De: 0.796 (unbabel-comet 1.1.2) vs 0.837 (2.2.2)
Owner:  Zouhar et al., 2024 (Table 1)
Scope:  Software-version effect only; checkpoint held constant. Version-specific.
```

```text
Figure: Average human DA per WMT direction ranges 0.51 (En->Gu, De->Cs) to 0.91 (Hi->Bn)
Owner:  Zouhar et al., 2024 (Table 6)
Scope:  WMT data up to 2023. Shows scores are not comparable across directions.
```

```text
Figure: Empty hypothesis scores positive (e.g. COMETDA22 En->De empty 0.335 vs real 0.837);
        some empty lines outscore a real translation (up to ~1.45% of lines, De->En kiwi)
Owner:  Zouhar et al., 2024 (Tables 3-4)
Scope:  WMT23 Online-A, COMETDA22 / COMETkiwiDA22. Version-specific.
```

```text
Figure: 98.8% of 769 MT papers (2010-2020) use BLEU; 74.3% use only BLEU; ~40% copy scores
Owner:  Marie et al., 2021 (Sec 3.1)
Scope:  *ACL main-conference MT papers. Background/motivation figure.
```

## Source assets

```text
Asset: Amrhein and Sennrich, 2022, Table 1 (worked MBR examples), and the "Green left
       the band in 1970/1980" line in particular.
Shows: In one glance, a real translation COMET preferred that changed a date and a name.
       This carries the "misled, with a cost" point better than any prose paraphrase.
Crop:  Keep the source, the reference, and the MBR-COMET output for one example so the
       reader sees the swapped number against the correct one; omit the second example if
       space is tight. Present as quoted text, not a screenshot of the PDF table.
```

```text
Asset: Zouhar et al., 2024, Table 1 (same checkpoint, two software versions).
Shows: A single number (En->De: 0.796 vs 0.837) proving the score is not reproducible
       without the software version. Strong, compact evidence for "report the version."
Crop:  The four direction rows and the two version columns. Retain the checkpoint name so
       the reader sees the model was held constant.
```

```text
Asset: Kocmi et al., 2021, Table 2 (accuracy column "All").
Shows: COMET 83.4 vs BLEU 74.6 in one column -- the size of COMET's reliability edge over
       BLEU for ranking systems, which is the "why it replaced BLEU" evidence.
Crop:  The "All" column and the COMET / ChrF / BLEU rows suffice; the significance-level
       columns are not needed for the lesson and would need their own explanation.
```

```text
Asset: A rendered chart (chart-N.py) is only worth it if the writer contrasts number/NE
       sensitivity across metrics (Amrhein Table 2 or 3). Otherwise the two-number
       comparisons above read better inline.
Shows: The gap between COMET's insensitivity to numbers/NEs and its sensitivity to
       ordinary words.
Crop:  n/a. If charted, label axes (F1 or MBR-score drop), name the COMET version, and
       cite Amrhein and Sennrich, 2022.
```

## Discarded

```text
URL: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00437 : MIT Press mirror of
     Freitag et al. 2021 (Experts, Errors, Context). Same paper as the ACL Anthology entry
     already cited; kept the aclanthology.org canonical page. Not a second source.
```

```text
URL: https://www.researchgate.net/publication/347234911 and other ResearchGate mirrors:
     re-hosted copies of the COMET 2020 paper; not canonical and gated. Used the ACL
     Anthology page instead.
```

```text
URL: https://arxiv.org/abs/2205.00978 (Fernandes et al., "Quality-Aware Decoding"):
     read far enough to see it proposes QE/COMET-guided decoding rather than documenting a
     harm. Amrhein and Sennrich and Zouhar et al. carry the over-optimization case more
     directly, so this was not cited to avoid padding.
```

```text
URL: https://aclanthology.org/2021.wmt-1.73 (Freitag et al., WMT21 metrics findings):
     relevant but its number-swap result reaches this record only through Amrhein and
     Sennrich's contrast (Sec 6). Cited via Amrhein rather than asserted independently,
     since the WMT21 passage was not read in full here. Flagged for a later round if the
     writer wants the corrupted-reference detail firsthand.
```

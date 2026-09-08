# Evidence: the-instruments/auroc (01)

The evidence fully supports the commission's angle. Hanley & McNeil (1982) owns
the claim that AUROC equals the probability a random positive is ranked above a
random negative, the same quantity the Wilcoxon statistic estimates. Saito &
Rehmsmeier (2015) owns the axis definitions, the 0.5-to-1.0 baseline, and the
central imbalance result: ROC and AUROC are unchanged between balanced and
imbalanced versions of the same data, while precision falls. Wong et al. (2021)
owns every Epic Sepsis Model figure the lesson turns on: external AUROC 0.63
against a vendor-reported 0.76-0.83, sensitivity 33% at the deployed threshold of
6 (missing 67% of sepsis cases), and an alert burden of 8 to 109 patients
evaluated per case found. Ostermayer et al. (2024) independently corroborates
poor field performance. Two places need care. First, the record supplies no
verified ROC *series* for a real system: Wong reports one operating point and a
single AUROC, not the curve's coordinates, so an honest ROC curve of Epic's model
cannot be drawn from this evidence. Second, McDermott et al. (2024) refutes the
blanket prescription "prefer AUPRC under imbalance." That nuances the lesson's
third teaching point but does not undercut the angle: AUROC's prevalence
independence, the thing that lets a high score coexist with poor PPV, is exactly
what McDermott confirms.

## Sources

```text
URL:         https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307
Kind:        primary. This external validation owns its own measured figures for
             the Epic Sepsis Model; it is the study the commission names.
Establishes: The Epic Sepsis Model (ESM), run on Michigan Medicine data, scored a
             hospitalization-level AUROC of 0.63 (95% CI, 0.62-0.64), well below
             Epic's own 0.76-0.83. At the deployed alert threshold (score >=6) it
             had sensitivity 33%, specificity 83%, PPV 12%, NPV 95%, missed 67%
             of sepsis cases, alerted on 18% of hospitalizations, and required
             evaluating 8 to 109 patients per true case.
Paraphrase:  In a retrospective cohort of 27,697 patients and 38,455
             hospitalizations (Dec 6, 2018 to Oct 20, 2019), sepsis occurred in
             2,552 (7%). At the developer-suggested threshold of 6 (range 5-8),
             the ESM identified a minority of sepsis cases and generated many
             alerts on patients who did not develop sepsis. Its externally
             measured AUROC was substantially below the AUC Epic reported in
             internal documentation and a prior conference proceeding.
Locators:    Abstract; Results; Methods ("Selection of High-risk Threshold");
             Discussion. Figure 1 (ROC and operating characteristics); Table 2
             (number needed to evaluate).
Quote:       "hospitalization-level area under the receiver operating
             characteristic curve of 0.63 (95% CI, 0.62-0.64)"
             "substantially worse than that reported by Epic Systems (AUC,
             0.76-0.83) in internal documentation ... and in a prior conference
             proceeding coauthored with Epic Systems (AUC, 0.73)"
             "The ESM did not identify 1709 patients with sepsis (67%), of whom
             1030 (60%) still received timely antibiotics."
             "clinicians would still need to evaluate 8 patients to identify a
             single patient with eventual sepsis."
             "they would need to evaluate 109 patients to find a single patient
             with sepsis."
             "An ESM score of 6 or higher occurred in 18% of hospitalizations
             (6971 of 38 455) even when not considering repeated alerts."
Citation:    Wong A, et al. External Validation of a Widely Implemented
             Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA
             Intern Med. 2021;181(8):1065-1070. doi:10.1001/jamainternmed.2021.2626
```

```text
URL:         https://jhanley.biostat.mcgill.ca/software/Hanley_McNeil_Radiology_82.pdf
Kind:        primary. This paper owns the interpretation of the ROC area and its
             equivalence to the Wilcoxon/Mann-Whitney statistic.
Establishes: The area under an ROC curve equals the probability that a randomly
             chosen diseased (positive) subject is rated with greater suspicion
             than a randomly chosen non-diseased (negative) subject, and this is
             the quantity the Wilcoxon statistic estimates.
Paraphrase:  The area is a ranking probability, not an accuracy or a threshold
             performance. It is estimable nonparametrically by the Wilcoxon rank
             sum, which is why AUROC and the Mann-Whitney U describe the same
             thing. Two consequences the lesson uses follow directly from this
             ranking-only definition and need no separate source: AUROC depends
             only on the order of scores, so any monotonic rescaling that changes
             calibration leaves AUROC unchanged (calibration-independence), and it
             averages over all thresholds rather than the one a deployment picks
             (threshold-independence).
Locators:    Abstract; opening exposition. (Source is a scanned PDF; the
             ranking-probability and Wilcoxon claims were read from the abstract
             and lead text. The 0.5/1.0 boundary reading below is pinned to Saito
             & Rehmsmeier, which states it in words.)
Quote:       "the area under it ... represents the probability that a randomly
             chosen diseased subject is (correctly) rated or ranked with greater
             suspicion than a randomly chosen non-diseased subject."
             "this probability of a correct ranking is the same quantity that is
             estimated by the already well-studied nonparametric Wilcoxon
             statistic."
Citation:    Hanley JA, McNeil BJ. The meaning and use of the area under a
             receiver operating characteristic (ROC) curve. Radiology.
             1982;143(1):29-36. PMID 7063747.
```

```text
URL:         https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432
Kind:        primary. Owns the axis definitions used here, the AUROC baseline
             statement, and the imbalance result contrasting ROC with
             precision-recall.
Establishes: The ROC plot has FPR (1-specificity) on x and TPR (sensitivity) on
             y; the precision-recall plot has recall/sensitivity on x and
             precision/PPV on y. AUROC is 0.5 for a random classifier and 1.0 for
             a perfect one. ROC curves and AUROC are unchanged between balanced
             and imbalanced versions of the same data; only the precision-recall
             curve changes with the positive-to-negative ratio, because its
             baseline is P/(P+N). A worked example: identical classifier outcomes
             give precision 0.6 when classes are balanced and 0.33 when
             imbalanced.
Paraphrase:  Because TPR and FPR are each computed within one class, class
             prevalence does not move the ROC curve or its area. Precision mixes
             true positives against all positive predictions, so it falls as
             negatives grow. This is why a model can hold a strong AUROC while its
             precision (PPV) collapses under rare positives.
Locators:    Sections "ROC: The ROC plot provides a model-wide evaluation";
             "PRC: ... its baseline moves with class distribution"; "Simulation";
             Table 2 (worked confusion-matrix example).
Quote:       "AUC is 0.5 for random and 1.0 for perfect classifiers."
             "The ROC plots are unchanged between balanced and imbalanced
             datasets ... and all AUC (ROC) scores are unchanged accordingly."
             "Only PRC changes with the ratio of positives and negatives."
             "The baseline of PRC is determined by the ratio of positives (P) and
             negatives (N) as y = P / (P + N)."
             "precision (PREC/PPV) indicates that the performance of the
             classifier is fine on the balanced (0.6) but relatively poor on the
             imbalanced dataset (0.33)."
Citation:    Saito T, Rehmsmeier M. The Precision-Recall Plot Is More Informative
             than the ROC Plot When Evaluating Binary Classifiers on Imbalanced
             Datasets. PLoS ONE. 2015;10(3):e0118432.
             doi:10.1371/journal.pone.0118432
```

```text
URL:         https://mlanthology.org/icml/2006/davis2006icml-relationship/
Kind:        primary. Owns the formal relationship between precision-recall and
             ROC space. Read at abstract level; the internal proofs were not
             extracted, so cite only what the abstract states.
Establishes: For highly skewed data, precision-recall curves give a more
             informative picture than ROC, and an algorithm that optimizes the
             area under the ROC curve is not guaranteed to optimize the area under
             the precision-recall curve.
Paraphrase:  The two curves are connected (dominance in one space implies
             dominance in the other), but the areas are not interchangeable
             optimization targets, and PR is the more revealing view when
             positives are rare.
Locators:    Abstract.
Quote:       "When dealing with highly skewed datasets, Precision-Recall (PR)
             curves give a more informative picture of an algorithm's
             performance."
             "algorithms that optimize the area under the ROC curve are not
             guaranteed to optimize the area under the PR curve."
Citation:    Davis J, Goadrich M. The Relationship Between Precision-Recall and
             ROC Curves. Proc. 23rd Int. Conf. Machine Learning (ICML). 2006:
             233-240.
```

```text
URL:         https://arxiv.org/abs/2401.06091
Kind:        primary. Owns a refutation of the "AUPRC is superior under imbalance"
             claim; relevant to the lesson's third teaching point and to
             Contradictions.
Establishes: The widespread claim that AUPRC is a superior metric to AUROC under
             class imbalance is wrong as stated. AUPRC can favor subpopulations
             with more frequent positives and worsen algorithmic disparities. The
             belief spread through uncited claims and over-generalizations. The
             paper does not dispute that AUROC is prevalence-independent; it
             disputes the prescription that follows.
Paraphrase:  Use this to keep the imbalance point precise. The defensible claim is
             that AUROC ignores prevalence, so a high AUROC can coexist with poor
             PPV. The claim this paper rejects is "therefore always prefer AUPRC."
Locators:    Abstract; framing of the two "fronts."
Quote:       "a widespread claim is that the area under the precision-recall curve
             (AUPRC) is a superior metric for model comparison to the area under
             the receiver operating characteristic (AUROC) for tasks with class
             imbalance. This paper refutes this notion on two fronts."
Citation:    McDermott MBA, et al. A Closer Look at AUROC and AUPRC under Class
             Imbalance. NeurIPS 2024. arXiv:2401.06091.
```

```text
URL:         https://pmc.ncbi.nlm.nih.gov/articles/PMC11560849/
Kind:        primary. An independent external validation of the Epic sepsis model;
             owns its own field figures and corroborates Wong et al.
Establishes: In two county emergency departments (145,885 encounters, 2023), the
             Epic sepsis predictive model (ESPMv1) had sensitivity 14.7%,
             specificity 95.3%, PPV 7.6%, NPV 97.7%, with a median alert lead time
             of 0 minutes and alerts before sepsis in only half of cases. The
             authors say results align with prior external validations and are
             slightly worse than Epic's published analysis. AUROC was not reported
             in the extracted content.
Paraphrase:  A second, larger, differently-sited validation finds the model even
             less sensitive than Wong did, reinforcing that the deployment
             shortfall is not a Michigan-specific artifact.
Locators:    Results; Discussion.
Quote:       "alerted providers with a median lead time of 0 minutes ... and only
             alerted providers in half of the cases prior to sepsis occurrence."
Citation:    Ostermayer DG, et al. External validation of the Epic sepsis
             predictive model in 2 county emergency departments. JAMIA Open.
             2024;7(4):ooae133. doi:10.1093/jamiaopen/ooae133
```

```text
URL:         https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781313
Kind:        secondary. An invited editorial commenting on Wong et al.; it repeats
             the study's figures and argues from them. It does not own the
             measurements.
Establishes: That independent experts read the Wong result as a failure of vendor
             self-report, and clarifies that the 0.76-0.83 vendor AUC was jointly
             reported by Epic and University of Colorado Health. Its argument is
             the general need for independent external validation of proprietary
             clinical prediction models.
Paraphrase:  Use for the "why this matters beyond one model" framing and to
             attribute the vendor AUC to a named joint report, not to Epic alone.
             The figures it cites are Wong's; cite Wong for the numbers.
Locators:    Full text; author block.
Quote:       "the ESM had a sensitivity of 33%, specificity of 83%, positive
             predictive value of 12%, and negative predictive value of 95%, with
             an area under the curve of 0.63 (95% CI, 0.62-0.64)."
             "falls short of the area under the curve of 0.76 to 0.83 that was
             jointly reported by Epic and University of Colorado Health."
Citation:    Habib AR, Lin AL, Grant RW. The Epic Sepsis Model Falls Short - The
             Importance of External Validation. JAMA Intern Med.
             2021;181(8):1040-1041. Authors: UCSF (Habib, Lin) and Kaiser
             Permanente Division of Research (Grant). doi:10.1001/jamainternmed.2021.3333
```

```text
URL:         https://www.statnews.com/2021/09/27/epic-sepsis-algorithm-antibiotics-model/
Kind:        secondary. Investigative reporting; owns none of the model figures
             but reports a mechanism and reactions from outside Epic.
Establishes: That the model's inputs included whether a clinician had already
             ordered antibiotics, an input Epic had not publicly disclosed, and
             that this contributed to the gap between internal and field
             performance. Multiple health systems that validated it locally found
             it worse than advertised.
Paraphrase:  This is the leakage explanation for the two AUROC numbers: an input
             that reflects the clinician's own suspicion inflates apparent ranking
             on retrospective data while adding little at the bedside. It also
             fits Wong's finding that 60% of missed cases got timely antibiotics
             anyway. The reported mechanism is single-origin (STAT's reporting);
             treat it as one source, not independent confirmation. Full text is
             partly paywalled; Epic's own on-record rebuttal was not fully
             captured here.
Locators:    Body (Casey Ross, Sept 27, 2021).
Quote:       "The use of that information, which has not been publicly disclosed by
             the company, is contributing to a discrepancy between the accuracy of
             the algorithm in Epic's internal testing and its performance in the
             outside world."
Citation:    Ross C. Epic's sepsis algorithm is going off the rails in the real
             world. STAT News. Sept 27, 2021.
```

## Contradictions

- **The imbalance prescription is contested; the imbalance fact is not.**
  Saito & Rehmsmeier (2015) and Davis & Goadrich (2006) argue precision-recall
  is more informative than ROC on skewed data. McDermott et al. (2024)
  *refutes* the stronger claim that AUPRC is a superior metric under imbalance,
  and shows it can worsen algorithmic disparities. All three agree on the
  underlying fact the lesson needs: AUROC does not move with prevalence, so a
  high AUROC can sit next to poor PPV. The lesson should teach the fact (AUROC
  ignores prevalence; precision does not) and avoid the contested prescription
  ("always prefer AUPRC"). Framing the imbalance point as a metric horse-race
  would import the dispute McDermott documents.

- **AUROC is not "wrong"; it answers a narrower question.** The steelman for
  AUROC is that its independence from class skew and threshold is a feature when
  the task is to compare rankers across settings with different prevalence.
  Saito & Rehmsmeier and the ROC literature treat prevalence-independence as a
  deliberate property, not a defect. The lesson's claim should be that AUROC is
  read as if it measured calibration, threshold performance, and precision when
  it measures none of them, not that AUROC is a bad number.

- **No dispute found over Wong's measured numbers.** The county-ED validation
  (Ostermayer 2024) finds field performance at least as poor. The STAT
  reporting explains, rather than contests, the gap between Epic's AUC and the
  external one. No source read here disputes Wong's 0.63 or the sensitivity at
  threshold 6.

- **Gap: Epic's own response and later model.** Epic's on-record rebuttal and
  any subsequent model revision (the commission asks about "Epic's subsequent
  model changes") are not established by a primary in this record; the STAT text
  that would carry Epic's statement is partly paywalled, and no primary Epic
  document was reachable. The lesson should not assert what Epic did next
  without a source. If that thread matters, it needs a further brief.

## Numbers

```text
Figure: AUROC 0.63 (95% CI, 0.62-0.64), hospitalization-level
Owner:  Wong et al. 2021 (external validation)
Scope:  27,697 patients / 38,455 hospitalizations, Michigan Medicine, Dec 6,
        2018 - Oct 20, 2019; sepsis in 2,552 (7%).
```

```text
Figure: Vendor-reported AUC 0.76-0.83 (internal documentation); 0.73 (prior
        conference proceeding coauthored with Epic)
Owner:  Epic Systems, as reported by Wong et al.; Habib et al. attributes the
        0.76-0.83 to a joint Epic / University of Colorado Health report
Scope:  Vendor / developer-side, not independently validated. Epic's own model
        documentation was not publicly reachable.
```

```text
Figure: Sensitivity 33%, specificity 83%, PPV 12%, NPV 95% at ESM score >=6
Owner:  Wong et al. 2021
Scope:  Deployed threshold; developer-suggested range 5-8. Implies an ROC
        operating point of (FPR 0.17, TPR 0.33).
```

```text
Figure: Missed 67% of sepsis cases (1,709 of 2,552); of those, 60% (1,030)
        received timely antibiotics anyway
Owner:  Wong et al. 2021
Scope:  Same cohort; second figure bounds the model's added value.
```

```text
Figure: Alert burden - 8 patients evaluated per case found (one alert per
        patient at first crossing of 6); 109 patients per case found (re-alerting
        each time score exceeds 6, 4-hour horizon); alerts on 18% of
        hospitalizations (6,971 of 38,455)
Owner:  Wong et al. 2021
Scope:  Same cohort; the two figures bracket best-case and repeated-alert
        strategies.
```

```text
Figure: Sensitivity 14.7%, specificity 95.3%, PPV 7.6%, NPV 97.7% (6-hour
        window); median alert lead time 0 minutes
Owner:  Ostermayer et al. 2024 (JAMIA Open)
Scope:  145,885 ED encounters, two Houston county EDs, 2023. Different site and
        care setting from Wong; corroborates poor field performance.
```

```text
Figure: AUROC baseline - 0.5 for a random classifier, 1.0 for a perfect one
Owner:  Saito & Rehmsmeier 2015
Scope:  General property of the metric.
```

```text
Figure: Worked imbalance example - identical classifier outcomes yield precision
        0.6 (balanced) vs 0.33 (imbalanced); ROC and AUROC unchanged; PRC
        baseline = P/(P+N)
Owner:  Saito & Rehmsmeier 2015 (Table 2)
Scope:  Illustrative confusion-matrix example, not a real system. This is the one
        verified, honestly-sourced series available for a teaching visual.
```

**On a possible ROC chart.** No verified ROC *series* for the Epic model (or any
real system) exists in the sources read. Wong reports a single AUROC (0.63) and a
single operating point (sensitivity 33%, specificity 83%, i.e. the ROC point
(0.17, 0.33)); the curve's coordinates are not published in extractable form. An
honest ROC *curve* of Epic's model therefore cannot be drawn from this evidence,
and the commission forbids fabricating one. Two honest options remain: (a) a
small table contrasting the balanced-vs-imbalanced worked example from Saito &
Rehmsmeier (precision 0.6 to 0.33 while AUROC holds), which teaches the imbalance
point directly; or (b) a schematic ROC diagram with a single plotted operating
point for Epic against the chance diagonal, captioned as one operating point on
an AUROC-0.63 model, not a reconstructed curve. Prefer (a) if a chart is used.

## Source assets

```text
Asset: Wong et al. 2021, Figure 1 (ROC curve and operating characteristics for
       the ESM).
Shows: The gap between the summary AUROC and the single point the deployment
       actually operates at; a reader can see the threshold-6 point sitting low
       on a mediocre curve.
Crop:  Must retain the axis labels (sensitivity vs 1-specificity), the chance
       diagonal, and the threshold-6 operating point if marked. Do not crop to a
       flattering segment of the curve.
```

```text
Asset: Wong et al. 2021, Table 2 (number needed to evaluate).
Shows: The 8-vs-109 alert burden, the concrete cost of a low PPV at a rare
       positive rate.
Crop:  Retain both the single-alert (8) and repeated-alert (109) rows and the
       threshold they assume. Omitting either row misstates the burden.
```

```text
Asset: Saito & Rehmsmeier 2015, the balanced-vs-imbalanced worked example (Table
       2 and its ROC/PRC panels).
Shows: The same classifier outcomes holding AUROC steady while precision drops
       from 0.6 to 0.33 as negatives grow.
Crop:  Keep the two confusion matrices and the precision figures side by side. A
       teaching table rebuilt from these numbers is cleaner than the source
       panels.
```

```text
Asset: None found for a defensible full ROC curve of the Epic model. See the
       chart note above.
Shows: -
Crop:  -
```

## Discarded

```text
URL: https://pubmed.ncbi.nlm.nih.gov/34152373/ - cookie wall on fetch; the full
     article at jamanetwork carries the same content and was used instead.
URL: https://journals.lww.com/ccejournal/fulltext/2023/07000/epic_sepsis_model_inpatient_predictive_analytic.8.aspx
     - HTTP 402 paywall; a second external validation, not needed once Wong and
     Ostermayer were secured.
URL: https://people.inf.elte.hu/kiss/13dwhdm/roc.pdf - Fawcett 2006, "An
     introduction to ROC analysis." A clean primary for the axis formulas and the
     0.5 diagonal, but the scanned/encoded PDF would not yield extractable text
     on repeated attempts. Those claims are pinned to Saito & Rehmsmeier and
     Hanley & McNeil instead, so nothing here rests on an unread source.
URL: https://vibegraveyard.ai/story/epic-sepsis-model-missed-patients/ - popular
     retelling of the Wong story; adds nothing the primary does not own, and its
     "109 alerts" phrasing risks being read as the only burden figure.
URL: https://www.obgproject.com/2021/07/18/... - secondary summary of Wong;
     redundant with the primary.
```

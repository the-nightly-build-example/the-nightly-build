# Evidence record: the-instruments/f1-score (01)

The evidence firmly supports the lesson's core teaching. The definitions and every
formula the article needs are pinned to primaries: precision and recall, the harmonic
mean, van Rijsbergen's effectiveness measure E and its Fβ descendant, the confusion-matrix
form 2TP/(2TP+FP+FN), and the micro/macro/weighted averaging schemes. The "misled people"
requirement has strong primary support in Chicco & Jurman (2020), whose six synthetic
confusion matrices and one real colon-cancer experiment are recorded here with exact
numbers, all recomputed independently and confirmed. A second, distinct ranking flip is
documented in Opitz & Burst (2019): two formulas both called "macro F1" reverse which of
two classifiers looks better. Lipton et al. (2014) supplies the sharpest single pitfall,
that an uninformative classifier maximizes F1 by labeling everything positive.

The record is thin in one specific place named by the brief. I did not find a single
real, named public leaderboard or shared task where a micro-versus-macro choice is
documented, with primary support, to have flipped the announced winner. The strongest
real ranking flip I could pin to primary data is Chicco's colon-cancer table, which turns
on metric choice (F1/accuracy versus MCC), not on micro-versus-macro averaging. The
micro/macro flip is supported at the level of demonstrated mechanism (Opitz & Burst) and
canonical definition (scikit-learn), not a named contest result. One primary that would
have strengthened this, Yang & Liu (1999), sits behind the ACM paywall and I did not read
it; its owner is the ACM Digital Library. The evidence does not undermine the commissioned
angle. It complicates one sub-claim: F1 is the correct tool, not a flaw, in the retrieval
setting it was built for, where true negatives are unbounded and uninformative. That
steelman is in Contradictions.

## Sources

```text
URL:         https://www.dcs.gla.ac.uk/Keith/Chapter.7/Ch.7.html
Kind:        primary. Van Rijsbergen is the author of Information Retrieval (Butterworths,
             1979); Chapter 7 is where he derives the effectiveness measure. He owns it.
Establishes: The origin of the measure. Recall is the "conditional probability that an item
             will be retrieved given that it is relevant"; precision is the "conditional
             probability that an item will be relevant given that it is retrieved." He
             derives the effectiveness measure E = 1 - 1/[a(1/P) + (1-a)(1/R)], sets
             a = 1/(b^2 + 1), and defines b as the P/R ratio at which dE/dR = dE/dP, for
             "a user who attaches b times as much importance to recall as precision." For
             a = 1/2 (b = 1), E reduces to the symmetric difference over the union,
             |A D B|/(|A|+|B|), whose complement is the harmonic mean 2PR/(P+R). Note: he
             defines E (effectiveness, to be minimized), not F. F = 1 - E and the name
             "F-measure" are later. Also: E -> 1-R as a->0 (precision dominates), E -> 1-P
             as a->1 (recall dominates).
Paraphrase:  Van Rijsbergen combines precision and recall into one number by taking a
             weighted harmonic combination of their reciprocals, tuned by a single
             importance parameter, and states his measure as the effectiveness E, with the
             equal-weight case equal to one minus the harmonic mean of P and R.
Locators:    Chapter 7, "Evaluation," subsections "Foundation," "The measurement of
             effectiveness"; Definition 6 and the E special cases (1)-(3).
Quote:       "the effectiveness of retrieval with respect to a user who attaches b times as
             much importance to recall as precision"
```

```text
URL:         https://aclanthology.org/M92-1002/
Kind:        primary. Nancy Chinchor, "MUC-4 Evaluation Metrics," Proc. Fourth Message
             Understanding Conference, 1992, pp. 22-29. This report owns the Fb notation and
             the evaluation-era "F-measure" name as adopted at MUC-4.
Establishes: The modern formula and naming. "we use van Rijsbergen's F-measure ... The
             formula ... is F = ((b^2 + 1) x P x R)/(b^2 x P + R) where P is precision, R
             is recall, and b is the relative importance given to recall over precision. If
             recall and precision are of equal weight, b = 1.0. For recall half as important
             as precision, b = 0.5. For recall twice as important as precision, b = 2.0." It
             reports three columns: "P&R" (b=1), "2P&R" (precision twice as important, i.e.
             b=0.5), and "P&2R" (recall twice as important, b=2).
Paraphrase:  MUC-4 adopted a single combined measure it called the F-measure, giving the
             Fb formula explicitly and using b to set how much more recall matters than
             precision, with b=1 the equal-weight case.
Locators:    Section "F-Measures," p. 24 (formula and b examples); references [1],[2] to
             van Rijsbergen 1979.
Quote:       "b is the relative importance given to recall over precision. If recall and
             precision are of equal weight, b = 1.0."
```

```text
URL:         https://people.cs.pitt.edu/~litman/courses/cs1671s20/F-measure-YS-26Oct07.pdf
Kind:        primary for its own algebra and the naming anecdote; secondary where it restates
             van Rijsbergen and Chinchor. Yutaka Sasaki, "The truth of the F-measure"
             (2007), an unpublished technical note (course-hosted copy).
Establishes: F1 = 2PR/(P+R) as the harmonic mean, and the general Fb = ((b^2+1)PR)/(b^2 P+R)
             (attributed to Chinchor 1992), with b>1 recall-oriented, b<1 precision-oriented,
             F0 = P. Derives E = 1 - Fb algebraically from van Rijsbergen's E with
             a = 1/(b^2+1). States "it seems that van Rijsbergen did not define the formula
             of the F-measure per se." Gives the finger-print intuition for why the harmonic
             mean is right: precision 1.0, recall 0.2 -> arithmetic mean 0.6, harmonic mean
             0.333, and the system is "almost useless," so 0.333 is the reasonable score.
             Reports (personal communication with David D. Lewis) that the name "F" at MUC-4
             "was accidentally selected by the consequence of regarding a different F
             function in van Rijsbergen's book as the definition."
Paraphrase:  Sasaki shows the F-measure is the harmonic mean of precision and recall,
             derives its equivalence to one minus van Rijsbergen's E, and records that its
             name was a historical accident.
Locators:    Sections 1 (Overview), 2 (Derivation), 3 (Further investigation in b), 4 (End
             Note); footnote 2 on the b = P/R vs R/P point.
Quote:       "the name was accidentally selected by the consequence of regarding a different
             F function in van Rijsbergen's book as the definition"
```

```text
URL:         https://arxiv.org/abs/2010.16061
Kind:        primary. David M. W. Powers, "Evaluation: from precision, recall and F-measure
             to ROC, informedness, markedness and correlation," J. Machine Learning
             Technologies 2(1):37-63, 2011 (this is the 2020 arXiv re-release). Powers owns
             the bias critique and the informedness/markedness measures.
Establishes: The named weaknesses. Recall, precision, and F-measure "are biased and should
             not be used without clear understanding of the biases." Their specific biases:
             "they ignore performance in correctly handling negative examples, they propagate
             the underlying marginal prevalences and biases, and they fail to take account
             the chance level performance." F1 "still completely ignores TN which can vary
             freely without affecting the statistic." F1 equals the Dice coefficient:
             F1 = TP/(TP + (FN+FP)/2). A blunt consequence: "a system that performs worse in
             the objective sense of Informedness, can appear to perform better under any of
             these commonly used measures."
Paraphrase:  Powers argues the precision/recall/F family is biased because it disregards
             true negatives and the base rate, so a genuinely worse system can score higher,
             and offers chance-corrected alternatives.
Locators:    Abstract; "The Binary Case" (Introduction); eqns (4)-(7) for the Dice/Jaccard
             identities and the TN-independence discussion.
Quote:       "it still completely ignores TN which can vary freely without affecting the
             statistic"
```

```text
URL:         https://doi.org/10.1186/s12864-019-6413-7
Kind:        primary. Davide Chicco and Giuseppe Jurman, "The advantages of the Matthews
             correlation coefficient (MCC) over F1 score and accuracy in binary
             classification evaluation," BMC Genomics 21:6 (2020). Open access. They own the
             six synthetic use cases and the colon-cancer experiment reported here. (The DOI
             page is the article's home; I read the full text from the DNB deposit copy of
             the same article at https://d-nb.info/1208103776/34, content identical.)
Establishes: The central "misled" case with data. Definitions: accuracy = (TP+TN)/(TP+TN+
             FP+FN); F1 = 2TP/(2TP+FP+FN) = 2 x precision x recall/(precision+recall);
             MCC = (TP.TN - FP.FN)/sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)), range [-1,+1]. Two
             properties separate F1 from MCC: "F1 is independent from TN, and it is not
             symmetric for class swapping." The six use cases (exact numbers in Numbers
             below) show accuracy and/or F1 reading high while the classifier fails one
             class; MCC is "the only score which correctly indicated the prediction problem
             in all six examples." The real colon-cancer table shows the ranking flip: the
             top classifier is gradient boosting under MCC but k-NN under both F1 and
             accuracy.
Paraphrase:  On imbalanced binary data, Chicco and Jurman demonstrate with exact confusion
             matrices that F1 and accuracy can look excellent while the classifier misses
             one class entirely, and that ranking real classifiers by F1 or accuracy picks a
             different winner than MCC does.
Locators:    "Notation and mathematical foundations" (eqns 1-3); "Use cases" A1,A2,B1,B2,
             C1,C2 and Table 4 recap; "Genomics scenario: colon cancer gene expression,"
             Table 5.
Quote:       "F1 is independent from TN, and it is not symmetric for class swapping"
```

```text
URL:         https://arxiv.org/abs/1911.03347
Kind:        primary. Juri Opitz and Sebastian Burst, "Macro F1 and Macro F1" (2019). They
             own the theorem and the worked ranking-flip tables.
Establishes: Two different formulas both called "macro F1." Averaged F1 (arithmetic mean of
             per-class F1, the scikit-learn "macro" default): F1 = (1/n) sum_x 2P_x R_x/
             (P_x+R_x). F1-of-averages (harmonic mean of macro-precision and macro-recall):
             = 2 P-bar R-bar/(P-bar + R-bar). Theorem: F1-of-averages >= averaged-F1 always,
             the gap can reach 0.5, and the two "can also lead to different classifier
             rankings." Worked flip (Numbers below): two confusion matrices where
             F1-of-averages prefers the second while averaged-F1 prefers the first. They
             note real shared tasks (SemEval-2015 Task 10) use the benevolent
             F1-of-averages, and recommend averaged-F1 as more robust.
Paraphrase:  Opitz and Burst prove that the two computations circulating under the name
             "macro F1" can disagree by up to 0.5 and can reverse which classifier ranks
             higher, and recommend the arithmetic mean of per-class F1.
Locators:    Sections 1-3; Theorem and Lemma (p. 2); Tables 1-2 (ranking flip); Discussion.
Quote:       "The two computations may not only diverge in their scalar result but can also
             lead to different classifier rankings."
```

```text
URL:         https://arxiv.org/abs/1402.1892
Kind:        primary. Zachary C. Lipton, Charles Elkan, Balakrishnan Naryanaswamy,
             "Thresholding Classifiers to Maximize F1 Score" (2014). They own the
             optimal-threshold theorem and the all-positive result.
Establishes: F1's base-rate and threshold dependence. For a classifier with well-calibrated
             probability outputs, "the optimal threshold is half the optimal F1 score." For
             a completely uninformative classifier, "the optimal behavior is to classify all
             examples as positive," which, given that positives are usually rare, "can be
             considered undesirable." Because the F1-optimal threshold depends on the base
             rate, F1 scores are hard to compare across systems or datasets with different
             prevalence. In the multilabel case, when features for rare labels are lost,
             maximizing macro F1 pushes the model to predict those rare labels frequently.
Paraphrase:  Lipton and colleagues show F1's optimal operating point is tied to the base
             rate, so a classifier that knows nothing maximizes F1 by calling everything
             positive, and F1 comparisons across differing base rates are unreliable.
Locators:    Abstract; Sections 1-2; the Medline case study predicting 26,853 labels.
Quote:       "if the classifier is completely uninformative, then the optimal behavior is to
             classify all examples as positive"
```

```text
URL:         https://scikit-learn.org/stable/modules/model_evaluation.html
Kind:        secondary. scikit-learn software documentation. Not the originator of these
             definitions, but the authoritative reference for how they are computed in the
             library most practitioners use, and it states the definitions precisely.
Establishes: The three averaging schemes for multi-class F1. "micro" sums the per-class
             dividends and divisors (total TP, FP, FN across labels) then takes one quotient;
             "If all labels are included, 'micro'-averaging in a multiclass setting will
             produce precision, recall and F that are all identical to accuracy." "macro"
             "calculates the mean of the binary metrics, giving equal weight to each class,"
             so it "will over-emphasize the typically low performance on an infrequent
             class." "weighted" averages the per-class metrics weighted by each class's
             support (its count in the true data), and "may produce an F-score that is not
             between precision and recall." "samples" applies only to multilabel problems.
Paraphrase:  scikit-learn documents micro F1 as a global pooled count (equal to accuracy
             when all labels are scored), macro F1 as the unweighted mean over classes, and
             weighted F1 as the support-weighted mean.
Locators:    "Precision, recall and F-measures" -> "From binary to multiclass and
             multilabel," the averaging table and its bullet notes.
Quote:       "'micro'-averaging in a multiclass setting will produce precision, recall and F
             that are all identical to accuracy"
```

## Contradictions

- The two macro-F1 definitions disagree (Opitz & Burst). "Macro F1" is not one number.
  The scikit-learn default (arithmetic mean of per-class F1) and the "harmonic mean of
  averaged precision and averaged recall" used by some SemEval tasks can rank two systems
  in opposite order. Any "macro F1" claim needs to say which formula.

- b direction, a real notational conflict between primaries. Van Rijsbergen's Chapter 7
  states the equal-gradient point at "P/R = b." Sasaki reproduces it as "b = R/P" and adds
  in a footnote: "In van Rijsbergen's book, b = P/R but I believe this is a typing error."
  The substance is not in dispute across van Rijsbergen, Chinchor, and Sasaki: b>1 weights
  recall more than precision (Chinchor: "recall twice as important as precision, b = 2.0").
  Only the crossover-ratio wording differs. The writer should use the agreed meaning and
  not reproduce the P/R-versus-R/P slip.

- The steelman for F1: ignoring true negatives is the point, not a defect, in the setting
  F1 was built for. Van Rijsbergen designed the measure for document retrieval, where the
  non-relevant, non-retrieved documents (the true negatives) are an unbounded and
  uninformative mass. Accuracy is useless there, since labeling everything negative scores
  near 1.0; Chicco makes the same point with the trivial majority classifier, whose
  accuracy equals the majority fraction. In needle-in-a-haystack detection and retrieval,
  a measure that ignores TN is appropriate. Powers frames the same fact as a bias; whether
  it is a feature or a bias depends on whether the negatives carry information. This is the
  honest counterweight to the "F1 misleads" case: it misleads when TN matters and is not
  reflected, and it is the right tool when TN does not matter.

- MCC is not a free lunch. Chicco & Jurman concede MCC "cannot be defined or it displays
  large fluctuations" in extreme cases (a whole row or column of the confusion matrix is
  zero), and they resolve the undefined 0/0 cases only "through a simple approximation via
  a calculus technique" (setting MCC = 0). The article should present MCC as a better
  default under imbalance, not as flawless.

- Chicco's own labeling has an internal slip. Use case A1 is a 91%-positive dataset,
  correctly called "positively imbalanced" in the section heading, Fig. 2, and Table 4, but
  the Recap paragraph once calls A1 "negatively imbalanced." Use the confusion-matrix
  numbers, not the prose label. Likewise the A1 MCC prints as -0.03 in the text and Table 4
  but -0.04 in the Fig. 1 caption; the value from the formula is -0.0316, so -0.03 is the
  honest reading.

## Numbers

```text
Figure: precision = TP/(TP+FP)
Owner:  van Rijsbergen 1979 (as conditional probability); confusion-matrix form in
        Chicco & Jurman 2020, Table 2.
Scope:  fraction of predicted-positive items that are correct.
```

```text
Figure: recall = TP/(TP+FN)
Owner:  van Rijsbergen 1979; Chicco & Jurman 2020, Table 2.
Scope:  fraction of actual-positive items the system found.
```

```text
Figure: F1 = 2PR/(P+R) = 2TP/(2TP+FP+FN)
Owner:  harmonic-mean form, Sasaki 2007; confusion-matrix form, Chicco & Jurman 2020,
        eqn (3). Recomputed and confirmed against use case A1: 2*90/(180+9+1) = 0.947.
Scope:  binary F1 for the class labeled positive; independent of TN.
```

```text
Figure: Fb = ((b^2+1) P R)/(b^2 P + R); F0 = P; b>1 recall-weighted, b<1 precision-weighted
Owner:  Chinchor 1992 (MUC-4), formula and b examples; Sasaki 2007 for F0=P and orientation.
Scope:  b is recall's importance relative to precision; b=1 gives F1.
```

```text
Figure: E = 1 - 1/[a(1/P) + (1-a)(1/R)], a = 1/(b^2+1); F = 1 - E
Owner:  van Rijsbergen 1979, Chapter 7; the F = 1-E identity derived in Sasaki 2007.
Scope:  effectiveness measure; equal-weight case a=1/2 gives F = 2PR/(P+R).
```

```text
Figure: MCC = (TP.TN - FP.FN)/sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)), range [-1,+1]
Owner:  Chicco & Jurman 2020, eqn (2). Recomputed and confirmed for A1: -9/sqrt(81081)
        = -0.0316.
Scope:  a Pearson correlation between actual and predicted labels; 0 = coin toss.
```

```text
Figure: Chicco use cases, exact confusion matrices and metrics (all recomputed, confirmed):
        A1  pos91/neg9   TP90 FN1  TN0  FP9   -> accuracy 0.90, F1 0.95, MCC -0.03
        A2  pos75/neg25  TP5  FN70 TN19 FP6   -> accuracy 0.24, F1 0.12, MCC -0.24
        B1  pos50/neg50  TP47 FN3  TN5  FP45  -> accuracy 0.52, F1 0.66, MCC +0.07
        B2  pos50/neg50  TP10 FN40 TN46 FP4   -> accuracy 0.56, F1 0.31, MCC +0.17
        C1  pos10/neg90  TP9  FN1  TN1  FP89  -> accuracy 0.10, F1 0.17, MCC -0.19
        C2  pos11/neg89  TP2  FN9  TN88 FP1   -> accuracy 0.90, F1 0.29, MCC +0.31
Owner:  Chicco & Jurman 2020, Table 4.
Scope:  synthetic binary classifiers. A1 is the showcase: F1=0.95 and accuracy=0.90 look
        excellent while the model gets 0 of 9 true negatives; MCC -0.03 flags it. B1 is the
        cleanest F1-specific failure: F1=0.66 looks fair, but the model gets 5 of 50
        negatives; MCC +0.07 and accuracy 0.52 both flag it, F1 does not.
```

```text
Figure: colon-cancer ranking flip (real data: 62 patients, 22 healthy / 40 cancer):
        Gradient boosting: MCC +0.55, F1 0.81, accuracy 0.78, TP rate 0.85, TN rate 0.69
        k-nearest neighbors: MCC +0.48, F1 0.87, accuracy 0.81, TP rate 0.92, TN rate 0.52
        Radial-kernel SVM:  MCC +0.29, F1 0.75, accuracy 0.67, TP rate 0.86, TN rate 0.40
Owner:  Chicco & Jurman 2020, Table 5 (averages over ten runs).
Scope:  Top classifier is gradient boosting by MCC, k-NN by F1 and by accuracy. k-NN's
        edge comes from recall (TP rate 0.92) while its specificity (TN rate 0.52) is weak;
        F1 and accuracy rank it first anyway. This is the article's real ranking flip, but
        it turns on metric choice (F1/accuracy vs MCC), not micro-vs-macro averaging.
```

```text
Figure: macro-F1 ranking flip (Opitz & Burst, Tables 1-2; per-class values recomputed):
        Matrix 1 = [[5,10],[5,10]]: F1-of-averages 0.50, averaged-F1 0.49
        Matrix 2 = [[1,1],[9,19]]:  F1-of-averages 0.55, averaged-F1 0.48
Owner:  Opitz & Burst 2019, Tables 1-2.
Scope:  Going from matrix 1 to matrix 2, F1-of-averages rises (0.50 -> 0.55, "better")
        while averaged-F1 falls (0.49 -> 0.48, "worse"). Which "macro F1" you pick reverses
        the verdict. (The paper's overbar notation was lost in text extraction; I identified
        which value is which via the theorem F1-of-averages >= averaged-F1 and by direct
        computation of the per-class P, R, F1.)
```

```text
Figure: F1-optimal threshold = half the optimal F1 score (for calibrated probabilities);
        uninformative classifier -> label all positive to maximize F1
Owner:  Lipton, Elkan & Naryanaswamy 2014, Abstract and Sections 1-2.
Scope:  binary and multilabel. Shows F1's operating point depends on the base rate, so F1
        is not comparable across datasets of different prevalence.
```

```text
Figure: harmonic mean punishes a lopsided pair (worked): precision 1.0, recall 0.2
        -> arithmetic mean 0.60, harmonic mean 0.333
Owner:  Sasaki 2007, Section 1.
Scope:  the finger-print-recognition intuition for why F1 uses the harmonic, not the
        arithmetic, mean. Confirmed: 2*1*0.2/(1.2) = 0.333.
```

```text
Figure: historical origin of the harmonic-mean-of-P-and-R measure
Owner:  reported in Chicco & Jurman 2020, Background (a repetition, not first-hand): the
        harmonic mean was introduced in statistical ecology by Dice (1948) and Sorensen
        (1948), rediscovered by van Rijsbergen in the 1970s, and given the "F1" notation at
        MUC-4 in 1992. Treat as a claim made, corroborated for the 1992 step by Chinchor
        1992 and Sasaki 2007. The Dice and Sorensen papers themselves were not read.
Scope:  provenance only.
```

## Source assets

```text
Asset: Chicco & Jurman 2020, Figure 2 (use case A1). A bar chart of accuracy 0.90, F1 0.95,
       and normalized MCC 0.48 side by side, with two pie charts: the confusion split
       (TP90/FN1/TN0/FP9) and the class balance (91 positive / 9 negative).
Shows: the whole "misled" argument in one image, that two tall bars (F1, accuracy) sit
       next to a middling MCC bar for a classifier that found 0 of 9 negatives.
Crop:  keep all three metric bars together; the point is the contrast between them. If the
       pies are dropped, the confusion numbers must be restated in the caption or nearby
       prose, or the tall bars lose their meaning.
```

```text
Asset: Chicco & Jurman 2020, Table 5 (colon-cancer rankings). The same five classifiers
       listed three times, reordered by MCC, then F1, then accuracy, with TP-rate and
       TN-rate columns.
Shows: that the top row changes with the metric, gradient boosting under MCC versus k-NN
       under F1 and accuracy, and that k-NN's weak TN rate (0.52) is what MCC penalizes.
Crop:  a crop must retain the classifier names, the metric being sorted on, and the TP/TN
       rate columns; without the TN-rate column the flip looks arbitrary.
```

```text
Asset: Opitz & Burst 2019, Tables 1-2 (the two 2x2 confusion matrices with their two macro
       F1 values). Compact, two small tables.
Shows: the minimal example where the two macro-F1 formulas reverse the ranking.
Crop:  keep both tables together with both F1 values under each; either table alone shows
       nothing.
```

```text
Asset: van Rijsbergen 1979, the E special-case list and the equal-effectiveness contour
       diagram (Figure 7.13) in Chapter 7.
Shows: geometrically why the combined measure is convex toward the origin and why a
       lopsided (P,R) pair scores worse than a balanced one of the same sum.
Crop:  low priority; the figure is dated and abstract. The worked harmonic-vs-arithmetic
       contrast from Sasaki carries the same idea more concretely for a general reader.
```

```text
Asset: F1 formula and confusion matrix, general. Best rendered fresh by the writer as a
       labeled 2x2 confusion matrix (TP/FN/FP/TN) with precision reading down the predicted-
       positive column and recall reading across the actual-positive row.
Shows: where precision, recall, and F1 come from, and visually that TN sits in the one cell
       F1 never touches.
Crop:  n/a; this is an authored diagram, not a source crop. Flagged because it is the single
       most useful visual for the lesson and no source figure does it cleanly.
```

## Discarded

```text
URL: https://dl.acm.org/doi/pdf/10.1145/312624.312647
     Yang & Liu 1999, the canonical micro/macro text-categorization primary. ACM returned a
     challenge page, not the PDF; gated, not read. Not cited, because I did not open it. Its
     micro/macro definitions are covered by scikit-learn (read) and Opitz & Burst (read).
     Owner of access: ACM Digital Library.
```

```text
URL: https://shmueli.medium.com/a-tale-of-two-macro-f1s-8811ddcf8f04
     A Medium blog restating Opitz & Burst. Rejected: blog post, and the commission requires
     the measurement's own literature. The primary (Opitz & Burst) is cited instead.
```

```text
URL: https://link.springer.com/article/10.1186/s12864-019-6413-7
     The Springer/BMC landing page for Chicco & Jurman. Not discarded as a source, only as a
     fetch route: WebFetch hit the cookie-authorization redirect (gated transport). The DOI
     address is recorded as the source's home; the identical full text was read from the DNB
     deposit copy.
```

```text
URL: https://www.researchgate.net/publication/338351315 and other ResearchGate mirrors
     Mirror copies of papers already read from primary hosts (Chicco, Powers, Sasaki, Yang &
     Liu). Not used; the primary or author-hosted address is recorded instead.
```

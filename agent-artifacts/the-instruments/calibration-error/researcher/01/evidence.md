# Evidence: the-instruments/calibration-error (01)

The evidence supports every part of the commissioned lesson. The definition of
calibration, the binned ECE estimator, and the reliability diagram are all read
from primaries in their own terms, with two slightly different formulations of
ECE (Naeini et al. 2015 and Guo et al. 2017) recorded so the writer knows which
one the field means when it writes "ECE." The overconfidence finding, the
depth/width/batchnorm/weight-decay effects, and temperature scaling as the fix
come from Guo et al. 2017 with exact figures. The binning pitfalls are read from
two primaries: Kumar et al. 2019 proves binned ECE lower-bounds the true error
and shows a 15-bin ImageNet estimate understating it by at least half; Nixon et
al. 2019 shows equal-width bins concentrate the estimate in one or two bins and
constructs a predictor with 0 ECE that is badly miscalibrated. The proper-scoring
alternative is read from Brier 1950 itself, including the exact property that it
cannot be improved by hedging. The misled case is read from the GPT-4 technical
report: pre-trained ECE 0.007, post-trained (PPO/RLHF) ECE 0.074.

Where it is thin: (1) the two worked examples in the Numbers section are
constructed by me to illustrate Guo's Equation 3, not drawn from any source's
data, and are labeled as such; their arithmetic is shown so either reader can
recheck it. (2) The GPT-4 report does not state its bin count or binning scheme
for the 0.007/0.074 figures, so those absolute numbers carry the same
bin-dependence caveat every ECE does. (3) DeGroot & Fienberg 1983, the origin of
reliability diagrams and the calibration-versus-refinement idea, is gated; I
could not read its full text and do not cite it firsthand, so the accuracy-blind
point is grounded through Guo's definition, Nixon's construction, and Brier's
constant-forecast baseline instead.

The evidence does not undermine the commissioned angle. It does force one
distinction the writer must keep, recorded under Contradictions: "ECE can be
gamed by binning" and "RLHF degraded GPT-4's calibration" are two different
pitfalls, and the GPT-4 numbers are an honest self-report of degradation, not an
example of binning manipulation.

## Sources

```text
URL:         https://ojs.aaai.org/index.php/AAAI/article/view/9602
Kind:        primary. It is the paper that defines Expected Calibration Error and
             Maximum Calibration Error under those names; it owns the estimator.
Establishes: The origin definitions of ECE and MCE. Predictions are sorted and
             partitioned into K fixed bins (K = 10 in their experiments). ECE is
             a weighted average over bins of |o_i - e_i|; MCE is the maximum of
             |o_i - e_i| over bins. Lower is better; 0 is perfect.
Paraphrase:  "These measures are called Expected Calibration Error (ECE), and
             Maximum Calibration Error (MCE). In computing these measures, the
             predictions are sorted and partitioned into K fixed number of bins
             (K = 10 in our experiments)." ECE = sum over i of P(i)*|o_i - e_i|;
             MCE = max over i of |o_i - e_i|, where o_i is the true fraction of
             positive instances in bin i, e_i is the mean predicted probability
             for the instances in bin i, and P(i) is the fraction of all
             instances that fall in bin i.
Locators:    Section "Calibration Measures", the displayed ECE/MCE equation and
             the sentence defining o_i, e_i, P(i). Naeini, Cooper, Hauskrecht,
             AAAI 2015, pp. 2901-2907.
Quote:       "where o_i is the true fraction of positive instances in bin i, e_i
             is the mean of the post-calibrated probabilities for the instances
             in bin i, and P(i) is the empirical probability (fraction) of all
             instances that fall into bin i."
```

```text
URL:         https://proceedings.mlr.press/v70/guo17a.html
Kind:        primary. Owns the ECE popularization for deep networks, the
             overconfidence finding, and temperature scaling with its results.
Establishes: (1) Perfect calibration, Eq. 1: P(Y-hat = Y | P-hat = p) = p for all
             p in [0,1]. (2) Reliability diagrams plot expected sample accuracy as
             a function of confidence; a perfectly calibrated model plots the
             identity (diagonal); any deviation is miscalibration; the diagrams do
             not show how many samples fall in each bin. (3) The binned estimator,
             Eq. 3: ECE = sum_{m=1}^{M} (|B_m|/n) * |acc(B_m) - conf(B_m)|, with
             acc(B_m) the fraction correct in bin m, conf(B_m) the mean confidence
             in bin m, bins being M equal-width intervals of size 1/M, and the
             predicted-class (top-label) probability used as the confidence.
             (4) MCE, Eq. 5: max_m |acc(B_m) - conf(B_m)|. (5) NLL, Eq. 6.
             (6) Modern networks are overconfident: a 110-layer ResNet on
             CIFAR-100 has far higher confidence than accuracy, while a 5-layer
             LeNet is well-calibrated. (7) Depth, width, and Batch Normalization
             worsen ECE; more weight decay improves calibration even past the
             point of best accuracy (Figure 2). (8) Temperature scaling, Eq. 9:
             q-hat_i = max_k softmax(z_i / T)_k, with T > 0 a single scalar
             learned by minimizing validation NLL; it does not change the
             argmax, so it does not change accuracy. It was the most effective
             method on the vision datasets tested.
Paraphrase:  ECE with M = 15 bins on standard vision/NLP datasets is typically
             between 4% and 10% before calibration. Temperature scaling reduces
             it sharply: on CIFAR-100 ResNet-110 from 16.53% to 1.26%, on
             ImageNet DenseNet-161 from 6.28% to 1.99%, on ImageNet ResNet-152
             from 5.48% to 1.86% (Table 1). During training, after the model fits
             the training set, NLL can still be reduced by raising confidence, so
             the network becomes overconfident; on CIFAR-100 test error drops
             from 29% to 27% in the region where NLL overfits.
Locators:    Section 2 (Definitions), Eqs. 1, 3, 5, 6; Figures 1, 2, 4; Table 1;
             Section 4.2 (temperature scaling, Eq. 9); Section 3 (Observing
             Miscalibration). Guo, Pleiss, Sun, Weinberger, ICML 2017 (PMLR 70).
Quote:       "we define perfect calibration as P(Y-hat = Y | P-hat = p) = p,
             for all p in [0,1]." And: "temperature scaling does not affect the
             model's accuracy."
```

```text
URL:         https://proceedings.neurips.cc/paper/2019/hash/f8c0c968632845cd133308b1a494967f-Abstract.html
Kind:        primary. Proves the statistical bias of the binned ECE estimator and
             demonstrates it empirically; owns that result.
Establishes: (1) The calibration error of a model that outputs a continuous range
             of probabilities cannot be measured with finitely many bins.
             (2) Proposition 3.3 (Binning underestimates error): for any binning
             scheme and model, CE(binned f) <= CE(f). Binning averages predictions
             within a bin, letting errors at different parts of the bin cancel,
             which lowers the measured error. (3) Example 3.2: there exists a
             distribution and a continuous model where the binned calibration
             error is 0 while the true calibration error is at least 0.49.
             (4) A finer set of bins gives a tighter lower bound, so measured ECE
             rises with bin count (Figure 2, ImageNet and CIFAR-10).
Paraphrase:  On ImageNet with a Platt-scaled VGG16, measured calibration error
             rises with the number of bins; with 15 bins (as in Guo et al.) one
             would read the error as about 0.02 "when in reality the calibration
             error is at least twice as high." The result holds for the L1
             calibration error (the standard ECE) and for equal-mass binning.
Locators:    Section 3 (Is Platt scaling calibrated?), Definition 3.1, Example
             3.2, Proposition 3.3, Section 3.1 and Figure 2. Kumar, Liang, Ma,
             NeurIPS 2019.
Quote:       "if we use 15 bins as in [9], we would think the calibration error
             is around 0.02 when in reality the calibration error is at least
             twice as high."
```

```text
URL:         https://arxiv.org/abs/1904.01685
Kind:        primary. Owns the catalogue of ECE's binning pathologies and the
             adaptive-binning fix.
Establishes: (1) Equal-width bins are a poor fit because confident-network
             predictions cluster near 1, so with the usual 10-20 bins only one or
             two bins carry most of the ECE. (2) Bin count is a bias-variance
             tradeoff: more bins lower bias but leave bins sparsely populated and
             raise variance. (3) Section 3.4 constructs a case that is 1.0 AUC,
             0 ECE, and yet uncalibrated, because opposite errors overlap inside a
             single static bin. (4) Adaptive Calibration Error (ACE) spaces bin
             edges so each bin holds an equal number of predictions, concentrating
             the estimate where predictions actually are. (5) ECE uses only the
             top predicted class's probability, so it ignores the other K-1 class
             probabilities and conflates calibration with sharpness.
Paraphrase:  The choice of binning changes both the number and, in the multiclass
             case with label noise, the rank ordering of recalibration methods;
             adaptive binning is more stable. ECE was designed to mirror
             binary reliability diagrams and is "reductive in a multi-class
             setting."
Locators:    Section 2.1 (the ECE formula and its equal-width, top-label
             implementation), Sections 3.2, 3.3, 3.4; Section 4.2 (ACE). Nixon,
             Dusenberry, Zhang, Jerfel, Tran, CVPR Workshops 2019.
Quote:       "we could simply output a prediction in the range of (0.41, 0.43)
             for the negative examples and (0.47, 0.49) for the positive examples
             to create a set of predictions that has 1.0 AUC, 0 ECE and yet be
             uncalibrated."
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. The GPT-4 technical report is OpenAI's own account of its
             model; it owns the calibration result.
Establishes: The pre-trained GPT-4 model is highly calibrated on a subset of
             MMLU; post-training reduces calibration. The confidence measured is
             the model's probability (logprob) across the A/B/C/D answer choices,
             binned against per-bin accuracy. The reported figures are ECE 0.007
             for the pre-trained model and ECE 0.074 for the post-trained (PPO)
             model, a roughly tenfold increase.
Paraphrase:  "the pre-trained model is highly calibrated (its predicted
             confidence in an answer generally matches the probability of being
             correct). However, after the post-training process, the calibration
             is reduced (Figure 8)." The calibration-curve figures label the
             pre-train model "ECE: 0.007" and the PPO model "ECE: 0.074". Figure 8
             is described as: x-axis bins by the model's confidence in each
             choice, y-axis accuracy within each bin, dotted diagonal is perfect
             calibration; "post-training hurts calibration significantly."
Locators:    Section 3 (Capabilities), the paragraph beginning "GPT-4 can also be
             confidently wrong"; Figure 8 and its caption; the calibration-curve
             figures reporting ECE 0.007 and 0.074. OpenAI, GPT-4 Technical
             Report, arXiv:2303.08774.
Quote:       "the pre-trained model is highly calibrated ... However, after the
             post-training process, the calibration is reduced."
```

```text
URL:         https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml
Kind:        primary. Brier's own paper; it owns the score and the proper-scoring
             property. (The journal page is gated: an automated request returns
             403, and the PDF downloads. This is the address where the source
             lives; DOI 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2.)
Establishes: (1) The verification score, Eq. 2: P = (1/n) * sum_{i=1}^{n}
             sum_{j=1}^{r} (f_ij - E_ij)^2, where f_ij is the forecast probability
             for class j on occasion i and E_ij is 1 if the event occurred in
             class j, else 0. Minimum 0 (perfect), maximum 2 (worst), summing over
             both classes. (2) The proper-scoring property: the scheme "cannot
             influence the forecaster in any undesirable way"; a forecaster
             minimizes P by getting forecasts right and stating honest
             probabilities, and gains nothing by hedging with extreme 0/1
             statements he cannot justify. (3) The no-skill constant baseline,
             Eq. 4: forecasting the base rates on every occasion gives mean score
             P-bar = 1 - sum_j p_j^2.
Paraphrase:  A worked rain/no-rain example of 10 forecasts scores P = 0.19. A
             constant 0.3-probability-of-rain forecast on every occasion (the
             actual rain frequency was 3 of 10) scores P' = 1 - (0.3^2 + 0.7^2)
             = 0.42; a constant climatological 0.2 forecast scores 0.44. So a
             constant predictor that matches the base rate is scored, and it is
             scored worse than a skilled forecaster, even though such a constant
             predictor is by construction calibrated.
Locators:    Section "Verification Formula", Eq. 2, Table 1 (P = 0.19), Eqs. 3-4
             and the P' = 0.42 / 0.44 computations. Brier, Monthly Weather Review
             78(1):1-3, 1950.
Quote:       "one essential criterion for satisfactory verification is that the
             verification scheme should influence the forecaster in no undesirable
             way." And: "he is fooling nobody but himself if he thinks he can beat
             the verification system by putting down only zeros and unities."
```

```text
URL:         https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf
Kind:        primary. The empirical study Guo et al. cite for the historical
             baseline; it owns the 2005 finding. (Author-hosted PDF; canonical
             record is ICML 2005, ACM DOI 10.1145/1102351.1102430.)
Establishes: Among the supervised learners of that era, neural nets and bagged
             decision trees "have little or no bias and predict well-calibrated
             probabilities" without any post-hoc correction. This is the baseline
             Guo et al. 2017 contrast against when they report that modern (deep)
             networks are no longer well-calibrated.
Paraphrase:  The study evaluates the probabilities from seven learning methods on
             classification problems and finds neural nets among the best-
             calibrated before any calibration step; boosting and SVMs are
             distorted (sigmoid-shaped) and benefit most from Platt scaling or
             isotonic regression.
Locators:    Abstract and Introduction (the well-calibrated-neural-nets finding);
             Section 2 (calibration methods). Niculescu-Mizil & Caruana, ICML
             2005, pp. 625-632.
Quote:       "bagged trees and neural nets ... have little or no bias and predict
             well-calibrated probabilities."
```

```text
URL:         https://arxiv.org/abs/2308.01222
Kind:        secondary. A survey that reports on and organizes others' calibration
             work rather than owning any of the results; it reports the ECE, MCE,
             and Brier definitions and the binning-bias critique from outside the
             authoring parties.
Establishes: Context and the state of the debate. It restates ECE (crediting
             Naeini et al. 2015) and MCE, gives the modern binary Brier Score
             BS = (1/N) sum (f_i - y_i)^2 crediting Brier 1950, and calls Brier
             "a proper scoring rule that measures both discrimination and
             calibration." It records that binning introduces bias in ECE,
             crediting Nixon et al. 2019, and lists proposed fixes (Adaptive ECE,
             Smooth ECE).
Paraphrase:  Exact calibration measurement with finite samples is impossible
             because confidence is continuous; ECE and its relatives are
             approximations. The survey groups binning bias with other sources of
             mis-measurement and frames the field as both relying on ECE and
             correcting for its known biases.
Locators:    Section 2.2.4 (Bias in Evaluation Metrics); Section 3.1 (ECE, Eqs.
             3-4), 3.2 (MCE, Eq. 5), 3.3 (Brier Score, Eq. 6). Wang, "Calibration
             in Deep Learning: A Survey of the State-of-the-Art," 2023.
Quote:       "The Brier Score (Brier et al., 1950) is a proper scoring rule that
             measures both discrimination and calibration of probabilistic
             predictions."
```

## Contradictions

- **Two different formulas both called "ECE."** Naeini et al. 2015 define ECE for
  a binary/positive-class setting: o_i is the true fraction of positives in bin
  i and e_i is the mean predicted probability, with K = 10 bins. Guo et al. 2017
  define it for multiclass top-label calibration: acc(B_m) is the fraction
  correct and conf(B_m) is the mean of the predicted-class probability, with
  M = 15 bins. They coincide in the binary top-label case but are stated
  differently. The writer should teach Guo's acc/conf form (it is the one meant
  in deep-learning usage) and attribute the metric's origin to Naeini et al.

- **Two different Brier scores, differing by a factor of two.** Brier's 1950
  formula sums the squared error over both outcome classes, so its range is 0 to
  2 and his constant-forecast baseline is 0.42. The modern machine-learning
  "Brier score" for binary problems (survey Eq. 6) is the mean squared error of
  the positive-class probability alone, range 0 to 1. The same constant 0.3
  predictor scores 0.42 under Brier's original and 0.21 under the modern binary
  form. State which convention any number uses.

- **The field both relies on ECE and rejects it as sufficient.** Guo et al. 2017
  use ECE as their "primary empirical metric." Nixon et al. 2019 say ECE has
  "numerous pathologies," and Kumar et al. 2019 show the binned estimator cannot
  measure the true error and only lower-bounds it. This is the live debate the
  brief asks for: ECE is standard and is also known to be biased and
  bin-dependent. Steelman both: ECE is a cheap, interpretable scalar tied
  directly to the reliability diagram; its critics do not abandon calibration,
  they propose better estimators (adaptive binning, proper scoring rules).

- **The GPT-4 case is degradation, not binning manipulation. Keep them apart.**
  The commission's "a headline calibration number can be gamed by binning" is a
  claim about the ECE metric (Kumar/Nixon). The GPT-4 result (0.007 -> 0.074) is
  a substantive finding that RLHF made the model overconfident, reported honestly
  by OpenAI using its own binning. Presenting the GPT-4 numbers as an example of
  binning gaming would misread the source. They are two distinct lessons: the
  metric can hide error, and, separately, post-training really does degrade a
  well-calibrated base model.

- **What "confidence" means in the GPT-4 figure.** The GPT-4 report measures the
  probability the model assigns across A/B/C/D choices (logprobs), not a
  confidence the chatbot types in words. The commission already routes verbalized
  confidence to the-mechanics/false-confidence; the writer should not let the
  GPT-4 numbers stand in for a claim about typed confidence.

## Numbers

```text
Figure: ECE = sum_{m=1}^{M} (|B_m|/n) * |acc(B_m) - conf(B_m)|
Owner:  Guo et al. 2017, Eq. 3 (estimator popularized from Naeini et al. 2015)
Scope:  M equal-width bins of width 1/M over confidence in [0,1]; n = total
        samples; confidence is the predicted (top) class probability.
```

```text
Figure: ECE origin form: sum_i P(i)*|o_i - e_i|; MCE = max_i |o_i - e_i|
Owner:  Naeini, Cooper, Hauskrecht 2015
Scope:  K = 10 fixed bins; o_i true positive fraction in bin i; e_i mean
        predicted probability in bin i; P(i) share of instances in bin i.
```

```text
Figure: Pre-training ECE 0.007; post-training (PPO/RLHF) ECE 0.074
Owner:  OpenAI, GPT-4 Technical Report, Figure 8 / calibration curves
Scope:  A subset of MMLU; confidence = model probability over A/B/C/D choices;
        bin count/scheme not stated in the report.
```

```text
Figure: Uncalibrated ECE typically 4%-10%; temperature scaling reduces it to
        roughly 1%-2% on vision datasets. Examples: CIFAR-100 ResNet-110
        16.53% -> 1.26%; ImageNet DenseNet-161 6.28% -> 1.99%; ImageNet
        ResNet-152 5.48% -> 1.86%; CIFAR-100 ResNet-110(SD) 12.67% -> 0.96%.
Owner:  Guo et al. 2017, Table 1 and Figure 4
Scope:  M = 15 bins; ECE reported as a percentage; test sets of each dataset.
```

```text
Figure: With 15 bins the ImageNet estimate reads ~0.02 while the true error is
        at least twice as high; measured ECE rises monotonically with bin count.
Owner:  Kumar, Liang, Ma 2019, Section 3.1 and Figure 2
Scope:  Platt-scaled VGG16 on ImageNet; equal-mass bins; 90% bootstrap CIs.
```

```text
Figure: Brier verification score P: min 0 (perfect), max 2 (worst); worked
        rain/no-rain example P = 0.19; constant base-rate 0.3 forecast P' = 0.42;
        constant climatological 0.2 forecast 0.44. No-skill baseline
        P-bar = 1 - sum_j p_j^2.
Owner:  Brier 1950, Eqs. 2-4 and Table 1
Scope:  r = 2 classes (rain, no-rain); n = 10 forecasts in the worked example;
        sum over both classes.
```

### Worked example A (illustrative, built by me from Guo Eq. 3 to teach the mechanic)

Not from any source's data. An overconfident classifier over n = 100 predictions,
M = 5 equal-width bins. Every bin has confidence above accuracy, the pattern Guo
reports for a deep network.

```text
Interval      | count |B_m| | conf(B_m) | acc(B_m) | gap |acc-conf| | (|B_m|/n)*gap
(0.0, 0.2]    |   5         |   0.10    |   0.00   |   0.10        |   0.005
(0.2, 0.4]    |  10         |   0.30    |   0.20   |   0.10        |   0.010
(0.4, 0.6]    |  15         |   0.50    |   0.40   |   0.10        |   0.015
(0.6, 0.8]    |  30         |   0.70    |   0.60   |   0.10        |   0.030
(0.8, 1.0]    |  40         |   0.95    |   0.80   |   0.15        |   0.060
```

Weights sum to (5+10+15+30+40)/100 = 1. ECE = 0.005 + 0.010 + 0.015 + 0.030 +
0.060 = 0.120 = 12.0%. MCE = max gap = 0.15 (the top bin).

### Worked example B (illustrative, built by me to show coarse binning hiding error)

Not from any source's data; it demonstrates the Kumar Prop. 3.3 / Nixon 3.4
cancellation mechanism with round numbers. Two groups of 50 predictions each.

```text
Fine bins (split at 0.6):
  (0.5, 0.6]  50 preds  conf 0.55  acc 0.75  gap 0.20   (underconfident)
  (0.6, 0.7]  50 preds  conf 0.65  acc 0.45  gap 0.20   (overconfident)
  ECE = 0.5*0.20 + 0.5*0.20 = 0.20 = 20%

One coarse bin (0.5, 1.0], merging both groups:
  conf = (0.55 + 0.65)/2 = 0.60 ; acc = (0.75 + 0.45)/2 = 0.60 ; gap = 0.00
  ECE = 0%
```

Same predictions, same outcomes: fine bins report 20% error, one coarse bin
reports 0%, because the under- and over-confident groups cancel inside the merged
bin. This is Kumar's Example 3.2 and Nixon's Section 3.4 in miniature.

### Worked example C (illustrative, accuracy-blind point, from Guo Eq. 1 + Brier)

A constant predictor outputs p = 0.30 on all 100 samples, of which exactly 30 are
positive. All predictions land in one bin: conf = 0.30, acc = 30/100 = 0.30, so
gap = 0 and ECE = 0. The predictor is perfectly calibrated by Guo's definition
yet has no discrimination. A proper scoring rule catches what ECE misses: its
Brier score is 0.42 in Brier's original two-class form (1 - (0.3^2 + 0.7^2)), or
0.21 in the modern binary form ([30*(0.3-1)^2 + 70*(0.3-0)^2]/100), while a
perfect predictor scores Brier 0 and is also perfectly calibrated. So ECE = 0
covers both the useless and the perfect predictor; Brier separates them.

## Source assets

```text
Asset: Guo et al. 2017, Figure 1. Confidence histograms (top) and reliability
       diagrams (bottom) for a 5-layer LeNet and a 110-layer ResNet on CIFAR-100.
Shows: The reliability diagram itself, and the overconfidence gap: LeNet's bars
       sit near the diagonal, the ResNet's accuracy bars sit well below its
       confidence. This is the single clearest picture of what ECE summarizes.
Crop:  Keep the bottom-row reliability diagrams with the diagonal and the "Gap"
       shading and the axis labels (Confidence, Accuracy). A crop must keep the
       diagonal reference line or the diagram loses its meaning.
```

```text
Asset: Guo et al. 2017, Figure 4 — CIFAR-100 ResNet-110 reliability diagrams
       before calibration (ECE 12.67) and after temperature scaling (ECE 0.96).
Shows: The same diagram before and after the fix, with the gap shrinking to the
       diagonal. Pairs the metric drop with the visual.
Crop:  Keep at least the uncalibrated and the temperature-scaled panels with
       their ECE labels; the two together make the point, either alone does not.
```

```text
Asset: GPT-4 Technical Report, Figure 8 / the two calibration curves labeled
       "ECE: 0.007" (pre-train) and "ECE: 0.074" (ppo).
Shows: A real, recent, named case: the pre-trained model's curve hugs the
       diagonal; the post-trained model's curve pulls away. Directly the misled
       case the lesson needs.
Crop:  Keep both panels side by side with their ECE labels and the diagonal.
       Omitting either panel destroys the before/after contrast.
```

```text
Asset: Kumar et al. 2019, Figure 2 — measured binned calibration error versus
       number of bins on ImageNet and CIFAR-10, with 90% confidence intervals.
Shows: The estimate climbing as bins are added, the visual proof that the number
       reported depends on the binning choice.
Crop:  Keep the axis showing number of bins and the rising curve with its CIs;
       the 15-bin reference is the point of contact with Guo's setup.
```

```text
Asset: Brier 1950, Table 1 — the 10 rain/no-rain forecasts scored to P = 0.19.
Shows: The score computed by hand on real forecasts, the origin worked example.
Crop:  A prose table reconstruction is cleaner than the 1950 scan; if the scan is
       used, keep the forecast/observed columns and the P = 0.19 total.
```

## Discarded

```text
URL: https://rss.onlinelibrary.wiley.com/doi/pdfdirect/10.2307/2987588
     (DeGroot & Fienberg 1983, "The comparison and evaluation of forecasters"):
     the origin of reliability diagrams and the calibration-versus-refinement
     decomposition. Gated behind Wiley/OUP; the fetch returned an HTML wrapper,
     not the article text, so I did not read the passage and do not cite it
     firsthand. Its two relevant claims are available in read primaries:
     reliability diagrams are defined by Guo et al. (who credit this paper), and
     the accuracy-blind point is grounded through Brier's constant-forecast
     baseline and Nixon's zero-ECE construction. Canonical: The Statistician
     32(1-2):12-22, DOI 10.2307/2987588.
```

```text
URL: https://www.dbmi.pitt.edu/wp-content/uploads/2022/10/Obtaining-well-calibrated-probabilities-using-Bayesian-binning.pdf
     A mirror of the Naeini et al. 2015 paper; returned HTTP 404. Rejected in
     favor of the AAAI page of record (ojs.aaai.org/index.php/AAAI/article/view/9602),
     which resolves and offers the PDF.
```

```text
URL: https://arxiv.org/html/2501.19047v1
     "Understanding Model Calibration, a gentle introduction" (2025): a readable
     secondary tutorial. Rejected as padding; the survey (2308.01222) already
     covers the same secondary ground with wider scope, and everything the lesson
     needs is in the primaries.
```

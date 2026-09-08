# Commission: the-instruments/auroc

## The measurement

AUROC, the area under the receiver operating characteristic curve, also written
AUC or c-statistic. The single number reported as "our model scores 0.90 AUC"
whenever a system sorts cases into two classes: sick or well, fraud or not,
click or no click. This desk teaches how that number is made and what it can and
cannot support.

## Why this measurement now

AUROC is the default score in medical-AI and risk-scoring claims, the number that
reaches the public when a model is called accurate. The reader keeps meeting it
and cannot tell whether a high AUROC means the tool works where it is deployed.
The course already teaches calibration (`../the-instruments/calibration-error.html`),
which measures something AUROC deliberately ignores, and it has a documented
deployment failure in `../when-ai-breaks/epic-sepsis-model.html` that a single
AUROC number papered over. This lesson gives the reader the tool to read both.

## The angle

AUROC measures one thing well and is read as if it measured three. It measures
ranking: the probability that the model scores a random positive case above a
random negative one. It says nothing about whether the model's probabilities are
calibrated, nothing about the operating point a deployment actually uses (the
threshold), and it is computed on a test set whose mix of positives to negatives
may not match the world. The real case that carries the lesson: the Epic Sepsis
Model, sold with a vendor-reported AUROC in the low-to-mid 0.8s, was measured by
an external validation (Wong et al., 2021, JAMA Internal Medicine) at an AUROC
around 0.63 and, at the alert threshold hospitals actually used, missed about
two-thirds of sepsis cases while generating heavy false alarms. One number looked
like a passing grade and the deployed tool did not work.

## What to teach (short list, in order)

1. What a binary classifier's score and threshold are: the model outputs a number,
   a threshold turns it into a yes/no. Sensitivity (recall) and specificity, and
   how moving the threshold trades one for the other. Define each in plain words
   at first use.
2. What the ROC curve is (sensitivity against false-positive rate as the threshold
   sweeps) and what its area, AUROC, equals: the ranking probability above. Give
   the reader the intuition with a tiny worked example. 0.5 is a coin flip, 1.0 is
   perfect ranking.
3. The three things AUROC does not tell you: calibration (link calibration-error,
   do not re-teach it), the performance at the one threshold you deploy, and the
   effect of class imbalance (why AUROC can look strong when positives are rare
   and the tool still floods clinicians with false alarms; contrast with
   precision / PPV).
4. The worked failure: Epic Sepsis Model, the two AUROC numbers, the threshold in
   the field, the missed-case fraction and false-alarm burden. Say plainly why a
   high headline AUROC and a broken deployment coexist.

## Template, bands, sources

- Template: lesson. Word band 1200-2200. Sections: why, orientation, 0-4 flex,
  takeaway, sources.
- Source floor (the-instruments/lesson): at least 8 sources, at least 4 primary
  and at least 1 secondary. Primary: the papers that own each claim (the Wong et
  al. JAMA Intern Med external validation; the ROC/AUROC methodological sources
  such as Hanley & McNeil 1982 and a precision-recall-vs-ROC paper such as Saito &
  Rehmsmeier 2015 or Davis & Goadrich 2006; Epic's own model documentation if
  reachable; any FDA/regulatory or health-system primary on the deployment).
  Reporting on the Epic story is secondary context.

## Production policy (resolved)

Profile balanced. writing-coach low/capable, researcher high/capable, writer
medium/capable, editor high/capable. None required. Roles run under the Claude
Code harness on this run's model; the writer records the actual harness and model
in nb-meta.

## A chart may earn its place

An ROC curve, or a small figure showing two thresholds on the same curve, could
carry the ranking-vs-threshold point better than prose. Build it only from the
evidence record's verified series with `nb chart`, label axes, cite the source in
the caption. Do not fabricate a curve; if no verified series supports one, use a
small table or none.

## Background links available (verify and link, do not re-teach)

`../the-instruments/calibration-error.html`,
`../when-ai-breaks/epic-sepsis-model.html`. Others only if the reader needs them.

## This run's neighbors (for coherence, not overlap)

Publishing tonight: the-evidence/alphazero, the-mechanics/attribute-binding,
what-could-go-wrong/encoded-reasoning, when-ai-breaks/waymo-recall. The
epic-sepsis link is to an already-published piece, not one of tonight's; no
cross-coordination needed.

## Habits not to inherit (voice and shape)

Recent the-instruments deks lean on the comma-and mold ("A MATH score is one
boxed answer matched against a key, and the numbers ...") and headings run to
full-sentence claims almost every time. Vary construction. Do not open with a
stock definition; open on the gap between what AUROC is read to mean and what it
measures. No colon-subtitle headline. Avoid the recurring "The one thing X never
shows" heading shape.

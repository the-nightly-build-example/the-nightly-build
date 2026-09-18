# Commission: the-instruments/mean-average-precision

## The assignment

Teach the reader how the mean Average Precision (mAP) number is made and what it can
and cannot support. The measurement is mAP as reported for object detection, the
score under nearly every detection leaderboard (PASCAL VOC and, dominantly, COCO).
One lesson on the lesson template.

The reader is the paper's declared reader: smart, widely read, no codebase. Assume
no computer-vision background. Teach precision and recall from scratch if the reader
needs them here; probability is assumable, the rest is not. The reader has a lesson
on the F1 score (the-instruments/f1-score) that already teaches precision and recall
and how a single summary number hides a class; link it at first use and build on it
rather than re-teaching precision and recall from zero.

## Why this measurement, tonight

The Instruments has taught classification and generation metrics (f1-score, auroc,
calibration-error, imagenet-top-5-accuracy, fid, inception-score, clipscore) but not
the number that ranks object detectors, the task behind "the model found the objects
in the image." mAP is the measurement a reader meets whenever a detection or
segmentation system is compared, and its construction (IoU thresholds, a
precision-recall curve per class, averaged) is genuinely non-obvious. It fits the
beat: a number in wide circulation whose procedure is worth showing step by step.

## The angle

Show, step by step, exactly what a single mAP number is built from, then show one
real case where it misled people:

- The pieces the reader needs first: what object detection outputs (boxes with class
  labels and confidence scores), and Intersection over Union (IoU) as the overlap
  test that decides whether a predicted box counts as a hit. Teach IoU in plain words
  with a worked number.
- Average Precision (AP): for one class, rank detections by confidence, sweep the
  threshold, trace the precision-recall curve, take the area under it. Walk one
  small worked example with real counts so the reader sees a curve become one number.
- mean Average Precision: average AP across all classes, and, on COCO, also average
  across ten IoU thresholds from 0.50 to 0.95 (the "mAP@[.5:.95]" that COCO made the
  default). Make the reader see that "mAP" names several different computations
  (VOC's single-threshold mAP@0.5 vs COCO's averaged-threshold primary metric), and
  that scores under the one name are not comparable across those definitions. This is
  the instrument's core honesty problem and should be the spine of the lesson.
- The real case where the number misled: choose the strongest documented one the
  researcher can source firsthand. Candidates: (a) the COCO metric change itself and
  how mAP@0.5 vs mAP@[.5:.95] produced non-comparable "state of the art" claims;
  (b) documented cases where higher mAP did not mean better real-world detection
  (mAP averages over classes and confidence thresholds, so it can hide failure on a
  rare but critical class, or reward a threshold no deployment uses), echoing the
  f1-score and auroc lessons' theme with detection-specific evidence. The writer
  commits to one case with a primary source and real figures.

Land the judgment the beat asks for: what claim a reported mAP does and does not
license.

## Boundaries

- The metric definitions come from the primary sources that own them: the PASCAL VOC
  papers/devkit and the COCO paper and its official evaluation documentation. The
  misled-people case needs a primary or firsthand source, not a blog restating it.
- Do not drift into teaching how detectors work internally; the lesson is about the
  number, not the architecture.
- No code. A small worked table of detections is welcome (it is furniture, not code);
  a chart of a precision-recall curve is welcome only if built from a verified series
  the researcher supplies, via nb chart.

## Neighbors in this run

Publishing alongside wavenet, typo-robustness, power-seeking-ai,
sports-illustrated-ai-authors. No subject overlap. The nearest taught neighbors are
f1-score and auroc; link and extend, do not repeat their worked examples.

## Recent habits not to inherit

From the last several Instruments lessons (winogrande, mean-opinion-score,
training-cost, clipscore, bertscore, f1-score):

- The desk keeps opening deks with a single vivid counterexample sentence and headlines
  with a surprising number ("more training lifts the score from 50% to 79%"). That is
  the format working; find this piece's own number and reversal rather than echoing a
  neighbor's sentence shape.
- The heading mold of a short noun phrase plus a participle ("Five words, averaged";
  "Eight listeners, screened and tested") recurs. Vary heading construction.
- The "a score doesn't travel between tests" framing was just used for mean opinion
  score. mAP has its own non-comparability story (definitions, not test conditions);
  make the distinction, do not reuse the phrasing.

## Source policy

Floor: at least 8 sources total, at least 4 primary and at least 1 secondary. Primary
means the VOC and COCO papers and their official metric documentation, and the
primary source behind the misled-people case. Meet the floor with sources that change
the interpretation.

## Production record

- Template: lesson. Series: the-instruments (open mode; no commissioned tag).
- Word band: 1200-2200.
- Model/effort actuals: production-policy resolved "capable"/non-required for all
  roles; all run on the available capable model (Claude via isolated subagents),
  coach low, researcher high, writer medium, editor high. Nothing traded down.
- Checkout revision: df69fc11a5d7fcdfdbc7eda5eb8a8d178b6d6a17.

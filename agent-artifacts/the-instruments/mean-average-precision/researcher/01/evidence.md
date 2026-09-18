# Evidence: the-instruments/mean-average-precision (round 01)

The evidence supports the commissioned angle and gives it a stronger, cleaner
spine than the commission sketched. The IoU test, per-class AP as area under a
precision-recall curve, and the VOC-vs-COCO threshold difference are all pinned
to their owning primaries, including the exact formulas and the exact procedural
change the definitions went through. The misled-people case is unusually
well documented: the YOLOv3 paper (Redmon and Farhadi, 2018) is itself both the
source of the confusion and the source that explains it, with two specific,
matched model configurations that swap rank depending on which "mAP" is read.
That is the record's most important limitation: the clearest documentation of
the metric's power to mislead is the original authors flagging their own result
in the same paper, not an independent account of a third party who was fooled
downstream and said so on the record. A second, harder limitation surfaced on
purpose: a 2023 study correlating detection metrics with actual self-driving
outcomes found mAP's analogue was a fairly good predictor of real performance,
not a false one, in that setting. The lesson should not overstate "mAP lies";
the sourced case is about definitions that silently changed what a number
measures, and about a metric that averages away information a reader may need,
not about a metric that is worthless.

## Sources

```text
URL:         http://host.robots.ox.ac.uk/pascal/VOC/pubs/everingham10.pdf
Kind:        primary — Mark Everingham, Luc Van Gool, Christopher K. I.
             Williams, John Winn, Andrew Zisserman, "The PASCAL Visual Object
             Classes (VOC) Challenge," International Journal of Computer
             Vision 88(2):303-338, 2010 (DOI 10.1007/s11263-009-0275-4). The
             VOC organizers' own account of their dataset and evaluation
             procedure; owns the VOC2007-era definitions.
Establishes: The IoU overlap test and its 0.5 threshold (Sect. 4.2, Eq. 3);
             the 11-point interpolated Average Precision used through 2009
             (Sect. 4.2, Eqs. 1-2); why the threshold was set at 0.5; and an
             empirical test of how measured AP changes as the overlap
             threshold is varied (Sect. 6.2.3, Fig. 19).
Paraphrase:  A detection counts as correct only if the overlap ratio a_o =
             area(B_p intersect B_gt) / area(B_p union B_gt) exceeds 0.5,
             where B_p is the predicted box and B_gt the ground-truth box.
             The threshold was set deliberately low "to account for
             inaccuracies in bounding boxes in the ground truth data." For a
             given class, AP is the mean of the interpolated precision at
             eleven equally spaced recall levels {0, 0.1, ..., 1}, where the
             precision at each recall level is the maximum precision measured
             at any recall greater than or equal to it (this was intended to
             smooth "wiggles" in the raw curve). Separately, the paper tested
             sensitivity to the overlap threshold itself, on the "car" class
             where methods scored best: AP fell steeply for thresholds above
             50%, and dropping the threshold to 10% raised measured AP by
             about 7.5 points, showing none of the 2007 methods produced
             tightly localized boxes.
Locators:    Sect. 4.2 "Evaluation of Results," subsections "Average
             Precision (AP)" and "Bounding Box Evaluation" (pp. 313-314);
             Sect. 6.2.3 "Evaluation of the Overlap Threshold" and Fig. 19
             (p. 328).
Quote:       "the overlap ratio ao between the predicted bounding box Bp and
             ground truth bounding box Bgt must exceed 0.5 (50%)"; "The
             threshold of 50% was set deliberately low to account for
             inaccuracies in bounding boxes in the ground truth data"; "the
             measured AP drops steeply for thresholds above 50%... Reducing
             the threshold to 10% results in an increase in measured AP of
             around 7.5%."
```

```text
URL:         https://www.robots.ox.ac.uk/~vgg/projects/pascal/VOC/pubs/everingham15.pdf
Kind:        primary — Mark Everingham, S. M. Ali Eslami, Luc Van Gool,
             Christopher K. I. Williams, John Winn, Andrew Zisserman, "The
             PASCAL Visual Object Classes Challenge: A Retrospective,"
             International Journal of Computer Vision 111(1):98-136, 2015
             (DOI 10.1007/s11263-014-0733-5). Same organizing team,
             reviewing 2008-2012; owns the record of the AP procedure change.
Establishes: That the method of computing AP changed starting with the 2010
             challenge, and names both what changed and why.
Paraphrase:  "Up until 2009 interpolated average precision... was used... from
             2010 onwards the method of computing AP changed to use all data
             points rather than TREC-style sampling" at the fixed 11 recall
             levels. The 11-point method's smoothing came at a cost: it "was
             too crude to discriminate between methods at low AP." The
             bounding-box overlap test itself (area of overlap must exceed
             50% by the intersection-over-union formula) is repeated
             unchanged from the 2010 paper.
Locators:    Sect. 2.4.3-2.4.4 (numbered "Detection" and neighboring
             subsections), p. 104.
Quote:       "from 2010 onwards the method of computing AP changed to use all
             data points rather than TREC-style sampling (which only sampled
             the monotonically decreasing curve at a fixed set of
             uniformly-spaced recall values 0, 0.1, 0.2, ..., 1)... the
             downside of this interpolation was that the evaluation was too
             crude to discriminate between the methods at low AP."
```

```text
URL:         https://www.robots.ox.ac.uk/~vgg/projects/pascal/VOC/voc2012/devkit_doc.pdf
Kind:        primary — Mark Everingham and John Winn, "The PASCAL Visual
             Object Classes Challenge 2012 (VOC2012) Development Kit," 18 May
             2012. The distributed technical specification participants
             coded against; owns the exact algorithmic definition of
             post-2010 AP.
Establishes: The precise two-step procedure for computing AP from 2010
             onward, and restates the IoU test and threshold for the
             detection task.
Paraphrase:  AP is computed by (1) making the precision/recall curve
             monotonically decreasing, setting precision at recall r to the
             maximum precision at any recall r' >= r, then (2) taking the
             area under that curve by exact numerical integration ("no
             approximation is involved since the curve is piecewise
             constant"). This replaced sampling the curve only at {0, 0.1,
             ..., 1}; from 2010 the challenge "effectively samples the curve
             at all unique recall values." Detections are still true
             positives only if the overlap ratio exceeds 50% by the same
             intersection-over-union formula as 2007.
Locators:    Sect. 3.4.1 "Average Precision (AP)," p. 12; Sect. 4.4
             "Evaluation," pp. 13-14.
Quote:       "The computation of the average precision (AP) measure was
             changed in 2010 to improve precision and ability to measure
             differences between methods with low AP... Note that prior to
             2010 the AP is computed by sampling the monotonically decreasing
             curve at a fixed set of uniformly-spaced recall values 0, 0.1,
             0.2, ..., 1. By contrast, VOC2010-2012 effectively samples the
             curve at all unique recall values."
```

```text
URL:         https://arxiv.org/pdf/1405.0312
Kind:        primary — Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir
             Bourdev, Ross Girshick, James Hays, Pietro Perona, Deva Ramanan,
             C. Lawrence Zitnick, Piotr Dollar, "Microsoft COCO: Common
             Objects in Context," arXiv:1405.0312v3 (last revised 21 Feb
             2015; originally ECCV 2014). The dataset paper; owns the dataset
             construction and cross-dataset comparison, but explicitly does
             not own the final detection metric definition.
Establishes: That the paper itself defers the detailed evaluation-metric
             definition to a not-yet-complete evaluation server, and gives
             the VOC-vs-COCO cross-dataset difficulty comparison using
             (single-threshold) AP.
Paraphrase:  At the time of this paper the authors write that the evaluation
             server for automatic test-set scoring was still being finished,
             and that "a full discussion of evaluation metrics" would follow
             once it was complete — the paper is not the source that defines
             mAP@[.5:.95]. Separately, comparing a DPM detector trained on
             PASCAL VOC 2012 against the same detector trained on COCO, the
             cross-dataset AP gap was 12.7 AP points for the VOC-trained model
             versus 7.7 AP points for the COCO-trained model, evidence COCO is
             harder and less iconic than VOC.
Locators:    Sect. 7 "Dataset Splits" note (printed p. 7); Sect. 8
             "Algorithmic Analysis," subsection "Bounding-box detection"
             (printed p. 9), Table 1.
Quote:       "We are currently finalizing the evaluation server for automatic
             evaluation on the test set. A full discussion of evaluation
             metrics will be added once the evaluation server is complete."
```

```text
URL:         https://cocodataset.org/#detection-eval
Kind:        primary — COCO Consortium, official "Detection Evaluation"
             documentation. This is the page that actually defines the 12
             COCO detection metrics, including the primary challenge metric;
             loaded by client-side script from the site's own
             dataset/detection-eval.htm partial, which is how the page
             renders its "Evaluate > Detection" tab content in every browser.
Establishes: The formal definition of AP@[.5:.95] as the COCO primary metric,
             its relationship to AP@0.5 ("the PASCAL VOC metric"), and the
             explicit statement that averaging over IoU is "a break from
             tradition."
Paraphrase:  COCO defines 12 metrics. The headline one, labeled simply "AP,"
             is "AP at IoU=.50:.05:.95," called out in bold as the "(primary
             challenge metric)." AP at a single IoU of 0.50 is listed
             separately and labeled "(PASCAL VOC metric)"; AP at IoU=0.75 is
             labeled "(strict metric)." The documentation states plainly that
             computing AP at one IoU of 0.5 is "tradition" and that COCO's
             average over ten thresholds is a deliberate break from it,
             because "averaging over IoUs rewards detectors with better
             localization." It also states COCO treats "AP" and "mAP"
             (averaged over categories) as interchangeable terms. About 41%
             of COCO instances are "small" (area < 32^2 px), 34% "medium," 24%
             "large."
Locators:    Sections "1. Detection Evaluation" and "2. Metrics," notes 1-4.
Quote:       "AP at IoU=.50:.05:.95 (primary challenge metric)"; "AP at
             IoU=.50 (PASCAL VOC metric)"; "Unless otherwise specified, AP and
             AR are averaged over multiple Intersection over Union (IoU)
             values. Specifically we use 10 IoU thresholds of .50:.05:.95.
             This is a break from tradition, where AP is computed at a single
             IoU of .50... Averaging over IoUs rewards detectors with better
             localization."; "AP is averaged over all categories.
             Traditionally, this is called 'mean average precision' (mAP). We
             make no distinction between AP and mAP."
```

```text
URL:         https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py
Kind:        primary — the COCO Consortium's own reference implementation
             (pycocotools), the code that actually computes every officially
             reported COCO AP/mAP number, including on the hidden test set
             and leaderboard.
Establishes: The exact numeric parameters behind the definitions in the
             evaluation documentation: ten IoU thresholds and 101 recall
             points, and that the headline number is a plain mean over the
             per-setting precision values.
Paraphrase:  The default parameters set iouThrs to np.linspace(.5, 0.95, 10)
             — i.e., [.50, .55, ..., .95] — and recThrs to np.linspace(0, 1,
             101) — i.e., 101 points from 0 to 1 in steps of .01. The
             summarize() method that produces the reported AP figure computes
             a plain arithmetic mean (np.mean) over the selected precision
             array, after selecting which IoU thresholds, classes, and area
             ranges to include.
Locators:    Class docstring, "iouThrs" and "recThrs" parameter comments
             (lines ~25-26); Params.setDetParams (iouThrs/recThrs
             assignments, lines ~506-507 and ~517-518); COCOeval.summarize()
             (line ~422 onward, mean_s = np.mean(s[s>-1])).
Quote:       "iouThrs - [.5:.05:.95] T=10 IoU thresholds for evaluation";
             "recThrs - [0:.01:1] R=101 recall thresholds for evaluation."
```

```text
URL:         https://arxiv.org/pdf/1804.02767
Kind:        primary — Joseph Redmon and Ali Farhadi, "YOLOv3: An Incremental
             Improvement," arXiv:1804.02767, 8 Apr 2018. The paper's own
             authors report and explain the discrepancy this lesson needs;
             it is the primary source for the misled-people case.
Establishes: Two matched head-to-head comparisons of the same models under
             AP50 ("the old .5 IOU mAP detection metric") versus COCO's
             primary AP@[.5:.95], where the ranking implied by one metric
             is contradicted by the other; the authors' own explanation of
             why (localization quality); and confirmation, from inside the
             field, that the COCO paper did not originally justify or fully
             specify the metric change.
Paraphrase:  Headline comparison (Abstract; Fig. 3 and its data table, "AP50"
             axis; Fig. 1 and its data table, "COCO AP" axis): YOLOv3-608
             scores AP50 = 57.9 in 51 ms on a Titan X; RetinaNet-101-800
             scores AP50 = 57.5 in 198 ms — YOLOv3 is stated as having
             "similar performance but 3.8x faster." On the same two model
             configurations, COCO's primary AP (averaged over IoU .5-.95)
             is 33.0 for YOLOv3-608 versus 37.8 for RetinaNet-101-800 — a
             4.8-point (about 14.5% relative) gap in RetinaNet's favor that
             the AP50 comparison does not show. A second, larger-backbone
             comparison (Table 3): YOLOv3-608 AP=33.0/AP50=57.9/AP75=34.4
             versus RetinaNet ResNet-101-FPN AP=39.1/AP50=59.1/AP75=42.3 and
             RetinaNet ResNeXt-101-FPN AP=40.8/AP50=61.1/AP75=44.1 — YOLOv3
             again looks close on AP50 (within 1.2-3.2 points) but is 6.1-7.8
             AP points behind on the primary metric. Section 5, "What This
             All Means," states this outright: "It's not as great on the
             COCO average AP between .5 and .95 IOU metric. But it's very
             good on the old detection metric of .5 IOU." Section 3 gives the
             mechanism: "performance drops significantly as the IOU threshold
             increases indicating YOLOv3 struggles to get the boxes perfectly
             aligned with the object." The paper also confirms, from a
             detection researcher reading the COCO paper at the time, that
             COCO's own paper did not explain the metric choice: "The
             original COCO paper just has this cryptic sentence: 'A full
             discussion of evaluation metrics will be added once the
             evaluation server is complete.'" The Rebuttal section adds the
             authors' own worked hypothetical showing mAP can be fooled by
             rank order alone, independent of the IoU-averaging question: two
             detectors with the same six per-class confidence-ranked outputs
             score identically under mAP despite very different score
             calibration, because mAP depends only on the rank ordering of
             detections within each class, not on the confidence values.
Locators:    Abstract; Sect. 3 "How We Do" (Table 3, printed p. 3); Fig. 1
             and its data table (printed p. 1) and Fig. 3 and its data table
             (printed p. 4); Sect. 5 "What This All Means" (printed p. 4);
             Rebuttal, response to "Reviewer #4" (printed p. 6, Fig. 5).
Quote:       "It achieves 57.9 AP50 in 51 ms on a Titan X, compared to 57.5
             AP50 in 198 ms by RetinaNet, similar performance but 3.8x
             faster."; "It's not as great on the COCO average AP between .5
             and .95 IOU metric. But it's very good on the old detection
             metric of .5 IOU."; "The original COCO paper just has this
             cryptic sentence: 'A full discussion of evaluation metrics will
             be added once the evaluation server is complete.'"
```

```text
URL:         https://github.com/rafaelpadilla/review_object_detection_metrics
Kind:        secondary — companion repository (same authors) to Rafael
             Padilla, Wesley L. Passos, Thadeu L. B. Dias, Sergio L. Netto,
             Eduardo A. B. da Silva, "A Comparative Analysis of Object
             Detection Metrics with a Companion Open-Source Toolkit,"
             Electronics 10(3):279, 2021 (DOI 10.3390/electronics10030279,
             open access). Independent academic surveyors of detection
             metrics, not the VOC or COCO organizers; reports on and
             quantifies the definitions the primaries above set. (The
             publisher page at mdpi.com returned HTTP 403 to automated
             fetches; this repository mirrors the paper's content, is
             maintained by its lead author, and reproduces the same
             comparison with a runnable worked example; see Discarded.)
Establishes: A concrete, numeric illustration that interpolation method
             alone (holding the IoU threshold fixed) changes the reported AP
             on identical detections, independent of the VOC/COCO threshold
             question — and states plainly that this proliferation of
             AP variants is a real problem for reproducibility.
Paraphrase:  On the toy example, 11-point interpolation gives AP = 88.64% at
             IoU 0.5, versus all-point interpolation giving AP = 89.58% on
             the same detections — the interpolation choice alone moves the
             score. At IoU 0.75, 11-point gives AP = 49.24% versus 50.97% for
             all-point. The repository's survey table lists which
             detector papers report COCO-style AP@[.5:.05:.95] and which
             report only AP@.5, underscoring that a "mAP" figure by itself
             does not say which of these an author used.
Locators:    README.md, section "Different Implementations of AP," toy
             example and per-model metrics table.
Quote:       "the 11-point interpolation method obtained AP=88.64% while the
             all-point interpolation method improved the results a little,
             reaching AP=89.58%... In both cases, the all-point interpolation
             approach considers larger areas above the curve into the
             summation and consequently obtains higher results."
```

```text
URL:         https://openaccess.thecvf.com/content/ICCV2023W/BRAVO/papers/Schreier_On_Offline_Evaluation_of_3D_Object_Detection_for_Autonomous_Driving_ICCVW_2023_paper.pdf
Kind:        secondary — Tim Schreier, Katrin Renz, Andreas Geiger, Kashyap
             Chitta, "On Offline Evaluation of 3D Object Detection for
             Autonomous Driving," ICCV 2023 Workshop on Benchmarking Robust
             and Agile Autonomous Vehicles (BRAVO), CVF Open Access.
             Independent empirical study of whether detection metrics
             predict downstream task performance; not affiliated with VOC,
             COCO, or the models it tests.
Establishes: Direct evidence on the commission's "did a higher mAP mean
             better real-world performance" question, for 3D detection in
             simulated self-driving — and complicates a blanket "mAP
             misleads" reading rather than confirming it.
Paraphrase:  Testing 16 3D object detectors integrated into a full
             self-driving stack in the CARLA simulator, the authors found
             standard mAP correlates strongly with the CARLA Driving Score
             (Pearson r = 0.80) and with collision count (r = 0.90). A
             task-specific alternative, the nuScenes Detection Score,
             correlated somewhat more strongly with Driving Score (r = 0.85)
             but similarly with collisions (r = 0.90). The authors conclude
             offline metrics, mAP included, "can provide reasonable
             heuristics" for a detector's real driving performance, while
             planner-centric alternatives correlated markedly worse. This is
             3D (LiDAR/camera) detection for driving, a different modality
             and task from the 2D image mAP this lesson teaches, and it
             measures correlation with a simulated downstream task, not
             whether any specific higher-mAP model was in fact worse.
Locators:    Abstract; Sect. 1 "Introduction," paragraph 1; Sect. 5
             "Results," "nuScenes Detection Score Ablation" and "Conclusion"
             (Table 1; printed pp. 4-6).
Quote:       "We find that even though mAP is highly correlated with driving
             performance, the nuScenes Detection Score... a task-specific
             variation, is even more predictive."; "NDS correlates more to
             the CARLA Driving Score than the standard mAP metric (0.85 vs.
             0.80). Both metrics have similar correlations to the number of
             collisions (0.90)."
```

## Contradictions

- The commission frames the lesson's "misled people" case as showing "a higher
  mAP misled people" or "higher mAP did not mean better real-world detection."
  The strongest documented case found (YOLOv3 vs. RetinaNet) is not quite that
  shape: it is two models that are near-tied, or even slightly reversed in
  YOLOv3's favor, under one common mAP definition (AP50) while a real gap
  favoring the other model exists under COCO's primary AP@[.5:.95]. No
  reported figure in this case is a mAP that is simply "higher" and wrong; the
  issue is that the same word names two computations with different rankings.
  The record above states the numbers precisely so the writer can decide
  whether to keep the "misled" framing (both metrics were widely reported and
  compared as if interchangeable, at a time the community mostly still cited
  AP50 by habit) or reframe around non-comparability rather than direction.

- Schreier et al. (2023) is a direct, searched-for counterweight: in a
  controlled study, a detection mAP analogue was found to correlate strongly
  (r = 0.80) with actual downstream task performance, not to mislead about it.
  This does not contradict the VOC/COCO definitional-incompatibility evidence,
  but it complicates any claim that mAP-type metrics are generally poor
  predictors of real-world quality. The domain (3D/LiDAR detection for
  self-driving, evaluated by simulated driving score) differs from the 2D
  COCO/VOC image detection this lesson teaches, so the finding should be
  used to temper the lesson's claim, not to stand in as its own worked case.

- No contradiction was found on the core definitions themselves (the IoU
  formula, the 0.5 threshold's rationale, or COCO's ten-threshold average):
  every primary source that states them agrees, including the reference
  implementation.

## Numbers

```text
Figure: IoU/overlap threshold for a correct detection = 0.5 (both VOC and
        COCO's AP@0.50)
Owner:  Everingham et al. 2010, Eq. 3; reaffirmed in VOC2012 devkit doc
        Sect. 4.4; COCO evaluation documentation lists "AP at IoU=.50" as
        "the PASCAL VOC metric"
Scope:  Per-detection true/false-positive test; same threshold value reused
        by COCO as one of its ten
```

```text
Figure: 11 (number of recall points sampled for VOC AP, 2005-2009)
Owner:  Everingham et al. 2010, Eq. 1 ({0, 0.1, ..., 1})
Scope:  VOC classification and detection tasks, challenge years up to 2009
```

```text
Figure: All unique recall values (VOC AP, 2010 onward) / 101 recall points
        [0:.01:1] (COCO AP)
Owner:  VOC2012 devkit doc Sect. 3.4.1 (VOC); COCO cocoeval.py Params
        (recThrs) and detection-eval documentation (COCO)
Scope:  VOC2010-2012 challenges; all COCO detection evaluation since the
        evaluation server went live
```

```text
Figure: 10 IoU thresholds, 0.50 to 0.95 in steps of 0.05 (COCO's iouThrs)
Owner:  COCO detection evaluation documentation; cocoeval.py Params
        (iouThrs = np.linspace(.5, .95, 10))
Scope:  COCO's primary "AP" figure, averaged over these 10 thresholds and
        all 80 categories; distinct from AP50 and AP75, which fix one
        threshold
```

```text
Figure: AP dropped ~7.5 points when the VOC overlap threshold was relaxed
        from 50% to 10% (best-performing 2007 "car" submissions)
Owner:  Everingham et al. 2010, Sect. 6.2.3, Fig. 19
Scope:  Single class ("car"), VOC2007 detection task, submitted 2007 methods
        only; illustrates threshold sensitivity, not a general constant
```

```text
Figure: YOLOv3-608 AP50 = 57.9 vs. RetinaNet-101-800 AP50 = 57.5 (near-tied,
        YOLOv3 slightly ahead); same two models' COCO primary AP: YOLOv3-608
        = 33.0 vs. RetinaNet-101-800 = 37.8 (RetinaNet ahead by 4.8 points)
Owner:  Redmon & Farhadi 2018 (YOLOv3 paper), Abstract; Fig. 1 and Fig. 3
        data tables
Scope:  Single-image inference on COCO test-dev (implied by paper's standard
        practice); inference times 51 ms (YOLOv3-608) vs. 198 ms
        (RetinaNet-101-800) on a Titan X/M40-class GPU
```

```text
Figure: Table 3 comparison: YOLOv3-608 AP/AP50/AP75 = 33.0/57.9/34.4 vs.
        RetinaNet ResNet-101-FPN = 39.1/59.1/42.3 and RetinaNet
        ResNeXt-101-FPN = 40.8/61.1/44.1
Owner:  Redmon & Farhadi 2018, Table 3 (adapted from the RetinaNet/Focal
        Loss paper, Lin et al. 2017, per the table's own credit line)
Scope:  COCO test-dev; a second, larger-backbone comparison, kept distinct
        from the abstract's 800-px RetinaNet pairing above
```

```text
Figure: COCO object-size mix: ~41% small (area < 32^2 px), 34% medium
        (32^2-96^2 px), 24% large (area > 96^2 px)
Owner:  COCO detection evaluation documentation, Metrics note 4
Scope:  COCO dataset as a whole; area measured on the segmentation mask
```

```text
Figure: 11-point-interpolated AP = 88.64% vs. all-point AP = 89.58% at IoU
        0.5 on one toy example; 49.24% vs. 50.97% at IoU 0.75
Owner:  Padilla et al. companion repository (review_object_detection_metrics
        README), reproducing the Electronics 2021 paper's worked example
Scope:  Single synthetic toy example built by the survey authors to isolate
        the effect of interpolation method alone; illustrative, not a
        benchmark result
```

```text
Figure: mAP-vs-driving-outcome correlation (Pearson r): 0.80 (mAP vs. CARLA
        Driving Score), 0.85 (nuScenes Detection Score vs. Driving Score),
        0.90 (both metrics vs. collision count)
Owner:  Schreier et al. 2023, Sect. 5, Table 1
Scope:  16 3D object detectors, CARLA simulator, self-driving stack; not
        image-plane COCO/VOC mAP
```

## Source assets

```text
Asset: Fig. 19 in Everingham et al. 2010 (p. 328) — AP plotted as a function
       of the overlap threshold, for the "car" class, VOC2007
Shows: How steeply measured AP falls once the IoU requirement is pushed
       above 0.5, and how flat it stays below 0.5 — the empirical basis for
       "0.5 is lenient" that motivates COCO's harder thresholds
Crop:  Keep the axis labels (overlap threshold vs. AP) and the 50% marker
       line; the caption's method-name legend is not needed if only the
       shape of the curve is being shown
```

```text
Asset: Fig. 1 and Fig. 3 in the YOLOv3 paper (pp. 1 and 4) — two
       speed/accuracy scatterplots of the same models, one axis "COCO AP,"
       the other "COCO mAP-50," each with a data table beside it
Shows: The same set of detectors reordering, or nearly tying, depending on
       which mAP definition sits on the y-axis — the visual form of the
       "misled" case
Crop:  Either plot works alone; if used together they must keep matching
       model labels (RetinaNet-50/101/800, YOLOv3-320/416/608) visible in
       both so a reader can track one model between the two charts
```

```text
None found — for the COCO detection-evaluation documentation itself (a
metrics table, not a chart) and for the cocoeval.py reference implementation
(source code); both are better shown as a short prose table than as an image,
per the boundaries in the commission.
```

## Discarded

```text
URL: https://www.mdpi.com/2079-9292/10/3/279 — the publisher's own page for
     the Padilla et al. Electronics 2021 paper returned HTTP 403 to every
     automated fetch attempt (direct curl with multiple user agents, and
     WebFetch). Substituted the lead author's companion GitHub repository
     (review_object_detection_metrics), which mirrors the paper's content
     under the same CC BY license and is cited above instead.
```

```text
URL: http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/devkit_doc.html —
     redirects (301) to a path that 404s on the new host
     (www.robots.ox.ac.uk); the equivalent content was obtained instead from
     the maintained devkit_doc.pdf at the same site, cited above.
```

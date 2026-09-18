# Writer handoff: the-instruments/mean-average-precision (round 01)

## Original work

The evidence record supplies the IoU formula, the VOC 2007-vs-2010
interpolation change, COCO's ten-threshold average, and the YOLOv3 paper's
AP50/COCO-AP figures as separate, discrete facts; this draft turns them into
one argument, that "mAP" names at least three incompatible computations
under one name, teaches Average Precision through an original six-detection
worked example (rank, hit/miss, running precision/recall, area under the
interpolated curve, worked to about 0.69) that the evidence does not
contain, renders the YOLOv3-vs-RetinaNet reversal as a chart built for this
piece from the paper's own reported figures, and uses that full construction
to weigh the Schreier counterweight explicitly and land a bounded verdict
("the number silently changed what it measures and averages away
information," not "mAP lies") that no single source in the record states.

## Proof result

`nb stamp` then `nb check ... --series the-instruments --library
<checkout>` (links included): **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**.
No warnings were intentionally left; none remained to leave. Word count
2199 (band 1200-2200), 9 sources (7 primary, 2 secondary, floor is 8/4/1),
first-citation order clean.

The chart (`chart-1.py`/`chart-1.png`, grouped bars: AP50 vs. COCO AP for
YOLOv3-608 and RetinaNet-101-800) was rendered with `nb chart` from the
YOLOv3 paper's own reported figures and inspected. The full rendered page
was checked with `nb preview` + `nb render-check` (390px viewport: no
overflow, styles attached, no page errors) and visually inspected via a
headless-Chrome screenshot with the proxy configured, which also confirmed
the inline IoU equation typesets correctly through the runtime's KaTeX load
(the render probe alone doesn't exercise that CDN fetch, so I verified it
separately).

## Open questions for the editor / researcher

- For word budget, I cut two evidence items that are true but not load-bearing
  for the spine: the COCO paper's PASCAL-VOC-trained-vs-COCO-trained
  cross-dataset AP gap (12.7 vs. 7.7 points), and the YOLOv3 authors calling
  COCO's deferred-metric sentence "cryptic." Both are still in the evidence
  record if a later round has room and wants them back; neither is needed for
  the current argument or citations.
- No voice-guide ambiguity surfaced. The three assigned voice moves (Lee's
  numbers-before-naming order for the worked AP example, Karpathy's flat
  list for what mAP averages away, and Thomas's proxy-paragraph triad) are
  each used exactly once, aimed at this lesson's own material.
- No researcher gap: every claim in the draft traces to a source the
  researcher opened; nothing needed inventing or working around.

# editor review-brief: the-instruments/mean-average-precision (01)

Inputs to read (in the order the skill names):
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/writing-coach/01/voice-guide.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/editorial-direction.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/commission.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/writer/01/brief.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/researcher/01/evidence.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/writer/01/draft-handoff.md
  the article: .nb-work/the-instruments/mean-average-precision/library/the-instruments/mean-average-precision.html
  the chart provenance: .nb-work/the-instruments/mean-average-precision/library/the-instruments/mean-average-precision/chart-1.py and chart-1.png
  template context under .nb-work/the-instruments/mean-average-precision/.nb-context/

Output: .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/editor/01/editorial-review.md

Recent-pattern notes (break any edge/heading/dek built like these):
  - The desk opens deks with one vivid counterexample sentence and headlines with a surprising number; the "a score doesn't travel between tests" framing was just used for mean-opinion-score. mAP's story is definitional non-comparability, a different thing; make sure the piece isn't echoing that neighbor's framing or sentence shape.
  - Heading mold to avoid: short noun phrase + participle ("Five words, averaged"; "Eight listeners, screened").

This round's focus (break the highest-risk claims first):
  - The central claim is "mAP names at least three incompatible computations under one name" (VOC 11-point vs all-point AP; VOC mAP@0.5 vs COCO AP@[.5:.95]; the ten-threshold average). Verify each definition against its owning primary in the evidence record (VOC papers/devkit, COCO paper, cocoeval.py).
  - The misled case: the YOLOv3-vs-RetinaNet reversal (AP50 57.9 vs 57.5 near-tied; COCO AP 33.0 vs 37.8) is the writer's, flagged by YOLOv3's own authors. Confirm the piece does NOT claim a specific named victim was deceived (the record found none) and frames it as definitional.
  - Do not overclaim "mAP is worthless": confirm the Schreier et al. 2023 counterweight (r=0.80 in a controlled driving study, different domain) is addressed and the verdict lands on "silently changed what it measures / averages away information."
  - Chart: inspect chart-1.py provenance and read chart-1.png as a reader — labels, scale, legend, and honesty — and compare its numbers with the evidence record and the YOLOv3 primary. Chart fixes route to the writer (they hold the tooling); do not edit chart provenance yourself.
  - The worked six-detection AP example is the writer's own; check its arithmetic. Confirm precision/recall are taught by linking f1-score, not re-derived; IoU/AP taught with the worked example.
  - Length is at 2199/2200; an addition needs an equal cut.

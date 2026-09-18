# writer brief: the-instruments/mean-average-precision (01)

Inputs:
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/editorial-direction.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/commission.md — angle, boundaries, reader
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/writing-coach/01/voice-guide.md
  .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/researcher/01/evidence.md
  the initialized article: .nb-work/the-instruments/mean-average-precision/library/the-instruments/mean-average-precision.html
  template contract and catalogs under .nb-work/the-instruments/mean-average-precision/.nb-context/

Output: .nb-work/the-instruments/mean-average-precision/agent-artifacts/the-instruments/mean-average-precision/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/mean-average-precision/library/the-instruments/mean-average-precision.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/67c352f8-06f4-5e83-b6d0-5e6a0d5d584d/scratchpad/library-checkout
       (--no-check-links while iterating; nb stamp before final check; final check BLOCK: 0 with links included)

Recent shapes to break: the desk keeps opening deks with one vivid counterexample sentence and headlines with a surprising number; the "a score doesn't travel between tests" framing was just used for mean-opinion-score. mAP's story is definitional non-comparability (same word, two computations), not test conditions. Avoid the heading mold of a short noun phrase plus a participle ("Five words, averaged"). Find this piece's own headline and headings.

This round's focus (from the evidence record):
  - The spine is definitional non-comparability: VOC's 11-point vs all-point AP, VOC mAP@0.5 vs COCO's primary AP@[.5:.95], the ten-threshold average. Pin each definition to its owning primary (VOC papers/devkit, COCO paper, cocoeval.py).
  - The misled-people case: frame it as the documented YOLOv3-vs-RetinaNet non-comparability (AP50 57.9 vs 57.5 near-tied, but COCO AP@[.5:.95] 33.0 vs 37.8 — ranking flips), flagged by YOLOv3's own authors. The record found NO named third party who was fooled on the record, so do not claim a specific victim was deceived; frame it as the definitions making rankings flip under the same name.
  - Do not overclaim "mAP is worthless": the record surfaces a counterweight (Schreier et al. 2023 found a detection-mAP analogue correlated r=0.80 with real driving outcomes in a controlled study, different domain). Land the judgment on "the number silently changed what it measures and averages away information," not "the number is useless." Address this contradiction in the prose.
  - Teach precision/recall by linking the-instruments/f1-score (already teaches them) rather than re-deriving from zero; teach IoU and AP with a small worked example. A PR-curve chart is welcome only if built from a verified series via nb chart; a small worked table of detections is welcome furniture.

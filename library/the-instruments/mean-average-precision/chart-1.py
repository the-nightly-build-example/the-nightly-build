"""YOLOv3-608 and RetinaNet-101-800 under two different "mAP" scores.

Source: Redmon & Farhadi, "YOLOv3: An Incremental Improvement" (2018),
arXiv:1804.02767. Abstract; Fig. 1 and Fig. 3 data tables.

AP50 (single IoU threshold of 0.5, "the old detection metric"):
  YOLOv3-608           57.9
  RetinaNet-101-800    57.5

COCO AP (primary metric, averaged over ten IoU thresholds 0.50-0.95):
  YOLOv3-608           33.0
  RetinaNet-101-800    37.8

Both figures for both models come from the same paper, reporting the same
two trained detectors under both metrics.
"""

import plotly.graph_objects as go

models = ["YOLOv3-608", "RetinaNet-101-800"]
ap50 = [57.9, 57.5]
coco_ap = [33.0, 37.8]

fig = go.Figure()
fig.add_trace(go.Bar(name="AP50 (IoU 0.5 only)", x=models, y=ap50, text=ap50))
fig.add_trace(
    go.Bar(
        name="COCO AP (avg. over IoU 0.50–0.95)",
        x=models,
        y=coco_ap,
        text=coco_ap,
    )
)
fig.update_traces(textposition="outside")
fig.update_layout(
    barmode="group",
    yaxis_title="AP (percent)",
    yaxis_range=[0, 70],
)

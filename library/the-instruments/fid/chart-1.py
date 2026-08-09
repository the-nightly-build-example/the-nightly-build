"""FFHQ: two face generators under Inception-FID vs a CLIP-feature FID.

Every figure below is owned by Kynkaanniemi, Karras, Aittala, Aila &
Lehtinen, "The Role of ImageNet Classes in Frechet Inception Distance"
(ICLR 2023), arXiv:2203.06026, Figure 7 (see the article's Sources list,
entry 4, and research.md Numbers). Lower is better for both distances.

  Inception-FID (the standard FID):
    - Projected FastGAN  5.28
    - StyleGAN2          5.30   -> essentially a tie
  CLIP-feature FID (same Frechet distance, CLIP features, quality cross-check):
    - Projected FastGAN  4.67
    - StyleGAN2          2.76   -> StyleGAN2 well ahead

The point of the chart: the two models are a tie under Inception features
and split under CLIP features, so the ranking exists only in one feature
space.
"""

import plotly.graph_objects as go

metrics = ["Inception-FID<br>(standard FID)", "CLIP-FID<br>(quality cross-check)"]

stylegan2 = [5.30, 2.76]
fastgan = [5.28, 4.67]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="StyleGAN2",
        x=metrics,
        y=stylegan2,
        text=[f"{v:.2f}" for v in stylegan2],
        textposition="outside",
    )
)
fig.add_trace(
    go.Bar(
        name="Projected FastGAN",
        x=metrics,
        y=fastgan,
        text=[f"{v:.2f}" for v in fastgan],
        textposition="outside",
    )
)
fig.update_layout(
    barmode="group",
    yaxis_title="distance (lower is better)",
    yaxis=dict(range=[0, 6.5]),
    title="Tied on Inception features, split on CLIP features",
)

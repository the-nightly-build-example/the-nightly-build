"""Winoground group score: CLIPScore against a compositional check.

Source: Zhiqiu Lin et al., "Evaluating Text-to-Visual Generation with
Image-to-Text Generation" (VQAScore, ECCV 2024), arXiv:2404.01291, Table 1
(see the article's Sources list, entry 5, and the evidence record Numbers).

The Winoground group metric scores a system only when it matches BOTH images
to BOTH captions correctly; the two captions are built from the same words in
a different arrangement, so the test is compositional. Random guessing lands
at 1/6 (about 16.7%) and reported human performance is about 85.5% -- both
standard properties of the group metric, used here as the floor and ceiling.

  CLIPScore group score  7.8   -> below the random-chance floor
  VQAScore group score  46.0   -> well above chance, still short of humans

The point of the chart: a cosine-similarity score reads below random guessing
on the swaps, while a compositional check clears the chance line by a wide
margin, on the same prompts.
"""

import plotly.graph_objects as go

metrics = ["CLIPScore", "VQAScore"]
group = [7.8, 46.0]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=metrics,
        y=group,
        text=[f"{v:.1f}" for v in group],
        textposition="outside",
        cliponaxis=False,
    )
)

# Random-chance floor (1/6) and reported human performance: definitional
# properties of the Winoground group metric, not fitted data.
fig.add_hline(
    y=16.7,
    line_dash="dash",
    annotation_text="random chance 16.7",
    annotation_position="top left",
)
fig.add_hline(
    y=85.5,
    line_dash="dot",
    annotation_text="human 85.5",
    annotation_position="bottom left",
)

fig.update_layout(
    yaxis_title="Winoground group score (%)",
    xaxis_title="Alignment metric on the same compositional prompts",
    yaxis=dict(range=[0, 100]),
    title="CLIPScore reads below random guessing on Winoground",
)

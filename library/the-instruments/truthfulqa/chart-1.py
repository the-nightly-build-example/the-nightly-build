"""Llama pretrained models on TruthfulQA: the generative rate rises with size.

Every figure below is owned by Touvron et al., "Llama 2: Open Foundation
and Fine-Tuned Chat Models" (Meta, 2023), arXiv:2307.09288, Table 11 (see
the article's Sources list, entry 3, and evidence.md Numbers). The metric is
the GENERATIVE task: the percentage of generations judged both truthful and
informative (higher is better). These are pretrained base models, not chat
models.

  Llama 1 (params -> truthful-and-informative %):
    7B  27.42
    13B 41.74
    33B 44.19
    65B 48.71
  Llama 2:
    7B  33.29
    13B 41.86
    34B 43.45
    70B 50.18

The point of the chart: within each pretrained family the number climbs as
the model gets bigger, which is the opposite of the "bigger models are less
truthful" reading. The x-axis is model size in billions of parameters on a
log scale.
"""

import plotly.graph_objects as go

llama1_x = [7, 13, 33, 65]
llama1_y = [27.42, 41.74, 44.19, 48.71]

llama2_x = [7, 13, 34, 70]
llama2_y = [33.29, 41.86, 43.45, 50.18]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Llama 1",
        x=llama1_x,
        y=llama1_y,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="Llama 2",
        x=llama2_x,
        y=llama2_y,
        mode="lines+markers",
    )
)
fig.update_layout(
    title="Within each pretrained family, the rate rises with size",
    yaxis_title="truthful and informative (%, generative task)",
    xaxis_title="model size (billion parameters, log scale)",
)
fig.update_xaxes(type="log", tickvals=[7, 13, 33, 65], ticktext=["7B", "13B", "33/34B", "65/70B"])
fig.update_yaxes(range=[0, 60])

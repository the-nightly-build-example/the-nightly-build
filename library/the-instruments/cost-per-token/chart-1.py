"""One fixed task on Claude Opus 5, priced five ways.

Task held constant: 10,000 input tokens, 2,000 output tokens.
Claude Opus 5 rates per million tokens (Anthropic pricing, retrieved 2026-08-03):
  input $5, output $25, cache-hit read $0.50,
  batch input $2.50, batch output $12.50, cache-hit + batch read $0.25.
Cost = tokens / 1_000_000 * rate. Every value below is recomputable from these.
"""

import plotly.graph_objects as go

labels = [
    "Input only<br>(sticker)",
    "Input + output",
    "With caching",
    "With batch",
    "Caching + batch",
]

# input-only: 10_000 * 5 / 1e6 = 0.05
# input + output: 0.05 + 2_000 * 25 / 1e6 (=0.05) = 0.10
# caching: 10_000 * 0.50 / 1e6 (=0.005) + 0.05 = 0.055
# batch: 10_000 * 2.50 / 1e6 (=0.025) + 2_000 * 12.50 / 1e6 (=0.025) = 0.05
# caching + batch: 10_000 * 0.25 / 1e6 (=0.0025) + 0.025 = 0.0275
costs = [0.05, 0.10, 0.055, 0.05, 0.0275]
value_labels = ["$0.05", "$0.10", "$0.055", "$0.05", "$0.0275"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=labels,
        y=costs,
        text=value_labels,
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="US$ per run of the task",
    xaxis_title=None,
    showlegend=False,
)
fig.update_yaxes(range=[0, 0.115])

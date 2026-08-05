"""Total parameters versus active-per-token parameters, three models.

Every figure is read off the model's own paper, card, or announcement:
  GPT-3 (dense):   175B total, all 175B active on every token.
                   Brown et al. 2020, arXiv:2005.14165.
  Mixtral 8x7B:    46.7B total, 12.9B active per token (2 of 8 experts fire).
                   Mistral AI announcement, mistral.ai/news/mixtral-of-experts.
  DeepSeek-V3:     671B total, 37B activated per token.
                   DeepSeek-V3 Technical Report, arXiv:2412.19437.

Active-fraction labels are exact arithmetic on those primary figures:
  175/175 = 100%,  12.9/46.7 = 27.6%,  37/671 = 5.5%.
"""

import plotly.graph_objects as go

models = ["GPT-3<br>(dense)", "Mixtral 8x7B", "DeepSeek-V3"]
total = [175, 46.7, 671]
active = [175, 12.9, 37]

total_labels = ["175", "46.7", "671"]
active_labels = ["175 (100%)", "12.9 (28%)", "37 (5.5%)"]

fig = go.Figure()
fig.add_trace(
    go.Bar(name="Total parameters", x=models, y=total, text=total_labels,
           textposition="outside")
)
fig.add_trace(
    go.Bar(name="Active per token", x=models, y=active, text=active_labels,
           textposition="outside")
)
fig.update_layout(
    barmode="group",
    yaxis_title="Parameters (billions)",
    xaxis_title=None,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[0, 760])

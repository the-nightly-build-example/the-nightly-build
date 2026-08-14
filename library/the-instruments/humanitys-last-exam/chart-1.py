"""Humanity's Last Exam: no-tool accuracy over time, with two tool-assisted runs.

Data from the evidence record (primary numbers only), kept as two separate
series so the tool-assisted points are never merged into the no-tool line:

No-tool track (best reported no-tool score per date):
  2025-01  13.4  o3-mini (high), launch top score      [HLE paper, Table 1]
  2025-08  24.8  GPT-5, reasoning, no tools             [OpenAI via Vellum]
  2026-08  46.4  gemini-3.1-pro-preview, board 2026-08-14 [Scale/CAIS leaderboard]

With-tools points (browsing + Python tools, plotted separately):
  2025-02  26.6  deep research                          [reported by Fortune]
  2025-08  42.0  GPT-5 Pro                              [OpenAI via Vellum]
"""

import plotly.graph_objects as go

no_tool_dates = ["2025-01-01", "2025-08-01", "2026-08-14"]
no_tool_scores = [13.4, 24.8, 46.4]
no_tool_labels = ["o3-mini (high)", "GPT-5 (no tools)", "gemini-3.1-pro"]

tool_dates = ["2025-02-12", "2025-08-01"]
tool_scores = [26.6, 42.0]
tool_labels = ["deep research", "GPT-5 Pro"]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=no_tool_dates,
        y=no_tool_scores,
        mode="lines+markers+text",
        name="No tools (best model per date)",
        text=no_tool_labels,
        textposition=["bottom right", "bottom right", "top center"],
        cliponaxis=False,
    )
)

fig.add_trace(
    go.Scatter(
        x=tool_dates,
        y=tool_scores,
        mode="markers+text",
        name="With browsing + code tools",
        text=tool_labels,
        textposition="top left",
        marker=dict(symbol="diamond", size=12),
        cliponaxis=False,
    )
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="HLE accuracy (%)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    margin=dict(r=90),
)
fig.update_yaxes(range=[0, 55])

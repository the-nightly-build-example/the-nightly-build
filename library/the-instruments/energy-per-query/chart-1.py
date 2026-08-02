"""Five published Wh-per-query figures, one axis: same denominator (one
typical text/chat query), traced to each owning source (see the article's
Sources list and researcher/01/evidence.md § Numbers, "Energy per
query/prompt (Wh)"):

  - Google, "existing" boundary (measured, direct production telemetry,
    active-accelerator-only, top-10%-most-efficient data centers): 0.10 Wh,
    median Gemini Apps text prompt, May 2025. Elsworth et al., "Measuring
    the environmental impact of delivering AI at Google Scale" (Aug 2025),
    Table 1.
  - Google, "comprehensive" boundary (measured, same telemetry, full-stack
    fleet average including CPU/DRAM, idle machines, overhead): 0.24 Wh,
    same prompt, same month, same paper, same table -- only what counts
    changed.
  - Epoch AI (estimated, bottom-up: FLOPs/token x output tokens / chip
    throughput, with utilization and power-draw discounts): 0.29 Wh, typical
    GPT-4o ChatGPT query, 500 output tokens, Feb 2025.
  - Sam Altman blog, "The Gentle Singularity" (self-reported, no method,
    model, or boundary disclosed): 0.34 Wh, "average" ChatGPT query, June
    2025.
  - Alex de Vries, Joule (2023) (estimated, top-down: SemiAnalysis's assumed
    fleet power / assumed daily request volume): 2.9 Wh ("at most"),
    ChatGPT/GPT-3.5 request, early 2023 hardware and traffic assumptions.

Not on this axis: the 2009 Google-search figure (a different kind of query)
and the water figures (a different unit) -- see the article's prose.
"""

import plotly.graph_objects as go

measured_labels = ["Google<br>existing boundary", "Google<br>comprehensive boundary"]
measured_values = [0.10, 0.24]

estimated_labels = ["Epoch<br>estimate", "Altman<br>self-report", "de Vries<br>estimate"]
estimated_values = [0.29, 0.34, 2.9]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Measured (production telemetry)",
        x=measured_labels,
        y=measured_values,
        text=[f"{v:.2f} Wh" for v in measured_values],
        textposition="outside",
    )
)
fig.add_trace(
    go.Bar(
        name="Estimated or self-reported",
        x=estimated_labels,
        y=estimated_values,
        text=[f"{v:.2f} Wh" for v in estimated_values],
        textposition="outside",
    )
)
fig.update_layout(
    title="One typical chat query, five published prices",
    yaxis_title="Watt-hours per query",
    xaxis_title="Source (same denominator: one typical text query)",
    legend=dict(orientation="h", yanchor="bottom", y=-0.32, xanchor="center", x=0.5),
    margin=dict(t=90, b=110),
)

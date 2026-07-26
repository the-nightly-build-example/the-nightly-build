"""GPT-4's own ~298/400 Uniform Bar Exam score, held fixed, plotted against
four different reference populations.

Data source: Eric Martinez, "Re-evaluating GPT-4's Bar Exam Performance"
(Artificial Intelligence and Law, 2024; DOI:10.1007/s10506-024-09396-9),
Table 1, "Estimated Percentile of GPT-4's Uniform Bar Examination
Performance" (see article Sources list and research.md, Numbers section,
"The reference-population series").

  - "OpenAI/Katz's implied population" (the pre-2019 February Illinois Bar
    chart Katz et al.'s uncited footnote points to, per Martinez's own
    investigation, section 2.3): overall ~90th percentile; the underlying
    chart reports no separate essay-only figure.
  - July test-takers, all first-time test-takers, and licensed/license-
    pending attorneys (passers) are Martinez's own computed percentiles for
    GPT-4's actual score, Table 1: overall 68th / 62nd / 45th; essay-only
    (MEE+MPT) 48th / 42nd / 15th.

Table 1 gives 45th for the attorneys/overall cell; Martinez's own Abstract
and Discussion round this to "~48th" elsewhere in the same paper, an
inconsistency addressed in the article prose. This chart uses the table's
computed figure, 45, not the abstract's rounding.
"""

import plotly.graph_objects as go

labels = [
    "OpenAI/Katz's implied<br>population (pre-2019 Feb.<br>Illinois chart)",
    "July test-takers<br>(most recent full exam)",
    "All first-time<br>test-takers",
    "Licensed attorneys<br>(passed the exam)",
]
overall = [90, 68, 62, 45]
essay_only = [None, 48, 42, 15]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="UBE overall",
        x=labels,
        y=overall,
        text=[f"{v}th" for v in overall],
        textposition="outside",
    )
)
fig.add_trace(
    go.Bar(
        name="Essay only (MEE+MPT)",
        x=labels,
        y=essay_only,
        text=["n/a" if v is None else f"{v}th" for v in essay_only],
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="Percentile of the same ~298/400 UBE score",
    yaxis=dict(range=[0, 100]),
    barmode="group",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)

"""Reported HumanEval pass@1, by model and year.

Data, each figure owned by the primary source that reported it (see the
article's Sources list and research.md § Numbers, "Reported HumanEval
pass@1, by lab and year"):
  - Codex-12B 28.8% (2021) -- Chen et al. 2021, arXiv:2107.03374, Table 1.
  - GPT-4 67.0% (2023) -- OpenAI, GPT-4 Technical Report, arXiv:2303.08774,
    Table 2 / Table 11.
  - Claude 3 Opus 84.9% (2024) -- Anthropic, Claude 3 Model Card, Table 1.
  - GPT-4o 90.2% (2024) -- Meta AI, Llama 3 Herd of Models, arXiv:2407.21783,
    Table 18. Per Meta's stated methodology (Llama 3 Herd of Models §5.1.1),
    this is the best score across results publicly reported or, where
    possible, reproduced by Meta itself -- not a guaranteed fresh Meta run.
  - Claude 3.5 Sonnet 92.0% (2024) -- same source, same caveat, Table 18.
"""

import plotly.graph_objects as go

labels = [
    "Codex-12B<br>2021",
    "GPT-4<br>2023",
    "Claude 3 Opus<br>2024",
    "GPT-4o<br>2024*",
    "Claude 3.5 Sonnet<br>2024*",
]
pass_at_1 = [28.8, 67.0, 84.9, 90.2, 92.0]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Reported pass@1",
        x=labels,
        y=pass_at_1,
        text=[f"{v:.1f}%" for v in pass_at_1],
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="HumanEval pass@1 (%)",
    yaxis=dict(range=[0, 100]),
    showlegend=False,
    title="The same 164 problems, five models, three years",
)

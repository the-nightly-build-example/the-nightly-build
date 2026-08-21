"""Answer-only vs chain-of-thought accuracy on BIG-Bench Hard, averaged over
the 23 BBH tasks, against the two human-rater reference bars. All values from
the BBH paper (Suzgun et al., 2022), Table 2 (see the article's Sources list
and researcher/01/evidence.md, s3 and the Numbers section):

  - Codex (code-davinci-002): 56.6% answer-only, 73.9% chain-of-thought.
  - PaLM 540B: 52.3% answer-only, 65.2% chain-of-thought.
  - Average human-rater across the 23 tasks: 67.7% (mean over BIG-bench's
    expert-rater team).
  - Max human-rater across the 23 tasks: 94.4% (best single rater per task).

Both models are 3-shot. The reference lines are the two human numbers the
selection rule and the "beats the average human" claim rest on.
"""

import plotly.graph_objects as go

models = ["Codex", "PaLM 540B"]
answer_only = [56.6, 52.3]
chain_of_thought = [73.9, 65.2]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Answer-only (3-shot)",
        x=models,
        y=answer_only,
        text=[f"{v:.1f}%" for v in answer_only],
        textposition="outside",
    )
)
fig.add_trace(
    go.Bar(
        name="Chain-of-thought (3-shot)",
        x=models,
        y=chain_of_thought,
        text=[f"{v:.1f}%" for v in chain_of_thought],
        textposition="outside",
    )
)
fig.add_hline(
    y=67.7,
    line_dash="dot",
    annotation_text="average human-rater 67.7%",
    annotation_position="top left",
)
fig.add_hline(
    y=94.4,
    line_dash="dash",
    annotation_text="max human-rater 94.4%",
    annotation_position="top left",
)
fig.update_layout(
    title="Chain-of-thought against the human bar on BBH",
    yaxis_title="Accuracy, averaged over 23 BBH tasks (%)",
    xaxis_title="Model (3-shot prompting)",
    yaxis_range=[0, 100],
    barmode="group",
    legend=dict(orientation="h", yanchor="bottom", y=-0.28, xanchor="center", x=0.5),
    margin=dict(t=90, b=100),
)

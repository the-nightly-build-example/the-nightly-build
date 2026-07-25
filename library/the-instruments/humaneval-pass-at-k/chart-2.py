"""Injected training-data leakage vs. accuracy, Llama-3.2-1B, on HumanEval
(memorizable, static) and DyCodeEval (regenerated fresh each run).

Data from Chen et al., "Benchmarking Large Language Models Under Data
Contamination: A Survey from Static to Dynamic Evaluation," arXiv:2502.17521
(2025), Appendix A, Table 3. The authors fine-tuned Llama-3.2-1B with a
controlled, deliberately injected share of each benchmark's own problems
(0/25/50/75/100%) and re-scored the model on both benchmarks.
"""

import plotly.graph_objects as go

leakage = [0, 25, 50, 75, 100]
humaneval = [19, 29, 48, 68, 82]
dycodeeval = [14, 8, 8, 7, 11]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="HumanEval (static, public)",
        x=leakage,
        y=humaneval,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="DyCodeEval (regenerated each run)",
        x=leakage,
        y=dycodeeval,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="Injected training-data leakage (%)",
    yaxis_title="Llama-3.2-1B accuracy (%)",
    yaxis=dict(range=[0, 100]),
    xaxis=dict(tickmode="array", tickvals=leakage),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
)

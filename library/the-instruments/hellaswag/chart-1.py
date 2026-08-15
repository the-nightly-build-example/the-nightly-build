import plotly.graph_objects as go

# Two anchored HellaSwag measurements against the human baseline.
# 2019: BERT-Large, best model at launch, 47.3% (HellaSwag paper, arXiv 1905.07830).
# 2023: GPT-4, ten-shot, 95.3% (GPT-4 Technical Report, arXiv 2303.08774).
# Human baseline: 95.6% overall (HellaSwag paper).
years = ["2019", "2023"]
best_model = [47.3, 95.3]
human = 95.6

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Best model (BERT-Large, then GPT-4)",
        x=years,
        y=best_model,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="Human baseline 95.6%",
        x=years,
        y=[human, human],
        mode="lines",
    )
)
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="HellaSwag accuracy (%)",
    xaxis_type="category",
)
fig.update_yaxes(range=[0, 100])

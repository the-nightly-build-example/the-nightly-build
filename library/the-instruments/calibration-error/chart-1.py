import plotly.graph_objects as go

# Illustrative reliability diagram, NOT from any source's data. The bins are the
# constructed 100-prediction, 5-bin classifier used in this article's worked
# example (built to match Guo et al. 2017, Eq. 3): every bin's accuracy sits
# below its confidence, the overconfidence pattern Guo report for a deep network.
# conf = mean stated confidence in the bin; acc = fraction actually correct.
conf = [0.10, 0.30, 0.50, 0.70, 0.95]
acc = [0.00, 0.20, 0.40, 0.60, 0.80]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Accuracy in the bin",
        x=conf,
        y=acc,
        width=0.16,
    )
)
fig.add_trace(
    go.Scatter(
        name="Perfect calibration",
        x=[0, 1],
        y=[0, 1],
        mode="lines",
        line=dict(dash="dash"),
    )
)
fig.update_layout(
    xaxis_title="Confidence (the model's stated probability)",
    yaxis_title="Accuracy (fraction actually correct)",
    xaxis=dict(range=[0, 1]),
    yaxis=dict(range=[0, 1]),
)

import plotly.graph_objects as go

# Multi-document QA accuracy by the position of the single answer-bearing
# document among 20 documents. Data from Liu et al. 2023, Appendix G Table 6.
position = ["1st", "5th", "10th", "15th", "20th"]
gpt35 = [75.8, 57.2, 53.8, 55.4, 63.2]
claude13 = [59.9, 55.9, 56.8, 57.2, 60.1]

fig = go.Figure()
fig.add_trace(go.Scatter(name="GPT-3.5-Turbo", x=position, y=gpt35, mode="lines+markers"))
fig.add_trace(go.Scatter(name="Claude-1.3", x=position, y=claude13, mode="lines+markers"))
fig.update_layout(
    xaxis_title="Position of the answer document (of 20)",
    yaxis_title="Accuracy (%)",
)
fig.update_yaxes(range=[45, 80])

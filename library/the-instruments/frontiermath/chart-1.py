import plotly.graph_objects as go

# Three FrontierMath results that circulated under the name "o3".
# Sources (see article Sources list):
#   Prior frontier models: under 2%  -- Epoch AI (FrontierMath paper; benchmark page)
#   OpenAI o3 preview claim, 20 Dec 2024: 25.2%  -- OpenAI announcement
#   Released o3, re-tested independently by Epoch, Apr 2025: ~10%  -- Epoch / TechCrunch
labels = [
    "Prior frontier models<br>(pre-o3)",
    "OpenAI o3 preview<br>(Dec 2024 claim)",
    "Released o3<br>(Epoch independent)",
]
scores = [2, 25.2, 10]
text = ["under 2%", "25.2%", "about 10%"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=labels,
        y=scores,
        text=text,
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="FrontierMath problems solved (%)",
    showlegend=False,
)
fig.update_yaxes(range=[0, 30])

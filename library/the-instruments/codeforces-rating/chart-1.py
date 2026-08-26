import plotly.graph_objects as go

# Estimated Codeforces ratings quoted for AI systems, with their source and
# conditions. All are estimates fit to placements in contests the systems did
# not enter live:
#   - AlphaCode 1238: Li et al., "Competition-Level Code Generation with
#     AlphaCode" (arxiv 2203.07814), estimated from 10 finished contests.
#   - GPT-4o / o1-preview / o1 / o1-ioi / o1-ioi (full strategy) / o3: OpenAI,
#     "Competitive Programming with Large Reasoning Models" (arxiv 2502.06807),
#     estimated from simulated contests.
# o1 and o1-ioi are the same base model: 1673 on its own, 2214 once the full
# hand-built test-time strategy is wrapped around it. Ordered by rating.
models = [
    "GPT-4o",
    "AlphaCode",
    "o1-preview",
    "o1",
    "o1-ioi",
    "o1-ioi (full)",
    "o3",
]
rating = [808, 1238, 1258, 1673, 1807, 2214, 2724]
labels = [str(r) for r in rating]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=rating,
        y=models,
        orientation="h",
        text=labels,
        textposition="outside",
        cliponaxis=False,
    )
)

# Codeforces title thresholds (as posted in 2013) that a reader can place each
# number against: Pupil, Expert, Grandmaster.
for x, name in [(1200, "Pupil"), (1600, "Expert"), (2400, "Grandmaster")]:
    fig.add_vline(x=x, line_dash="dot", line_width=1)
    fig.add_annotation(
        x=x, y=6.6, text=name, showarrow=False, yshift=6, font=dict(size=12)
    )

fig.update_layout(
    xaxis_title="Estimated Codeforces rating (from simulated or reconstructed contests)",
    yaxis_title="",
)
fig.update_yaxes(autorange="reversed")
fig.update_xaxes(range=[0, 2950])

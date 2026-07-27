import plotly.graph_objects as go

# GSM8K -> GSM-Symbolic accuracy drop (percentage points), renaming only:
# only the names and numbers inside each problem template were changed; the
# reasoning steps required did not change. Full ranked list from Mirzadeh et
# al., "GSM-Symbolic," arXiv:2410.05229, Fig. 3 / Sec. 4.1.
models = [
    "Mistral-7b-it-v0.1",
    "Gemma2-2b",
    "Gemma2-2b-it",
    "Gemma2-9b",
    "Gemma2-9b-it",
    "Mistral-7b-it-v0.3",
    "Mathstral-7b-v0.1",
    "Phi-3-medium",
    "Phi-3-small",
    "Gemma2b",
    "Gemma2b-it",
    "Gemma-7b-it",
    "Mistral-7b-v0.1",
    "Phi-3-mini",
    "Phi-3.5-mini-it",
    "GPT-4o-mini",
    "o1-preview",
    "Gemma2-27b-it",
    "Llama3-8b-it",
    "Mistral-7b-v0.3",
    "o1-mini",
    "GPT-4o",
]
drops = [
    -9.2, -7.4, -7.4, -6.2, -6.2, -6.2, -6.1, -4.8, -4.8, -3.9, -3.9, -3.7,
    -3.4, -3.0, -2.8, -2.4, -2.2, -1.4, -1.3, -0.7, -0.6, -0.3,
]

# Plot largest drop at top: reverse so Plotly (bottom-to-top y-axis) renders
# the largest-magnitude drop at the top of the chart.
models_r = list(reversed(models))
drops_r = list(reversed(drops))

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=drops_r,
        y=models_r,
        orientation="h",
        name="Accuracy drop",
    )
)
fig.update_layout(
    xaxis_title="GSM8K → GSM-Symbolic accuracy drop (percentage points)",
    yaxis=dict(tickfont=dict(size=11)),
    height=620,
    margin=dict(l=170),
)

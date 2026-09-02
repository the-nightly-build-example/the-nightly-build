import plotly.graph_objects as go

# T2I-CompBench++ numeracy score (0-1, detection-based via UniDet: does the
# image contain the requested count of the named object, 1-8 objects per
# prompt) for five text-to-image models spanning two generations. Figures are
# the paper's own reported scores, read via the HTML mirror (ar5iv) since the
# arXiv PDF endpoint returned undecodable binary; treated here as approximate,
# per the researcher's transcription-risk note, and labeled accordingly.
#   Huang et al., "T2I-CompBench++", arxiv.org/abs/2307.06350, numeracy table.
models = ["Stable Diffusion 1.4", "Stable Diffusion 2", "DALL-E 3", "Stable Diffusion 3", "FLUX.1"]
score = [0.45, 0.46, 0.59, 0.62, 0.62]
labels = ["~0.45", "~0.46", "~0.59", "~0.62", "~0.62"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=models,
        y=score,
        text=labels,
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Numeracy score, 0-1 (approximate; higher is better)",
    xaxis_title="Model (left to right, earlier to later release)",
    yaxis_range=[0, 0.8],
)

import plotly.graph_objects as go

# Amortized latency per token, Shazeer's baseline setup (TPUv2, batch of
# 1024 sequences, source length 128 / target length 128 tokens).
# Source: Shazeer 2019, "Fast Transformer Decoding: One Write-Head is All
# You Need" (arXiv:1911.02150), Section 4, Experimental Results.
stages = [
    "Prompt reading<br>(parallel)",
    "Sequential decoding<br>(no cache fix)",
    "Sequential decoding<br>(multi-query fix)",
]
latency_us = [1.7, 46, 3.8]

fig = go.Figure()
fig.add_trace(go.Bar(x=stages, y=latency_us))
fig.update_layout(
    yaxis_title="Microseconds per token (amortized)",
)

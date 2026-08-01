import plotly.graph_objects as go

# GCG transfer attack success rate (ASR), by target model and attack
# condition. Suffixes were optimized only against open-weight Vicuna and
# Guanaco, then fired blind at these five closed models. Zou, Wang, Carlini,
# Nasr, Kolter, Fredrikson, "Universal and Transferable Adversarial Attacks
# on Aligned Language Models," arXiv:2307.15043, Table 2.
conditions = [
    "Behavior only",
    "+ “Sure, here's”",
    "+ single suffix (Vicuna)",
    "+ single suffix (Vicuna & Guanaco)",
    "+ ensemble of suffixes",
]
models = ["GPT-3.5", "GPT-4", "PaLM-2", "Claude-1", "Claude-2"]

# rows follow `models` order; columns follow `conditions` order.
asr = [
    [1.8, 5.7, 34.3, 47.4, 86.6],   # GPT-3.5
    [8.0, 13.1, 34.5, 29.1, 46.9],  # GPT-4
    [0.0, 0.0, 31.7, 36.1, 66.0],   # PaLM-2
    [0.0, 0.0, 2.6, 37.6, 47.9],    # Claude-1
    [0.0, 0.0, 0.0, 1.8, 2.1],      # Claude-2
]

fig = go.Figure(
    data=go.Heatmap(
        z=asr,
        x=conditions,
        y=models,
        colorscale="Reds",
        zmin=0,
        zmax=100,
        text=[[f"{v:.1f}%" for v in row] for row in asr],
        texttemplate="%{text}",
        textfont=dict(size=12),
        colorbar=dict(title="ASR"),
        xgap=3,
        ygap=3,
    )
)
fig.update_layout(
    xaxis_title="attack condition, weakest to strongest (left to right)",
    yaxis_title=None,
    height=430,
    margin=dict(l=90, b=90),
)

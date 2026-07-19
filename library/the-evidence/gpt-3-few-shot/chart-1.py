import plotly.graph_objects as go

# Few-shot GPT-3 175B minus the prior fine-tuned state of the art, in each
# benchmark's own 0-100 metric (accuracy or F1). Read from Brown et al. (2020),
# Tables 3.2, 3.3, 3.5, 3.6, 3.7, 3.8. Translation (BLEU) is left out so every
# bar shares a 0-100 scale. PIQA carries the paper's own contamination
# asterisk. Positive means few-shot beats the fine-tuned record.
rows = [
    ("LAMBADA", 86.4 - 68.0),
    ("PIQA *", 82.8 - 79.4),
    ("TriviaQA", 71.2 - 68.0),
    ("CoQA", 85.0 - 90.7),
    ("Winogrande", 77.7 - 84.6),
    ("Natural Questions", 29.9 - 44.5),
    ("SuperGLUE (avg)", 71.8 - 89.0),
    ("SQuAD 2.0", 69.8 - 93.0),
    ("WiC", 49.4 - 76.1),
    ("ARC-Challenge", 51.5 - 78.5),
    ("QuAC", 44.3 - 74.4),
    ("RACE-h", 46.8 - 90.0),
    ("DROP", 36.5 - 89.1),
]
rows.sort(key=lambda r: r[1], reverse=True)
labels = [r[0] for r in rows]
gaps = [round(r[1], 1) for r in rows]

win = "#008a74"
loss = "#a8332e"
colors = [win if g >= 0 else loss for g in gaps]

fig = go.Figure(
    go.Bar(
        x=gaps,
        y=labels,
        orientation="h",
        marker_color=colors,
        text=[f"{g:+.1f}" for g in gaps],
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    xaxis_title="Few-shot GPT-3 175B minus prior fine-tuned SOTA (points)",
    showlegend=False,
    margin=dict(l=180, r=70, t=30, b=70),
)
fig.update_yaxes(autorange="reversed")
fig.update_xaxes(zeroline=True, zerolinewidth=2, range=[-60, 30])

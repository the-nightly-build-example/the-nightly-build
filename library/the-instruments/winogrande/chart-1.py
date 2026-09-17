import plotly.graph_objects as go

# WinoGrande paper (Sakaguchi et al. 2019/2020), Table 4: RoBERTa test accuracy
# on the same filtered WinoGrande set, trained on training splits of growing size.
training_examples = [160, 640, 2558, 10234, 40938]
test_accuracy = [50.4, 58.6, 67.6, 74.7, 79.1]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="RoBERTa on WinoGrande",
        x=training_examples,
        y=test_accuracy,
        mode="lines+markers+text",
        text=[f"{a:.1f}%" for a in test_accuracy],
        textposition="top center",
    )
)
fig.add_hline(
    y=94.0,
    line_dash="dot",
    annotation_text="Human 94.0%",
    annotation_position="top right",
)
fig.update_xaxes(type="log", title_text="Training examples (log scale)")
fig.update_yaxes(title_text="Test accuracy (%)", range=[45, 100])
fig.update_layout(
    title_text="Same questions, different training budgets",
    showlegend=False,
)

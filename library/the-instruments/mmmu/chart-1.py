import plotly.graph_objects as go

# Four flagships' own headline MMMU (validation) score beside their MMMU-Pro
# scores, all read from one table so the protocol is constant across every bar.
# Source: MMMU-Pro paper (Yue et al., 2024), Table 1 -- "Results of models on
# MMMU-Pro and MMMU (Val)". Standard is the ten-option setting; Vision is the
# screenshot setting that feeds the model no separate text.
models = ["GPT-4o", "Claude 3.5 Sonnet", "Gemini 1.5 Pro", "Qwen2-VL-72B"]
mmmu_val = [69.1, 68.3, 62.2, 64.5]
pro_standard = [54.0, 55.0, 46.5, 49.2]
pro_vision = [49.7, 48.0, 40.5, 43.3]

fig = go.Figure()
fig.add_trace(go.Bar(name="MMMU (Val)", x=models, y=mmmu_val,
                     text=[f"{v:.1f}" for v in mmmu_val], textposition="outside"))
fig.add_trace(go.Bar(name="MMMU-Pro, ten options", x=models, y=pro_standard,
                     text=[f"{v:.1f}" for v in pro_standard], textposition="outside"))
fig.add_trace(go.Bar(name="MMMU-Pro, vision-only", x=models, y=pro_vision,
                     text=[f"{v:.1f}" for v in pro_vision], textposition="outside"))
fig.update_layout(
    barmode="group",
    yaxis_title="Accuracy (%)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[0, 80])

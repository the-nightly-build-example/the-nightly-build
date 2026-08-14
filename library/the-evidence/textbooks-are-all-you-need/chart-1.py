import plotly.graph_objects as go

# HumanEval pass@1 on the NON-SIMILAR problems only, after retraining phi-1
# with matching CodeExercises removed, at four similarity thresholds.
# Source: arXiv:2306.11644, Table 3. Lower tau prunes more aggressively.
thresholds = ["τ = 0.95", "τ = 0.90", "τ = 0.85", "τ = 0.80"]
retrained_phi1 = [32.3, 36.6, 34.5, 27.1]
starcoder = [29.0, 32.4, 31.0, 31.2]

fig = go.Figure()
fig.add_trace(go.Bar(name="retrained phi-1 (1.3B)", x=thresholds, y=retrained_phi1))
fig.add_trace(go.Bar(name="StarCoder-Prompted (15.5B)", x=thresholds, y=starcoder))
fig.update_layout(
    barmode="group",
    yaxis_title="pass@1 on non-similar HumanEval (%)",
    xaxis_title="similarity threshold τ (lower prunes more aggressively)",
)
fig.update_yaxes(range=[0, 40])

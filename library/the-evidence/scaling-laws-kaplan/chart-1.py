import plotly.graph_objects as go

# Exponents from N_opt ∝ C^a (model size) and D_opt ∝ C^b (training data),
# as a fixed compute budget C grows. Kaplan et al. 2020, Eq. 6.1-6.2 (Section
# 6.1); Hoffmann et al. 2022 (Chinchilla), Table 2, three independently fit
# approaches (Sections 3.1-3.3).
fits = [
    "Kaplan\n(2020)",
    "Chinchilla\ntraining curves",
    "Chinchilla\nIsoFLOP profiles",
    "Chinchilla\nparametric fit",
]
model_exponent_a = [0.73, 0.50, 0.49, 0.46]
data_exponent_b = [0.27, 0.50, 0.51, 0.54]

fig = go.Figure()
fig.add_trace(go.Bar(name="model size, a", x=fits, y=model_exponent_a))
fig.add_trace(go.Bar(name="training data, b", x=fits, y=data_exponent_b))
fig.add_hline(y=0.5, line_dash="dot", annotation_text="equal split (a = b = 0.5)")
fig.update_layout(
    barmode="group",
    yaxis_title="fitted exponent (share of compute growth)",
    yaxis_range=[0, 0.85],
)

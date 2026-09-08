"""The Epic Sepsis Model's one deployed operating point on the ROC square.

Source: Wong A, et al. External Validation of a Widely Implemented Proprietary
Sepsis Prediction Model in Hospitalized Patients. JAMA Intern Med. 2021.
At the deployed alert threshold (ESM score >= 6):
  sensitivity = 33%  -> true-positive rate y = 0.33
  specificity = 83%  -> false-positive rate x = 1 - 0.83 = 0.17
The chance diagonal (y = x) is definitional, not fabricated data.
Wong reports this single operating point and one summary AUROC (0.63); the
curve's coordinates are not published, so no curve is drawn here.
"""

import plotly.graph_objects as go

# Deployed operating point (the only ROC coordinate Wong publishes).
point_x = [0.17]  # false-positive rate = 1 - specificity (0.83)
point_y = [0.33]  # sensitivity (true-positive rate)

fig = go.Figure()

# Chance diagonal: a model no better than a coin toss.
fig.add_trace(
    go.Scatter(
        name="Chance (AUROC 0.5)",
        x=[0, 1],
        y=[0, 1],
        mode="lines",
        line=dict(dash="dash"),
    )
)

# The one point the deployment actually runs at.
fig.add_trace(
    go.Scatter(
        name="Deployed alarm (score ≥ 6)",
        x=point_x,
        y=point_y,
        mode="markers+text",
        text=["0.17, 0.33"],
        textposition="bottom right",
        marker=dict(size=14),
    )
)

fig.update_layout(
    xaxis_title="False-positive rate (1 − specificity)",
    yaxis_title="Sensitivity (true-positive rate)",
)
fig.update_xaxes(range=[0, 1], constrain="domain")
fig.update_yaxes(range=[0, 1], scaleanchor="x", scaleratio=1)

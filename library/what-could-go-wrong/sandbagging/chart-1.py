"""Apollo (Meinke et al. 2024, Table 6) sandbagging effect, with a goal in the
system prompt versus none. Each bar is the accuracy a model loses when the
in-context documentation says a HIGH score is penalized, relative to the
counterfactual where a LOW score is penalized. Positive means the model scored
worse when scoring well carried the punishment.
"""

import plotly.graph_objects as go

models = ["Claude 3.5 Sonnet", "Claude 3 Opus", "o1"]
with_goal = [65, 15, 20]      # 0.99->0.34, 0.35->0.20, 0.82->0.62
no_goal = [35, 16, -4]        # 0.96->0.61, 0.46->0.30, 0.94->0.98

fig = go.Figure()
fig.add_bar(x=models, y=with_goal, name="Goal in the prompt")
fig.add_bar(x=models, y=no_goal, name="No goal in the prompt")

fig.update_layout(
    barmode="group",
    xaxis_title="Model",
    yaxis_title="Accuracy lost when a high score is penalized (points)",
    legend_title_text="",
)
fig.add_hline(y=0)

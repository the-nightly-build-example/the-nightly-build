import plotly.graph_objects as go

# Elo ratings from a single 100-game, 2-hour-time-control tournament run by
# DeepMind to compare all four named AlphaGo systems on one scale.
# Source: Silver et al. 2017 (AlphaGo Zero, Nature 550:354-359), p. 12,
# "Final Elo comparison" passage in the evidence record.
systems = ["AlphaGo Fan", "AlphaGo Lee", "AlphaGo Master", "AlphaGo Zero"]
elo = [3144, 3739, 4858, 5185]
dates = ["beat Fan Hui, Oct 2015", "beat Lee Sedol, Mar 2016", "online only, late 2016", "no human data, 2017"]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=systems,
        y=elo,
        mode="lines+markers+text",
        text=[f"{v:,}" for v in elo],
        textposition="top center",
        marker=dict(size=12),
        line=dict(width=3),
        customdata=dates,
        hovertemplate="%{x}<br>Elo %{y:,}<br>%{customdata}<extra></extra>",
    )
)
fig.update_layout(
    yaxis_title="Elo rating (interval scale, no true zero; same tournament, 2-hour time controls)",
    xaxis_title=None,
)
fig.update_yaxes(range=[2900, 5450])

import plotly.graph_objects as go

# Nvidia (NVDA) closing price, raw close, around the 27 Jan 2025 selloff.
# Source: stockanalysis.com daily OHLC history, corroborated by statmuse.com.
dates = ["Fri Jan 24", "Mon Jan 27"]
closes = [142.62, 118.42]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=dates,
        y=closes,
        text=[f"${v:,.2f}" for v in closes],
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="NVDA close (US$)",
    yaxis_range=[0, 160],
)

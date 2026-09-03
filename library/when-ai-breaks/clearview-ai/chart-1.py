# Clearview AI's scraped database, as counted by regulators and courts, 2021-2024.
# Each figure is the count reported on that date by a named authority, drawn from
# the evidence record:
#   3 billion  - OAIC determination, 3 Nov 2021 ("more than three billion images")
#   10 billion - Italian Garante, decision Feb 2022 ("over 10 billion faces")
#   20 billion - UK First-tier Tribunal [2023] UKFTT 819, para 40 (Oct 2022 estimate)
#   30 billion - Dutch DPA, decision 16 May 2024 ("more than 30 billion photos")
#
# The four points are drawn as discrete bars, not a connected line: the chart
# asserts nothing about the dates between them, only the four counts each source
# actually reported. Later self-reported company figures (40-50 billion) are
# Clearview's own unverified claims and are deliberately left off.
import plotly.graph_objects as go

dates = ["Nov 2021", "Feb 2022", "Oct 2022", "May 2024"]
billions = [3, 10, 20, 30]
labels = ["3 billion", "10 billion", "20 billion", "30 billion"]
owners = ["OAIC", "Garante", "UK tribunal", "Dutch DPA"]
xlabels = [f"{d}<br>{o}" for d, o in zip(dates, owners)]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=xlabels,
        y=billions,
        text=labels,
        textposition="outside",
        name="Images in the database",
    )
)
fig.update_layout(
    xaxis_title="Date the count was reported, and by whom",
    yaxis_title="Images in the database (billions)",
    showlegend=False,
)
fig.update_yaxes(range=[0, 34])

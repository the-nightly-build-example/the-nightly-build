import plotly.graph_objects as go

# GSM8K solve rate (%), standard prompting vs chain-of-thought, by PaLM size.
# Source: Wei et al. 2022 (arXiv:2201.11903), Table 2 (Appendix B).
sizes = ["PaLM 8B", "PaLM 62B", "PaLM 540B"]
standard = [4.9, 9.6, 17.9]
cot = [4.1, 29.9, 56.9]

fig = go.Figure()
fig.add_trace(go.Bar(name="Standard prompting", x=sizes, y=standard))
fig.add_trace(go.Bar(name="Chain-of-thought prompting", x=sizes, y=cot))
fig.update_layout(
    barmode="group",
    yaxis_title="GSM8K solve rate (%)",
    xaxis_title="Model size (parameters)",
)
fig.update_yaxes(range=[0, 60])

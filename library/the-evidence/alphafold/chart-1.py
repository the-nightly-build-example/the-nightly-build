import plotly.graph_objects as go

# Median CASP14 prediction error in ångströms (r.m.s.d.95), lower is better.
# Source: Jumper et al., Nature 2021 (Abstract and opening Main paragraph).
measures = ["Backbone (Cα)", "All atoms"]
alphafold = [0.96, 1.5]
next_best = [2.8, 3.5]

fig = go.Figure()
fig.add_trace(go.Bar(name="AlphaFold", x=measures, y=alphafold))
fig.add_trace(go.Bar(name="Next-best CASP14 method", x=measures, y=next_best))
fig.update_layout(
    barmode="group",
    yaxis_title="Median error (Å r.m.s.d.95)",
    xaxis_title="What is measured",
)

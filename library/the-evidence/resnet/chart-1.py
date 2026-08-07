import plotly.graph_objects as go

# ImageNet-2012 validation top-1 error (%), 10-crop testing.
# Source: He, Zhang, Ren & Sun, "Deep Residual Learning for Image
# Recognition" (arXiv:1512.03385), Table 2. The residual nets carry no
# extra parameters over their plain counterparts.
depth = ["18 layers", "34 layers"]
plain = [27.94, 28.54]
residual = [27.88, 25.03]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Plain network",
        x=depth,
        y=plain,
        text=[f"{v:.2f}" for v in plain],
        textposition="outside",
    )
)
fig.add_trace(
    go.Bar(
        name="Residual network",
        x=depth,
        y=residual,
        text=[f"{v:.2f}" for v in residual],
        textposition="outside",
    )
)
fig.update_layout(
    barmode="group",
    yaxis_title="ImageNet top-1 validation error (%)",
    xaxis_title="Network depth",
)
fig.update_yaxes(range=[0, 31])

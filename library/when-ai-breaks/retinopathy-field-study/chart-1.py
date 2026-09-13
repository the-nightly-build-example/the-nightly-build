import plotly.graph_objects as go

# The double fact this lesson turns on. Two different quantities share the
# percent axis, kept in separate traces so the share of ungraded images is
# never folded into an accuracy figure.
#
# Diagnostic accuracy for vision-threatening diabetic retinopathy, measured in
# the field against an adjudicated reference standard:
#   AI system         94.7%   (Ruamviboonsuk et al. 2022, Lancet Digital Health)
#   Retina specialist 93.5%   (the over-readers in the same cohort)
# Share of real clinic images the system refused to grade at all:
#   21% (393 of 1,838), first six months across the three Pathum Thani clinics
#   (Beede et al. 2020, CHI, "Gradability").
accuracy_x = ["AI system", "Retina specialists"]
accuracy_y = [94.7, 93.5]
accuracy_text = ["94.7%", "93.5%"]

ungradable_x = ["First six months"]
ungradable_y = [21.0]
ungradable_text = ["21%"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Field accuracy, vision-threatening DR",
        x=accuracy_x,
        y=accuracy_y,
        text=accuracy_text,
        textposition="outside",
        cliponaxis=False,
    )
)
fig.add_trace(
    go.Bar(
        name="Share of images the system would not grade",
        x=ungradable_x,
        y=ungradable_y,
        text=ungradable_text,
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Percent",
    yaxis_range=[0, 100],
    barmode="group",
)

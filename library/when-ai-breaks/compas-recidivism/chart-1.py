import plotly.graph_objects as go

# Broward County, Florida, defendants scored on COMPAS's General Recidivism
# Risk Scale, 2013-2014. "Reoffended within two years" is the base
# recidivism rate for each group. "Wrongly rated high risk" is the false
# positive rate: among defendants who did NOT reoffend, the share COMPAS
# scored "Not Low." "Wrongly rated low risk" is the false negative rate:
# among defendants who DID reoffend, the share COMPAS scored "Low."
# Source: research.md sources 3 (base rate, cross-confirmed by Chouldechova
# 2017) and 2/"How We Analyzed the COMPAS Recidivism Algorithm" (error rates).
categories = [
    "Reoffended within<br>two years",
    "Wrongly rated<br>high risk",
    "Wrongly rated<br>low risk",
]
black = [51, 44.85, 27.99]
white = [39, 23.45, 47.72]

fig = go.Figure()
fig.add_trace(go.Bar(name="Black defendants", x=categories, y=black))
fig.add_trace(go.Bar(name="White defendants", x=categories, y=white))
fig.update_layout(
    barmode="group",
    yaxis_title="Percent",
    yaxis_ticksuffix="%",
)

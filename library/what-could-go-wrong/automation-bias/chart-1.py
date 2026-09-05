import plotly.graph_objects as go

# Where a prescribing decision-support system moved general practitioners'
# decisions. 26 GPs each prescribed for 20 validated scenarios (520 decisions).
# The system's advice was correct 70% of the time. Decision accuracy without the
# aid was 50.4%; with it, 58.3%. Inside that net gain, the advice moved 13.1% of
# decisions from wrong to right and 5.2% from right to wrong (automation bias
# measured directly). 50.4 + 13.1 - 5.2 = 58.3. Figures are the study's own.
#   Goddard, "Automation Bias and Prescribing Decision Support," PhD thesis,
#   City University London, 2012. openaccess.city.ac.uk/id/eprint/3005/
labels = ["Doctors alone", "Advice helped", "Advice misled", "Doctors with advice"]
measure = ["absolute", "relative", "relative", "total"]
values = [50.4, 13.1, -5.2, 58.3]
text = ["50.4%", "+13.1", "-5.2", "58.3%"]

fig = go.Figure()
fig.add_trace(
    go.Waterfall(
        x=labels,
        measure=measure,
        y=values,
        text=text,
        textposition="outside",
        connector={"line": {"width": 1}},
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Correct prescriptions (% of 520 decisions)",
    xaxis_title="",
    yaxis_range=[0, 70],
    showlegend=False,
)

import plotly.graph_objects as go

# England, A-level entries, all ages, summer 2020. Percent of centre
# assessment grades (CAGs) adjusted DOWN by at least one grade once Ofqual's
# standardisation model ran, by centre type, before the 17 August 2020
# reversal. Candidate counts (n) are printed in each category label so a
# reader can see which rows rest on the fewest students.
# Source: research.md source 3, Ofqual, "Summer 2020 results analysis -
# GCSE, AS and A level" (17 Dec 2020), Table 6, p.10. The 39.1% national
# figure (source 2/3) is drawn as a reference line.
centre_types = [
    "Independent<br>(n=98,966)",
    "Tertiary College<br>(n=19,606)",
    "Secondary Modern<br>(n=4,469)",
    "Free Schools<br>(n=9,389)",
    "Secondary Selective<br>(n=31,239)",
    "Academy<br>(n=297,547)",
    "Sixth Form College<br>(n=119,048)",
    "Sec Comp or Middle<br>(n=106,614)",
    "FE Establishment<br>(n=23,352)",
]
pct_down = [33.8, 34.7, 34.5, 38.9, 39.1, 39.7, 39.8, 41.2, 45.6]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=pct_down,
        y=centre_types,
        orientation="h",
        name="% of A-level CAGs adjusted down",
    )
)
fig.add_vline(
    x=39.1,
    line_dash="dash",
    annotation_text="All centres: 39.1%",
    annotation_position="top",
)
fig.update_layout(
    xaxis_title="Percent of A-level grades adjusted down at least one grade",
    showlegend=False,
    margin=dict(l=190, r=10, t=40, b=60),
)
fig.update_xaxes(ticksuffix="%")

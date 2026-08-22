import plotly.graph_objects as go

# Best (winning) ILSVRC top-5 error rate per year, 2010-2015, in percent.
# 2010-2014 winning entries and the 5.1% human figure are from Russakovsky
# et al. 2015 (arXiv:1409.0575), Tables 6-7 and Sec 6.4.1; the 2015 winning
# entry (ResNet, 3.57%) is from He et al. 2015 (arXiv:1512.03385, Abstract).
# The ~6% label-error band is the human-validated outright-error rate in the
# 50,000-image validation set from Northcutt et al. 2021 (arXiv:2103.14749,
# 2,916/50,000 = 5.83%, rounded to 6%). Winning entry per year: 2010 NEC,
# 2011 XRCE, 2012 AlexNet (15.3% test), 2013 Clarifai, 2014 GoogLeNet,
# 2015 ResNet.
years = ["2010", "2011", "2012", "2013", "2014", "2015"]
top5_error = [28.2, 25.8, 15.3, 11.7, 6.66, 3.57]
labels = ["28.2", "25.8", "15.3", "11.7", "6.66", "3.57"]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Winning top-5 error",
        x=years,
        y=top5_error,
        mode="lines+markers+text",
        text=labels,
        textposition="top center",
        cliponaxis=False,
    )
)

# Reference bands the curve falls into by 2015.
fig.add_hline(
    y=6.0,
    line_dash="dot",
    annotation_text="Validation label errors: ~6%",
    annotation_position="top left",
)
fig.add_hline(
    y=5.1,
    line_dash="dash",
    annotation_text="Human annotator: 5.1%",
    annotation_position="bottom left",
)

fig.update_layout(
    yaxis_title="Top-5 error (%)",
    xaxis_title="ILSVRC year",
)
fig.update_yaxes(range=[0, 30])

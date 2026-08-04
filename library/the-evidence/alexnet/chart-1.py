# Winning top-5 error at the ImageNet challenge (ILSVRC), three benchmark years.
# Data: Russakovsky et al., ImageNet Large Scale Visual Recognition Challenge
# (arXiv:1409.0575), section 6.1.1 and Figure 9; the 2012 point is AlexNet's
# winning entry (15.3%), cross-checked to Krizhevsky et al. (2012). The paper
# reports a 4.2x reduction across the challenge's first five years, from 28.2%
# (2010) to 6.7% (2014).
#
# Only the three contests the evidence record verifies exactly are plotted, and
# they are drawn as discrete bars, not a connected line: the chart asserts
# nothing about the 2011 and 2013 contests it does not show, so it cannot
# flatten AlexNet's 2012 break into a false continuous slope.
import plotly.graph_objects as go

years = ["2010", "2012", "2014"]
top5_error = [28.2, 15.3, 6.7]
labels = ["28.2%", "15.3%", "6.7%"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=years,
        y=top5_error,
        text=labels,
        textposition="outside",
        name="Winning top-5 error",
    )
)
fig.update_layout(
    xaxis_title="ILSVRC year (contests shown, not every year)",
    yaxis_title="Winning top-5 error (%)",
    showlegend=False,
)
fig.update_yaxes(range=[0, 34])
fig.add_annotation(
    x="2012",
    y=12.5,
    text="AlexNet",
    showarrow=True,
    arrowhead=2,
    ax=48,
    ay=-70,
)

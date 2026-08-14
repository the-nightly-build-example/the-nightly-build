import plotly.graph_objects as go

# LMSYS Chatbot Arena style-control coefficients, with BOTH answer length and
# markdown controlled, from the style-control analysis:
#   lmsys.org/blog/2024-08-28-style-control (Results coefficient table).
# The four style features are fit alongside content in the arena rating model;
# the values are normalized, unitless regression coefficients (not win-rate
# percentage points). Length is far the largest; the three markdown features
# are small once length is held fixed. For contrast, when length is left FREE
# and only markdown is controlled, the lists coefficient rises to 0.111 -- the
# entanglement noted in the caption and body, not plotted here.
features = ["Answer length", "Lists", "Headers", "Bold"]
coefficient = [0.249, 0.031, 0.024, 0.019]
labels = ["0.249", "0.031", "0.024", "0.019"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=features,
        y=coefficient,
        text=labels,
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Normalized style coefficient (both length and markdown controlled)",
    xaxis_title="Style feature in the arena rating model",
)

import plotly.graph_objects as go

# Delivery skew across identically-targeted, identically-budgeted Facebook
# job ads. Each bar is a figure the authors report directly (not a derived
# complement): the share of the delivered audience matching the stated
# gender or race, for five stock-photo image variants of the same job ad,
# aggregated per job category, on one fixed custom audience (99% Agresti-
# Coull confidence intervals; job ads also checked against Bonferroni
# correction for the 55-way comparison, appendix Fig. 10).
# Source: Ali, Sapiezynski, Bogen, Rieke, Korolova, Mislove, "Discrimination
# through optimization: How Facebook's ad delivery can lead to skewed
# outcomes" (arXiv:1904.02095), Introduction and Fig. 8.
categories = [
    "Lumber ads → men",
    "Cashier ads → women",
    "Taxi ads → Black users",
    "Janitor ads → Black users",
    "Lumber ads → white users",
    "Janitor ads → women",
]
shares = [90, 85, 75, 75, 72, 65]

fig = go.Figure()
fig.add_trace(go.Bar(x=shares, y=categories, orientation="h"))
fig.update_layout(
    xaxis_title="Share of the delivered audience (%)",
    yaxis_title=None,
    margin={"l": 230},
)
fig.update_xaxes(range=[0, 100])
fig.update_yaxes(autorange="reversed")

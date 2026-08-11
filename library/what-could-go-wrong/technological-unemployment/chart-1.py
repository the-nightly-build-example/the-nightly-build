import plotly.graph_objects as go

# The same US economy, measured two ways, as the share of employment at
# "high risk" of automation (an automation probability above 70%).
# Occupation-based: Frey & Osborne score whole occupations and put 47% of
# US employment in the high-risk band. Task-based: Arntz, Gregory & Zierahn
# (OECD) score the tasks workers actually do, weighted to individual
# workers, and the US figure falls to 9%.
# Sources: Frey & Osborne, "The Future of Employment" (2013), 47%;
# Arntz, Gregory & Zierahn, "The Risk of Automation for Jobs in OECD
# Countries," OECD Working Paper No. 189 (2016), US 9%.
methods = ["Whole occupations<br>(Frey & Osborne, 2013)",
           "Tasks within occupations<br>(OECD, 2016)"]
high_risk_share = [47, 9]

fig = go.Figure()
fig.add_trace(go.Bar(x=methods, y=high_risk_share,
                     text=["47%", "9%"], textposition="outside"))
fig.update_layout(
    yaxis_title="Share of US employment at high risk (%)",
    xaxis_title="How the same economy was scored",
)
fig.update_yaxes(range=[0, 55])

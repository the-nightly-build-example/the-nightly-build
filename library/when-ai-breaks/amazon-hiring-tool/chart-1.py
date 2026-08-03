import plotly.graph_objects as go

# University of Washington study (Wilson & Caliskan, AAAI/ACM AIES 2024;
# UW News, Oct. 31, 2024). Three open-source LLMs screened 550+ real resumes
# with 120 names associated with white and Black men and women across nine
# occupations, 3M+ paired comparisons. Each value is the share of comparisons
# in which a name group was the one favored. Race pair: white 85 vs Black 9.
# Gender pair: male 52 vs female 11. Reported percentages, rebuilt here.
groups = [
    "White-<br>associated",
    "Black-<br>associated",
    "Male-<br>associated",
    "Female-<br>associated",
]
favored = [85, 9, 52, 11]

fig = go.Figure()
fig.add_trace(go.Bar(x=groups, y=favored))
fig.update_layout(
    yaxis_title="Favored",
    yaxis_ticksuffix="%",
    yaxis_range=[0, 100],
    showlegend=False,
)

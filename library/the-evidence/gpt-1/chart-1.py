import plotly.graph_objects as go

# Absolute point gain over the prior best reported for each dataset, in the
# metric the paper reports for that dataset (GPT-1 paper, Abstract and Sec. 4.2,
# Tables 2-3). Ordered largest to smallest to show the spread.
datasets = ["Story Cloze", "QNLI", "RACE", "SciTail", "MNLI", "SNLI"]
gains = [8.9, 5.8, 5.7, 5.0, 1.5, 0.6]

fig = go.Figure()
fig.add_trace(go.Bar(x=datasets, y=gains, text=gains, textposition="outside"))
fig.update_layout(
    yaxis_title="Gain over prior best (points)",
    xaxis_title="Dataset",
    showlegend=False,
)
fig.update_yaxes(range=[0, 10])

import plotly.graph_objects as go

# BERT-base ablation, dev-set scores, across three training configurations.
# "No NSP": next-sentence prediction removed, bidirectional reading kept.
# "LTR & No NSP": next-sentence prediction removed AND reading restricted to
# left-to-right only (no bidirectionality).
# Source: Devlin et al. 2018 (arXiv:1810.04805), Table 5, Section 5.1.
tasks = ["MNLI-m", "QNLI", "MRPC", "SST-2", "SQuAD F1"]
full_model = [84.4, 88.4, 86.7, 92.7, 88.5]
no_nsp = [83.9, 84.9, 86.5, 92.6, 87.9]
ltr_no_nsp = [82.1, 84.3, 77.5, 92.1, 77.8]

fig = go.Figure()
fig.add_trace(go.Bar(name="Full model", x=tasks, y=full_model))
fig.add_trace(go.Bar(name="No NSP", x=tasks, y=no_nsp))
fig.add_trace(go.Bar(name="LTR & No NSP (unidirectional)", x=tasks, y=ltr_no_nsp))
fig.update_layout(
    barmode="group",
    yaxis_title="Dev-set score",
    xaxis_title="Task",
)
fig.update_yaxes(range=[70, 95])

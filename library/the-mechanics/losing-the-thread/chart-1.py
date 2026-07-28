import plotly.graph_objects as go

# Multi-document QA accuracy by the position of the document holding the
# answer, GPT-3.5-Turbo (16K), 20-document and 30-document settings. Both
# settings fit well inside the model's 16,000-token window.
# Source: Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang, "Lost in
# the Middle: How Language Models Use Long Contexts" (arXiv:2307.03172),
# multi-document QA results.
positions = ["Start", "Middle", "End"]
acc_20docs = [75.8, 53.8, 63.2]
acc_30docs = [73.4, 50.5, 63.7]

# The same model's accuracy with no documents supplied at all (closed-book).
closed_book = 56.1

fig = go.Figure()
fig.add_trace(go.Bar(name="20 documents", x=positions, y=acc_20docs))
fig.add_trace(go.Bar(name="30 documents", x=positions, y=acc_30docs))
fig.add_hline(
    y=closed_book,
    line_dash="dash",
    annotation_text="No documents at all (closed-book): 56.1%",
    annotation_position="top left",
)
fig.update_layout(
    yaxis_title="Accuracy answering the question (%)",
    xaxis_title="Position of the document holding the answer",
    barmode="group",
)

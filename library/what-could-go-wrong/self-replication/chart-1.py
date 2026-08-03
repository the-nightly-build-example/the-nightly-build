import plotly.graph_objects as go

# Source: Pan et al., Fudan University, "Frontier AI systems have surpassed the
# self-replicating red line" (arXiv:2412.12140), Fig. 4. Ten trials per model.
# Three logged behaviors, as a percentage of the ten trials.
behaviors = ["Agrees to replicate", "Knows how to replicate", "Creates a live copy"]
qwen = [100, 100, 90]   # Qwen2.5-72B-Instruct: 10/10, 10/10, 9/10
llama = [100, 70, 50]   # Llama3.1-70B-Instruct: 10/10, 7/10, 5/10

fig = go.Figure()
fig.add_trace(go.Bar(name="Qwen2.5-72B-Instruct", x=behaviors, y=qwen))
fig.add_trace(go.Bar(name="Llama3.1-70B-Instruct", x=behaviors, y=llama))
fig.update_layout(
    barmode="group",
    yaxis_title="Percentage of 10 trials",
)
fig.update_yaxes(range=[0, 100])

"""Throughput vs. latency policy, same model, three audited platforms.

Source: MLCommons, MLPerf Inference v5.1 results (raw results file),
filtered to Model=="llama2-70b-99", Category=="closed",
Availability=="available", grouped by (Submitter, Platform).
https://raw.githubusercontent.com/mlcommons/inference_results_v5.1/main/summary_results.json

Same model (Llama 2 70B) and same hardware per platform; only the latency
policy differs. Offline has no latency bound (the system batches as much
as it can). Server requires 200 ms per output token (a floor of 5
tokens/sec reaching any one user). Interactive requires 40 ms per output
token (a floor of 25 tokens/sec per user). All figures are aggregate
throughput across the full accelerator count named. Three of the
evidence record's 20 matched platforms are shown for readability, chosen
to span the reported 32-66% Server-to-Interactive drop: Nebius B200x8
(41.3% drop), Nebius H200x8 (32.2% drop, the smallest in the record), and
AMD 8xMI300X (64.1% drop, near the largest).
"""

import plotly.graph_objects as go

platforms = ["Nebius, B200x8", "Nebius, H200x8", "AMD, 8xMI300X"]
offline = [101246.0, 34812.1, 27803.9]
server = [101611.0, 34029.4, 24593.8]
interactive = [59622.7, 23079.9, 8840.4]

fig = go.Figure()
fig.add_trace(go.Bar(name="Offline (no latency bound)", x=platforms, y=offline))
fig.add_trace(go.Bar(name="Server (200 ms/token)", x=platforms, y=server))
fig.add_trace(
    go.Bar(name="Interactive (40 ms/token)", x=platforms, y=interactive)
)
fig.update_layout(
    barmode="group",
    xaxis_title="Platform (same model, Llama 2 70B, per platform)",
    yaxis_title="Throughput (tokens/sec, aggregate)",
)

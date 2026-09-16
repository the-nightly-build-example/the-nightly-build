import plotly.graph_objects as go

# FlashAttention paper (arXiv:2205.14135), Appendix E.6, Table 21.
# "Memory usage (MB) ... by sequence length": combined forward+backward pass,
# no dropout/no masking, 8 heads, head dim 64, batch 16, one A100 (40GB).
seq_len_flash = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
flash_mb = [22, 44, 104, 209, 418, 836, 1672, 3344, 6688, 13376]

# Same table's "PyTorch Attention" column: out of memory beyond seq. 4096.
seq_len_standard = [128, 256, 512, 1024, 2048, 4096]
standard_mb = [36, 104, 336, 1184, 4416, 17024]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Standard attention",
        x=seq_len_standard,
        y=standard_mb,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="FlashAttention",
        x=seq_len_flash,
        y=flash_mb,
        mode="lines+markers",
    )
)
fig.update_xaxes(title_text="sequence length, tokens (log scale)", type="log")
fig.update_yaxes(title_text="memory, MB (log scale)", type="log")

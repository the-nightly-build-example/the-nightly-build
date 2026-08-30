import plotly.graph_objects as go

# How often OpenAI's gpt-4.1 returned each number when asked, 10,000 times, for
# a random integer between 1 and 100 (Responses API, temperature 1.0, a fixed
# system prompt, a unique uuid4 per call). A uniform generator would return each
# number about 100 times; the dashed line marks that expectation. The full 1-100
# axis is kept on purpose: every multiple of 10 except 10 was returned exactly 0
# times, and 69 was returned only 29 times, both part of the finding.
# Source: exmergo, "research-chatgpt-guesses-between-1-and-100" (MIT license),
# data/processed/distribution.csv.
numbers = list(range(1, 101))
counts = [
    0, 1, 2, 1, 0, 0, 5, 1, 2, 1,       # 1-10
    8, 56, 87, 83, 4, 25, 182, 42, 44, 0,   # 11-20
    7, 31, 90, 48, 5, 54, 350, 87, 94, 0,   # 21-30
    4, 73, 13, 109, 12, 146, 404, 120, 45, 0,  # 31-40
    46, 401, 207, 53, 18, 155, 526, 81, 46, 0,  # 41-50
    9, 127, 269, 196, 6, 225, 457, 133, 61, 0,  # 51-60
    28, 294, 286, 302, 13, 12, 391, 106, 29, 0,  # 61-70
    17, 415, 343, 313, 12, 143, 115, 93, 92, 0,  # 71-80
    13, 179, 156, 267, 15, 145, 337, 30, 35, 0,  # 81-90
    17, 221, 84, 107, 2, 23, 98, 14, 1, 0,   # 91-100
]

fig = go.Figure()
fig.add_trace(go.Bar(name="Times returned", x=numbers, y=counts))
fig.add_hline(
    y=100,
    line_dash="dash",
    annotation_text="A uniform generator: about 100 each",
    annotation_position="top right",
)
fig.update_layout(
    yaxis_title="Times returned out of 10,000 calls",
    xaxis_title="Number returned (1 to 100)",
    showlegend=False,
)

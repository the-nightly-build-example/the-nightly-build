import plotly.graph_objects as go

# Tokens needed to encode the same paragraph -- Article 1 of the Universal
# Declaration of Human Rights -- in each of 13 languages, under the cl100k_base
# tokenizer used by ChatGPT and GPT-4. English is the baseline at 33 tokens;
# every other language costs more, and the non-Latin low-resource scripts cost
# many times more. Reproduced firsthand with tiktoken 0.13.0:
#   text  = <article number="1"> paragraph from udhr_<key>.xml,
#           github.com/unicode-org/udhr (whitespace collapsed)
#   count = len(tiktoken.get_encoding("cl100k_base").encode(text))
# Multipliers vs English follow each count in the label.
languages = [
    "English", "Spanish", "German", "French", "Chinese", "Russian",
    "Korean", "Arabic", "Japanese", "Hindi", "Telugu", "Amharic", "Burmese",
]
tokens = [33, 44, 44, 50, 50, 74, 85, 88, 93, 182, 281, 305, 512]
multiplier = ["1.0x", "1.3x", "1.3x", "1.5x", "1.5x", "2.2x",
              "2.6x", "2.7x", "2.8x", "5.5x", "8.5x", "9.2x", "15.5x"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=languages,
        y=tokens,
        text=multiplier,
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Tokens for the same paragraph (UDHR Article 1)",
    xaxis_title="Language of the paragraph (English = 33 tokens)",
)

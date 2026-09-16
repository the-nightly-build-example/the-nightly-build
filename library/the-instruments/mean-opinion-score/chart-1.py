import plotly.graph_objects as go

# Mean Opinion Score reported for genuine human recordings -- not synthetic
# speech -- across seven listening tests run by five different research
# groups, 2018-2022. None of these is the "same" recording under test twice
# except the two Blizzard 2013 points (original 44.1kHz vs a 16kHz downsampled
# re-test of the identical audio). The other five split across two more
# corpora: one paper's own single-speaker studio corpus, and four papers all
# using the public LJSpeech recordings, but in four different test batches.
#   Le Maguer, King & Harte, "Back to the Future: Extending the Blizzard
#     Challenge 2013," Interspeech 2022, Table 1 (Blizzard 2013 points)
#   Shen et al., "Natural TTS Synthesis by Conditioning WaveNet on Mel
#     Spectrogram Predictions" (Tacotron 2), ICASSP 2018, Table 1
#   Hayashi et al., "ESPnet-TTS," ICASSP 2020, Table 5
#   Tan et al., "NaturalSpeech," 2022, Table 1 and Table 2
#   Li, Han & Mesgarani, "StyleTTS," 2022, Table I

points = [
    ("Blizzard 2013<br>original test", 4.74, "Blizzard 2013 corpus"),
    ("Tacotron 2<br>2018", 4.58, "a single studio corpus"),
    ("ESPnet-TTS<br>2020", 4.46, "LJSpeech"),
    ("Blizzard 2013<br>2021 re-test", 4.39, "Blizzard 2013 corpus"),
    ("NaturalSpeech<br>2022, Table 1", 4.52, "LJSpeech"),
    ("NaturalSpeech<br>2022, Table 2", 4.58, "LJSpeech"),
    ("StyleTTS<br>2022", 4.32, "LJSpeech"),
]

groups = ["Blizzard 2013 corpus", "a single studio corpus", "LJSpeech"]

fig = go.Figure()
for group in groups:
    xs = [label for label, _, corpus in points if corpus == group]
    ys = [score for _, score, corpus in points if corpus == group]
    fig.add_trace(
        go.Bar(
            name=group,
            x=xs,
            y=ys,
            text=[f"{y:.2f}" for y in ys],
            textposition="outside",
            cliponaxis=False,
        )
    )

fig.update_layout(
    xaxis=dict(
        categoryorder="array",
        categoryarray=[label for label, _, _ in points],
        tickangle=0,
    ),
    yaxis_title="MOS given to the human recordings (1-5 ACR scale)",
    xaxis_title="Paper and the year its listening test ran",
    yaxis_range=[1, 5],
    legend_title_text="Which recordings",
    margin=dict(b=120),
)

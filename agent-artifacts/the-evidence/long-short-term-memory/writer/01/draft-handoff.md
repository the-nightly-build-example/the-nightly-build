# draft-handoff: the-evidence/long-short-term-memory (01)

## Original-work sentence
This lesson pulls apart the two things a citation of "LSTM" silently merges: the
compact, synthetic, two-gate demonstration the 1997 paper actually contains, and
the larger three-gate machine that later groups built and ran, so a reader can
see which one any given claim rests on.

## Proof result
`nb check .../long-short-term-memory.html --series the-evidence --repo .` (links
included): BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp` written: words
2199, reading_minutes 10, sources 8. No warning left standing.

## How the angle was held
- Scale, not strength: the piece credits the 1997 result as strong and genuinely
  new within its scope (solved >1,000-step long-lag tasks nothing else could) and
  shows the small scale beside it (synthetic tasks, 93 to ~6,000 weights, largest
  ~10,500, two to four memory cells). It never implies the paper was weak, and it
  states that the small scale was the authors' deliberate choice. The "never
  measured what it is famous for" dek mold was avoided; the paper did demonstrate
  what it is famous for.
- Corrections honoured: the forget gate is attributed to Gers, Schmidhuber &
  Cummins 2000 ("Learning to Forget") and marked as absent from the 1997 model.
  It is sourced to the xLSTM paper (s3), which attributes it to Gers, plus the
  1997 paper's own silence (s1); no firsthand quote from the paywalled 2000 paper
  is used, and that paper is not in the source list. The 2013 real-speech result
  is attributed to Graves, Mohamed & Hinton (Toronto), with Schmidhuber not an
  author; the 2005 TIMIT result is Graves & Schmidhuber.
- Taught-ground links, not re-teaching: backpropagation and gradient-descent are
  linked in Background and at first mention in prose; seq2seq and word-embeddings
  are plain prose links where the present-day section leans on them.

## Furniture
Two components, each built only from the record and where it beats prose: a source
asset (Figure 1 of the 1997 paper, captured with `nb asset pdf` from the cited
PDF, cropped to the memory cell, its self-loop of weight 1.0, and both gates, with
no forget gate) in the mechanism section; and a table of the paper's experiments
and their whole-network weight counts in the scale section. A timeline carries the
1997-to-2024 arc in the present section.

## Open question
The Gers, Schmidhuber & Cummins 2000 forget-gate paper could not be opened
firsthand (paywalled), per the researcher's record. The forget gate's origin,
date, and purpose are carried by corroborating primaries (xLSTM 2024, and the 1997
paper's silence); if the desk wants a firsthand citation of the 2000 paper's own
wording, new evidence would be needed. No other gap; nothing blocks handoff.

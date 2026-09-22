# Commission: the-evidence/long-short-term-memory

## The assignment
Read the paper that introduced Long Short-Term Memory: Sepp Hochreiter and
Jürgen Schmidhuber, "Long Short-Term Memory," *Neural Computation* 9(8), 1997
(and the 1995/1996 technical-report versions where they differ). This desk reads
one famous AI document and tells the reader what it actually says. Do that for
LSTM.

The reader should leave knowing: what problem the paper set out to solve (why
plain recurrent networks could not learn to connect events far apart in a
sequence), what the paper actually built to solve it (the constant error
carousel and the gate units that protect a stored value), and how large the
evidence in the paper really was (the experiments are small, synthetic sequence
tasks, not natural-language or real-world benchmarks). Then bring it to the
present: LSTM ran production speech recognition and machine translation through
the mid-2010s, transformers then displaced it for large language models, and the
architecture is still used and was revisited in 2024 (xLSTM). Say plainly where
today's citations of LSTM match what the 1997 paper showed and where they run
ahead of it.

## The one-sentence contribution this article owes
State, from the document itself, how modest the 1997 evidence was — synthetic
tasks with tiny networks — against how load-free the reputation is, and settle
what the paper did and did not demonstrate. (The writer states its own
original-work sentence in draft-handoff; this is the commissioned angle, not that
sentence.)

## Boundaries and what not to re-teach
- The vanishing-gradient problem is the heart of this lesson: teach it here from
  the document (Hochreiter's 1991 diploma thesis and the 1997 paper's analysis).
  Do not assume the reader knows it.
- Backpropagation and gradient descent are taught. Link the library's
  `the-evidence/backpropagation` and `the-mechanics/gradient-descent` in
  Background instead of re-teaching them; use them in prose with a plain link at
  first mention, not a numbered source.
- Recurrent networks, sequence models and word embeddings appear across the
  library (`the-mechanics/word-embeddings`, `the-evidence/seq2seq`). Link, do not
  re-teach.
- This is the document desk, not the mechanics desk: keep the lesson on what the
  paper claimed and showed, not a general tutorial on how RNNs work today.
- No code (the series does not forbid it, but the lesson template and this paper
  are better served by prose and one diagram/table). A small worked example of a
  gate holding a value across time steps is welcome as prose or a table.

## Source obligations (resolved)
`nb source-policy --series the-evidence`: minimum 6 sources; at least 3 primary,
at least 1 secondary. Primary here means the documents that own the claim: the
1997 *Neural Computation* paper, the 1995/1996 tech-report version, Hochreiter's
1991 thesis (vanishing gradients), Gers/Schmidhuber/Cummins 2000 (the forget
gate, added later — the 1997 paper has no forget gate), Graves & Schmidhuber
2005/2013 (LSTM on real speech), Sutskever/Vinyals/Le 2014 (seq2seq with LSTM),
and the 2024 xLSTM paper (Beck et al.). Secondary: reputable history/coverage for
context only, never for a number. Read the paper's own experiment sections for
the network sizes, task definitions, and success criteria.

## Production record (resolved)
`nb production-policy --series the-evidence`: profile balanced. researcher effort
high / model capable; writer effort medium / model capable; editor effort high /
model capable; writing-coach effort low / model capable. None required. Runtime
uses the most capable available model for each role; record the actual model in
`nb-meta` and any deviation here. No `required` directive to trade down.

## Tonight's neighbours (one paper, no overlap)
Four other lessons publish tonight. Do not cover their ground.
- the-instruments/helm — how a holistic benchmark leaderboard is built.
- the-mechanics/answer-length-bias — why chatbot answers run long.
- what-could-go-wrong/responsibility-gap — accountability for autonomous-system harm.
- when-ai-breaks/iruda-chatbot — a 2021 chatbot privacy/toxicity failure.
This lesson is the only historical-architecture piece; keep it there.

## Recent shapes and habits to break (from the last ~2 weeks of this desk)
- Do not reuse the "the paper never measured/reports the thing it is famous for"
  dek mold (wavenet, imagenet used it). Only make that claim if the document
  literally supports it.
- Avoid the two-sentence dek whose second sentence reverses the first with a
  bare "actually/still" (brier-score, comet-score, backpropagation lean on it).
- Avoid comma-triad headings closed with "and" ("Six wins, nine losses, one
  benchmark with no comparison"). Build each heading differently.
- Recent openers lead with a single hard number as the surprise. That is fine,
  but find this lesson's own surprise (e.g. the size of the 1997 experiments, or
  the gap between the 1997 model and the LSTM people mean today) rather than
  echoing the neighbour's cadence.

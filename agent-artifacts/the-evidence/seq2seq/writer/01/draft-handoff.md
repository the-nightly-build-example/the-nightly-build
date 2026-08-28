# Draft handoff: the-evidence/seq2seq (writer 01)

## Original-work statement
The article turns the evidence record's flat list of numbers and its four
Contradictions into one argument that separates the durable encoder-decoder idea
from the single fixed vector the paper never conceded, and it reassigns the
bottleneck diagnosis off seq2seq and onto the same-month Bahdanau and Cho papers
where the record shows it actually belongs.

## Proof result
`./nb check .nb-work/the-evidence/seq2seq/library/the-evidence/seq2seq.html --series the-evidence`
(links included): **BLOCK: 0, WARN: 0** — PUBLISHABLE.

- No warnings left standing. Three W-SENTENCE-DENSITY notes from the first pass
  were resolved by splitting quote-bearing long sentences (Bahdanau conjecture,
  Cho measurement, the T5 recipe line) and the orientation opener; every verbatim
  quotation was preserved intact across the splits.
- The proof prints one informational line, `library state not provided
  (--library); open-mode dedupe and commission checks skipped`. That is expected
  in the writer workspace (no full library checkout here); it is not a warning.
  The PR-time proof runs those library checks.

## Corrected-angle compliance (for the editor's audit)
- The piece never says seq2seq conceded the fixed-vector bottleneck. It quotes
  the paper's opposite claim ("We were surprised to discover that the LSTM did
  well on long sentences," Section 3.7) in the note, and attributes the
  bottleneck diagnosis to Bahdanau et al. (1409.0473) and the measured long-
  sentence degradation to Cho et al. (1409.1259), noting the latter was measured
  on a single-layer model without reversing, not on Sutskever's system.
- 34.81 is stated as reversing + 5-model ensemble + beam 12; the single reversed
  model (30.59), the SMT baseline (33.30), and the SMT-rescoring number (36.5)
  are each labelled distinctly, in prose and in the Table 1 furniture.
- Reversing: perplexity 5.8→4.7, BLEU 25.9→30.6, with the paper's own "no
  complete explanation" candor and the narrow-vs-broad admission the record's
  Contradiction 3 calls for.

## Open continuity question for the orchestrator/editor
The body prose link and Background row point to
`../the-evidence/attention-is-all-you-need.html` for what removed the bottleneck,
per the brief and commission ("already published in this library"). The writer
workspace library holds only this article, so I could not verify the published
filename/slug resolves; internal prose links are not probed by `nb check`. Please
confirm the attention-is-all-you-need lesson's path matches at PR time. I did not
link `the-mechanics/word-order` (brief marked it "if useful"): reversing is about
source-token order for the encoder, not linguistic word order, so the link would
mislead more than help.

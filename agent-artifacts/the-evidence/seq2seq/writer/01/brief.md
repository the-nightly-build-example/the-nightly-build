# writer brief: the-evidence/seq2seq (01)

Inputs:
- editorial-direction.md   (house standard, paper voice, series prompt, template identity)
- writing-coach/01/voice-guide.md   (how this piece should sound; read before drafting)
- researcher/01/evidence.md   (the complete claim set; read its Contradictions closely)
- the initialized article at library/the-evidence/seq2seq.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-evidence/seq2seq/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/seq2seq/library/the-evidence/seq2seq.html --series the-evidence

Corrected angle — read before you outline (the research changed it):
The seq2seq paper does NOT concede the fixed-length-vector bottleneck. It claims
the OPPOSITE for its own model — the authors were "surprised" the LSTM did well on
long sentences and report no degradation up to ~35 words (Section 3.7). So do NOT
write that seq2seq admitted or worried about the bottleneck. The honest lineage:
(1) seq2seq compressed a whole sentence into one fixed-length vector and showed it
worked, even claiming it held on long sentences; (2) the fixed-vector bottleneck
was named by Bahdanau, Cho, and Bengio (arXiv:1409.0473) and measured by Cho et
al. (arXiv:1409.1259) on the BASIC single-layer RNN encoder-decoder (no
reversing), both the same month, not on Sutskever's deep reversed LSTM; (3)
attention then removed the single vector, a line that runs to the Transformer
(already published in this library as the-evidence/attention-is-all-you-need).
Attribute the bottleneck diagnosis to those attention papers, not to seq2seq.

Numbers to use exactly (from the record):
- Headline WMT'14 En->Fr BLEU 34.81 is reversing + a 5-model ENSEMBLE + beam 12.
  Reversing a single model alone gives 30.59; SMT-rescoring gives 36.5; the SMT
  baseline is 33.30. Be precise about which number is which — do not present
  34.81 as a bare single-model result.
- The reversing-the-source trick: perplexity 5.8 -> 4.7, BLEU 25.9 -> 30.6. The
  paper offers "no complete explanation" (Section 3.3) — say so; do not invent one.
- Scale: 4 layers, 1000 cells and 1000-dim embeddings, ~384M parameters; 12M
  sentence-pair WMT'14 En-Fr subset; 160k source / 80k target vocab caps; 8 GPUs,
  ~10 days.
- Only one language pair (WMT'14 En-Fr) — this is what qualifies the sweeping way
  "sequence to sequence" is invoked today.

Continuity: link the-evidence/attention-is-all-you-need for what removed the
bottleneck; do not re-derive LSTMs from scratch (teach only encode->vector->decode
as far as the reader needs). Center the DOCUMENT. No verdict block in the body;
the takeaway lands the judgment.

Recent shapes in The Evidence to break: avoid the "[Subject] [verb] [surprising
quantified result]" mold by reflex; avoid banned dek molds (comma-triad, semicolon
reversal, suspended question) and the comma-plus-"and" heading join.

nb-meta you own: date 2026-08-28; harness "Claude Code"; model "claude-opus-4-8".

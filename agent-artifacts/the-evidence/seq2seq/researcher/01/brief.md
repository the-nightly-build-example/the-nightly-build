# researcher brief: the-evidence/seq2seq (01)

Inputs:
- editorial-direction.md  (citation standard, the-evidence territory, declared reader)

Output: agent-artifacts/the-evidence/seq2seq/researcher/01/evidence.md

The document under examination: Sutskever, Vinyals, Le, "Sequence to Sequence
Learning with Neural Networks" (arXiv:1409.3215; NeurIPS 2014). Read the paper
itself and cite to it.

Research questions the evidence record must answer, each traced to the paper's own
text (give section/table locators):
- What the paper actually did: the architecture (a deep LSTM encoder reading the
  source into a fixed-length vector; a deep LSTM decoder generating the target;
  beam-search decoding), and the exact task — WMT'14 English-to-French.
- The headline numbers as the paper reports them: the BLEU it achieved directly
  with the LSTM/ensemble, and the BLEU from rescoring the baseline SMT system's
  n-best (1000-best) list. Give both and say which is which.
- The reported scale: number of LSTM layers, hidden/embedding dimensions, total
  parameters, the size of the training subset (sentence pairs / vocabulary caps),
  hardware (how many GPUs), and training time.
- The reversing-the-source-sentence trick: what it is, and the exact BLEU/
  perplexity improvement the paper attributes to it. This is a key honest-scale
  detail.
- The fixed-length-vector bottleneck: how the paper frames encoding a whole
  sentence into one vector, and any limitation it acknowledges.
- The afterlife, from primary sources: the attention mechanism that removed the
  bottleneck (Bahdanau, Cho et al., 2014-2015 — read the paper[s] that own the
  claim) and, as already published in this paper's library, the Transformer.
  Confirm each "superseded/fixed" claim against the document that owns it; do not
  assert a lineage you cannot source.
- At least one clear example of how seq2seq / encoder-decoder is invoked today in
  a way the 2014 paper's actual result qualifies.

Search for what breaks the angle: if the paper's result was broader than one
language pair, or if the reversing trick was less important than the commission
assumes, record it in Contradictions in full.

Source policy: at least 6 sources, at least 3 primary, at least 1 secondary.
Classify each by authorship and stake and say why. Confirm every URL resolves to
the document's own page. Preserve any numeric series a chart could use.

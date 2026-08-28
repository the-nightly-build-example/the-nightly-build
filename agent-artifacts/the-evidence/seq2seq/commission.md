# Commission: the-evidence/seq2seq

## The document
Ilya Sutskever, Oriol Vinyals, and Quoc V. Le, "Sequence to Sequence Learning
with Neural Networks" (Google), NeurIPS 2014 (arXiv:1409.3215). The paper that
established the encoder-decoder framing — map a variable-length input sequence to
a variable-length output sequence with neural networks — that every later
translation and language model inherited.

## Why this document, now
The Evidence has already read the Transformer ("attention-is-all-you-need") and
several model papers. seq2seq is the document those stand on: the 2014 result
that showed a plain recurrent network could do machine translation end to end,
and named the problem shape the field has used ever since. Reading it lets the
reader see where "encoder-decoder" came from and how small and specific the
original result was. The honest-scale angle is sharp: this is a single-language-
pair translation result from a 4-layer LSTM, and it leaned on a hack (reversing
the input word order) that a better idea made obsolete within months.

## The angle (what it did, its scale, then its afterlife)
State plainly what the paper did: a deep LSTM read an English sentence into one
fixed-length vector, and a second deep LSTM generated the French translation from
that vector, decoded with beam search. Report the real numbers from the paper —
the WMT'14 English-to-French BLEU it reached directly and by rescoring the
statistical baseline's n-best list, the model size (layers, dimensions,
parameters), the training data subset, the hardware and days of training. Show
the honest scale: one language pair, a bounded dataset, a single architecture.
Give the reversing-the-source-sentence trick its due — the paper reports it
bought several BLEU points — as a concrete sign of how much the fixed-vector
bottleneck strained the approach. Then the afterlife: the encoder-decoder framing
and the seq2seq problem formulation held and spread; the fixed-length-vector
bottleneck did NOT — it was the paper's central limitation, and the attention
mechanism (Bahdanau, Cho, and colleagues, within months) removed the bottleneck
and made the reversing trick unnecessary, a line that runs straight to the
Transformer. Say plainly what today's "seq2seq is the basis of modern NLP"
invocation credits to this paper versus what later documents actually delivered.

## Boundaries and continuity
This is The Evidence: claims come from the paper itself (arXiv v3 / NeurIPS
camera-ready), not coverage. The reader has already been taught, in published
lessons, that self-attention replaced recurrence: link the-evidence/
attention-is-all-you-need for what superseded the fixed-vector bottleneck, and
the-mechanics/word-order if useful, rather than re-teaching attention here. Do
not re-derive LSTMs from scratch — teach only what the reader needs to follow
what the paper did (an encoder that compresses a sentence to a vector, a decoder
that unrolls it). Center the DOCUMENT. No verdict block in the body; the takeaway
lands the judgment.

## Template, furniture, policy
- Template: lesson. Stat strip fits the honest-scale figures (BLEU, params,
  layers, training days). A small numbered-steps or table component could show
  the encode->vector->decode pipeline if it aids the reader. Use only what the
  evidence verifies. Do not let furniture crowd the reporting.
- Source policy: >=6 sources, >=3 primary, >=1 secondary. Primary = the paper and
  other primary documents (the attention paper[s] that fixed the bottleneck, the
  contemporaneous Cho et al. encoder-decoder paper, the WMT'14 task). Secondary =
  reporting/context.
- Production policy (balanced): researcher high/capable, coach low/capable,
  writer medium/capable, editor high/capable. No `required` directives.

## Recent shapes in this series to break
Recent The Evidence headlines run "[Subject] [verb] [surprising quantified
result]." Do not reach for that mold by reflex. Avoid the banned dek molds
(comma-triad, semicolon reversal, suspended question) and the comma-plus-"and"
heading join.

## What this article must add
The reader should be able to say what the 2014 seq2seq paper actually did (an
LSTM translation result at a stated scale, with a telling hack), and distinguish
the durable idea it contributed (encoder-decoder / the seq2seq problem shape)
from the bottleneck a later idea had to remove.

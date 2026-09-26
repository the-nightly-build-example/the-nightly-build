# Commission: the-evidence/align-and-translate

## The document

Bahdanau, Dzmitry; Cho, Kyunghyun; Bengio, Yoshua. "Neural Machine
Translation by Jointly Learning to Align and Translate." First posted to
arXiv September 2014 (arXiv:1409.0473), presented at ICLR 2015. This desk
reads one famous AI document; this is the document.

## The assignment

Teach what this paper actually did and why it is now cited as the origin of
the attention mechanism. Cover, in the desk's order:

1. What the document is, who wrote it, and the problem it set out to solve.
   The standard 2014 encoder-decoder for translation squeezed a whole source
   sentence into a single fixed-length vector, then generated the translation
   from that one vector. The paper's claim is that this fixed-length
   bottleneck is what caps quality, especially on long sentences.
2. What it did: the method. The model (the authors call it RNNsearch) lets the
   decoder, at each output word, compute a set of weights over all the encoder
   positions and read a different weighted combination of the source
   representations for each target word. That weighting is the "alignment"
   /"soft attention." Explain the mechanism in plain words at the altitude a
   smart newcomer needs; do not derive it as math unless one small equation
   genuinely teaches faster than prose (at most one, and only if the evidence
   record supplies the exact form).
3. The scale and the numbers, honestly. The training data (WMT'14
   English-to-French, the specific corpus size the paper reports), the model
   size and vocabulary limit, and the BLEU results: RNNsearch vs the fixed-
   vector baseline (RNNencdec), at the sentence lengths the paper breaks out,
   and how RNNsearch held up on long sentences where the baseline fell off.
   Report BLEU as the paper reports it. Give the reader an honest sense of how
   large or small this evidence base was for a claim now treated as settled.
4. Bring it to the present. This paper is routinely cited as where attention
   began, and "Attention Is All You Need" (2017) built the Transformer on the
   same idea after dropping the recurrence. Say plainly what the 2014 paper
   did and did not show: it introduced soft attention/alignment inside an RNN
   translator; it did not propose the Transformer, self-attention, or language-
   model pretraining. Where today's shorthand ("attention was invented here")
   overreaches or compresses history, correct it exactly.

## The one thing this article does that the sources do not

Separate what the 2014 paper actually demonstrated (a soft-alignment fix to
the fixed-vector bottleneck in RNN translation, measured in BLEU on one
language pair) from the origin-of-attention story now told about it, and show
the reader the size of the evidence under that story.

## Angle correction (post-research, orchestrator decision)

The researcher's record settles two points that reshape the correction, and the
writer must draft to these, not to a naive version:

1. The paper DOES name the mechanism "attention." Section 3.1 says it
   "implements a mechanism of attention in the decoder." The word is rare and
   the model is named RNNsearch, with the formal method built on alignment,
   annotations, and a context vector, but the article must NOT claim the authors
   spoke only of alignment. That is false and the record shows it.
2. The paper DOES credit a precursor. Section 6.1 points to Graves (2013) on
   handwriting synthesis for a similar alignment approach. The authors did not
   claim to have invented learned alignment.

So the correction is about SCOPE, not vocabulary. What the 2014 paper actually
did: it introduced soft attention/alignment as a fix to the fixed-vector
bottleneck, demonstrated it only inside an RNN translator on one language pair
(WMT'14 English-French), named it an attention mechanism in passing, and
credited a 2013 precursor. What it did NOT do: propose the Transformer,
self-attention, or language-model pretraining, which came later (Vaswani et al.
2017 kept the idea and dropped the recurrence). The over-credit to correct is
the sweeping "this paper invented attention / started the LLM era," not the
word choice.

One numbers caveat the writer must honor: cross-paper BLEU is not like-for-like.
Sutskever et al.'s fixed-vector LSTM reports 34.8 on the same WMT'14 En-Fr test
set versus RNNsearch-50's 26.75, but depth, input reversal, and ensembling
differ. Do not present that as a head-to-head loss for alignment. The honest
in-paper comparison is RNNsearch vs RNNencdec (Table 1) and the
BLEU-vs-sentence-length figure (Fig. 2), where the fixed-vector baseline falls
off on long sentences and RNNsearch holds up.

## Boundaries — do not re-teach taught ground

The course has already published these. Link them in Background at first use;
do not re-teach the mechanism or the history they cover:
- the-evidence/attention-is-all-you-need — the 2017 Transformer paper. This
  lesson is its predecessor, not a re-run. Draw the line between them.
- the-mechanics/attention — how an attention head works as an operation.
  Do not re-derive attention here; this desk reads the document.
- the-evidence/seq2seq — the fixed-vector encoder-decoder this paper improves on.
- the-evidence/word2vec, the-evidence/long-short-term-memory — the word-vector
  and recurrent-cell background the paper builds on.
Assume algebra and probability. Everything else about AI is taught before use
or linked to an earlier lesson.

## Sources (the-evidence policy: min 6, primary >=3, secondary >=1)

Primary must include the paper itself (arXiv:1409.0473 / ICLR 2015 version).
Strong additional primaries: the earlier Cho et al. 2014 RNN encoder-decoder
paper (the fixed-vector baseline, arXiv:1406.1078); Sutskever et al. 2014
"Sequence to Sequence Learning"; "Attention Is All You Need" (Vaswani et al.
2017) as the document that carried the idea forward. Cite figures to the
document that owns them, at a real locator (section, page, table, figure).

## Recent shapes to break (house-wide; compare against the recent library)

- Do not default to the "You have probably seen / noticed / heard ..." second-
  person opener. Several recent lessons use it. Find this lesson's own way in.
- Do not close the opener on the house tricolon "By the end you will know A, B,
  and C." Preview what the reader will gain without that three-item cadence.
- Vary the self-description; "This lesson reads that paper / takes one apart /
  works backward from" recurs across the desk.
- Check this article's dek and headings against the recent the-evidence deks
  and headings (elmo, deep-double-descent, mamba, llama-3, react) so it is not
  built to the same mold.

## Production record

Profile balanced. Models: all roles "capable." Effort targets: researcher
high, writer medium, editor high, writing-coach low. Roles run as isolated
subagents on a capable model (Claude Opus-class); reasoning-effort is not
separately dialed per role in this harness, recorded here as a deviation from
the effort field. No `required` model/effort directive on this series, so
nothing was traded down.

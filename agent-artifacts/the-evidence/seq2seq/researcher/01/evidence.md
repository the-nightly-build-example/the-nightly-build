# Evidence: the-evidence/seq2seq (01)

The evidence supports a precise account of what Sutskever, Vinyals, and Le
actually built and measured in "Sequence to Sequence Learning with Neural
Networks" (arXiv:1409.3215, NIPS 2014): a 4-layer LSTM encoder that reads an
English sentence into one 1000-dimensional vector, a second 4-layer LSTM that
decodes French from that vector, beam search, and a single benchmark, WMT'14
English-to-French. The headline BLEU numbers, the architecture and scale, the
reversing trick, and the beam-search figures are all read from the paper's own
abstract, Section 3, and Table 1, with exact quotes recorded below. The
"afterlife" claims (attention removed the bottleneck; the Transformer dropped
recurrence) are each traced to the document that owns them: Bahdanau, Cho, and
Bengio (arXiv:1409.0473) for attention, Cho et al. (arXiv:1409.1259) for the
long-sentence degradation the attention paper set out to fix, and Vaswani et al.
(arXiv:1706.03762) for the Transformer.

The record is thin, and the commissioned angle is complicated, on one point: the
"fixed-length-vector bottleneck" is not a limitation the seq2seq paper
acknowledges. The paper reports the opposite for its own model. It was
"surprised to discover that the LSTM did well on long sentences." The bottleneck
was named and measured by a different, near-simultaneous group (Bahdanau/Cho),
on the basic single-layer RNN encoder-decoder, not on Sutskever's deep reversed
LSTM. The lineage the commission wants is real but has to be stated in that
order. See Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/1409.3215
             (venue page: https://papers.neurips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks)
Kind:        primary. The document under examination. Sutskever, Vinyals, and Le
             (all Google) own every architecture, scale, and result claim below;
             read via the arXiv rendering of this same paper.
Establishes: The full method and every headline number. A multilayer LSTM maps
             the input to a fixed-dimensional vector; a second LSTM decodes the
             target from it. WMT'14 English-to-French only.
Paraphrase:  The encoder LSTM reads the source one token at a time into a single
             fixed-length vector; the decoder LSTM generates the target
             conditioned on that vector, using left-to-right beam search. Trained
             on a 12M-sentence-pair subset of WMT'14. The best result comes from
             an ensemble of 5 reversed LSTMs with beam size 12.
Locators:    Abstract; Section 1 (intro/architecture); Section 2 (the model);
             Section 3.2 (dataset); Section 3.3 (reversing); Section 3.4
             (training detail/hardware); Section 3.5 (parallelization); Section
             3.6 and Table 1 (results); Section 3.7 (long-sentence analysis).
Quote:       Abstract: "Our method uses a multilayered Long Short-Term Memory
             (LSTM) to map the input sequence to a vector of a fixed
             dimensionality, and then another deep LSTM to decode the target
             sequence from the vector." Abstract: the LSTM "achieved a BLEU score
             of 34.8 on the entire test set" and, used to rescore the baseline,
             "its BLEU score increases to 36.5." Section 3.3: "the LSTM's test
             perplexity dropped from 5.8 to 4.7, and the test BLEU scores of its
             decoded translations increased from 25.9 to 30.6." Section 3.7: "We
             were surprised to discover that the LSTM did well on long
             sentences."
```

```text
URL:         https://arxiv.org/abs/1409.0473
Kind:        primary. Bahdanau (Jacobs University Bremen), Cho, and Bengio
             (Universite de Montreal) own the attention/alignment claim and the
             bottleneck diagnosis; read via the arXiv rendering.
Establishes: That the fixed-length vector is a bottleneck, and that attention
             ("soft-search") is the fix. This is the paper that named the
             limitation the commission attributes to seq2seq.
Paraphrase:  The authors conjecture the single fixed-length vector caps the
             performance of the basic encoder-decoder, and replace it: encode the
             source into a sequence of vectors and let the decoder adaptively
             select a subset while generating each target word.
Locators:    Abstract; Section 1 (introduction); Section 3 (the model). Cites
             Sutskever et al. 2014 and Cho et al. 2014 as the encoder-decoder
             work it improves on.
Quote:       "we conjecture that the use of a fixed-length vector is a bottleneck
             in improving the performance of this basic encoder-decoder
             architecture." And: it "does not attempt to encode a whole input
             sentence into a single fixed-length vector. Instead, it encodes the
             input sentence into a sequence of vectors and chooses a subset of
             these vectors adaptively while decoding."
```

```text
URL:         https://arxiv.org/abs/1409.1259
Kind:        primary. Cho, van Merrienboer, Bahdanau, and Bengio own the measured
             finding that the basic RNN encoder-decoder degrades on long
             sentences; read via the arXiv rendering.
Establishes: That the fixed-length representation empirically fails on long
             inputs, on the basic RNN encoder-decoder (not on Sutskever's model).
             This is the evidence that motivates attention, and the counterpoint
             to seq2seq's own "did well on long sentences" claim.
Paraphrase:  Both neural models translate short sentences well and lose quality
             sharply as length grows; the authors attribute this to the capacity
             of the fixed-length vector.
Locators:    Section 5 / Figure 4 (performance vs sentence length).
Quote:       "The most obvious explanatory hypothesis is that the fixed-length
             vector representation does not have enough capacity to encode a long
             sentence with complicated structure and meaning." Models "suffer
             significantly as the length of the sentences increases."
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary. Vaswani et al. (Google Brain / Google Research) own the
             Transformer claim; read via the arXiv rendering.
Establishes: The architecture that dropped recurrence entirely and now dominates.
             Cited here only to source the "later work replaced it" step, which
             the seq2seq lesson's library already covers.
Paraphrase:  The Transformer removes recurrence and convolution and relies wholly
             on attention. On WMT'14 English-to-French the big model reports 41.8
             BLEU; on English-to-German, 28.4.
Locators:    Abstract; Section 1; results tables. Cites Sutskever et al. 2014
             and Bahdanau et al. 2014.
Quote:       "We propose a new simple network architecture, the Transformer,
             based solely on attention mechanisms, dispensing with recurrence and
             convolutions entirely."
```

```text
URL:         https://arxiv.org/abs/1910.10683
Kind:        primary. Raffel et al. (Google) own the T5 text-to-text framing;
             read via the arXiv page.
Establishes: A concrete modern invocation of the encoder-decoder / sequence-to-
             sequence idea far broader than the 2014 result. T5 casts every
             text task as sequence-in, sequence-out, on an encoder-decoder
             Transformer. Published in JMLR (2020).
Paraphrase:  The framework treats every text-based language problem as a
             text-to-text task, feeding text in and generating text out, on a
             single encoder-decoder model.
Locators:    Abstract; Section 2 (the text-to-text framework).
Quote:       The approach treats "all text-based language problems into a
             text-to-text format," where the model takes text as input and
             produces text as output.
```

```text
URL:         https://d2l.ai/chapter_recurrent-modern/seq2seq.html
Kind:        secondary. "Dive into Deep Learning" (Zhang, Lipton, Li, Smola) is a
             textbook explaining the architecture from outside the authoring
             party. Used for context and teaching framing, not for any contested
             figure.
Establishes: An independent, plain restatement of the encoder-decoder design and
             the fixed-length-state framing, useful to confirm the standard
             pedagogical account matches the primary.
Paraphrase:  The encoder RNN turns a variable-length input into a fixed-shape
             hidden state that conditions the decoder; the text flags that later
             chapters add attention to move past this single fixed-length
             bottleneck.
Locators:    Chapter "Sequence-to-Sequence Learning for Machine Translation."
Quote:       "the encoder RNN will take a variable-length sequence as input and
             transform it into a fixed-shape hidden state."
```

## Contradictions

The commissioned angle rests on a "fixed-length-vector bottleneck" that the
seq2seq paper itself acknowledges. It does not. This is the most important
finding for the editor to weigh.

- **The seq2seq paper claims its model did not suffer on long sentences.**
  Section 3.7: "We were surprised to discover that the LSTM did well on long
  sentences." The paper reports no degradation up to about 35 words and only
  minor degradation on the longest (Figure 3, BLEU vs sentence length). So the
  paper does not present the fixed vector as a limitation; it presents its model
  as having beaten the expected limitation. Any sentence saying "seq2seq
  acknowledged the bottleneck" is wrong. The honest lineage is: seq2seq
  compressed a sentence into one vector and reported this worked even for long
  sentences; Bahdanau et al. (arXiv:1409.0473) then conjectured the fixed vector
  was a bottleneck, and Cho et al. (arXiv:1409.1259) measured the basic RNN
  encoder-decoder failing on long inputs; attention removed the single vector.
  The two critique papers were submitted the same month (September 2014) as
  seq2seq, not years later.

- **The critique was measured on a different model.** Cho et al.'s degradation
  result is for a single-layer RNN encoder-decoder without the reversing trick,
  not for Sutskever's deep, reversed, ensembled LSTM. The bottleneck is real as a
  general property of the fixed-vector design, but the specific model in
  arXiv:1409.3215 is not the model shown to break. State the bottleneck as a
  property of the approach, and attribute the "it breaks on long sentences"
  evidence to Cho/Bahdanau, not to the seq2seq paper.

- **The reversing trick partly reconciles this.** Reversing the source words was
  a workaround for exactly the long-range dependency problem that the fixed
  vector creates (Section 3.3: it reduces the "minimal time lag" between matching
  source and target words). So the seq2seq authors did feel the problem and hand-
  patched it, even as they reported their patched model handled long sentences
  well. This supports the commission's interest in reversing as an honest-scale
  detail, and it undercuts the cleaner story that seq2seq was oblivious to the
  bottleneck. The paper is candid that it lacks a full account: Section 3.3, "we
  do not have a complete explanation to this phenomenon."

- **The reversing trick is not overstated by the commission.** Its effect is
  large and primary-sourced: single-model BLEU 25.9 to 30.6, perplexity 5.8 to
  4.7 (Section 3.3), and the single reversed LSTM scores 30.59 versus the forward
  LSTM's 26.17 in Table 1. Nothing in the sources shrinks it. One caveat for
  scale honesty: the 34.81 headline is not reversing alone. It stacks reversing,
  a 5-model ensemble, and beam size 12.

- **The result covers one language pair.** The paper's only translation
  benchmark is WMT'14 English-to-French. There is no second language pair and no
  second task in the reported MT results (the paper adds a qualitative
  representation analysis, not another benchmark). Modern usage of "sequence to
  sequence" spans every text task (see T5) and many modalities; the 2014 result
  that anchors the name is one direction of one language pair. That gap is the
  commission's "invoked today in a way the actual result qualifies," and it is
  well supported.

## Numbers

```text
Figure: 34.81 BLEU (abstract rounds to 34.8)
Owner:  Sutskever et al. 2014, Table 1 (Section 3.6)
Scope:  WMT'14 English-to-French test set; ensemble of 5 reversed LSTMs, beam
        size 12; direct LSTM translation (no SMT). This is the headline result.
```

```text
Figure: 36.5 BLEU
Owner:  Sutskever et al. 2014, abstract and Section 3.6
Scope:  Same test set; the LSTM ensemble used to rescore (rerank) the baseline
        SMT system's 1000-best list. NOT direct LSTM output. Best number in the
        paper, and it depends on the SMT system.
```

```text
Figure: 33.30 BLEU
Owner:  Sutskever et al. 2014, Section 3.6 (baseline)
Scope:  Same test set; the phrase-based statistical MT (SMT) baseline the LSTM
        was compared against and later used to rescore.
```

```text
Figure: 25.9 to 30.6 BLEU; perplexity 5.8 to 4.7
Owner:  Sutskever et al. 2014, Section 3.3
Scope:  Effect of reversing source-sentence word order, single-model, on the
        development/test configuration described in 3.3.
```

```text
Figure: 26.17 / 30.59 / 33.00 / 34.50 / 34.81 BLEU (full Table 1 series)
Owner:  Sutskever et al. 2014, Table 1 (Section 3.6)
Scope:  WMT'14 En-Fr test. Single forward LSTM (beam 12) 26.17; single reversed
        LSTM (beam 12) 30.59; ensemble of 5 reversed LSTMs at beam 1 = 33.00,
        beam 2 = 34.50, beam 12 = 34.81. Ensemble of 2 reversed LSTMs (beam 12)
        = 33.27. Preserved as a series for a possible chart on ensembling and
        beam width.
```

```text
Figure: 4 LSTM layers; 1000 cells per layer; 1000-dimensional word embeddings
Owner:  Sutskever et al. 2014, Section 3.4
Scope:  Both encoder and decoder are deep LSTMs of this size.
```

```text
Figure: 384M total parameters, of which 64M are pure recurrent connections
Owner:  Sutskever et al. 2014, Section 3.4
Scope:  Whole model. The remaining ~320M are dominated by the input and output
        embedding matrices over the 160,000 source / 80,000 target vocabularies.
```

```text
Figure: 12M sentence pairs; 348M French words, 304M English words
Owner:  Sutskever et al. 2014, Section 3.2
Scope:  The training subset of WMT'14 En-Fr actually used.
```

```text
Figure: source vocabulary 160,000; target vocabulary 80,000
Owner:  Sutskever et al. 2014, Section 3.2
Scope:  Most frequent words kept; out-of-vocabulary words replaced by a special
        token, which the abstract notes is penalized in scoring.
```

```text
Figure: 8 GPUs; ~6,300 words/second; ~10 days training
Owner:  Sutskever et al. 2014, Sections 3.4-3.5
Scope:  One 8-GPU machine, one LSTM layer per GPU, remaining GPUs for the
        softmax; full training run.
```

```text
Figure: beam sizes 1, 2, and 12
Owner:  Sutskever et al. 2014, Section 3.6 and Table 1
Scope:  Decoding. The paper reports the system "performs well even with a beam
        size of 1" (33.00 for the 5-model ensemble); beam 12 is the headline
        setting.
```

```text
Figure: Transformer big model 41.8 BLEU (En-Fr), 28.4 BLEU (En-De)
Owner:  Vaswani et al. 2017
Scope:  WMT'14. Recorded only to size the later state of the art against the
        2014 34.81; do not present as a like-for-like comparison, the training
        data and years differ.
```

```text
Figure: Bahdanau RNNsearch-50 26.75 (all) / 34.16 (no unknown words); Moses
        33.30 / 35.63
Owner:  Bahdanau et al. 2014
Scope:  WMT'14 En-Fr. Recorded to source the attention paper's own results if the
        writer contrasts attention with seq2seq; note the "no unknown words"
        subset is a different denominator than the full test set.
```

## Source assets

```text
Asset: Figure 1, the unrolled encoder-decoder diagram (Section 1), reading a
       source sequence and emitting a target after an end-of-sequence marker.
Shows: The whole mechanism at a glance: one network reads "A B C" then a second
       generates "W X Y Z," with the sentence funneled through a single vector
       at the boundary. This is the clearest single image of what seq2seq does.
Crop:  Keep the end-of-sequence marker and the direction of the arrows; the
       teaching point is that generation starts only after the full input is
       read into one state.
```

```text
Asset: Table 1 (Section 3.6), BLEU by method and beam size.
Shows: How the 34.81 headline is assembled from reversing, ensembling, and beam
       width, and how far a single model (30.59) sits below it. Good raw data for
       an honest-scale chart.
Crop:  Retain the method labels and beam sizes; the numbers mean nothing without
       which configuration produced them.
```

```text
Asset: Figure 3 (Section 3.7), BLEU versus sentence length, and BLEU versus
       average word-frequency rank.
Shows: The paper's own evidence that its LSTM held up on long sentences, the
       claim that complicates the bottleneck angle. Pair it with Cho et al.
       Figure 4 if the writer contrasts the two.
Crop:  Keep the x-axis (sentence length) labeled; the point is the flatness of
       the curve up to ~35 words.
```

```text
Asset: Figure 2 (Section 3.6), 2-D PCA projection of LSTM phrase representations.
Shows: Phrases cluster by meaning and are sensitive to word order, the paper's
       argument that the fixed vector encodes structure, not just a bag of words.
Crop:  Keep the labeled example clusters; without the phrase labels the scatter
       is decorative.
```

```text
Asset: Bahdanau et al. 2014, the alignment heatmap (its Figure 3) and BLEU-vs-
       length plot (its Figure 2).
Shows: Attention aligning target words to source words, and RNNsearch staying
       flat as sentence length grows while the fixed-vector model drops. Carries
       the "attention removed the bottleneck" step better than prose.
Crop:  Keep both axes and the word labels on the heatmap; the alignment is the
       whole point.
```

## Discarded

```text
URL: https://proceedings.neurips.cc/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html
     Returned 404. Not a rejected source, a wrong address. The paper's real venue
     page is https://papers.neurips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks,
     which resolves and confirms NIPS 2014; recorded with source 1.
```

```text
URL: Medium, ResearchGate, and liner.com "quick review" pages surfaced in search
     for the seq2seq paper. Not opened or cited: they are secondary retellings of
     the primary already read, and would add repetition, not evidence.
```

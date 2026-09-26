# Evidence: the-evidence/align-and-translate (01)

The primaries support the commission's spine: Bahdanau, Cho, and Bengio argue in
their own words that squeezing a source sentence into one fixed-length vector
caps the basic encoder-decoder, they add a decoder that reads a distinct
weighted combination of source annotations per target word, and they measure the
gain in BLEU on WMT'14 English-French, where their RNNsearch holds up on long
sentences while the RNNencdec baseline falls off. The scale is exact and modest:
one language pair, a 30,000-word shortlist, 348M training words, two length
configurations. The lineage is confirmed from primaries: the fixed-vector
baseline is Cho et al. 2014 and Sutskever et al. 2014, and Vaswani et al. 2017
cites this paper and drops recurrence for self-attention.

The angle is that the paper introduced soft alignment as a fix and is now
over-credited as "inventing attention," told partly by contrasting the paper's
"alignment" language with the modern "attention" shorthand. That contrast is
weaker than the commission assumes. The paper itself uses "attention" and
"attention mechanism" in Section 3.1, and it names Graves 2013 as a prior
alignment approach in Section 6.1. The honest correction is not that the authors
avoided the word "attention," but that they framed it as one intuition for a
mechanism they called alignment, built inside an RNN translator, on one task, and
did not propose the Transformer or self-attention. Two contradictions below
matter to the editor: the paper's own use of "attention," and Sutskever's
fixed-vector LSTM reporting no long-sentence difficulty.

## Sources

```text
URL:         https://arxiv.org/abs/1409.0473
Kind:        primary. The authors own every claim about the RNNsearch method,
             the bottleneck conjecture, and the BLEU results reported here.
Establishes: Authorship, version history, venue, the problem statement, and the
             abstract's framing of the fix.
Paraphrase:  Bahdanau, Cho, and Bengio propose extending the fixed-vector
             encoder-decoder by letting the model soft-search the source for the
             parts relevant to each target word. Accepted at ICLR 2015 as an
             oral presentation. First posted 1 Sep 2014; v7 (19 May 2016) is the
             current version, and v5/v6 (Mar-Apr 2015) are the ICLR camera-ready
             era.
Locators:    Abstract; arXiv listing (version dates, "Accepted at ICLR 2015 as
             oral presentation").
Quote:       "we conjecture that the use of a fixed-length vector is a bottleneck
             in improving the performance of this basic encoder-decoder
             architecture, and propose to extend this by allowing a model to
             automatically (soft-)search for parts of a source sentence that are
             relevant to predicting a target word"
```

```text
URL:         https://arxiv.org/abs/1409.0473 (full text via
             https://ar5iv.labs.arxiv.org/html/1409.0473)
Kind:        primary. Same document; separated here to record the method,
             affiliations, data, and results with their own locators.
Establishes: Authors and affiliations; the bottleneck argument; the alignment
             method; the paper's terminology, including its use of "attention";
             the training data and model size; the BLEU table; the two figures.
Paraphrase:  Authors: Dzmitry Bahdanau (Jacobs University Bremen, Germany);
             KyungHyun Cho and Yoshua Bengio (Universite de Montreal, Bengio also
             CIFAR Senior Fellow). Section 1 states the fixed-vector concern and
             that it hurts long sentences. Section 3.1 defines the decoder that
             conditions each output word on a distinct context vector, and calls
             this "a mechanism of attention." Section 3.2 builds annotations from
             a bidirectional RNN. Section 4 gives the corpus, shortlist, and two
             length configurations; the appendix gives model sizes. Section 5 and
             Table 1 give BLEU; Figures 2 and 3 give the length curve and the
             alignment heatmaps.
Locators:    Author block (header); Section 1; Section 3.1 (Eqs. 5-6, context
             vector, alignment weights, "attention"); Section 3.2 (annotations,
             BiRNN); Section 4.1-4.2; Appendix A.2.3; Section 5.1; Table 1;
             Figures 2 and 3; Section 6.1; Section 7 (conclusion).
Quote:       Section 1: "A potential issue with this encoder-decoder approach is
             that a neural network needs to be able to compress all the necessary
             information of a source sentence into a fixed-length vector."
             Section 3.1: "Intuitively, this implements a mechanism of attention
             in the decoder. The decoder decides parts of the source sentence to
             pay attention to. By letting the decoder have an attention
             mechanism, we relieve the encoder from the burden of having to
             encode all information in the source sentence into a fixed-length
             vector."
             Section 3.1: "It should be noted that unlike the existing
             encoder-decoder approach (see Eq. (2)), here the probability is
             conditioned on a distinct context vector c_i for each target word
             y_i."
             Section 3.2: "we obtain an annotation for each word x_j by
             concatenating the forward hidden state and the backward one".
             Section 3.1 alignment model: "We parametrize the alignment model a
             as a feedforward neural network which is jointly trained with all the
             other components of the proposed system."
             Section 6.1: "A similar approach of aligning an output symbol with
             an input symbol was proposed recently by Graves (2013) in the
             context of handwriting synthesis."
             Section 7: "the proposed approach achieved a translation performance
             comparable to the existing phrase-based statistical machine
             translation." "One of challenges left for the future is to better
             handle unknown, or rare words."
```

```text
URL:         https://arxiv.org/abs/1406.1078
Kind:        primary. Cho and co-authors own the RNN Encoder-Decoder and its
             fixed-length-vector framing, which this paper improves on.
Establishes: The fixed-vector baseline lineage. Bahdanau is a co-author here,
             so the later paper is by overlapping authors improving their own
             prior model.
Paraphrase:  Cho, van Merrienboer, Gulcehre, Bahdanau, Bougares, Schwenk, and
             Bengio propose an RNN Encoder-Decoder: one RNN encodes a source
             sequence into a fixed-length vector, another decodes it into the
             target sequence. Used to score phrases for statistical MT. EMNLP
             2014.
Locators:    Abstract; arXiv listing (v3, 3 Sep 2014; "EMNLP 2014").
Quote:       "One RNN encodes a sequence of symbols into a fixed-length vector
             representation, and the other decodes the representation into another
             sequence of symbols."
```

```text
URL:         https://arxiv.org/abs/1409.3215
Kind:        primary. Sutskever, Vinyals, and Le own the Seq2Seq LSTM result and
             its long-sentence claim.
Establishes: A second fixed-vector baseline on the same WMT'14 English-French
             task, with a directly comparable BLEU. Its own abstract claims the
             fixed-vector LSTM did not struggle on long sentences, which bears on
             the angle.
Paraphrase:  A multilayer LSTM maps the input to a fixed-dimensional vector and a
             second LSTM decodes the target. Reports BLEU 34.8 on the full WMT'14
             English-French test set (penalized on out-of-vocabulary words), and
             36.5 when reranking a phrase-based system's 1000 hypotheses; the
             phrase-based system scores 33.3. States the LSTM did not have
             difficulty on long sentences, helped by reversing source word order.
Locators:    Abstract; arXiv listing (v3, 14 Dec 2014).
Quote:       "Our method uses a multilayered Long Short-Term Memory (LSTM) to map
             the input sequence to a vector of a fixed dimensionality, and then
             another deep LSTM to decode the target sequence from the vector."
             "Additionally, the LSTM did not have difficulty on long sentences."
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary. Vaswani et al. own the Transformer and self-attention, and
             own their citation of this paper.
Establishes: That the 2017 Transformer built on attention and cites Bahdanau et
             al., and that it dropped recurrence for self-attention. Draws the
             line the commission asks for between 2014 and 2017.
Paraphrase:  Proposes the Transformer, based solely on attention, removing
             recurrence and convolution. Cites Bahdanau et al. 2014 (reference
             [2]) as prior work that made attention integral to sequence models.
             Defines self-attention as an attention mechanism relating positions
             within a single sequence.
Locators:    Abstract; Introduction; Background (self-attention definition);
             References entry [2].
Quote:       "We propose a new simple network architecture, the Transformer,
             based solely on attention mechanisms, dispensing with recurrence and
             convolutions entirely."
             Reference [2]: "Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio.
             Neural machine translation by jointly learning to align and
             translate. CoRR, abs/1409.0473, 2014."
             "Self-attention, sometimes called intra-attention is an attention
             mechanism relating different positions of a single sequence in order
             to compute a representation of the sequence."
```

```text
URL:         https://arxiv.org/abs/1308.0850
Kind:        primary. Graves owns the handwriting-synthesis soft-window
             mechanism. It is a primary for the precursor claim, and it is the
             work Bahdanau et al. cite as a prior alignment approach.
Establishes: A pre-2014 differentiable soft-alignment ("window") mechanism that
             dynamically aligns a character sequence to an output sequence.
             Central to testing the "invented attention" shorthand.
Paraphrase:  A soft window over the character sequence, defined by a mixture of
             K Gaussians whose parameters the network emits at each step, lets an
             LSTM dynamically align text to pen positions and decide which
             character to write next. Section 5.1.
Locators:    Section 5.1 (Synthesis Network), Eqs. 46-47; arXiv listing (v5,
             5 Jun 2014; originally 4 Aug 2013).
Quote:       "The parameters of the window are output by the network at the same
             time as it makes the predictions, so that it dynamically determines
             an alignment between the text and the pen locations."
             "the window weight phi(t,u) can be loosely interpreted as the
             network's belief that it is writing character c_u at time t"
```

```text
URL:         https://www.semanticscholar.org/paper/fa72afa9b2cbc8f0d7b05d52548906610ffbb9c5
             (data via https://api.semanticscholar.org/graph/v1/paper/arXiv:1409.0473)
Kind:        secondary. A citation index counts how others cite the paper; it
             does not author any claim in it.
Establishes: The order-of-magnitude of citations, showing how heavily the paper
             is used. Supports the "treated as settled" framing without lending
             it authority.
Paraphrase:  Semantic Scholar records roughly 30,000 citations for the paper
             (30,066 exact at retrieval), listing venue "International Conference
             on Learning Representations" and year 2014.
Locators:    Semantic Scholar Graph API, fields citationCount/venue/year;
             retrieved 2026-09-26.
Quote:       (none; report as approximate magnitude, ~30,000 citations, Semantic
             Scholar, retrieved 2026-09-26)
```

## Contradictions

The paper uses "attention," so the framing that the authors spoke only of
alignment is inaccurate. Section 3.1 says the mechanism "implements a mechanism
of attention in the decoder" and describes "an attention mechanism." The word is
rare in the paper and confined to that intuitive passage; the model is named
RNNsearch, and the method sections use alignment, soft alignment, annotations,
and context vector. The defensible correction is narrower than "they did not call
it attention." They did, in passing, while the paper's formal apparatus is
alignment inside an RNN translator.

The paper names a precursor. Section 6.1 credits Graves 2013 with "a similar
approach of aligning an output symbol with an input symbol" in handwriting
synthesis. The authors did not claim to invent the idea of learned alignment.
This supports the "over-credited" half of the angle and undercuts any telling
that treats the mechanism as originating whole in this paper.

Sutskever et al. 2014 report that a fixed-vector LSTM "did not have difficulty on
long sentences" and reached BLEU 34.8 on the same WMT'14 English-French test set,
above Bahdanau's RNNsearch-50 (26.75 on all sentences). This complicates the flat
claim that the fixed-vector bottleneck necessarily caps long-sentence quality:
one contemporaneous fixed-vector model, with reversed source inputs, reported the
opposite on long sentences. Bahdanau's evidence for the bottleneck is his own
RNNencdec baseline degrading with length (Figure 2), not a defeat of every
fixed-vector system. The two results are not strictly comparable: Sutskever uses
a deep LSTM with reversed inputs and an ensemble in its strongest numbers, and
BLEU protocols differ, so the editor should not read 34.8 against 26.75 as a
like-for-like loss.

## Numbers

```text
Figure: RNNencdec-30 BLEU 13.93 (all), 24.19 (no-UNK)
Owner:  Bahdanau et al. 2014, Table 1
Scope:  WMT'14 En-Fr news-test-2014 (3003 sentences); no-UNK = sentences with no
        unknown word in source or reference. Trained on sentences up to 30 words.
```

```text
Figure: RNNsearch-30 BLEU 21.50 (all), 31.44 (no-UNK)
Owner:  Bahdanau et al. 2014, Table 1
Scope:  Same test set; trained on sentences up to 30 words.
```

```text
Figure: RNNencdec-50 BLEU 17.82 (all), 26.71 (no-UNK)
Owner:  Bahdanau et al. 2014, Table 1
Scope:  Same test set; trained on sentences up to 50 words.
```

```text
Figure: RNNsearch-50 BLEU 26.75 (all), 34.16 (no-UNK)
Owner:  Bahdanau et al. 2014, Table 1
Scope:  Same test set; trained on sentences up to 50 words.
```

```text
Figure: RNNsearch-50* BLEU 28.45 (all), 36.15 (no-UNK)
Owner:  Bahdanau et al. 2014, Table 1 (starred row)
Scope:  Same as RNNsearch-50 but trained much longer, until development-set
        performance stopped improving. This is the paper's best neural number.
```

```text
Figure: Moses (phrase-based SMT baseline) BLEU 33.30 (all), 35.63 (no-UNK)
Owner:  Bahdanau et al. 2014, Table 1
Scope:  Same test set. Moses uses a separate monolingual corpus of 418M words;
        the RNN models do not.
```

```text
Figure: Training corpus 348M words
Owner:  Bahdanau et al. 2014, Section 4.1
Scope:  WMT'14 En-Fr combined bilingual corpora total 850M words, reduced to
        348M by the Axelrod et al. 2011 data-selection method (per Cho et al.
        2014a). Dev set = news-test-2012 + news-test-2013; test = news-test-2014.
```

```text
Figure: Vocabulary shortlist 30,000 most frequent words per language
Owner:  Bahdanau et al. 2014, Section 4.1
Scope:  Source and target each; words outside the shortlist map to a special
        unknown token.
```

```text
Figure: Model sizes: 1000 hidden units per RNN direction (n=1000); 620-dim word
        embeddings (m=620); 1000 alignment-model hidden units (n'=1000); 500
        maxout hidden units (l=500)
Owner:  Bahdanau et al. 2014, Appendix A.2.3
Scope:  Per model; the encoder is bidirectional, so it has forward and backward
        RNNs of 1000 units each.
```

```text
Figure: BLEU-vs-length curve: RNNencdec BLEU drops sharply as source length
        grows; RNNsearch-50 shows no deterioration at length 50 and beyond
Owner:  Bahdanau et al. 2014, Figure 2 (full test set, includes unknown words)
Scope:  BLEU by sentence-length bin on news-test-2014. This is the paper's
        central visual evidence for the bottleneck claim.
```

```text
Figure: Citation magnitude ~30,000 (30,066 exact)
Owner:  Semantic Scholar (secondary index), retrieved 2026-09-26
Scope:  Total citing works recorded by one index; other indexes differ. Report
        as approximate magnitude.
```

## Limits

The precise BLEU protocol (tokenization, single model vs ensemble, casing) is
not fully captured here beyond Table 1's two columns and the Moses monolingual
footnote; treat cross-paper BLEU comparisons (Sutskever's 34.8 vs Bahdanau's
26.75) as indicative, not like-for-like.

The exact form of the alignment equations is recorded as Eqs. 5-6 (context
vector as a weighted sum of annotations; weights from a softmax over a
feedforward energy a(s_{i-1}, h_j)), sufficient for the one small equation the
commission permits, but the full GRU/maxout parametrization from the appendix is
summarized, not transcribed line by line.

KyungHyun Cho's affiliation is recorded as Universite de Montreal from the paper
header and the standard camera-ready; the ar5iv rendering did not surface an
explicit affiliation line beside his name, so this rests on the shared
Montreal affiliation line and common record rather than an isolated printed line.

Everything else the commission asked for is established from primaries: the
problem statement, the method and its terminology, the data and scale, the BLEU
table with all four configurations plus the starred best and Moses, the two
figures, the Transformer lineage, the two fixed-vector baselines, the Graves
precursor, and the citation magnitude.

## Source assets

```text
Asset: Figure 2, the BLEU-vs-sentence-length plot, Bahdanau et al. 2014.
Shows: RNNencdec's BLEU falling as source sentences get longer while
       RNNsearch-50 stays flat past length 50. This is the paper's own picture of
       the fixed-vector bottleneck and the fix, and it carries the argument
       better than the single Table 1 numbers.
Crop:  Keep both curves, the length axis with its scale, and the BLEU axis
       labels. Do not crop to a single curve, which would hide the comparison
       that is the point.
```

```text
Asset: Figure 3, the four sample alignment heatmaps, Bahdanau et al. 2014.
Shows: Per-word alignment weights alpha_ij as grayscale pixels between English
       source words (x-axis) and generated French words (y-axis), including
       non-monotonic reordering (for example the phrase order in "European
       Economic Area" mapping to "zone economique europeenne"). Makes the
       "soft alignment" concept concrete.
Crop:  Keep the axis word labels on at least one panel, or the heatmap is
       unreadable. If cropping to one panel, keep the panel showing reordering,
       and retain the grayscale so weights remain legible.
```

```text
Asset: Table 1, the BLEU results table, Bahdanau et al. 2014.
Shows: The full head-to-head: RNNencdec vs RNNsearch at 30 and 50 words, the
       starred best, and Moses, in both the all-sentences and no-unknown-words
       columns. Better as a small table than as prose if the article shows the
       numbers side by side.
Crop:  Reproduce as a table, not an image crop; keep both columns and the Moses
       row, and note in a caption that Moses used extra monolingual data.
```

```text
Asset: Figure 1, the RNNsearch model diagram, Bahdanau et al. 2014.
Shows: The decoder generating the t-th target word y_t from a context vector
       formed over the bidirectional annotations h_1..h_T. A schematic of the
       mechanism.
Crop:  Optional; keep the annotation sequence and the single target-word context
       if used. Lower priority than Figures 2 and 3.
```

## Discarded

```text
URL: https://www.semanticscholar.org/paper/... (HTML page): returned empty
     content on fetch; replaced by the Semantic Scholar Graph API, which returned
     the citation count directly. The API is the recorded route; the page is the
     document's home.
```

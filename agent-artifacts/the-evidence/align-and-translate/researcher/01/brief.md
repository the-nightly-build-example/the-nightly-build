# researcher brief: the-evidence/align-and-translate (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/agent-artifacts/the-evidence/align-and-translate/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/agent-artifacts/the-evidence/align-and-translate/commission.md — the assignment, boundaries, and the required contribution.

Output:
- /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/agent-artifacts/the-evidence/align-and-translate/researcher/01/evidence.md

Work from these inputs. Do not tour the repository or the archive for
background. Read primary documents, not coverage of them. Where something you
need is missing, ask me.

Source policy (the-evidence): at least 6 sources total, at least 3 primary, at
least 1 secondary. Meet counts with sources that change the interpretation, not
padding.

## The document to read first, in full

Bahdanau, Cho, Bengio, "Neural Machine Translation by Jointly Learning to Align
and Translate," arXiv:1409.0473 (v7 is the ICLR 2015 camera-ready). Read the
whole paper, including the experiment section and the appendices/figures.

## Questions the record must answer (with exact locators)

1. The problem statement. Where does the paper argue the fixed-length vector is
   the bottleneck of the basic encoder-decoder? Capture the exact claim.
2. The method. How the decoder computes alignment weights over the source
   annotations and forms a distinct context vector per target word; the
   bidirectional RNN encoder producing the annotations. Capture the paper's own
   terms (RNNsearch, RNNencdec, annotations, alignment, context vector). Note
   whether the paper itself uses the word "attention" (it speaks of alignment /
   soft alignment); record this precisely, since the article corrects the
   modern shorthand.
3. The data and scale. The exact training corpus (WMT'14 English-French), the
   number of sentence pairs / tokens the paper reports it trained on, the
   vocabulary size cap, and the model dimensions. Report the exact figures with
   units.
4. The numbers. The BLEU scores for RNNsearch vs RNNencdec, at both the 30-word
   and 50-word training configurations (RNNsearch-30/50, RNNencdec-30/50), on
   the test set, and the with/without-unknown-words variants the paper breaks
   out. The long-sentence result: the plot/figure showing RNNsearch holding up
   as sentence length grows while RNNencdec degrades. Give exact readings and
   the table/figure numbers.
5. The alignment visualization (the figure showing soft-alignment heatmaps
   between source and target words). Record where it is and what it shows.
6. Legacy and present use. Confirm from primaries: that "Attention Is All You
   Need" (Vaswani et al. 2017, arXiv:1706.03762) built on and cites this idea,
   and that it dropped recurrence for self-attention. Confirm the fixed-vector
   baseline lineage: Cho et al. 2014 (arXiv:1406.1078) and Sutskever et al.
   2014 (Seq2Seq, arXiv:1409.3215). Record citation-count magnitude for the
   Bahdanau paper from a citation index (Google Scholar / Semantic Scholar) as
   a secondary, to show how heavily it is cited — report it as an approximate
   magnitude with the source and retrieval date, not false precision.

## Look for what breaks the angle

The article's angle is that the paper introduced soft alignment as a fix to the
fixed-vector bottleneck and is now over-credited as "inventing attention."
Search for: earlier alignment/attention precursors the paper itself cites or
that predate it (e.g., Graves 2013 on handwriting synthesis attention; any
earlier alignment work), and any claim that the fixed-vector bottleneck was not
really the limiting factor. Record contradictory evidence in full so the editor
can test the angle.

## Source assets

For the paper, identify the exact figures that could carry the argument better
than prose: the BLEU-vs-sentence-length plot and the alignment heatmap figure.
Give the figure number, where it lives, and what a crop must keep. Do not
prescribe crop coordinates.

Classify every source primary/secondary with the authorship-and-stake test.
Record exact author names, affiliations (Jacobs University Bremen / Université
de Montréal for the authors), and paper titles as the documents state them.

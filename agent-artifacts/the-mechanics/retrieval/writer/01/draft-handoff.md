# Draft handoff: the-mechanics/retrieval (writer/01)

## Original work

The piece threads one concrete query, a "can I sublet" question against a lease
clause that shares no keyword with it ("assign or transfer occupancy"), down the
full retrieval ladder, and uses that single thread to localize the familiar
bad-citation failure to two named rungs (retrieval returned the wrong chunk, or
generation ignored the right one) that the evidence record measures end-to-end
but cannot cleanly separate.

## Proof result

`nb check ... --series the-mechanics --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Words 2199
(band 1200-2200), sources 9 (8 primary, 1 secondary), reading 10 min. No
warnings intentionally left; earlier rounds cleared length-high, two
sentence-density flags (one was a semicolon chain, now split), a cite-order flag
(sources renumbered to first-appearance order: SBERT=2 before DPR=3, Liu=8 before
BEIR=9), and all-caps stat-strip labels (rewritten in sentence case).

## How the round-focus items were honored

- Ranking is stated as "closeness in embedding space"; cosine similarity is named
  as the common default (Sentence-BERT), with the RAG/DPR lineage ranking by raw
  dot product called out explicitly. Not asserted as universal.
- Honesty note uses the sharpened form: Lewis et al. 2020 kept the document
  encoder and index fixed and trained only the query encoder and generator
  together; shipped "Naive RAG" trains neither. Precise, per the evidence.
- The bad-citation failure is presented as owned by either retrieval or
  generation, with the explicit statement that no cited source partitions the two.
  Not resolved to one step.
- No code (series rule). Furniture: one table (DPR vs BM25 top-20/top-100 on
  Natural Questions), one stat strip (51.5% / 74.5%), one "In plain language" note.

## Links (not numbered sources)

word-embeddings, instructions-are-data, knowledge-cutoff, losing-the-thread,
hallucination are all linked via `../the-mechanics/<slug>.html`; all five target
slugs confirmed present in /home/user/library-checkout and resolved under the
links-included proof.

## Open questions

None for evidence or voice. One judgment call recorded: harness string set to
`claude-code-routine`, matching tonight's other the-mechanics publication
(prefill-and-decode), since the brief named the value to record only for date and
writer model; flag if this run wants a different harness label.

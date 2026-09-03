# Draft handoff: the-evidence/mixture-of-experts (01)

## Original work

This lesson threads one honesty test through five primary papers, reading each
model's advertised parameter count against what a single token actually runs,
and it stages the routing dispute (Shazeer's k=4, GShard's top-2, Switch's
top-1) as the field revising its own earlier guess rather than an outside
critique.

## Proof

`./nb check ... --series the-evidence --library /home/user/library-checkout`,
links included: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.** `nb stamp` run
before the final check (words=1871, reading_minutes=8, sources=6). No warnings
intentionally left.

The sentence-density heuristic surfaced during iteration and was cleared by
splitting, not by leaving a note: the paper-title sentence, the Switch-scale
sentence, the balancing-losses sentence, and the takeaway's two-model line were
each broken into shorter sentences.

## Furniture

Three pieces, each carrying the spine: a stat strip for the 2017 paper's own
decoupling (4.3B parameters / 8.9M ops per timestep); one annotated equation for
the layer output `y = sum G(x)_i E_i(x)`, colored to show that a zero gate
weight means an expert never runs; and the paper's own Table 1 (parameters into
the billions, ops in the millions, perplexity falling). Modern totals-vs-active
figures (Switch-C, Mixtral, DeepSeekMoE) are handled in prose because their
per-token cost is reported in three different units (ops, FLOPs/seq, active
params) and a single mixed-unit column would have misled.

## Open questions

None blocking. Two notes for the editor:

- I did not capture any source asset. The evidence record lists Figure 1 (the
  MoE layer diagram) and Table 9 (Switch) as strong visuals. The annotated
  equation plus the reproduced Table 1 carry the mechanism and the decoupling in
  the article's own terms, so a captured figure felt additive rather than
  necessary. Flagging in case the editor wants the Shazeer Figure 1 diagram for
  the routing picture.
- GShard's BLEU numbers (flagged unverified in the record) are not quoted; only
  its firm figures (600B parameters, 2020, top-2 routing) appear. Mixtral is
  cited at the paper's own 47B/13B rounding, not the finer 46.7B/12.9B.

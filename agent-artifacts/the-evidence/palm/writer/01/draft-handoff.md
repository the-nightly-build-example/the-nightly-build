# Draft handoff: the-evidence/palm (01)

## Original work

The article turns the evidence record's separately listed figures into one
measured comparison: it sets PaLM's 1.44 tokens per parameter beside
Chinchilla's ~11-trillion-token compute-optimal budget for a model its size to
show the one-fourteenth shortfall on the page, then reads that shortfall as a
retrospective efficiency verdict (not weakness) and stages PaLM's emergence and
GSM8K headlines as claim-then-challenge, so the reader can see exactly where
today's citations outrun what the paper showed.

## Proof

`./nb check ... --series the-evidence --library /tmp/claude-0/library-checkout`
(final run, links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**

No warnings left standing. (An interim W-SENTENCE-DENSITY on the PaLM 2 sentence
was resolved by splitting it, not waived.)

## Handling of the brief's caveats

- Figure-read caveat respected: the piece uses only the textual aggregates (44
  of 58 common tasks; 25% of 150 tasks >+10%, 15% >+20%). No per-task Figure 5
  percentage is printed, and Figure 5 is not reproduced as an asset. The
  load-bearing token comparison is carried by a table, not a chart, so no
  figure-capture or chart tooling was needed.
- Two flagged quotes were paraphrased rather than printed verbatim, per the
  evidence notes: the PaLM 2 scaling-section line and the Schaeffer abstract
  line. The unverified "NeurIPS 2023" venue for Schaeffer is not printed.

## Open questions

None blocking. All seven sources and every internal lesson link resolve.

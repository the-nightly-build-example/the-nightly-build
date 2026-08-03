# Draft handoff: the-mechanics/prefill-and-decode (writer 01)

## Original work
This lesson maps the reader's own felt timeline (the pause, then the
word-by-word stream) onto the two phases and the cache that the primaries
describe only in hardware terms, so that prefill, the KV cache, and decode each
earn their name by explaining a duration the reader actually sat through, and it
collapses the sources' scattered, model-specific magnitudes into the single
reader-facing inversion no source states outright: the long prompt is the cheap
part and the short reply is the expensive one.

## Proof result
`./nb check --series the-mechanics ... ` (links included, after `nb stamp`):
**BLOCK: 0, WARN: 0 — PUBLISHABLE.** words=2077, reading_minutes=9, sources=8
(7 primary, 1 secondary; primary >= 4 and secondary >= 1 satisfied).

No warnings were left standing. The four W-SENTENCE-DENSITY warnings the first
pass raised were fixed by splitting each long sentence into shorter
single-purpose sentences (including the one earned-contrast inversion, which now
lands across two parallel sentences rather than one 43-word run). The
W-SELF-COUNT warnings cleared on `nb stamp`.

## How the round's named decisions were handled
- Every magnitude carries its stated conditions and is labelled illustrative:
  800 KB/token and 1.6 GB/request (OPT-13B, FP16); 128 prefill tokens ≈ 1 decode
  token (Mistral-7B, one A100); 512-token prefill saturating an A100 (13B-class);
  Splitwise's ~1.4x / ~20% (its own model/GPU mix). Directions (prefill
  compute-bound/parallel, decode memory-bandwidth-bound/sequential) are stated
  flatly as settled.
- No chart: no clean sourced TTFT-vs-prompt-length numeric series exists in the
  evidence, so the felt "pause grows with prompt length" claim is carried in
  prose only. The one furniture figure-family used is a comparison table of the
  two phases; a note pre-empts the common wrong explanation.
- The open frontier is marked honestly in its own section: mechanism settled,
  hardware organization not — disaggregation (Splitwise/DistServe) vs fusion
  (Sarathi-Serve chunked prefill), presented as a live primary-vs-primary
  disagreement, not a solved question.
- The wrong explanation is pre-empted in "The step an explanation skips": decode
  is memory-bandwidth-bound, not compute-bound, and the KV cache is not optional.
- Prior lessons are linked, not re-taught: `attention` (keys/values) and
  `autoregressive-generation` (sequential one-token-at-a-time generation) appear
  as prose links and Background rows. The dollar cost of output tokens gets one
  sentence and is handed to the cost-per-token lesson with no cross-link (that
  piece is not yet published).
- Headline and dek avoid the series' banned molds: no "A model that X never Y" /
  declarative-mechanism frame, no colon subtitle, no comma-triad or
  semicolon-reversal dek. The single licensed contrast is spent on the
  cost-asymmetry inversion.

## Open questions for the orchestrator
None blocking. One note for the editor's awareness: `autoregressive-generation`
already touches the KV cache and decode's memory-bandwidth cost (Shazeer). This
lesson deliberately treats that as taught ground (linked) and claims new ground
in the prefill/decode *split*, the cache's memory *footprint* and *sizes*, the
TTFT/ITL metric mapping, the cost inversion, and the disaggregation-vs-fusion
frontier. If the desk judges the overlap too close, that is a commission-level
scope call, not an evidence gap.

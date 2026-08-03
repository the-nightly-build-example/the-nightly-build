# review-brief: the-mechanics/prefill-and-decode (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/writer/01/brief.md — the exact writer brief (for instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/writer/01/draft-handoff.md
- Article: /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/library/the-mechanics/prefill-and-decode.html
- Template context dir: /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/editor/01/editorial-review.md

Recent-pattern notes (this series, break formulas): the series overuses the
"A model that X never Y" / "The instant a model writes a token" declarative-
mechanism headline (tool-use, losing-the-thread, autoregressive-generation) and
comma-triad / semicolon-reversal deks. Check headline, dek, and headings against
these; a repeated shape is a formula to break.

This round's focus:
- Verify every magnitude carries its stated model/GPU conditions and reads as
  illustrative, not a universal constant (evidence flags 800 KB/token as
  OPT-13B FP16; 128:1 decode:prefill as Mistral-7B on one A100; etc.). A number
  without its conditions is a finding.
- Confirm directional claims (prefill parallel/compute-bound; decode
  sequential/memory-bandwidth-bound; KV cache as cause of the latency) are
  stated as settled and are correct against the evidence's primaries.
- Confirm the open frontier (disaggregation vs chunked-prefill fusion) is marked
  as unsettled, not smoothed over.
- Watch the overlap with the published autoregressive-generation lesson: the new
  ground must be genuinely new (prefill/decode split, cache footprint, TTFT/ITL,
  cost inversion, disaggregation). If a paragraph re-teaches taught ground, cut
  or route it.
- No chart is expected (no sourced TTFT-vs-length series existed). If one was
  added, verify its provenance hard.

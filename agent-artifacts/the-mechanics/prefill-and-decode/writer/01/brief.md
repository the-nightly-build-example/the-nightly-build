# writer brief: the-mechanics/prefill-and-decode (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/commission.md — assignment, angle, boundaries
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/writing-coach/01/voice-guide.md — register and licensed forms
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/researcher/01/evidence.md — the complete claim set; use its Numbers exactly
- Article to edit: /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/library/the-mechanics/prefill-and-decode.html
- Template context dir: /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/writer/01/draft-handoff.md

Proof: run from repo root /home/user/the-nightly-build using the checkout's nb.
  Iterate: ./nb check --series the-mechanics .nb-work/the-mechanics/prefill-and-decode/library/the-mechanics/prefill-and-decode.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout --no-check-links
  Final (BLOCK: 0, links included): same without --no-check-links. Run ./nb stamp before the final check.

This round's focus (decisions the inputs do not fully carry):
- Every magnitude in the evidence is illustrative and model/GPU-specific (e.g.
  800 KB/token is OPT-13B FP16; 128:1 decode-to-prefill is Mistral-7B on one
  A100). Carry each number WITH its stated conditions and label it illustrative,
  never as a universal constant. Directions (prefill parallel/compute-bound,
  decode sequential/memory-bandwidth-bound) are settled and can be stated flatly.
- Do NOT build a chart: there is no clean sourced TTFT-vs-prompt-length numeric
  series in the evidence. The qualitative claim (TTFT grows with prompt length)
  is supported; a number series is not in hand. If you want a chart, you would
  need a new sourced series first — for this round, prose only.
- Mark the one genuine open frontier honestly: the mechanism is settled, but its
  hardware organization is not — Splitwise/DistServe disaggregate prefill and
  decode onto separate machines while Sarathi-Serve fuses them with chunked
  prefill (a primary-vs-primary disagreement). That is the "open question" the
  desk asks you to flag.
- Pre-empt the common wrong explanation the evidence flags (that decode is
  compute-bound or the KV cache is optional).
- Build on published lessons by LINKING, not re-teaching: attention
  (the-mechanics/attention) and autoregressive-generation
  (the-mechanics/autoregressive-generation) are in the library — link in prose
  or Background. The dollar cost of output tokens is another lesson; give it one
  sentence and do not price it here (no cross-link exists yet; that piece is not
  published).
- Headline/dek: avoid this series' "A model that X never Y" / "The instant a
  model writes a token" declarative-mechanism frame and the comma-triad /
  semicolon-reversal dek. Spend the piece's single licensed contrast on the
  cost-asymmetry inversion (long prompt cheap, short reply expensive) per the
  voice guide.
- nb-meta: date 2026-08-03, harness, writer model you ran as; tags array empty.

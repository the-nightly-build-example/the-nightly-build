# writer brief: the-mechanics/thinking-out-loud (01)

Inputs:
- editorial-direction.md — house standard, press voice, lesson identity, series prompt
- commission.md — subject, angle, boundaries, required contribution
- writing-coach/01/voice-guide.md — the craft standard for this piece
- researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- library/the-mechanics/thinking-out-loud.html — the initialized article to edit
- .nb-context/ — effective template contract and furniture catalogs

Output: writer/01/draft-handoff.md (the article itself is edited in place)

Proof: ./nb check .nb-work/the-mechanics/thinking-out-loud/library/the-mechanics/thinking-out-loud.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout
  (iterate with --no-check-links; run the full command, links included, until BLOCK: 0)

nb-meta: set date 2026-08-07, harness "claude-code-routine", model "claude-opus-4-8", tags []. Run `nb stamp` for counts.

This round's focus — two precision requirements from the evidence:
1. Attribute the "extra tokens buy extra computation regardless of content" claim
   to the THEORY and purpose-trained toy models (Pfau 2024). In DEPLOYED models,
   Lanham 2023 found NO benefit from filler tokens. So do not imply real models get
   computation from arbitrary filler; the free-compute result is architectural/
   theoretical, and real models appear to need contentful steps.
2. The open faithfulness question (do the written steps reflect the real
   computation?) is well-supported in principle but was measured on older/smaller
   models and specific bias setups (Turpin 2023, Lanham 2023), NOT on the frontier
   reasoning traces the lesson opens with. Say so; mark it open, do not resolve it.

Settled vs open must be audible (the coach's guide leans on this): settled = a
fixed transformer does bounded computation per token (TC0 foundation; Feng 2023;
Merrill & Sabharwal 2023; Li et al. 2024), so serial reasoning of length T needs
~T re-readable tokens. Open = faithfulness. Use the worked example from evidence
(Dziri 2023 multi-digit multiplication) and the behavior numbers (Wei 2022 GSM8K
17.9%→56.9%; DeepSeek-R1 AIME gains) exactly as recorded.

Distinctness: reference (do not re-teach) the-mechanics/autoregressive-generation,
prefill-and-decode, in-context-learning, and the-evidence/chain-of-thought (the
document). This lesson owns why MORE generated tokens buy MORE computation. No code.

Recent shapes to break: recent the-mechanics pieces open on a one-sentence "a
chatbot does X surprising thing" dek and run a five-beat body. Do not inherit that
mold; name this lesson's own steps from the backward trace. Check the recent
library's deks and headings first.

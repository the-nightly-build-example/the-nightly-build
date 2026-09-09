# Commission: the-mechanics/speculative-decoding

## Authorized work
Scheduled `nb duty` for 2026-09-09 returned `the-mechanics` in open mode. This
commission authorizes exactly one lesson on speculative decoding. Template:
lesson. Series floor: >=8 sources, >=4 primary, >=1 secondary. Word band
1200-2200. Verified against the full published library: `first-token-latency`,
`prefill-and-decode`, `nondeterminism`, `sampling-temperature`, and
`tokens-per-second` (an instruments piece) are covered; speculative decoding is a
genuine gap.

## Why this behavior, and the mechanism
The Mechanics works backward from a behavior to its cause. The behavior: the same
open model, given the same prompt, can return the identical text two to three
times faster on one service than another, and its tokens often arrive in bursts
rather than a steady drip. Work down to the cause:
1. A model normally emits one token per forward pass, and a forward pass over the
   big model is the expensive step. So speed looks capped at one big-model pass
   per token.
2. Speculative decoding breaks that cap without changing the output. A small,
   cheap "draft" model proposes several next tokens quickly. The big "target"
   model then scores all of those proposed positions in a single forward pass
   (it can, because a transformer processes a whole sequence in parallel), and
   accepts the longest run of proposed tokens that matches what it would have
   produced anyway, rejecting the rest.
3. Why the output is identical: the acceptance test is built so the accepted
   tokens are distributed exactly as the target model's own decoding would be
   (greedy: accept while the draft's argmax equals the target's; sampling: a
   modified-rejection step preserves the target's distribution). So you get
   several tokens for roughly one big-model pass when the draft guesses right,
   and a pause (one wasted big-model pass) when it guesses wrong. That is the
   burstiness.
Ground floor: a transformer scores many positions in one parallel forward pass,
so verification is cheap relative to generation. Mark settled vs open: the
speedup is settled engineering a provider chooses; how much you get depends on
how often the draft agrees with the target, which varies by workload.

## What the lesson teaches (short, complete)
1. The bottleneck: one big-model forward pass per token, and why that seems to
   cap speed. Define "forward pass" and "token" in plain words.
2. The trick: a draft model proposes, the target verifies many positions in one
   pass, and accepts the matching run. A worked example of a few proposed tokens,
   some accepted, one rejected.
3. Why quality does not change, and what sets the speedup: the acceptance rule
   preserves the target's own output distribution; the gain rides on the draft's
   agreement rate, so it is workload-dependent and provider-chosen.

## Boundaries and neighbors
- Distinct from `first-token-latency` (time to first token), `prefill-and-decode`
  (reading the prompt vs writing the reply), `nondeterminism` and
  `sampling-temperature` (why outputs vary). This is how identical output is
  produced faster. Do not re-teach attention from scratch; link where useful.
- Tonight's edition also ships: the-evidence/react-reasoning-and-acting,
  the-instruments/model-flops-utilization, what-could-go-wrong/flash-crash-risk,
  when-ai-breaks/cigna-pxdx.
- Required contribution: the reader leaves able to explain why a provider can
  serve the same model, same output, two to three times faster, down to the
  parallel-verification step, and can spot the claim that speculative decoding
  changes what a model says (it does not).

## Sources plan
Primary: Leviathan et al., "Fast Inference from Transformers via Speculative
Decoding" (Google, 2023) and Chen et al., "Accelerating Large Language Model
Decoding with Speculative Sampling" (DeepMind, 2023) for the method and the
distribution-preserving proof; an inference-stack doc that ships speculative
decoding (a serving framework's official documentation) for how it is deployed
and the acceptance/rejection mechanics; optionally a later variant (Medusa /
EAGLE) as a primary refinement. Secondary: a careful explainer. Every URL must
resolve; cite only what was read. NOTE: github.com is blocked here (egress 403) —
use arXiv and official hosted docs, not GitHub, as sources.

## Recent patterns to break (habits, not rules)
- Mechanics headlines are behavior-first (keep). Avoid the semicolon-reversal dek
  mold ("gpt-3.5-turbo-instruct plays legal chess; the chatbots don't"); no
  suspended-question or comma-triad dek. Do not name a final body section "How
  far the explanation reaches" (that shape recurred). Vary heading construction.

## Production policy (recorded)
Profile balanced. Stages, none `required`: writing-coach effort low, researcher
effort high, writer effort medium, editor effort high; model tier "capable".
Executed with capable (Claude Opus-class) models at closest available effort. No
`required` directive traded down.

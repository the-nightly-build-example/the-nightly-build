# Commission: the-instruments/model-flops-utilization

## Authorized work
Scheduled `nb duty` for 2026-09-09 returned `the-instruments` in open mode. This
commission authorizes exactly one lesson on Model FLOPs Utilization (MFU), the
training-efficiency number labs report. Template: lesson. Series floor: >=8
sources, >=4 primary, >=1 secondary. Word band 1200-2200. Verified against the
full published library: `training-compute`, `tokens-per-second`, `cost-per-token`,
`energy-per-query`, and `parameter-count` are covered; MFU (achieved vs peak
FLOPs) is a genuine gap.

## Why this measurement, and the honest angle
The Instruments teaches how a public number is made and what it can and cannot
support. MFU is the number a lab cites to say a training run used its hardware
well: the ratio of the FLOPs the run actually did for useful model math to the
hardware's theoretical peak FLOPs over the same wall-clock time. Explain it step
by step: count the model FLOPs per token (the standard 6N-per-token estimate for
an N-parameter dense model, times tokens), divide by (peak FLOPs of the chips x
seconds). Then show what it cannot support. The denominator is the catch: "peak
FLOPs" is a spec-sheet number that depends on numeric precision (fp32 vs bf16 vs
fp8) and on whether the vendor's headline figure assumes structured sparsity, so
two MFU numbers can use different peaks and are not comparable; and MFU says
nothing about whether the FLOPs were spent on the right computation. Include a
real case where the number misled: comparing MFU across runs on different chips
or precisions, or reading a chip's sparse-fp8 peak TFLOPS as if it were the dense
number the run could reach (a gap of 2x or more). Draw the clean line between MFU
and adjacent numbers: total training-compute (already a lesson) is the numerator's
scale; tokens-per-second is inference throughput; MFU is a utilization ratio.

## What the lesson teaches (short, complete)
1. How MFU is computed: model FLOPs (the 6N-per-token estimate, defined in plain
   words) over peak-FLOPs-times-time, with a worked number from a real reported
   run (e.g. PaLM's reported MFU).
2. Why the denominator makes MFU slippery: peak FLOPs depends on precision and on
   the sparsity assumption in a vendor's headline figure, so two MFU numbers can
   quote different peaks. Worked with the dense-vs-sparse or bf16-vs-fp8 gap.
3. What MFU can and cannot tell you: it bounds how much faster a run could get on
   the same chips, but says nothing about whether the compute was well spent, and
   is not comparable across setups unless the peak baseline is stated.

## Boundaries and neighbors
- Distinct from `training-compute` (total FLOPs / regulatory thresholds),
  `tokens-per-second` (inference throughput), `parameter-count`,
  `cost-per-token`, `energy-per-query`. Assume algebra; define FLOP and "peak
  FLOPs" in plain words on first use.
- Tonight's edition also ships: the-evidence/react-reasoning-and-acting,
  the-mechanics/speculative-decoding, what-could-go-wrong/flash-crash-risk,
  when-ai-breaks/cigna-pxdx. Stay on the measurement.
- Required contribution: the reader leaves able to compute MFU in principle, say
  why two MFU figures may not be comparable, and spot a peak-FLOPs denominator
  that inflates the number.

## Sources plan
Primary: a training report that defines and reports MFU (the PaLM paper is the
canonical one; Megatron-LM / other model reports also report it), for the
definition and a real figure; a vendor datasheet (e.g. an NVIDIA GPU spec) that
shows peak TFLOPS with and without sparsity and across precisions; a primary
source for the 6N-per-token FLOPs estimate (the Kaplan or Chinchilla scaling
paper, or the Transformer-FLOPs derivation). Secondary: a careful explainer of
MFU / hardware utilization. Every URL must resolve; cite only what was read.
NOTE: github.com is blocked here (egress 403) — prefer arXiv/official vendor
docs, not GitHub, as sources. Verify the reported MFU figure and any peak-FLOPS
numbers against the primary source.

## Recent patterns to break (habits, not rules)
- This desk's headlines are counterintuitive numeric facts (keep that), but avoid
  the recurring molds "The number that ..." and "X is a Y that pays out for Z"
  (chatbot-arena-elo: "Chatbot Arena's Elo is a preference vote that pays out for
  style"; mteb; alpacaeval). Commit the headline to one concrete surprise about
  MFU.
- Deks: avoid the "X is [definition], and [limitation]" mold (auroc,
  calibration-error). Do not name a final body section "How far the X reaches".
  Vary heading construction.

## Production policy (recorded)
Profile balanced. Stages, none `required`: writing-coach effort low, researcher
effort high, writer effort medium, editor effort high; model tier "capable".
Executed with capable (Claude Opus-class) models at closest available effort. No
`required` directive traded down.

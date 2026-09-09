# Draft handoff: the-instruments / model-flops-utilization

## Status
Filled the starter HTML in place. Self-proof clean: `nb check ... --series
the-instruments --library <checkout>` returns BLOCK 0, WARN 0, verdict
PUBLISHABLE. Stamped: 1,811 words, 8 sources, 8 min read.

## Headline and dek
- Title: "PaLM's training ran at 46 percent efficiency, or 58, depending on which
  FLOPs you count"
- Dek (identical to the rendered dekline): "A lab reports it to show a training
  run used its chips well, and precision plus a sparsity footnote can swing the
  peak underneath it fourfold on a single card."

The headline commits to one concrete, published surprise (PaLM's single run
carries two honest utilization numbers) and names the actor. It avoids the
desk's flagged molds ("The number that ...", "X is a Y that pays out for Z").
The dek supplies the deeper catch, the peak-FLOPs denominator, and dodges the
"X is [definition], and [limitation]" mold used by auroc/calibration-error.

## Structure (orientation + 3 flex, body first, bookends last)
1. `orientation` — "A fraction with a measured top and a spec-sheet floor."
   Defines FLOP and peak FLOPs in plain words on first use; frames MFU as a
   ratio; anchors on PaLM 46.2% / 57.8%. Stat strip (46.2%, 238.3K tok/s, 6,144
   chips).
2. `counting-flops` — "Six FLOPs per parameter, per token." Teaches the
   numerator: 2N forward, 6N round trip (Kaplan), 6ND checked to ~10% by
   Chinchilla. Worked PaLM number reproduces ~46% from six figures. Bare display
   equation for the MFU ratio; inline math for C ≈ 6N. Links parameter-count and
   training-compute in prose rather than re-teaching.
3. `the-denominator` — "The denominator the chipmaker defines." The catch:
   precision and structured sparsity. H100 table (tf32/bf16/fp8, dense vs
   sparse). Worked trap: same run reads 47% or 12% depending on which spec-sheet
   line is the denominator (3,958 is 4x the ~990 dense bf16 peak).
4. `the-limits` — "What a utilization number cannot see." What MFU bounds
   (headroom, ~2x for PaLM; same-chip yardstick; Megatron 56% on A100s;
   GPT-NeoX ~150 of 312) versus what it cannot (whether FLOPs were well spent;
   MFU>HFU gap from rematerialization; not comparable across chips/precision;
   Epoch's assume-30% guidance).

## Furniture used, and why
- Stat strip (orientation): the three headline numbers the PaLM worked example
  rests on, each cited in adjacent prose.
- Bare display equation (counting-flops): the MFU ratio in one line, the
  derivation the whole lesson leans on. Inline math span for C ≈ 6N.
- Table (the-denominator): the H100's dense-vs-sparse peaks across three
  precisions. A comparison is the point, so it earns the component.
No chart (no committed chart-N.py needed; the numbers are few and exact). No pull
quote, note, or claim card: none earned its place here.

## Sources (8; 6 primary, 2 secondary)
Numbered in order of first appearance. s1 PaLM (def + 46.2/57.8 + 238.3K + 6,144
chips), s2 Kaplan (2N / 6N), s3 Chinchilla (6ND ~10%), s4 Google Cloud TPU v4
(275 TFLOP/s), s5 NVIDIA H100 (peaks + sparsity footnote), s6 Megatron/Korthikanti
(MFU/HFU + 56% + A100 312), s7 EleutherAI Transformer Math (secondary), s8 Epoch
AI (secondary). Every URL HTTP-checked live. Full record in
`researcher/01/evidence.md`.

## Notes for the editor
- The 6N worked number lands at ~45.7% and the paper reports 46.2%; I state
  plainly that PaLM's own count adds a small attention term on top of 6N. Not
  fabricated, and the gap is explained rather than hidden.
- The 47%/12% figure in the-denominator is an illustrative computation off
  NVIDIA's own 4x denominator range, framed as an example ("say, 47 percent"),
  not attributed to a specific published run.
- No em-dashes used (well under the limit of 4). No banned terms.
- Bookends written after the body; the opener's three promises (compute an MFU,
  see 46% fall out of six numbers, catch the spec-sheet choice) are each resolved
  in the takeaway. Body addresses no one and never mentions the lesson.

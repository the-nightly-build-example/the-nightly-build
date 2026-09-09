# Editorial review: the-instruments / model-flops-utilization (01)

## Decision
Approved: no required change remains. Two edits made in place; both are settled
from evidence.md, so nothing routes back to the writer.

## Numbers re-verified against evidence.md (all trace)
- PaLM worked example: 6N = 6 x 540e9 = 3.24e12/token; 238,300 tok/s x 3.24e12 =
  7.72e17; 6,144 x 275e12 = 1.69e18; ratio 0.457. Matches evidence. The draft's
  "you get 0.46" and "reproduces the reported 46.2 percent almost exactly" is the
  bare-6N ~45.7% honestly rounded, and the text names the reason for the gap
  (PaLM's count adds an attention term). Kept as written.
- 46.2% MFU / 57.8% HFU (S1), 238.3K tok/s (S1), 6,144 chips (S1): correct.
- 275 TFLOP/s peak cites s4 = Google Cloud TPU v4 docs, the source actually read.
  evidence.md is explicit that the benchmarking PDF did not extract and was not
  cited. Citation is correct.
- H100 table: TF32 495/989, bf16 990/1979, fp8 1979/3958; dense = half of the
  with-sparsity headline; bf16-dense ~990 to fp8-sparse 3,958 is the 4x swing.
  All match S3.
- 47%/12% illustration: framed as "reporting, say, 47 percent" off NVIDIA's own
  denominator range (47/4 = ~12), not attributed to a real run. Reads correctly
  as an illustration. Kept.
- Megatron 56% on 2,240 A100s (S4), GPT-NeoX ~150 of 312 (S7), Epoch "assume
  ~30%" and the 30-to-75% band (S8): all match.
- Source list is numbered by first appearance (renumbered vs evidence.md's S-IDs,
  as the handoff states). Checked every inline citation against the HTML's own
  ordered list: each points to the correct document.

## Edits made (both in the final body section, "What a utilization number cannot see")
1. Factual correction. The draft read "A100s peak near 312 ... while H100s peak
   near 990, so a 56 percent MFU on the first and a 46 percent on the second."
   That attributes PaLM's 46.2% to an H100. PaLM ran on TPU v4 (275 TFLOP/s); no
   H100 run at 46% exists in evidence. Rewrote to keep each figure on its real
   hardware: Megatron's 56% against an A100's 312, PaLM's 46% against a TPU v4's
   275, with the H100's ~990 named as the illustrative larger denominator. Cites
   now s6 (A100 312), s4 (TPU v4 275), s5 (H100 990).
2. Cut the body's closing sentence, "The number is a ratio with a soft floor,
   and it is worth precisely as much as the peak printed beneath it." It restates
   the denominator thesis to grade the argument rather than continue it, which
   the press rule (no restate-the-finding close) and the recent-pattern note
   forbid, and it fails the slop noun-replacement test as a generic aphorism.
   Deleted, not repaired. The body now closes on the concrete, sourced Epoch AI
   observation. Also dropped the filler adverb "simply" from that sentence.

## Checks that passed without change
- Headline: subject + verb + numeric surprise, actor named, no colon subtitle,
  avoids the desk's flagged molds. Kept.
- Dek: adds the denominator/sparsity catch the headline omits; not the
  "X is [definition], and [limitation]" mold, not a semicolon reversal or a
  comma-and triad. Kept.
- Headings vary in construction; none is a "How far the X reaches" or a
  scaffolding slot. Kept.
- "FLOP" and "peak FLOPs" defined in plain words on first use (orientation).
  parameter-count, training-compute, tokens-per-second linked in prose, not
  re-taught. Correct.
- Three-part lesson shape intact; bookends address the reader (allowed), body
  addresses no one and never names the lesson. Takeaway lands the judgment
  ("cannot tell you the run was training anything worth the electricity").
- Edge sentences run through the slop test; the surviving vivid closers
  ("without anyone touching a transistor") depend on the subject's own nouns and
  carry real content.

## Claims hedged or cut for lack of a source
None. Both edits were resolvable from evidence.md; no claim needed hedging and no
source was invented.

# editor brief: the-instruments/model-flops-utilization (01)

Inputs (read each):
- editorial-direction.md — the concatenated governing standard.
- commission.md — assignment, teach-list, boundaries, sources plan.
- writer/01/draft-handoff.md — the writer's account of choices and open risks.
- writing-coach/01/voice-guide.md — how this piece should sound.
- researcher/01/evidence.md — the source record; every body claim traces here,
  each cited URL must resolve.
- library/the-instruments/model-flops-utilization.html — the article to edit.

Output: editorial-review.md (this directory) — cuts/changes and your decision.

Proof: after editing, run
  ./nb stamp .nb-work/the-instruments/model-flops-utilization/library/the-instruments/model-flops-utilization.html
  ./nb check .nb-work/the-instruments/model-flops-utilization/library/the-instruments/model-flops-utilization.html --series the-instruments
Leave verdict PUBLISHABLE, no BLOCK, word count 1200-2200.

Recent-pattern notes for this desk:
- Headlines are counterintuitive numeric facts (fine). Dek molds this desk has
  over-used: "The number that ..." and "X is a Y that pays out for Z"
  (chatbot-arena-elo, mteb, alpacaeval), and the "X is [definition], and
  [limitation]" mold (auroc, calibration-error). Check the dek.
- Reject a final section named "How far the X reaches"; check headings vary.
- Press rule: the takeaway lands the judgment; the body must not close on a
  restate-the-finding block.

This round's focus (numbers are the whole lesson — verify hard):
- Re-verify EVERY figure against evidence.md: the 6N-per-token worked number
  (~45.7%) vs PaLM's reported 46.2% and the small attention-term gap the writer
  says is explained in-text; the H100 dense-vs-sparse / precision peaks and the
  "4x" swing; the 47%/12% illustrative computation (must read as an illustration
  off NVIDIA's own denominator range, NOT attributed to a real run); the
  46.2 vs 57.8 MFU/HFU gap, Megatron ~56%, and any Epoch "assume 30%" figure.
  If evidence.md is not unambiguous on a figure, hedge or cut rather than ship it.
- The 275 TFLOP/s TPU v4 peak: the writer says the TPU benchmarking PDF didn't
  extract and the figure comes from official Google Cloud TPU v4 docs — confirm
  the citation points to the source actually read.
- "FLOP" and "peak FLOPs" must be defined in plain words on first use; assume only
  algebra. training-compute / tokens-per-second / parameter-count linked, not
  re-taught.
- Slop at edges; the last sentence hardest. Delete, do not repair.
Nothing else.

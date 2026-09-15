# editor review-brief: the-instruments/training-cost (editor/01)

Inputs (read in the order your skill names):
- ../../writing-coach/01/voice-guide.md — read first.
- ../../editorial-direction.md — house standard, the paper's voice, the series prompt.
- ../../commission.md — the assignment, boundaries, required contribution.
- ../../writer/01/brief.md — the exact writer brief (check authored text against it for leaks).
- ../../researcher/01/evidence.md — open on the skeptic read; recompute figures against it.
- ../../writer/01/draft-handoff.md — the original-work sentence; open on the reader read.
- Article under edit: /home/user/the-nightly-build/.nb-work/the-instruments/training-cost/library/the-instruments/training-cost.html
- Its committed furniture: library/the-instruments/training-cost/chart-1.py + chart-1.png, and asset-1.png (a crop of the DeepSeek-V3 report's Table 1). Inspect both.
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/training-cost/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-instruments/training-cost/agent-artifacts/the-instruments/training-cost/editor/01/editorial-review.md

Proof (the orchestrator stamps and runs this after your edits): from repo root /home/user/the-nightly-build:
  ./nb check .nb-work/the-instruments/training-cost/library/the-instruments/training-cost.html --series the-instruments

Recent-pattern notes (flag any formula against these):
- Heading mold "The number is the model plus the effort" and openers "A number for how well X" recur in this series.
- Closer mold "What a high score does not promise" / "Where the same X lives" recurs.
- Comma-triad and semicolon-reversal dek molds are banned by spec/headlines.md.

This round's focus:
- Recompute every load-bearing figure against the evidence: 2.788M H800 GPU-hours, the assumed $2/GPU-hour, the $5.576M total and its Table 1 stage split; and Nvidia's 27 Jan 2025 move ($142.62 -> $118.42, 16.97%, ~$589B, "largest single-day company loss on record"). Check the headline's ratio ("more than 100,000 times DeepSeek's training bill": ~589e9/5.576e6 ≈ 105,600).
- Guard the honesty of the cross-number comparison: a one-day market-capitalization move and a training-run bill are different kinds of number. The headline and prose may set them side by side, but must not imply they are the same quantity or that the bill caused the loss. Confirm the piece keeps "no source ties the loss to that reading alone" (partly, not solely) and that reported fact / analyst estimate / synthesis stay distinct.
- Confirm the attribution corrections held: DeepSeek's exclusion caveat quoted to what it actually says (prior research + ablations only); the salaries/hardware-capital framing attributed to SemiAnalysis and Bernstein's Rasgon, not to DeepSeek.
- Inspect the chart (labels, axes, scale, the Friday->Monday close honestly drawn) and the Table 1 asset crop (retains the GPU-hours/cost rows the argument spends, omits clutter; caption is a factual cited label). Route any chart/asset fix to the writer.
- The lesson allows only its two bookends to address the reader; hold all other prose to no-self-reference.

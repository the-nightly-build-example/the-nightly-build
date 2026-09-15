# writer brief: the-instruments/training-cost (01)

Inputs:
- ../../editorial-direction.md — house standard, the paper's voice, the series prompt.
- ../../commission.md — the measurement, teaching steps, boundaries, required contribution, source floor, recent-pattern habits to break.
- ../../writing-coach/01/voice-guide.md — how this piece should sound (read before drafting).
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers exactly and address its Contradictions.
- Initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-instruments/training-cost/library/the-instruments/training-cost.html
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/training-cost/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-instruments/training-cost/agent-artifacts/the-instruments/training-cost/writer/01/draft-handoff.md

Proof (from repo root /home/user/the-nightly-build; iterate with --no-check-links, final with links until BLOCK: 0):
  ./nb stamp .nb-work/the-instruments/training-cost/library/the-instruments/training-cost.html
  ./nb check .nb-work/the-instruments/training-cost/library/the-instruments/training-cost.html --series the-instruments

This round (honor these corrections from the evidence record):
- Attribute the exclusions correctly. DeepSeek-V3's own caveat excludes only "prior research and ablation experiments on architectures, algorithms, or data" — it does NOT say salaries or data-acquisition. The "salaries / hardware capital (~$1.6B server capex, >$500M hardware, ~50,000 GPUs)" framing belongs to analysts (SemiAnalysis, Bernstein's Stacy Rasgon), so present those as analyst estimates with their owners, kept distinct from DeepSeek's words.
- Keep the causal claim bounded. No source isolates the $5.6M misreading as the sole cause of Nvidia's ~$589B one-day loss (the sell-off also ran on R1's performance, the app topping the store, and chip-demand fears). Keep the "moved partly on" hedge; do not claim sole cause. Use the verified figures: $142.62 -> $118.42, a 16.97% fall, ~$589B, the largest single-day company loss on record.
- The number itself is GPU-hours x an assumed price: 2.788M H800-hours x an assumed $2/GPU-hour = ~$5.576M, final run only (Table 1 stage split available). Teach both inputs as choices.
- Link, do not re-teach: no dedicated GPU-hours lesson exists; the closest is the-instruments/tokens-per-second; also the-instruments/training-compute (FLOPs), parameter-count, cost-per-token, and the-evidence/deepseek-r1 (which already fixes $5.576M to V3, not R1). Use Background/prose links.
- Break the "The number is the model plus the effort" heading mold and the "Where the same X lives / What a high score does not promise" closer mold. Fresh dek, no comma-triad / semicolon-reversal.
- nb-meta: date "2026-09-15", harness "claude-code-routine", model "claude-sonnet-5".

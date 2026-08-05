# Draft handoff: the-instruments/parameter-count (01)

## Original work

The piece decomposes a single parameter count into the two separate costs its
owning sources only ever state apart — the total as the memory footprint that
must stay resident, the active count as the per-token compute — and on one
isolated three-model comparison shows that the very figure making DeepSeek-V3
look four times GPT-3's size (671B vs 175B) simultaneously makes each of its
tokens cheaper to compute (37B vs 175B), a juxtaposition none of the primaries
draws.

## Proof

`./nb check ... --series the-instruments --library /home/user/library-checkout`
(final pass, links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
No warnings intentionally left. `nb stamp`: words 1671, reading 7 min, sources 9.
Chart rendered with `nb chart` and inspected; preview site builds with the draft
merged (100 articles).

## Sources and figures

9 sources (8 primary, 1 secondary), numbered in first-citation order; floor
(>=8, primary>=4, secondary>=1) met. Every headline figure is read off the
model's own paper, card, or announcement. One committed chart
(`parameter-count/chart-1.py` -> `chart-1.png`): total vs active per token
across GPT-3, Mixtral, DeepSeek-V3, all inputs primary-owned. One worked table
for the 56 / 46.7 / 12.9 arithmetic.

## Both overclaim cautions honored

- Active tracks compute/speed, not memory: the "The total is still the memory
  bill" section states total drives VRAM (every expert resident) and active
  drives per-token compute; the draft never calls active "the real cost."
- Chinchilla is compute-optimal allocation, not parameter irrelevance: the draft
  states that within one family (GPT-2 to GPT-3) more parameters did buy
  capability, and frames Chinchilla as the equal-compute allocation result, not
  "the count tells you nothing."

## Open questions

None blocking. The unverified per-expert sub-breakdown (attention ~5B, each FFN
~5.25B) flagged in the evidence record was deliberately not used; the table and
prose carry only primary-owned figures plus the plain 8x7 arithmetic. If the
editor wants the crux sentence promoted, "The total is the memory the model
needs. The active count is the speed and compute each token costs." sits in the
takeaway and could become a pull quote; I left the furniture at two figures to
keep the page reading as an article.

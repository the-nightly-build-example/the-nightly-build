# researcher brief: the-mechanics/first-token-latency (02)

Inputs: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editorial-direction.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editor/01/editorial-review.md   the two source-fidelity findings to repair
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/researcher/01/evidence.md   your prior record; preserve still-valid work, do not overwrite it
Output: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/researcher/02/evidence.md

Apply exactly the two findings in editor/01's review; change nothing else the
record already got right.

1. Feed-forward / projection complexity. The record and draft attribute
   O(n*d^2) for the feed-forward and Q/K/V-projection cost to Vaswani et al.
   Table 1, but Table 1 lists O(n*d^2) only for the recurrent layer and has no
   feed-forward row. Supply a primary that actually owns the O(n*d^2) per-layer
   feed-forward / projection cost (the Transformer FLOPs accounting in a primary
   such as Kaplan et al.'s scaling-laws appendix, or another source that states
   the per-token matmul cost), or, if the crossover argument can rest only on
   Table 1's actual contents, state precisely what Table 1 does and does not
   support so the writer can recast to it. Give the exact locator either way.

2. Network latency. The record's Contradictions entry says Anthropic's latency
   page lists network latency among the factors; the page does not (it names
   model size, prompt complexity, and underlying infrastructure). Correct the
   record: the network-latency point survives on Artificial Analysis (the
   existing source 11). Fix the attribution so no claim rests on the Anthropic
   page for network latency.

Write a complete new evidence.md that preserves the still-valid prior record and
clearly records these two corrections. Confirm every URL still resolves to the
source's own page. The record meets spec/slop.md.

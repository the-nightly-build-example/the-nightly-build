# writer brief: the-mechanics/first-token-latency (02)

Inputs: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editorial-direction.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writing-coach/01/voice-guide.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/researcher/02/evidence.md   the corrected record; supersedes researcher/01
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editor/01/editorial-review.md   the required-work items to apply
        .nb-work/the-mechanics/first-token-latency/library/the-mechanics/first-token-latency.html   the article as the editor left it; edit in place
        .nb-work/the-mechanics/first-token-latency/.nb-context/
Output: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writer/02/draft-handoff.md
Proof:  ./nb check .nb-work/the-mechanics/first-token-latency/library/the-mechanics/first-token-latency.html --series the-mechanics --library /home/user/library-checkout

Apply exactly the editor/01 required-work items, using researcher/02's corrected
record. Preserve the editor's direct edits already in the article and all settled
work; do not independently expand the claim set.

- Recast the crossover argument so the O(n·d²) feed-forward/projection term is
  attributed to Kaplan et al. (the primary that owns it, with its locator in
  researcher/02), and state Vaswani's Table 1 for exactly what it contains
  (self-attention O(n²·d) and the recurrent layer O(n·d²), no feed-forward row).
  Number the new Kaplan source in first-citation order and carry its kind.
- Fix the network-latency sentence so it rests on Artificial Analysis, not the
  Anthropic page (which does not mention network latency).
- Researcher/02 flags that Kaplan's constant-aware crossover sits near
  n_ctx ≈ 12·d_model (tens of thousands of tokens), roughly an order above the
  bare n≈d threshold. Decide whether to adopt that threshold; if the current
  wording pegs the crossover at "several thousand tokens," reconcile it with the
  record so the prose and the source agree.
- Verify the Together AI TTFT definition string is verbatim against the source
  (the editor flagged a possible mismatch); fix if needed.

This is the-mechanics: no code. Run the display-text pass, then `nb stamp` and
the full `nb check` WITH links until BLOCK: 0. Write draft-handoff.md with the
original-work sentence, the proof result, and one line per editor item resolved.

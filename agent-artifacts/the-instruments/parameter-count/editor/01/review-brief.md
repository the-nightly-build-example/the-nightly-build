# editor review-brief: the-instruments/parameter-count (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/editorial-direction.md — house standard, paper voice, series prompt
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/writer/01/brief.md — the exact writer brief (for instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/writer/01/draft-handoff.md
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/library/the-instruments/parameter-count.html — the drafted article (includes chart-1.py/chart-1.png)
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/.nb-context/ — the effective template contract

Output: /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/editor/01/editorial-review.md

If your cuts leave the article publishable, the orchestrator runs nb stamp and
the final nb check; return to the writer only if the proof needs new prose.

This round's focus:
- Two overclaims the evidence record forbids; verify the draft honors both: (1)
  active parameters track compute/speed per token but NOT memory (an MoE must
  hold all total parameters in VRAM); (2) Chinchilla shows compute-optimal
  allocation, not that parameters are irrelevant. Flag any sentence that drifts
  into "active is the real cost" or "parameters tell you nothing."
- Verify every headline figure against the evidence record's Numbers section:
  GPT-3 175B; Mixtral 46.7B total / 12.9B active and the "not 56B" reasoning
  (shared attention/embeddings); DeepSeek-V3 671B / 37B; Chinchilla ~70B beating
  ~280B at equal compute. Audit each data-nb-kind primary/secondary label.
- Inspect the committed chart: compare its numbers to the evidence record and the
  owning primaries, and read it as a reader (axes, labels, honesty).
- Recent-pattern check: the recent the-instruments deks overuse the "same X, two
  numbers" reversal (tokens-per-second "both are true"; energy-per-query "0.3 vs
  2.9"; arc-agi "scored X and Y, only the compute changed"). The total-vs-active
  split is a two-number story, so scrutinize the dek and headings for that mold
  and for comma-and-clause heading cadence; break any recurrence.
- Confirm the takeaway bookend lands judgment without a Verdict-style restatement
  block (the press bans that), and that Background/Go-deeper rows are honest.

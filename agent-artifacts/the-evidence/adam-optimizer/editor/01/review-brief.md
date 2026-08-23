# editor review-brief: the-evidence/adam-optimizer (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/commission.md
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/writer/01/brief.md — the exact writer brief
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/writer/01/draft-handoff.md
- Article: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/library/the-evidence/adam-optimizer.html
- Template context: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/editor/01/editorial-review.md

Recent-pattern notes (catch what one article cannot show):
- Series openers to break: "what 'trained with X' actually names," "X's best score
  was never the point." Confirm this piece's orientation heading is in Adam's own
  nouns.
- House catchphrases recurring across the paper, cut on sight if present: "X was
  never the point"; "where the same X still runs/lives" (a closer tic);
  self-grading punchlines. Check the dek against the banned dek molds in
  spec/headlines.md (semicolon reversal, suspended question, comma triad).
- `the-evidence/batch-normalization` already ran a "the paper's own explanation
  was wrong" story. Verify this piece does not reuse its headings or its closer,
  and that the distinction (a disproven convergence theorem, not a wrong causal
  mechanism) is doing real work.

Round focus:
- Verify the load-bearing correctness claim most skeptically: the piece must NOT
  say Adam simply "does not converge." It must hold the flawed-2015-proof fact
  apart from the later-proven convergence under large-β2 (Zhang 2022; Défossez
  TMLR). Check Reddi's named error (Γ_t not PSD) against the source.
- Check the scale honesty: the 2015 experiments are small (MNIST/CIFAR-10/IMDB,
  largest a 2×1000 MLP); the piece must not let them read as frontier-scale.
- Audit every data-nb-kind (7 primary + 1 secondary claimed) and open every
  citation href as printed.
- The writer worked Reddi's counterexample in prose rather than as a Figure-1
  asset; judge whether that is the right call or whether a source asset would let
  the reader test the central claim better.

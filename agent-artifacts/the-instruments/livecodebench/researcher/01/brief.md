# researcher brief: the-instruments/livecodebench (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — subject, angle, and source obligations

Output: evidence.md

Central primary is the LiveCodeBench paper ("LiveCodeBench: Holistic and
Contamination Free Evaluation of Large Language Models for Code", Jain et al.,
2024) and the official LiveCodeBench site/leaderboard. Read the paper. Establish
firsthand, with locators:
- Who built it and when, and the stated purpose (contamination, saturation of
  prior code benchmarks).
- The data source: which contest platforms the problems come from, how many
  problems, and how each problem carries a release date.
- The procedure: how the moving cutoff works (scoring a model only on problems
  released after its training cutoff), the pass@1 metric and how tests are used,
  and the multiple scenarios (code generation, self-repair, test-output
  prediction, code execution) — name them as the paper does.
- Concrete numbers: at least one exact reported figure with its scope (model,
  date window, scenario, version), so the article can show a score paired with
  its window.
For the "misled" case, verify one of these with a primary:
- Contamination/saturation of HumanEval or similar: find a primary or strong
  secondary documenting that models scored high partly because problems were in
  training data, and what followed. OR
- A LiveCodeBench figure reported on a favorable date window, or a cross-version
  comparison that was not like-for-like. Record exactly what was claimed, by
  whom, and why it misled.
Also record: at least one model card or launch post that cites a LiveCodeBench
number (primary for the claim it was reported), and one independent secondary on
benchmark contamination or LiveCodeBench methodology.
Search for what breaks the angle: criticism that LiveCodeBench itself can be
gamed or contaminated, or that its date windows are not a clean fix. Record
contradictions in full. Meet counts (min 8; primary >=4; secondary >=1) with
sources that change the interpretation. Confirm every URL resolves to the
document's own page.

# researcher brief: the-mechanics/lost-in-the-middle (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md   (citation standard, series territory, reader)

Output: ./evidence.md

Read the primary research. Governing primary: Liu et al. 2023, "Lost in the
Middle: How Language Models Use Long Contexts" (TACL / arXiv). Pin down the exact
experiments (multi-document QA and key-value retrieval), the U-shaped
accuracy-by-position result with numbers, which models were tested (including
extended-context variants), and the paper's own analysis of causes and of whether
larger context windows fix it.

Establish the mechanism claims the article rests on from primary or authoritative
technical sources: how positional information enters a transformer, how attention
distributes over long inputs, and any primary work attributing the effect to
positional-encoding behavior, attention dilution, or training-data structure.
Then search for what bounds or complicates the finding and record it in
Contradictions: later evaluations on newer long-context models, mitigations
(reordering retrieved passages, attention or positional-encoding changes,
prompting), and any dispute over the mechanism or the effect's persistence.
Distinguish reported measurement from interpretation throughout.

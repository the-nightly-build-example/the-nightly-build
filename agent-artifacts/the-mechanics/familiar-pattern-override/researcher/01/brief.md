# researcher brief: the-mechanics/familiar-pattern-override (01)

Inputs:
- ../../commission.md — the assignment, backward causal chain, boundaries, and the
  three neighbours this must stay distinct from.
- ../../editorial-direction.md — citation standard, series territory, declared reader.

Output: ./evidence.md

Sourcing floor (nb source-policy): at least 8 sources, at least 4 primary, at
least 1 secondary. Read the primary documents.

Primary demonstrations to read and record with locators (each with the exact
measured effect):
- Nezhurina et al., "Alice in Wonderland: Simple Tasks Showing Complete Reasoning
  Breakdown in State-Of-the-Art Large Language Models" (2024, arXiv:2406.02061) —
  verify the AIW problem, the models tested, and the accuracy collapse numbers.
- At least one study on modified classic puzzles / memorized-template override,
  read firsthand: e.g. work showing models give the canonical answer to altered
  versions of the Monty Hall problem, the river-crossing puzzle, or the surgeon
  riddle (search for peer-reviewed or arXiv papers and well-run write-ups with
  measured results). Record exact examples and numbers.
- A primary that grounds the mechanism claim (strong training prior / frequency
  effect on next-token prediction): a memorization or n-gram-frequency study, or a
  paper on models relying on surface pattern-matching over the literal prompt (e.g.
  the GSM-Symbolic / pattern-matching line, or a "reasoning vs retrieval" paper).
  Extract the plain claim, not the math.
- Primaries for BOTH sides of the open question: one arguing these gotchas show a
  real reasoning limit, and one arguing scale, reasoning-training, or prompting
  substantially reduces the effect (so it is a prior-vs-reasoning tradeoff, not a
  hard wall). Record what each actually measured.

Mechanism facts to pin (classified honestly): that a language model predicts the
most probable continuation; that canonical puzzles and their solutions appear many
times in web-scale training data; that surface similarity to the canonical version
strengthens the reversion. If a primary states these cleanly, cite it; otherwise
record the best technical source and mark it.

Numbers section: each demonstration's accuracy drop, with model, task, and owning
primary.

Contradictions: the reasoning-limit reading vs. the tradeoff reading; any evidence
that reasoning models or a warning prompt fixes it. Record both in full.

Source assets: note any figure/table (e.g. the AIW accuracy chart, a
modified-vs-canonical results table) that could carry the argument. Do not
prescribe crops.

Do not browse the repository for background. Confirm every URL resolves. Flag any
commission claim the evidence cannot support, and keep the distinction from
irrelevant-context (added distractor) and memorization (verbatim recall) clear in
the record.

# Commission: what-could-go-wrong/sharp-left-turn

## Assignment
Teach the "sharp left turn" argument at full strength, then test it against
what real systems do. The argument (named by Nate Soares / MIRI, 2022): as a
system's capabilities generalize far and fast, the safety properties trained in
at lower capability may not generalize with them, so a single broad capability
jump could carry a system past the regime where its alignment holds. Open with
the argument as its careful defenders state it and what they had seen that
worried them. Draw a sharp line between what has been shown in a working system
(narrow capability-vs-alignment generalization gaps) and what is still analogy
about a sudden, global jump in systems that do not exist yet. Bring it to the
present: who presses it, who dismisses it, and where confidence outruns proof.

## Why this argument, now
It is the argument that ties "capabilities are improving fast" to "so safety
could break," and it is distinct from the arguments this desk has already
taught. Naming it lets the reader judge the specific claim that alignment
generalizes worse than capability, rather than a vaguer "AI gets dangerous."

## Angle boundaries
- Steelman first, from the primary (Soares 2022 "A central AI alignment problem:
  capabilities generalization, and the sharp left turn," and any careful
  restatements). The reader should feel the argument's pull before any test.
- Distinctness is critical. This desk has published:
  - goal-misgeneralization (a trained agent pursues the wrong goal off-
    distribution — the CoinRun coin). That is the EMPIRICAL ANCHOR for the
    sharp left turn's "alignment generalizes poorly" premise; build on it and
    link it, do not re-run it.
  - intelligence-explosion (capabilities improve recursively/discontinuously).
    The sharp left turn is NOT that; it is about alignment failing to keep pace
    with a capability jump, whatever causes the jump. Keep them separate.
  - mesa-optimization, deceptive-alignment, instrumental-convergence,
    orthogonality-thesis. Reference as needed; do not restate.
  This lesson owns exactly one claim: capability generalizes better/faster than
  trained-in alignment, so safety can break at a jump.
- The shown/analogy line is the core deliverable. Shown: cite the specific
  generalization-gap experiments (goal misgeneralization; capability-vs-safety
  generalization studies; any measured case where a safety property degraded as
  capability rose). Analogy: the sudden, global, civilization-scale turn.
- Name no company as an authority (series rule). Cite documents. Steelman the
  skeptics from their own writing (e.g. arguments that capabilities and
  alignment are not cleanly separable, or that gradual scaling shows no such
  discontinuity). Leave the reader to decide how worried to be.

## Required contribution
The reader should be able to state the argument as its defenders would, name at
least one real, measured generalization gap that bears on it and exactly how
narrow it is, name what remains untested analogy (the sudden global turn), and
locate where today's confidence (alarm or dismissal) runs past the evidence.

## This edition (neighbors — keep distinct)
- the-evidence/resnet — a landmark paper as a document
- the-instruments/hallucination-rate — how a reliability number is manufactured
- the-mechanics/thinking-out-loud — why writing steps improves answers
- when-ai-breaks/apple-card — algorithmic credit-limit bias

## Template & policy
- Template: lesson.
- Source policy: min 8 sources; >=4 primary, >=1 secondary. Primary: Soares
  2022 and related MIRI/alignment write-ups; the goal-misgeneralization papers
  (Langosco et al. 2022; Shah et al. 2022) and any capability-vs-alignment
  generalization studies; skeptics' primary essays. Secondary: reporting.
- Production policy (balanced): coach low, researcher high, writer medium,
  editor high; model "capable"; none required.
- Actual harness/model: `claude-code-routine`, `claude-opus-4-8` for all roles.
  Record in nb-meta (date 2026-08-07).

## Habits not to inherit (for the writer brief)
Recent what-could-go-wrong pieces open with a headline stating a null-ish or
"never been logged" empirical finding and close on a "what no experiment has
caught yet" beat. That shape now recurs across the desk. Do not inherit the
mold. Find this argument's own frame. Check the recent library's deks and
headings first.

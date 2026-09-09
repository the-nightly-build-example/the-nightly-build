# editor brief: the-evidence/react-reasoning-and-acting (01)

Inputs (read each):
- editorial-direction.md — the concatenated governing standard.
- commission.md — assignment, teach-list, boundaries, sources plan.
- writer/01/draft-handoff.md — the writer's account of choices and open risks.
- writing-coach/01/voice-guide.md — how this piece should sound.
- researcher/01/evidence.md — the source record; every body claim must trace to
  a source here, and each cited URL must resolve.
- library/the-evidence/react-reasoning-and-acting.html — the article to edit.

Output: editorial-review.md (this directory) — what you cut/changed and your
decision (approved, or the specific change routed back to the writer).

Proof: after editing, run
  ./nb stamp .nb-work/the-evidence/react-reasoning-and-acting/library/the-evidence/react-reasoning-and-acting.html
  ./nb check .nb-work/the-evidence/react-reasoning-and-acting/library/the-evidence/react-reasoning-and-acting.html --series the-evidence
Leave it at verdict PUBLISHABLE, no BLOCK, word count 1200-2200.

Recent-pattern notes for this desk (catch a formula no single article shows):
- the-evidence over-uses the corrective-twist headline "The paper credited with X
  never did Y" (attention-is-all-you-need, foundation-models, gans,
  gpt-4-technical-report). Confirm this headline does NOT fall into that mold.
- Deks over-use the comma-tail reversal "X did A, and lost at B" (t5, alphazero).
  Check the dek.
- A final body section named "How far the X reaches" has recurred. Reject that
  shape; check headings are not all comma-and clauses.
- Press rule: the takeaway lands the judgment; the body must not close on a
  Verdict note or restate-the-finding block.

This round's focus:
- Substance first: this lesson reads a specific paper and rests on its Table 1
  numbers. The writer flagged that an automated page summarizer returned WRONG
  HotpotQA scores (78/69/39) and that the correct figures from Table 1 are
  27.4 / 29.4 / 28.7 (ReAct / CoT / Standard), with FEVER, ALFWorld (71 vs 37),
  WebShop (40 vs 30), and hallucination (0% vs 56%). Re-verify every number in
  the article against evidence.md, and if evidence.md itself is not unambiguous
  on a figure, hedge or cut rather than ship a wrong number.
- The honest angle must land: what ReAct actually measured (uneven, task-specific
  gains; below CoT on HotpotQA EM) vs the "agents started here" credit, and how
  today's function-calling loops depart from the paper. Do not let the piece
  overclaim ReAct's results.
- chain-of-thought and tool-use are existing lessons: linked in Background, not
  re-taught.
- Slop at edges; the last sentence hardest. Delete, do not repair.
Nothing else.

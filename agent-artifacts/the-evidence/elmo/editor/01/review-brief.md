# editor brief: the-evidence/elmo (editor/01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md),
writer brief (../../writer/01/brief.md) + draft-handoff.md (../../writer/01/draft-handoff.md).
Article HTML: .nb-work/the-evidence/elmo/library/the-evidence/elmo.html
Output: ./editorial-review.md
Proof:  ./nb check .nb-work/the-evidence/elmo/library/the-evidence/elmo.html --series the-evidence --repo $(pwd)

Follow the nb-editor skill. Correct, reads well, good to read.

Correctness priorities: recompute the six-task numbers (metric, prior SOTA,
ELMo, error reduction) against the ELMo paper's Table 1. Verify the idea-vs-
machinery claim is precise: the contextual-representation idea survived; the
frozen-biLSTM feature-based recipe was displaced by fine-tuning (BERT) — the
piece must not overstate into "ELMo was a dead end" (its idea is universal) or
understate the displacement. Verify BERT's feature-based/fine-tuning distinction
is represented from BERT's own words. Audit data-nb-kind (ELMo and BERT papers
primary; retrospective framing secondary). Open every href.

Recent-pattern enforcement: no "the famous X was not the real X" closing reveal;
headings distinct from each other and from recent evidence headings; dek carries
no comma-triad/"and" mold. Read the last sentence of the piece and each section
hardest. Confirm the takeaway resolves the opener, teaches nothing new, and the
body never refers to itself. Redraft only for a wrong argument; else edit
directly, re-run nb stamp + proof to BLOCK: 0, record the decision.

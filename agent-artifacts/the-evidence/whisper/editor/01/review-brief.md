# editor review-brief: the-evidence/whisper (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — the assignment, angle, boundaries, non-overlap notes
- ../../writer/01/brief.md — the exact writer brief (check for leakage against it)
- ../../writing-coach/01/voice-guide.md — the voice guide and its verified exemplar passages
- ../../researcher/01/evidence.md — the evidence record
- ../../writer/01/draft-handoff.md — the draft handoff and its original-work sentence
- The article: /home/user/the-nightly-build/.nb-work/the-evidence/whisper/library/the-evidence/whisper.html
- Template context: /home/user/the-nightly-build/.nb-work/the-evidence/whisper/.nb-context/

Output: ./editorial-review.md (beside this brief)

## Recent-pattern notes (The Evidence — compare the draft's edges, headings, dek against these)

- Recent Evidence deks lead with "The [X] paper/report [surprising verb]..."
  (batch-normalization "got its own explanation wrong", GANs "generated blurry
  thumbnails", knowledge-distillation "trained a network to recognize a digit it
  never saw", gpt-2 "never mentions danger"). If this draft's dek falls into that
  mold, it is a formula — flag it. Confirm the draft's dek and headline read in the
  subject's own nouns.
- Recent orientation openers use definitional molds: "What 'X' actually names",
  "The number on the model card". A first heading built that way is a formula.
- Watch for the house habit of author/number-count headings ("204 tasks from 450
  authors", "Four assumptions hold the proof together"). One is fine; a copy is
  formula.
- The whole paper's dek style is a single concrete finding with a number. That is
  the register, not a defect; the defect is a repeated *construction*.

## This round's focus

- Verify the piece's central synthesis (robustness and hallucination are one
  design property, seen twice) is earned from the evidence, not overreach. It is
  the article's original-work claim; push hardest on it in the first read. The
  paper proves an *average* robustness result and never makes a per-record
  guarantee — confirm the draft says exactly that and does not imply the paper was
  refuted by the hallucinations.
- Confirm no single figure is presented as *the* hallucination rate. The writer
  flagged two open items: (1) source 5 (Koenecke et al.) and source 6 (the AP
  article) were rendered descriptively because the evidence record did not carry
  exact printed titles — check the citations land on the right documents and the
  source labels are accurate; (2) the writer used the measured 1.4% (scoped to
  AphasiaBank) over the abstract's "roughly 1%" — judge whether the scope is stated
  honestly, and route to the writer only if the evidence cannot settle it.
- Check every display-text number/name against the evidence: the 680,000 /
  117,000 / 125,000 hours, the 65%-of-compute anchor, the clean-benchmark tie, the
  off-distribution figures and the 55.2% reduction, and the Nabla/AP deployment
  figures with their scopes.
- Audit data-nb-kind (5 primary, 1 secondary) and open every citation href as
  printed. Confirm the WER worked example is correct and that zero-shot is linked
  to the-evidence/gpt-2 rather than re-taught.
- The lesson template allows the two bookend cards to address the reader; judge
  them like any other prose (do they say anything particular to this lesson?).

Edit prose, structure, and documented furniture directly. Route to the writer only
what needs reporting or a redraft, and to the researcher only missing evidence.
Record every change. Decide approve or revise.

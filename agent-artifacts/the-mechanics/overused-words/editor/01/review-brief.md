# editor review-brief: the-mechanics/overused-words (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — the assignment, the causal chain, settled-vs-open, boundaries
- ../../writer/01/brief.md — the exact writer brief (check for leakage against it)
- ../../writing-coach/01/voice-guide.md — the voice guide and its verified exemplar passages
- ../../researcher/01/evidence.md — the evidence record
- ../../writer/01/draft-handoff.md — the draft handoff and its original-work sentence
- The article: /home/user/the-nightly-build/.nb-work/the-mechanics/overused-words/library/the-mechanics/overused-words.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/overused-words/.nb-context/

Output: ./editorial-review.md (beside this brief)

## Recent-pattern notes (The Mechanics — compare the draft's edges, headings, dek)

- Recent Mechanics deks pair a behavior with a mechanism, often with a number
  ("A model can't count the words it's writing", "The model sees your whole
  conversation for the first time on every turn"). That is the register; a copied
  *construction* is the formula. Judge this draft's dek in the subject's own nouns.
- Watch for a stock "What's settled / What's open" scaffold heading. The beat
  requires marking settled vs open, but the heading must be in the piece's own
  nouns, not a scaffold slot.
- Vary orientation openers away from definitional molds.

## This round's focus (specific risks in this draft)

- FURNITURE — check the "Verdict note" the writer says they added. press/editorial.md
  is explicit: "The takeaway bookend is where a lesson lands its judgment. Do not
  close the body with a Verdict note, or any block that restates the finding. Some
  older articles still carry that block from the paper's earlier template. It is a
  leftover, not a model to copy." If the note near the end restates the finding or
  functions as a body-closing verdict, remove or recast it; the takeaway bookend is
  where judgment lands. Judge it against that rule directly.
- HEADLINE — the draft headline is two sentences ("The 'delve' spike is real. The
  popular reason for it failed its one test."). Judge it against spec/headlines.md:
  does it put subject-verb-surprise up front, or is the two-beat construction a
  machine tell? Rewrite if it grades the piece rather than states the finding.
- The settled/open seam is the spine. Confirm the article presents the annotator
  ("delve") hypothesis at its real weak strength — one failed DIRECT test (Juzek &
  Ward's ICE-corpus analysis did not support it) plus one indirect test that cannot
  isolate rater dialect — and does NOT let it read as the answer. Confirm the
  SETTLED claim (post-training/RLHF narrows the output distribution) is not blurred
  into the open one.
- Numbers: confirm Kobak is cited as one version and called a moving lower bound,
  and that the abstract-only figures (Kobak per-word r-values, Sadasivan
  99.3%→9.7%, InstructGPT alignment-tax numbers) are kept qualitative. The one
  frequency table should draw from Liang's cleanly-sourced multipliers — verify the
  table's numbers against the evidence.
- The detection limit (population-level, correlational, no per-document verdict)
  must be explicit. Confirm it.
- CITATIONS/LINKS: the writer linked the-evidence/instructgpt for the RLHF recipe
  rather than adding Ouyang et al. as a numbered source (per the "link taught
  mechanics, never a numbered source" rule). Judge whether that is right or whether
  any claim actually rests on Ouyang and needs a citation. Confirm the required
  Background link to the-mechanics/formatting-defaults is present and that
  autoregressive-generation / sampling-temperature are linked, not re-taught.
- Do NOT let the piece showcase the overused words it names — check that they
  appear as data, not as performed style, especially at the edges.
- Audit data-nb-kind (6 primary, 2 secondary), open every citation href as printed,
  and do the display-text verification.

Edit prose, structure, and documented furniture directly. Route to the writer only
reporting/redraft, to the researcher only missing evidence. Record every change.
Decide approve or revise.

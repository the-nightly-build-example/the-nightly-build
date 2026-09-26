# editor review-brief: the-evidence/align-and-translate (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — the governing standard.
- commission.md (../../commission.md) — the assignment, boundaries, and the "Angle correction" the writer drafted to. Read it; a claim narrowed past the record is your business.
- writer/01/brief.md (../../writer/01/brief.md) — the exact brief the writer worked from.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — read first, before the evidence.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — open when a claim needs testing.
- writer/01/draft-handoff.md (../../writer/01/draft-handoff.md) — the writer's original-work sentence and proof result.
- The article: /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/library/the-evidence/align-and-translate.html

Output:
- /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/agent-artifacts/the-evidence/align-and-translate/editor/01/editorial-review.md

Proof (run it yourself after any edit, links included): /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-evidence/align-and-translate/library/the-evidence/align-and-translate.html --series the-evidence --repo /home/user/the-nightly-build

## What to test hardest on this piece

- The scope-not-vocabulary correction. The paper DOES name attention (Sec 3.1)
  and DOES credit Graves 2013 (Sec 6.1). Confirm the article does not claim the
  authors spoke only of alignment, and does not overclaim the paper "invented
  attention" or "started the LLM era."
- The BLEU numbers. Recompute/verify RNNsearch vs RNNencdec (Table 1) against the
  record, and confirm the Sutskever 34.8 vs 26.75 comparison is NOT presented as
  head-to-head. Check every number, title, author, affiliation, and date in the
  headline, dek, and subheads against the document that owns it.
- The captured alignment-heatmap asset: confirm what the caption claims matches
  the figure and the record, and that the cited href/locator resolves to the
  source.
- data-nb-kind on every source against the primary/secondary test.

## Recent-pattern notes (compare against these; one article cannot show formula)

- Do not accept the "You have probably ..." / "Every large language model ..."
  opener molds or the "By the end you will know A, B, and C" closer.
- ANTI-ECHO with the neighbouring published lesson the-evidence/attention-is-all-
  you-need (headline "The paper credited with starting the LLM era never trained
  a language model"; headings "Eight authors, two language pairs, one new
  architecture", "Five mentions of 'language model,' zero about this one"). This
  predecessor piece must NOT reuse a "credited with X, never did Y" headline, an
  "N authors, M language pairs" heading, or an "X mentions of Y, zero about Z"
  heading. Flag any echo.
- Recent the-evidence deks (elmo, deep-double-descent, mamba) pair a number with
  a reversal; check this dek is built on its own pattern.

## Your job

Decide whether it publishes; edit anything except the facts to get there. Cut
slop against spec/slop.md (run the placeholder test on the edges), check for
briefing leaks (read commission.md for reader-situation sentences taken whole)
and voice-guide borrowings, and check the piece repeats neither the recent record
nor its neighbour. Fix what you can from the record and this checkout, and run
the proof to BLOCK: 0 after your edits. If you make direct cuts and the proof
still passes, no writer round is owed for the proof alone. Send back for a
redraft only if it needs a different argument.

Write editorial-review.md in the shape your skill specifies (Correct / Reads well
/ The experience / Edits / Decision). Report the review path and the decision
(approve or redraft) and, if any fact needs the orchestrator, say so.

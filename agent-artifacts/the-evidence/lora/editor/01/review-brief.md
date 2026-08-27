# editor review-brief: the-evidence/lora (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, series prompt
- ../../commission.md — the assignment, its angle, boundaries, and the reader's situation
- ../../writer/01/brief.md — the exact writer brief, so a leak is visible against it
- ../../writing-coach/01/voice-guide.md — how the piece should sound, with the exemplar passages the writer read
- ../../researcher/01/evidence.md — the evidence record to test claims against
- ../../writer/01/draft-handoff.md — the writer's original-work sentence and any warnings left
- article to edit: /home/user/the-nightly-build/.nb-work/the-evidence/lora/library/the-evidence/lora.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/lora/.nb-context

Output: editorial-review.md (this directory)

Proof (after your direct edits, the orchestrator stamps; you may run this to check): ./nb check /home/user/the-nightly-build/.nb-work/the-evidence/lora/library/the-evidence/lora.html --series the-evidence --library /home/user/library-checkout

Recent-pattern notes (compare edges, headings, dek, furniture against these):
- The two-clause dek joined by "and"/"but" is the house default right now, and
  the three dek molds in `spec/headlines.md` (semicolon reversal, suspended
  question, comma triad) recur. Check this dek against them.
- "How...", "What...", "Where..." section-heading openers are overused across
  the-evidence, and the desk keeps closing on a "Where X still..." present-day
  section. Flag a stamped heading or a formulaic present-day close.
- The "Why this matters" opener habit is to end by telling the reader "Read it
  and you can see...". Check the bookends against it.

This round's focus: the load-bearing correctness check is the bounded parity
claim. Confirm the article never states "matches full fine-tuning" without its
scope, and that the Biderman 2024 code/math limitation is represented honestly
and cited by its arXiv page (not called a TMLR paper unless the venue is
confirmed). Confirm the discarded figures (97-99% GLUE, Gartner 85%) did not
slip in.

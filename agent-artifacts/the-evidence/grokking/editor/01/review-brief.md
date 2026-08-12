# editor review-brief: the-evidence/grokking (01)

Inputs (read in the order your skill names):
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/writing-coach/01/voice-guide.md — read first.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/commission.md — the assignment, its boundaries, the reader's situation.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/writer/01/brief.md — the exact writer brief (to catch leakage and habits).
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/researcher/01/evidence.md — open when the first read calls for it.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/writer/01/draft-handoff.md — original-work sentence, open only on the third read.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/library/the-evidence/grokking.html — the article to edit in place.
- template context under /home/user/the-nightly-build/.nb-work/the-evidence/grokking/.nb-context/.

Output: /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/editor/01/editorial-review.md

After any direct edits you make, the orchestrator runs `nb stamp` and `nb check`
before the PR; you do not run the proof. Route to the writer only what needs new
reporting or a redraft.

## Recent-pattern notes (catch formula against these; one article cannot show it)

Cross-desk house formulas this run is deliberately breaking — flag any that survived:
1. "Why this matters" opening on a nostalgic or second-person recall ("If you have
   heard one thing about...", "You may remember when...") or pivoting on "This
   lesson reads/shows/takes apart...".
2. The opener closing on a "set the measured result and the famous story side by
   side" line.
3. "The takeaway" landing on a "So when someone tells you X..." portable rebuttal.
4. "this desk" or any body self-reference; the body narrates no one.

the-evidence-specific molds: the recent dek mold is the concessive reversal
"[names] reported X in [year], and later analyses found Y" (a second clause that
reverses the first); recent headings lean on "The X that Y" relative-noun-phrases
and the "noun, the appositive" comma mold. A dek or heading built like those is a
formula even if sharp.

## Round focus

Verify the piece holds a real, small result apart from the large claim it is cited
for, and that these evidence-record boundaries survived:
- The author line is Power, Burda, Edwards, Babuschkin, Misra (it is Burda, not
  "Burns"). Check the names in display text and body against the evidence record.
- "Sudden" is a property of the watched test-accuracy curve; the generalizing
  circuit forms gradually beneath it on the progress measures. The draft must not
  claim generalization is literally instantaneous.
- Weight decay: the original paper says "most effective," Nanda et al. say
  "necessary." Whichever wording the draft uses must match the source it cites; the
  two must not be merged into a stronger claim.
- The 2025 7B mixture-of-experts result must be weighed honestly: it widens
  grokking's reach beyond toy scale but reframes it as local, asynchronous,
  per-domain delayed generalization and cuts against the "sudden unlock" shorthand.
  The draft must not use it to claim big models simply "grok."
Audit every data-nb-kind (each paper's authors are primary for their own result; a
later restatement is secondary). Confirm the three ordered reads, edit directly
what is yours, route only what needs reporting, and record every change.

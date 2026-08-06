# editor review-brief: the-instruments/glue (editor/01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../writer/01/brief.md — the exact writer brief (check for instruction leakage)
- ../../writing-coach/01/voice-guide.md — the craft standard for this article
- ../../researcher/01/evidence.md — the evidence record (open as an opponent)
- ../../writer/01/draft-handoff.md — original-work sentence + proof notes
- ../../library/the-instruments/glue.html — the article to review
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Proof (writer owns proof; you run nb stamp after direct cuts): 
./nb check .nb-work/the-instruments/glue/library/the-instruments/glue.html --series the-instruments --library /home/user/library-checkout

This round's focus:
- Load-bearing framing check: verify the "misled" is located in RECEPTION/
  shorthand, NOT attributed to the benchmark authors (they built SuperGLUE
  because they treated saturation as a reason to raise the bar; the DeBERTa team
  disclaimed human-level). If the draft pins "solved understanding" on the
  authors, that is a required revision.
- Reception is sourced on a single secondary (Gilbane Advisor) plus the primaries
  (Bender & Koller for saturation≠comprehension; the authors' own actions). Judge
  whether the reception claim is carried or overreaches its single secondary; if
  it overreaches, cut it back to what the primaries support rather than requesting
  more evidence.
- Numbers/labels: check every figure and date against the evidence — the human
  baselines (GLUE 87.1 Nangia & Bowman; SuperGLUE 89.8), surpass dates (6 Jun 2019
  MT-DNN 87.6; 6 Jan 2021 DeBERTa 89.9/90.3), and the artifact figures
  (hypothesis-only ~67%/~53% vs ~33%; COPA cues-only 59.6% vs 50%). Confirm
  artifact reliance is stated as model-specific ("consistent with," not "every
  high scorer exploits shortcuts").
- Recent-pattern notes to enforce: no "two true numbers / both are true" headline
  mold; no semicolon-reversal / suspended-question / comma-triad dek; vary section
  headings away from comma-and pairs. Confirm the mmlu Background link is a link,
  not re-teaching.

Decision: approve only when no publication-blocking issue remains. Record the
review at ../../editor/01/editorial-review.md.

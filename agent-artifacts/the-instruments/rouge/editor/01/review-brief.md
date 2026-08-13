# editor review-brief: the-instruments/rouge (01)

Inputs (all under this article's artifact root unless absolute):

- `editorial-direction.md` — house standard, slop, headline standard, press voice,
  lesson identity, series prompt.
- `commission.md` — the assignment; note its "misled" framing was corrected by the
  evidence, so judge the article against the evidence, not the commission's
  cleaner version.
- `writer/01/brief.md` — the exact writer brief (check for leakage against it).
- `writing-coach/01/voice-guide.md` — register and quoted exemplars.
- `researcher/03/evidence.md` — THE evidence record (carries rounds 01 and 02
  forward and adds the secondary). Use this one, not the earlier numbered records.
- `writer/01/draft-handoff.md` — the original-work sentence (third read only).
- Article: `/home/user/the-nightly-build/.nb-work/the-instruments/rouge/library/the-instruments/rouge.html`
- Template context: `/home/user/the-nightly-build/.nb-work/the-instruments/rouge/.nb-context/`

My recent-pattern notes (compare edges, deks, headings; a match is a formula to
break):

- Paper-wide opener tic: "By the end you will know X. You will also see Y."
- The Instruments opener tic: "every flagship ships an X score" / "two labs report
  the same number and mean different things."
- Takeaway on negative parallelism ("a high X score is worth what it measures ...
  It is not a reading of ..."). Deks: banned molds; headings: comma-and triad.

This round's focus — the accuracy of the reframe is the main risk:

- The article must NOT claim ROUGE "correlates weakly with human judgment" in
  general. Verify the dimension picture is kept distinct (strong-but-confounded on
  consistency; weak on coherence/relevance; ROUGE-L weak throughout).
- Faithfulness must be stated as "ROUGE does not track faithfulness," not "rewards
  the unfaithful" (Maynez's best-ROUGE model is also most faithful — the BERTS2S
  guard must survive). Check the Maynez figures against the record.
- Confirm Bhandari is not miscited (the writer says it is not cited at all — fine),
  and Graham is cited only for variant fragility, not "weak correlation."
- Recompute the hand-worked ROUGE example; a wrong count there discredits the
  lesson. Check Lin's reversed-sentence example (ROUGE-2 = 1/3 for both) is stated
  correctly.
- Sai 2022 is the secondary, used as outside characterization, not a standalone
  correlation number.

The orchestrator stamps after your direct edits and proves before the PR; return
to the writer only if the proof would demand new prose.

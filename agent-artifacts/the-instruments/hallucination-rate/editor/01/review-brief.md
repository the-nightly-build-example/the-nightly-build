# editor review-brief: the-instruments/hallucination-rate (01)

Inputs:
- editorial-direction.md — house standard, headline standard, press voice, lesson identity, series prompt
- writer/01/brief.md — the exact writer brief (read to catch instruction leakage)
- writing-coach/01/voice-guide.md — the craft standard and licenses to enforce
- researcher/01/evidence.md — the claim set to test display text and citations against
- writer/01/draft-handoff.md — the writer's original-work sentence and warnings left
- library/the-instruments/hallucination-rate.html — the article to review
- .nb-context/ — the effective template contract and furniture catalogs

Proof (writer owns re-proof; you run `nb stamp` after direct cuts):
  ./nb check .nb-work/the-instruments/hallucination-rate/library/the-instruments/hallucination-rate.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout

Recent-pattern notes (check the draft's dek, headline, openers, closers, and
section headings against these and against the recent published library):
- the-instruments headlines recur as two conflicting numbers side by side; deks/headings lean on a stacked-choices table. Flag if inherited.

Round focus:
- The 'misled' case must be framed as press/procurement generalization + the task-vs-open-use gap (33-48% PersonQA fabrication vs low summarization scores), with NO invented dollar cost. Verify no hard cost figure was fabricated.
- Push hardest on the core claim that a hallucination rate measures summary faithfulness, not general truthfulness, and that the three benchmarks define hallucination incompatibly (rates not stackable). Check the HHEM classifier weakness numbers against the record; check that llm-as-a-judge and the-mechanics/hallucination are linked, not re-derived. Watch date currency (source snapshot 'May 11 2026').

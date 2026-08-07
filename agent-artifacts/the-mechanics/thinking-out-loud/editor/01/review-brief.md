# editor review-brief: the-mechanics/thinking-out-loud (01)

Inputs:
- editorial-direction.md — house standard, headline standard, press voice, lesson identity, series prompt
- writer/01/brief.md — the exact writer brief (read to catch instruction leakage)
- writing-coach/01/voice-guide.md — the craft standard and licenses to enforce
- researcher/01/evidence.md — the claim set to test display text and citations against
- writer/01/draft-handoff.md — the writer's original-work sentence and warnings left
- library/the-mechanics/thinking-out-loud.html — the article to review
- .nb-context/ — the effective template contract and furniture catalogs

Proof (writer owns re-proof; you run `nb stamp` after direct cuts):
  ./nb check .nb-work/the-mechanics/thinking-out-loud/library/the-mechanics/thinking-out-loud.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout

Recent-pattern notes (check the draft's dek, headline, openers, closers, and
section headings against these and against the recent published library):
- the-mechanics deks recur as a one-sentence 'a chatbot does X surprising thing'; bodies recur at five beats. Flag if inherited.

Round focus:
- Two precision checks: (a) the 'extra tokens = compute regardless of content' claim must be attributed to theory / toy models (Pfau), NOT deployed models — Lanham found filler tokens gave no gain; flag any sentence implying real models compute from arbitrary filler. (b) the faithfulness open question must be marked open and noted as measured on older/smaller models, not the frontier reasoning traces the piece opens with.
- Push hardest on the settled-vs-open seam being audible. Verify Wei/DeepSeek-R1/Dziri numbers against the record. Confirm neighbors (autoregressive-generation, prefill-and-decode, chain-of-thought doc) are linked, not re-taught.

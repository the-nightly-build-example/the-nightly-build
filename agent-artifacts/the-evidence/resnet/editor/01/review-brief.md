# editor review-brief: the-evidence/resnet (01)

Inputs:
- editorial-direction.md — house standard, headline standard, press voice, lesson identity, series prompt
- writer/01/brief.md — the exact writer brief (read to catch instruction leakage)
- writing-coach/01/voice-guide.md — the craft standard and licenses to enforce
- researcher/01/evidence.md — the claim set to test display text and citations against
- writer/01/draft-handoff.md — the writer's original-work sentence and warnings left
- library/the-evidence/resnet.html — the article to review
- .nb-context/ — the effective template contract and furniture catalogs

Proof (writer owns re-proof; you run `nb stamp` after direct cuts):
  ./nb check .nb-work/the-evidence/resnet/library/the-evidence/resnet.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout

Recent-pattern notes (check the draft's dek, headline, openers, closers, and
section headings against these and against the recent published library):
- the-evidence deks recur as a plain declarative + 'and' clause; headlines recur as 'credited-with X / never did Y'. Flag if this piece inherits either.

Round focus:
- Verify the two evidence corrections were honored: (a) the paper DID forecast generality (a forecast, not a demonstration, naming no architecture) — the draft must not claim it made no generalization claim; (b) the paper explicitly says the degradation is NOT vanishing gradients — the draft must not repeat that gloss.
- Push hardest on the degradation-vs-overfitting distinction (higher TRAINING error, Fig 1) and the 1202-layer-did-worse fact. Confirm the transformer 'Add & Norm' residual link is sourced and that attention/architecture are linked, not re-taught.

# draft-handoff: when-ai-breaks/apple-card (writer 01)

## Original work
The article turns the DFS report's own buried caveat into a concrete
impossibility proof: it names the three specific artifacts that would settle
the bias question (the model's feature list, the regression specification, and
a mediation analysis of those features against applicants' real gender) and
shows that the one person with legal standing to complain is structurally
barred from every one of them.

## Proof result
`./nb check ... --check-links` → BLOCK: 0, WARN: 2, verdict PUBLISHABLE.

Both warnings are W-SENTENCE-DENSITY (40 words, 2 clause joins), left
intentionally:
- The "three things: a, b, and c" sentence in "The proof an applicant can
  never reach" is a single introduced list; splitting it would break the
  enumeration.
- The takeaway's "the reason the story does not end there is the proxy..."
  sentence pairs the proxy definition with its immediate consequence; splitting
  severs the claim from the point it exists to make.
Both are controlled single-idea sentences the house standard permits.

## Notes for the editor
- The original viral posts (Hansson, Wozniak) are gated on X (HTTP 451) and were
  not opened on-source, so neither is cited as a read primary. Hansson's 20x and
  the Nov 7 2019 date are attributed to the DFS report, which confirms both
  firsthand (s1). Wozniak's 10x is carried as his own claim via Futurism (s3),
  never as a DFS finding. Goldman's denial is via AppleInsider reproduction (s4).
- The unreconciled-pair, understatement, and diagnostic-question licenses are each
  used once: the pair in "Cleared on bias, faulted on secrecy," the diagnostic
  question in "The proof an applicant can never reach."
- Fig. 1 (asset-1.png) is the Apple Card site panel reproduced in the DFS report
  p.9 (PDF page 10), captured with `nb asset pdf`; caption flags it as a snapshot
  of the site, not the model.
- 8 sources: 5 primary (DFS report, Jamie Hansson's account, DFS press release,
  ECOA, CFPB circular), 3 secondary (Futurism, AppleInsider, TechCrunch/
  O'Sullivan). Meets the >=8 / >=4 primary / >=1 secondary policy.

## Open questions
None blocking. One residual: the piece leans on the DFS report and the single
O'Sullivan/Hall critique for the proxy argument because the report itself
publishes no proxy analysis to weigh against; if the editor wants a second
independent expert voice on the proxy point, that requires a new researcher
artifact (the writer does not expand the claim set).

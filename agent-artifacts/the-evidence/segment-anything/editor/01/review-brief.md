# editor review-brief: the-evidence/segment-anything (01)

Inputs:
- ../../editorial-direction.md — the standards to apply
- ../../commission.md — the assignment, boundary, and reader
- ../../writer/01/brief.md — the exact writer brief this draft answered
- ../../writing-coach/01/voice-guide.md — how the piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the evidence record to test claims against
- ../../writer/01/draft-handoff.md — the writer's original-work sentence and proof note
- ../../../../library/the-evidence/segment-anything.html — the drafted article to edit in place
- ../../../../.nb-context/ — effective template contract and furniture catalogs

Output: ./editorial-review.md

Recent-pattern notes (compare edges, deks, headings against these as formula):
- Deks in this series state a finding with one number; watch the comma-triad,
  semicolon-reversal, and suspended-question molds.
- Recent openers begin "what X is counting" or "the paper that..."; recent
  closers are bare assessment headings. Flag either if inherited.
- Headings should be concrete in the piece's own nouns; flag a comma-and join.

This round's focus: test the load-bearing synthesis — that SAM's masks are
class-agnostic (99.1% model-drawn, audited only on 500 of 11M images) and that
zero-shot SAM loses to the detector whose boxes it is handed — against the
evidence and its owning primaries, including the two tables' figures. Confirm the
masks-not-labels boundary stays sharp and that clip and vision-transformer are
linked as Background rather than re-taught.

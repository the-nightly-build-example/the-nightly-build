# editor review-brief: the-evidence/clip (editor/01)

Inputs (all at the artifact root unless noted):
- editorial-direction.md
- commission.md
- writer/01/brief.md
- writing-coach/01/voice-guide.md
- researcher/01/evidence.md
- writer/01/draft-handoff.md (open the original-work sentence only on the
  third read)
- The article: .nb-work/the-evidence/clip/library/the-evidence/clip.html
- Template context under .nb-work/the-evidence/clip/.nb-context/

Output: agent-artifacts/the-evidence/clip/editor/01/editorial-review.md

## My recent-pattern notes (catch formula/catchphrase no single article shows)
Verified against the recent published the-evidence library:
- Heading mold "What <authors> actually built / did / proved" recurs; flag it
  if this piece uses it.
- Structural mold recurring in the-evidence: [the shorthand vs the reality] ->
  [what X actually built] -> [a numbers table] -> [what inherited the name /
  what changed]. If the draft marches through this by default, that is a
  formula finding.
- Takeaway closer mold across the paper: a directive handing the reader a
  question ("when a claim about X reaches for Y, ask which..."). Cut if present.
- Negative parallelism in the takeaway ("X was not Y, it was Z"); check the
  last card hardest against spec/slop.md.
- Deks: reject comma-triad, semicolon-reversal, suspended-question molds; check
  against recent the-evidence deks.

## This round's focus
- Confirm the piece credits the two genuine strengths the evidence records, so
  it does not read as a pure debunk: CLIP's real robustness to natural
  distribution shift, and the paper's own train/test contamination audit
  showing a near-null effect.
- The writer deliberately omitted ResNet-50's own ~76.1% figure (evidence
  marks it context-only) and the 85.4% linear-probe number (flagged
  verify-before-print). Leave them omitted unless you verify the exact figure
  against the paper's table; do not add an unverified number.
- A source asset (CLIP Fig. 5) is optional; request it only if an exact visual
  would let the reader test a central claim better than the prose table does.
- Audit data-nb-kind labels: 5 primary, 1 secondary per the evidence record.

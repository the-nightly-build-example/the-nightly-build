# writer brief: the-instruments/inception-score (01)

Inputs:
- editorial-direction.md (house standard, slop/headline rules, press voice, lesson identity, The Instruments prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; read before drafting)
- researcher/01/evidence.md (the complete claim set; use its Numbers section exactly; address its Contradictions)
- commission.md (assignment, boundaries, original-contribution target)
- the initialized article at library/the-instruments/inception-score.html (edit in place; keep chrome exact)
- effective template contract and furniture catalogs under .nb-context/

Output: writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build):
  ./nb stamp .nb-work/the-instruments/inception-score/library/the-instruments/inception-score.html
  ./nb check --series the-instruments --library /home/user/library-checkout .nb-work/the-instruments/inception-score/library/the-instruments/inception-score.html
(iterate with --no-check-links; final proof with links, to BLOCK: 0)

This round's focus (from the researcher's report; detail and Contradictions in the evidence file):
- Make the WGAN-initialized attack the load-bearing "it misled" case: Barratt & Sharma got
  IS ~900 (against a hard max near 1000) from images that look realistic, which is the result
  a defender cannot wave off. Acknowledge honestly the companion caveat: optimizing IS from
  pure noise (IS 986.10) reproduces a failure Salimans et al. themselves warned about, so a
  defender could call the noise case contrived. Present both; lean on the WGAN one.
- "Blindness to intra-class diversity" is NOT a named primary finding. Present it as a
  consequence of the construction (the one-image-per-class attack shows it implicitly); do not
  attribute it as a direct claim any paper headlines.
- Do not overclaim "how widely it was used." The evidence has the authors' own "most widely
  used" claims and one concrete headline figure (BigGAN IS 166.5), not a systematic count.
  Scope the "what it cost" section to what the record supports.
- Watch the scope caution: comparing BigGAN's IS to a real-data IS is not apples-to-apples
  (IS never looks at real images); and note the internal 900.10-vs-900.15 discrepancy in the
  Barratt paper as the record gives it.
- Record formulas in the papers' own terms (the record has them). The reader holds
  probability; define only the one idea the metric needs (the gap between a single image's
  label distribution and the average over all images).
- Link, do not re-teach: the-instruments/fid is the successor and the natural Background link
  and contrast; do not retell FID. This lesson owns the Inception Score itself.

Recent library shapes to break (keep required content):
- Dek: avoid the two-clause "claim, and/so the twist" mold, the comma-triad, and the
  "The [number] that..." opener.
- The Instruments desk keeps closing on a verdict-of-limits heading ("A high GAIA score
  licenses less than the headline says," "What a utilization number cannot see," "Where the
  number keeps its word"). Keep the "what it cannot support" content; do NOT build the closing
  heading to that stamp.
- Orientation heading is its own concrete step, not a paraphrase of the headline.
- Furniture: the metric's definition may genuinely want an nb-math block; a before/after or
  attack table may be genuine; nb-note and nb-stat-strip recur by reflex. Earn each.

nb-meta: harness "claude-code"; model = the model you are actually running as (report it).
No charts or source assets unless the evidence record names an exact visual the argument spends.

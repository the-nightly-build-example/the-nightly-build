# editor review brief: the-mechanics/random-numbers (editor/01)

Inputs (all under the artifact root, plus the article and template context):
- editorial-direction.md (house/slop/headline standards, the paper's voice, The
  Mechanics prompt)
- commission.md (assignment, boundaries, the reader's situation)
- writer/01/brief.md (check the draft against it for leaks)
- writing-coach/01/voice-guide.md (read first; register and exemplar passages)
- researcher/01/evidence.md (the claim set; test claims and open every href)
- writer/01/draft-handoff.md (original-work sentence: open on the third read)
- library/the-mechanics/random-numbers.html (the article to edit)
- .nb-context/ (effective template contract and furniture)

## This round's focus
- The article must hold the line the commission names: this is about the SHAPE of
  the distribution over which number gets chosen (why it is biased/lumpy), not
  run-to-run variation (nondeterminism) and not what the temperature knob does
  (sampling-temperature). Both are linked, not re-taught. Confirm the draft never
  slides into re-explaining those, and that "why 7" is answered by distribution
  shape, not by randomness of draw.
- Confirm the bias is scoped to chat / instruction-tuned models (base models are
  closer to uniform; alignment sharpens the preference). A claim that this is
  architecture-level would be a sourcing error — check it against West & Potts.
- The two human sources must be distinct and cited to their owners: peer-reviewed
  Kubovy & Psotka 1976 (carries the load) vs the Veritasium crowdsourced survey
  (flagged in prose as a rough survey, video not opened by the researcher). Judge
  whether the Veritasium datapoint earns its place as flagged corroboration or
  should be dropped; the writer notes it lifts out cleanly if you prefer.
- The chart is evidence: inspect its committed provenance and read the image
  (labels, the fair-rate reference line, the visible 69 dip, no round numbers)
  for honesty, and confirm it is built only from the verified 1-100 series. No
  browser is available here, so inspect the chart PNG file directly.
- Do not print a precision the record does not support (large-study per-cell
  percentages read from HTML are approximate; headline figures are solid).

## Recent-pattern notes (compare edges, dek, headings against these)
House-wide (recurring across recent 2026-08-29 pieces):
- "By the end you will know / be able to …" syllabus-closer in the opener; recast
  if present (the writer reports it was avoided — verify).
- Generic second-person everyday-scene openers used reflexively.
- Deks as a two-clause "and" contrast or comma-triad; check dek against
  spec/headlines.md's banned molds.
- Same-built declarative headings, some joined by comma+"and".
Series-specific: avoid a quoted-failing-prompt headline that echoes the recent
the-mechanics piece (negation: "'No onions' gets onions"), and the recent heading
rhythm ("Two systems drop the same word" / "A language model bets on the words it
has seen most"). Headings in this piece's own nouns; a reader skimming only the
headings should reconstruct THIS argument.

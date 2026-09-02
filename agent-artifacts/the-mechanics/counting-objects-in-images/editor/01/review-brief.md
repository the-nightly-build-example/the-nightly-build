# editor review-brief: the-mechanics/counting-objects-in-images (01)

Inputs (read in the order your skill names):
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md)
- the writer brief (../../writer/01/brief.md)
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- evidence.md (../../researcher/01/evidence.md)
- draft-handoff.md (../../writer/01/draft-handoff.md)
- the article: ../../../../library/the-mechanics/counting-objects-in-images.html
- the chart provenance: ../../../../library/the-mechanics/counting-objects-in-images/chart-1.py
  and its rendered chart-1.png
- template context under ../../../../.nb-context/

Output: editorial-review.md (this directory)

Proof after your edits is the orchestrator's to run; route new prose/reporting,
source assets, or chart provenance to the writer.

## Recent-pattern notes (compare the article's edges, dek, headings, furniture)

- Deks recur as a two-clause ", and"-twist (quantization, hands, toxicity-score,
  gradient-hacking) or a comma triad (adversarial-examples, banned by
  spec/headlines.md). Flag either mold here.
- Headlines default to a negative-fact reveal. The closest neighbor is
  hands-in-generated-images — same desk, same image-generation failure family —
  headlined "An image generator never counts the fingers it draws," dek "Hands are
  the worst case..., and better data is slowly closing the gap," closing heading
  "The gap keeps closing." This piece must not echo that headline, that ", and"
  dek, or that closing-heading shape, and must not restage the fingers argument
  (its cause is the quantity-weak encoder + no counting step, not anatomy).
- The present-day closing keeps getting a "Where/The gap still Y" heading; check
  this one is built differently.

## This round's focus

- Numbers need the hardest check. The writer flagged (and self-corrected once) that
  exact before/after percentages carry transcription risk: CLIP counting accuracy
  (~32% → ~76% after fine-tuning; that is ~2.4x, not 3x) and the Make It Count
  benchmark deltas. Recompute every ratio and compare each figure against the
  evidence record's owning primary; where the evidence itself gives a figure two
  ways (the researcher noted one value came back as both ~59% and ~63%), require a
  sourced range or the value the evidence states with confidence, not false
  precision. No DALL-E 3 caption-quality claim should appear (unsourced — confirm
  it does not).
- Confirm the two complementary causes are both held (quantity-weak encoder AND no
  per-object counting step), not collapsed onto the encoder, and that the calibration
  is honest (reliable ~≤5 objects, degrading beyond, improving but unsolved).
- Inspect the chart: provenance numbers must match the evidence and cited primary;
  axes, scale, and legend honest.
- Everything else per your three reads and spec/slop.md.

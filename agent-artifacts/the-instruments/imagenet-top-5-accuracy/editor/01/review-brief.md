# editor review-brief: the-instruments/imagenet-top-5-accuracy (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — the assignment, the two cracks, the misled case, boundaries
- ../../writer/01/brief.md — the exact writer brief (check for leakage against it)
- ../../writing-coach/01/voice-guide.md — the voice guide and its verified exemplar passages
- ../../researcher/01/evidence.md — the evidence record
- ../../writer/01/draft-handoff.md — the draft handoff and its original-work sentence
- The article: /home/user/the-nightly-build/.nb-work/the-instruments/imagenet-top-5-accuracy/library/the-instruments/imagenet-top-5-accuracy.html
  (the committed chart-N.py and its PNG sit in the same library/the-instruments/ dir)
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/imagenet-top-5-accuracy/.nb-context/

Output: ./editorial-review.md (beside this brief)

## Recent-pattern notes (The Instruments — compare the draft's edges, headings, dek)

- Recent Instruments deks use "A [perfect/faithful] X score means Y" and "An X
  rate/win rate is Z" molds (needle-in-a-haystack, hallucination-rate, alpacaeval,
  rouge). A dek in that construction is a formula — confirm this one leads with the
  concrete finding in ImageNet's own nouns.
- Recent orientation openers: "The number on the model card", "What X actually
  names". A first heading in that mold is a formula.

## This round's focus (specific risks in this draft)

- CHART — inspect it as the skill's "Inspect visual evidence" section requires.
  Open the committed chart-N.py and the rendered PNG. Compare every plotted number
  with the evidence record and the owning primary. The chart plots year-by-year
  winning top-5 error against the 5.1% human line and the ~6% label-error band. The
  writer EXCLUDED the unverified 2016-2017 figures (~2.99%, ~2.25%) from prose — the
  chart must not sneak them back in; every plotted point must trace to a verified
  source. Read the image as a reader: axis labels, scale, legend, and the visual
  implication must be honest (a non-linear axis noted, the human line and label band
  clearly labeled). Route any chart correction to the writer, who holds the tooling.
- Confirm the three error measurements (Russakovsky ~0.3%, Northcutt ~6%, Beyer
  ~29%) are held apart and never merged, and that Northcutt's ranking point is exact
  (overall rankings unaffected; instability near-top only; ResNet-18 over ResNet-50
  only at raised mislabeled share). A claim that corrected labels reorder the whole
  leaderboard is an error to fix.
- Confirm the misled case leads with the LABELS and the human-baseline crack is
  secondary, told in ImageNet's own annotation record (one trained annotator, not a
  crowd), staying off the GLUE lesson's ground. The required Background link to the
  GLUE lesson must be present.
- DEK judgment: the dek quotes "superhuman" as the framing the piece dismantles.
  Judge whether it reads as quotation (fine) or endorsement (recast). Verify the
  dek in nb-meta matches the rendered dekline verbatim.
- Confirm this lesson defines top-1 and top-5 itself and links, rather than
  re-teaches, the ImageNet ground other lessons already cover.
- FURNITURE: if any body-closing "Verdict note" or block restates the finding,
  press/editorial.md forbids it (the takeaway bookend is where judgment lands) —
  remove or recast. Judge every component on whether it changes understanding.
- Audit data-nb-kind (7 primary, 2 secondary), open every citation href as printed,
  and do the display-text verification (all years, error figures, class/image
  counts).

Edit prose, structure, and documented furniture directly. Route chart provenance,
source assets, and any reporting/redraft to the writer; missing evidence to the
researcher. Record every change. Decide approve or revise.

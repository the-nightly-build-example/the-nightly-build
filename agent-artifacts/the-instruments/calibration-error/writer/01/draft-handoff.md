# Draft handoff: the-instruments/calibration-error (01)

## Original-work sentence

The article turns the evidence's scattered pieces — Guo's estimator, Kumar's and
Nixon's binning proofs, Brier's constant-forecast baseline, and OpenAI's GPT-4
figures — into one reader-followable argument that a low ECE certifies only that
binned confidence matched accuracy on a test set, and it deliberately holds apart
the two failure modes the sources report in isolation: the metric a coarse
binning can flatter (Kumar/Nixon) and the substantive RLHF degradation OpenAI
reported honestly with its own binning.

## Proof result

`nb stamp` then `nb check ... --series the-instruments --library
/home/user/library-checkout` (final run with link checking):

- BLOCK: 0, WARN: 0, verdict: PUBLISHABLE
- words 2199, reading 10 min, sources 8 (7 primary, 1 secondary)

Getting there cleared three warnings honestly rather than by suppression: the
length was trimmed from 2365 to 2199 words (under the 2200 band), one 41-word
Brier sentence was split, and the Brier/survey citations were reordered so
sources number in first-citation order (s5 before s6).

## Furniture and the chart

One annotated equation (Guo Eq. 3), one worked table, and one reliability-diagram
chart. The chart, the table, and the equation caption all use the same
constructed 100-prediction classifier; per the brief the chart was built with
`nb chart` from that illustrative series and is cited as illustrative (a
`data-nb-note` on the figure and table captions states the figures are
constructed by the author, not measured from Guo). No source asset was captured.

## Accuracy cautions (all applied)

- Worked examples A/B/C are presented as illustrative constructions with the
  arithmetic shown; captions carry the "not data measured from this source" note.
- One ECE definition throughout (Guo's acc/conf top-label form, M equal-width
  bins), origin attributed to Naeini et al. 2015.
- Brier stated in the modern binary convention (0–1, the do-nothing model scores
  0.21); the piece states that Brier's original 1950 score runs to 2 and doubles
  every figure.
- GPT-4: 0.007 → 0.074 reported as an honest self-report of degradation, its
  "confidence" defined as the model's probability across A/B/C/D (not typed
  confidence), and the missing bin count flagged as carrying the same
  bin-dependence caveat. Kept explicitly distinct from the "binning flatters ECE"
  metric flaw.
- the-mechanics/false-confidence is linked in prose (mechanism), not re-taught.

## Open questions

None blocking. Note carried from the evidence record: DeGroot & Fienberg 1983
(origin of the reliability diagram and calibration-vs-refinement) is gated and
was not read firsthand, so the reliability diagram is grounded through Guo and the
accuracy-blind point through Guo's definition plus Brier's constant-forecast
baseline. No researcher request is needed for this round.

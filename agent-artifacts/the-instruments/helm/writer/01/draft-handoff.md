# draft-handoff: the-instruments/helm (01)

## What this article does to the evidence that the evidence does not do itself
It reads HELM's three separate method changes (Lite dropping the correlated
axes, the seed cut, Capabilities replacing mean win rate) as one continuous
retreat from a single choice-dependent number, and uses the paper's own Figure
26 to let the reader watch the same 30 models reorder across axes, so a scattered
set of admissions becomes one demonstration that a HELM rank compares choices as
much as it compares models.

## Proof result
`nb check ... --series the-instruments --repo /home/user/the-nightly-build`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** Also clean with
`--no-check-links`. Stamped words=1943, reading_minutes=8, sources=8. No warning
left on purpose.

## Furniture and asset
- Used Figure 26 as a source asset (the brief's preferred option), captured with
  `nb asset pdf` from the HELM paper PDF (arxiv 2211.09110), page 51, cropped to
  the six per-metric panels only (printed caption and page number cropped out).
  Verified the render by eye: 962x780px, within limits. It carries the whole
  argument at once (accuracy/robustness/fairness agree; calibration/bias/toxicity
  disagree), and the T0pp/davinci toxicity-vs-bias swap the prose names is
  readable in it. No table needed.
- Two `nb-note` components: the verbatim mean-win-rate definition (s3) and the
  verbatim two-reason quote from HELM Capabilities (s8).

## Reorder case
Built on the axes the researcher verified move the order (toxicity, bias,
calibration) plus model-set selection, the tie-handling fix, sampling size, and
HELM's own two changes of aggregation method. The correction is stated in-body:
accuracy, robustness and fairness are "extremely strongly correlated," so
dropping robustness/fairness does not reorder, and that is given as CRFM's own
reason for dropping them in Lite. Did not use "a model judge prefers longer
answers." Kept clear of the answer-length-bias neighbour.

## Open question for the orchestrator
Per the evidence Limits note, the exact metric set feeding the HELM Classic
headline mean win rate column could not be read off the JavaScript-rendered
board. I treated "the leaderboard's mean win rate" as CRFM's across-scenarios
definition (from the Lite announcement) and did not assert which metrics enter
the Classic headline column. If a later capture pins that column's definition,
one sentence in "What a HELM rank sits on top of" could be sharpened; nothing in
the argument depends on it.

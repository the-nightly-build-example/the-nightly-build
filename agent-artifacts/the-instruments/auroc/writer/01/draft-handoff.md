# Draft handoff: the-instruments/auroc (01)

## Original work

The article turns AUROC's ranking-only definition (Hanley & McNeil) into a
three-part test — the number is silent on calibration, silent on the one
threshold a deployment runs at, and silent on prevalence — and then reads Epic's
two AUROC figures and its field numbers (Wong) as the predictable payoff of that
definition rather than as a scattered set of results, making the
ranking-versus-threshold gap visible by plotting the single deployed operating
point (FPR 0.17, TPR 0.33) against the chance diagonal.

## Proof result

`./nb check … --series the-instruments --library <checkout>` (links included):
**BLOCK: 0, WARN: 0 — PUBLISHABLE.** Stamped words=2109 (band 1200-2200),
reading 9 min, sources=8 (6 primary, 2 secondary; floor is 8 / ≥4 primary / ≥1
secondary). All eight source URLs and both Background library links resolve.

No warnings intentionally left standing — all cleared (citation order, three
sentence-density flags split, self-count stamped).

## Chart honesty

Used one chart: the Epic model's single deployed operating point on the ROC
square with the chance diagonal, built with `nb chart` from the only ROC
coordinate the evidence verifies (sensitivity 33% → TPR 0.33; specificity 83% →
FPR 0.17, both Wong). No ROC curve is drawn; the caption states Wong does not
publish the curve's coordinates. `chart-1.py` carries the provenance and the
recomputation. I did **not** render the Saito & Rehmsmeier imbalance worked
example as a chart or table: the evidence supplies only the two precision figures
(0.60 → 0.33) and "AUROC unchanged," not the confusion-matrix counts, so a figure
of it would have been thin or required invented cells. That point is taught in
prose from the two verified precision values instead.

## Open evidence / voice questions

- Epic's on-record rebuttal and any later model revision are not pinned to a
  primary in the evidence (STAT is partly paywalled; no Epic primary was
  reachable). Per the brief I attribute no rebuttal I cannot cite and left the
  "what Epic did next" thread out entirely rather than assert it. If a future
  round wants that thread, it needs a new researcher artifact.
- The imbalance point is framed as the uncontested fact (AUROC ignores
  prevalence; precision/PPV does not), with McDermott 2024 cited to reject the
  blanket "always prefer AUPRC" prescription. No metric horse-race asserted.

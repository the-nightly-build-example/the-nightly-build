# draft-handoff: the-instruments/calibration-error (writer/02)

## Original-work sentence

The article holds the metric flaw (opposite-error cancellation under coarse bins,
plus accuracy-blindness) apart from the substantive RLHF degradation of GPT-4's
calibration — a synthesis stated in no single source, spanning Kumar/Nixon and
the GPT-4 report. (Unchanged this round; confirmed still holding.)

## Editorial request resolved

- Reliability-diagram alt text corrected. It read "five accuracy bars rising from
  left to right," but only four bars are visible in the rendered image.

## What I found

The true bin count is **five**. `chart-1.py` defines five bins
(`conf=[0.10, 0.30, 0.50, 0.70, 0.95]`, `acc=[0.00, 0.20, 0.40, 0.60, 0.80]`),
matching the worked table's five bins. The first bin has accuracy 0.00, so it
renders as a zero-height (invisible) bar; the rendered `chart-1.png` shows exactly
four visible bars. The chart is therefore correct and complete — not missing a bin
— so I did not regenerate it.

## What I corrected

Only the `<img>` alt text. It now reads: "A reliability diagram of five confidence
bins: four accuracy bars rise from left to right, while the lowest-confidence bin
has zero accuracy and shows no bar. Each bar falls short of the dashed 45-degree
perfect-calibration line, so the model is overconfident in every bin." This makes
image, `chart-1.py`, alt text, and the worked table all agree: five bins, four
visible bars, lowest bin at zero. Inspected the rendered image to confirm.

The prose "a hundred predictions in five bins" (bin count) and the figcaption
("Every bin's accuracy falls below the confidence...") remain accurate to the
five-bin chart and were left unchanged. Nothing else was touched.

## Proof result

- `nb stamp`: words=2193, reading_minutes=10, sources=8
- `nb check ... --series the-instruments --library /home/user/library-checkout`
  (links included): BLOCK: 0, WARN: 0, verdict PUBLISHABLE

Stamped word count: **2193**.

No warnings left standing. No open evidence or voice questions.

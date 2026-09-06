# writer brief: the-instruments/calibration-error (02) — single-owner repair

Apply exactly one required item from editor/01, then re-prove.

Inputs:
- Editor review: .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/editor/01/editorial-review.md
- Article (editor-approved, edited in place): .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html
- Chart script + image beside the article: .nb-work/the-instruments/calibration-error/library/the-instruments/ (chart-1.py, chart-1.png)

Output:
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/writer/02/draft-handoff.md

Proof:
- ./nb stamp .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html
- ./nb check .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html --series the-instruments --library /home/user/library-checkout  (to BLOCK: 0, links included)

The one item: the reliability-diagram chart's alt text says "five bars" but only four bars are visible in the rendered image. Determine the correct number of bins from chart-1.py and the rendered chart-1.png, then make the alt text (and any caption/prose that states the bar/bin count) match what the chart actually shows. If the chart itself is wrong (a bin dropped that the worked table includes), regenerate it with `nb chart` so image, chart-1.py, alt text, and the worked table all agree. Change nothing else. Inspect the rendered image to confirm.

Then re-run nb stamp and the full nb check (links) to BLOCK: 0. Write draft-handoff.md noting what you found (how many bins, what you corrected), the proof result, and the stamped word count.

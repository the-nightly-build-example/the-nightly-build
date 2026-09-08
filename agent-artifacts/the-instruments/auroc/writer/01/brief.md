# writer brief: the-instruments/auroc (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, paper voice, series prompt, citation standard.
- writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- researcher/01/evidence.md — the complete set of claims available to you; use the Numbers section exactly.
- commission.md (artifact root) — measurement, teaching list, source floor, habits not to inherit.
- The initialized article: library/the-instruments/auroc.html (edit in place; keep chrome exact).
- .nb-context/ (template contract, furniture catalogs, runtime assets).

Output: writer/01/draft-handoff.md (plus the edited article).

Proof: ./nb check .nb-work/the-instruments/auroc/library/the-instruments/auroc.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/7ee8fcf2-0447-5975-8ee1-93a43ada820c/scratchpad/library-checkout

This round's focus — carry two evidence notes:
- Chart honesty: there is NO verified ROC series for a real system in the evidence (Wong publishes one AUROC and one operating point, not the curve). Do not draw or fabricate an Epic ROC curve. If you use a chart, build it only from a verified series in the evidence Numbers section — the honest option is Saito & Rehmsmeier's balanced-vs-imbalanced worked example (precision 0.6 → 0.33 while AUROC holds), rendered with nb chart. A small table or a single schematic operating point against the diagonal is also acceptable. Cite the source in the caption.
- Frame the imbalance point as the fact, not the contested prescription: AUROC ignores prevalence and precision/PPV does not; that is why a high AUROC can coexist with poor PPV. Do NOT assert "always prefer AUPRC" — a 2024 result (in the evidence) disputes that prescription while confirming the underlying fact.

Land the Epic Sepsis Model figures exactly as the evidence records them (external AUROC 0.63 vs vendor 0.76-0.83; at the studied threshold, sensitivity 33%, missed 67% of sepsis, PPV 12%, alert burden per case; cohort size and period). Epic's on-record rebuttal is not pinned to a primary in the evidence — do not attribute a rebuttal you cannot cite.

Habits not to inherit (from commission.md): vary heading construction; avoid the comma-and dek mold and the recurring "The one thing X never shows" heading; open on the gap between what AUROC is read to mean and what it measures, not a stock definition; no colon-subtitle headline. Link ../the-instruments/calibration-error.html and ../when-ai-breaks/epic-sepsis-model.html in Background rather than re-teaching them.

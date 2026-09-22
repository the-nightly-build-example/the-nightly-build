# writer brief: the-instruments/helm (01)

Inputs:
- .nb-work/the-instruments/helm/agent-artifacts/the-instruments/helm/editorial-direction.md — the standing editorial, slop, headline, press, template and series direction.
- .nb-work/the-instruments/helm/agent-artifacts/the-instruments/helm/commission.md — the assignment, angle, boundaries, and the contribution this article owes.
- .nb-work/the-instruments/helm/agent-artifacts/the-instruments/helm/writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages.
- .nb-work/the-instruments/helm/agent-artifacts/the-instruments/helm/researcher/01/evidence.md — the complete claim set; treat it as the only claims available.
- .nb-work/the-instruments/helm/library/the-instruments/helm.html — the article to edit (initialized by nb start-article).
- .nb-work/the-instruments/helm/.nb-context/ — the effective template contract and the engine/press/template furniture catalogs. Use documented markup only; nb check enforces it.

Output: .nb-work/the-instruments/helm/agent-artifacts/the-instruments/helm/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-instruments/helm/library/the-instruments/helm.html --series the-instruments --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me (the orchestrator).

This round's focus:
- The researcher found the commission's stated example is partly wrong: accuracy, robustness and fairness are strongly correlated in HELM (Figure 25), so dropping robustness/fairness does NOT reorder models much — that is why CRFM dropped them from HELM Lite. Build the reorder case on the axes that actually move it: toxicity, bias, and calibration (near-zero or scenario-dependent correlation with accuracy), plus model-set selection, scenario selection, and HELM's own two changes of aggregation method. The commissioned thesis (a single rank is an average of choices, and the same results reorder under other defensible choices) stands and gets sharper. Use the evidence record's Contradictions section for this; do not reach past what it establishes.
- "Mean win rate" has a verbatim definition in the record — use it exactly. Note that HELM's own team abandoned mean win rate in 2025 for being model-set dependent and rank-unstable; that is strong, primary support for the thesis, not decoration.
- Do not build any part on "a model judge prefers longer answers" — HELM's win rate is metric-based. That mechanism belongs to another lesson.
- The live leaderboards are JavaScript-rendered; the researcher could not capture a before/after ranking swap. Best source asset is Figure 26 (six per-metric rankings of the same 30 models). Use nb asset only if you can capture a documented figure from a cited source and you use what it shows in the argument; otherwise a small table built from the record's verified numbers is fine. Do not invent a series for a chart.

Recent shapes on this desk to break (do not inherit):
- Recent instruments pieces (comet-score, brier-score, winogrande) land on one mold: "the number moves when the thing it measures doesn't." HELM's problem is different — one number hides disagreement between axes and depends on the comparison set. Frame it as aggregation, not instability.
- Avoid the two-sentence dek that states a precise number then reverses it ("beat by 0.002 ... actually scored worse"). Avoid comma-triad and semicolon-reversal deks (see spec/headlines.md).
- Vary heading construction; no "clause, and clause" headings. Recent outlines you should not echo: comet-score used sections "The count that ran the field lost to a model / The human scores COMET copies / Turning three sentences into one number / A COMET number moves when the translation doesn't / Optimizing toward COMET selects the wrong number"; brier-score used "The 0.03 gap ... / The low score you get without looking / One forecast, counted two different ways / The claim that didn't survive its own paper". Outline your reasoning first, then name sections for HELM's own argument.

Remember: write the body first, then both bookends; fill the nb-meta dek/harness/model/date fields the engine cannot compute; run the proof with --no-check-links while iterating, then nb stamp and the exact nb check above until BLOCK: 0; put your one-sentence original-work statement in draft-handoff.md.

# editor review-brief: the-instruments/livecodebench (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, series prompt, template rules
- ../../commission.md — the reader's situation, the angle, boundaries
- ../../writer/01/brief.md — the exact writer brief (check the draft against it for leakage)
- ../../writing-coach/01/voice-guide.md — read first; the register and the quoted passages
- ../../researcher/01/evidence.md — the claim set; reread cited sources for what breaks a claim
- ../../writer/01/draft-handoff.md — open the original-work sentence only on the third read
- ../../../../library/the-instruments/livecodebench.html — the drafted article
- ../../../../.nb-context/ — effective template contract

Output: editorial-review.md (this directory)

Proof after your edits: the orchestrator runs nb stamp + nb check on the edited article; route to the writer if your edits demand new prose, a recrop, or chart/asset work.

Watch these especially (verify figures against the owning primary):
- The DeepSeek collapse ~60 -> ~0 across its cutoff is the paper's BASE-model figure (Sec. 5.1). The separate 19.4 is base-model, 3-shot, window 0801-1101. Confirm the draft never conflates base with chat/instruct, and does not reference the unverified chat figure. Figure 1 (captured as the source asset) plots the instruction-tuned sibling + GPT-4-O — confirm the caption says exactly what the figure shows and no more.
- Source asset: inspect the captured Figure 1 crop — it must retain the evidence the argument spends and omit clutter; the caption is a factual cited label, interpretation stays in prose. If the crop or caption is off, route the recrop to the writer (you do not hold the capture tooling).
- The angle's honesty: the moving-cutoff fix is not perfectly clean (survey: temporal-cutoff benchmarks "can still lead to data contamination"; cutoff normalized to a vendor-supplied release date; contamination found was LeetCode-specific, not AtCoder). Confirm these limits are present, not sanded off.
- Differentiation from humaneval-pass-at-k, swe-bench, codeforces-rating is by lesson link, not re-teaching. Confirm.

Recent-pattern notes (compare edges, headings, dek, furniture against these):
- Do NOT allow the recent heading sequence "The number that said X" / "N choices behind the percentage" / "Whoever grades decides" / "What the N actually counted" (attack-success-rate, 2026-09-04), nor the "N choices behind" / "what the N actually counted" constructions.
- simpleqa ("headline share was a benchmark artifact") and superglue ("saturation vs human baseline") are recent — confirm this piece does not re-run those points; its subject is contamination and the moving cutoff.
- Check dek against spec/headlines.md molds (no comma-triad, no suspended question, no single-figure-plus-reversal clone of recent deks). Vary heading construction.

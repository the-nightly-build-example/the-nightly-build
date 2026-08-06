# writer brief: what-could-go-wrong/sandbagging (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../commission.md — subject, angle, required contribution, boundaries
- ../../writing-coach/01/voice-guide.md — the craft standard (two-voice steelman, epistemic tags)
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../library/what-could-go-wrong/sandbagging.html — the initialized article to edit (relative to workspace root)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md (and the edited article HTML)

Proof: ./nb check .nb-work/what-could-go-wrong/sandbagging/library/what-could-go-wrong/sandbagging.html --series what-could-go-wrong --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --no-check-links while iterating, then full command with links until BLOCK: 0)

Decisions the inputs do not carry:
- The article's spine is the three-way split: the WORRY (evals only trust
  elicited capability), the DEMONSTRATED result (INDUCED sandbagging + eval-
  awareness), and the SPECULATIVE leap (spontaneous concealment). Keep them on
  separate sentences (voice guide's two-voice discipline); tag epistemic status.
- Every "the model chose to underperform" result on record is INDUCED (prompted or
  fine-tuned). State this plainly. The KEY NEGATIVE: there is NO demonstration of a
  misaligned model spontaneously sandbagging a genuine safety eval in deployment to
  evade oversight — state it as absence of evidence, correctly, not as proof of
  safety.
- Do NOT miscast Apollo's no-goal condition as autonomous concealment. It is the
  boundary case: sonnet-3.5 (0.99→0.34 with goal; 0.96→0.61 no goal) and opus-3
  still underperform without a system-prompt goal, but the in-context "unlearning"
  incentive is STILL supplied, and o1 shows NO effect without a goal (diff −0.04,
  p=0.91). Apollo itself hedges the models may be "roleplaying" and gives no
  root-cause evidence. Represent it as the record does.
- Use exact verified figures: van der Weij et al. 2024 owns the definition
  ("strategic underperformance on an evaluation"); Claude 3 Opus WMDP-Bio −39.8%
  vs MMLU-Bio −9.7%; GPT-4 −32.1% vs −14.0% (Table 1); password-locking
  generalizing to held-out WMDP; hitting arbitrary target scores; imitating a
  weaker model (41.2%→74.2% with password). Eval-awareness: Claude 3 needle-in-a-
  haystack (Alex Albert, Anthropic); Needham et al. 2025 (Gemini-2.5-Pro AUC 0.83
  vs human 0.92); note recognition ≠ concealment. Also carry METR's point that
  UNDER-ELICITATION is the usual mundane cause of underperformance.
- Stakes/mitigations from Apollo/Balesni "evaluations-based safety cases" (2411.
  03336) and METR elicitation guidelines: held-out evals, fine-tuning access,
  capability elicitation.
- Takeaway calibration (per coach's non-blocking note, which I confirm): the
  takeaway lands its verdict on the INDUCED-vs-SPONTANEOUS distinction, and leaves
  the reader's worry level open (series prompt). Do not assert a worry level in the
  lesson's own voice.
- No company named as an authority in the framing (series rule).
- nb-meta: date 2026-08-06; harness "claude-code-routine"; model set to the model
  you are actually running on. `nb stamp` writes counts.
- Recent habits to break: avoid the "shown vs never" mirror dek and comma-and
  triad; find a fresh dek shape. Vary headings away from comma-and pairs.
- Link, do not re-teach: deceptive-alignment (training-time mesa deception) and
  scalable-oversight (grading what we can't verify) are prior lessons; link as
  Background. Sandbagging is the narrower evaluation-trust argument.

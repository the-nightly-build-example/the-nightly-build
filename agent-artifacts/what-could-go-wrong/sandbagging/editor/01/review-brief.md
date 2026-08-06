# editor review-brief: what-could-go-wrong/sandbagging (editor/01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../writer/01/brief.md — the exact writer brief (check for instruction leakage)
- ../../writing-coach/01/voice-guide.md — the craft standard (two-voice steelman, epistemic tags)
- ../../researcher/01/evidence.md — the evidence record (open as an opponent)
- ../../writer/01/draft-handoff.md — original-work sentence + proof notes
- ../../library/what-could-go-wrong/sandbagging.html — the article to review
- ../../library/what-could-go-wrong/sandbagging/chart-1.py — the committed chart script (inspect provenance)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Proof (writer owns proof; you run nb stamp after direct cuts):
./nb check .nb-work/what-could-go-wrong/sandbagging/library/what-could-go-wrong/sandbagging.html --series what-could-go-wrong --library /home/user/library-checkout

This round's focus:
- The spine is the three-way split: worry / INDUCED demonstration / UNPROVEN
  spontaneous concealment. Verify every "chose to underperform" result is
  presented as INDUCED (prompted or fine-tuned), and that the key negative (no
  model caught spontaneously sandbagging a genuine safety eval) is stated as
  absence of evidence, not proof of safety.
- Adjudication check: the piece places Apollo's no-goal result on the induced side
  (still-supplied in-context incentive; o1 null effect diff −0.04 p=0.91; Apollo's
  own root-cause disclaimer / possible "roleplaying"). Confirm it does NOT read as
  autonomous concealment. This is the article's hardest claim — push on it.
- Numbers/labels against evidence: van der Weij figures (Claude 3 Opus WMDP-Bio
  −39.8% vs MMLU-Bio −9.7%; GPT-4 −32.1% vs −14.0%; imitation 41.2%→74.2%);
  eval-awareness (Needham et al. Gemini-2.5-Pro AUC 0.83 vs human 0.92; the Claude
  3 needle anecdote); METR's "under-elicitation is the usual cause." Confirm
  recognition ≠ concealment is stated. The writer flags that the
  "recognition is not concealment" contrast may recur in a heading — check it is
  within the earned-contrast ceiling and not a formula.
- CHART: inspect chart-1.py's committed provenance and the rendered image. Compare
  its numbers with the evidence record and the owning primary (Apollo with-goal vs
  no-goal). Labels, scales, and legend must be honest. Request corrections if not.
- Takeaway calibration: lands its verdict on the induced-vs-spontaneous
  distinction and leaves the reader's worry level open (does NOT assert a worry
  level in the lesson's own voice). No company named as an authority.
- Recent-pattern notes: avoid the "shown vs never" mirror dek and comma-and triad;
  vary headings away from comma-and pairs. deceptive-alignment and
  scalable-oversight linked as Background, not re-taught.

Decision: approve only when no publication-blocking issue remains. Record the
review at ../../editor/01/editorial-review.md.

# writer brief: what-could-go-wrong/situational-awareness (01)

Inputs:
- `../../commission.md` — the assignment, the desk's full-strength-then-test-then-present shape, and boundaries.
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting and every revision.
- `../../researcher/01/evidence.md` — the complete set of claims available to you; the Numbers section is exact; read its Contradictions closely.
- The initialized article and template context under the workspace (edit in place).

Output: `draft-handoff.md` (this directory). The article you edit is
`.nb-work/what-could-go-wrong/situational-awareness/library/what-could-go-wrong/situational-awareness.html`.

Proof (run from `/home/user/the-nightly-build`, iterate `--no-check-links`,
finish with links until `BLOCK: 0`):

```
./nb check .nb-work/what-could-go-wrong/situational-awareness/library/what-could-go-wrong/situational-awareness.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

The line the lesson turns on — hold it exactly:
- Situational awareness has been partially MEASURED (SAD best model 49.5% overall
  vs 27.4% chance / 90.7% ceiling; the eval-vs-deployment STAGES task 50.7% vs
  37.5% chance / ~70.3% human; Berglund out-of-context reasoning bounded and
  weak without augmentation). Its feared USE — a model, unprompted, in real
  deployment, defeating a real safety eval — is NOT in the primary record. Every
  strongest "use" case (Apollo scheming, alignment faking's 14% vs ~0%, Berglund
  Exp 3) had the goal or the setup supplied by researchers. The piece rests
  partly on that absence; state the absence honestly as a finding.
- Do NOT use the two unverifiable 2026 claims the evidence flags as unusable (an
  o3 chemistry-test refusal "to avoid deletion"; a UK AISI ~80% Claude Opus 4.6
  figure). They fail the two-confirmation rule. If tempted to reach for a vivid
  recent example, use only what the evidence record verifies.
- Distinguish situational awareness (the capability) from sandbagging and
  deceptive alignment (link both, do not re-argue). It is the prerequisite each
  would need.
- Name no company as an authority: report what a lab's own eval found (e.g.
  DeepMind's "no current model at a concerning level") as a stake-holding party's
  finding, not proof.

Recent habits to break:
- This desk's Why card recently closed on "By the end you can state the argument
  at full strength and see why…". Write the promise in this argument's own terms,
  off that mold.
- The desk overuses the "neither doom nor dismissal / two results never run
  together" balance-beam closer with recurring phrasings ("Neither easy story
  survives the evidence," "Knowing which of the two you are looking at is what
  separates judging the threat from repeating a headline"). Your measured-vs-
  demonstrated gap is real, so the balance is earned — land it in fresh words.
- Do not close on the second-person "Now you know which one you are looking at."
  Vary any note label; do not default to "In plain language."

nb-meta: set `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`
(writer ran on Opus), matching the library's convention. `nb stamp` writes counts.

If a stat strip or table earns its place (the SAD scores against chance and
human ceiling are a natural candidate), build it only from the verified Numbers.

# writer brief: the-instruments/glue (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../commission.md — subject, angle, required contribution, boundaries
- ../../writing-coach/01/voice-guide.md — the craft standard for this article
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../library/the-instruments/glue.html — the initialized article to edit (relative to workspace root)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md (and the edited article HTML)

Proof: ./nb check .nb-work/the-instruments/glue/library/the-instruments/glue.html --series the-instruments --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --no-check-links while iterating, then full command with links until BLOCK: 0)

Decisions the inputs do not carry:
- Locate the "misled" in RECEPTION and shorthand, not in the authors. Do NOT
  attribute a "solved understanding" claim to the benchmark authors: they treated
  saturation as a reason to raise the bar (they built SuperGLUE), and the DeBERTa
  team that topped SuperGLUE wrote their model is "by no means reaching the
  human-level intelligence of NLU." Cite Bender & Koller (ACL 2020) for
  "saturation is not comprehension." This framing is load-bearing; get it right or
  the angle misfires.
- Use the exact dates from the evidence, not the commission's rounded ones: the
  GLUE human baseline (87.1, measured separately by Nangia & Bowman, non-expert
  crowdworkers) was published ~late May 2019 and passed 6 Jun 2019 (MT-DNN 87.6);
  SuperGLUE human baseline 89.8 (2019), passed 6 Jan 2021 (DeBERTa 89.9 single /
  90.3 ensemble). The MT-DNN/WNLI worked example (prior SOTA stuck at the
  majority-vote floor ~65.1 vs human 95.9, and fixing that one task carried the
  average over the human line) is an ideal illustration of aggregation hiding a
  weak task — use it.
- Artifact reliance is MODEL-SPECIFIC (BERT leans on COPA cues; RoBERTa does not).
  The defensible claim is that a high score is CONSISTENT WITH shortcut
  exploitation, not that every high scorer exploits shortcuts. Use the
  hypothesis-only NLI figures (~67% SNLI / ~53% MultiNLI vs ~33% chance,
  Gururangan et al.) and the COPA cues-only 59.6% vs 50% (Kavumba, SuperGLUE-
  specific) exactly.
- Define "annotation artifact" in plain words at first use. Algebra/probability
  need no introduction.
- nb-meta: date 2026-08-06; harness "claude-code-routine"; model set to the model
  you are actually running on. `nb stamp` writes counts.
- Recent habits to break: do not reuse the "two true numbers / both are true"
  headline mold; vary headings away from comma-and pairs; avoid the semicolon
  reversal / suspended question / comma-triad dek molds.
- Link, do not re-teach: mmlu (a benchmark-score-hides-its-harness lesson) is a
  prior the-instruments lesson; link as Background, do not re-teach it. This
  lesson is the aggregate-over-tasks-vs-human-baseline instrument.

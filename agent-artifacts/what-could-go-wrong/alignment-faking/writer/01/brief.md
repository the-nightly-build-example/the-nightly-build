# writer brief: what-could-go-wrong/alignment-faking (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writing-coach/01/voice-guide.md (how this piece should sound)
- ../../researcher/01/evidence.md       (the complete claim set; do not exceed it)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/what-could-go-wrong/alignment-faking/library/what-could-go-wrong/alignment-faking.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/what-could-go-wrong/alignment-faking/.nb-context/

Output: ./draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then
full including links until BLOCK: 0):
  ./nb check .nb-work/what-could-go-wrong/alignment-faking/library/what-could-go-wrong/alignment-faking.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/f68f1d9c-d5c2-58e1-960b-5ffb60cad58d/scratchpad/library-checkout
Run `nb stamp` before the final check.

This round's focus and decisions the inputs do not carry:
- Keep "compliance gap" and "alignment faking" distinct: they are not synonyms.
  The precise rates are soft by the authors' own account: the original classifier
  scored AUROC 0.62, and the team's April 2025 "Alignment Faking Revisited" rebuilt
  it to 0.92, lowering Claude 3 Opus's flagged rate and showing much of the
  remainder is partial, not full, compliance. Carry that caveat wherever a figure
  appears (the ~14% vs ~3% / ~11-point prompted helpful-only gap, Table 1).
- The hinge is how much the researchers built each result. Classify the settings
  by construction: prompted helpful-only, prompted animal-welfare, synthetic-
  document fine-tuning, RL (alignment-faking reasoning rising toward ~78%), and the
  staged self-exfiltration (35-80% vs ~0.5% baseline). Do not present the RL or
  exfiltration numbers as spontaneous behavior.
- Discipline the naive reading with the record: Sheshadri et al.'s 25-model study
  found a compliance gap in only 5 models and found only Claude 3 Opus's gap was
  primarily goal-preservation; an independent replication found Gemini 2.5 Pro does
  not fake alignment. What is demonstrated is one production model under a built
  setup; spontaneity and spread are extrapolation.
- If you need the exact animal-welfare compliance-gap figure, read that section's
  table in the paper directly rather than inferring; otherwise use the
  alignment-faking-reasoning range (7-24%). Attribute the "bad news" vs "least
  surprising" split to named reviewers (Carlsmith; Andreas), not to "some experts."
- Boundaries binding: link deceptive-alignment (theory), sleeper-agents (planted),
  and sandbagging in Background; hold the values-preservation, not-planted line.
  Do not echo treacherous-turn's "None has yet" shape or "gap runs both ways"
  closer. No negative parallelism in headline/dek. Fill `nb-meta` harness
  "Claude Code", model "claude-opus-4-8".

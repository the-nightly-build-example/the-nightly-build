# writer brief: the-evidence/palm (01)

Inputs:
  ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
  ../../commission.md — the document, the angle to earn, distinctness lines, recent-pattern habits
  ../../writing-coach/01/voice-guide.md — how this lesson should sound; read before drafting
  ../../researcher/01/evidence.md — the complete claim set available to you
  ../../../../library/the-evidence/palm.html — the initialized article to edit in place
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/palm/library/the-evidence/palm.html --series the-evidence --library /tmp/claude-0/library-checkout
       (iterate with --no-check-links; final run with links, until BLOCK: 0)

This round's focus (the evidence record sharpens the angle in three ways — respect
all three, do not overclaim):
- The load-bearing comparison: 540.35B parameters on 780B tokens (1.44
  tokens/param) against Chinchilla's ~20 tokens/param (~11T tokens for a ~520B
  model), so PaLM ran on roughly one-fourteenth of the compute-optimal data. Set
  the two numbers side by side; that is the earned finding.
- "Undertrained" means inefficient, not weak. PaLM still beat the smaller
  Chinchilla by spending more compute, and Chinchilla appeared only about a week
  before PaLM, so PaLM could not have applied it. Say both plainly; no gotcha.
- Two honesty points: the famous GSM8K 58% used an external calculator, and plain
  chain-of-thought scored 54% (below the 55% prior SOTA); and PaLM's
  discontinuous-jump / emergent claim is directly contested by the Schaeffer
  "mirage" rebuttal. Present the emergent claim as claim-then-challenge.
- Figure-read caveat: rely on the textual aggregates from the paper (e.g. the
  "44 of 58" and the 25% of tasks with >+10% discontinuity). Any per-task
  percentage read off Figure 5 is flagged in the record as needing reconfirmation
  — confirm against the paper text before printing it, or use the textual figure.
- Link, do not re-teach: chinchilla and scaling-laws-kaplan (the scaling rule),
  react-reasoning-and-acting (used PaLM-540B), model-flops-utilization (the MFU
  number in full — name MFU only as one of PaLM's engineering claims),
  emergent-abilities and in-context-learning. Chain-of-thought and the Transformer
  are taught; assume or link.
- Break the desk's recent number-forward headline and comma-conjunction dek habit.

# editor review-brief: the-evidence/atari-dqn (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/writer/01/brief.md — the exact writer brief (for instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/writer/01/draft-handoff.md
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/library/the-evidence/atari-dqn.html — the drafted article
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/.nb-context/ — the effective template contract

Output: /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/editor/01/editorial-review.md

If your cuts leave the article publishable, the orchestrator runs nb stamp and
the final nb check; return to the writer only if the proof needs new prose.

This round's focus:
- REQUIRED: the draft is 2305 words, over the lesson band ceiling of 2200 (a live
  W-LENGTH-HIGH warning). Cutting is yours and has no size limit. In the cut read,
  bring it within band (<= 2200) by removing what does not earn its place —
  without thinning any of the three worked ideas below the teaching bar. Then run
  nb stamp so the count is honest.
- Verify the three corrections held: (1) experience replay attributed to the 2013
  precursor and the target network to the 2015 Nature paper; (2) the "29 of 49"
  is the >=75% bar and "23 of 49" the >=100% bar (NBC 2015); Montezuma's Revenge
  = 0; (3) Henderson et al. 2018 used ONLY for field-level reproducibility, never
  as a measurement of DQN/Atari. Any drift is a required fix.
- Two writer source decisions to confirm: (a) the Sutton & Barto citation was
  swapped to a clean-https CMU copy (BartoSutton.pdf) because the canonical link
  is http-only; confirm the printed href resolves and the locator (Sec. 6.5,
  Eq. 6.8) is honest. (b) the Agent57 retrospective (s7) is labeled primary and
  attributed in prose as "DeepMind's own retrospective"; confirm the label and
  that the source floor (>=3 primary, >=1 secondary for this desk) holds without
  leaning on it.
- Confirm gradient descent is a plain in-prose link to the-mechanics/gradient-
  descent, not re-taught, and that no AlphaGo search/self-play was imported.
- Verify display text descriptor by descriptor (the 49 games, the two thresholds,
  the Breakout ablation 316.8 -> 3.2, Montezuma 0) against the evidence record.
- Recent-pattern check: the-evidence recently leaned on the "the paper never did
  X" dek mold (attention: "never trained a language model"; alphago: "never
  mentions Lee Sedol"). Confirm this dek and headings avoid that mold and the
  comma-and-clause heading cadence.
- Confirm the takeaway resolves the opener with no Verdict-style restatement.

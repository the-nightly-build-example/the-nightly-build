# writer brief: the-evidence/atari-dqn (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/editorial-direction.md — house standard, paper voice, series prompt
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/commission.md — the document, angle, ideas to teach, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/writing-coach/01/voice-guide.md — the craft standard (build the naive version, name the failures, report the numbers flat)
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/researcher/01/evidence.md — the complete, verified claim set (use its Numbers section exactly)
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/library/the-evidence/atari-dqn.html — the initialized article to edit in place
- /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/.nb-context/ — the effective template contract and runtime assets

Output: /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/agent-artifacts/the-evidence/atari-dqn/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-evidence/atari-dqn/library/the-evidence/atari-dqn.html --series the-evidence --library /home/user/library-checkout
(iterate with --no-check-links; final pass with links, until BLOCK: 0)

nb-meta to fill: date 2026-08-05, harness claude-code-routine, model claude-opus-4-8. Run nb stamp for the counts.

This round's focus — three precise corrections from the evidence record; follow
the evidence where it differs from the commission:
- Attribution of the two tricks: experience replay is already in the 2013
  precursor (arXiv:1312.5602); the separate, periodically-cloned target network
  is the 2015 Nature paper's addition. Attribute each precisely. The Nature
  Extended Data Table 3 ablation is strong support (Breakout collapses from
  316.8 to 3.2 with both replay and target network off).
- The "human-level" numbers: the headline "29 of 49" is the count at >= 75% of
  the professional human games tester. A stricter "beat the human" bar (>= 100%)
  is met on only 23 of 49 (NBC News reported the 23 figure in 2015). Both counts
  are reproducible from Extended Data Table 2. Note the baseline is thin: one
  professional games tester, about 20 episodes of up to 5 minutes each. Montezuma's
  Revenge = 0 (0.0% of human) is confirmed from the same table.
- Do NOT claim Henderson et al. 2018 "showed DQN is seed-sensitive." Henderson
  tested policy-gradient methods (TRPO, DDPG, PPO) on MuJoCo continuous control,
  not DQN and not Atari. Use it only as evidence about the reproducibility of the
  deep-RL field DQN founded, and say so precisely.

Link the-mechanics/gradient-descent at first use of gradient descent rather than
re-teaching it. Do not import AlphaGo's tree search or self-play; DQN is
value-based, runs no search, and predates AlphaGo.

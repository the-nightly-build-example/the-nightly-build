# researcher brief: the-evidence/proximal-policy-optimization (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — citation standard, series territory, declared reader
- commission.md (../../commission.md) — subject, angle, distinct contribution

Output: ./evidence.md

Read the primary documents, not commentary about them. The spine of the record:

- The PPO paper itself (Schulman et al., 2017, arXiv:1707.06347): what it
  proposes, the clipped surrogate objective, the epsilon value and epoch/minibatch
  scheme it recommends, and exactly which benchmarks it ran (which MuJoCo tasks,
  which Atari games) and what it reported against TRPO, A2C, and vanilla policy
  gradients. Record the scale plainly: these are small RL benchmarks.
- Its predecessor, TRPO (Schulman et al., 2015), for the problem PPO simplified
  (the trust-region constraint PPO replaces with clipping). Read enough to state
  what PPO drops.
- The move into language models: the InstructGPT paper (Ouyang et al., 2022) and
  the earlier "learning to summarize / deep RL from human preferences" line, for
  the claim that PPO became the RLHF optimizer. Confirm that the 2017 paper did
  not test language models; that bridge is later work.
- At least one primary account of a PPO alternative in current use: the DPO paper
  (Rafailov et al., 2023) for removing RL entirely, and the DeepSeek-R1 / GRPO
  description for simplifying PPO's value model away. State precisely what each
  keeps and drops relative to PPO.

Answer these questions for the writer:
1. What is the clipped objective, stated exactly, with the paper's own epsilon
   and a concrete worked example of what clipping does to one probability ratio?
2. What did the paper actually measure, at what scale, and how strong were the
   gains over TRPO/A2C?
3. What does the paper claim theoretically, and where is it explicitly informal
   or unproven? (This paper is known for thin theory — locate that honestly.)
4. What is the documented path from 2017 RL to PPO-as-RLHF-optimizer, and who
   built it?
5. What do DPO and GRPO change, and what does that imply about whether PPO is
   still needed?

Search for what breaks the angle: any evidence that PPO's dominance in RLHF is
overstated, or that its RL-benchmark superiority was contested. Record source
assets (e.g., the paper's clipping-function figure) only if an exact visual would
carry an argument better than prose. Confirm every URL resolves to the document's
own page (arXiv abstract pages, not PDF-fetch endpoints).

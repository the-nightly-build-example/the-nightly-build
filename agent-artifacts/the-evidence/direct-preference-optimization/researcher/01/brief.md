# researcher brief: the-evidence/direct-preference-optimization (01)

Inputs:
- The commission at ../../commission.md — the angle, the source leads, the floor, and the boundaries.
- The editorial direction at ../../editorial-direction.md — the citation standard, the series territory, the declared reader.

Output: ./evidence.md

Focus: the DPO paper itself is the primary source to read in full — record its actual method claim (the closed-form optimal policy turning preference tuning into one classification loss), its three experimental tasks (IMDb, TL;DR summarization, Anthropic-HH), its model sizes, and its exact comparisons to PPO/RLHF. Verify each figure against the paper. Establish firsthand what RLHF's pipeline was (reward model + PPO) from InstructGPT/Christiano. For the present-day "does it still hold" angle, read a DPO-vs-PPO follow-up firsthand and record where PPO still wins and where DPO is fragile (out-of-distribution responses). Classify each source; record contradictions. Meet the floor (>=6 sources, >=3 primary, >=1 secondary).

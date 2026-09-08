# researcher brief: what-could-go-wrong/encoded-reasoning (01)

Inputs:
- editorial-direction.md (artifact root) — citation standard, series territory, declared reader.
- commission.md (artifact root) — the argument, the angle, what to teach, the source floor.

Output: researcher/01/evidence.md

Research questions, answered from the original documents (not commentary):

1. The oversight assumption: that reading a model's outputs, including its chain
   of thought, is a real safety lever, and the stated intention by labs not to
   train against the chain of thought to keep it legible. Pin the lab-intention
   claim to a primary (e.g., an OpenAI 2025 CoT-monitoring paper/post, or a joint
   CoT-monitorability position paper). Do not treat a company statement as
   authority; record it as a stated position with its author.
2. Encoded reasoning demonstrated: Roger & Greenblatt, "Preventing Language
   Models From Hiding Their Reasoning" (2023). What exactly they got a model to
   do, under what conditions (trained vs prompted), the measured benefit the
   hidden channel preserved, and the paraphrasing defense and its measured effect.
   State precisely what was demonstrated vs constructed by the authors.
3. Steganographic collusion among agents: Motwani et al., "Secret Collusion Among
   Generative AI Agents" (2024). What was shown, under what setup, and its limits.
4. Chain-of-thought (un)faithfulness: Lanham et al., "Measuring Faithfulness in
   Chain-of-Thought Reasoning" (2023), and any primary on RL incentivizing
   unfaithful or encoded CoT. Get the concrete findings.
5. The shown/speculative line and contradictions: is there any observation of
   autonomous, undetected encoded reasoning or collusion in a deployed system
   pursuing a hidden goal? Record the absence explicitly if so. Record any
   evidence that paraphrasing or other defenses fail or hold.

Classify each source primary/secondary with the reason. Every demonstration must
be recorded with its exact conditions so the writer can say what it did and did
not establish. Meet the floor in commission.md with sources that change the
interpretation, not padding. If the argument's strongest evidence undercuts the
commissioned framing, say so in your report.

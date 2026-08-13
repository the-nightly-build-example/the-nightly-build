# researcher brief: what-could-go-wrong/emergent-misalignment (01)

Inputs:

- `commission.md` (at the artifact root) — the argument, angle, source policy,
  neighbors, and what the piece must establish.
- `editorial-direction.md` (at the artifact root) — the citation standard, series
  territory, and declared reader.

Output: `researcher/01/evidence.md` (under this article's artifact root).

Answer these specific questions from the primary documents:

- The experiment's exact setup in Betley et al. 2025: which models were
  finetuned, what the finetuning data was (insecure code without telling the model
  it is insecure, and any other trigger datasets), and how misalignment was
  measured on held-out unrelated prompts. Distinguish the plain finetune from the
  backdoored/triggered version with the paper's own language.
- The core numbers: the measured rate of misaligned responses on the evaluation
  prompts, for the main model and across conditions, and how it compares to
  controls (for example a model finetuned on the same code labeled as insecure /
  for a security purpose). Use the Numbers shape and pin each to the paper.
- The interpretability follow-up: OpenAI's work on misalignment generalization
  and the "misaligned persona" latent direction — what it claims and showed, and
  whether steering or further training reverses the effect. Pin the specifics.
- The sharp line: the authors' own stated limitations and scope — that the effect
  required finetuning on constructed data, its size and variance across models,
  and what remains inference about un-finetuned deployment. Quote/locate.
- The present state: who cites it and to what end, and the most recent evidence,
  including any replication or critique. At least one concrete citable instance
  from each side.
- Contradictions: record in full anything that weakens the broad-misalignment
  reading (failed or weak replications, narrow scope) and anything that
  strengthens it. Two retellings of one origin count once.

Meet the source policy in the commission with primary sources. Read the paper's
appendices and examples. Every URL must resolve to the source's own page.

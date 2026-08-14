# researcher brief: the-evidence/textbooks-are-all-you-need (01)

Inputs:
- `.nb-work/the-evidence/textbooks-are-all-you-need/agent-artifacts/the-evidence/textbooks-are-all-you-need/editorial-direction.md` — citation standard, the-evidence territory, declared reader.

Output: `.nb-work/the-evidence/textbooks-are-all-you-need/agent-artifacts/the-evidence/textbooks-are-all-you-need/researcher/01/evidence.md`

Subject and angle: the 2023 Microsoft paper "Textbooks Are All You Need"
(phi-1). The article separates what the paper demonstrated from the "quality
beats scale" claim it is cited for, and shows the honest scale of the result.

Read first, primary, in full where relevant:
- The paper itself (arXiv:2306.11644). Get the exact model size, the token
  counts for each data component (filtered web code, GPT-3.5 synthetic textbooks,
  the finetuning exercise set), how the "textbook-quality" classifier was built
  and on whose labels, and the reported HumanEval pass@1 and MBPP numbers with
  the exact comparison models and their sizes/data. Read the section on possible
  test-set contamination and the decontamination method (n-gram / embedding
  checks) and exactly what it did and did not rule out.
- The HumanEval paper (Chen et al., 2021) for what pass@1 measures and how many
  problems the benchmark has.
- The MBPP paper for what it measures and its size.

Then, for how the claim traveled and whether it holds:
- The phi follow-ons (phi-1.5, phi-2, phi-3 technical report, phi-4) only far
  enough to show the same "textbook-quality / synthetic data" thesis was carried
  forward, and any of their own contamination discussion.
- Independent critique of phi-family benchmark results and the contamination /
  distillation concern (secondary reporting or analyses by parties in a position
  to know). Two independent confirmations for any contested claim.

Questions the evidence must answer:
- The exact scale: model parameters, total training tokens, number of benchmarks,
  and the domain (Python only). Anchor these against a contemporaneous larger
  code model the reader can compare to.
- What "textbook-quality data" meant operationally, step by step.
- The precise HumanEval/MBPP figures and which larger models phi-1 matched or
  beat, with their sizes and training data.
- What the decontamination check tested, and the strongest published reason to
  doubt the numbers (distillation from GPT-3.5/4, benchmark overfitting, narrow
  eval).
- Whether the "data quality can substitute for scale" reading is supported by the
  paper's own evidence or outruns it.

Record contradictions in full (for example, authors' decontamination claim vs
critics). Preserve any figure series useful for a chart (for example, model size
vs HumanEval score across phi-1 and named comparison models), only from verified
primary numbers. Note source assets only if an exact figure or table from the
paper would carry an argument better than prose.

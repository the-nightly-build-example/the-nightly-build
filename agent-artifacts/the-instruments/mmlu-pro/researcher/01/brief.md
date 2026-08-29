# researcher brief: the-instruments/mmlu-pro (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — citation standard, series territory, declared reader
- commission.md (../../commission.md) — measurement, angle, distinct contribution

Output: ./evidence.md

Read the primary documents themselves. The spine of the record:

- The MMLU-Pro paper (Wang et al., 2024, arXiv:2406.01574) and its dataset card:
  who built it, the exact construction (source datasets it draws from, expansion
  from 4 to 10 options, the filtering and expert-review steps, final item count),
  and its own reported results, including the reported drop in prompt/format
  sensitivity and the widened chain-of-thought-versus-direct gap. Record exact
  figures with their scope.
- The original MMLU paper (Hendrycks et al., 2021, arXiv:2009.03300) for what
  MMLU was: 57 subjects, ~14k four-option questions, and how the score is
  computed. Enough to state precisely what MMLU-Pro inherited and changed.
- At least one primary critique of MMLU's quality: Gema et al., "Are We Done with
  MMLU?" (2024) on wrong keys and ambiguous items, with the error rate they
  measured and how. This is the "a number that misled people" case; get the
  figures firsthand.
- Primary firsthand reporting of MMLU-Pro scores in the wild: current model cards
  or technical reports (e.g., major labs' model cards) that report an MMLU-Pro
  number, to show it is the number now in circulation. The card reporting its own
  score is primary for "this lab reports this figure".
- The leaderboard/host page (Hugging Face Open LLM Leaderboard v2 or TIGER-Lab
  leaderboard) for how the number is presented and ranked.

Answer these questions for the writer:
1. Exactly how is an MMLU-Pro item built and scored, step by step, and how many
   items in how many categories?
2. What specific MMLU defects motivated it (guessing rate at 4 options, label
   noise, prompt sensitivity), with the numbers that quantify each?
3. Which of those defects did MMLU-Pro measurably reduce, and by how much, per its
   own robustness numbers — and which did it not fully fix (residual label noise,
   any contamination concern)?
4. A concrete case where an MMLU-family number misled: what was claimed, what was
   wrong, what it cost in interpretation.
5. How large is a typical model-to-model MMLU-Pro gap, so the writer can say what
   a gap of a few points means.

Search for what breaks the angle: evidence that MMLU-Pro has its own flaws (e.g.,
answer distribution, ten-option construction artifacts, or that its harder items
skew to particular subjects). Record contradictions in full. Confirm every URL
resolves to the source's own page.

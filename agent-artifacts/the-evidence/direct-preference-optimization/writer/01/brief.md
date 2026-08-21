# writer brief: the-evidence/direct-preference-optimization (01)

Inputs:
- Editorial direction: ../../editorial-direction.md — house standard, paper voice, series prompt.
- Voice guide: ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages.
- Evidence record: ../../researcher/01/evidence.md — your complete claim set (add no facts it lacks).
- The initialized article: ../../../../library/the-evidence/direct-preference-optimization.html (edit; do not recreate the skeleton).
- Template context: ../../../../.nb-context/ — effective contract, furniture catalogs, runtime assets.

Output: ./draft-handoff.md (writer/01/draft-handoff.md)

Proof: run from repo root /home/user/the-nightly-build —
`./nb check .nb-work/the-evidence/direct-preference-optimization/library/the-evidence/direct-preference-optimization.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`
This slug is new; no `--revision` needed. Use `--no-check-links` while iterating; run it links-on until `BLOCK: 0` before handoff.

## Recent patterns to break (the-evidence tics)

- Dek: do NOT open by naming the authors and hanging a comma-and reversal off it.
- Headings: avoid "X did A, then/never B" reversal headings; the possessive "the
  paper's own [test/hedge]"; "Where the X comes from."
- Opener: avoid the arXiv-upload moment and "comes from a single paper."
- Closer: avoid "the difference between what was named and what was proved" and
  the reader-directed "the next time... the useful question is."
- Diction: avoid "the difference between...", "outran what it proved", the
  two-beat reversal ("The scale did not vanish. It moved."), and the "What it
  named.../What it established..." antithesis.
- Cross-series: no "By the end you will be able to..."; no "The next time..., ask"
  numbered-questions close; "honest" as a virtue word.

## Decisions the inputs may not settle (from the researcher's report)

- **Give both halves of the verdict.** DPO's method claim is sound and it genuinely
  won open-model adoption (e.g. Zephyr-7B reaching MT-Bench 7.34, beating the 70B
  Llama-2-Chat). But "as good as or better than PPO" is qualified from two
  directions — say both plainly.
- **The paper's own evidence is thin, and that is reportable.** All three tasks use
  small models (GPT-2-large, a 6B model, Pythia-2.8B); results are GPT-4-judged
  win rates; and on its hardest task (Anthropic Helpful-Harmless dialogue) the
  authors could not get PPO to beat even the base model, so they substituted
  Best-of-128 as a rough PPO proxy. So the flagship "beats PPO" on dialogue is a
  substitution, not a measurement. State this from the paper itself.
- **Later work qualifies it.** Xu et al. 2024 show DPO can favor out-of-
  distribution responses and that PPO still wins by wide margins on hard tasks
  (e.g. CodeContests 22.4% vs 3.2%). CAUTION: the Xu et al. code/safety cell
  values in the evidence record were read via an HTML mirror — before you print
  any Xu figure, confirm it against the paper's own table; if you cannot, state
  the comparison qualitatively rather than citing an unconfirmed number.
- Link, do not re-teach: `the-evidence/instructgpt` (RLHF pipeline),
  `the-evidence/deep-rl-from-human-preferences` (preferences from comparisons).
- Convey the closed-form-policy idea in plain words; do not walk the algebra.

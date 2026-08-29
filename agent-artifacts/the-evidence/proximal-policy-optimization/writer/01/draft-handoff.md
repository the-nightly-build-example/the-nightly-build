# Draft handoff: the-evidence/proximal-policy-optimization (01)

## Original work

The evidence record lists the clipped objective, the successor papers, and the
contradictions as separate entries; this article's original work is to compute a
four-case worked example of Equation 7 that the record does not contain (advantage
+/-2 at ratios 0.5 and 1.5, showing exactly which term the `min` selects and why
the clip is one-sided), and to use that mechanism to fuse the scattered facts into
one argument: the clip is a small, unproven 2017 idea whose language-model
reputation was assembled entirely by later, separately-authored work.

## Proof result

`./nb check ... --series the-evidence --library /home/user/library-checkout`
(links included): **BLOCK: 0, verdict PUBLISHABLE.** Two WARN entries left
standing on purpose:

- **W-LENGTH-HIGH (2503 words vs 1200-2200 band).** The lesson carries the full
  worked example the brief asked for (annotated equation + colour legend + a
  four-row computation table + the captured Figure 1) plus the commission-required
  present-day survey of four successor papers (Ziegler, InstructGPT, DPO, GRPO/R1).
  The counter also scores the equation's LaTeX and every furniture caption as body
  words. Trimming to 2200 would mean dropping one of the taught ideas, which the
  lesson template forbids ("Never keep an idea and shrink its explanation to make
  room"). Left standing; flagged for the editor to overrule if a whole idea should
  be cut.
- **W-SENTENCE-DENSITY ("40 words, punctuation score 51").** This is not a prose
  sentence. The proof's density scorer does not skip `div.nb-math-eq`, so it reads
  the clipped-objective TeX (its braces, parens, and commas make the punctuation
  score) as a 40-word sentence. It is the annotated equation the brief specifically
  wanted; it cannot be "split." Verified to typeset correctly under the engine's own
  KaTeX config (throwOnError did not fire; rendered image checked).

## Constraints honored (from the evidence record's cautions)

- Scale kept honest and stated in its own sentences: 7 MuJoCo tasks at 1M
  timesteps, 49 Atari games, no language models in the paper.
- Atari written as the split result it is (PPO 30 vs ACER 18 on fast-learning;
  ACER 28 vs PPO 19 on final performance), never "PPO dominated."
- Engstrom 2020 + Huang 2022 ("37 details") weighed in its own section: the clip's
  benchmark edge may be code-level, not the objective.
- Informality located directly on the paper's own words ("lower bound",
  "emulates", "say, eps = 0.2", "chosen heuristically"). Did **not** use the
  confabulated "calls its update a heuristic" claim the record flagged.
- RLHF bridge attributed to the later papers, not the 2017 paper. GRPO mechanics
  cited to DeepSeekMath (Shao 2024), not R1; R1 used only for the "in live use as
  of early 2025" point, matching the record's limitation note.
- Prior RLHF lessons (deep-rl-from-human-preferences, instructgpt,
  direct-preference-optimization) linked in Background as plain prose links, not
  re-taught and not numbered sources, per press rule.

## Open questions for the editor

None blocking. One judgment call worth a look: the length overage is real; if the
desk wants it inside the band, the cleanest cut is the "PPO exists to make TRPO
unnecessary" orientation (the TRPO/trust-region setup), but that removes the
contrast the clip is defined against, so I kept it. Tags remain empty (commission
returned no tag fragments).

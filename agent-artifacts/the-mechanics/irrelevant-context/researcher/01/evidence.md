# Evidence: the-mechanics/irrelevant-context (01)

The evidence strongly supports the commission's core behavior: a change that leaves
a word problem's logic intact — renamed people, swapped numbers, or one added
true-but-irrelevant sentence — measurably lowers accuracy, and this is documented
across many models by the two anchor papers and corroborated by three independent
lines of work (a "how many sisters" template that swings from near-1 to near-0,
counterfactual task variants, and multiplication that decays to near zero as digits
grow). The settled part is firm: models condition on the whole surface string and
have no filter that reliably separates relevant from irrelevant tokens, so surface
form moves the answer. The contested part is what that implies about "reasoning,"
and here the evidence is genuinely two-sided. The single most-quoted number — the
"up to 65%" GSM-NoOp drop — is the weakest link: a 2026 re-analysis argues most of
those "irrelevant" clauses were actually ambiguous, and that when only unambiguous
distractors are kept the drop for frontier models falls to roughly zero. That
directly stresses the sharpest form of the commission's angle (that the added detail
is one "a reasoner would ignore"), so the writer must keep the clearly-irrelevant
perturbations (GSM-IC distractors, name/number swaps, the AIW template) separate from
the contested GSM-NoOp headline. Also thin: the GSM-Symbolic per-model table figures
below were read from the HTML rendering and should be treated as the paper's own
Table 1 values, not independently recomputed.

## Sources

```text
URL:         https://arxiv.org/abs/2302.00093
Kind:        primary — Shi, Chen, Misra, Scales, Dohan, Chi, Schärli, Zhou (Google
             DeepMind; Shi also TTI-Chicago, corresponding; Misra also Purdue) own
             the GSM-IC benchmark and the distraction measurements. ICML 2023.
Establishes: That adding one irrelevant sentence to a grade-school math problem the
             model otherwise solves lowers accuracy; that the effect is large under a
             strict "solve every variant" measure; and that instructions, exemplars,
             and self-consistency reduce but do not remove it.
Paraphrase:  GSM-IC is built from 100 GSM8K problems that at least one prompting
             method solved correctly, each rewritten with an added irrelevant
             sentence. On code-davinci-002 with chain-of-thought, per-problem (micro)
             accuracy is 72.4% against a 95.0% base on plain GSM8K, and the fraction
             of base problems solved correctly across ALL irrelevant-context variants
             (macro) is 6.0%. No more than 18% of solvable problems survive every type
             of irrelevant information. The best macro accuracy across all prompting
             techniques is only 45%. Self-consistency, an instruction to ignore
             irrelevant information, and exemplars that themselves contain irrelevant
             sentences each raise robustness (CoT macro rises from 6% to 30% with
             self-consistency).
Locators:    Abstract; Section 3 (GSM-IC construction, 100 base problems); Table 2
             (GSM8K baselines); Table 3 (GSM-IC micro/macro); Sections on instructions,
             exemplars, and self-consistency.
Quote:       "no more than 18% of them can be consistently solved for all types of
             irrelevant information"
```

```text
URL:         https://arxiv.org/abs/2410.05229
Kind:        primary — Mirzadeh, Alizadeh, Shahrokhi, Tuzel, Bengio, Farajtabar
             (Apple) own the GSM-Symbolic benchmark and every figure below. ICLR 2025
             (v1 Oct 7 2024; v2 Aug 27 2025).
Establishes: That regenerating the same GSM8K problems with different names/numbers
             produces a spread of accuracy per model rather than a stable score; that
             changing numbers hurts more than changing names; and that adding one
             topical-but-irrelevant clause (GSM-NoOp) drops accuracy sharply across
             all tested models.
Paraphrase:  More than 20 open models (2B–27B) plus GPT-4o-mini, GPT-4o, o1-mini, and
             o1-preview were evaluated (~25 models in Table 1). Regenerating names and
             numbers moves each model's accuracy across a distribution: the worst-to-
             best gap is more than 12% for Gemma2-9B and about 15% for Phi-3.5-mini.
             Changing only names causes noticeable variation; changing only numbers
             causes more; changing both is worst, and the original GSM8K score sits
             near the center of the changed-names distribution but not the
             changed-numbers one. Adding a single seemingly-relevant clause (GSM-NoOp)
             causes drops of up to 65% across all state-of-the-art models. The
             worked example: kiwis picked over three days, with an added clause that
             five were "a bit smaller than average," and models subtract the five.
Locators:    Abstract ("up to 65%"); Section 3.2 (model list); Section 4.1 and
             Figure 2 (name/number spread, worst-best gaps); Figure 4 (names-only vs
             numbers-only vs both); Section 4.4 and Figure 8a (GSM-NoOp, Phi-3-mini
             >65% drop); Table 1 / Appendix A.2 (per-model means and standard
             deviations).
Quote:       "Adding a single clause that seems relevant to the question causes
             significant performance drops (up to 65%) across all state-of-the-art
             models." / "We found no evidence of formal reasoning in language models."
```

```text
URL:         https://arxiv.org/abs/2406.02061
Kind:        primary — Nezhurina, Cipolina-Kun, Cherti, Jitsev (LAION; Juelich
             Supercomputing Center, Research Center Juelich) own the AIW problem and
             its measurements. NeurIPS 2024 SciDL workshop.
Establishes: That a trivially simple, unambiguous common-sense problem produces both
             low average accuracy and violent instability across cosmetic variations
             of the same template, in models that score high on hard benchmarks.
Paraphrase:  The AIW problem is "Alice has N brothers and M sisters; how many sisters
             does Alice's brother have?" with N, M and order varied. Across 15+ models
             (GPT-3.5, GPT-4, GPT-4o, Claude 3 Opus, Claude 3.5 Sonnet, Gemini, Llama
             2/3, Mistral, Mixtral, Command R+, Qwen and others) most score near zero;
             the strongest, including GPT-4o and Claude 3 Opus, sit only modestly above
             a 0.3 correct-response rate. Correct-response rate for a single model can
             fluctuate from near 1 to near 0 depending only on which N/M variation is
             used, though the variations do not change the problem's structure or
             difficulty. A harder variant (AIW+) collapses even GPT-4 and Claude 3 Opus
             toward zero.
Locators:    Abstract; Section 3.1; Figure 2 (mean correct-response rates); Figure 3
             (fluctuation across variations); AIW+ results.
Quote:       "correct response rates can fluctuate between being close to 1 all the way
             down to being close to 0, depending on AIW variation"
```

```text
URL:         https://aclanthology.org/2024.naacl-long.102/
Kind:        primary — Wu, Qiu, Ross, Akyürek, Chen, Wang, Kim, Andreas, Kim (MIT and
             collaborators) own the counterfactual-task framework and its results.
             NAACL 2024. (arXiv preprint 2307.02477, July 2023.)
Establishes: That the surface-form effect generalizes well beyond math: across many
             task types, models do worse on "counterfactual" variants that keep the
             task's logic but change a default assumption, evidence that some of the
             apparent skill is tied to the familiar default form.
Paraphrase:  Across a suite of 11 tasks the authors build counterfactual variants that
             deviate from a task's default assumptions (for example arithmetic in a
             non-base-10 system). Models show non-trivial but substantially and
             consistently lower accuracy on the counterfactual variants than on the
             default versions, which the authors read as reliance on narrow,
             non-transferable procedures alongside whatever general skill exists.
Locators:    Abstract; the 11-task suite; per-task default-vs-counterfactual
             comparisons.
Quote:       "Across a suite of 11 tasks, we observe nontrivial performance on the
             counterfactual variants, but nevertheless find that performance
             substantially and consistently degrades compared to the default
             conditions."
```

```text
URL:         https://arxiv.org/abs/2305.18654
Kind:        primary — Dziri, Lu, Sclar, X.L. Li, Jiang, Lin, West, Bhagavatula, Le
             Bras, Hwang, Sanyal, Welleck, Ren, Ettinger, Harchaoui, Choi own the
             compositionality experiments and the mechanism claim. NeurIPS 2023
             (Spotlight).
Establishes: A mechanism-level account that supports the "settled" side: transformers
             solve multi-step problems by matching linearized subgraphs seen in
             training rather than by executing a general procedure, so accuracy decays
             as a problem needs computation paths that were not in the training
             distribution.
Paraphrase:  On three compositional tasks (multi-digit multiplication, logic-grid
             puzzles, a dynamic-programming problem), zero-shot accuracy falls toward
             zero as complexity grows; off-the-shelf ChatGPT and GPT-4 reach only 55%
             and 59% on 3-digit-by-3-digit multiplication. Correctly predicted test
             cases are those whose full computation subgraph appeared often in training
             data. Even models finetuned with explicit scratchpads fail to generalize
             to out-of-distribution sizes.
Locators:    Abstract; Section 1 (55%/59% on 3x3 multiplication); Section 3.1 (limits
             with scratchpad training, Figure 5); Section 3.2.2 title and Figure 7
             (subgraph-frequency analysis).
Quote:       "transformer LLMs solve compositional tasks by reducing multi-step
             compositional reasoning into linearized subgraph matching, without
             necessarily developing systematic problem-solving skills"
```

```text
URL:         https://arxiv.org/abs/2110.14168
Kind:        primary — Cobbe, Kosaraju, Bavarian, Chen, Jun, Kaiser, Plappert, Tworek,
             Hilton, Nakano, Hesse, Schulman (OpenAI) own GSM8K, the dataset both
             anchor papers modify. Preprint Oct 2021.
Establishes: What GSM8K is: the shared substrate the whole behavior is measured on.
Paraphrase:  GSM8K is a dataset of 8,500 high-quality, linguistically diverse
             grade-school math word problems requiring multi-step reasoning, described
             as conceptually simple. The paper's own contribution is training verifiers
             to rank candidate solutions.
Locators:    Abstract; dataset description (8.5K problems).
Quote:       "8.5K high quality linguistically diverse grade school math word problems"
```

```text
URL:         https://appleinsider.com/articles/24/10/12/apples-study-proves-that-llm-based-ai-models-are-flawed-because-they-cannot-reason
Kind:        secondary — AppleInsider (Charles Martin, Oct 12 2024) reports on the
             GSM-Symbolic paper from outside the authoring party.
Establishes: How the finding was carried into public discussion: as proof that LLMs
             "cannot reason." Useful only to show the reception, not to source a number.
Paraphrase:  The article repeats the paper's "up to 65%" drop and the kiwi example, and
             frames the result as showing LLMs lack genuine reasoning and cannot be a
             foundation for reliable agents.
Locators:    Headline and body; kiwi example; "up to 65 percent."
Quote:       "We found no evidence of formal reasoning in language models" (quoting the
             paper) / a foundation on which "there is just no way you can build reliable
             agents."
```

```text
URL:         https://www.lesswrong.com/posts/Ze4C99Dasj74YKCFh/revisiting-gsm-symbolic-models-seem-to-reason-okay-actually
Kind:        secondary on GSM-Symbolic, but primary for its own re-analysis — author
             "Sturb" (June 5 2026) reruns the GSM-NoOp test and owns that new result.
             Non-peer-reviewed blog; treat its numbers as the author's claim.
Establishes: The strongest steelman of the "models do reason" side and the clearest
             contradiction of the sharpest reading of GSM-NoOp: that the drop reflects
             ambiguous distractors, not a reasoner ignoring an irrelevant detail.
Paraphrase:  The author has auditors classify the GSM-NoOp distractor clauses and finds
             only 117 of 945 (12.4%) are unambiguously irrelevant; the rest could
             plausibly bear on the answer (e.g. a clause about baskets "reviewed and
             confirmed as 2-pointers"). Re-running on the unfiltered set reproduces the
             original ~65%-scale drop, but on the 117 unambiguous distractors the
             accuracy loss is statistically indistinguishable from zero (0–2 points)
             for GPT-4o, Claude Opus 4.6, and Claude Haiku 4.5.
Locators:    Post body; the 117-of-945 filtering; the filtered-vs-unfiltered comparison.
Quote:       (paraphrased) filtered-set drops were "statistically indistinguishable from
             zero."
```

## Contradictions

- **The GSM-NoOp "up to 65%" drop versus the ambiguity re-analysis.** GSM-Symbolic
  (Mirzadeh et al.) reports up to a 65% drop from one added clause and reads it as
  absence of formal reasoning. The LessWrong re-analysis (Sturb, 2026) argues most of
  those clauses were not truly irrelevant, and that on the unambiguous subset the drop
  for 2026 frontier models is near zero. Both cannot be fully right about what the
  clause tests. This is the central contradiction and it bites the commission's angle
  precisely where the angle is sharpest ("a detail a reasoner would ignore"): the GSM-
  NoOp clauses are the least clearly irrelevant of the perturbations in this record.
  The GSM-IC distractors (Shi et al.) and the pure name/number swaps (GSM-Symbolic
  Figure 2/4) and the AIW template are not open to this objection, so the underlying
  behavior survives even if the 65% headline is contested.
- **Reasoning-tuned models resist the effect more.** Within GSM-Symbolic's own Table 1,
  o1-preview drops far less on GSM-NoOp (92.7% to 77.4%) than GPT-4o (94.9% to 63.1%)
  or Gemma2-9B (79.1% to 22.3%). The effect is real but not uniform, which cuts against
  any flat claim that "models" cannot handle irrelevant context and supports the "how
  much genuine computation sits on top" being the open question.
- **AIW's severity versus model generation.** AIW (mid-2024) shows GPT-4o and Claude 3
  Opus only modestly above a 0.3 correct-response rate on a trivial problem. Later
  models and the GSM-Symbolic re-analysis suggest frontier systems now handle many such
  cases; the record should present AIW as evidence the effect existed sharply in 2024
  models, not as a current ceiling.
- **Interpretation split, stated plainly.** Settled and uncontested: surface form
  (names, numbers, added tokens) changes the output, because the model conditions on
  all tokens and has no reliable relevance filter (GSM-IC, GSM-Symbolic name/number
  spread, Faith and Fate, Reasoning or Reciting). Contested: whether this means "no
  formal reasoning" (Mirzadeh et al.; AppleInsider framing) or reflects a mix of real
  procedure plus ambiguity and narrow shortcuts (Sturb re-analysis; Wu et al.'s
  "to an extent"). Keep these two apart.

## Numbers

```text
Figure: GSM8K size = 8,500 grade-school word problems
Owner:  Cobbe et al. 2021 (GSM8K)
Scope:  full dataset (7.5K train / 1K test in the paper)
```

```text
Figure: code-davinci-002 CoT — 95.0% base GSM8K -> 72.4% micro on GSM-IC
Owner:  Shi et al. 2023 (GSM-IC), Tables 2 and 3
Scope:  micro = per-problem average over GSM-IC-4K; base = plain GSM8K, greedy decoding.
        ~22.6 percentage-point drop from adding one irrelevant sentence, per problem.
```

```text
Figure: code-davinci-002 CoT — 95.0% base -> 6.0% macro on GSM-IC
Owner:  Shi et al. 2023 (GSM-IC), Table 3
Scope:  macro = fraction of base problems solved across EVERY irrelevant-context
        variant. The strict measure; "no more than 18%" survive all variant types;
        best macro across all prompting methods is 45%.
```

```text
Figure: CoT macro robustness 6% -> 30% with self-consistency
Owner:  Shi et al. 2023 (GSM-IC)
Scope:  same 100 base problems; shows the effect is reducible, not removable.
```

```text
Figure: GSM-NoOp drop "up to 65%" across all SOTA models; Phi-3-mini > 65%
Owner:  Mirzadeh et al. 2024 (GSM-Symbolic), Abstract and Figure 8a
Scope:  one added topical-but-irrelevant clause vs GSM-Symbolic baseline; ~25 models.
        Contested: see Contradictions (ambiguity re-analysis).
```

```text
Figure: GSM-NoOp per model — GPT-4o 94.9% -> 63.1% (±4.53); Gemma2-9B 79.1% -> 22.3%
        (±5.11); o1-preview 92.7% -> 77.4% (±3.84)
Owner:  Mirzadeh et al. 2024 (GSM-Symbolic), Table 1 / Appendix A.2 (HTML reading)
Scope:  standard deviations are across regenerated versions; reasoning model resists more.
```

```text
Figure: name/number regeneration spread — worst-to-best gap > 12% (Gemma2-9B),
        ~15% (Phi-3.5-mini); numbers-only hurts more than names-only
Owner:  Mirzadeh et al. 2024 (GSM-Symbolic), Section 4.1, Figures 2 and 4
Scope:  same problems, only names/numbers changed; logic identical.
```

```text
Figure: AIW correct-response rate — best models (GPT-4o, Claude 3 Opus) ~just above
        0.3; most models near 0; single-model fluctuation near 1 down to near 0
Owner:  Nezhurina et al. 2024 (AIW), Figures 2 and 3
Scope:  "Alice has N brothers and M sisters" template, N/M and order varied; 15+ models.
```

```text
Figure: 3x3-digit multiplication — ChatGPT 55%, GPT-4 59%; accuracy -> near zero as
        digit count grows
Owner:  Dziri et al. 2023 (Faith and Fate), Section 1 and Figure 2
Scope:  off-the-shelf, zero-shot; decay with problem size, even with scratchpad training.
```

```text
Figure: counterfactual re-analysis of GSM-NoOp — 117 of 945 clauses (12.4%)
        unambiguously irrelevant; filtered-set drop 0-2 points (indistinguishable
        from zero) for GPT-4o, Claude Opus 4.6, Claude Haiku 4.5
Owner:  Sturb 2026 (LessWrong re-analysis)
Scope:  author's own rerun; non-peer-reviewed; unfiltered set still shows ~65%-scale drop.
```

## Source assets

```text
Asset: GSM-Symbolic Figure 2 — per-model accuracy distribution over regenerated
       name/number versions, with the plain-GSM8K score marked against the spread.
Shows: that a single "GSM8K score" hides a band of outcomes for the same logic; the
       reader sees the spread, not a point.
Crop:  keep the axis labels and the marked original-GSM8K line; a crop to two or three
       named models is fine, but must retain the spread width for each.
```

```text
Asset: GSM-Symbolic Figure 8a — GSM-NoOp accuracy drop per model.
Shows: the size and unevenness of the added-clause effect, including that reasoning-
       tuned models fall less.
Crop:  must retain both the baseline and NoOp bars per model, and label which is which;
       do not crop to only the largest drop.
```

```text
Asset: GSM-Symbolic kiwi example (worked prompt and the wrong model completion, text).
Shows: concretely how one irrelevant clause ("five were smaller than average") pulls a
       subtraction the problem never asked for.
Crop:  quote the clause and the erroneous step; the commission bars a headline that
       quotes a prompt and its wrong result, so this belongs in the body, not the head.
```

```text
Asset: AIW Figure 3 — correct-response rate per AIW variation for a single model.
Shows: that the same trivial problem swings from near-1 to near-0 on cosmetic changes.
Crop:  keep the full 0-to-1 vertical range so the swing is not visually compressed.
```

```text
Asset: GSM-IC Table 3 (micro vs macro accuracy by prompting method).
Shows: the gap between "usually right" (micro) and "right on every variant" (macro),
       which is the honest way to state the drop.
Crop:  keep both micro and macro columns together; showing one without the other
       misleads.
```

## Discarded

```text
URL: https://circleid.com/posts/apples-new-benchmark-gsm-symbolic-highlights-ai-reasoning-flaws
     Same origin as the AppleInsider retelling (the Apple paper); a second retelling of
     one origin counts as one, so it adds no independent confirmation.
```

```text
URL: https://medium.com/@sharakusatoh/apple-is-wrong-llm-has-reasoning-ability-8feb3db0af8e
     Opinion post rebutting the Apple paper; the LessWrong re-analysis makes the same
     "models reason" case with an actual rerun and audited data, so this is redundant
     and weaker.
```

```text
URL: https://techxplore.com/news/2024-07-ai-reveals-breakdown-large-language.html
     Press release retelling of the AIW paper; the primary (2406.02061) owns every
     number, so the retelling adds nothing citable.
```

```text
URL: https://arxiv.org/pdf/2511.11810 ("On the Notion that Language Models Reason")
     Not opened in full; the settled/open interpretation is already carried by the
     primaries plus the Sturb re-analysis, so this would be padding rather than a
     source that changes the reading.
```

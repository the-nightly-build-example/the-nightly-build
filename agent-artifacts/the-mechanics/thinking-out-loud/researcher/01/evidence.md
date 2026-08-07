# evidence: the-mechanics/thinking-out-loud (01)

The evidence strongly supports the commissioned mechanism. The behavior is
documented: chain-of-thought prompting lifts a large model's math-word-problem
accuracy several-fold (PaLM 540B on GSM8K, 17.9% to 56.9%), and a reasoning
model's measured accuracy climbs as its "thinking" traces lengthen during
training (DeepSeek-R1-Zero on AIME 2024, 15.6% to 71.0% pass@1). The cause is
settled at the level the commission needs: three independent theory primaries
(Feng et al. 2023; Merrill & Sabharwal 2023; Li et al. 2024), all resting on
the foundational result that a fixed transformer answering immediately is a
constant-depth circuit (Merrill, Sabharwal & Smith 2022, TC0), prove that such
a model does a bounded amount of computation per emitted token, so serial
reasoning of length T provably requires emitting on the order of T intermediate
tokens the model reads back. Where the evidence is thin is exactly where the
commission wants it left open: whether the printed steps ARE that computation or
a fluent story told beside it. Here the record is genuinely mixed. Turpin et al.
2023 and Lanham et al. 2023 show verbalized CoT can be unfaithful and that
faithfulness often falls as models scale; Pfau et al. 2024 and Lanham disagree
on whether meaningless filler tokens can substitute for real steps. The
strongest caveat, stated by the theorists themselves, is that a proof that
tokens CAN buy computation is not evidence that a given trained model's printed
chain is the computation it used. The evidence does not undermine the angle; it
confirms the settled mechanism and substantiates the deliberate open question.

## Sources

```text
URL:         https://arxiv.org/abs/2201.11903
Kind:        primary — the paper owns the chain-of-thought prompting finding
             (Wei et al., Google Research). The-evidence/chain-of-thought owns
             this as a document; here it establishes the behavior only.
Establishes: That prompting a large model with a few worked examples that show
             intermediate steps sharply raises accuracy on multi-step reasoning,
             and that this benefit is an emergent ability of model scale, absent
             or harmful below roughly 100B parameters.
Paraphrase:  Eight chain-of-thought exemplars given to PaLM 540B set state of
             the art on GSM8K, beating a fine-tuned GPT-3 with a verifier. On
             GSM8K, standard prompting scored 17.9% and chain-of-thought 56.9%
             for PaLM 540B; LaMDA 137B went 6.5% to 14.3%; GPT-3 175B went
             15.6% to 46.9% (Table 2, appendix). The gains appear only at large
             scale; small models wrote fluent but illogical chains and did worse
             than standard prompting.
Locators:    Abstract; Section 3 (Results) and Figure 4 (arithmetic scaling
             curves); Table 2 in the appendix for GSM8K solve rates.
Quote:       "chain-of-thought prompting is an emergent ability of model
             scale—it does not positively impact performance until used with a
             model of sufficient scale."
```

```text
URL:         https://arxiv.org/abs/2106.16213
Kind:        primary — Merrill, Sabharwal & Smith (TACL 2022) own this circuit-
             complexity result about transformers.
Establishes: The architectural ground under the whole lesson: a transformer
             (saturated attention, bounded precision) computing one output does
             work no deeper than a constant-depth threshold circuit (class TC0).
             This is the formal content of "bounded, fixed computation per
             token."
Paraphrase:  Saturated transformers with floating-point values can be simulated
             by constant-depth threshold circuits, placing an upper bound of TC0
             on the languages a single forward pass can recognize. Depth does
             not grow with input length, so per-token computation is bounded.
Locators:    Abstract; main theorem (saturated transformers ⊆ TC0).
```

```text
URL:         https://arxiv.org/abs/2305.15408
Kind:        primary — Feng et al. (NeurIPS 2023) own this theory-of-CoT result.
             Referred to in coverage as the "Peking University" work.
Establishes: The impossibility/possibility pair. A bounded-depth transformer
             provably cannot output correct answers to basic arithmetic and
             linear-equation tasks unless its size grows super-polynomially in
             the input length; a constant-size transformer that is allowed to
             GENERATE a chain-of-thought derivation can solve the same tasks,
             and a general class of dynamic-programming problems.
Paraphrase:  Using circuit complexity, direct (no-CoT) bounded-depth
             transformers are shown unable to solve elementary arithmetic and
             equation solving at feasible size; autoregressive transformers of
             constant size suffice once they emit step-by-step derivations. The
             extra tokens are where the missing computation happens.
Locators:    Abstract; impossibility theorems for arithmetic/equation solving;
             constructive CoT results; dynamic-programming section.
```

```text
URL:         https://arxiv.org/abs/2310.07923
Kind:        primary — Merrill & Sabharwal (ICLR 2024) own this exact
             characterization of transformers-with-CoT by decoding-step count.
Establishes: That the NUMBER of generated intermediate tokens is the dial on
             computational power. Immediate-answer transformers cannot solve
             graph connectivity or simulate a finite-state machine; adding
             intermediate decoding steps buys graded new power.
Paraphrase:  With a logarithmic number of decoding steps a transformer gains
             little; with a linear number (under standard conjectures) it can
             recognize all regular languages, including finite-state-machine
             simulation it could not do immediately; with a polynomial number it
             recognizes exactly the polynomial-time-solvable problems (P). Chain
             length maps onto a spectrum of complexity classes.
Locators:    Abstract; theorems for logarithmic, linear, and polynomial steps.
```

```text
URL:         https://arxiv.org/abs/2402.12875
Kind:        primary — Li, Liu, Zhou & Ma (ICML 2024) own this "inherently
             serial" result.
Establishes: The plainest statement of the mechanism: CoT supplies serial
             computation that a shallow transformer structurally lacks.
Paraphrase:  Constant-depth, constant-precision transformers without CoT are
             confined to a low parallel class (a subset of TC0); with T steps of
             chain-of-thought they can compute anything a boolean circuit of size
             T can, so a linear or polynomial number of steps unlocks inherently
             serial problems. Without CoT the count of serial operations is
             capped by the fixed depth; each generated token adds one serial
             step.
Locators:    Abstract; main expressivity theorem; discussion of serial vs
             parallel computation.
Quote:       "CoT empowers the model with the ability to perform inherently
             serial computation, which is otherwise lacking in transformers,
             especially when depth is low."
```

```text
URL:         https://arxiv.org/abs/2501.12948
Kind:        primary — DeepSeek-AI own these measurements of their own model.
Establishes: The reasoning-model half of the behavior: accuracy rises as the
             model learns to spend more "thinking" tokens.
Paraphrase:  DeepSeek-R1-Zero, trained by reinforcement learning with no
             supervised warm-up, improved AIME 2024 pass@1 from 15.6% to 71.0%
             over training, and to 86.7% with majority voting (cons@64),
             matching OpenAI o1. Its average response length (thinking time)
             grew steadily across training, and it spontaneously learned to
             re-evaluate its approach and allocate more thinking to hard
             problems (the "aha moment"). The released DeepSeek-R1 reached 79.8%
             pass@1 on AIME 2024.
Locators:    Section 2.2 (R1-Zero results); Figure 2 (AIME accuracy vs training
             step); Figure 3 (average response length vs training step); the
             "aha moment" subsection.
```

```text
URL:         https://arxiv.org/abs/2305.04388
Kind:        primary — Turpin, Michael, Perez & Bowman own this faithfulness
             experiment.
Establishes: That a model's stated chain-of-thought can misrepresent the real
             cause of its answer. This is direct evidence for the open question.
Paraphrase:  Inserting a biasing feature into the prompt (e.g., reordering
             few-shot multiple-choice options so the answer is always "(A)")
             swings the model's answer, yet the generated CoT rationalizes the
             new answer without ever mentioning the bias. Across 13 BIG-Bench
             Hard tasks this dropped accuracy by as much as 36% on GPT-3.5 and
             Claude 1.0.
Locators:    Abstract; Section 3 (bias interventions); results across 13 BBH
             tasks.
Quote:       "CoT explanations can be heavily influenced by adding biasing
             features to model inputs ... which models systematically fail to
             mention in their explanations."
```

```text
URL:         https://arxiv.org/abs/2307.13702
Kind:        primary — Lanham et al. (Anthropic) own these faithfulness
             measurements.
Establishes: That whether the printed CoT drives the answer varies by task, and
             that faithfulness tends to FALL as models get larger. Central to
             the open question.
Paraphrase:  Four interventions probe faithfulness. Early answering (truncate
             the CoT and force an answer) and adding mistakes reveal wide
             variation: on some tasks the answer barely changes without the full
             chain (post-hoc, unfaithful reasoning), on harder logic tasks
             (AQuA, LogiQA) it changes a lot (more faithful). Paraphrasing the
             CoT leaves accuracy essentially unchanged, so the chain is not
             smuggling information through exact wording. Replacing the CoT with
             filler "..." tokens produced no accuracy gain. Across models from
             13B to 175B, larger models produced LESS faithful reasoning on most
             tasks studied.
Locators:    Sections on Early Answering, Adding Mistakes, Paraphrasing, Filler
             Tokens; the model-size / inverse-scaling discussion.
Quote:       "As models become larger and more capable, they produce less
             faithful reasoning on most tasks we study."
```

```text
URL:         https://arxiv.org/abs/2404.15758
Kind:        primary — Pfau, Merrill & Bowman own this filler-token result.
Establishes: The "just more compute" side of the contradiction: on constructed
             tasks, meaningless tokens can carry hidden computation.
Paraphrase:  Transformers can be trained to use meaningless filler tokens
             ("......") in place of a chain-of-thought and thereby solve two hard
             algorithmic tasks they cannot solve answering immediately, showing
             the benefit of extra tokens can be computation independent of the
             tokens' content. But learning to use filler tokens is hard and
             needs specific dense supervision; it does not arise in off-the-shelf
             models. They characterize the problems where filler helps by the
             quantifier depth of a first-order formula.
Locators:    Abstract; task construction and accuracy comparisons; supervision
             caveat; theoretical characterization.
```

```text
URL:         https://arxiv.org/abs/2409.12183
Kind:        primary — Sprague et al. (ICLR 2025) own this meta-analysis and its
             new evaluations.
Establishes: The scope limit on the behavior: CoT does not help everywhere. It
             is a counter-weight to any overreach in the angle.
Paraphrase:  A meta-analysis over 100+ papers plus fresh evaluations on 20
             datasets across 14 models finds CoT's gains concentrated on math and
             symbolic/logic tasks and small elsewhere. On MMLU, generating the
             answer directly matches CoT accuracy unless the question or response
             contains an equals sign, i.e., unless symbolic computation is
             involved. Much of CoT's benefit is symbolic execution, which a real
             symbolic solver still beats.
Locators:    Abstract; meta-analysis; MMLU "equals sign" analysis.
```

```text
URL:         https://arxiv.org/abs/2305.18654
Kind:        primary — Dziri et al. (NeurIPS 2023) own these compositionality
             measurements.
Establishes: The concrete worked example the brief asks for, and its ceiling.
             Multi-digit multiplication is a multi-step problem a fluent model
             gets wrong when it answers in one shot.
Paraphrase:  On 3-digit by 3-digit multiplication, GPT-3.5 scored about 55% and
             GPT-4 about 59% answering directly, and accuracy falls toward zero
             as the digit count grows. Giving the model a scratchpad to write
             intermediate steps restores near-perfect accuracy in-distribution
             but does not fix generalization to larger (out-of-distribution)
             problems. Worked example for the writer (prose only, no code):
             ask a model to compute a product such as 837 x 649 in one step and
             it typically errs; have it write the partial products and add them
             (837 x 9, 837 x 40, 837 x 600, then sum) and it succeeds — each
             written line is one bounded step of serial computation the single
             answer token could not hold. GSM8K word problems (Wei et al.) are
             the same phenomenon on everyday arithmetic.
Locators:    Multiplication section and its accuracy tables/figures; scratchpad
             / OOD-generalization discussion.
Quote:       Performance "deteriorates significantly from near perfection to zero
             with increasing complexity."
```

```text
URL:         https://www.quantamagazine.org/how-chain-of-thought-reasoning-helps-neural-networks-compute-20240321/
Kind:        secondary — Quanta Magazine (Ben Brubaker, March 21, 2024) reports
             on the theory primaries above; it authors none of the results.
Establishes: A durable plain-language framing of the compute view, and an
             on-record statement of the theory's own limit. Useful for phrasing,
             not as a source of fact.
Paraphrase:  Reports that a transformer asked for an immediate answer is
             computationally weak, and that chain-of-thought lets it reuse
             intermediate results on later passes, evading the limits of
             parallel computation. Attributes the linear/step characterization to
             Merrill & Sabharwal (Oct 2023) and the impossible-math result to the
             Peking University team (Feng et al., May 2023). Notes the caveat that
             positive expressivity proofs do not imply a trained model actually
             learns or uses those solutions.
Locators:    Body of the article; quotations of the researchers.
Quote:       "Transformers are quite weak if the way you use them is you give an
             input, and you just expect an immediate answer."
```

## Contradictions

- Compute vs latent reasoning, unresolved between two primaries. Pfau et al.
  2024 show meaningless filler tokens CAN replace a chain-of-thought on
  constructed tasks, arguing the gain is extra computation independent of token
  content. Lanham et al. 2023 tested filler tokens on real models and found no
  accuracy gain. Reconciliation: Pfau's models were trained from scratch with
  dense supervision specifically to use filler; deployed LLMs were not, so in
  practice their extra computation currently rides on meaningful (if sometimes
  unfaithful) text. The article must not claim real models get free compute from
  arbitrary filler; the clean "tokens = compute" statement belongs to the theory
  and to purpose-trained models.

- "CoT always helps" is false. Wei et al. 2022 find CoT HURTS sub-~100B models
  (fluent but illogical chains). Sprague et al. 2024 find the benefit is largely
  confined to math and symbolic tasks and is small on general knowledge
  benchmarks like MMLU. The mechanism explains WHY it helps where the task needs
  serial computation; it also predicts little help where it does not.

- Writing steps is not a universal fix. Dziri et al. 2023 show a scratchpad
  restores multiplication accuracy only within the training distribution and
  fails to generalize to larger problems, and they argue the autoregressive
  form itself is a limit that step-by-step prompting cannot remove. So "more
  tokens buy more compute" has bounds: the compute is real, but it does not
  confer systematic generalization on its own.

- Faithfulness cuts against the folk story, not against the mechanism. Turpin
  and Lanham show the printed steps can fail to reflect the true cause, and that
  faithfulness can worsen with scale. This is the commissioned open question and
  should be presented as unresolved, not as a refutation of the compute account.

- Theory-to-practice gap (Quanta, quoting the theorists): a proof that a
  transformer with T steps CAN express a computation does not show a trained
  model learns or uses that computation. This is the deepest limit on any claim
  that the printed chain IS the computation.

## Numbers

```text
Figure: 17.9% -> 56.9%
Owner:  Wei et al. 2022 (2201.11903), Table 2
Scope:  GSM8K test set, PaLM 540B, standard prompting vs 8-shot chain-of-thought
```

```text
Figure: 6.5% -> 14.3%
Owner:  Wei et al. 2022 (2201.11903), Table 2
Scope:  GSM8K test set, LaMDA 137B, standard vs chain-of-thought prompting
```

```text
Figure: 15.6% -> 46.9%
Owner:  Wei et al. 2022 (2201.11903), Table 2
Scope:  GSM8K test set, GPT-3 175B, standard vs chain-of-thought (lower
        confidence than the PaLM/LaMDA rows; verify against Table 2 if quoted)
```

```text
Figure: 15.6% -> 71.0% pass@1 (86.7% with cons@64 majority voting)
Owner:  DeepSeek-AI 2025 (2501.12948), Section 2.2 / Figure 2
Scope:  AIME 2024, DeepSeek-R1-Zero, start of RL training vs after RL training
```

```text
Figure: 79.8% pass@1
Owner:  DeepSeek-AI 2025 (2501.12948)
Scope:  AIME 2024, released DeepSeek-R1 (post cold-start + multi-stage RL)
```

```text
Figure: 3-digit x 3-digit multiplication, direct answer: ~55% (GPT-3.5),
        ~59% (GPT-4); falls toward 0% as digits grow
Owner:  Dziri et al. 2023 (2305.18654)
Scope:  Single-shot multiplication accuracy vs number of digits; scratchpad
        restores in-distribution accuracy but not OOD generalization
```

```text
Figure: accuracy drop of as much as 36%
Owner:  Turpin et al. 2023 (2305.04388)
Scope:  13 BIG-Bench Hard tasks, GPT-3.5 and Claude 1.0, under the "always (A)"
        and similar biasing interventions
```

```text
Figure: faithfulness decreases from 13B to 175B on most tasks (direction, not a
        single scalar)
Owner:  Lanham et al. 2023 (2307.13702)
Scope:  Anthropic model family 13B–175B, across AQuA, LogiQA, MMLU, TruthfulQA
        and other tasks
```

```text
Figure: ~100B parameters (order-of-magnitude emergence threshold)
Owner:  Wei et al. 2022 (2201.11903), Figure 4 scaling curves
Scope:  Point below which CoT gives no gain or hurts; not a sharp constant.
        PaLM steps tested: 8B, 62B, 540B.
```

## Source assets

```text
Asset: Wei et al. 2022, Figure 4 — solve-rate vs model scale curves for GSM8K
       and other benchmarks, standard prompting vs chain-of-thought.
Shows: The emergence visually: the two lines sit together at small scale and
       fan apart above roughly 100B, so CoT's benefit appearing only at scale is
       readable at a glance.
Crop:  Keep both series labeled and the x-axis parameter counts; keep the
       divergence point visible. A single-benchmark panel (GSM8K) is enough; do
       not crop away the small-model region where the lines coincide.
```

```text
Asset: DeepSeek-AI 2025, Figure 2 — AIME 2024 pass@1 of R1-Zero vs RL training
       step, and Figure 3 — average response length vs training step.
Shows: The two curves rising together make the lesson's claim concrete: as the
       model learns to emit longer thinking traces, accuracy climbs.
Crop:  If both are shown, keep the shared x-axis (training steps) so the reader
       can see accuracy and length move together. Retain axis labels and the
       pass@1 unit.
```

```text
Asset: Turpin et al. 2023 — the "always (A)" biased-prompt illustration and the
       per-task accuracy-drop bars across the 13 BBH tasks.
Shows: How a hidden bias flips answers while the CoT never names it; the bar
       chart shows the effect is broad, not one cherry-picked task.
Crop:  Keep task labels and the unbiased-vs-biased comparison; do not crop to a
       single most-extreme task.
```

```text
Asset: Dziri et al. 2023 — multiplication accuracy plotted against the number
       of digits (the collapse toward 0%).
Shows: The worked example made visual: a fluent model's single-shot accuracy
       falling off a cliff as a problem needs more serial steps than one token
       can hold.
Crop:  Keep the digit-count axis and the accuracy axis with its 0% floor; a
       clean two-line panel (with vs without scratchpad, if shown together) is
       ideal. Do not crop away the largest-problem region where accuracy hits 0.
```

```text
Asset: Theory primaries (Feng 2023; Merrill & Sabharwal 2023; Li 2024).
Shows: None found. Their figures are proof schematics and complexity-class
       diagrams, not reader-facing evidence; the argument is carried better in
       prose than by reproducing a circuit diagram.
Crop:  n/a
```

## Discarded

```text
URL: https://arxiv.org/abs/2308.03212 (Average-Hard Attention Transformers are
     Constant-Depth Uniform Threshold Circuits) — tighter TC0 refinement; the
     2106.16213 result already grounds "bounded compute per token" for a lay
     lesson, and adding this would deepen the circuit-complexity thicket without
     changing the claim.
```

```text
URL: https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/
     — relevant to faithfulness but secondary and overlapping with Turpin and
     Lanham, which own the claim firsthand; held in reserve only if a plain-
     language faithfulness quote is needed.
```

```text
URL: https://medium.com/@tang.xuning/why-does-chain-of-thought-make-a-transformer-more-powerful-...
     — a personal blog restating the theory papers; the Quanta piece is the more
     durable, editorially reviewed secondary, so this adds nothing.
```

```text
URL: https://openreview.net/pdf?id=_VjQlMeSB_J — the OpenReview copy of Wei et
     al. 2022; same content as the arXiv page recorded above, which is the
     canonical resolvable home.
```

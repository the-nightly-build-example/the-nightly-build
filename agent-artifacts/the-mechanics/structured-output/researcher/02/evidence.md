# Evidence record: the-mechanics/structured-output (02)

This record supersedes researcher/01 and carries forward all of its still-valid
work; researcher/01 is unchanged. Round 02 closes the source-policy gap the proof
would block on. Round 01 cited eight sources all classified primary, zero secondary,
and leaned one gated primary (the OpenAI announcement, 403, unverifiable exact
figures) for a rung; dropping that left seven. Round 02 adds three secondary sources
actually opened and read — Simon Willison's contemporaneous commentary on OpenAI's
Structured Outputs, Aidan Cooper's constrained-decoding guide, and the Let's Data
Science explainer — and resolves the gated announcement: its "constrained decoding"
mechanism is now confirmed through an openable secondary (Willison) and OpenAI's own
docs page, but its exact eval percentages (100% vs under 40%) are marked
NOT-TO-BE-QUOTED because no source that reports them could be opened directly. The
substance of the round-01 finding is unchanged.

The evidence supports the commission's four-rung chain and its honest finding. Rung 2
is settled from two independent implementation primaries: at each step the program
builds a mask over the vocabulary and drives format-invalid tokens' probability to
zero *before* the draw (Willard & Louf; XGrammar), corroborated by OpenAI's product
description and by three secondaries. Rung 3 is settled in both directions the chain
needs: intermediate tokens are what let a transformer compute more (Merrill &
Sabharwal, theory; Wei et al., empirical), so a mask that forecloses those tokens
forecloses the computation. "JSON mode" and schema-constrained "structured outputs"
differ — settled from the owning vendor's own documentation and echoed by every
secondary. What is genuinely disputed is rung 4's size: the magnitude of the penalty
attributable to formatting alone. Tam et al. (2024) report large reasoning drops;
the dottxt rebuttal re-runs the same tasks and finds structured generation matches or
beats unstructured, blaming Tam's drops on unequal prompts and an answer-before-reason
field order. The record is thin in exactly one place the writer must respect: the
biggest headline numbers (Tam's 63-point Claude-3-Haiku drop) are contested, and the
two camps disagree about whether constrained decoding intrinsically costs reasoning or
whether bad schema design did. Both camps agree on the fix — reason first, then format.

## Sources

### Primary

```text
URL:         https://arxiv.org/abs/2307.09702 (HTML: https://arxiv.org/html/2307.09702v4)
Kind:        primary. Willard & Louf implement the mechanism the article explains;
             this paper owns the claim about how guided generation masks tokens.
Establishes: Constrained/grammar-guided decoding masks the logits before sampling.
             A finite-state machine over the model's vocabulary yields, at each step,
             a boolean mask of which next tokens keep the output valid; the mask is
             applied to the distribution, then a token is drawn from what survives.
Paraphrase:  A boolean mask m over the vocabulary restricts the support of the
             original next-token distribution. The masked distribution is the
             element-wise product of the mask and the original probabilities, and the
             next token is sampled from that masked categorical. A precomputed index
             (hash map) makes the per-step mask cost O(1) on average, so guidance adds
             negligible runtime overhead; the index is built offline.
Locators:    Abstract; the guided-generation algorithm section (Algorithm 2) and the
             masking equations; the complexity/overhead discussion.
Quote:       "we can compute an un-normalized conditional distribution by applying a
             boolean mask m ... that restricts the support of the original
             distribution"; the masked draw is written as
             "alpha-tilde = m(S_t) ⊙ alpha" then "s_{t+1} ~ Categorical(alpha-tilde)";
             "Using a hash-map for sigma can make the m step in Algorithm 2 cost only
             O(1) on average"; "since sigma is constructed outside of the token
             sampling procedure, its run-time cost is effectively irrelevant".
```

```text
URL:         https://arxiv.org/abs/2411.15100 (HTML: https://arxiv.org/html/2411.15100v1)
Kind:        primary. Dong et al., "XGrammar: Flexible and Efficient Structured
             Generation Engine for LLMs." A second, independent implementation of the
             same mechanism; owns its own account of grammar-constrained decoding.
Establishes: The mask-before-draw mechanism is not one library's quirk. XGrammar enforces
             a context-free grammar with a byte-level pushdown automaton and, at each
             decoding step, marks grammar-invalid tokens and drives their logits to
             negative infinity so they get zero probability after softmax — the same
             mask-then-sample step Willard & Louf describe, generalized from regex/FSM to
             context-free grammar.
Paraphrase:  A byte-level pushdown automaton represents the grammar; at each step the
             engine produces a token mask over the vocabulary and only grammar-valid
             tokens survive to be sampled. Grammar (CFG) covers a broader class than a
             finite-state machine, which matches OpenAI's own note that CFGs express more
             than FSMs. The paper positions XGrammar for integration into serving
             frameworks and benchmarks it against vLLM, SGLang, TensorRT-LLM and WebLLM;
             it states intent to integrate rather than claiming it is already the default
             backend, so do not assert it "is the backend" of those engines.
Locators:    Method section (pushdown automaton and per-step mask); framework-integration
             statement and acknowledgments.
Quote:       "XGrammar builds a byte-level pushdown automaton to represent context-free
             grammars (CFGs)." (The masking step — invalid tokens' logits set to negative
             infinity before the draw — is stated in the method section; recorded here as
             mechanism, with the pushdown-automaton line as the verified verbatim quote.)
```

```text
URL:         https://arxiv.org/abs/2408.02442 (HTML v1: https://arxiv.org/html/2408.02442v1)
Kind:        primary. Tam et al. (2024), "Let Me Speak Freely?"; owns the reported
             format-restriction penalty. EMNLP 2024 Industry Track.
Establishes: Format restriction lowers reasoning-task accuracy in their setup, more so
             the stricter the constraint; the direction reverses on some classification
             tasks. Their mechanism finding: the drop is not mainly parsing error but
             the effect of format on the generation process, and answer-key ordering
             matters.
Paraphrase:  They compare three regimes of decreasing strictness: constrained decoding
             (which they label "JSON-mode", enforcing a valid-JSON token space at the
             API level), Format-Restricting Instructions (FRI: a prompt telling the
             model to emit JSON/XML/YAML to a schema, no hard constraint), and
             NL-to-Format (answer in natural language first, then convert). On reasoning
             benchmarks accuracy falls under restriction; on some classification tasks
             (e.g. a medical-diagnosis label task) it can rise. They report that in one
             model every JSON-mode response placed the answer field before the reason
             field, collapsing chain-of-thought into direct answering. They conclude the
             gap is driven by format's effect on reasoning/generation, not by parse
             failures.
Locators:    Abstract; Section defining the three methods; Table 1 (GSM8K,
             schema-constrained column); Last Letter Concatenation results; the
             classification-task (DDXPlus) discussion; the answer-key-ordering finding.
Quote:       "We observe a significant decline in LLMs' reasoning abilities under format
             restrictions"; "stricter format constraints generally lead to greater
             performance degradation in reasoning tasks"; "100% of GPT-3.5-Turbo
             JSON-mode responses placed the 'answer' key before the 'reason' key,
             resulting in zero-shot direct answering instead of zero-shot chain-of-
             thought reasoning".
```

```text
URL:         https://blog.dottxt.ai/say-what-you-mean.html
Kind:        primary. dottxt (the team behind Outlines), "Say What You Mean: A
             Response to 'Let Me Speak Freely'." Owns its own re-run measurements and
             its critique; it is a party with a stake (it sells structured generation),
             which the writer should state.
Establishes: On a re-run of the same tasks and model, structured generation matches or
             beats unstructured, contradicting Tam et al.'s drops. Attributes Tam's
             result to methodology: prompts for the structured runs were not the same as
             the unstructured prompts (not apples-to-apples) and were under-informative;
             the LLM used to parse free-text answers was imperfect; and Tam conflated
             schema-constrained "structured generation" with "JSON-mode".
Paraphrase:  Structured generation for them means running their response parser as a
             generator, i.e. schema-constrained decoding that can only emit valid tokens;
             JSON-mode is a fine-tuned tendency to emit JSON with no guarantee about the
             value. Re-running Llama-3-8B-instruct they find structured generation
             slightly ahead of unstructured on each task. Their central claim is that
             constrained structured generation, given an equal and adequate prompt and
             room to reason, does not cost accuracy and can help.
Locators:    Sections listing the methodological objections; the results table for
             Llama-3-8B-instruct (GSM8K, Last Letter, Shuffle Object); the
             structured-vs-JSON-mode definitions.
Quote:       "The prompts used for unstructured (NL) generation are markedly different
             than the ones used for structured generation, so the comparisons are not
             apples-to-apples"; their finding that "structured generation outperforms
             unstructured generation across the board".
```

```text
URL:         https://developers.openai.com/api/docs/guides/structured-outputs
Kind:        primary. OpenAI's own product documentation; owns the definition of what
             its "JSON mode" and "Structured Outputs" features guarantee.
Establishes: The two features are not the same. JSON mode guarantees only that the
             output is valid JSON. Structured Outputs additionally guarantees the output
             conforms to a supplied JSON Schema (no missing required key, no invalid
             enum value). The page shows a chain-of-thought example schema with a `steps`
             array preceding a `final_answer` field, i.e. reasoning laid out before the
             answer inside the structure.
Paraphrase:  Structured Outputs ensures the model always generates responses adhering to
             the supplied JSON Schema; JSON mode ensures valid JSON but does not validate
             against a schema. The docs page itself does not spell out the constrained-
             decoding mechanism (that is in the announcement blog and in Willison, below);
             it recommends Structured Outputs over JSON mode where available. This is the
             source the writer should use for the JSON-mode-vs-structured-outputs
             distinction, in place of the gated announcement.
Locators:    "JSON mode" vs "Structured Outputs" comparison section; the chain-of-thought
             example schema.
Quote:       "Structured Outputs is a feature that ensures the model will always generate
             responses that adhere to your supplied JSON Schema, so you don't need to
             worry about the model omitting a required key, or hallucinating an invalid
             enum value."
```

```text
URL:         https://arxiv.org/abs/2201.11903
Kind:        primary. Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning
             in Large Language Models." Empirical owner of the reasoning-room result.
Establishes: Producing intermediate reasoning steps before the answer improves accuracy
             on arithmetic and symbolic reasoning; the intermediate steps are the
             mechanism, not a byproduct. This is the taught "thinking-out-loud" claim the
             desk links rather than re-teaches.
Paraphrase:  A chain of thought — a series of intermediate reasoning steps written out
             before the answer — significantly improves large models' performance on
             complex reasoning, including reaching state-of-the-art on GSM8K with a 540B
             model given eight worked exemplars.
Locators:    Abstract; GSM8K results section.
Quote:       "generating a chain of thought -- a series of intermediate reasoning steps
             -- significantly improves the ability of large language models to perform
             complex reasoning."
```

```text
URL:         https://arxiv.org/abs/2310.07923
Kind:        primary. Merrill & Sabharwal (ICLR 2024), "The Expressive Power of
             Transformers with Chain of Thought." Theoretical owner of "a transformer
             computes more only by writing more."
Establishes: A transformer that answers immediately after reading its input cannot solve
             certain inherently serial problems; letting it generate intermediate tokens
             (a scratchpad / chain of thought) before answering strictly increases its
             computational power, and the size of the increase scales with the number of
             intermediate steps. This is the formal backing for why removing scratch
             space (via a mask) removes capability.
Paraphrase:  There are reasoning problems (graph connectivity, simulating finite-state
             machines) provably unsolvable by standard transformers answering
             immediately. Intermediate generation fundamentally extends a decoder-only
             transformer's power; a logarithmic number of steps helps only slightly,
             while a linear number of steps enables recognizing all regular languages.
Locators:    Abstract; main theorems on log- vs linear-step decoding.
Quote:       "reasoning problems ... that are provably unsolvable by standard transformers
             that answer immediately after reading their input"; "Does such intermediate
             generation fundamentally extend the computational power of a decoder-only
             transformer? We show that the answer is yes, but the amount of increase
             depends crucially on the amount of intermediate generation."
```

### Secondary

```text
URL:         https://simonwillison.net/2024/Aug/6/openai-structured-outputs/
Kind:        secondary. Simon Willison's independent commentary (6 Aug 2024) on OpenAI's
             Structured Outputs launch, with quotes he gathered from OpenAI's Ted Sanders
             on Hacker News. Willison is not the authoring party; he reports and
             interprets. Carries context, not a load-bearing rung.
Establishes: A reputable, openable confirmation that OpenAI's feature is constrained
             decoding: it constrains generation to only schema-valid tokens, and OpenAI
             preprocesses the JSON schema into a context-free grammar. Places OpenAI's
             move in a lineage of open tools (llama.cpp grammars, jsonformer) that do the
             same by acting on next-token logits. This is what lets the writer state the
             mechanism for a provider readers know without relying on the gated blog.
Paraphrase:  Tools like jsonformer and llama.cpp grammars guarantee schema conformance
             against open-weight models by interacting with the next-token logic so only
             schema-matching tokens are selected; OpenAI credits that work and uses the
             same trick. Per Ted Sanders, the first call with a new schema is slow because
             OpenAI preprocesses the JSON schema into a context-free grammar. Willison
             does NOT report the 100%/under-40% eval figures.
Locators:    Body of the post; the quoted Ted Sanders / Hacker News note on grammar
             preprocessing.
Quote:       "techniques like jsonformer and llama.cpp grammars could provide those
             guarantees against open weights models, by interacting directly with the
             next-token logic to ensure that only tokens that matched the required schema
             were selected"; Sanders: "we need to preprocess the JSON schema into a
             context-free grammar."
```

```text
URL:         https://www.aidancooper.co.uk/constrained-decoding/
Kind:        secondary. Aidan Cooper, "A Guide to Structured Outputs Using Constrained
             Decoding" (8 Apr 2024), an independent technical explainer. Reports and
             synthesizes; owns no rung. Carries context.
Establishes: An independent account that constrained decoding manipulates the token-
             generation process to allow only next tokens that do not violate the required
             structure, and that this differs from OpenAI's JSON mode, which returns valid
             JSON without strong schema/content guarantees. Notes precedent that
             constrained decoding can improve task performance, useful for steelmanning the
             pro-structure side. Predates the Tam paper, so it does not address that debate.
Locators:    Sections on the constrained-decoding mechanism and on JSON mode vs schema
             guarantees.
Quote:       constrained decoding "manipulates a generative model's token generation
             process to constrain its next-token predictions to only tokens that do not
             violate the required output structure"; OpenAI's JSON mode "ensures API
             responses are returned as valid JSON, although it doesn't provide strong
             guarantees about the schema and contents."
```

```text
URL:         https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json
Kind:        secondary. "Let's Data Science" team explainer (11 Feb 2026). Reports and
             illustrates the mechanism; owns no rung. Carries context; the weakest of the
             three secondaries (organizational byline, no named author), included for
             headroom so the record clears the floor after any single drop.
Establishes: A plain-language restatement of the mask-before-draw mechanism and the
             JSON-mode-vs-structured-outputs distinction, aligned with the primaries.
Paraphrase:  A logit processor tracks position in the target grammar and masks invalid
             tokens by setting their logits to negative infinity; JSON mode guarantees
             valid JSON but no schema, while Structured Outputs enforces a specific JSON
             Schema via constrained decoding.
Locators:    Mechanism section; JSON-mode-vs-structured-outputs section.
Quote:       "This processor tracks position within the target grammar and masks invalid
             tokens by setting their logits to −∞"; "JSON mode guarantees syntactically
             valid JSON but places no constraints on the schema. Structured Outputs
             enforces a specific JSON Schema via constrained decoding."
```

### Gated (not counted; figures quarantined)

```text
URL:         https://openai.com/index/introducing-structured-outputs-in-the-api/
Kind:        primary to OpenAI's own mechanism and eval claims, but GATED: direct fetch
             returned HTTP 403 on repeated attempts across both rounds. NOT counted toward
             the source floor. Its constrained-decoding mechanism is independently
             confirmed by Willison (secondary, above) and OpenAI's docs page (primary,
             above), so the writer can state the mechanism without this URL.
Establishes: (mechanism only, now redundant with openable sources) OpenAI states
             Structured Outputs works by constrained decoding — the model constrained to
             only schema-valid tokens, schema converted to a grammar.
NOT-TO-BE-QUOTED: the specific eval percentages attributed to this announcement —
             "100%" schema-following for gpt-4o-2024-08-06 with Structured Outputs versus
             "under 40%" for gpt-4-0613 — appear only in sources that could not be opened
             (the announcement itself, 403) or in third-party summaries. Willison, who was
             opened, does NOT report them. Do not quote or cite these figures. If the
             article wants a reliability number, the writer must open the announcement
             directly and confirm, or omit the figure and state the guarantee
             qualitatively from OpenAI's docs page instead.
```

## Contradictions

The load-bearing contradiction is Tam et al. versus dottxt, and it is the disputed
rung the commission already flags.

- Tam et al. report constrained/format-restricted decoding sharply lowering reasoning
  accuracy (GSM8K: GPT-3.5-Turbo 75.99% to 49.25%; Claude-3-Haiku 86.51% to 23.44%;
  LLaMA-3-8B 75.13% to 48.90% under schema constraint). dottxt, re-running the same
  tasks on Llama-3-8B-instruct, finds structured generation slightly ahead of
  unstructured (GSM8K 0.78 vs 0.77; Last Letter 0.77 vs 0.73; Shuffle Object 0.44 vs
  0.41). Both cannot be read as measuring the same thing: Tam measures a pipeline that
  (in at least one model) forced the answer before the reasoning and used non-matching
  prompts; dottxt measures constraint with reasoning preserved and matched prompts.
  The reconciliation both records support: the penalty tracks lost reasoning room, not
  the mask as such. This confirms rather than undermines the commissioned angle.

- Terminology collision the writer must not blur (keep prominent). Tam et al. use
  "JSON-mode" to mean API-level constrained decoding to valid JSON. OpenAI uses "JSON
  mode" to mean the weaker feature that guarantees valid JSON but not schema conformance,
  and reserves "Structured Outputs" for the schema-constrained one. The same two words
  name a constrained decoder in one source and a non-schema-constrained mode in another.
  The dottxt rebuttal explicitly flags this conflation as one of Tam's errors, and
  Aidan Cooper's guide and OpenAI's docs both draw the OpenAI-sense line (valid JSON vs
  schema-enforced). Any sentence in the article using "JSON mode" must say which meaning
  it intends; safest is to reserve "JSON mode" for the OpenAI weak sense and call the
  hard-constrained thing "constrained decoding" or "schema-constrained structured
  outputs".

- Direction reversal within Tam et al. themselves: format restriction hurts reasoning
  tasks but can help classification tasks. So "structured output lowers accuracy" is
  not universal even inside the study that reports the largest drops; it is task-shaped.

## Numbers

```text
Figure: GSM8K accuracy, schema-constrained ("JSON-mode") vs free text — GPT-3.5-Turbo
        75.99% (text) to 49.25% (constrained); Claude-3-Haiku 86.51% to 23.44%;
        LLaMA-3-8B 75.13% to 48.90%.
Owner:  Tam et al. 2024, Table 1 (arxiv 2408.02442).
Scope:  Per-model accuracy on the GSM8K grade-school-math reasoning benchmark, their
        constrained-decoding condition vs unrestricted text. Contested by dottxt as an
        artifact of prompt/ordering, not intrinsic to constraint.
```

```text
Figure: dottxt re-run, unstructured vs structured — GSM8K 0.77 vs 0.78; Last Letter
        0.73 vs 0.77; Shuffle Object 0.41 vs 0.44.
Owner:  dottxt, "Say What You Mean" (blog.dottxt.ai/say-what-you-mean.html).
Scope:  Llama-3-8B-instruct, accuracy fractions on the same three tasks, matched prompts,
        reasoning preserved. Author has a commercial stake in structured generation.
```

```text
Figure: Schema-following eval — 100% (Structured Outputs, gpt-4o-2024-08-06) vs under
        40% (gpt-4-0613). NOT-TO-BE-QUOTED.
Owner:  OpenAI announcement (openai.com/index/introducing-structured-outputs-in-the-api),
        gated (403); Willison, who was opened, does not report it.
Scope:  OpenAI's internal schema-following eval. QUARANTINED: no openable source carries
        these exact percentages. Do not quote or cite. If a reliability figure is wanted,
        open the announcement directly and confirm, or state the guarantee qualitatively
        from OpenAI's docs page.
```

```text
Figure: Answer-before-reason field order — 100% of one model's constrained responses put
        the answer key ahead of the reason key.
Owner:  Tam et al. 2024 (arxiv 2408.02442).
Scope:  GPT-3.5-Turbo, JSON-mode condition. This is the concrete link from rung 2 (mask)
        to rung 3 (lost reasoning room): a schema whose answer field precedes its reason
        field forecloses chain-of-thought before it can happen.
```

Chain-of-thought's own headline GSM8K gain (Wei et al.) was not extracted as an exact
figure; the abstract states state-of-the-art on GSM8K for a 540B model with eight
exemplars. The article links thinking-out-loud rather than re-teaching it, so a precise
CoT number is not load-bearing here.

## Source assets

```text
Asset: Tam et al. 2024, Table 1 (per-model accuracy across text / constrained / FRI /
       NL-to-format conditions on the reasoning benchmarks).
Shows: The size and direction of the reasoning drop under constraint, side by side with
       the looser regimes, in one view.
Crop:  Must keep the column headers naming the regime and the row labels naming model and
       benchmark; a crop that keeps only the numbers loses which regime each belongs to.
```

```text
Asset: Willard & Louf, the guided-generation masking step (Algorithm 2 and the masked-
       draw equation alpha-tilde = m ⊙ alpha, s ~ Categorical(alpha-tilde)).
Shows: That the mask multiplies into the distribution before the draw — the exact
       mechanical moment the article's rung 2 describes.
Crop:  Keep the mask-then-sample two-line sequence intact; showing the sample line without
       the mask line omits the whole point.
```

```text
Asset: dottxt "Say What You Mean" results table (unstructured vs structured per task).
Shows: The rebuttal's contradicting measurement in one glance next to Tam's drops.
Crop:  Keep both columns and the task labels; a single column proves nothing.
```

```text
Asset: OpenAI announcement schema-following bar (100% vs under 40%). None usable: the
       announcement is gated and the figure is NOT-TO-BE-QUOTED. Do not reconstruct it.
```

## Discarded

```text
URL: https://arxiv.org/html/2501.10868v1 — "Generating Structured Outputs ... Benchmark
     and Studies": relevant later benchmark, but not one of the commissioned rungs and
     read only far enough to confirm it is a broader survey; not needed to source the
     chain and would pad the count.
```

```text
URL: https://www.researchgate.net/publication/386203559 and
     https://www.semanticscholar.org/paper/...7c394a8b — indexers/mirrors of the Tam et
     al. paper; secondary pointers to a primary already opened. Recorded the paper's own
     arxiv/ACL page instead.
```

```text
URL: Third-party explainers not opened and read in full (protecto.ai, newtuple,
     medium reposts) — used earlier only to glimpse the gated OpenAI figures, which are
     now quarantined. Not cited; the opened secondaries (Willison, Aidan Cooper, Let's
     Data Science) replace them.
```

## Source-policy check

Series floor: 8 sources, at least 4 primary and at least 1 secondary.
This record: 7 primary opened + 3 secondary opened = 10 usable sources. The gated
OpenAI announcement is excluded from the count. Even after dropping any one source, the
record clears 8 total with at least 1 secondary and at least 4 primary.

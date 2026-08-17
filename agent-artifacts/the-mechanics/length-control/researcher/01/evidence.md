# Evidence: the-mechanics/length-control (01)

This record supports the commission's chain in full: generation is left-to-right,
one token at a time, each token conditioned only on the text so far, with no
lookahead and no engineered length counter (settled, from the architecture
papers themselves); the emitted unit is a token, which does not line up with a
word (settled, from the tokenizer papers, and already taught in the published
letter-counting lesson); post-training reward shaping measurably favors longer
outputs (settled at the reward-model level, from a dedicated RLHF study); and,
separately, dedicated length-instruction benchmarks measure large, model-
dependent miss rates against explicit word/character/sentence targets, with one
very well specified example — GPT-4 Turbo violating an explicit word-count
ceiling on 49.3% of 802 test prompts. Two things are thinner than the rest.
First, no source in this record demonstrates the causal link the commission's
chain assumes between the reward-shaping finding (which was measured with no
length instruction in the prompt) and the count-miss finding (which is always
against an explicit instruction) — the two are consistent with each other and
plausibly compound, but that specific compounding is the writer's earned
synthesis, not a finding either study makes on its own. Second, "how well a
model can implicitly track its own length" has active, mixed evidence: one 2025
paper finds length information is partially, controllably encoded in
disentangled hidden units, while a self-report experiment in a second finds
models cannot accurately state their own already-generated word count when
asked directly — genuinely open, not merely under-cited. Nothing here
contradicts the commission's angle; the two soft spots above are gaps to word
carefully, not fractures in the argument.

## Neighbor lessons to link (do not re-derive; confirmed via `nb history --library`)

- `the-mechanics/autoregressive-generation` — "The instant a model writes a
  token, it becomes fact" (published 2026-07-25). Establishes: once a token is
  appended, it is ordinary input for the next step, which is why generation
  never revises a word once written. This is the "no draft-then-trim" half of
  the commission's chain; link it at first use, do not re-explain the
  causal-mask mechanics.
- `the-mechanics/letter-counting` — "A model can recognize strawberry's letters
  and still miscount them" (published 2026-07-20). Establishes: a model reads
  integer token IDs, not letters, so even the token-vs-word gap this article
  needs is already taught. Link it at first use for "tokens are not words";
  do not re-derive byte-pair encoding.
- `the-mechanics/formatting-defaults` — "One line in the system prompt turns
  off the bullet points" (published 2026-08-14). Establishes: post-training
  (mainly a reward-modeling stage) rewards structure and length "largely
  regardless of whether they improved the answer," and already cites Singhal
  et al. for the RLHF length-correlation finding. Link it for the post-training
  length habit; the new synthesis here is connecting that habit to the
  *counting* failure specifically, which formatting-defaults does not cover.

## Sources

```text
URL:         https://arxiv.org/abs/2311.07911
Kind:        primary — Zhou, Lu, Mishra, Brahma, Basu, Luan, D. Zhou, Hou
             (Google Research / Yale), authors of IFEval, own the benchmark
             design, the metric definitions, and the reported model scores.
Establishes: IFEval ("Instruction-Following Eval"), a 541-prompt benchmark
             built from 25 "verifiable instruction" types, one of which is
             "Length Constraints" (four sub-types: Number Paragraphs, Number
             Words, Number Sentences, and paragraphs-plus-first-word). Defines
             four accuracy metrics: prompt-level strict, instruction-level
             strict, prompt-level loose, instruction-level loose (loose applies
             8 text transforms — e.g. stripping markdown, dropping intro/outro
             lines — before re-checking, to reduce false negatives). Reports
             GPT-4 (Nov 2023 API) and PaLM 2 S (Aug 2023 API) on all four
             metrics overall, and instruction-level strict accuracy broken out
             per instruction category (bar chart, not a table).
Paraphrase:  A verifiable instruction is one a simple program can check
             automatically, e.g. "write in more than 400 words." IFEval is
             the benchmark's own name for this approach; length constraints
             are one of nine instruction categories in its per-category
             breakdown (change_case, combination, detectable_content,
             detectable_format, keywords, language, length_constraint,
             punctuation, start/end).
Locators:    pp. 2-5 (Table 1: full instruction list; Table 3: overall
             accuracy; Figure 2: per-category instruction-level strict
             accuracy; Section 2.2: metric definitions and equations).
Quote:       "we discuss how we synthesized prompts with verifiable
             instructions, and how we compute instruction-following metrics"
             (p.3); loose accuracy defined as
             "is_followed_loose(resp, inst) = Any(is_followed(transform_t(resp),
             inst) for t = 1, 2, ...)" (p.4, Eq. 2).
```

```text
URL:         https://arxiv.org/abs/2406.17744
Kind:        primary — Yuan, Kulikov, Yu, Cho, Sukhbaatar, Weston, Xu (Meta
             FAIR / NYU), authors of the length-instruction study, own the
             benchmark construction (AlpacaEval-LI, MT-Bench-LI) and the
             reported violation rates for every model in Table 2, including
             the models they did not train.
Establishes: A dedicated evaluation of length-instruction following. Builds
             AlpacaEval-LI: takes AlpacaEval 2's 805 general instruction-
             following prompts, drops 3 that already carry an explicit length
             constraint, and prepends "Answer the following instruction using
             <MAX_LEN> words or less." to the remaining 802, where <MAX_LEN>
             is set per-prompt to the *shortest* of the response lengths that
             GPT-4 Turbo (11/06), Claude 3 Opus (02/29), and Mistral Large
             (24/02) produced on the unconstrained original prompt — so the
             target is tight but guaranteed achievable by at least one strong
             model. MT-Bench-LI does the same for 240 first-turn MT-Bench
             prompts (80 questions x 3 sampled length caps). A response
             violates the instruction (Vlt%) if its word count (NLTK word
             tokenizer, punctuation excluded) exceeds <MAX_LEN>; this is a
             hard constraint, checked automatically, not judged by an LLM.
             Table 2 reports Vlt% for 9 off-the-shelf "standard" models on
             both benchmarks.
Paraphrase:  On AlpacaEval-LI, GPT-4 Turbo (gpt-4-turbo-2024-04-09) exceeded
             its own instructed word ceiling on 49.3% of 802 prompts (44.2%
             of 240 MT-Bench-LI prompts). This is the paper's own headline
             number: "GPT4-Turbo violates length constraints almost 50% of
             the time." The failure is not confined to output length overall
             — the same paper's Figure 2 shows the ratio of actual to target
             length climbing above 1.0 (a violation) especially as the target
             length grows past ~200 words, for both GPT-4-0409 and Claude
             3 Opus.
Locators:    p.1 (Abstract); p.4, Section 3.1-3.1.2 (benchmark construction,
             target-length rule, baseline rule); p.4, Figure 2 and its
             caption; p.5, Section 3.1.3 (Vlt% metric definition, NLTK word
             count); p.6, Table 2 (full per-model violation rates).
Quote:       "We find that, for example, GPT4-Turbo violates length
             constraints almost 50% of the time, highlighting a significant
             flaw in these models when it comes to steering their output
             length." (p.1). "GPT4-0409 generations exceed the target length
             limits almost 50% of the time (red dots), especially when target
             lengths are over 200 words." (p.4).
```

```text
URL:         https://arxiv.org/abs/2310.03716
Kind:        primary — Singhal (UT Austin), Goyal (Princeton), Xu (Salesforce
             AI), Durrett (UT Austin); published as a conference paper at
             COLM 2024. The authors ran the RLHF pipelines themselves (PPO
             with learned reward models, and a controlled length-only-reward
             variant) on three preference datasets and report their own
             measurements.
Establishes: That RLHF's reward-model stage, not RL optimization generally,
             is the dominant driver of the length increase RLHF produces.
             Tested on three "helpfulness" preference datasets — WebGPT
             (19.6K human-labeled QA pairs), Stack (100K StackExchange pairs,
             upvote-derived labels), RLCD (40K synthetic multi-turn dialogue
             pairs) — using Llama-7B base models. Standard PPO increases
             mean output length substantially on all three (Figure 2). When
             the learned reward model is replaced with a reward that is
             *purely* output length (no other signal), PPO's win rate over
             SFT is nearly unchanged: 56% (length-only) vs 58% (standard
             reward) on WebGPT; 64% (length-only) vs 63% (standard reward)
             on RLCD. On two of the three settings, PPO's apparent
             improvement over SFT disappears once outputs are compared only
             at matched length. Reward models themselves show strong,
             consistent correlation between assigned score and output length
             (Figure 1 heatmap, WebGPT).
Paraphrase:  Preference-based reward models learned in RLHF reward length as
             a shallow, largely content-independent feature, and policies
             trained against them move toward longer output for that reason,
             separate from any actual gain in answer quality. This is a
             finding about general "helpfulness" RLHF with no length
             instruction present in the prompt — it establishes *why*
             post-training biases models toward writing long by default, not
             that models ignore explicit length instructions (see
             Contradictions).
Locators:    p.1 (Abstract); p.2 (Introduction, length-only reward result);
             p.3, Figure 1 (WebGPT reward-vs-length heatmap) and Figure 2
             (SFT-vs-PPO length histograms, all three settings).
Quote:       "we find that even a purely length-based reward reproduces most
             downstream RLHF improvements" (Abstract). "PPO performance with
             this length-only reward is close to standard PPO (56% vs 58%
             win-rate of standard PPO on WebGPT and 64% vs 63% win-rate of
             standard PPO on RLCD)." (p.2).
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez,
             Kaiser, Polosukhin (Google Brain / Google Research / U. Toronto),
             the paper that introduces the Transformer decoder architecture
             this claim describes.
Establishes: The canonical statement of autoregressive decoding: the decoder
             produces its output sequence one symbol at a time, and at each
             step consumes everything it has already generated as additional
             input to produce the next symbol. This is the architectural
             basis for "no lookahead, conditioned only on the text so far" —
             there is no step in the described procedure that looks past the
             position currently being generated or that carries a separate
             tally of output length.
Paraphrase:  Output generation is sequential and self-conditioning: each new
             symbol is chosen using the symbols already produced, one at a
             time, until the sequence is complete. Nothing in the described
             mechanism reserves a slot for "how many symbols have I
             produced" or "how many are left" — the only carried state is
             the symbols themselves.
Locators:    p.2, Section 3 ("Model Architecture"), second paragraph.
Quote:       "Given z, the decoder then generates an output sequence
             (y1, ..., ym) of symbols one element at a time. At each step
             the model is auto-regressive, consuming the previously
             generated symbols as additional input when generating the
             next."
```

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
Kind:        primary — Radford, Wu, Child, Luan, Amodei, Sutskever (OpenAI),
             the GPT-2 paper; OpenAI's own hosted copy is the document's
             canonical location (it was not posted to arXiv). Owns both the
             explicit autoregressive factorization used by this model family
             and the description of its own byte-pair-encoding vocabulary.
Establishes: (1) The explicit factorization of language modeling as a
             left-to-right product of conditional probabilities — the
             equation the "no separate counter" claim rests on: the model
             only ever conditions on the symbols already generated, nothing
             else. (2) That the model's vocabulary is built by byte-pair
             encoding (BPE) over byte sequences, and that BPE merges produce
             tokens that do not line up with word boundaries: the paper
             gives its own example of "dog", "dog.", "dog!", and "dog?" each
             occupying separate vocabulary slots because BPE treats them as
             different byte sequences.
Paraphrase:  A language model's probability over a sequence is defined as
             the product of per-symbol probabilities, each conditioned only
             on the symbols before it — there is no term in the equation for
             a running length count or a look-ahead. Separately, the tokens
             a GPT-style model actually emits are byte-pair-encoded pieces,
             not words: common words fragment across many token variants
             (with attached punctuation, in this case), so counting tokens
             is not the same operation as counting words.
Locators:    p.3, Section 1 (Eq. 1, the factorization); p.4, Section 2.2
             ("Input Representation," the BPE vocabulary description and the
             dog/dog./dog!/dog? example).
Quote:       "it is common to factorize the joint probabilities over symbols
             as the product of conditional probabilities ... p(x) =
             product_{i=1}^{n} p(s_n | s_1, ..., s_{n-1})" (p.3). "We
             observed BPE including many versions of common words like dog
             since they occur in many variations such as dog. dog! dog? .
             This results in a sub-optimal allocation of limited vocabulary
             slots and model capacity." (p.4).
```

```text
URL:         https://arxiv.org/abs/1508.07909
Kind:        primary — Sennrich, Haddow, Birch (University of Edinburgh),
             the paper that adapts byte-pair encoding (originally a 1994
             compression algorithm) into the subword tokenization method
             GPT-family and most modern LLM tokenizers descend from. Owns
             the method, not merely a report of it.
Establishes: That subword segmentation — encoding rare and unknown words as
             sequences of smaller, reusable units rather than as single
             word-level tokens — is the deliberate design this family of
             tokenizers uses, precisely because a fixed word-level
             vocabulary cannot cover an open vocabulary of names,
             compounds, and morphological variants.
Paraphrase:  The token vocabulary is built to represent pieces of words
             (and, for some words, the whole word as one piece), never
             assuming that "one token" and "one word" coincide. This is the
             origin of the mechanism the letter-counting lesson already
             walks through in detail for a specific case (strawberry); this
             record cites it only to confirm the method's own primary
             source, not to re-derive it.
Locators:    p.1 (Abstract, Introduction); p.2, Section 2 ("Neural Machine
             Translation") background on the subword motivation.
Quote:       "we introduce a simpler and more effective approach, making the
             NMT model capable of open-vocabulary translation by encoding
             rare and unknown words as sequences of subword units."
```

```text
URL:         https://arxiv.org/abs/2505.16234
Kind:        primary — Zhang, Zhou, Wang, Fang, Zhang, Wang, Zhang, Li, Sun,
             Lyu, Liu, Su (BUPT, NTU, NUS, and others), authors of LIFEBENCH,
             own the benchmark, the two metrics they define, and every score
             in the paper's tables.
Establishes: A benchmark built specifically to test length-instruction
             following at scale: 10,800 instances across 4 task types
             (QA, summarization, reasoning, creative generation), bilingual
             (English/Chinese), 10 length constraints from 16 to 8,192 words,
             under three control methods (Equal To, At Most, At Least).
             Evaluates 26 models (9 proprietary, 8 open-source, 3 long-text-
             specialized). Defines Length Deviation (LD, signed proportional
             miss) and Length Score (LS, 0-100, penalizing under-generation
             more steeply than over-generation). Separately runs a "length
             awareness" experiment: models are asked to append a self-
             reported word count to their own output, and the self-report is
             compared against the true count.
Paraphrase:  Under the strict "Equal To" control, 23 of 26 models score below
             60 (of 100) on Length Score; the best (o3-mini) scores 75.4, and
             performance separates sharply by model — e.g. Mistral-7B-
             Instruct-v0.2 shows 84% mean absolute length deviation against
             its "Equal To" 100-point score of 26.7, versus o3-mini's 13%
             deviation and 75.4 score. Models also increasingly resort to
             "lazy strategies" (refusing, or stopping early) as constraints
             lengthen, surpassing 10% prevalence for all models at an
             8,192-word target. In the length-awareness experiment, models'
             self-reported word counts diverge from their true output word
             counts — one model, GLM-4-9B-Chat, reports a count matching the
             *instruction* even when its real output does not match it,
             which the authors read as evidence the model is not actually
             measuring its own output.
Locators:    p.2 (Abstract, RQ1-RQ3); p.6, Table 1 (per-model LD/LS scores,
             all three control methods); p.7, Section 5.1 (headline
             "23 out of 26 models score below 60" claim) and Figure 3; p.8,
             Section 5.3 "Length Awareness Deficits" and Figure 5; p.9,
             "Prevalence of Lazy Generation Strategies" and Figure 7.
Quote:       "23 out of 26 models score below 60 under length instruction
             following under the Equal To control method... with o3-mini,
             Claude-Sonnet-Thinking, and Gemini-2.5-Pro achieving 75.4, 61.3,
             and 60.0" (p.7). "GLM-4-9B-Chat reports word counts that match
             the instructions, even when its actual outputs do not,
             suggesting that it assumes compliance rather than measuring the
             true output length." (p.8).
```

```text
URL:         https://arxiv.org/abs/2507.20398
Kind:        primary — Moon, Choi, Kwon (Chungnam National University),
             Kamigaito (NAIST), Okumura (Institute of Science Tokyo), authors
             of the probing study; the finding is their own empirical result
             (hidden-state probing and hidden-unit scaling), not a report of
             someone else's work.
Establishes: That some information correlated with intended/eventual output
             length is present, and partially separable from semantic
             content, inside a model's internal activations — specifically,
             outputs of multi-head attention in lower transformer layers.
             Scaling specific identified hidden units up or down lengthens
             or shortens generation without degrading how informative the
             text is, on a summarization task across Llama, Phi-3, and
             Qwen-2.5 model families.
Paraphrase:  This is direct evidence on the "open" side of the commission's
             distinction: models are not simply blind to length internally.
             Some proxy for length exists in their activations and is
             partially controllable. It does not show the model tracks
             length accurately or reliably during ordinary generation (that
             is a separate, unresolved question — see the LIFEBench
             self-report finding above, which points the other way at the
             behavioral level).
Locators:    p.1 (Abstract, Introduction).
Quote:       "we provide empirical evidence on how output sequence length
             information is encoded within the internal representations in
             LLMs... multi-head attention mechanisms are critical in
             determining output sequence length, which can be adjusted in a
             disentangled manner." (Abstract).
```

```text
URL:         https://www.saxifrage.xyz/post/chatgpt-wordcount
Kind:        secondary — Michael Taylor, an independent practitioner (course
             creator, open-source prompt-testing tooling), reporting his own
             small test of a model he did not build; not a research paper,
             but a documented, reproducible test with a stated method,
             offered here as informal corroboration of the pattern the
             primary benchmarks measure, not as a source for any figure the
             argument depends on.
Establishes: One independently run, small-scale illustration of the same
             failure pattern the primary benchmarks measure, on a different
             model (gpt-3.5-turbo) and a plainer prompt style ("write N
             words on {topic}", no additional framing).
Paraphrase:  Across 150 API calls (5 requested word counts x 3 topics x 10
             runs), short requests were badly overshot (a 10-word request
             produced roughly 100 words) and long requests were undershot,
             with output length plateauing around 600-700 words even when
             1,000-2,000 words were requested; a 300-word request came back
             10-30% over. Posted September 7, 2023.
Locators:    Full post (methodology section describing the 150-call test;
             results section with the per-target-length pattern).
Quote:       (paraphrased by the fetch tool from the live page; treat the
             specific figures above as approximate, sourced to this post,
             not as an exact quotation)
```

## Contradictions

- **IFEval's headline accuracy is not a length-following number.** GPT-4's
  76.89% prompt-level strict accuracy (Table 3) is averaged across all 25
  verifiable instruction types; "Length Constraints" is only one of nine
  categories in the per-category chart (Figure 2), and that chart shows both
  evaluated models scoring visibly below their own overall average on it —
  but IFEval does not publish an exact per-category percentage, only the bar
  chart, so no precise length-only figure can be pulled from this source. Do
  not cite the 76.89%/83.57% headline numbers as if they characterize length
  following specifically; if a precise length-category number is needed, use
  LIFEBench or the LIFT paper's Table 2 instead, both of which measure length
  in isolation.
- **The commission's causal chain is a synthesis, not a single finding.**
  Singhal et al. measure reward-model and PPO behavior with *no* length
  instruction in the prompt (general "helpfulness" preference tuning); Yuan
  et al. and Zhang et al. measure violation rates *against* an explicit
  instruction. No source in this record runs both conditions on the same
  model to show the post-training length habit is what specifically drives
  the miss rate against explicit counts, as opposed to the token-by-token
  no-counter mechanism alone being sufficient to explain it. The two
  findings are consistent and plausibly compound (a model already biased
  toward writing long has further to overshoot before self-correction is
  even attempted, and self-correction is architecturally foreclosed either
  way) — but that compounding is the article's own argument to earn, not a
  measured result to cite as such.
- **The "open" question has evidence pulling in both directions.** Moon et
  al. (2025) find length-correlated signal is present and partially
  controllable inside hidden states. Zhang et al.'s length-awareness
  experiment (2025, in the same LIFEBench paper used for the miss-rate
  numbers) finds models cannot accurately self-report their own already-
  written word count when asked to. Read together: some internal proxy for
  length exists, but it is not reliable enough (or not the thing being
  probed) to produce accurate self-knowledge during ordinary generation.
  Present both; do not resolve the tension, since neither source resolves it
  either.
- **Model and date mismatch across benchmarks.** IFEval's own reported scores
  are for GPT-4 (Nov 2023) and PaLM 2 S (Aug 2023). LIFT's Table 2 and
  LIFEBench's Table 1 test newer models (GPT-4 Turbo 04/09, GPT-4o, Claude 3
  Opus/3.7, o3-mini, Mistral Large, Llama 3). Do not string these into one
  trend line ("length following has gotten worse/better over time") — the
  three papers use different prompts, different violation definitions, and
  different model line-ups; only within-paper comparisons are safe.

## Numbers

```text
Figure: GPT-4 (Nov 2023): 76.89% prompt-level strict / 83.57%
        instruction-level strict / 79.30% prompt-level loose / 85.37%
        instruction-level loose accuracy. PaLM 2 S (Aug 2023): 43.07% /
        55.76% / 46.95% / 59.11%.
Owner:  Zhou et al. 2023, IFEval, Table 3.
Scope:  541 prompts, 25 verifiable instruction types pooled (length
        constraints are one of nine categories, not isolated in this
        figure). Not a length-specific number — see Contradictions.
```

```text
Figure: GPT-4 Turbo (gpt-4-turbo-2024-04-09) violates an explicit
        word-count ceiling on 49.3% of AlpacaEval-LI prompts and 44.2% of
        MT-Bench-LI prompts.
Owner:  Yuan et al. 2024 (LIFT paper), Table 2.
Scope:  AlpacaEval-LI = 802 general instruction-following prompts (from
        AlpacaEval 2's 805, minus 3 with pre-existing length constraints);
        MT-Bench-LI = 240 first-turn prompts (80 questions x 3 sampled
        length caps). Violation = generated word count (NLTK tokenizer,
        punctuation excluded) exceeds the instructed <MAX_LEN>.
```

```text
Figure: Full model series, violation rate (Vlt%), AlpacaEval-LI / MT-Bench-LI:
        GPT-4 Omni (gpt-4o-2024-05-13): 39.0% / 39.2%
        GPT-4 Turbo (gpt4_1106_preview): 46.1% / 45.0%
        GPT-4 Turbo (gpt-4-turbo-2024-04-09): 49.3% / 44.2%
        Claude 3 Opus (02/29): 37.0% / 37.9%
        Mistral Large (24/02): 17.6% / 20.8%
        Llama3-70B-Instruct: 10.2% / 20.3%
        Llama3-8B-Instruct: 7.0% / 20.0%
        Llama2-70B-Chat: 28.2% / 38.3%
        Llama2-70B-Base (zero shot): 62.6% / 63.8%
        Llama3-8B-Base (zero shot): 71.6% / 27.9%
Owner:  Yuan et al. 2024 (LIFT paper), Table 2 ("Standard models" block).
Scope:  Same two benchmarks and violation definition as above. Preserved in
        full because the spread (7% to 71.6%) is itself the evidence that
        length-following ability is not uniform across models — useful if
        a chart is wanted.
```

```text
Figure: Length-only reward vs. standard learned reward, PPO win-rate over
        SFT: 56% vs 58% (WebGPT); 64% vs 63% (RLCD).
Owner:  Singhal et al. 2024, "A Long Way to Go," p.2.
Scope:  AlpacaFarm-simulated pairwise preference win rates (500 held-out
        prompts per task; no length instruction present in any prompt).
```

```text
Figure: 23 of 26 models score below 60 (of 100) on LIFEBench's Length Score
        under the strict "Equal To" control; best score 75.4 (o3-mini);
        next-best 61.3 (Claude-3.7-Sonnet-Thinking), 60.0 (Gemini-2.5-Pro).
        Mistral-7B-Instruct-v0.2: 84% mean absolute length deviation, LS
        26.7. Lazy-strategy prevalence (refusal/premature stop) exceeds 10%
        for every model tested once the length constraint reaches 8,192
        words.
Owner:  Zhang et al. 2025, LIFEBench, Table 1 and Section 5.1/5.3.
Scope:  10,800 instances, 26 models, 10 length constraints (16-8,192
        words), English and Chinese, three control methods (Equal To/At
        Most/At Least figures differ; the 23-of-26 figure is Equal To).
```

```text
Figure: 10-word request -> ~100 words delivered; 300-word request -> 330-390
        words (10-30% over); 1,000-2,000-word requests -> output plateaus
        around 600-700 words regardless of the higher target.
Owner:  Michael Taylor, saxifrage.xyz, Sept 2023 (secondary; independent
        test, not a peer-reviewed source).
Scope:  150 API calls to gpt-3.5-turbo (5 requested lengths x 3 topics x 10
        runs each). One model, one prompt style, informal corroboration
        only — do not present as measuring the same thing as the LIFT or
        LIFEBench figures above.
```

## Source assets

```text
Asset: LIFT paper (arXiv:2406.17744), Figure 2 — two scatter plots
       (GPT4-0409 and Claude3-Opus), target length on the x-axis,
       ratio of actual generated length to target length on the y-axis,
       802 points each, colored red (violation, ratio > 1) or blue
       (compliant).
Shows: The violation is not a fixed small overshoot — the ratio fans out
       and skews upward as the target length grows past roughly 200
       words, visually showing the miss getting worse for longer asks,
       not just present at a flat rate.
Crop:  Must retain both axis labels, the y=1.0 reference line, and the
       red/blue color legend; the ratio-vs-target-length relationship is
       the point, not the absolute count of dots.
```

```text
Asset: LIFEBench paper (arXiv:2505.16234), Table 1 — per-model Length
       Deviation and Length Score under all three control methods
       (Equal To / At Most / At Least), 26 models grouped as
       Proprietary / Open-Source / Long-Text Enhanced.
Shows: The spread between best (o3-mini, LS 75.4) and worst (e.g.
       Mistral-7B-Instruct-v0.2, LS 26.7; Suri-I-ORPO, LD 506%) under the
       identical test — grounds the "why do some models follow length
       instructions far better than others" open question with a real,
       wide, measured range rather than an anecdote.
Crop:  Must keep the model name column, the Equal To LD/LS columns
       together (they are the strict test), and enough of the table to
       show at least one strong and one weak model; do not crop to a
       single row, which would lose the comparison that makes the table
       useful.
```

```text
Asset: LIFEBench paper (arXiv:2505.16234), Figure 5 — "Length Awareness
       Experiment": real output word count vs. self-reported word count,
       log-log axes, for four models (Gemini-2.0-Flash-Thinking,
       DeepSeek-R1, GLM-4-9B-Chat, Mistral-7B-Instruct-v0.2), against a
       reference line and separate regression fits for real vs. reported
       counts.
Shows: A model's own claimed word count and its true word count are
       different fitted lines, not the same line — direct visual evidence
       that the model is not accurately tracking (or at least not
       accurately reporting) its own output length as it writes.
Crop:  Must keep both fit lines and the reference line together with
       axis labels on at least one panel; a single panel (e.g. GLM-4-9B-
       Chat, the paper's own example of a model that "assumes compliance
       rather than measuring") would carry the point without needing all
       four.
```

```text
Asset: IFEval paper (arXiv:2311.07911), Figure 2 — bar chart, instruction-
       level strict accuracy per category, PaLM 2 S vs. GPT-4.
Shows: length_constraint is visibly one of the weaker categories for both
       models relative to their own overall average (see Contradictions
       for why no exact number can be pulled from it).
Crop:  None recommended — the chart's bars are not numerically labeled, so
       a crop could not carry a precise claim; use only if the point being
       made is qualitative ("even the model that scores best in aggregate
       is weaker on this specific category") and say so in the caption.
```

## Discarded

```text
URL: https://platform.openai.com/tokenizer — interactive JS tool, returned
     HTTP 403 to a plain fetch and could not be read as static text; not
     pursued further since Radford et al. 2019 and Sennrich et al. 2016
     already establish tokens-are-not-words from open-access primary
     sources with a quotable example.
URL: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
     — returned HTTP 403 to a plain fetch; same reason as above, not
     pursued further.
URL: https://languagelog.ldc.upenn.edu/nll/?p=68167 — opened and read (Mark
     Liberman, "AI systems still can't count," Jan 29 2025). Concerns
     models failing an acrostic task (spelling a word using the second
     letter of consecutive sentences), not word/character/sentence-count
     following. Related mechanism (tokenization vs. character-level
     structure) but a different task; using it here risks conflating two
     distinct failure modes the commission asks to keep separate from
     spelling/counting (already the letter-counting lesson's territory).
     Not cited.
```

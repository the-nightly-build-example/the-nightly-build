# Evidence record: the-mechanics/getting-math-wrong (01)

The evidence supports the commission's spine firmly at its two ends and more thinly
in its middle. It is settled and well sourced that a language model has no built-in
arithmetic unit, that its accuracy on multi-digit multiplication falls sharply as the
digit count grows (GPT-4: 59% at 3x3, ~4% at 4x4, ~0% at 5x5, zero-shot), that
frontier tokenizers still chop numbers into runs of up to three digits rather than
clean place-value digits (OpenAI's current `o200k_base`, GPT-4o's tokenizer, caps
digit tokens at `\p{N}{1,3}`), and that writing the steps out (scratchpad /
chain-of-thought) or calling a calculator (tool use) recovers the accuracy. A single
concrete, independently verified failed calculation is available for the anchor:
57,897 x 12,832, where ChatGPT returned 742,021,104 and the true product is
742,934,304. The thin part is the commission's step 4, "what interpretability has
found." The real-model interpretability studies cover only small numbers (two-digit
operands, 0-99) on mid-size open models, and two of them disagree about whether the
mechanism is a structured trigonometric "algorithm" or an unordered "bag of
heuristics." The clean, fully reverse-engineered circuit (Nanda et al.) is a toy
trained only on modular addition, not a chatbot doing multiplication. So the settled
claims (no exact human-style carrying algorithm; accuracy degrades with size) hold,
but the "exactly how" is genuinely open and must not be overclaimed. Two scoping
facts belong in the piece: modern reasoning models and tool-wrapped products
increasingly get large arithmetic right, but they do so precisely by the fixes in
step 3 (built-in chain-of-thought, code execution), not by a new arithmetic unit; and
OpenAI's frontier tokenizer still uses chunked digits, so tokenization is not
"solved" on the frontier the way single-digit models solved it.

## Commission chain: support and status

- **Step 1 — predicts text, no arithmetic unit; right for common small sums, plausible-wrong for large rare ones.** SETTLED. Supported by Dziri et al. (accuracy is high on small in-distribution problems and collapses out of distribution), Nikankin et al. and Kantamneni & Tegmark (the internal mechanism is representational/heuristic, not a computation unit), and the worked TechCrunch failure. The "confident and wrong" quality is reported by TechCrunch (Wiggers) and the Waterloo work of Yuntian Deng.
- **Step 2 — numbers tokenized in chunks, not clean digits, so no place value.** SETTLED for the mechanism, with a scope caveat. The tiktoken source shows GPT-3.5/4 (`cl100k_base`) and GPT-4o (`o200k_base`) both cap digit tokens at three (`\p{N}{1,3}`). Singh & Strouse own the claim that GPT-3.5/4 assign separate tokens to 1-, 2-, and 3-digit numbers while LLaMa and PaLM use single-digit tokenization. OPEN/SCOPED: many current open models (Llama, Mistral, Gemma, DeepSeek) use single-digit tokenization, so "chunks" is a frontier-OpenAI-and-similar fact, not universal. Differentiate from `the-mechanics/letter-counting`: that lesson is characters hidden inside a token; this is that the token boundaries do not line up with place value.
- **Step 3 — left-to-right generation, no scratchpad; carry has nowhere to live; CoT or a calculator fixes it.** SETTLED. Nye et al. (scratchpad), Bai/Deng et al. (implicit chain-of-thought reaches ~100% where standard training is <1%), and Toolformer (calculator API) each support a distinct fix. Singh & Strouse add that a right-to-left rewrite alone (comma-separating digits) already improves GPT-3.5/4. Link `the-mechanics/thinking-out-loud` and `the-mechanics/tool-use`.
- **Step 4 — models implement approximate/heuristic representations of number, not a carrying algorithm; accuracy falls with size.** PARTLY SETTLED, PARTLY OPEN. SETTLED: there is no exact digit-by-digit carrying circuit, and accuracy degrades with digit count (Dziri; Bai/Deng attribute multiplication failure to missing long-range dependencies / uncached partial products). OPEN: how numbers are represented and combined. Kantamneni & Tegmark find a structured helical "Clock" mechanism for two-digit addition; Nikankin et al. find an unordered "bag of heuristics." These frame the same territory differently — record as the live disagreement, and note both are small-range studies on mid-size open models, not frontier multiplication.

## Sources

```text
URL:         https://arxiv.org/abs/2305.18654
Kind:        primary — the authoring team (Dziri et al.) owns the measurement of transformer accuracy vs multiplication size
Establishes: LLM multi-digit multiplication accuracy falls sharply as digit count grows; transformers reduce compositional tasks to shortcut pattern-matching rather than executing the full computation
Paraphrase:  On zero-shot multi-digit multiplication, off-the-shelf ChatGPT and GPT-4 reach only 55% and 59% on 3-digit x 3-digit problems, and performance degrades toward zero as the number of digits increases. The paper argues transformers solve such tasks by linearized subgraph matching, not by executing the multi-step algorithm.
Locators:    Abstract; introduction (the 55%/59% sentence); Figures 3-4 (accuracy by problem size); NeurIPS 2023
Quote:       "off-the-shelf ChatGPT and GPT4 achieve only 55% and 59% accuracies on this task" (3-digit by 3-digit multiplication)
```

```text
URL:         https://allenai.org/blog/faith-and-fate-limits-of-transformers-on-compositionality-d90726d635ef
Kind:        primary — authored by Nouha Dziri, the paper's lead author, at Ai2; restates the study's own figures
Establishes: the per-digit fall-off numbers for GPT-4 in plain form (the arxiv text states 3x3 explicitly; this restates the larger sizes)
Paraphrase:  GPT-4 reaches 59% on 3-digit by 3-digit multiplication, ~4% on 4-digit by 4-digit, and near 0% as size grows further (5-digit).
Locators:    Body of the Ai2 blog post; author Nouha Dziri
Quote:       "GPT-4 achieves only 59% accuracy on this task ... dropping to 4% for 4-digit x 4-digit multiplication"
```

```text
URL:         https://arxiv.org/abs/2402.14903
Kind:        primary — Singh & Strouse own the first controlled study of number-tokenization effects on arithmetic
Establishes: how frontier vs open models tokenize numbers, and that tokenization direction/scheme changes arithmetic accuracy
Paraphrase:  LLaMa and PaLM tokenize numbers one digit at a time; GPT-3.5 and GPT-4 assign separate tokens to each 1-, 2-, and 3-digit number. Forcing right-to-left tokenization (inserting commas between digits) markedly improves GPT-3.5/4 arithmetic; left-to-right errors are systematic, and the gap between directions shrinks as models scale.
Locators:    Abstract; tokenization-scheme section; results tables
Quote:       "models like LLaMa and PaLM opt for single-digit tokenization while GPT-3.5 and GPT-4 have separate tokens for each 1-, 2-, and 3-digit number"
```

```text
URL:         https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py
Kind:        primary — the source artifact defining OpenAI's tokenizers; it owns the exact splitting rule
Establishes: current OpenAI frontier tokenizers cap a numeric token at three digits, so long numbers are split into runs of up to three that do not respect place value
Paraphrase:  Both the cl100k_base (GPT-3.5/GPT-4) and o200k_base (GPT-4o) pre-tokenization patterns include the digit component \p{N}{1,3}+, which limits any number token to at most three consecutive digits.
Locators:    cl100k_base pattern (the pat_str for the cl100k encoder); o200k_base pattern (the o200k pat_str)
Quote:       "\p{N}{1,3}"  (appears in both the cl100k_base and o200k_base pattern strings)
```

```text
URL:         https://arxiv.org/abs/2410.21272
Kind:        primary — Nikankin, Reusch, Mueller, Belinkov own this causal/interpretability analysis
Establishes: LLMs do arithmetic with a collection of heuristics rather than a robust general algorithm or memorization
Paraphrase:  Using causal circuit analysis, the authors identify sparse sets of neurons that each fire for specific input patterns (for example, an operand falling in a certain range), and show that the unordered combination of these heuristic neurons explains most of the model's arithmetic accuracy. They conclude the models neither memorize nor run a generalizable algorithm.
Locators:    Abstract; circuit-identification and heuristic-taxonomy sections; ICLR 2025
Quote:       (paraphrase) "a bag of heuristics" — individual neurons implementing simple pattern rules, whose combination accounts for most arithmetic accuracy
```

```text
URL:         https://arxiv.org/abs/2502.00873
Kind:        primary — Kantamneni & Tegmark own this reverse-engineering of addition in real LLMs
Establishes: three real pretrained LLMs represent numbers as a generalized helix and add them with a "Clock" manipulation, evidenced by causal intervention; scope is small (two-digit) numbers
Paraphrase:  Studying GPT-J (6B), Pythia-6.9B, and Llama-3.1-8B on problems a+b for a,b in [0,99], the authors find numbers encoded as a generalized helix that is causally implicated in addition and subtraction, and describe a "Clock" algorithm that rotates the a and b helices to produce the a+b helix, which later layers read out.
Locators:    Abstract; model/range statement ("we analyze 3 LLMs: GPT-J (6B), Pythia-6.9B, and Llama3.1-8B"; "problems a+b for integers a,b in [0,99]"); causal-intervention sections
Quote:       "numbers are represented in these LLMs as a generalized helix, which is strongly causally implicated for the tasks of addition and subtraction"
```

```text
URL:         https://arxiv.org/abs/2301.05217
Kind:        primary — Nanda et al. own this fully reverse-engineered circuit; included to mark the modular-toy boundary honestly
Establishes: a small transformer trained ONLY on modular addition learns a discrete-Fourier / trigonometric circuit; this is the clean "algorithm" result and is a toy, not a chatbot doing multiplication
Paraphrase:  A small transformer trained on modular addition is fully reverse-engineered to a mechanism that maps addition to rotation on a circle using discrete Fourier transforms and trig identities. The clarity of this circuit comes from the toy, single-task setting.
Locators:    Abstract; algorithm reverse-engineering section; ICLR 2023
Quote:       "uses discrete Fourier transforms and trigonometric identities to convert addition to rotation about a circle"
```

```text
URL:         https://arxiv.org/abs/2112.00114
Kind:        primary — Nye et al. own the scratchpad result
Establishes: models fail at long/unbounded addition when answering directly but succeed when made to emit intermediate steps
Paraphrase:  Language models struggle with tasks needing unbounded multi-step computation, such as adding integers, but when prompted to work "step by step" and write intermediate results into a scratchpad, accuracy on long addition and other multi-step tasks improves dramatically.
Locators:    Abstract; long-addition experiments
Quote:       "scratchpads dramatically improve the ability of language models to perform multi-step computations"
```

```text
URL:         https://arxiv.org/abs/2302.04761
Kind:        primary — Schick et al. own the Toolformer result
Establishes: the fix by tool use — a model that learns to call a calculator API removes the arithmetic weakness
Paraphrase:  Language models "struggle with basic functionality, such as arithmetic." Toolformer teaches a model, self-supervised, to decide when to call external APIs (a calculator among them) and to fold the returned result into its next-token prediction, improving zero-shot performance.
Locators:    Abstract; tool set (calculator, QA, search, translation, calendar)
Quote:       "struggle with basic functionality, such as arithmetic or factual lookup"
```

```text
URL:         https://arxiv.org/abs/2510.00184
Kind:        primary — Bai, Pres, Deng, Tan, Shieber, Viegas, Wattenberg, Lee own this reverse-engineering of why multiplication fails
Establishes: standard fine-tuning fails to learn multi-digit multiplication because it does not form the long-range dependencies (cached partial products / running sum) the task needs; supplying that inductive bias fixes it
Paraphrase:  A transformer fine-tuned normally on multiplication converges to a local optimum lacking the long-range dependencies multiplication requires (it fails to cache and retrieve pairwise partial products). A model trained with implicit chain-of-thought, or with an auxiliary running-sum objective, forms those dependencies and succeeds. This is the mechanism behind step 3's "the carry has nowhere to live."
Locators:    Abstract; "Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls"; submitted 2025-09-30
Quote:       (abstract, paraphrase) standard fine-tuning "converges to a local optimum that lacks the required long-range dependencies"; the successful model caches and retrieves pairwise partial products
```

```text
URL:         https://techcrunch.com/2024/10/02/why-is-chatgpt-so-bad-at-math
Kind:        secondary — Kyle Wiggers, TechCrunch, reporting on the phenomenon and on Yuntian Deng's work
Establishes: the worked, confidently-wrong failure for the anchor, and the popular framing that ties the failure to tokenization; source for Deng's title
Paraphrase:  Asked to multiply 57,897 x 12,832, ChatGPT returned 742,021,104; the correct product is 742,934,304. The article attributes LLM math trouble to tokenization ("tokenizers don't really know what numbers are" and can split 380 as one token but 381 as "38" + "1"), and quotes Yuntian Deng, an assistant professor at the University of Waterloo, on GPT-4o failing beyond ~4-digit operands. The article does not discuss tool use / code interpreter as a fix.
Locators:    Body of the article; author Kyle Wiggers, 2024-10-02
Quote:       "ChatGPT gave me the answer 742,021,104; the correct one is 742,934,304"
```

```text
URL:         https://www.beren.io/2024-05-11-Integer-tokenization-is-now-much-less-insane/
Kind:        secondary — Beren Millidge, analysis of tokenizer number-handling across models over time
Establishes: the history and current landscape of number tokenization; supports the "shift" and the scope caveat on step 2
Paraphrase:  Older tokenizers (GPT-2/GPT-3/GPT-NeoX) split integers inconsistently (2249 -> ['2','249'], 2250 -> ['22','50']). Llama, Mistral, Gemma, DeepSeek and Yi tokenize each digit separately; GPT-4 and Llama-3 chunk into groups of up to three digits. Millidge argues the move away from the chaotic old schemes likely improved models' math.
Locators:    Full post; author Beren Millidge
Quote:       "large numbers of integers were assigned a single unique token, and even multi-token integers were not split in a consistent way"
```

```text
URL:         https://techxplore.com/news/2025-12-ai-stumble-basic-multiplication-special.html
Kind:        secondary — reporting (Dec 2025) on the Bai/Deng et al. study; supplies the exact accuracy figures the primary abstract does not state
Establishes: the scoping counter-point — even recent standard-trained models fail 4-digit multiplication (<1%), and targeted training methods reach ~100%, with no claim that reasoning models have solved it
Paraphrase:  The article reports that with standard fine-tuning, models scored less than 1% on 4-digit-by-4-digit multiplication, while implicit chain-of-thought reached 100% and a running-sum training objective reached 99%. It names the study authors (Bai, Tan, and collaborators from Chicago, MIT, Harvard, Waterloo, Google DeepMind) and makes no claim that reasoning models fixed multiplication.
Locators:    Body of the article; reporting on arXiv 2510.00184
Quote:       "less than 1% accuracy when multiplying two four-digit numbers" vs "100% accuracy" with implicit chain-of-thought
```

## Contradictions

- **Structured algorithm vs bag of heuristics (the core open question).** Kantamneni & Tegmark
  (https://arxiv.org/abs/2502.00873) describe a genuine, causally-verified trigonometric "Clock"
  mechanism for two-digit addition — arguably more than a "heuristic." Nikankin et al.
  (https://arxiv.org/abs/2410.21272) describe an unordered "bag of heuristics" with no general
  algorithm. Both study small-range arithmetic on mid-size open models, and both agree it is NOT the
  human digit-by-digit carrying algorithm. The commission's "heuristic, not a carrying algorithm"
  framing is safe; the two papers' disagreement is exactly the "open" part of step 4. Do not present
  either as the settled account of how numbers are combined.

- **"Chunks, not clean digits" is not universal, and not even monotonic over time.** Singh & Strouse
  and the tiktoken source establish chunked digits for OpenAI frontier models (still true in
  o200k_base / GPT-4o). But Millidge and Singh & Strouse both note Llama, Mistral, Gemma, DeepSeek and
  PaLM use single-digit tokenization. So the failure's tokenization cause holds for the OpenAI-style
  frontier the reader is most likely using, but the piece must not claim all models chop numbers into
  chunks. Scope the claim to models whose tokenizer does.

- **"AI can't do arithmetic" vs modern products getting it right.** The naked claim is undermined by
  three things the commission itself anticipates: reasoning models with long built-in chain-of-thought,
  tool routing to a calculator/code interpreter (Toolformer is the mechanism; shipped products do this),
  and targeted training (implicit CoT reaching ~100%, per techxplore/Bai-Deng). None of these is a new
  arithmetic unit — they are step 3's fixes wrapped around the same next-token core. The honest scope:
  the raw, no-tool, no-scratchpad generation still fails large multiplication (techxplore, Dec 2025,
  reports <1% for standard-trained 4-digit multiplication), and that is the behavior the lesson explains.
  This scopes the angle; it does not break it.

- **The worked example's wrongness is real but its magnitude is modest.** ChatGPT's 742,021,104 vs the
  true 742,934,304 differ by 913,200 (about 0.12%) — "looks about right," which fits the commission's
  framing ("a confident, wrong answer that looks about right") rather than a wild miss. Present it as
  plausibly-wrong, not absurd.

## Numbers

```text
Figure: ChatGPT 55%, GPT-4 59% accuracy on 3-digit x 3-digit multiplication (zero-shot)
Owner:  Dziri et al., "Faith and Fate" (https://arxiv.org/abs/2305.18654)
Scope:  Zero-shot, off-the-shelf models, 3x3-digit integer multiplication; per-cell denominator (number of sampled problems) shown in Figures 3-4, not given as a single number in the text
```

```text
Figure: GPT-4 ~4% at 4-digit x 4-digit, ~0% at 5-digit (zero-shot)
Owner:  Dziri (Ai2 blog, author-owned restatement of the study; https://allenai.org/blog/faith-and-fate-limits-of-transformers-on-compositionality-d90726d635ef)
Scope:  Same zero-shot multiplication setting; degradation as digit count grows
```

```text
Figure: Digit-token cap = 3 (regex \p{N}{1,3})
Owner:  openai/tiktoken source (https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py)
Scope:  cl100k_base (GPT-3.5/GPT-4) and o200k_base (GPT-4o); a number token is at most three consecutive digits
```

```text
Figure: 57,897 x 12,832 -> ChatGPT 742,021,104; true product 742,934,304 (difference 913,200)
Owner:  TechCrunch/Wiggers for the transcript (https://techcrunch.com/2024/10/02/why-is-chatgpt-so-bad-at-math); true product independently recomputed by the researcher
Scope:  Single documented failure; use as the concrete anchor. True product verified: 57897 x 12832 = 742,934,304
```

```text
Figure: Standard fine-tuning <1% vs implicit chain-of-thought 100% (running-sum objective 99%) on 4-digit x 4-digit multiplication
Owner:  Bai/Deng et al. (https://arxiv.org/abs/2510.00184); exact percentages as reported by techxplore (https://techxplore.com/news/2025-12-ai-stumble-basic-multiplication-special.html)
Scope:  Purpose-trained small transformers on 4x4-digit multiplication; shows the failure and the fix in one controlled setting. The <1%/100% figures are from the secondary report; the abstract owns the mechanism (missing long-range dependencies / uncached partial products), not the exact numbers
```

```text
Figure: Addition interpretability range a,b in [0,99]; models GPT-J (6B), Pythia-6.9B, Llama-3.1-8B
Owner:  Kantamneni & Tegmark (https://arxiv.org/abs/2502.00873)
Scope:  Two-digit operands only, three mid-size open models; the ceiling on how far the "how it adds" evidence reaches
```

## Source assets

```text
Asset: Faith and Fate, Figures 3-4 — accuracy vs multiplication problem size (digit count on the axes)
Shows: the fall-off from near-perfect on small in-distribution products to near-zero as digits grow; the trend the commission's optional chart would carry
Crop:  keep the axis labels (digit counts) and the accuracy scale; a crop must retain the out-of-distribution collapse, not just the high-accuracy corner. If the paper's per-cell denominators are needed for an honest caption, read them from the figure caption/appendix
```

```text
Asset: tiktoken openai_public.py — the literal pattern string containing \p{N}{1,3}
Shows: the splitting rule in the model-maker's own code; a reader sees place value is not preserved because the token boundary is fixed at three digits regardless of the number
Crop:  keep the \p{N}{1,3} component readable and label which encoding (cl100k_base / o200k_base) it belongs to; the surrounding regex is not needed
```

```text
Asset: Kantamneni & Tegmark — the generalized-helix / circular number representation figure
Shows: numbers laid out on a helix/circle, the visual that makes "not a carrying algorithm, a geometric representation" concrete
Crop:  retain the circular/helical structure and the number labels; omit the layer-by-layer intervention plots unless the piece explains them
```

```text
Asset: A verified worked long-multiplication of 57,897 x 12,832 alongside ChatGPT's 742,021,104
Shows: the confident-but-wrong behavior with the true answer beside it; the concrete anchor the commission requires
Crop:  none — this is a number pair to typeset, not an image to crop
```

The chart earns its place only if the writer uses the accuracy-vs-digit-count trend (Faith and Fate) and
supplies the verified series; per the template, do not force one. No decorative images.

## Discarded

```text
URL: https://medium.com/@philipokoampah/chat-gpt-is-bad-at-math-... — personal blog, no primary measurement, adds nothing over TechCrunch
URL: https://www.retable.io/blog/why-is-chatgpt-bad-at-math — vendor blog, no firsthand data
URL: https://www.vertechacademy.com/blog/chatgpt-wrong-math-answers-how-to-fix — SEO how-to, not evidence
URL: https://www.meter.net/news/why-cant-chatgpt-calculate-... — general explainer, no primary claim owned
URL: https://euronews.com/next/2025/12/30/which-ai-chatbot-is-the-best-at-simple-math-... — chatbot-comparison listicle, not needed for the mechanism
URL: https://montrealethics.ai/faith-and-fate-... — third-party summary of Dziri et al.; the arxiv paper and the author's own Ai2 blog are better owners
URL: https://arxiv.org/abs/2410.15580 (Language Models are Symbolic Learners in Arithmetic) — read far enough to confirm it argues for subgroup/symbolic learning; adjacent but not needed to source the commission's four steps, and would add a second framing dispute without changing the settled claims
```

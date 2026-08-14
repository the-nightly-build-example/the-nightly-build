# Evidence: the-mechanics/formatting-defaults (01)

The evidence supports the article's core chain from the preference-tuning end
inward, and it is strongest exactly where the brief needs it most: there are
published, primary numbers showing that human-and-model preference judgments
reward structure and length independent of content. Three independent primary
measurements agree that length is a large, real driver of preference wins
(LMSYS style-control coefficients; Singhal et al. length-correlation
experiments; Dubois et al. length-controlled AlpacaEval), and two more show the
same machinery rewards formatting and verbosity directly (Zheng et al.
verbosity attack; RM-Bench style interference). That labs treat markdown as a
learned default they must actively steer is settled by primary lab documents:
the OpenAI Model Spec makes markdown the interactive default that a developer
can switch off, and Anthropic's published Claude system prompts spend whole
paragraphs telling the model to stop defaulting to bullets, lists, and headers.

The chain is thin at two links, and the article should mark them open. First,
the pretraining contribution ("the model has seen markdown and knows the
tokens") has no dedicated primary here; it is background inferred from how
autoregressive models work, not a measured claim. Second, the specific
formatting content of instruction-tuning demonstration data is undisclosed: the
SFT-imitates-the-demonstration-shape mechanism is settled, but no lab publishes
what fraction of its demonstrations were bulleted or headed, so the "instruction
tuning installs the shape" step is mechanism-settled and quantity-unknown. A
third caution runs through the whole record: the strongest single number,
LMSYS's, shows length dwarfing markdown once both are controlled, and markdown's
own independent pull is small. That does not undermine the angle, but it does
mean the honest version of the claim is "structure-and-length," with length the
heavier half. See Contradictions.

## Sources

```text
URL:         https://arxiv.org/abs/2203.02155
Kind:        primary — the paper's authors (OpenAI) own the InstructGPT training
             procedure and the labeler-agreement statistics it reports.
Establishes: The instruction-tuning + RLHF pipeline that shapes answer behavior:
             supervised fine-tuning on ~13k human-written or API demonstrations
             from ~40 contractors, then a reward model trained on human rankings
             of K=4–9 responses, then PPO against that reward model. Labelers were
             told to judge "helpful, honest, harmless," inferring user intent.
Paraphrase:  Demonstrations were written/collected by hired labelers; the model is
             first trained to imitate them (SFT), then optimized against a reward
             model fit to human preference rankings. Inter-labeler agreement was
             72.6±1.5% (training labelers) and 77.3±1.3% (held-out labelers). The
             1.3B InstructGPT model's outputs were preferred to the 175B GPT-3's.
Locators:    Secs. 3.4–3.5 (data, ~13k SFT prompts; rankings of K=4–9); Sec. 3.5 /
             App. B (labeling instructions: helpful/honest/harmless, infer intent);
             agreement figures in the human-data quality discussion (Sec. 3 / App.).
Quote:       Labelers "agreed with each-other 72.6 ± 1.5% of the time" (training),
             "77.3 ± 1.3%" (held-out). Not quoted because paraphrase is exact.
```

```text
URL:         https://www.lmsys.org/blog/2024-08-28-style-control/
Kind:        primary — LMSYS owns the Chatbot Arena human-vote data and ran the
             style-control regression; the coefficients are their firsthand result.
Establishes: The strongest quantified separation of style from substance. Fitting
             the arena rating model with four style features — answer token length,
             number of markdown headers, number of bold elements, number of lists —
             shows all four independently raise win probability, with length far
             the largest, and re-ranks the leaderboard when style is held constant.
Paraphrase:  With BOTH length and markdown controlled, the normalized style
             coefficients are: length 0.249, markdown lists 0.031, headers 0.024,
             bold 0.019. Controlling markdown ONLY (length left free) raises the
             markdown coefficients — lists 0.111, headers 0.044, bold 0.056 —
             showing most of markdown's apparent pull is entangled with length.
             Length measured as the normalized difference
             (len_A − len_B)/(len_A + len_B). Controlling style shifts ranks:
             e.g. GPT-4o-mini falls, Claude 3.5 Sonnet rises; on hard prompts
             Claude 3.5 Sonnet ties for #1.
Locators:    Blog body: "Results" coefficient table; the ranking-shift figures and
             the "still observational" limitations paragraph near the end.
Quote:       "our analysis is still observational" — flagged because it is the load-
             bearing causal caveat the article must carry (see Contradictions).
```

```text
URL:         https://arxiv.org/abs/2310.03716
Kind:        primary — Singhal et al. designed and ran the RLHF length experiments
             and own the reward-length correlations and length-only-reward results.
Establishes: That length is a dominant, often majority, driver of the reward gains
             RLHF produces on helpfulness data, to the point a length-only reward
             reproduces most of the win-rate improvement.
Paraphrase:  Within-batch Pearson correlation between reward-model score and output
             length: WebGPT 0.72, Stack 0.55, RLCD 0.67 (Table 4). The share of
             reward improvement coming from NON-length features (length-stratified)
             was 2.0% on WebGPT, 53.4% on Stack, 27.2% on RLCD (Table 1) — i.e. on
             WebGPT almost all measured reward gain is length. A reward that
             optimizes length alone wins against SFT about as often as standard PPO:
             56% vs 58% (WebGPT), 59% vs 58% (Stack), 64% vs 63% (RLCD) (Table 2).
Locators:    Abstract; Table 1 (nrg / ΔR ratio); Table 2 (length-only vs PPO win
             rates vs SFT); Table 4 (eval acc and within-batch corr).
Quote:       "we find that even a purely length-based reward reproduces most
             downstream RLHF improvements over supervised fine-tuned models."
```

```text
URL:         https://arxiv.org/abs/2306.05685
Kind:        primary — Zheng et al. built MT-Bench and ran the bias probes; the
             verbosity-attack success rates and human-agreement numbers are theirs.
Establishes: That an LLM judge (the same kind of preference signal that trains and
             ranks chat models) prefers a needlessly longer, more-listed answer that
             adds no information — verbosity bias — and that strong judges otherwise
             track human preference well.
Paraphrase:  A "repetitive list" attack took 23 MT-bench answers containing numbered
             lists and had GPT-4 rephrase the list longer without new information,
             prepending it. The judge picked the padded version as better in 91.3%
             of cases for Claude-v1 and 91.3% for GPT-3.5; GPT-4 fell for it 8.7% of
             the time. GPT-4-vs-human agreement reached 85% (S2, w/o tie), above the
             81% agreement among humans. Position-bias consistency (same verdict
             after swapping order) was 23.8% Claude-v1, 46.2% GPT-3.5, 65.0% GPT-4.
Locators:    Sec. 3.3 "Limitations of LLM-as-a-judge" — verbosity bias (repetitive-
             list attack, failure-rate table), position-bias consistency table, and
             the agreement figures in Sec. 4.
Quote:       verbosity bias is when a judge "favors longer, verbose responses, even
             if they are not as clear, high-quality, or accurate as shorter ones."
```

```text
URL:         https://arxiv.org/abs/2404.04475
Kind:        primary — Dubois et al. built AlpacaEval and its length-controlled
             version; the debiasing effect on correlation is their firsthand result.
Establishes: That automatic preference evaluators favor longer outputs strongly
             enough that removing the length effect measurably improves agreement
             with human arena rankings — a second, independent length-bias result.
Paraphrase:  AlpacaEval's auto-annotator favors longer outputs. Fitting a GLM on the
             length difference and predicting preference at zero length difference
             ("length-controlled") raises Spearman correlation with LMSYS Chatbot
             Arena from 0.94 to 0.98 and makes the metric robust to deliberate
             verbosity manipulation; shorter-output proprietary models rise under
             the correction, consistent with open models having exploited the bias.
Locators:    Abstract; methods (GLM on length-difference mediator); results
             (Spearman 0.94 → 0.98; robustness-to-verbosity section).
Quote:       length control "increases the Spearman correlation with ... Chatbot
             Arena from 0.94 to 0.98."
```

```text
URL:         https://arxiv.org/abs/2410.16184
Kind:        primary — the RM-Bench authors built the benchmark and ran reward
             models against style-controlled pairs; the accuracy figures are theirs.
Establishes: That reward models themselves — the component that carries preference
             into training — prefer a well-formatted or longer answer over a plain
             correct one, directly, when style and correctness are put in conflict.
Paraphrase:  RM-Bench pairs a correct answer against a worse one and varies style.
             Reported accuracies: Easy 89.0% (style favors the correct answer),
             Normal 74.7% (matched style), Hard 46.6% (style favors the WRONG
             answer). Hard accuracy falls below random (50%): a state-of-the-art
             reward model picks the incorrectly-substanced but better-formatted /
             longer answer more than half the time. The Normal→Hard gap is 28 points.
Locators:    Results tables for easy/normal/hard accuracy; the "style bias" /
             style-interference discussion naming the below-chance hard result.
Quote:       state-of-the-art reward models "fail to resist style biases, achieving
             only 46.6% accuracy, falling short of random guess accuracy under style
             interference."
```

```text
URL:         https://model-spec.openai.com/2025-12-18.html  (interactive-default
             wording quoted from the 2024-05-08 edition, cdn.openai.com/spec/
             model-spec-2024-05-08.html; both are the document's own pages)
Kind:        primary — OpenAI's own specification of intended model behavior; it
             owns the claim that markdown is the default and is overridable.
Establishes: That markdown formatting is a deliberate default policy, not a task
             requirement, and that a developer instruction turns it off — the
             clearest primary that the format is a learned/assigned policy.
Paraphrase:  The 2024-05-08 spec defines an "interactive" setting: interactive=true
             (the default) means the assistant "defaults to using markdown
             formatting"; interactive=false means "minimal formatting" and only the
             requested content. Any such attribute "can be overridden by additional
             instructions in the request message." The current (2025-12-18) spec
             keeps a formatting guideline, "Use Markdown with LaTeX extensions,"
             under its "Use appropriate style" section.
Locators:    2024-05-08 spec, Definitions ("interactive"); 2025-12-18 spec, Sec. 7
             "Use appropriate style."
Quote:       "When interactive=true (default), the assistant defaults to using
             markdown formatting ... When interactive=false, generated messages
             should have minimal formatting."
```

```text
URL:         https://docs.anthropic.com/en/release-notes/system-prompts
             (also served at platform.claude.com/docs/en/release-notes/system-prompts)
Kind:        primary — Anthropic's own published production system prompts; it owns
             the claim about what Claude is instructed to do with formatting.
Establishes: That a shipping lab treats markdown/list output as a strong learned
             default it must actively suppress by instruction, and that a system
             prompt changes the format — direct primary support for "learned policy,
             steerable by the prompt, not a task requirement."
Paraphrase:  Multiple recent Claude system prompts instruct the model AWAY from its
             default: to "avoid over-formatting with bold emphasis, headers, lists,
             and bullet points, using the minimum formatting needed for clarity,"
             to use lists "only when (a) asked, or (b) the content is multifaceted
             enough that they're essential," and for reports/documents/explanations
             to "write prose without bullets, numbered lists, or excessive bolding
             ... unless the person asks for a list or ranking." The instruction
             recurs across Opus 4.7 (Apr 2026), Opus 4.8 (May 2026), and Fable 5
             (Jun 2026), each a system prompt Anthropic publishes with the release.
Locators:    Release-notes entries for Claude Opus 4.7, Opus 4.8, and Fable 5;
             the formatting paragraph within each.
Quote:       "Claude writes prose without bullets, numbered lists, or excessive
             bolding ... unless the person asks for a list or ranking." (Opus 4.8)
```

```text
URL:         https://simonwillison.net/2025/May/25/claude-4-system-prompt/
Kind:        secondary — independent commentary on Anthropic's published system
             prompt; the author owns the reading, not the underlying document.
Establishes: Context and interpretation only: that the default-to-lists behavior is
             widely observed, and that a counter-instruction in a system prompt is
             read as evidence the model was over-formatting by default. Supports that
             a claim was made and observed; does not itself prove the mechanism.
Paraphrase:  Willison observes that "LLMs love to answer with lists of things," and
             reads Anthropic's dedicated anti-list paragraph — telling Claude not to
             use lists in casual/empathetic chat or for reports unless asked — as a
             sign the model had been defaulting to over-formatting.
Locators:    Body, the section quoting Claude's list-formatting instructions.
Quote:       "LLMs love to answer with lists of things."
```

## Contradictions

- **How much is length vs. markdown.** The commission frames "bulleted lists and
  bold headers" as the driver. LMSYS's own numbers say length is the far heavier
  factor: with both controlled, length's coefficient (0.249) is roughly 8–13×
  each markdown element (0.019–0.031). Markdown's independent contribution is
  real but small. The larger markdown coefficients (lists 0.111) appear only when
  length is left uncontrolled, i.e. much of what looks like a markdown effect is
  length riding along. The honest claim is structure-and-length together, length
  dominant. This refines the angle rather than breaking it: bullets and headers
  are both longer-looking and separately rewarded.

- **Length is not purely a bias.** LMSYS states the analysis is "still
  observational" and names the confounder plainly: length can correlate with
  substantive quality, so part of the length preference may be earned. Singhal et
  al. show the split varies wildly by dataset — non-length features explain only
  2.0% of reward gain on WebGPT but 53.4% on Stack. The article should not claim
  formatting/length wins are entirely content-free; the evidence is that they are
  substantially, measurably content-independent, not that they are wholly so.

- **Judge/reward bias vs. human preference.** The verbosity and reward-model
  results (Zheng, RM-Bench) are strongest for automated judges and reward models.
  The human-vote evidence (LMSYS) is where the "humans prefer it too" claim lives.
  These are different populations; the article should attribute each to its own
  source and not blur "reward models prefer structure" into "humans prefer
  structure" without the arena data doing that specific work.

- **Instruction-tuning content is undisclosed.** No source here quantifies how
  formatted the SFT demonstration data is. The mechanism (SFT imitates the shape
  of demonstrations) is settled; the specific claim that demonstrations were
  heavily bulleted is not sourced and should be marked inferred/undisclosed.

- **Pretraining link unmeasured.** No primary here measures markdown prevalence in
  pretraining corpora. Treat "the base model already knows markdown from web
  text" as background, marked open, not a cited finding.

## Numbers

```text
Figure: length style-coefficient 0.249 (normalized); markdown lists 0.031,
        headers 0.024, bold 0.019 — all with length AND markdown controlled
Owner:  LMSYS style-control analysis (Chatbot Arena human votes)
Scope:  Coefficients in the arena rating (Bradley-Terry-style) model; unitless,
        normalized; Aug 2024 arena battle data. Not win-rate percentage points.
```

```text
Figure: markdown lists 0.111, headers 0.044, bold 0.056 — markdown controlled,
        length NOT controlled
Owner:  LMSYS style-control analysis
Scope:  Same model, showing markdown coefficients inflate when length is free —
        the length/markdown entanglement.
```

```text
Figure: reward–length within-batch Pearson r = 0.72 (WebGPT), 0.55 (Stack),
        0.67 (RLCD)
Owner:  Singhal et al. 2023, Table 4
Scope:  Correlation between reward-model score and output length, per preference
        dataset (helpfulness).
```

```text
Figure: non-length share of reward gain = 2.0% (WebGPT), 53.4% (Stack),
        27.2% (RLCD)
Owner:  Singhal et al. 2023, Table 1
Scope:  Length-stratified decomposition of standard-PPO reward improvement; the
        remainder is attributable to length.
```

```text
Figure: length-only reward vs standard PPO, win rate against SFT — 56% vs 58%
        (WebGPT), 59% vs 58% (Stack), 64% vs 63% (RLCD)
Owner:  Singhal et al. 2023, Table 2
Scope:  Simulated preference win rate vs the SFT baseline; length-only reward
        nearly matches full PPO.
```

```text
Figure: verbosity "repetitive list" attack success — 91.3% (Claude-v1),
        91.3% (GPT-3.5), 8.7% (GPT-4)
Owner:  Zheng et al. 2023, verbosity-bias probe (23 padded MT-bench answers)
Scope:  Share of cases the judge preferred a longer, list-padded answer adding
        no information.
```

```text
Figure: GPT-4–human agreement 85% (S2, w/o tie), vs 81% human–human
Owner:  Zheng et al. 2023
Scope:  Agreement on MT-bench/arena pairwise judgments; context that judges
        otherwise track humans.
```

```text
Figure: RM-Bench reward-model accuracy — Easy 89.0%, Normal 74.7%, Hard 46.6%
Owner:  RM-Bench (2410.16184)
Scope:  Correct-vs-worse answer pairs; Hard = style favors the wrong answer;
        46.6% is below the 50% random baseline. Normal→Hard gap 28 pts.
```

```text
Figure: length-controlled AlpacaEval raises Spearman vs Chatbot Arena 0.94 → 0.98
Owner:  Dubois et al. 2024
Scope:  Rank correlation of the automatic evaluator with human arena rankings,
        before vs after removing the length effect.
```

## Source assets

```text
Asset: LMSYS style-control coefficient bar chart (the four style features with
       their estimated coefficients), on the blog's results section.
Shows: At a glance that length towers over the three markdown features — the
       single clearest image of "length dominant, markdown secondary."
Crop:  Must keep all four bars and the axis so length's dominance is visible; do
       not crop to markdown-only, which would misstate the finding.
```

```text
Asset: LMSYS before/after ranking table (leaderboard with and without style
       control), same blog.
Shows: That holding style constant reorders real, named models — the concrete
       payoff of the effect.
Crop:  Keep both the pre- and post-control columns; a single column shows nothing.
```

```text
Asset: RM-Bench easy / normal / hard accuracy bars.
Shows: A reward model dropping from 89% to below-chance 46.6% as style is turned
       against correctness — the reward component preferring format over truth.
Crop:  Must retain the 50% reference line / all three bars so the below-chance
       hard bar reads correctly.
```

```text
Asset: Singhal et al. reward-vs-length scatter / correlation figures (Table 4 and
       accompanying plots).
Shows: The tight reward-length relationship a chart conveys better than the raw r.
Crop:  Keep axis labels (reward, length) and the per-dataset identity.
```

## Discarded

```text
URL: https://blog.promptlayer.com/what-we-can-learn-from-anthropics-system-prompt-updates/ — secondary summary of Anthropic's system prompts; superseded by reading the primary release-notes page directly.
URL: https://arxiv.org/html/2502.00814 (Disentangling Length Bias in Preference Learning) — a mitigation follow-up; not read to depth because the three length-bias primaries above already own the effect this article needs.
URL: https://arxiv.org/pdf/2310.03716 and https://par.nsf.gov/servlets/purl/10596575 — same Singhal paper; the PDF endpoints returned unparseable binary, so figures were read from the ar5iv HTML rendering. Not a source rejection; the canonical page recorded above is arxiv.org/abs/2310.03716.
URL: https://arxiv.org/pdf/2306.05685 and https://arxiv.org/pdf/2306.05685 (MT-Bench PDF) — PDF failed to parse; read via ar5iv HTML. Canonical page arxiv.org/abs/2306.05685 recorded instead.
```

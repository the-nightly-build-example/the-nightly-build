# Evidence: the-evidence/llama-3-herd-of-models (01)

The record supports the commissioned angle directly. Meta's own document
discloses an unusually detailed engineering record: three dense-Transformer
sizes (8B, 70B, 405B), a 15.6T-token pretraining corpus, a 3.8×10²⁵ FLOP
training budget for the 405B on up to 16K H100 GPUs, and a public benchmark
table pitting the 405B against GPT-4 (0125), GPT-4o, and Claude 3.5 Sonnet. All
of those figures are verified below against the paper (and the 405B's GPU-hours
and emissions against the model card that owns them). The document is equally
clear about what it withholds: it names no specific data sources, gives only a
four-way percentage split of the mix, and — most usefully for the angle — its
own contamination analysis (Table 15) cannot produce a performance-gain estimate
for MMLU, MMLU-Pro, HumanEval, or MBPP, four of the headline benchmarks in
Table 2. The evidence is thin in exactly one place the angle needs care: the
benchmark table is Meta's self-report, and the independent check available
(LMArena blind human preference) measures a different thing (preference, not
accuracy), so it contextualizes rather than refutes the table. The record does
not undermine the commission; it strengthens it. One naming correction the
writer must not get wrong: the paper is titled "The Llama 3 Herd of Models," but
Table 1 states "All results in this paper are for the Llama 3.1 models," and the
405B ships as Llama 3.1 under the Llama 3.1 Community License.

## Sources

```text
URL:         https://arxiv.org/abs/2407.21783
Kind:        primary — Meta AI is the authoring party and owns every claim about
             its own models; this is the report the lesson reads.
Establishes: The report's identity, authorship, and headline claims. Title "The
             Llama 3 Herd of Models"; 558+ listed authors (lead names include
             Aaron Grattafiori, Abhimanyu Dubey); submitted 31 Jul 2024, revised
             15 Aug 2024 (v2) and 23 Nov 2024 (v3). Abstract states the largest
             model is "a dense Transformer with 405B parameters and a context
             window of up to 128K tokens" and that Llama 3 "delivers comparable
             quality to leading language models such as GPT-4 on a plethora of
             tasks." Meta "publicly release[s]" pretrained and post-trained 405B
             plus Llama Guard 3.
Paraphrase:  A Meta foundation-model report announcing an 8B/70B/405B family and
             claiming rough parity with GPT-4-class models, with weights released
             under a community license.
Locators:    Abstract; arXiv abs page (title, author list, v1/v2/v3 dates).
Quote:       "Our largest model is a dense Transformer with 405B parameters and a
             context window of up to 128K tokens."
```

```text
URL:         https://arxiv.org/html/2407.21783v3  (body read from the arXiv PDF,
             pages cited by the paper's own PDF pagination)
Kind:        primary — same authoring party; this is the report body.
Establishes: (Architecture & training, verified from the PDF text, not coverage.)
             - Family: three dense Transformers, 8B / 70B / 405B. Meta "opt[s]
               for a standard dense Transformer model architecture ... rather than
               for a mixture-of-experts model ... to maximize training stability."
             - Table 1: the original 8B/70B released April 2024; the multilingual,
               long-context, tool-use versions and the 405B are "Llama 3.1"
               (July 2024). "All results in this paper are for the Llama 3.1 models."
             - Pretraining scale: "we pre-train a model with 405B parameters on
               15.6T tokens using a context window of 8K tokens," later extended in
               a continued-pretraining stage to 128K. (Abstract rounds to "~15T.")
             - Tokenizer: 128,000-token vocabulary, "100K tokens from the tiktoken
               tokenizer with 28K additional tokens" for non-English; compression
               on English improves "from 3.17 to 3.94 characters per token" vs the
               Llama 2 tokenizer.
             - 405B hyperparameters (Table 3): 126 layers, model dimension 16,384,
               FFN dimension 53,248, 128 attention heads, 8 key/value heads (GQA),
               SwiGLU, RoPE θ=500,000, peak LR 8×10⁻⁵.
             - Compute: training budget "3.8 × 10²⁵ FLOPs"; "Llama 3 405B is
               trained on up to 16K H100 GPUs, each running at 700W TDP with 80GB
               HBM3," on Meta's Grand Teton platform (RoCE cluster of 24K GPUs, of
               which up to 16K used for pretraining).
             - Data disclosure: dataset drawn "from a variety of data sources
               containing knowledge until the end of 2023"; PII and adult-content
               domains removed; no specific sites, datasets, or proportions of
               named sources are listed. Final mix: "roughly 50% of tokens ...
               general knowledge, 25% of mathematical and reasoning tokens, 17%
               code tokens, and 8% multilingual tokens."
             - Benchmark comparison: Table 2 (see Numbers).
             - Contamination: Section 5.1.4, Table 15 (see Numbers and
               Contradictions). Method scores examples by 8-gram overlap with the
               pretraining corpus, following Singh et al. (2024); the report states
               the field is unsettled and the method "can suffer from false
               positives and negatives."
             - Evaluation method for competitors: "we evaluate the performance of
               other models ourselves and compare the results with the reported
               numbers, selecting the best score."
             - Human eval (Section 5.3, Figure 17): against GPT-4 (0125), GPT-4o,
               and Claude 3.5 Sonnet, the 405B is "approximately on par" with
               GPT-4, "mixed results" vs GPT-4o and Claude 3.5 Sonnet, and "trails
               Claude 3.5 Sonnet in capabilities such as coding and reasoning."
Paraphrase:  A dense-transformer family trained at fixed, disclosed compute on an
             undisclosed-in-detail 15.6T-token corpus, benchmarked by Meta against
             three closed models, with a contamination check that fails to resolve
             the headline benchmarks.
Locators:    §"General Overview" (dense vs MoE; 15.6T; 8K→128K); Table 1;
             Table 2; Table 3; §3.1–3.1.2 (data, cutoff, mix); §3.2 (tokenizer,
             FLOPs, 126 layers); §"Compute" (16K H100, 700W); §5.1.4 + Table 15
             (contamination); §5.2 (competitor-eval method); §5.3 (human eval).
Quote:       "we pre-train a model with 405B parameters on 15.6T tokens using a
             context window of 8K tokens." / "This leads to a model size that is
             approximately compute-optimal according to scaling laws on our data
             for our training budget of 3.8 × 10²⁵ FLOPs."
```

```text
URL:         https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md
Kind:        primary — Meta's own model card; owns the GPU-hours and emissions
             accounting and the statement of what is released.
Establishes: Training compute in wall-clock terms and the release framing.
             "39.3M GPU hours of computation on H100-80GB" across the family, of
             which the 405B accounts for 30.84M H100-80GB hours. Emissions:
             11,390 tons CO2eq location-based; 0 tons CO2eq market-based (Meta
             matched with renewables). Knowledge cutoff "December 2023."
             Pretraining used "~15 trillion tokens of data from publicly available
             sources"; fine-tuning used public instruction data plus "over 25M
             synthetically generated examples." Release is under "a custom
             commercial license, the Llama 3.1 Community License."
Paraphrase:  The card supplies the GPU-hours and carbon accounting the paper body
             does not tabulate, and confirms the release is weights-plus-license,
             not data.
Locators:    Model card, "Training Energy Use / Greenhouse Gas Emissions" table;
             "Training Data" and "Intended Use / License" sections.
Quote:       "39.3M GPU hours of computation on H100-80GB"; 405B "30.84M".
```

```text
URL:         https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE
             (reader-facing copy also at https://developer.meta.com/ai/llama3_1/license/,
             to which https://www.llama.com/llama3_1/license/ 301-redirects)
Kind:        primary — the license text itself; owns exactly what a downloader is
             and is not granted.
Establishes: What "open" grants and withholds here. "Llama 3.1" is defined as the
             models plus "machine-learning model code, trained model weights,
             inference-enabling code, training-enabling code, fine-tuning enabling
             code" — weights and code, with no grant of the training data. Use
             carries conditions: display "Built with Llama"; any downstream AI
             model trained on Llama or its outputs must include "Llama" at the
             start of its name; retain the copyright notice; comply with the
             Acceptable Use Policy (https://llama.meta.com/llama3_1/use-policy).
             Section 2: a licensee with more than 700 million monthly active users
             on the release date "must request a license from Meta," grantable "in
             its sole discretion." California governing law; EEA/Switzerland users
             contract with Meta Platforms Ireland.
Paraphrase:  A conditional commercial license over weights and code — not the
             training data — with an attribution rule, a naming rule for derived
             models, an acceptable-use policy, and a 700M-MAU carve-out for the
             largest competitors.
Locators:    Definitions ("Llama 3.1", "Llama Materials"); §1.b.i (Built with
             Llama, naming); §1.b.iv (Acceptable Use Policy); §2 (700M MAU);
             §5 (trademark, ownership, litigation termination).
Quote:       "If you use the Llama Materials or any outputs or results of the Llama
             Materials to create, train, fine tune, or otherwise improve an AI
             model, which is distributed or made available, you shall also include
             'Llama' at the beginning of any such AI model name." / "is greater
             than 700 million monthly active users in the preceding calendar
             month, you must request a license from Meta".
```

```text
URL:         https://ai.meta.com/blog/meta-llama-3-1/
Kind:        primary — Meta's launch announcement; owns Meta's own positioning
             language (it is evidence of how Meta framed the release, not an
             outside assessment).
Establishes: The positioning half of the document's dual character. Meta calls
             the 405B "the first frontier-level open source AI model" and "the
             world's largest and most capable openly available foundation model,"
             and frames the release as open source "leading the way" after open
             models "mostly trailed behind their closed counterparts." Claims it
             is "competitive with leading foundation models across a range of
             tasks, including GPT-4, GPT-4o, and Claude 3.5 Sonnet." Dated 23 Jul
             2024, Meta.
Paraphrase:  Meta markets the same release as frontier-level and "open source,"
             the framing the OSI source below disputes.
Locators:    Meta blog, opening and "open source" framing sections.
Quote:       "the first frontier-level open source AI model."
```

```text
URL:         https://opensource.org/blog/metas-llama-license-is-still-not-open-source
Kind:        secondary — the Open Source Initiative writes from outside Meta and
             stewards the Open Source Definition; it assesses Meta's claim rather
             than owning the underlying facts.
Establishes: An outside, authoritative rejection of the "open source" label. OSI
             (author Jordan Maris, 18 Feb 2025) argues the Llama 3.x license fails
             the Open Source Definition: freedom 0 (use for any purpose), OSD
             point 5 (no discrimination against persons/groups), and point 6 (no
             discrimination against fields of endeavor); it flags the 700M-MAU
             clause and an exclusion of EU persons, and accuses Meta of "open
             washing."
Paraphrase:  The recognized steward of the term says the license Meta calls open
             source is not, on specific, checkable grounds.
Locators:    OSI blog post, body (three OSD failure points; open-washing).
Quote:       "Meta is trying to redefine Open Source for their own benefit and at
             the expense of our freedom."
```

```text
URL:         https://www.lmsys.org/blog/2024-08-28-style-control/
Kind:        secondary — LMSYS/LMArena runs an independent blind human-preference
             leaderboard; it measures the models from outside Meta on a different
             axis than Meta's accuracy benchmarks.
Establishes: An independent, non-benchmark check on where the 405B actually lands.
             Authors Tianle Li, Anastasios Angelopoulos, Wei-Lin Chiang (LMSYS),
             29 Aug 2024. On the Hard Prompts subset, "Claude 3.5 Sonnet ties for
             #1 with chatgpt-4o-latest and Llama-3.1-405B climbs to #3" after
             style control (rank 4 before). Style control normalizes for response
             length and markdown formatting (headers, bold, lists) to isolate
             substance from presentation.
Paraphrase:  On blind human preference for hard prompts, the 405B sits just behind
             GPT-4o and Claude 3.5 Sonnet — competitive, not ahead — consistent
             with the report's own admission that it trails Claude on coding and
             reasoning.
Locators:    LMSYS style-control blog, Hard Prompts ranking and style-control
             method.
Quote:       "In the Hard Prompt subset, Claude 3.5 Sonnet ties for #1 with
             chatgpt-4o-latest and Llama-3.1-405B climbs to #3."
```

## Contradictions

1. "Open source," disputed at the source of the term. Meta's launch blog calls
   the 405B "the first frontier-level open source AI model"
   (https://ai.meta.com/blog/meta-llama-3-1/). OSI, which authors the Open Source
   Definition, says the Llama 3.x license fails it on three specific points and
   calls the labeling "open washing"
   (https://opensource.org/blog/metas-llama-license-is-still-not-open-source).
   The license text supports the substance of OSI's objection: rights run to
   weights and code, not training data, and are conditioned by attribution, a
   naming rule, an acceptable-use policy, and the 700M-MAU carve-out. The writer
   should present "open weights under a conditional community license," and treat
   "open source" as a contested marketing term, not a settled fact.

2. The report's contamination check cannot clear its own headline numbers. Table
   15 lists a contamination percentage and an estimated performance gain per
   benchmark, but the cells for MMLU, MMLU-Pro, HumanEval, and MBPP are dashes.
   The text explains why: "for MBPP, HumanEval, MMLU and MMLU-Pro, other
   contamination detection methods may be needed: even with higher thresholds,
   8-gram overlap gives such high contamination scores that it is impossible to
   get a good performance gain estimate." Those four are among the general/code
   benchmarks in the flagship Table 2. So the document itself cannot quantify
   whether contamination inflated its headline scores — a limitation the report
   discloses but does not resolve. (Note: keep this about the report's own
   inability to certify its numbers; the mechanics of contamination-as-a-
   measurement-problem belong to the-instruments/livecodebench per the commission.)

3. Self-report wins the table; independent preference does not put the 405B on
   top. In Table 2, GPT-4o and Claude 3.5 Sonnet hold most of the boldfaced
   "best" cells in the General, Code, Math, and Reasoning blocks; the 405B leads
   on GSM8K, ARC Challenge, Nexus, and the long-context rows. Meta's own human
   eval and the independent LMArena hard-prompt ranking both place the 405B just
   behind GPT-4o and Claude 3.5 Sonnet, and the report concedes it "trails Claude
   3.5 Sonnet in capabilities such as coding and reasoning." The "best openly
   available model" claim is defensible; a "beats the closed frontier" reading of
   the table is not.

4. Common misconception about the license to avoid. Llama 2's license forbade
   using outputs to "improve any other large language model." The Llama 3.1
   Community License does NOT carry that prohibition — §1.b.i instead requires
   that a model trained on Llama or its outputs be renamed to begin with "Llama."
   Do not write that Llama 3.1 bars training competitors; the verified restriction
   is naming plus attribution plus the 700M-MAU threshold.

No source contradicts the core disclosed figures (sizes, 15.6T tokens, 3.8×10²⁵
FLOPs, GPU-hours, the Table 2 values); those are single-owner facts from the
report and model card and were read directly from the primary.

## Numbers

```text
Figure: 8B, 70B, 405B parameters — the three released model sizes
Owner:  Llama 3 report, Table 1 / General Overview
Scope:  Trainable parameters; dense Transformer (not MoE)
```

```text
Figure: 15.6T tokens (abstract rounds to "about 15T")
Owner:  Llama 3 report, General Overview / §3
Scope:  405B pretraining corpus, multilingual, knowledge to end of 2023
```

```text
Figure: 128,000-token vocabulary; English compression 3.17 → 3.94 chars/token
Owner:  Llama 3 report, §3.2 / Table 3
Scope:  Tokenizer; compression measured on a sample of English data vs Llama 2
```

```text
Figure: 3.8 × 10²⁵ FLOPs
Owner:  Llama 3 report, §3.2
Scope:  405B pretraining compute budget (the paper's stated training budget)
```

```text
Figure: up to 16K H100 GPUs, 700W TDP each, 80GB HBM3
Owner:  Llama 3 report, §"Compute"
Scope:  405B pretraining hardware (of a 24K-GPU RoCE cluster)
```

```text
Figure: 30.84M H100-80GB GPU-hours (405B); 39.3M GPU-hours (whole family)
Owner:  Llama 3.1 model card
Scope:  Cumulative training compute in wall-clock GPU-hours
```

```text
Figure: 11,390 tons CO2eq location-based; 0 tons CO2eq market-based
Owner:  Llama 3.1 model card
Scope:  Training greenhouse-gas emissions (market-based zero via renewables)
```

```text
Figure: Data mix — ~50% general knowledge, 25% math/reasoning, 17% code, 8% multilingual
Owner:  Llama 3 report, §3.1.2
Scope:  Final pretraining token mix, by broad category (no named sources given)
```

Table 2 — "Performance of finetuned Llama 3 models on key benchmark evaluations."
Read directly from the report PDF. Four columns relevant to the commission
(Llama 3 405B / GPT-4 (0125) / GPT-4o / Claude 3.5 Sonnet), by row and setting:

```text
Benchmark (setting)          405B   GPT-4(0125)  GPT-4o  Claude 3.5 Sonnet   Owner/Scope
MMLU (5-shot)                87.3   85.1         89.1    89.9                report Table 2; accuracy %
MMLU (0-shot, CoT)           88.6   85.4         88.7    88.3                report Table 2
MMLU-Pro (5-shot, CoT)       73.3   64.8         74.0    77.0                report Table 2
IFEval                       88.6   84.3         85.6    88.0                report Table 2
HumanEval (0-shot)           89.0   86.6         90.2    92.0                report Table 2; code
MBPP EvalPlus (0-shot)       88.6   83.6         87.8    90.5                report Table 2; code
GSM8K (8-shot, CoT)          96.8   94.2         96.1    96.4                report Table 2; math
MATH (0-shot, CoT)           73.8   64.5         76.6    71.1                report Table 2; math
ARC Challenge (0-shot)       96.9   96.4         96.7    96.7                report Table 2; reasoning
GPQA (0-shot, CoT)           51.1   41.4         53.6    59.4                report Table 2; reasoning
BFCL                         88.5   88.3         80.5    90.2                report Table 2; tool use
Nexus                        58.7   50.3         56.1    45.7                report Table 2; tool use
ZeroSCROLLS/QuALITY          95.2   95.2         90.5    90.5                report Table 2; long context
InfiniteBench/En.MC          83.4   72.1         82.5    (blank)             report Table 2; long context
NIH/Multi-needle             98.1   100.0        100.0   90.8                report Table 2; long context
MGSM (0-shot, CoT)           91.6   85.9         90.5    91.6                report Table 2; multilingual
```

Notes on the table: values are the report's own accuracy figures; Meta ran the
competitor evals itself and selected the best score. Comparisons the table runs:
against GPT-4 (0125), GPT-4o, Claude 3.5 Sonnet (and, in other columns not listed
here, Gemma 2 9B, Mistral 7B, Mixtral 8x22B, GPT-3.5 Turbo, Nemotron 4 340B).
Obvious gaps: no Gemini 1.5 Pro column in this table; Claude 3.5 Sonnet has a
blank on InfiniteBench/En.MC; and on the General/Code/Reasoning rows the closed
models (GPT-4o, Claude 3.5 Sonnet) hold most of the top cells, so the table shows
parity-to-slightly-behind, not a lead, on those capabilities.

Table 15 — contamination percentage and estimated performance gain (8B/70B/405B).
The load-bearing detail is which cells are dashes:

```text
Benchmark        Contam.%   Perf-gain (8B/70B/405B)
HellaSwag        85         14.8 / 14.8 / 14.3
PiQA             55          8.5 /  7.9 /  8.1
AGIEval          98          8.5 / 19.9 / 16.3   (per report; large, noisy)
BIG-Bench Hard   95         26.0 / 36.0 / 41.0
MMLU             —          — / — / —            (no estimate possible)
MMLU-Pro         —          — / — / —            (no estimate possible)
HumanEval        —          — / — / —            (no estimate possible)
MBPP             —          — / — / —            (no estimate possible)
GSM8K            41          0.0 / 0.1 / 1.3
MATH              1          0.0 / -0.1 / -0.2
SQuAD             0          0.0 / 0.0 / 0.0
Owner/Scope: Llama 3 report Table 15; % of eval set flagged by 8-gram overlap
with the pretraining corpus, and the estimated accuracy points attributable to it.
```

## Source assets

```text
Asset: Table 2, "Performance of finetuned Llama 3 models on key benchmark
       evaluations," in the report (front matter, page 3 of the PDF).
Shows: The whole self-report at a glance — 405B beside GPT-4, GPT-4o, and
       Claude 3.5 Sonnet across sixteen benchmarks, with Meta's boldfacing of
       the per-class winner. A reader sees both the parity claim and where the
       closed models still lead.
Crop:  Must retain the 405B column and the three closed-model columns with their
       benchmark labels and shot settings. Safe to omit the small-model columns
       (Gemma 2 9B, Mistral 7B) if space is tight, but keep the header row so the
       settings (5-shot, 0-shot CoT, etc.) stay attached to the numbers.
```

```text
Asset: Table 15, contamination percentage and estimated performance gain, in
       §5.1.4 (page 34 of the PDF).
Shows: The document's own admission, in its own table, that MMLU, MMLU-Pro,
       HumanEval, and MBPP carry dashes — no performance-gain estimate — while
       HellaSwag and PiQA show large ones. This is the single strongest visual
       for "what the report cannot certify about its headline numbers."
Crop:  Must retain the benchmark-name column and the dashed rows (MMLU, MMLU-Pro,
       HumanEval, MBPP) alongside a high-gain row (HellaSwag) so the contrast is
       legible. Do not crop away the dashes; they are the point.
```

```text
Asset: Table 3, key hyperparameters (page 7 of the PDF).
Shows: The 405B's shape in one place — 126 layers, dimension 16,384, 128 heads,
       8 KV heads, 128K vocab, RoPE θ=500,000 — useful if the lesson teaches what
       "dense Transformer at this scale" concretely means.
Crop:  Keep the 405B column and row labels; the 8B/70B columns are optional
       context.
```

```text
Asset: Llama 3.1 model card training/emissions table.
Shows: 30.84M (405B) and 39.3M (family) H100-80GB GPU-hours and the
       11,390-vs-0-ton emissions split, anchoring "how much compute" in
       wall-clock terms a reader can hold.
Crop:  Retain GPU-hours and both CO2eq figures with their labels.
```

## Discarded

```text
URL: https://arxiv.org/pdf/2407.21783v3 — used only as the byte source for the
     PDF actually read; the WebFetch summarizer could not parse the raw PDF, so
     the text was extracted locally with PyMuPDF. Not a separate source; the
     citable page is the arXiv abs/HTML entry above.
URL: https://www.llama.com/llama3_1/license/ — 301-redirects to
     developer.meta.com; recorded as the redirect target and cross-checked
     against the GitHub raw LICENSE (identical text). Not double-counted.
URL: General "openwashing"/leaderboard aggregator pages surfaced in search
     (analyticsvidhya, chatbench.org, agileleadershipdayindia, promise.legal
     blog, theregister opinion) — rejected as second-hand retellings; the
     primary OSI post and the LMSYS post they draw on are cited instead.
```

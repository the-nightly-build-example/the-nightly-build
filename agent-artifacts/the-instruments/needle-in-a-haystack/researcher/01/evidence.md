# Evidence record: the-instruments/needle-in-a-haystack (01)

The evidence firmly supports the commissioned angle. The original NIAH construction
(Greg Kamradt, 2023) is a single planted sentence buried in Paul Graham essays,
swept across document depth (0-100%) and context length (1K to the model's limit),
scored by whether the model returns the fact, and displayed as a green/red grid.
Labs adopted it and reported near-perfect numbers: Anthropic's Claude 2.1 post
records a jump from 27% to 98% after one prompt line, and the Gemini 1.5 report
records >99.7% single-needle recall to 1M tokens. The retrieval-vs-reasoning
critique is well-sourced from primaries: RULER shows near-perfect vanilla NIAH
collapsing once tasks add multiple needles, tracing, or aggregation, with most
models' "effective" context far below their claimed length; "Lost in the Middle"
shows a U-shaped positional collapse on multi-document QA; NoLiMa shows that
removing literal lexical overlap alone drops GPT-4o from a 99.3% baseline to 69.7%
at 32K; and LangChain's multi-needle extension (by the eval author's collaborator)
shows retrieval falling as needles and length grow, with reasoning trailing
retrieval. The record is thin in two places, both recorded below: exact wording in
the Anthropic and Gemini posts was read through the fetch summarizer rather than
copied character-for-character from the rendered page, and a few per-position
figures in "Lost in the Middle" were read off charts and should be treated as
approximate (about +/-1 point). The strongest honest defense of NIAH is also
recorded: it is a cheap, legible diagnostic that catches real, position-dependent
failures (it caught Claude 2.1's default-prompt refusal), and full-grid green is a
necessary, not sufficient, condition for long-context use.

## Sources

```text
URL:         https://github.com/gkamradt/LLMTest_NeedleInAHaystack
Kind:        primary. It is the artifact that owns the popular NIAH construction;
             Greg Kamradt authored the code and method.
Establishes: The method: plant one fact ("needle") inside a long filler text
             ("haystack") of Paul Graham essays, ask the model to retrieve it using
             only the provided context, repeat across document depth and context
             length, and render a colored grid. Depth is swept 0% (top) to 100%
             (bottom); context length from ~1K up to the model's limit. The original
             single-needle task is exact-match scored.
Paraphrase:  A simple in-context retrieval probe that stress-tests whether a long
             context model can recall one out-of-place fact at any position and
             length. The current repo has since grown UUID and UUID-chain multi-hop
             variants and configurable linear/sigmoid sweeps, but the origin is the
             single planted sentence.
Locators:    Repository README (Overview, task descriptions, example config with
             context_lengths min 2000 / max 32000 and depth_percents 0-100).
Note:        The live README describes the evolved repo (UUID tasks, JSONL scoring).
             The exact 2023 needle sentence and the original GPT-4/Claude runs are
             documented in the Anthropic post and the Arize write-up below.
```

```text
URL:         https://claude.com/blog/claude-2-1-prompting
             (canonical live page; formerly anthropic.com/news/claude-2-1-prompting,
             which 308-redirects here)
Kind:        primary. Anthropic owns this claim about its own model, Claude 2.1.
Establishes: On Kamradt's NIAH run, Claude 2.1 scored 27% with default prompting on
             the 200K-token window over Paul Graham essays; adding one directive line
             to the start of the model's reply raised it to 98%. The needle used is
             "The best thing to do in San Francisco is eat a sandwich and sit in
             Dolores Park on a sunny day," with the question "What is the most fun
             thing to do in San Francisco?"
Paraphrase:  A single sentence of prompt scaffolding, not any change to the model or
             its context length, moved the NIAH score by ~71 points. The post frames
             the low default score as a reluctance to answer from an out-of-place
             sentence, not an inability to attend to it.
Locators:    Body of the post; the fix and before/after figures; the secondary note
             that on sentences that fit naturally in context (the Viaweb/Yahoo
             example) the same technique reached ~90-95%.
Quote:       Added prompt line: "Here is the most relevant sentence in the context:"
Caveat:      Exact percentages and quoted lines were read via the fetch summarizer,
             not copied from the rendered HTML. The 27% -> 98% figures match the
             widely cited public record for this post; the writer should re-open the
             page to lift any quoted string verbatim.
```

```text
URL:         https://arxiv.org/abs/2403.05530
             (official report PDF: storage.googleapis.com/deepmind-media/gemini/
             gemini_v1_5_report.pdf, which did not parse as text on fetch)
Kind:        primary. Google DeepMind reports NIAH results for its own model,
             Gemini 1.5 Pro.
Establishes: Single-needle recall of 100% up to 530K tokens and >99.7% up to 1M
             tokens (text), retained at 99.2% out to 10M tokens; near-perfect recall
             also across audio and video haystacks up to ~1M tokens. The multiple-
             needles variant (100 distinct needles inserted, count correctly
             retrieved) is far weaker: ~70% recall up to 128K and >60% up to 1M,
             versus GPT-4 Turbo's average ~50% at 128K.
Paraphrase:  The same model that is essentially perfect at one needle is well below
             perfect the moment the task requires many needles at once. The single-
             needle 99%+ headline and the ~60-70% multi-needle number come from the
             same report and describe the same system.
Locators:    Long-context evaluation section; single-needle recall figures; the
             "multiple needles-in-a-haystack" subsection.
Caveat:      Numbers read from the arXiv HTML (v2) via summarizer. Official PDF is
             the canonical page but returned binary on fetch; arXiv abs resolves and
             carries the same report.
```

```text
URL:         https://arxiv.org/abs/2404.06654
Kind:        primary. This is the RULER benchmark paper (Hsieh, Sun, Kriman,
             Acharya, Rekesh, Jia, Zhang, Ginsburg, NVIDIA), which owns its own
             method and measurements.
Establishes: RULER extends NIAH with more and harder needle types (multi-key,
             multi-value, multi-query) plus categories that go beyond retrieval:
             multi-hop tracing (variable tracking) and aggregation (common/frequent
             word extraction), plus QA. Headline: despite near-perfect vanilla NIAH,
             almost all models drop sharply as length grows, and most models' usable
             ("effective") context is well under their claimed length.
Paraphrase:  A near-100% single-needle grid does not survive contact with tasks
             needing several facts, variable chains, or counting. "Effective context
             length" = the longest length a model still beats a Llama2-7B reference
             (85.6% at 4K). Of the flagship models ranked, only GPT-4 (effective 64K
             vs 128K claimed), Command-R (32K vs 128K), Yi-34B (32K vs 200K) and
             Mixtral (32K vs 32K) hold performance at 32K.
Locators:    Abstract (17 models, 13 tasks); effective-context-length table; the
             sentence that only four ranked models hold at 32K.
Quote:       "While all models claim context sizes of 32k tokens or greater, only
             four models ... can maintain satisfactory performance at the length of
             32K." (read via summarizer)
Caveat:      The abstract states 17 models across 13 tasks; the "only four hold at
             32K" claim refers to the smaller ranked leaderboard (about 10 flagship
             models). The load-bearing figures are the per-model effective lengths;
             the writer should confirm the ranked-model count against the table.
```

```text
URL:         https://arxiv.org/abs/2307.03172
Kind:        primary. "Lost in the Middle: How Language Models Use Long Contexts"
             (Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang), which owns
             its own positional-degradation measurements.
Establishes: A U-shaped accuracy curve by position of the relevant item: highest at
             the start or end of the context, lowest in the middle. On multi-document
             QA, GPT-3.5-Turbo with 20 documents scored ~75.8% (relevant doc first),
             ~53.8% (middle), ~63.2% (last); with 30 documents ~73.4% / ~50.9% /
             ~63.7%. Middle-position accuracy falls below the closed-book baseline of
             56.1% (no documents), against an oracle of 88.3% (only the correct
             document given).
Paraphrase:  Position, not just length, governs whether a model uses information it
             was given; in the worst case a long context is worse than no context at
             all. Key-value retrieval shows the same shape and is near-perfect only
             with query-aware contextualization.
Locators:    Abstract (U-shaped finding); multi-document QA results (20- and 30-doc
             figures); closed-book 56.1% and oracle 88.3%; key-value retrieval
             section.
Caveat:      Per-position percentages were read off the paper's figures/tables via
             summarizer; treat as approximate (about +/-1 point). The shape, the
             below-closed-book middle, and the 56.1%/88.3% baselines are the reliable
             load-bearing claims.
```

```text
URL:         https://arxiv.org/abs/2502.05167
Kind:        primary. NoLiMa: Long-Context Evaluation Beyond Literal Matching
             (Modarressi, Deilamsalehy, Dernoncourt, Bui, Rossi, Yoon, Schutze),
             which owns its own benchmark and measurements.
Establishes: Standard NIAH lets models exploit literal word overlap between question
             and needle, which turns the task into lexical lookup. NoLiMa removes that
             overlap (needle and question linked only by association/world knowledge).
             Across 13 LLMs that claim >=128K context, 11 drop below 50% of their
             short-context baseline at 32K; GPT-4o, a top performer, falls from a
             99.3% short baseline to 69.7%.
Paraphrase:  This is the cleanest documented case that a near-perfect NIAH number
             oversells real long-context ability: the only thing changed is the
             lexical shortcut, and scores collapse. It directly supports "retrieval
             != comprehension."
Locators:    Abstract (13 models; 11 below 50% at 32K; GPT-4o 99.3% -> 69.7%).
Quote:       "GPT-4o ... experiences a reduction from an almost-perfect baseline of
             99.3% to 69.7%." (read via summarizer)
```

```text
URL:         https://www.langchain.com/blog/multi-needle-in-a-haystack
             (formerly blog.langchain.com/multi-needle-in-a-haystack, redirects here)
Kind:        primary. Original analysis by Lance Martin (LangChain), extending
             Kamradt's own repo; it owns the data it reports on GPT-4-128k.
Establishes: Testing GPT-4-128k with 1, 3, and 10 needles (pizza ingredients) across
             1K-120K tokens: retrieval degrades as needle count rises 1->10 and as
             context grows 1K->120K. Example: 10 needles at ~24.8K tokens returned
             only 4 of 10. The model favors recency (misses early needles). A
             reasoning variant added on top: "reasoning lags retrieval," so
             retrieval accuracy caps how well the model can reason over the facts.
Paraphrase:  The eval's own extended form shows the single-needle grid is the easy
             case; multi-fact retrieval, and reasoning over those facts, both fall
             away with length. Useful bridge from "one lab's near-perfect number" to
             "why that number says little about real work."
Locators:    Body; the 1/3/10-needle charts; the 4-of-10 example; the reasoning-vs-
             retrieval section.
Caveat:      A vendor engineering blog, not peer-reviewed, but it is firsthand
             experimental data from the tool's authors; treat its exact percentages
             as author-reported.
```

```text
URL:         https://arize.com/blog/the-needle-in-a-haystack-test-evaluating-the-performance-of-llm-rag-systems/
Kind:        secondary. Arize AI reports on and re-runs Kamradt's test; it does not
             own the original construction.
Establishes: Documents the original 2023 construction firsthand-enough for
             corroboration: the exact needle sentence, Paul Graham haystack, the
             0-100% depth by 1K-to-limit length sweep, green=pass/red=fail grid, and
             the GPT-4 (128K) vs Claude 2.1 (200K) runs. Reports GPT-4's grid weakens
             above 64K and falls sharply at 100K+, worst in the upper-right (long
             context, needle near the start).
Paraphrase:  Confirms the construction details and the shape of the original grids.
             Used only for context and for the grid description, not as the owner of
             any lab's number.
Locators:    Body sections describing the test setup and the GPT-4 grid.
```

## Contradictions

- NoLiMa model count: a secondary retelling in search results said "12 models
  evaluated" and "10 models drop below 50% at 32K." The primary abstract says
  13 models and 11 dropping below 50%. Use the primary: 13 and 11.
- Claude 2.1 "70%" framing: a secondary (MarkTechPost) headlines a "70% recall
  increase." The primary post states the specific before/after, 27% -> 98% (a ~71
  point jump). Cite the primary figures, not the rounded headline.
- Interpretation clash with the commission's angle: none found that undermines it.
  The one point that keeps NIAH honest is that it did catch a real failure (Claude
  2.1's 27%); that is a limit on the critique, not a contradiction of it. NIAH's
  green grid is necessary but not sufficient for long-context competence, which is
  exactly the lesson's claim.
- Kamradt origin thread: his Claude 2.1 announcement thread (x.com/GregKamradt/
  status/1727018183608193393) was gated on fetch (see Discarded). The construction
  and the 27% figure are independently established by the Anthropic post and the
  Arize write-up, so the gap does not affect any claim.

## Numbers

```text
Figure: 27% -> 98% NIAH retrieval accuracy for Claude 2.1
Owner:  Anthropic (claude.com/blog/claude-2-1-prompting)
Scope:  200K-token window, Paul Graham essays haystack, single San Francisco needle;
        change is one added prompt line, model and context unchanged.
```
```text
Figure: ~90-95% after the same fix on a naturally-fitting needle (Viaweb/Yahoo)
Owner:  Anthropic (same post)
Scope:  Same setup, needle that is not out-of-place.
```
```text
Figure: 100% recall to 530K tokens; >99.7% to 1M; 99.2% at 10M (single needle, text)
Owner:  Google DeepMind, Gemini 1.5 Pro (arxiv.org/abs/2403.05530)
Scope:  Single-needle recall by context length, text modality; near-perfect also in
        audio/video to ~1M.
```
```text
Figure: ~70% recall to 128K, >60% to 1M (100 needles); GPT-4 Turbo ~50% at 128K
Owner:  Google DeepMind, Gemini 1.5 report (same)
Scope:  Multiple-needles variant, 100 distinct needles, count correctly retrieved.
```
```text
Figure: Effective context length vs claimed - GPT-4 64K/128K, Command-R 32K/128K,
        Yi-34B 32K/200K, Mixtral 32K/32K; only these four hold at 32K
Owner:  RULER (arxiv.org/abs/2404.06654)
Scope:  Effective length = longest length above the Llama2-7B reference (85.6% at 4K)
        on RULER's 13 tasks; ranked flagship leaderboard (~10 models), 17 total in
        the study.
```
```text
Figure: GPT-3.5-Turbo multi-doc QA by position - 20 docs ~75.8% (first) / ~53.8%
        (middle) / ~63.2% (last); 30 docs ~73.4% / ~50.9% / ~63.7%
Owner:  Lost in the Middle (arxiv.org/abs/2307.03172)
Scope:  Accuracy vs position of the single relevant document; approximate (read off
        figures). Closed-book baseline 56.1%; oracle 88.3%. Middle < closed-book.
```
```text
Figure: NoLiMa - 11 of 13 models below 50% of short baseline at 32K; GPT-4o
        99.3% -> 69.7%
Owner:  NoLiMa (arxiv.org/abs/2502.05167)
Scope:  Needle/question share no literal words; drop measured against each model's
        short-context (<1K) baseline.
```
```text
Figure: GPT-4-128k multi-needle - 10 needles at ~24.8K tokens returned 4 of 10;
        retrieval falls as needles 1->10 and length 1K->120K; reasoning lags
        retrieval
Owner:  LangChain / Lance Martin (langchain.com/blog/multi-needle-in-a-haystack)
Scope:  GPT-4-128k, pizza-ingredient needles, retrieval and a reasoning variant.
```

## Source assets

```text
Asset: The Claude 2.1 green/red NIAH grid on the Anthropic post
       (claude.com/blog/claude-2-1-prompting). X axis = context length up to 200K,
       Y axis = document depth (top to bottom).
Shows: The before/after of the prompt fix - a band of red at long contexts / lower
       depths under the default prompt versus near-all-green after the added line.
       Lets the reader see that the 27%->98% move is a prompt effect, not a model
       change.
Crop:  Must retain both axes with their scales and, if the post shows the pair,
       both grids side by side so the reader can compare. Do not crop to only the
       green "after" grid; the red "before" is half the argument.
```
```text
Asset: The Gemini 1.5 single-needle NIAH heatmap in the technical report
       (arxiv.org/abs/2403.05530). X = context length out to 1M (and a 10M panel),
       Y = depth.
Shows: An essentially all-green wall to 1M tokens - the visual that produced the
       "near-perfect recall" headline. Best used beside a weaker grid (multi-needle
       or a critique) so the reader sees what one green grid does and does not prove.
Crop:  Keep the full length axis and its 1M/10M label; the scale is the point.
```
```text
Asset: The original GPT-4 (128K) grid from Kamradt's run, reproduced in the Arize
       write-up. X = context length to 128K, Y = depth 0-100%.
Shows: Red concentrated in the upper-right - long context with the needle near the
       start - the first public evidence that position and length interact. Anchors
       the "Lost in the Middle" point visually.
Crop:  Retain the upper-right quadrant and both axis labels; that quadrant is the
       finding.
```
```text
Asset: RULER effective-context-length table (arxiv.org/abs/2404.06654).
Shows: Claimed vs effective length per model in one view (GPT-4 64K/128K, etc.).
       Carries the "usable context is shorter than advertised" claim better than
       prose. A small table, not a grid.
Crop:  If reproduced, keep the claimed and effective columns together; the gap is
       the point.
```

## Discarded

```text
URL: https://x.com/GregKamradt/status/1727018183608193393 - Kamradt's original
     Claude 2.1 200K NIAH announcement thread. Gated: fetch returned HTTP 402 (X
     login wall), so the thread text could not be verified firsthand. Not counted.
     Its content (the construction, the low default score) is independently
     established by the Anthropic post and the Arize write-up.
```
```text
URL: https://www.anthropic.com/news/prompting-long-context - a DIFFERENT, earlier
     Anthropic post about multiple-choice QA over government documents (~70-95K
     tokens). It has no NIAH result and is not the Claude 2.1 needle post; opened,
     read, and set aside to avoid confusing it with claude-2-1-prompting.
```
```text
URL: https://medium.com/@amanatulla1606/... and marktechpost.com "70% recall"
     coverage - secondary retellings of the Anthropic Claude 2.1 result. Not needed;
     the primary post owns the 27%->98% figures and the rounded "70%" framing is
     less precise.
```

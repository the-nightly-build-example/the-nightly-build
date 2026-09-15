# Evidence: the-instruments/training-cost (01)

The evidence supports every step of the commissioned angle. The DeepSeek-V3
technical report is the primary owner of the headline number, and it states the
figure exactly as a construction: 2.788M H800 GPU-hours for the full training,
an assumed rental price of $2 per GPU-hour, and a resulting $5.576M, with a
stage breakdown (pre-training, context extension, post-training) in its Table 1.
The report's own caveat says the figure covers only the official training run
and excludes prior research and ablation experiments. The market event of 27
January 2025 is well anchored: exchange close data gives Nvidia's one-day fall
(raw close $142.62 to $118.42, a 16.97% drop), and Bloomberg, CNBC, and Forbes
report the ~$589B market-value loss as the largest single-day loss for any
company in history. Named primaries and analysts corrected the "built for $5.6M"
reading: SemiAnalysis (its own estimate, read directly) and Bernstein's Stacy
Rasgon.

The record is thin in one place that matters, and it does not undermine the
angle so much as bound it. The evidence supports that the $5.6M number was
widely repeated and widely read as an all-in cost, and that the market moved
enormously in the same window. It does not support a sole-cause claim that the
misreading caused the $589B loss. The sell-off had several drivers at once
(R1's reasoning performance at a claimed low cost, DeepSeek's app topping the
App Store, and broad fear about future demand for Nvidia's chips). The
commission already hedges this as "moved partly on" the reading, and the writer
must keep that hedge. Second thin spot: the report's caveat does not use the
word "salaries" or name data-acquisition or personnel costs. The commission's
brief lists "salaries" among the report's exclusions; the report does not. The
"salaries and hardware capital" framing belongs to the analysts (SemiAnalysis,
Rasgon), not to DeepSeek's own caveat, and the writer must attribute it that way.

## Sources

```text
URL:         https://arxiv.org/abs/2412.19437
Kind:        primary. It is the document that owns the training-cost figure; DeepSeek-AI is the authoring party and the stakeholder.
Establishes: The exact GPU-hour count, the assumed rental price, the dollar total, the three-stage breakdown, and the scope caveat.
Paraphrase:  DeepSeek-V3 (671B total parameters, 37B activated per token, pre-trained on 14.8 trillion tokens) required 2.788M H800 GPU-hours for its full training. Assuming a rental price of $2 per H800 GPU-hour, the total training cost is $5.576M. Table 1 splits this into pre-training (2664K GPU-hours, $5.328M), context extension (119K, $0.238M), and post-training (5K, $0.01M). The report states the costs cover only the official training run and exclude prior research and ablation experiments on architectures, algorithms, or data. It does not mention salaries, personnel, or data-acquisition costs.
Locators:    Abstract; Introduction (the "economical training costs" paragraph); Table 1 ("Training costs of DeepSeek-V3, assuming the rental price of H800 is $2 per GPU hour"). Submitted 27 Dec 2024 (v1); revised 18 Feb 2025 (v2).
Quote:       "Assuming the rental price of the H800 GPU is $2 per GPU hour, our total training costs amount to only $5.576M." And: "Note that the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments on architectures, algorithms, or data." And: "During the pre-training stage, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, i.e., 3.7 days on our cluster with 2048 H800 GPUs."
```

```text
URL:         https://newsletter.semianalysis.com/p/deepseek-debates
Kind:        primary, for its own estimate. SemiAnalysis is an outside consultancy, so it is secondary to DeepSeek; but it is the primary owner of the cost estimate the article would cite, which is its own analysis. Read directly.
Establishes: An owner-attributed estimate of DeepSeek's total cost, kept distinct from the reported $5.576M.
Paraphrase:  SemiAnalysis estimates DeepSeek/High-Flyer has access to roughly 50,000 Hopper GPUs (about 10,000 H800s and about 10,000 H100s, plus H20s), that its total server capital expenditure is about $1.6B (with about $944M in operating cost for the clusters), and that its hardware spend over the company's history is well over $500M. It states the $6M figure covers only the GPU cost of the pre-training run, a portion of the model's total cost, and excludes R&D and the total cost of ownership of the hardware.
Locators:    "DeepSeek Debates," 31 Jan 2025, sections on hardware/GPU inventory and total cost of ownership.
Quote:       "The $6M cost in the paper is attributed to just the GPU cost of the pre-training run, which is only a portion of the total cost of the model." And: "Our analysis shows that the total server CapEx for DeepSeek is ~$1.6B, with a considerable cost of $944M associated with operating such clusters." And: "We are confident their hardware spend is well higher than $500M over the company history."
```

```text
URL:         https://stockanalysis.com/stocks/nvda/history/
Kind:        primary (market/exchange price data). The closing price is authored by the exchange; the data service republishes it. Read via the site's daily-history data.
Establishes: Nvidia's exact daily closes around the event and the size of the one-day fall.
Paraphrase:  NVDA closed at $142.62 on Friday 24 Jan 2025 and at $118.42 on Monday 27 Jan 2025, a fall of $24.20, or 16.97% on a raw-close basis. (Split-/dividend-adjusted closes are $142.25 and $118.11, a 16.99% fall; the two bases agree to within a rounding.)
Locators:    Daily OHLC records for 2025-01-24 (close 142.62) and 2025-01-27 (close 118.42).
Quote:       (numeric; no prose quote)
```

```text
URL:         https://www.statmuse.com/money/ask/nvidia-stock-price-in-january-2025
Kind:        primary (market/exchange price data), independent second read of the close. Read directly.
Establishes: Corroborates the one-day fall from a separate data service.
Paraphrase:  NVDA closed at $142.25 on 24 Jan 2025 and $118.11 on 27 Jan 2025, a change of -$24.14, or -16.99% (adjusted-close basis).
Locators:    Daily price answer for January 2025.
Quote:       (numeric; no prose quote)
```

```text
URL:         https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html
Kind:        secondary. Authoritative newsroom reporting of the close and the record. Direct fetch is bot-gated (HTTP 403); content confirmed through CNBC's own summary via search, consistent across two reads.
Establishes: The percentage fall, the dollar market-value loss, and the "largest single-day loss in U.S. history" framing; the Nasdaq move.
Paraphrase:  Nvidia's stock dropped about 17% Monday to close near $118.58, shedding about $589B in market cap, described as the biggest one-day loss in market value for any company in U.S. history. The tech-heavy Nasdaq slid about 3.1%.
Locators:    CNBC, "Nvidia sheds almost $600 billion in market cap, biggest one-day loss in U.S. history," 27 Jan 2025.
Quote:       Reported figure: "$589 billion" market-cap loss; "biggest drop for any company on a single day in U.S. history."
```

```text
URL:         https://www.bloomberg.com/news/articles/2025-01-27/asml-sinks-as-china-ai-startup-triggers-panic-in-tech-stocks
Kind:        secondary. Authoritative headline anchor for the record. Direct fetch gated; headline and figure confirmed via search.
Establishes: The $589B loss as the largest in market history.
Paraphrase:  Bloomberg headlined the day "Nvidia's $589 Billion DeepSeek Plunge Is Largest in Market History."
Locators:    Bloomberg, 27 Jan 2025.
Quote:       Headline: "Nvidia's $589 Billion DeepSeek Plunge Is Largest in Market History."
```

```text
URL:         https://www.forbes.com/sites/dereksaul/2025/01/27/biggest-market-loss-in-history-nvidia-stock-sheds-nearly-600-billion-as-deepseek-shakes-ai-darling/
Kind:        secondary. Reporting that supplies the prior-record comparison. Direct fetch gated (403); content confirmed via search.
Establishes: The $589B loss, and that it more than doubled the prior single-day record.
Paraphrase:  Nvidia lost $589B in market capitalization, by far the single greatest one-day value loss of any company in history, more than doubling the previous record of about $279B, also set by Nvidia, on 3 September 2024.
Locators:    Forbes (Derek Saul), 27 Jan 2025.
Quote:       "$589 billion in market capitalization ... by far the single greatest one-day value wipeout of any company in history, more than doubling the $279 billion market cap lost by none other than Nvidia on Sept. 3, 2024."
```

```text
URL:         https://finance.yahoo.com/news/nvidia-stock-plummets-loses-record-589-billion-as-deepseek-prompts-questions-over-ai-spending-135105824.html
Kind:        secondary. Reporting of the close. Read directly.
Establishes: The percentage fall and the record loss, tied to the DeepSeek news and the "$5.6 million to train" claim.
Paraphrase:  Nvidia dropped nearly 17% Monday; the decline shaved $589B off its market cap, the largest single-day loss in stock market history. Coverage tied the move to DeepSeek's claim that one of its latest models cost just $5.6M to train.
Locators:    Yahoo Finance, 27 Jan 2025.
Quote:       "Nvidia's decline shaved $589 billion off the AI chipmaker's market cap, the largest single-day loss in stock market history."
```

```text
URL:         https://www.ig.com/en/news-and-trade-ideas/why-nvidia-s-share-price-dropped-17--after-deepseek-news-250128
Kind:        secondary. Reporting of the move. Read directly.
Establishes: The ~17% fall and the ~$600B market-value erasure.
Paraphrase:  Nvidia fell about 17% on 27 Jan 2025, erasing nearly $600B in market value, its largest single-day decline, on the DeepSeek news.
Locators:    IG, 28 Jan 2025.
Quote:       "falling 17%"; "erasing nearly $600 billion in market value."
```

```text
URL:         https://www.cnbc.com/2025/01/27/deepseek-sell-off-nvidia-analysts-react.html
Kind:        secondary. Reports a named analyst's correction. Direct fetch gated (403); the quotes were confirmed consistently across two search reads and a second outlet (techstrong.ai).
Establishes: The "$5.6M is not the all-in cost" correction, attributed to a named analyst at the time.
Paraphrase:  Bernstein analysts, led by Stacy Rasgon, wrote that DeepSeek did not "build OpenAI for $5M," that the models "look fantastic" but "shouldn't be thought of as miracles," and that panic about the "death-knell of the AI infrastructure complex as we know it" was "overblown." Rasgon noted DeepSeek spent more to build its system than the headline figure claims.
Locators:    CNBC, "The DeepSeek sell-off: What major analysts are saying," 27 Jan 2025.
Quote:       Bernstein: DeepSeek did not "build OpenAI for $5M"; the models "look fantastic" but are not "miracles"; the panic was "overblown."
```

```text
URL:         https://fortune.com/2025/01/27/china-deepseek-ai-claims-true/
Kind:        secondary. Read directly.
Establishes: That the skepticism about DeepSeek's cost/compute claims was broad and named, beyond one analyst.
Paraphrase:  Named skeptics questioning DeepSeek's claims included Alexandr Wang (Scale AI CEO), Elon Musk, Ted Mortonson (Baird), and Gavin Baker (Atreides Management). The doubts centered on DeepSeek having far more GPUs than its low-cost story implied. This article does not quote Rasgon.
Locators:    Fortune, 27 Jan 2025.
Quote:       (named attributions as above; no single load-bearing quote)
```

```text
URL:         https://www.theregister.com/2025/09/19/deepseek_cost_train/
Kind:        secondary. Read directly. Bears on a different, later figure and is useful only to keep figures distinct.
Establishes: That a separate, smaller figure ($294,000) belongs to R1's post-training reinforcement-learning run, not to V3's pre-training, and that the two are routinely confused.
Paraphrase:  A September 2025 round of coverage misread a $294,000 figure (R1's reinforcement-learning run: 512 H800 GPUs for ~198 hours, plus SFT data generation) as the cost of the whole model. V3's pre-training required 2.79M GPU-hours at an estimated $5.58M; the article notes you cannot have R1 without first building V3, putting the combined figure near $5.87M.
Locators:    The Register, 19 Sept 2025.
Quote:       "DeepSeek V3 was trained on 2,048 H800 GPUs for approximately two months. In total, the model required 2.79 million GPU hours at an estimated cost of $5.58 million." And: "Since you can't have R1 without first building V3, the actual cost of the model was closer to $5.87 million."
```

## Contradictions

- **The core misreading, which the angle rests on.** The $5.576M is the compute
  cost of one training run. It was widely repeated as the all-in cost of
  building a frontier, GPT-4-class model ("built OpenAI for $5M"). Two named
  owners contradict that reading directly: SemiAnalysis (its own estimate of
  ~$1.6B total server capex and >$500M hardware spend, with the $6M covering
  only the pre-training GPU cost) and Bernstein's Stacy Rasgon (DeepSeek did not
  "build OpenAI for $5M"). This contradiction supports the commission's angle
  rather than breaking it.

- **The report's caveat does not say what the brief says it says.** The
  commission lists the report's exclusions as "prior research, ablations, data,
  salaries." The report's caveat names only "prior research and ablation
  experiments on architectures, algorithms, or data." It does not mention
  salaries, personnel, or data-acquisition cost. The salaries-and-capital
  framing is the analysts' (SemiAnalysis, Rasgon), not DeepSeek's own words. Keep
  reported fact (the report's caveat) and estimate (the analysts' all-in) distinct.

- **Causation is bounded.** Coverage tied the sell-off to DeepSeek's "$5.6M to
  train" claim, but the same coverage also credits R1's reasoning performance,
  the app topping the App Store, and demand fears for Nvidia's chips. The
  evidence supports "the market moved partly on reading the number as something
  it never claimed to be," not "the misreading caused the $589B loss." No source
  isolates the misreading as the sole cause.

- **Which model owns the number.** The $5.576M / 2.788M-H800-hour figure is
  DeepSeek-V3's, from the V3 technical report, not from the R1 paper or its model
  card. Separately, R1's much smaller figures ($202k in the library's existing
  R1 lesson for the pure RL run; ~$294k in later coverage that adds SFT-data and
  cold-start hours) belong to a different model and a different scope. The lesson
  should state whose hours, at what price, and which run, and not blend these.

- **Minor: the exact close and percentage vary by data vendor.** Raw close gives
  $142.62 to $118.42 (-16.97%); adjusted close gives $142.25 to $118.11
  (-16.99%); some outlets cite a $118.58 close and "17%." All agree on "about a
  17% one-day fall." The market-value loss is reported as $589B (Bloomberg, CNBC,
  Forbes), sometimes rounded to "nearly $600B."

## Numbers

```text
Figure: 2.788M H800 GPU-hours (full training); reported as 2,788K
Owner:  DeepSeek-V3 Technical Report (arXiv 2412.19437), Table 1
Scope:  DeepSeek-V3 full training run only (pre-training + context extension + post-training); excludes prior research and ablations
```

```text
Figure: $2 per H800 GPU-hour (assumed rental price)
Owner:  DeepSeek-V3 Technical Report, Table 1 caption / Introduction
Scope:  An assumption about rental cost, not a price DeepSeek states it paid
```

```text
Figure: $5.576M total training cost
Owner:  DeepSeek-V3 Technical Report (2.788M GPU-hours x $2)
Scope:  Compute cost of the final training run; the report's own arithmetic
```

```text
Figure: Pre-training 2,664K GPU-hours = $5.328M; Context extension 119K = $0.238M; Post-training 5K = $0.01M
Owner:  DeepSeek-V3 Technical Report, Table 1
Scope:  Stage breakdown of the $5.576M total
```

```text
Figure: 180K H800 GPU-hours per trillion tokens (3.7 days on a 2,048-H800 cluster); 14.8T tokens pre-training
Owner:  DeepSeek-V3 Technical Report, Introduction
Scope:  Pre-training throughput, the measured input behind the hour count
```

```text
Figure: ~$1.6B total server capex; ~$944M cluster operating cost; >$500M hardware spend; ~50,000 Hopper GPUs (~10,000 H800 + ~10,000 H100 + H20s)
Owner:  SemiAnalysis ("DeepSeek Debates," 31 Jan 2025) - estimate, its own
Scope:  DeepSeek/High-Flyer company-history capital, not one run; explicitly an estimate
```

```text
Figure: NVDA close $142.62 (Fri 24 Jan 2025) -> $118.42 (Mon 27 Jan 2025); -$24.20; -16.97% raw close (-16.99% adjusted)
Owner:  Exchange close data (stockanalysis.com and statmuse.com, two reads)
Scope:  One trading session, 27 Jan 2025
```

```text
Figure: ~$589B one-day market-value loss; largest single-day loss for any company in U.S./market history; prior record ~$279B (Nvidia, 3 Sept 2024)
Owner:  Bloomberg, CNBC, Forbes (reporting of the close)
Scope:  Nvidia only, one session; a market-cap change, not a realized loss
```

```text
Figure: Nasdaq Composite ~-3.1% on 27 Jan 2025
Owner:  CNBC
Scope:  Index move the same session; context for the single-name move
```

## Source assets

```text
Asset: Table 1, "Training costs of DeepSeek-V3," in the technical report (arXiv 2412.19437).
Shows: The three-stage split of GPU-hours and dollars, and the $2/GPU-hour assumption stated in the caption. It is the single clearest object showing that the headline number is an arithmetic construction.
Crop:  Must retain all four rows (pre-training, context extension, post-training, total), both columns (H800 GPU-hours and USD), and the caption's "$2 per GPU hour." Omit nothing that carries the assumption, since the assumption is the point.
```

```text
Asset: Nvidia one-day close series around 27 Jan 2025 (exchange data), for a possible committed chart-N.py.
Shows: The single-session drop from $142.62 to $118.42. This is data for a chart the paper renders itself, not an image lifted from a source.
Crop:  If charted, label the axis in dollars, mark the two dates, and cite the price-data source in the caption. Do not imply the whole move was one cause.
```

```text
Asset: SemiAnalysis "DeepSeek Debates" - the total-cost-of-ownership breakdown (server capex vs. the pre-training GPU cost).
Shows: The gap between the reported $5.576M and an owner's estimate of company-wide capital. Useful only if presented as an estimate with its owner named.
Crop:  None prescribed; if quoted, keep the estimate labeled as SemiAnalysis's, distinct from the reported figure.
```

## Background links (library, for the writer)

Surfaced with `nb history` against the library checkout. Link these in Background
rather than re-teaching; do not cite them as sources for this article's claims.

Recommended:

- **the-instruments/training-compute** (2026-08-04, "GPT-4 sits above the EU's
  systemic-risk line on a number OpenAI never disclosed"). The other frontier
  number, training compute in FLOPs, and how it too is reconstructed and
  estimated. This is the commission's "training compute measured in FLOPs" link.
- **the-instruments/parameter-count** (2026-08-05, "DeepSeek-V3 lists 671 billion
  parameters and runs 37 billion per token"). Covers this exact model's size, so
  the lesson can state 671B/37B and link instead of re-teaching parameter counts.
- **the-instruments/cost-per-token** (2026-08-03, "Claude Opus 5 publishes five
  different per-token prices"). The inference-price sibling and the commission's
  "per-token price" link; the same "one number, hidden inputs" move applied to
  serving cost.
- **the-instruments/tokens-per-second** (2026-08-01, "Groq's 270 tokens a second
  and Anyscale's 185 are both true"). The closest existing treatment of a
  hardware rate; the nearest match to the commission's "GPU-hours as a throughput
  idea." Note: there is no dedicated GPU-hours lesson in the library; this
  throughput lesson is the best available anchor, with GPU-hours also appearing
  in the deepseek-r1 and llama-3 lessons below.
- **the-evidence/deepseek-r1** (2026-07-30, "DeepSeek trained a model to reason
  without ever showing it a worked example"). Establishes that the $5.576M /
  2.788M-H800-hour figure belongs to V3, not R1, and gives R1's own small run
  (512 H800 GPUs, ~198 hours, ~$202,000). Link this so the lesson does not
  re-teach R1 and so "which run" is already grounded for the reader.

Optional:

- **the-instruments/model-flops-utilization** (2026-09-09). How much of a chip's
  peak a run actually uses, background for why an hour of GPU time is not a fixed
  amount of work.
- **the-evidence/llama-3-herd-of-models** (2026-09-05). Reports 30.84M H100
  GPU-hours for Llama 3 405B, a comparison anchor for the scale of 2.788M H800
  GPU-hours, if the writer wants one.
- **the-instruments/energy-per-query** (2026-08-02) and **the-instruments/arc-agi**
  (2026-07-21). Series siblings that run the same "same number, different
  assumptions" argument; useful for tone continuity, not for teaching background.

## Discarded

```text
https://interestingengineering.com/culture/deepseeks-ai-training-cost-billion — repeats SemiAnalysis's $1.3B/$1.6B estimate secondhand; the SemiAnalysis primary is read directly, so this adds nothing.
https://tech.slashdot.org/story/25/01/28/1315215/ — aggregator summary of the SemiAnalysis report; superseded by the primary.
https://www.macrotrends.net/stocks/charts/NVDA/nvidia/stock-price-history — HTTP 403 to the fetcher; the close is covered by two other price-data reads.
https://www.macroaxis.com/invest/history/NVDA--NVIDIA-traded-on--01-27-2025 — HTTP 403; redundant with the price data secured.
https://www.thenationalnews.com/future/technology/2025/01/27/... — general reaction piece, no figure the primaries do not own better.
https://www.tomshardware.com/.../deepseek-might-not-be-as-disruptive... — would corroborate SemiAnalysis's 50,000-GPU / $1.6B numbers, but its body was truncated behind promo content on fetch; the SemiAnalysis primary already carries these verbatim.
```

# Evidence: what-could-go-wrong/ai-environmental-cost (01)

The evidence supports the commission's core distinction cleanly. Per-unit figures
(one training run, one query) are measured in some cases and badly extrapolated in
others, and they swing by one to three orders of magnitude on choices of grid,
hardware, model size, and accounting boundary. The aggregate figure is the firmer
one: the IEA measures data-centre electricity at 415 TWh in 2024 (~1.5% of world
electricity) and projects ~945 TWh by 2030 in its Base Case, with a stated
700-1,720 TWh spread by 2035. The full-strength opening (Strubell 2019) and its
best-documented walk-backs (Patterson's 88x correction of the NAS number; Epoch
AI's 10x correction of the per-query energy number) are both nailed down from
primaries. Two things are thin. Water use per query has no primary number I could
verify, and the de Vries (2023) primary is gated behind a bot check, so its
projection figures are recorded from cross-checked reporting, not from my own
reading of the paper. Both are in Limits.

## Sources

```text
URL:         https://aclanthology.org/P19-1355/
Kind:        primary. Strubell, Ganesh & McCallum authored these measurements and estimates; they own the numbers the modern debate started from.
Establishes: Energy and CO2e of training several NLP models on measured GPU power, plus the widely-misquoted neural-architecture-search figure.
Paraphrase:  The authors sampled GPU/CPU power while training four off-the-shelf models, converted to kWh using a 1.58 PUE (2018 global average, Ascierto/Uptime) and to CO2e using the US EPA average of 0.954 lbs CO2e/kWh. Training a Transformer (big) once emits 192 lbs CO2e. The headline "five cars" figure is a separate row: a full neural architecture search (NAS) for the Evolved Transformer, 979M training steps, 274,120 P100-GPU-hours, 626,155 lbs CO2e. The car row it is compared against is "Car, avg incl. fuel, 1 lifetime" at 126,000 lbs (so the NAS run ~= 5 car-lifetimes). BERT-base on GPU is 1,438 lbs, which they call "roughly equivalent to a trans-American flight." NAS added 0.1 BLEU for at least $150k in compute.
Locators:    Table 1 (p.3645, the cars comparison); Methods eqns 1-2 (p.3646, PUE 1.58, CO2e=0.954*pt); Table 3 (p.3648, per-model kWh/CO2e/cost); Sec 4.1 (p.3648, BERT ~= flight, NAS 0.1 BLEU).
Quote:       "Transformer (big) 192 ... w/ neural arch. search 626,155" (Table 1)
```

```text
URL:         https://arxiv.org/abs/2104.10350
Kind:        primary. Patterson et al. (Google + UC Berkeley) computed these figures from their own hardware/datacenter measurements.
Establishes: How grid, location, hardware, and datacenter efficiency move a training run's carbon by large factors; direct correction of Strubell's NAS estimate; carbon of five large models.
Paraphrase:  The choice of DNN, processor, datacenter, and grid can move a training run's carbon "up to ~100-1000X." Same Transformer(big): gross 0.429 kg CO2e/kWh on the US average vs Google Iowa gross 0.478 but net 0.080 kg/kWh after 24/7 carbon-free matching. They reduce Strubell's Evolved Transformer NAS estimate "by 88X": Strubell put NAS at 284 tCO2e (=626,155 lbs), the actual search was ~3.2 tCO2e; 18.7x of the gap is proxy-task confusion (the search ran on a small proxy, not full-size tasks) and the rest is Google's efficient datacenters. NAS is run once per problem-domain + search-space, not once per model, so its cost was misattributed to single-model training. Five-model training emissions (net tCO2e / MWh): GPT-3 552.1 / 1,287 (Microsoft Azure, US avg 0.429 kg/kWh, V100, 2020); T5 46.7 / 86 (Google Taiwan, 2019); Meena 96.4 / 232 (Google Georgia, 2019); GShard-600B 4.3 / 24.1 (Google N. Carolina, 2020); Switch Transformer 59.1 / 179 (Google Georgia, 2020). Context: Masanet et al. (Science 2020) found global datacenter energy rose only ~6% from 2010-2020 while compute capacity rose ~550%. Overall Evolved-Transformer-on-TPU-in-Iowa vs Transformer-on-P100-in-avg-US datacenter is a 57X CO2e improvement.
Locators:    Abstract (100-1000X); Table 1 (p.3, Transformer gross/net, PUE 1.59 vs 1.11); Sec 2.3 (p.4, Masanet 6%/550%); Sec 4.1 (p.8, "88X off", 18.7X, proxy-task); Table 4 (p.6, five models, "Fraction of NAS Estimate in [Str19] (284 tCO2e)").
Quote:       "reduce by 88X an earlier estimate of the CO2e for the neural architecture search for Evolved Transformer" (Intro, p.1)
```

```text
URL:         https://arxiv.org/abs/2211.02001
Kind:        primary. Luccioni, Viguier & Ligozat measured BLOOM's training and ran its inference API themselves.
Establishes: Training and inference carbon of a 176B model with an explicit life-cycle accounting boundary, and how a low-carbon grid changes the answer.
Paraphrase:  BLOOM (176B params, 1.08M A100-GPU-hours, 433,196 kWh dynamic) emitted 24.69 tonnes CO2eq counting only dynamic power on a 57 gCO2eq/kWh grid (French nuclear-heavy, IDRIS Jean Zay). Adding embodied hardware (11.2 t) and idle infrastructure (14.6 t) brings the life-cycle total to 50.5 tonnes; embodied is ~20-30% of the total, use ~70-80%. In their Table 4 comparison BLOOM is 25 t vs OPT-175B 70 t and GPT-3 502 t (their inferred GPT-3 figure, using 429 gCO2eq/kWh; note Patterson's own GPT-3 number is 552 t). Inference: an 18-day API deployment on GCP (16 A100s, us-central1 at 394 gCO2eq/kWh) handling ~558 requests/hour (230,768 total) consumed 914 kWh and emitted ~19 kg CO2eq/day, 340 kg over the run; ~0.28 kWh was drawn even at near-zero requests, and ~75% of energy went to keeping the model in memory.
Locators:    Table 1 (p.2, 433,196 kWh, 57 gCO2eq/kWh); Sec 4.2 (p.4, 24.69 t dynamic); Table 3 (p.5, 50.5 t life-cycle split); Table 4 (p.7, BLOOM/OPT/GPT-3/Gopher); Sec 4.4 (p.5-6, inference API, 340 kg, 558 req/hr, 75% memory).
Quote:       "24.7 tonnes of CO2eq if we consider only the dynamic power consumption, and 50.5 tonnes if we account for all processes" (Abstract)
```

```text
URL:         https://www.iea.org/reports/energy-and-ai  (full text opened at https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf)
Kind:        primary. IEA World Energy Outlook Special Report "Energy and AI" (April 2025); IEA is the authoring body and owns the aggregate measurement and projection. This is the measured-aggregate anchor.
Establishes: Measured 2024 data-centre electricity and the 2030/2035 projection with an explicit scenario range; IEA's own measured per-task inference energy; GPT-4 training energy.
Paraphrase:  Data centres used ~415 TWh in 2024, ~1.5% of world electricity (US 45%, China 25%, Europe 15%), and have grown ~12%/year since 2017, four times faster than total electricity. Base Case: ~945 TWh by 2030, "slightly more than Japan's total electricity consumption today," AI the most important driver. Sensitivity cases at 2030: Lift-Off over 1,260 TWh, High Efficiency ~800 TWh, Headwinds ~670 TWh; by 2035 the four-case spread is 700-1,720 TWh. Data centres are less than ~10% of global electricity demand growth to 2030 (below industrial motors, air conditioning, or EVs), but >20% of demand growth in advanced economies. IEA's own measured per-task inference (Figure 1.16, with Sasha Luccioni): text generation ~0.3 Wh on a small language model, ~5 Wh on a medium one; image generation ~1.7 Wh; video generation ~115 Wh for a 6-second clip; a phone charge is ~15 Wh. GPT-4 training: ~25,000 GPUs, ~22 MW total equipment, ~14 weeks at 84% load factor = ~42.4 GWh, ~0.43 GWh/day.
Locators:    Executive Summary p.13-15 (415 TWh/1.5%/2024; 945 TWh/2030; 700-1,720 TWh/2035); Ch.2 exec bullets (Lift-Off 1,260 / High Efficiency 800 / Headwinds 670 by 2030); Ch.1 Fig 1.16 text p.45 (per-task Wh); Ch.1 p.44 (GPT-4 42.4 GWh).
Quote:       "Data centre electricity consumption is set to more than double to around 945 TWh by 2030."
```

```text
URL:         https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
Kind:        primary. Epoch AI (Josh You) owns this recalculation of per-query energy; it is the correction record for the viral figure.
Establishes: A worked ~0.3 Wh estimate for a typical GPT-4o query, and an explicit trace of where the older ~3 Wh figure came from and why it was too high.
Paraphrase:  A typical GPT-4o query uses ~0.3 Wh: assumptions are ~500 output tokens, ~100B active parameters (of ~200B, mixture-of-experts), H100s at 1500W with overhead, 10% compute and 70% power utilization. The commonly cited ~3 Wh ("10x a Google search") figure comes from Alex de Vries (2023), built on a Feb 2023 SemiAnalysis estimate assuming 4,000 input + 2,000 output tokens on A100 hardware. It is ~10x too high for three reasons: pessimistic token count (2,000 output vs a realistic ~269), older A100 (not H100) hardware, and use of peak rather than utilized power. Caveat on the new number: it excludes image generation and long inputs; a 10k-token input reaches ~2.4 Wh and a 100k-token input ~40 Wh. Corroborated later by Sam Altman (~0.34 Wh) and Google's Gemini per-prompt figure.
Locators:    Body sections "Our estimate", "Where does the 3 Wh figure come from", "Caveats"; footnote naming de Vries (2023) and SemiAnalysis.
Quote:       "typical ChatGPT queries using GPT-4o likely consume roughly 0.3 watt-hours"
```

```text
URL:         https://techcrunch.com/2025/02/11/chatgpt-may-not-be-as-power-hungry-as-once-assumed/
Kind:        secondary. TechCrunch reports on Epoch AI's analysis from outside; it confirms that a claim was walked back, not that either number is true.
Establishes: That the ~3 Wh per-query figure was publicly disputed and revised down to ~0.3 Wh, and records Josh You's caveats.
Paraphrase:  Reports Epoch AI's finding that the "~3 Wh, 10x a Google search" figure "assumed OpenAI used older, less-efficient chips," and that GPT-4o averages ~0.3 Wh per query. Josh You stresses the estimate is approximate because OpenAI publishes little, and that it omits image generation and long-input queries.
Locators:    Paragraphs 1-6.
Quote:       "the average ChatGPT query consumes around 0.3 watt-hours"
```

```text
URL:         https://www.datacenterfrontier.com/energy/article/33038469/iea-study-sees-ai-cryptocurrency-doubling-data-center-energy-consumption-by-2026
Kind:        secondary. Trade outlet reporting the IEA Electricity 2024 figures from outside the IEA.
Establishes: That the IEA's earlier (Electricity 2024) edition put 2022 data-centre electricity near 460 TWh and projected a possible >1,000 TWh by 2026; used here to date and scope the earlier IEA edition, not as an owner of the number.
Paraphrase:  Attributes to IEA Electricity 2024: data centres ~460 TWh in 2022 (~2% of global electricity); crypto ~110 TWh in 2022 (0.4%); projection to more than 1,000 TWh by 2026, "roughly equivalent to the electricity consumption of Japan"; crypto up >40% to ~160 TWh by 2026. Also repeats the per-request comparison ChatGPT 2.9 Wh vs Google search 0.3 Wh.
Locators:    Body, IEA-attributed paragraphs.
Quote:       "data centers' total electricity consumption could reach more than 1,000 terawatt-hours (TWh) in 2026"
```

```text
URL:         https://www.downtoearth.org.in/science-technology/global-electricity-consumption-by-ai-could-increase-by-85-134-twh-annually-by-2027-92286
Kind:        secondary. Reports de Vries (2023) from outside; stands in for the gated primary and confirms the claim exists, not that it is correct.
Establishes: The de Vries projection figures used in the present-day argument, recorded because the Joule primary is bot-gated (see Limits).
Paraphrase:  Attributes to de Vries (Joule 2023): worldwide AI electricity could rise 85-134 TWh/year by 2027; a worst case where Google AI matches Ireland's ~29.3 TWh/year; if generative AI ran in every Google search, ~80 GWh/day; ChatGPT inference ~564 MWh/day vs GPT-3 training 1,287 MWh. De Vries's own hedge: innovations in model architecture and algorithms could mitigate or even reduce AI electricity use.
Locators:    Body, de Vries-attributed paragraphs.
Quote:       "85-134 TWh annually by 2027"
```

## Contradictions

- **Per-query energy: alarmist vs corrected.** The viral figure is ~2.9-3 Wh per
  ChatGPT query, "10x a Google search," which the IEA Electricity 2024 edition
  repeated (2.9 Wh) and which traces to de Vries (2023) via a Feb-2023 SemiAnalysis
  estimate (4,000 in / 2,000 out tokens, A100). Epoch AI (Feb 2025) put a typical
  GPT-4o query at ~0.3 Wh, ~10x lower, and Sam Altman later stated ~0.34 Wh. The
  correction is not that per-query use is trivial in all cases: Epoch's own numbers
  reach ~2.4 Wh for a 10k-token input and ~40 Wh for 100k tokens, and IEA's measured
  per-task figures span 0.3 Wh (small text model) to 5 Wh (medium text model) to
  115 Wh (a 6-second video). The two sides often mean different models and tasks.

- **"Training one model = five cars."** Strubell's five-car row is the neural
  architecture search (626,155 lbs = 284 tCO2e), not training a Transformer, which
  is 192 lbs. Patterson corrects the NAS estimate by 88x (actual ~3.2 tCO2e),
  attributing the gap to a proxy-task misunderstanding and to efficient datacenters,
  and notes NAS is run once per problem-domain, not once per model. The popular
  press attached the five-car figure to ordinary model training.

- **Grid and boundary swamp the per-run number.** The same-size model varies wildly:
  GPT-3 at 552 tCO2e (US-average grid, Patterson) vs BLOOM at 25 tCO2e (French
  57 gCO2eq/kWh grid) for comparable scale. Patterson's Iowa net figure (0.080
  kg/kWh) is ~5x below the US average (0.429). Any per-run carbon claim without a
  grid and a boundary is unfalsifiable.

- **Efficiency counterpoint vs measured aggregate growth.** Masanet et al. (Science
  2020, via Patterson) found global datacenter energy rose only ~6% over 2010-2020
  while compute grew ~550%; Patterson reports sparse models at <1/10th the energy of
  dense ones and up to 100-1000x reducibility. Against that, the IEA measures
  data-centre electricity growing ~12%/year since 2017 and doubling to ~945 TWh by
  2030. Efficiency per unit has improved fast; total load has still risen fast. Both
  are true, and the argument turns on which the reader weighs.

- **IEA scope mismatch across editions.** Electricity 2024 reports ~460 TWh in 2022
  (data centres, AI and crypto); Energy and AI 2025 reports ~415 TWh in 2024 (data
  centres, ~1.5% of world electricity). The later, lower base year is not a decline;
  it is a narrower boundary (crypto, at ~110 TWh in 2022, is counted separately).
  Any TWh aggregate has to state whether crypto and transmission networks are in it.

## Numbers

```text
Figure: Transformer (big), trained once: 192 lbs CO2e (~87 kg)
Owner:  Strubell et al. 2019, Table 1/Table 3
Scope:  Single training run; 84 P100-GPU-hours; PUE 1.58; US EPA average grid (0.954 lbs/kWh); 2019 estimate
```
```text
Figure: Neural architecture search (Evolved Transformer): 626,155 lbs CO2e = 284 metric tons
Owner:  Strubell et al. 2019, Table 1 (Patterson restates as 284 tCO2e)
Scope:  Full NAS, 979M training steps / 274,120 P100-GPU-hours; the "~5 car-lifetimes" figure; 2019 estimate later corrected 88x
```
```text
Figure: Evolved Transformer NAS, corrected: ~3.2 tCO2e (net)
Owner:  Patterson et al. 2021, Table 4 / Sec 4.1
Scope:  Actual search on Google TPU v2, Google Georgia datacenter; corrects Strubell 284 tCO2e by 88x (18.7x from proxy-task error)
```
```text
Figure: GPT-3 training: 552.1 net tCO2e; 1,287 MWh
Owner:  Patterson et al. 2021, Table 4
Scope:  175B params; Microsoft Azure, US-average grid 0.429 kg CO2e/kWh; V100; ran 2020. (BLOOM authors independently infer ~502 t for GPT-3.)
```
```text
Figure: BLOOM training: 24.69 tCO2eq (dynamic only) / 50.5 tCO2eq (life-cycle)
Owner:  Luccioni et al. 2022, Sec 4.2 / Table 3
Scope:  176B params; 433,196 kWh; French grid 57 gCO2eq/kWh; life-cycle = embodied 11.2 + dynamic 24.69 + idle 14.6; 2022
```
```text
Figure: BLOOM inference (API): ~340 kg CO2eq over 18 days; ~19 kg/day
Owner:  Luccioni et al. 2022, Sec 4.4
Scope:  16 A100s on GCP us-central1 (394 gCO2eq/kWh); 230,768 requests (~558/hr); 914 kWh; ~75% of energy for in-memory model
```
```text
Figure: GPT-4 training: ~42.4 GWh total; ~0.43 GWh/day
Owner:  IEA Energy and AI 2025, Ch.1 p.44 (from EpochAI 2024, Shehabi 2024)
Scope:  ~25,000 GPUs, ~22 MW equipment, ~14 weeks, 84% load factor
```
```text
Figure: Per-query/per-task energy: 0.3 Wh (small text model) to 5 Wh (medium text model); image 1.7 Wh; video 115 Wh
Owner:  IEA Energy and AI 2025, Fig 1.16 (with S. Luccioni), measured under test conditions
Scope:  GPU energy per single inference task; excludes non-GPU overhead; phone charge ~15 Wh for scale
```
```text
Figure: Per-query energy, viral: ~2.9-3 Wh ("10x a Google search")
Owner:  de Vries 2023 (via SemiAnalysis Feb 2023); repeated by IEA Electricity 2024
Scope:  Assumed 4,000 in / 2,000 out tokens on A100; superseded 10x by Epoch (see below)
```
```text
Figure: Per-query energy, corrected: ~0.3 Wh (typical GPT-4o); ~0.34 Wh (Altman)
Owner:  Epoch AI / Josh You, Feb 2025
Scope:  ~500 output tokens, ~100B active params, H100; rises to ~2.4 Wh at 10k-token input, ~40 Wh at 100k tokens; excludes image/video
```
```text
Figure: Data-centre electricity: 415 TWh in 2024 (~1.5% of world); projected ~945 TWh by 2030 (Base Case)
Owner:  IEA Energy and AI 2025, Executive Summary
Scope:  Data centres excluding crypto; ~12%/yr growth since 2017; 2030 range 670 (Headwinds) / 800 (High Efficiency) / 945 (Base) / 1,260+ (Lift-Off); 2035 spread 700-1,720 TWh; ~Japan's current total at 945
```
```text
Figure: Data-centre electricity (earlier edition): ~460 TWh in 2022 (~2%); projected >1,000 TWh by 2026
Owner:  IEA Electricity 2024 (recorded via reporting; primary bot-gated)
Scope:  Data centres, AI AND crypto combined; crypto ~110 TWh in 2022 rising >40% to ~160 TWh by 2026
```
```text
Figure: AI electricity growth: +85-134 TWh/year by 2027; Google-AI worst case ~29.3 TWh/year (~Ireland)
Owner:  de Vries 2023, Joule (recorded via reporting; primary bot-gated)
Scope:  Based on projected NVIDIA AI-server shipments; ChatGPT inference ~564 MWh/day
```

## Limits

- **Water per query has no verified primary number.** No source I opened owns a
  per-query or per-training water figure. The IEA report treats water only as
  auxiliary cooling load, without a headline per-task figure. The commonly quoted
  "~500 mL per ChatGPT exchange" traces to Li et al., "Making AI Less Thirsty,"
  which I did not open and cannot vouch for. The commission asks for water figures;
  I could not establish one from a primary, and the writer should treat water as an
  acknowledged disclosure gap, not assert a number.
- **The de Vries (2023) Joule primary is bot-gated.** cell.com and sciencedirect
  returned 403/CAPTCHA to every route tried. Its projection figures (85-134 TWh by
  2027; ~29.3 TWh Google-AI worst case; 564 MWh/day ChatGPT) are recorded from
  cross-checked reporting and from Epoch AI's characterization of its method, not
  from my own reading of the paper. Treat these as attributed, not verified in situ.
- **The IEA aggregate is measured but the projection is a scenario, not a
  measurement.** The 415 TWh 2024 figure is IEA's estimate for a base year; the 945
  TWh 2030 figure is a Base Case among four cases that span 670-1,260 TWh at 2030 and
  700-1,720 TWh by 2035. The commission's "measured but uncertain" framing holds:
  measured base, wide projected band.
- **Grid-carbon base years differ across the training-carbon sources.** Strubell
  uses a 2018 US grid, Patterson a 2020-2021 grid, BLOOM a 2022 French grid. Cross-
  model carbon comparisons carry that mismatch; energy (kWh/MWh) is the cleaner
  cross-source unit, carbon the grid-dependent one.
- Everything else the brief asked for (training-carbon headline and its misquote,
  the per-unit vs aggregate split with numbers on both sides, one traced-and-
  corrected viral per-query figure, the aggregate anchor with base year and range,
  the efficiency counterpoint) is established from primaries.

## Source assets

```text
Asset: IEA Energy and AI 2025, data-centre electricity consumption to 2030/2035 (Executive Summary chart; Chapter 2 Base/Lift-Off/High Efficiency/Headwinds cases)
Shows: The measured 2024 level and the projected doubling, with the scenario band that makes "uncertain but measured" visible in one image.
Crop:  Must retain the 2024 base value, the case labels, and the y-axis unit (TWh); may omit region splits.
```
```text
Asset: IEA Energy and AI 2025, Figure 1.16/1.17, GPU energy per inference task (text small/medium, image, video) under test conditions
Shows: That "per query" is not one number: it ranges from 0.3 to 115 Wh by model size and task, which is the per-unit half of the argument.
Crop:  Must retain the task labels and the Wh scale (note it is often log); keep the phone-charge reference if shown.
```
```text
Asset: Patterson et al. 2021, Figure 1 (CO2e improvement, Transformer-on-P100-US-avg vs Evolved-Transformer-on-TPU-Iowa; 57X total, per-step gains)
Shows: How model, chip, datacenter, and grid each multiply down a training run's carbon; the visual case that per-run carbon is a choice, not a constant.
Crop:  Must retain the four step labels and the cumulative multiplier; note the y-axis is log.
```
```text
Asset: Strubell et al. 2019, Table 1 (CO2e of models vs familiar consumption: air travel, human/American life, car lifetime)
Shows: The original comparison that launched the debate, including the NAS row (626,155 lbs) beside the car-lifetime row (126,000 lbs) that produced "five cars."
Crop:  Must keep both the "Transformer (big) 192" and "w/ neural arch. search 626,155" rows so the misquote is legible; omit nothing between them.
```
```text
Asset: Luccioni et al. 2022, Table 3 (BLOOM life-cycle split: embodied 11.2 / dynamic 24.69 / idle 14.6 = 50.5 t)
Shows: How much the accounting boundary changes a single answer, one model, doubling depending on what you count.
Crop:  Must retain all three rows and the total with their percentages.
```

## Discarded

```text
URL: https://ahmdtaha.medium.com/energy-and-policy-considerations-for-deep-learning-in-nlp-... — blog summary of Strubell; superseded by the ACL primary.
URL: https://www.sciencedaily.com/releases/2023/10/231010133607.htm — de Vries press release; the DownToEarth report already carries the same figures with the country comparison.
URL: https://www.eurekalert.org/news-releases/1003775 — same de Vries press release, duplicate of ScienceDaily; two retellings of one origin count as one.
URL: https://birchtree.me/blog/... — personal blog on the Epoch correction; the Epoch primary and TechCrunch cover it.
URL: https://ehsanyousefzadehasl.medium.com/... — Medium summary of Patterson; superseded by the arXiv primary.
URL: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai — same report as the PDF I opened; recorded once via the full text.
```

# Evidence: the-instruments/energy-per-query

This record supports the commission's central claim: the same "energy per
AI query" number has been reported at roughly 3 Wh (de Vries, 2023) and
roughly 0.3 Wh (Epoch AI, 2025), a genuine 10x gap between two honest,
first-hand-read estimates, and the gap is explained by stacked, nameable
modeling choices (output-token count, active-parameter count, chip
generation, and peak vs. utilization-adjusted power), not by one side being
wrong. All primary numbers below were read in the original document, not
in a summary, and the arithmetic in each was independently recomputed and
checked against the source's own stated inputs. The water-figure case is
equally strong: Li et al.'s per-request figure is exactly reproducible from
their own published table, and Google's 2025 self-report explicitly frames
its low number as coming from a smaller, differently-measured energy base,
not an apples-to-apples water comparison. The evidence is thin in one
place: the IEA's own report page could not be opened directly (Cloudflare
bot-challenge, confirmed across three pages and multiple browser user
agents), so the context scale-figure rests on secondary corroboration
only, clearly flagged below. The "Google search = 10x" origin claim is
solidly two-sourced (de Vries's own paper plus the Reuters wire report it
draws on), satisfying the two-independent-confirmation bar for the
specific claim that Alphabet's chairman, not Google's engineering team,
supplied the "10x" figure.

## Sources

### 1. Epoch AI, "How much energy does ChatGPT use?" (Josh You, Feb 7, 2025)
URL: https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
(resolves, HTTP 200, fetched directly; byline: Josh You, "with substantial
help from Alex Erben and Ege Erdil")

**Classification: primary.** Epoch AI is an independent AI research
nonprofit; it owns this specific reanalysis and its underlying spreadsheet
of assumptions. It is not a provider reporting on its own product, so it
carries no direct financial stake, though its explicit thesis — that the
"3 Wh" figure other people cite is an overestimate — is the article's own
point to prove, a mild motivated-reasoning risk worth naming even though
it is not commercial.

**What it establishes first-hand:** a bottom-up (FLOPs × tokens × chip
efficiency) estimate that a typical GPT-4o query on ChatGPT costs
**~0.3 Wh**. Exact assumption chain, quoted:
- Active parameters: "We previously estimated that GPT-4o has roughly 200
  billion total parameters (likely between 100 and 400 billion)... we'll
  use a 4 to 1 ratio and assume that GPT-4o has 100B active parameters
  against 400B total parameters" (mixture-of-experts architecture,
  pessimistically taking the high end of the total-parameter range).
- Compute per token: "generating a token requires approximately two FLOP
  for every active parameter... 2 * 100 billion = 200 billion FLOP are
  needed to generate one token."
- Output length: "I assume that a typical number of output tokens per
  query is 500 tokens (~400 words, or roughly a full page of typed
  text). This is somewhat pessimistic — for example, Chiang et al. found
  an average response length of 261 tokens [and, elsewhere in the same
  piece, 269 tokens] in a dataset of chatbot conversations." → "500 * 2 *
  100 billion = 1e14 FLOP for a GPT-4o query with 500 output tokens."
- Chip: "I assume that OpenAI uses Nvidia H100 GPUs for ChatGPT
  inference. These have a power rating of 700 watts, but H100 clusters
  can consume up to ~1500 W per GPU due to the overhead costs of servers
  and data centers... H100s can perform up to 989 trillion (9.89e14) FLOP
  per second."
- Utilization: "I use 10% as a rough estimate of typical utilization
  rates for inference clusters," and separately "GPUs can't actually
  achieve their max FLOP/second output in practice... [one estimate]
  suggest[s] around 70% of peak power on average" — a power-utilization
  factor distinct from the compute-utilization factor.
- Final arithmetic, quoted exactly: "one second of H100-time per query,
  1500 watts per H100, and a 70% factor for power utilization gets us
  1050 watt-seconds of energy, which is around 0.3 watt-hours per query.
  This is around 10 times lower than the widely cited 3 watt-hour
  estimate!" (Independently recomputed: 1050 Ws ÷ 3600 s/h = 0.2917 Wh —
  checks out.)

**Its critique of de Vries, quoted exactly:** "The most important reason
our estimate differs is that we use a more realistic assumption for the
number of output tokens in typical chatbot usage. We also base our
estimate on a newer and more efficient chip (NVIDIA H100 vs A100), and a
model with somewhat fewer active parameters. In the original estimate, De
Vries cites a February 2023 estimate from SemiAnalysis of the compute cost
of inference for ChatGPT. This calculation assumed 175B parameters for
GPT-3.5 (vs our assumed active parameter count of 100B for GPT-4o),
running on A100 HGX servers (less efficient than the more modern H100),
and most importantly, assumed 4000 input tokens and 2000 output tokens per
query. This is equivalent to 1500 words, which is likely quite
unrepresentative of typical queries... De Vries then converts this compute
cost to energy using the A100 server's max power capacity of 800 W
p[er GPU]" — i.e., de Vries's chain used peak power, not a utilization- or
power-draw-adjusted average.

**On the "10x a Google search" claim, quoted exactly:** "A commonly-cited
claim is that powering an individual ChatGPT query requires around 3
watt-hours of electricity, or 10 times as much as a Google search... we
believe that this figure of 3 watt-hours per query is likely an
overestimate." And in the footnotes: "The comparison with Google searches
comes from a very old estimate from Google in 2009 that each search
consumes 0.3 Wh. Estimating Google search's energy cost today is outside
the scope of this post. It could easily be lower today due to increased
chip and data center efficiency, or higher if Google searches have
b[ecome more complex, e.g. with AI features]." Epoch does not itself
re-estimate today's Google-search energy cost — it only flags that the
2009 baseline is stale.

**Everyday comparisons, quoted exactly:** "0.3 watt-hours is less than
the amount of electricity that an LED lightbulb or a laptop consumes in a
few minutes... The average US household uses 10,500 kilowatt-hours of
electricity per year, or over 28,000 watt-hours per day."

**Locators:** main body (assumption walkthrough), footnote/"Notes"
section (Google-search caveat), no in-article chart or table — the
detailed spreadsheet is referenced but not independently opened by this
researcher, so it is not cited as read.

### 2. Alex de Vries, "The growing energy footprint of artificial intelligence," Joule 7(10):2191–2194, Oct 18, 2023
Canonical URL (resolves, HTTP 200): https://doi.org/10.1016/j.joule.2023.09.004
(redirects to the Cloudflare-gated cell.com page; full text read via a
mirror PDF at https://asociace.ai/wp-content/uploads/2023/10/ai-spotreba.pdf,
which reproduces the publisher's exact "Commentary" formatting, author
bio, DOI header, figure, and reference list — verified against the
citation record, not a paraphrase)

**Classification: primary.** De Vries's own peer-reviewed commentary; he
is founder of Digiconomist, a firm whose stated mission is "exposing the
unintended consequences of digital trends" — an independent-researcher
advocacy stance (skeptical-of-tech-hype bias), not a commercial stake in
any AI provider.

**What it establishes first-hand:** de Vries does not assert one single
point estimate for ChatGPT; he presents two convergent derivations that
later coverage flattened into "de Vries said 3 Wh":
- **Derivation A (top-down from SemiAnalysis hardware data), quoted
  exactly:** "Research firm SemiAnalysis suggested that OpenAI required
  3,617 of NVIDIA's HGX A100 servers, with a total of 28,936 graphics
  processing units (GPUs), to support ChatGPT, implying an energy demand
  of 564 MWh per day." Then: "This figure aligns with SemiAnalysis'
  assessment of ChatGPT's operating costs in early 2023, which estimated
  that ChatGPT responds to 195 million requests per day, requiring an
  estimated average electricity consumption of 564 MWh per day, or, **at
  most, 2.9 Wh per request**." (Recomputed: 564,000,000 Wh ÷ 195,000,000
  requests = 2.892 Wh — checks out.)
- **Derivation B (the "10x a Google search" claim), quoted exactly:**
  "Alphabet's chairman indicated in February 2023 that interacting with
  an LLM could 'likely cost 10 times more than a standard keyword
  search.' As a standard Google search reportedly uses 0.3 Wh of
  electricity, this suggests an electricity consumption of approximately
  **3 Wh per LLM interaction**." De Vries treats A and B as confirming
  each other ("This figure aligns with...").
- Figure 1 (page 3 of the PDF), a bar chart titled "Estimated energy
  consumption per request for various AI-powered systems compared to a
  standard Google search," plotting: Google search (0.3 Wh), ChatGPT
  (~2.9 Wh), BLOOM (~3.96 Wh), AI-powered Google search per New Street
  Research (~6.9 Wh), AI-powered Google search per SemiAnalysis (~8.9
  Wh) — all five on one Wh-per-request y-axis.
- BLOOM figure, quoted: "Hugging Face's BLOOM model, which consumed 914
  kWh of electricity for 230,768 requests, averaging to 3.96 Wh per
  request." (Recomputed: 914,000 ÷ 230,768 = 3.961 Wh — checks out.)
- AI-powered Google-search scenario, quoted: "SemiAnalysis estimated that
  implementing AI similar to ChatGPT in each Google search would require
  512,821 of NVIDIA's A100 HGX servers... At a power demand of 6.5 kW per
  server, this would translate into a daily electricity consumption of 80
  GWh and an annual consumption of 29.2 TWh... Google currently
  processing up to 9 billion searches daily, these scenarios would
  average to an energy consumption of 6.9–8.9 Wh per request." New Street
  Research's independent estimate: "approximately 400,000 servers...
  daily consumption of 62.4 GWh." (Both recomputed and checked: 80,000
  MWh ÷ 9B = 8.89 Wh; 62,400 MWh ÷ 9B = 6.93 Wh.)
- Global 2027 projection, quoted: NVIDIA "could be shipping 1.5 million
  of its AI server units" by 2027, with "these machines could have a
  combined power demand of 9.75–15.3 GW. Annually, this quantity of
  servers could consume **85.4–134.0 TWh of electricity**." Compared
  against "historical estimated annual electricity consumption of data
  centers, which was 205 TWh" (his citation, not independently verified
  by this researcher beyond de Vries's own citation of Patterson et al.
  2022).
- Explicitly invokes Jevons' Paradox as a reason efficiency gains might
  not reduce total AI energy use.

**Locators:** "AI and energy consumption" section (training vs.
inference definitions), "Future energy footprint development" section
(the SemiAnalysis/Hennessy numbers and Figure 1), references 5, 6, 9 (for
SemiAnalysis, Reuters, and the 2009 Google post respectively).

### 3. SemiAnalysis, "The Inference Cost of Search Disruption – Large Language Model Cost Analysis" (Feb 9, 2023)
URL (resolves, HTTP 200): https://www.semianalysis.com/p/the-inference-cost-of-search-disruption
(mirror also live at https://newsletter.semianalysis.com/p/the-inference-cost-of-search-disruption)

**Classification: primary.** This is the original hardware/cost model
that both de Vries and (by Epoch's account) the "2,000 output tokens"
assumption trace back to. SemiAnalysis is an independent semiconductor/AI
industry-analysis publication; it has a commercial interest in being
seen as an authoritative, headline-generating source (subscription
business), though no direct stake in OpenAI's or Google's numbers.

**What it establishes first-hand:** OpenAI needs "approximately 3,617
HGX A100 servers" (28,936 A100 GPUs) to serve ChatGPT, at an estimated
"$694,444 per day" in compute hardware cost. Usage assumptions: 13
million daily active users × 15 responses per user (≈195 million
requests/day — the same figure de Vries uses); **input sequence length
of 4,000 tokens, average output of 2,000 tokens per response**; implied
cost per query ≈ 0.36 cents. This 2,000-output-token assumption is the
single largest lever in the de Vries/Epoch gap (Epoch uses 500).

**Locators:** main body cost-model section; the authors themselves flag
"several unknown variables" and invite challenge to their assumptions.

### 4. Li, Yang, Islam, Ren, "Making AI Less 'Thirsty': Uncovering and Addressing the Secret Water Footprint of AI Models," arXiv:2304.03271v5 (originally submitted Apr 6, 2023; this revision Mar 26, 2025)
URL (resolves, HTTP 200): https://arxiv.org/abs/2304.03271 (full text read
directly from the PDF, https://arxiv.org/pdf/2304.03271)

**Classification: primary.** Authors' own methodology paper (UC
Riverside / UT Arlington researchers); an academic paper with an
explicit advocacy stance ("we advocate for a holistic approach to
sustainable AI") but no commercial stake in any AI provider.

**What it establishes first-hand, quoted exactly:** "training the GPT-3
language model in Microsoft's state-of-the-art U.S. data centers can
directly evaporate 700,000 liters of clean freshwater" (of 5.4 million
liters total including embodied training energy elsewhere) and "GPT-3
needs to 'drink' (i.e., consume) a 500ml bottle of water for roughly 10 –
50 medium-length responses, depending on when and where it is deployed."

**Method, quoted:** for inference, "we consider a medium-sized request,
each with approximately ≤800 words of input and 150–300 words of
output... The official estimate indicates that GPT-3 consumes an order of
0.4 kWh of electricity to generate 100 pages of content, equivalent to
roughly 0.004 kWh per page [OpenAI's own figure, uncredited beyond
'official estimate']... To account for both the prompt phase and the
non-GPU energy consumption of servers, we assume a per-request server
energy consumption of 0.004 kWh [4 Wh] for our conversation task." Water
is then computed as energy × (on-site WUE + PUE × off-site EWIF), using
Microsoft's own published location-level PUE and WUE figures.

**Explicit scope definitions, quoted:** "Water withdrawal: freshwater
taken from the ground or surface water sources... Water consumption: ...
'water withdrawal minus water discharge' ... AI's water usage spans three
scopes: on-site water for data center cooling (scope 1), off-site water
for electricity generation (scope 2), and supply-chain water for server
manufacturing (scope 3)." Off-site WUE is explicitly defined as "the
electricity water intensity factor (EWIF)."

**Table 1 (location-by-location breakdown), key rows (PUE / on-site WUE
L-per-kWh / off-site EWIF L-per-kWh / total water per request in mL / #
of 500ml-bottle-equivalent requests):**
- U.S. Average: PUE 1.170, on-site WUE 0.550, EWIF 3.142 → total water
  16.904 mL/request → 29.6 requests per 500 mL.
- Washington: PUE 1.150, on-site WUE 0.950, EWIF 9.501 → total water
  47.506 mL/request → 10.5 requests per 500 mL (highest water use).
- Texas: PUE 1.280, on-site WUE 0.250, EWIF 1.287 → total water 7.590
  mL/request → 65.9 requests per 500 mL (among the lowest).
- Ireland: total water 7.107 mL/request → 70.4 requests per 500 mL
  (lowest of all 18 locations listed).

**Explicit conservatism caveat, quoted:** "Our estimate of inference
water consumption for GPT-3 is on the conservative side, and the actual
water consumption could be several times higher. Specifically... the
inference server energy consumption for a much smaller model (e.g.,
Llama-3-70B) is already approximately 0.010 kWh per medium-sized request
[2.5x their GPT-3 assumption]... For the Falcon-180B model... approximately
0.016 kWh per medium-sized request [4x]." Also: "some subsequent models
like GPT-4 could consume substantially more energy and water than GPT-3
for processing the same request."

**Global 2027 projection, quoted:** citing de Vries [ref 7] for "85 – 134
TWh of electricity in 2027," the paper derives "the combined scope-1 and
scope-2 water withdrawal of global AI is projected to reach **4.2 – 6.6
billion cubic meters** in 2027... more than the total annual water
withdrawal of 4 – 6 Denmark or half of the United Kingdom," and water
*consumption* (evaporated) of "0.38 – 0.60 billion cubic meters."

**Locators:** Abstract; Section 2.1–2.2 (scope definitions); Section 3.3
and Table 1 (the case study and per-request numbers); Appendix
(the 2027 global projection arithmetic).

### 5. Sam Altman, "The Gentle Singularity," blog.samaltman.com (June 2025)
URL (resolves, HTTP 200, fetched directly): https://blog.samaltman.com/the-gentle-singularity

**Classification: primary, but interest-laden.** OpenAI's CEO writing
about his own company's flagship product's environmental footprint on
his personal blog, with an evident interest in a small, reassuring
number and zero disclosed methodology. No date-stamp is exposed on the
page itself; June 2025 is corroborated by Google's own paper, which
cites it as "Sam Altman. The gentle singularity, June 2025."

**Exact quote, verified against the live page:** "People are often
curious about how much energy a ChatGPT query uses; the average query
uses about 0.34 watt-hours, about what an oven would use in a little
over one second, or a high-efficiency lightbulb would use in a couple of
minutes. It also uses about 0.000085 gallons of water; roughly one
fifteenth of a teaspoon." (0.000085 gallons ≈ 0.322 mL, using 1 gal =
3,785.41 mL.)

No model version, no mean-vs-median distinction, no measurement boundary
(training amortization? idle machines? data-center overhead?), and no
denominator (single query of what length?) is disclosed anywhere in the
post. This absence is independently confirmed as a real gap, not just
this researcher's complaint — see source 6 below, which flags the exact
same absence.

### 6. Elsworth, Huang, Patterson, Schneider, Sedivy, Goodman, Townsend, Ranganathan, Dean, Vahdat, Gomes, Manyika (Google), "Measuring the environmental impact of delivering AI at Google Scale" (Aug 2025)
URL (resolves, HTTP 200): https://arxiv.org/abs/2508.15734; full text read
from https://services.google.com/fh/files/misc/measuring_the_environmental_impact_of_delivering_ai_at_google_scale.pdf

**Classification: primary, but interest-laden.** Google's own
measurement of its own Gemini product, authored by Google Research and
infrastructure staff (including Jeff Dean and David Patterson). Strong
incentive to present the lowest defensible number and to frame prior
literature as overestimating — but unusually transparent about its own
methodology and its own two internal numbers (0.10 vs 0.24 Wh) differing
2.4x depending only on what gets counted, which cuts against a reading
of pure spin. Also functions as a secondary compilation of five other
providers'/researchers' figures (summarized below), each of which this
researcher has NOT independently verified beyond what Google's paper
states — flagged accordingly.

**Its own finding, quoted:** "the median Gemini Apps text prompt
consumes 0.24 Wh of energy — a figure substantially lower than many
public estimates... the median Gemini Apps text prompt uses less energy
than watching nine seconds of television (0.24 Wh) and consumes the
equivalent of five drops of water (0.26 mL)."

**Its own measurement-boundary sensitivity, quoted and tabulated (Table
1, May 2025 data):**
| Approach | Active AI Accelerators | CPU & DRAM | Idle Machines | Overhead | **Total Wh/prompt** |
|---|---|---|---|---|---|
| "Existing" (narrow, matches literature convention; top-10%-most-efficient DCs only) | 0.10 | (0.04, excluded) | (0.02, excluded) | (0.01, excluded) | **0.10** |
| "Comprehensive" (fleet average, full stack) | 0.14 | 0.06 | 0.02 | 0.02 | **0.24** |

Water: 0.12 mL (existing) vs. 0.26 mL (comprehensive). Emissions: 0.02
vs. 0.03 gCO2e. WUE used: "For both 2023 and 2024, Google's WUE Category
2 value was 1.15 L/kWh." Quoted: "This suggests that a scaling of 1.72
would need to be applied to active AI accelerator energy consumption to
include the energy consumed in a production serving environment... The
comprehensive approach reveals a total energy consumption that is 2.4
times greater than the estimate from the existing approach."

**Efficiency-gain claim, quoted:** "a 33x reduction in energy
consumption and a 44x reduction in carbon footprint for the median
Gemini Apps text prompt over one year" (May 2024 to May 2025), broken
down as "23x reduction from model improvements, and a 1.4x reduction
from improved machine utilization" plus clean-energy procurement effects
on emissions.

**Its water-comparison framing, quoted exactly (important caveat the
writer should preserve):** "The water use of 0.26 mL equals five drops
of water (based on a standard 0.05 mL drop), orders of magnitude less
than previous estimates of 45 [Mistral] to 50 mL [Li et al.]." This
comparison is offered without controlling for the fact that Google's own
energy-per-prompt figure (0.24 Wh) is itself roughly an order of
magnitude below Li et al.'s implicit ~4 Wh-per-request GPT-3 assumption
— so a large share of the water gap could follow mechanically from the
smaller energy base, not from water efficiency alone; the paper does not
separate these two effects.

**Its own catalogue of other estimates (Section 2.1, "Estimated
metrics" — read directly, but the underlying five source documents were
NOT independently opened by this researcher except where separately
listed above):**
- "De Vries, 2023: ...results suggest that a single GPT-3.5 prompt may
  consume around 3 watt-hours (Wh) of energy." (Independently verified —
  see source 2.)
- "Epoch.AI, 2025: ...The energy consumption of a typical ChatGPT prompt
  is estimated to be approximately 0.3 Wh." (Independently verified —
  see source 1.)
- "EcoLogits: ...For a small (50 output token) prompt, the EcoLogits
  calculator estimates a range from 1.83 Wh to 6.95 Wh." (NOT
  independently verified by this researcher — reported only as it
  appears in Google's paper.)
- "Li et al., 2025: ...approximately 10-50 mL per prompt." (Independently
  verified — see source 4.)
- "Sam Altman, 2025: ...0.34 Wh... 0.000085 gallons, or 0.3 mL. The
  disclosure provides no explanation of the measurement boundary or
  methodology used to arrive at this number, making it impossible to
  compare with other estimates." (Independently verified — see source
  5; Google's characterization of the missing methodology matches what
  this researcher found directly.)
- "Mistral AI, 2025: A peer-reviewed lifecycle assessment (LCA)... For a
  typical 400-token response... 1.14 grams of CO2e, and 45 milliliters
  (mL) of water consumed." (NOT independently verified by this
  researcher — no Wh figure is given in what Google reports, so this
  number is not on the same energy axis as the others; usable only for
  the water table, and flagged as second-hand.)
- Also reports two directly-measured (not estimated) academic figures:
  "Luccioni et al., 2022: ...4 Wh/prompt and 1.5 gCO2e/prompt" for BLOOM
  (measured via CodeCarbon over 18 days, no batching), and "Samsi et al.,
  2023: ...approximately 0.3 Wh per response" for LLaMA-65B.

**Locators:** Abstract; Section 2.1 (catalogue of other estimates,
Related Work); Section 3 (methodology, PUE/WUE formulas); Section 4.1–4.2
and Table 1/Table 2 (Google's own results); Figure 2 (cross-provider
comparison chart, see Source assets); Figure 3 (Gemini's own energy
breakdown, see Source assets).

### 7. Google, "Powering a Google search," Official Google Blog (Jan 11, 2009)
URL (resolves, HTTP 200, fetched directly): https://googleblog.blogspot.com/2009/01/powering-google-search.html
Byline confirmed in page HTML: "Posted by Urs Hölzle, Senior Vice
President, Operations"

**Classification: primary, but interest-laden and stale.** Google's own
16-year-old claim about its own product's energy use — the sole origin
of the "0.3 Wh Google search" figure everyone, including de Vries and
Epoch, still cites.

**Exact quote, confirmed in page source:** "...this amounts to 0.0003
kWh of energy per search, or 1 kJ. For comparison, the average adult
needs about 8000 kJ a day of energy from food, so a Google search uses
just about the same amount of energy that your body burns in ten
seconds." (0.0003 kWh = 0.3 Wh — the figure de Vries and every
downstream retelling uses.) The post also gives a carbon-equivalent
figure ("about 0.2 gr[ams]...") not relevant to the energy-per-query
comparison.

**Locator:** main body, the paragraph beginning "Queries vary in degree
of difficulty."

### 8. Jeffrey Dastin and Stephen Nellis, "For tech giants, AI like Bing and Bard poses billion-dollar search problem," Reuters (Feb 22, 2023)
Reuters.com itself returned HTTP 401 (access wall) on direct fetch; the
same wire-service text was read via its syndication mirror at
https://ca.finance.yahoo.com/news/tech-giants-ai-bing-bard-110652362.html
(HTTP 200, fetched directly)

**Classification: secondary.** Reuters is reporting on quotes from
Alphabet's chairman and OpenAI's CEO; it does not own either company's
footprint claim. The quotes themselves function as primary statements
from the companies, carried by a secondary reporter.

**Exact quotes:** "having an exchange with AI known as a large language
model likely cost 10 times more than a standard keyword search" —
attributed to John Hennessy, Alphabet's chairman, in an interview with
Reuters. Separately, Sam Altman (OpenAI CEO) described ChatGPT's
computing costs as "eye-watering," "a couple of cents or more" per
conversation — sourced by the article to Altman's public Twitter posts,
not a direct interview.

This is the second, independent confirmation (alongside de Vries's own
paper, which quotes the same line) that the "10x" claim originated with
Alphabet's chairman specifically, not with any Google engineering
disclosure — satisfying the two-independent-confirmation bar for this
specific attribution.

### 9. IEA "Energy and AI" (April 2025) — context figure only, read second-hand
IEA's own pages (https://www.iea.org/reports/energy-and-ai/executive-summary,
.../energy-demand-from-ai, and its news release) each returned HTTP 403
(Cloudflare bot-challenge) on repeated attempts with multiple realistic
browser user-agent strings; this is a genuine access gate, not a dead
link, but this researcher could not clear it. The PDF URL cited inside
Google's Aug 2025 paper (iea.blob.core.windows.net/.../EnergyandAI.pdf)
returned HTTP 404 (the blob no longer exists).

Numbers instead corroborated via a secondary source read directly:
**Carbon Brief, "AI: Five charts that put data-centre energy use — and
emissions — into context" (Sept 15, 2025)**, URL (resolves, HTTP 200):
https://www.carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context

**Classification: secondary** (science-journalism outlet interpreting
IEA data; read first-hand).

**Quoted:** "data centres are currently responsible for just over 1% of
global electricity demand and 0.5% of CO2 emissions, according to IEA
data" (citing "IEA global energy review 2025"), and "Under the IEA's
central scenario for data-centre growth, the sector's global electricity
consumption would more than double between 2024 and 2030, reaching 945
terawatt-hours (TWh) by the end of the decade."

**Flagged discrepancy:** multiple other secondary summaries (not
independently opened by this researcher; found via search snippets only)
attribute a different, higher figure — ~415 TWh and ~1.5% of global
electricity for 2024 — to the IEA's separate "Energy and AI" report
(April 2025), the same report Google's paper cites as reference [11].
This researcher could not resolve the ~1% vs. ~1.5% discrepancy against
IEA's own text directly; it most likely reflects two different IEA
publications with different scopes or vintages ("Global Energy Review
2025" vs. "Energy and AI"), but this is not confirmed first-hand and
should be presented with that uncertainty intact, or the 945 TWh/2030
figure used alone since it is the one this researcher verified from a
directly-read source.

## Contradictions

**1. De Vries (~2.9–3 Wh) vs. Epoch (~0.3 Wh) — the ~10x gap, both sides
read first-hand.** The gap is not one number being wrong; it is four
compounding, nameable modeling choices, each independently confirmed
against both papers' own text:
- **Output tokens:** SemiAnalysis/de Vries assumed 2,000 output tokens
  per query (SemiAnalysis, Feb 2023, confirmed directly); Epoch assumed
  500 (confirmed directly) — a 4x factor on its own.
- **Active vs. total parameters:** de Vries's chain (via SemiAnalysis)
  used the full 175B GPT-3.5 parameter count as active/dense; Epoch
  assumed a mixture-of-experts model with only 100B of ~400B parameters
  active per token — roughly a 1.75x factor.
- **Chip generation:** A100 (de Vries) vs. H100 (Epoch) — Epoch states
  this as a real efficiency difference but does not give a single clean
  multiplier for chip generation alone in the passage read.
- **Peak vs. utilization-adjusted power:** Epoch's own text states "De
  Vries then converts this compute cost to energy using the A100
  server's max power capacity of 800 W," i.e., peak power with no
  utilization discount; Epoch instead applies both a 10% compute-
  utilization factor and a 70%-of-peak power-draw factor, which lowers
  its own final number substantially relative to a peak-power
  assumption. This is the same "denominator problem" applied twice: once
  to how many output tokens a query produces, once to how efficiently
  the hardware serving it is actually run.

**2. The "de Vries said 3 Wh" popularization vs. what the primary paper
actually says.** De Vries's own text never asserts a single point
estimate. It presents two separate, converging derivations (2.9 Wh from
SemiAnalysis hardware data; ~3 Wh from multiplying the Hennessy "10x"
quote by the 2009 Google figure) and a five-bar chart with values from
0.3 to 8.9 Wh. The flattening of this into "de Vries's 3 Wh number" is a
compression that happened somewhere in secondary retellings, not in the
primary paper itself — worth naming as its own small case of the
denominator problem (which of five bars does "the" number refer to?).

**3. Provider self-report vs. independent estimate — a false
corroboration.** Altman's self-reported 0.34 Wh (June 2025) sits close
to, even slightly above, Epoch's independent 0.3 Wh estimate (Feb 2025)
for the same product family. But Google's own Aug 2025 paper explicitly
states Altman's number "provides no explanation of the measurement
boundary or methodology... making it impossible to compare with other
estimates or to understand which components of the serving stack were
included" — a critique this researcher independently confirmed is
accurate (the blog post genuinely discloses nothing beyond the two
numbers). The numeric proximity to Epoch's figure is very likely
coincidence of magnitude, not confirmation, since neither the model
version, the query mix, nor whether training is amortized in is stated.
Meanwhile Google's own self-report (0.24 Wh comprehensive / 0.10 Wh
narrow) sits below Epoch's independent ChatGPT estimate, and Google's
paper demonstrates, using only its own internal accounting, that varying
the measurement boundary alone (what counts: idle machines, CPU/DRAM,
data-center overhead) swings its own number 2.4x (0.10 vs 0.24 Wh) — a
clean, self-supplied illustration that "per query" hides a boundary
choice, not only a token-count choice.

**4. Water-figure framing dispute.** Li et al.'s 10–50 mL-per-response
figure explicitly sums on-site (scope-1, evaporated at the cooling
tower) and off-site (scope-2, evaporated at the power plant generating
the electricity) water, and varies roughly 20x by location alone in
their own table (7.1 mL in Texas vs. 47.5 mL in Washington state, for
identical PUE/energy assumptions). Google's Aug 2025 self-report (0.26
mL comprehensive) is offered as "orders of magnitude less than previous
estimates of 45 to 50 mL," but this comparison does not hold energy
constant: Google's energy-per-prompt figure (0.24 Wh) is itself roughly
an order of magnitude below the ~4 Wh/request Li et al. assume for
GPT-3, so a large share of the water gap likely follows mechanically
from the smaller energy base rather than from superior water efficiency
alone — Google's paper does not decompose the two effects, and this
researcher could not find a place in either paper that isolates a pure
WUE-only comparison at matched energy. Sam Altman's 0.000085-gallon
(~0.32 mL) figure has no disclosed WUE, cooling technology, or data
center location, so it cannot be checked against Li et al.'s
location-dependent range at all.

**5. IEA context-figure discrepancy** — see Source 9 above (~1% vs.
~1.5% of global electricity for data centres in 2024, from what appear
to be two different IEA publications). Not resolved first-hand; flagged
rather than adjudicated.

## Numbers

### Energy per query/prompt (Wh) — comparable series for a chart
| Value (Wh) | System / "query" definition | Method | Chip / model / year | Owning source |
|---|---|---|---|---|
| 0.3 | Standard Google keyword search | Provider's own internal accounting, no method detail given | Google infrastructure, 2009 | Google, "Powering a Google search" (2009) |
| 2.9 (de Vries: "at most") | ChatGPT / GPT-3.5, one request | Top-down: SemiAnalysis's assumed daily fleet power (564 MWh/day) ÷ assumed daily request volume (195M) | NVIDIA A100 HGX servers, 175B params, early 2023 | de Vries, *Joule* (2023), citing SemiAnalysis (Feb 2023) |
| ~3 (derived, not measured) | "LLM interaction" vs. "standard keyword search" | Multiplies Alphabet chairman's "10x" verbal claim by the 2009 Google 0.3 Wh figure | N/A — not hardware-based | de Vries, *Joule* (2023), quoting Hennessy via Reuters |
| 3.96 | BLOOM (176B params), one inference request | Measured: total metered electricity (914 kWh) ÷ measured requests (230,768) | Unspecified GPUs, BLOOM training-era hardware, 2022 | Hugging Face / Luccioni et al. 2022, as cited by de Vries |
| 6.9 | Hypothetical "AI-powered Google search," one search | Top-down: estimated server fleet (400,000 servers × 6.5 kW) ÷ Google's daily search volume (9B) | NVIDIA A100 HGX, 2023 | New Street Research estimate, as cited by de Vries |
| 8.9 | Hypothetical "AI-powered Google search," one search | Top-down: estimated server fleet (512,821 servers × 6.5 kW) ÷ Google's daily search volume (9B) | NVIDIA A100 HGX, 2023 | SemiAnalysis estimate, as cited by de Vries |
| 0.3 | ChatGPT / GPT-4o, one query, 500 output tokens | Bottom-up: FLOPs/token (2 × active params) × output tokens ÷ chip throughput, with utilization and power-draw discounts | NVIDIA H100, ~100B active / ~400B total params (MoE), 2025 | Epoch AI (Josh You, Feb 2025) |
| 1.83–6.95 | Various models, 50-output-token prompt | Regression model on GPU power vs. LLM performance + average DC PUE | Various, 2025 | EcoLogits, as reported (second-hand) inside Google (2025) |
| 4 | BLOOM, one prompt | Measured (CodeCarbon: GPU+CPU+DRAM), averaged over 18 days, no batching | Multiple A100s, 2022 | Luccioni et al. 2022, as reported inside Google (2025) |
| ~0.3 | LLaMA-65B, one response | Measured benchmark | NVIDIA V100/A100, 2023 | Samsi et al. 2023, as reported inside Google (2025) |
| 0.34 | ChatGPT, "average query" | Provider self-report, no methodology disclosed | Unspecified model/hardware, mid-2025 | Sam Altman blog post (June 2025) — **interest-laden** |
| 0.10 (narrow) / 0.24 (comprehensive) | Gemini Apps, median text prompt | Direct production telemetry; two boundaries: active-accelerator-only (narrow, top-10%-efficient DCs) vs. full-stack fleet average (comprehensive) | Google TPUs/GPUs, May 2025 | Google (Aug 2025) — **interest-laden** |

Not directly comparable on this axis: Mistral AI's July 2025 figure is
reported only in gCO2e (1.14 g for a 400-token response), not Wh, so it
cannot be placed on this table without an assumed grid emissions factor
this researcher did not independently derive.

### Water per query/response (mL) — comparable series for a chart
| Value (mL) | System / denominator | Method | Location dependency | Owning source |
|---|---|---|---|---|
| 10–50 (U.S. average: 16.9) | GPT-3, one "medium-length response" (≤800 input words, 150–300 output words) | Computed: assumed 4 Wh/request server energy × (on-site WUE + PUE × off-site EWIF), using Microsoft's published per-location PUE/WUE | Yes — ranges 7.1 mL (Texas) to 47.5 mL (Washington) across 18 Microsoft datacenter locations in their own Table 1 | Li et al., arXiv:2304.03271 (2023/2025) |
| 45 | Mistral Large 2 "Le Chat," one 400-token response | Peer-reviewed lifecycle assessment (with ADEME, Carbone 4) | Not stated in what was read | Mistral AI (July 2025), as reported (second-hand) inside Google (2025) — **interest-laden, unverified first-hand** |
| ~0.32 (0.000085 gal) | ChatGPT, "average query" | Provider self-report, no methodology disclosed | Not stated | Sam Altman blog post (June 2025) — **interest-laden** |
| 0.12 (narrow) / 0.26 (comprehensive) | Gemini Apps, median text prompt | Computed from measured energy × Google's fleet WUE (1.15 L/kWh, Category 2 consumptive) | Fleet-average only; no per-location breakdown given | Google (Aug 2025) — **interest-laden** |

Flag: the Li et al. figure and the Google/Altman figures are not on a
like-for-like basis even before location is considered — they are for
different model generations (GPT-3 vs. Gemini/ChatGPT-current), and Li
et al.'s number is a computed extrapolation from a borrowed OpenAI
energy figure ("the official estimate indicates that GPT-3 consumes an
order of 0.4 kWh of electricity to generate 100 pages of content"), not
an independent energy measurement of its own.

### Context figure (scale only, NOT comparable to per-query numbers)
- Global data-centre electricity consumption: "just over 1%" of global
  electricity demand in a recent year per "IEA global energy review
  2025," projected to "more than double between 2024 and 2030, reaching
  945 TWh by the end of the decade" under the IEA's central scenario —
  read via Carbon Brief (Sept 2025), IEA's own report page inaccessible
  (see Source 9 and Contradiction 5 for the ~1%/~1.5% discrepancy this
  researcher could not resolve first-hand).
- Global AI-attributable electricity, 2027 projection: 85–134 TWh (de
  Vries's own projection from NVIDIA server-shipment trends, independently
  confirmed in de Vries's paper and re-cited by Li et al.).
- Historical baseline data-centre electricity (de Vries's citation, not
  independently verified beyond his own reference): ~205 TWh/year,
  ~1% of global electricity.

## Source assets

1. **De Vries, *Joule* (2023), Figure 1** ("Estimated energy consumption
   per request for various AI-powered systems compared to a standard
   Google search," page 3 of the read PDF). A single bar chart placing
   Google search (0.3 Wh), ChatGPT (~2.9 Wh), BLOOM (~3.96 Wh), and two
   AI-powered-search scenarios (6.9, 8.9 Wh) on one axis. This is the
   original visual home of the "10x a Google search" comparison the
   entire commission is built around — reproducing or closely modeling
   it would let a reader see exactly which five numbers get compressed
   into "3 Wh" and "10x" in later retellings. A crop must keep the y-axis
   label ("Wh per request"), all five bar labels and values, and the 0–10
   scale; safe to crop out the surrounding body text.

2. **Li et al., Table 1** (page 5 of the read PDF), the 18-location
   breakdown of GPT-3's per-request water cost (PUE, on-site WUE,
   off-site EWIF, total mL per request, requests per 500 mL bottle).
   Shows the location-dependency claim with real numbers rather than
   assertion: the same model, same energy assumption, ranges nearly 7x
   in water cost by where it runs (7.1–47.5 mL/request). A crop must
   retain at minimum the location column, the "Total Water" per-request
   column, and the "# of Requests for 500ml Water" column; the
   PUE/WUE/EWIF intermediate columns can be omitted if space is tight.

3. **Google (Aug 2025), Figure 2** (page 4, "Energy per prompt results
   for large production AI models plotted against LMArena score"). This
   is the single richest visual found in any source: it plots nearly
   every disputed number in this evidence record — GPT-4o (Epoch
   estimate), "Average ChatGPT" (Altman blog estimate), Llama 3.1 70B/405B
   (multiple measured methodologies, showing a 6x spread from
   measurement-boundary differences alone), GPT-3.5 (de Vries estimate),
   and median Gemini (both of Google's own boundaries) — on one
   Prompts-per-kWh axis, color-coded by company, with estimated (gray
   text) visually distinguished from measured (colored text) figures. A
   crop must retain the axis labels ("Prompts per kWh," "Arena Score"),
   the color legend (Meta/OpenAI/Google), and the note "(larger values
   indicate less energy use per prompt)"; must not crop away the
   gray-vs-colored-text distinction, since that is the chart's whole
   point about estimated vs. measured figures.

4. **Google (Aug 2025), Figure 3 / Table 1** (page 5–6), the internal
   breakdown of the 0.24 Wh Gemini prompt into Active AI Accelerators
   (58%), CPU & DRAM (24–25%), Idle Machines (10%), and Overhead (8%). A
   complementary, simpler visual for the "denominator problem applies to
   measurement boundary, not just tokens" point — useful if Figure 2 is
   judged too dense for the piece. Must retain all four segment labels
   with their Wh and percentage values.

## Discarded

- **ResearchGate copy of de Vries (2023):** returned HTTP 403; not read;
  superseded by the asociace.ai mirror PDF, which matches the publisher
  formatting exactly.
- **cell.com / ScienceDirect direct pages for de Vries (2023):**
  Cloudflare bot-challenge (HTTP 403) on repeated attempts with
  realistic browser user-agent strings; the DOI resolves but redirects
  to the same gated page; read via mirror PDF instead (see Source 2).
- **deeprogram.org mirror of de Vries (2023):** resolved (HTTP 200) but
  contained only a bibliography stub with no article text; not used.
- **ui.adsabs.harvard.edu abstract page for de Vries (2023):** fetched
  but returned no usable abstract text; not used.
- **IEA "Energy and AI" report and executive-summary/news pages
  (iea.org):** HTTP 403 (Cloudflare challenge) on three separate pages
  across multiple browser user-agent strings; not read directly. Context
  figure instead sourced from Carbon Brief (see Source 9), with the
  resulting ~1%/~1.5% discrepancy flagged rather than resolved.
- **IEA report PDF linked from Google's Aug 2025 paper's own reference
  list** (iea.blob.core.windows.net/.../EnergyandAI.pdf): returned HTTP
  404 (link rot / blob no longer exists); not used.
- **EcoLogits calculator and Mistral AI's lifecycle-assessment report:**
  not independently opened by this researcher; both figures are used
  only as reported inside Google's Aug 2025 paper, and are explicitly
  flagged as second-hand wherever cited above (not counted toward the
  "primary sources read first-hand" total).
- **reuters.com direct URL for the Dastin/Nellis piece:** returned HTTP
  401 (access wall); read instead via the Yahoo Finance wire-syndication
  mirror (HTTP 200, same wire text).
- **money.usnews.com mirror of the same Reuters piece:** repeated
  connection timeouts/errors on fetch; not used (Yahoo mirror was
  sufficient and resolved cleanly).

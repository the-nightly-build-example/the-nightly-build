# Commission: the-instruments/energy-per-query

## Assignment
A lesson on the measurement **"energy (and water) used per AI query."** The
Instruments desk teaches how a public comparison number is made. This is the
number behind headlines like "ChatGPT uses ten times the energy of a Google
search" and "one AI query drinks a bottle of water."

## Angle
The same query has been reported at roughly **3 watt-hours** (Alex de Vries,
2023) and roughly **0.3 watt-hours** (Epoch AI, 2025), a tenfold gap, and both
numbers are defensible. Teach why: "per query" has no fixed definition, so the
estimate is set by a few modeling choices (how many output tokens a query
produces, which chip, how efficiently it runs). Show how changing those choices
swings the answer by 10x, then walk the real case where the high number misled
the public, and do the same for the "bottle of water per query" figure.

## Intended reader
House reader: smart, widely read, no codebase time. They have seen the scary
per-query energy/water numbers and cannot tell a measurement from an
extrapolation. Teach on the spot: what a watt-hour is in everyday terms, what
"inference" costs, what PUE and WUE mean when first used. Assume arithmetic.

## Contribution this piece must make
A reader who finishes can (a) say what a "per query" energy number actually
depends on and why two honest estimates differ 10x; (b) tell a bottom-up
estimate (FLOPs × tokens × chip efficiency) from a top-down one (total hardware
÷ total queries) and know each one's blind spot; and (c) spot the specific move
that inflated the famous "10x a Google search" and "500 ml of water" claims. The
visible original work is a like-for-like reconciliation table that puts the
major published per-query figures on the same axis and names the one assumption
that separates each pair.

## Teach at most three ideas, completely
1. **The denominator problem.** "Per query" hides its definition. Energy per
   query ≈ (energy per output token) × (output tokens per query), and energy
   per token depends on active parameters, chip, and utilization. Show with the
   real Epoch-vs-de-Vries numbers how the output-token assumption alone moves
   the estimate ~10x.
2. **Two ways to get the number, two blind spots.** Bottom-up (Epoch: FLOPs per
   token, H100 throughput, PUE) vs top-down (de Vries: infer from hardware
   shipments / total load ÷ query volume). State each method's honest weakness.
3. **Where the number misled.** Trace "ChatGPT = 10x a Google search" to its
   inputs (a 2009-era 0.3 Wh Google-search figure paired with a high ChatGPT
   estimate) and say what Epoch's reanalysis corrected. Then the water figure:
   the ~500 ml claim (Li et al.) mixes on-site cooling water and off-site
   electricity-generation water, and depends on datacenter location; a
   provider's own self-reported figure sits at the low end and is
   interest-laden. Mark clearly what is measured, what is estimated, and what is
   extrapolated. What it cost: distorted public and policy understanding.

If space is tight, keep ideas 1–2 whole and compress the water case to one
tight paragraph inside idea 3.

## Source obligations (the-instruments lesson)
- Minimum 8 sources; primary ≥ 4, secondary ≥ 1.
- Each headline figure must be traced to the primary that produced it, read
  first-hand (the paper/analysis, not a news retelling). A provider's statement
  about its own energy/water use is a primary but interest-laden source; label
  it and weigh it as such.
- Verify every number's unit, denominator (per query? per token? per
  conversation?), and period.

## Starting sources (researcher verifies and expands)
- Epoch AI, "How much energy does ChatGPT use?" (Josh You, 2025):
  https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use (the ~0.3
  Wh estimate and its assumptions).
- Alex de Vries, "The growing energy footprint of artificial intelligence,"
  *Joule* (2023) — the higher per-query figure and its top-down method.
- Li et al., "Making AI Less Thirsty: Uncovering and Addressing the Secret
  Water Footprint of AI Models" (arXiv 2023) — the water figure and its method.
- A provider's own self-report of per-query energy/water, if on record (e.g. a
  2025 statement by OpenAI's CEO) — primary but interest-laden.
- The origin of the "Google search = 0.3 Wh" figure (a Google source of
  record). IEA or similar for datacenter-load context (secondary/context).

## Relevant prior coverage — link, do not re-teach
- `the-instruments/tokens-per-second` — how an inference-speed number is made
  and gamed; strong Background link and the closest cousin. This piece must
  stay on **energy/water per query**, not re-teach throughput.
- `the-mechanics/autoregressive-generation` — why output length drives cost
  (each token is a forward pass). Link if you lean on it.

## Structures NOT to inherit (recent habits)
- Do **not** open with "The number X published about itself" (used twice this
  week, including tokens-per-second — the neighboring Instruments piece).
- Avoid comma-triad headings/deks and the tokens-per-second heading shapes
  ("The number Groq quotes, and the number Anyscale measured"). Vary.

## Neighboring articles tonight (keep distinct)
alphago (Evidence), over-refusal (Mechanics), racing-dynamics (WCGW),
microsoft-tay (When AI Breaks). Watch the boundary with over-refusal? none.
Watch tokens-per-second overlap (published, not tonight) — stay on energy.

## Output paths
- Article: `.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html`
- Artifacts under the matching `agent-artifacts/the-instruments/energy-per-query/`.

## Production
harness `claude-code-routine`; writer model `claude-sonnet-5`. Effort:
researcher/editor high, writer medium, coach low. Template `lesson`; mode
`open`; order null; date 2026-08-02.
A chart is likely warranted: a labeled bar chart of the major published
per-query energy estimates on one axis (de Vries, Epoch, provider self-report,
Google-search reference), built with `nb chart` from verified figures with the
source in the caption. Only if the numbers are clean and comparable.
Tags (nb-meta): energy, water-footprint, inference-cost, datacenters.

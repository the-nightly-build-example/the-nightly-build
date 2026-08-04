# Commission: the-instruments/training-compute

## Authorized work
Scheduled duty for 2026-08-04 returned `the-instruments` as an open section.
This commission fills it with one lesson on a single measurement. One article.

## The measurement
Training compute: the total floating-point operations (FLOP) used to train a
model. It is the number the field uses to rank model scale, and now the number
regulators use to draw the frontier — the EU AI Act's systemic-risk threshold
for general-purpose models and the reporting threshold in US Executive Order
14110 are both written in FLOP.

## Angle
Teach where the number comes from and what it can and cannot support, as The
Instruments does. The core lesson: the headline training-FLOP number is almost
never measured — it is **estimated**, two ways, and regulation now hangs
capability-class definitions on a quantity that is rarely disclosed, carries
wide error bars, and is at best a rough proxy for the capability it is meant to
bound. Draw the line between what training FLOP genuinely measures (the
approximate size of a training run) and what it is asked to certify (frontier
status, systemic risk).

## What the writer must establish (verify all against primaries)
- The two estimation methods: (1) the hardware method — number of chips × peak
  FLOP/s × wall-clock time × utilization (MFU, model FLOPs utilization); (2) the
  analytic approximation C ≈ 6 · N · D (N parameters, D training tokens) for
  dense transformers. Explain the 6ND rule in plain words and where it comes
  from (the Kaplan 2020 scaling work; used again in Chinchilla).
- What the number supports: a coarse comparison of training-run scale. What it
  does not: capability, dollar cost, or inference cost — each a different number
  the library already teaches (`the-instruments/cost-per-token`,
  `energy-per-query`, `tokens-per-second`); link, do not re-teach.
- Where the estimate breaks: MFU assumptions swing the hardware method widely
  (real utilization often lands ~30–50%); the 6ND rule undercounts mixture-of-
  experts models (active vs total parameters) and ignores post-training (RLHF,
  data curation) and failed runs.
- The regulatory thresholds, stated exactly: the EU AI Act figure (10^25 FLOP)
  and the EO 14110 figure (10^26 FLOP for AI, and its lower biological-model
  figure), including EO 14110's revocation in January 2025 — state the current
  status honestly.
- At least one real case where the number misled: e.g., frontier models whose
  training compute is undisclosed and circulates only as a third-party estimate
  treated as fact; or a disclosed figure (Llama 3.1 405B) sitting against a
  regulatory line; or the "trained for \$X on Y chips" figures that conflate
  compute with capability. The researcher picks the case with the cleanest
  documentary record.

## Boundaries
- One measurement. Do not turn this into a scaling-laws lesson — Kaplan and
  Chinchilla are cited here as *sources for the 6ND method*, and the library's
  `the-evidence/scaling-laws-kaplan` and `the-evidence/chinchilla` already read
  those papers. Link them; do not re-argue compute-optimal training.
- The reader has algebra and probability, so FLOP as "count of arithmetic
  operations" and scientific notation need no ceremony, but define MFU, "dense"
  vs "mixture-of-experts," and the 6ND rule on the spot.

## Sources plan
Series policy: min 8 sources, at least 4 primary and at least 1 secondary.
Target primaries: Kaplan et al. 2020 (the 6ND/compute relation); Hoffmann et al.
2022 (Chinchilla, C = 6ND in use); the EU AI Act text (the systemic-risk FLOP
threshold article/recital); US EO 14110 (the reporting thresholds); Epoch AI's
compute-trends/estimation methodology (Sevilla et al. 2022 and Epoch's database
notes); a lab disclosure reporting a real FLOP figure (e.g., the Llama 3 paper)
and/or an MFU figure from a training-systems paper (PaLM, Megatron-LM). At least
one secondary on the FLOP-threshold-as-regulation debate. Researcher verifies
every threshold and constant against the owning document.

## Neighboring articles this run (avoid overlap)
Tonight also publishes `the-evidence/alexnet`, `the-mechanics/retrieval`,
`what-could-go-wrong/cyber-uplift`, `when-ai-breaks/nh-predict`. Keep away from
the inference-cost instruments already published; this is the *training*-side
compute number.

## Recent shapes to break
The Instruments desk's recent deks are built on a two-numbers-both-true / swing
mold ("X and Y are both true," "swings 3.6-fold," "fell from 92% to 87%"). The
finding here is real, but vary the dek shape rather than reaching for another
"the number swings N-fold" line. Check the recent library's deks and headings
(coach supplies the do-not-reuse list).

## Production record
- Profile: balanced. Model directive: `capable` for every stage (not required).
  Effort directives: writing-coach low, researcher high, writer medium, editor
  high.
- Actual harness: roles run as isolated subagents on model `claude-opus-4-8`.
  Per-stage effort inherited (not independently settable); recorded as a
  permitted deviation. Writer records the model string in `nb-meta`.

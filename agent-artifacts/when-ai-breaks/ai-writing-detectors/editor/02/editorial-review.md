# Editorial review: when-ai-breaks/ai-writing-detectors (editor/02)

Narrow second read to confirm the single required item from editor/01 is
resolved and nothing regressed. Settled matters from round 01 are not reopened.

## Skeptic

The one item routed to the writer in round 01 was the paraphrase-collapse table's
scale claim: the body lead-in "One common score runs from 50, a coin flip, up to
100, perfect." and the DetectGPT cell "detection score, 50 to 100" both asserted a
floor of 50, contradicted on the same line by DetectGPT's after-value of 25.2, and
the single 50-floor scale fit only the DetectGPT row while the other two rows are
detection rates with a floor of zero.

The fix resolves it, per metric, grounded in Sadasivan (s6):

- Body lead-in (ceiling section) now reads: "The scores below are each out of 100,
  but they are not one scale. DetectGPT's is an AUROC, where 50 is a coin flip and
  a lower score is worse than one; the other two are detection rates, the share of
  AI or watermarked text caught, and their floor is zero." This states the scale
  honestly for each metric and no longer asserts a shared 50-floor.
- DetectGPT "What is scored" cell changed from "detection score, 50 to 100" to
  "detection AUROC, 50 is a coin flip". It names the metric and drops the false
  floor. The 25.2 after-value is now consistent: below 50 reads as worse than a
  coin flip, exactly what the prose now says.
- The OpenAI RoBERTa cell ("AI text caught at a 1% false-alarm setting") and the
  watermarking cell ("watermarked text detected") are detection rates with an
  implicit floor of zero; they never asserted the false 50-floor and are left as-is,
  and the new lead-in now covers them accurately.

Checked each metric against the evidence record's Sadasivan entry. DetectGPT is an
AUROC (50 = chance, lower is worse); the RoBERTa figure is TPR@1%FPR, a detection
rate; the watermark figure is a detection rate. The lead-in's three-way description
matches. None of the six numbers moved: DetectGPT 96.5% -> 25.2%, OpenAI RoBERTa
100% -> 60%, watermarking 99.3% -> 9.7%, all still matching the evidence. No claim
was altered, no number touched, nothing routed.

## Cut

Ran the cut read against spec/slop.md across the two changed sentences and the
DetectGPT cell, and re-read the ceiling section's edges to be sure the reframe
introduced no slop.

- "The scores below are each out of 100, but they are not one scale." carries a
  fact the reader needs to read the table (the columns are not comparable) and
  survives the delete test; without it the per-metric distinction that follows has
  no setup. Not a signpost: it describes the data, not the article's method.
- "DetectGPT's is an AUROC, where 50 is a coin flip and a lower score is worse than
  one; the other two are detection rates, the share of AI or watermarked text
  caught, and their floor is zero." is factual, per-metric, and grammatical. The
  semicolon joins two independent clauses in a clean parallel, not a splice. "worse
  than one" reads cleanly as worse than a coin flip.
- The DetectGPT cell "detection AUROC, 50 is a coin flip" is a factual column
  label, no slop.

No reader address was reintroduced: the round-01 cut of "Watch where the
paraphrase leaves it." stands, and the new lead-in opens on the table, not an
imperative. Confirmed the other three round-01 cuts also still stand: the
orientation signpost, the accusations-section tell, and "The argument is short to
state." are all absent. No new slop, no regression.

## Reader

Read the ceiling section straight through as the paper's reader. The reframed
lead-in makes the table more honest, not less readable: a reader now knows the
three columns are not one scale and can read the 25.2 as worse than chance rather
than as an impossible sub-floor value. The causal account the piece is built on is
untouched. The prose holds the voice-guide register.

## Edits

None. The writer's fix is complete and correct; no prose repair was needed.

## Required work

None. The single blocking item from editor/01 is resolved.

Note for the orchestrator: nb check (no-links) returns BLOCK: 0, WARN: 0, verdict
PUBLISHABLE. The only note is the expected single-file "library state not provided"
line.

## Decision

approve. The table and its prose now state the metric scale honestly per metric,
grounded in Sadasivan, with none of the six numbers changed; the reframe introduced
no slop and nothing else regressed.

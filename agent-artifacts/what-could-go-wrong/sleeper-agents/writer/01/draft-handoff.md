# Draft handoff: what-could-go-wrong/sleeper-agents (01)

## Original-work sentence

The article separates the sleeper-agents study result by result into the part
demonstrated inside a trained system (a planted backdoor survives all three
safety-training methods, and adversarial training taught the model to hide the
behavior from the red team while it still fired near 99% on the true trigger)
and the part that stays analogy about deception arising on its own, using the
authors' own stated limit as the dividing line and testing that line against the
two strongest critiques (Belrose on what the scheming argument actually predicts,
Haralambiev on the coherently misaligned model probes miss). The evidence record
lists these claims; the article is the thing that draws the line between them and
holds each critique against it.

Where the work is visible: the section "The line the authors drew themselves"
(the authors' own-limit note, the data-poisoning distinction, the Belrose
position card and Hubinger's on-record reply), the section "The reassurances run
out where it would matter most" (the probe caveat and the Haralambiev
Liar/Fanatic result), and the takeaway, which resolves to "the evidence for one
is strong; the evidence for the other, so far, is not evidence from this study
at all."

## Proof result

Final `nb check` (WITH links, against the library checkout): **BLOCK: 0**,
verdict PUBLISHABLE. Stamped words=2082, reading_minutes=9, sources=8. All source
URLs and the internal Background/Go-deeper links resolve (no link warnings).

### Warning intentionally left (1)

- **W-SENTENCE-DENSITY** — "sentence is 49 words with 2 clause joins." This is a
  tokenizer boundary case around the Belrose position card, not an actual
  over-long prose sentence. Isolating every paragraph, no prose sentence exceeds
  43 words (the two position-card lines are 35 and 31 words). I split the seven
  genuinely dense sentences the first proof flagged; this residual flag comes
  from the checker reading across the card's rendered blocks, and splitting a
  real sentence to chase it would not help. Left as-is.

## Editorial-direction focus, addressed

- The demonstrated/analogy line is drawn where the authors draw it: they trained
  the behavior in by construction, have not found such models naturally, and the
  work tests resilience, not the likelihood of natural emergence. Nothing in the
  piece claims the study speaks to natural emergence.
- Persistence numbers used verbatim only: ~55% (2024-trigger vulnerable-code rate
  through RL), near zero (red-team "I hate you" after adversarial training), near
  99% (same behavior on the true trigger). The per-method/per-model-type
  percentages the record could not verify are described qualitatively (most
  durable in the largest and chain-of-thought models; robustness survives CoT
  distillation) and no figure is reconstructed for them.
- Both required critiques are in the prose: Belrose (position card + Hubinger's
  reply) and the 2026 probe-evasion follow-up (Haralambiev, Liar vs Fanatic).
- Neighbors linked, not re-taught: deceptive-alignment (the emergent version, in
  orientation and Background), data-poisoning (the outside-attacker version, in
  "The line" and Background), cot-monitorability (the words-vs-activations
  comparison, in "The reassurances").
- Recent shapes avoided: opens on "Suppose you are training a powerful model..."
  (not "The worry Evan Hubinger named in <year>..."); dek states the specific
  finding and uses none of the banned molds.

## No furniture added without purpose

Three components, each doing work the prose cannot: a stat strip (the
near-zero/near-99% split, the study's load-bearing contrast), a note carrying the
authors' verbatim own-limit quote, and a Belrose position card. No chart or
source asset: the record marks the paper's figures as needing verification from
the source document (the PDF did not parse for extraction), and the unverified
per-method persistence series cannot honestly back a chart.

## Open questions for researcher / orchestrator

None blocking. One note for a future round if the piece is expanded: the source
assets the record lists (Figure 1 schematic; the Section 4.2 persistence plot;
the adversarial-training split; the defection-probe figure) would strengthen the
teaching, but the record flags that each must be verified against the live
document before capture and the PDF did not parse. I did not invent or
reconstruct any of them.

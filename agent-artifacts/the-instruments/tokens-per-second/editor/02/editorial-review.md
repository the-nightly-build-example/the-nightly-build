# Editorial review 02 — the-instruments/tokens-per-second (re-review after correction)

## Skeptic
Skeptic: thesis unchanged from 01 ("a bare tokens-per-second figure is
uninterpretable until you name which phase was timed, how many requests
shared the chip, whose tokenizer counted, and what hardware/context produced
it"); tested the two items 01 required — the rebuilt pillar-2 worked example
and the loosened pillar-4 aside — plus the chart; broke: none.

The confound is gone. "More users, less speed each" no longer claims "128
input and 128 output tokens held fixed" or "nothing changed but the request
count." It now opens on MLPerf's own audited Offline/Server/Interactive
series (20 platforms, same model, tightening the latency bound cuts
throughput "roughly a third to two-thirds") and lands the Nebius B200
arithmetic (101,611 → 59,622.7, 41 percent) explicitly labeled by submitter,
sourced to `s5`. I pulled `summary_results.json` directly again and checked
every figure the rebuilt chart and prose now use — Nebius B200x8 (101,246 /
101,611 / 59,622.7), Nebius H200x8 (34,812.1 / 34,029.4 / 23,079.9), and AMD
8xMI300X (27,803.9 / 24,593.8 / 8,840.42) — all match the primary exactly,
including the 32.2% and 64.1% drops the chart script's docstring claims for
the H200 and MI300X rows. No residual sentence anywhere in the article
implies batch size alone drove the retracted 1,349/4,750/11,819 figures; a
full-text search for those numbers, "8.8-fold," and "held fixed" turns up
nothing but the new, accurate use of "hardware and model held fixed" in the
chart caption, which is true of the MLPerf series. The one llama_70b matched
pair (341 vs. 303 tok/s/GPU) that the brief permitted as an optional aside
was cut rather than kept — a legitimate call under the word band, not a gap.

Pillar 4's H200-vs-H100 aside is now honest: it states plainly that the two
cited examples "differ in model and parallelism, not context length alone,"
before drawing the narrower, defensible conclusion that speed at different
context lengths is not the same claim. This matches what I verified against
the primary in the 01 round.

## Cut
Cut: 0 sentences; worst tell: none found in the changed prose. The new
pillar-2 paragraphs, the rebuilt transition line ("Loosen the bound... tighten
it and that room shrinks"), the loosened pillar-4 aside, and the rewritten
takeaway opening are all new material since 01, and none of it reads as
padding, prompt leakage, or a formula. The takeaway specifically no longer
echoes the commission's "is not one number; it is a family of numbers"
framing — it now closes on the article's own terms ("A published
tokens-per-second figure describes one specific run. It is not a fixed
property of the chip"), a legitimate callback to the misconception the
orientation section named early ("tokens per second is a property of the
chip, the way clock speed is a property of a CPU. It is not"), not an
invented strawman. The one semicolon in the new material ("Loosen the
bound... climbs; tighten it... shrinks") joins two tightly parallel,
genuinely independent clauses — a defensible rare use, not a comma-splice
patch or a chain.

## Reader
Reader: this still gives me the four questions plus the six-way comparison
table (unchanged, now correctly citing the corrected MLPerf source), and now
also a chart that itself teaches something no prose sentence alone would:
three different hardware platforms, same model, same three latency policies,
show the same direction (tighter bound, lower throughput) at visibly
different magnitudes (32%, 41%, 64% drops) — a range, not a single ratio,
which is a more honest picture of the mechanism than a single "8.8x" number
would have been. The piece still reads continuously; the section that took
the surgery has no seam a reader would notice. Prose register holds at the
voice-guide level throughout the new material.

## Direct edits made
None required. The revision resolved every item from `editor/01/editorial-review.md`
correctly; nothing in this round called for a further cut or citation fix.

## Required work by owner
None.

## Decision
Publishable. Both 01 findings are resolved and independently re-verified
against the owning primaries (MLPerf's raw v5.1 results file, fetched and
filtered directly) rather than taken on the evidence record's word alone.

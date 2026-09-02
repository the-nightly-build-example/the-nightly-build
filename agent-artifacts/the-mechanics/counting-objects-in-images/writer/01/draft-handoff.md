# Draft handoff: the-mechanics/counting-objects-in-images (writer, round 01)

## Original work

The evidence record supplies the encoder's quantity-weak bag-of-words
behavior, the diffusion mechanism, and the counting benchmarks as separate
findings from separate papers; this article's work is assembling them into
one ordered causal chain specific to counting (encoder checklist → no
per-object tally in generation → the resulting count-vs-accuracy curve →
which fixes close which half of the gap), holding the two causes as
complementary rather than collapsing either into the other, at a calibration
the evidence actually supports (reliable for roughly five objects or fewer,
unreliable and improving beyond that) — which no single cited source states
as a chain.

## Proof result

Final run: `nb stamp` then
`nb check .nb-work/the-mechanics/counting-objects-in-images/library/the-mechanics/counting-objects-in-images.html --series the-mechanics --library /home/user/library-checkout`
(links included) → **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**.

No warnings left standing.

## Notes for the editor

- Chart 1 (`chart-1.py`/`.png`, T2I-CompBench++ numeracy by model generation)
  uses the evidence record's own approximate figures; both the axis label and
  the caption mark them as approximate per the researcher's transcription-risk
  note, and bar labels carry a "~" prefix rather than bare decimals.
- Two exact-figure claims from the evidence (CLIP counting accuracy 31.67% →
  75.93%, and the Make It Count count-accuracy deltas) are rounded and stated
  as plain before/after figures rather than as invented ratios, after an
  earlier draft pass overstated one as "three times as often" (actual ratio
  is closer to 2.4x) — worth a second look given the researcher's general
  caution on exact table-cell numbers.
- The DALL-E 3 caption-quality thesis was left out entirely, per the
  commission and evidence record (that source was never primary-read).
- No open evidence or voice question remains from this round.

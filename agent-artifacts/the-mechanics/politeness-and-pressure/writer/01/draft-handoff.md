# Draft handoff: the-mechanics/politeness-and-pressure (01)

## Original-work sentence

The article reads the studies' disagreement over whether politeness helps or
hurts as itself the result: it splits the settled fact that the model was
trained to react to tone from the folklore's unsupported claim that a
particular phrasing reliably improves the answer, and marks the point along
that chain where the engineering stops being settled.

Where it is visible: the "How the words reach the model" section states the two
settled steps (the output is computed from every token; the sensitivity to tone
is a trained disposition) and names the hinge; the "controlled tests disagree"
section treats the cross-study contradiction (Yin: polite helps; Mind Your
Tone: rude helps; Wharton: no reliable direction) as the finding rather than as
noise to reconcile; the steelman section weighs the big-gain papers and reads
the whole record as gains that shrink as models improve.

## Proof result

`./nb check --series the-mechanics --library /home/user/library-checkout .nb-work/the-mechanics/politeness-and-pressure/library/the-mechanics/politeness-and-pressure.html`
→ BLOCK: 0, WARN: 0, verdict PUBLISHABLE (links on, after `nb stamp`).

No warnings intentionally left. The five warnings from the first pass (four
W-SENTENCE-DENSITY, one W-SELF-COUNT) were all resolved: the four dense
sentences were split, and `nb stamp` wrote the counts (words 1766, reading 8
min, sources 9).

## Evidence caveats honored

- Only the verbatim-confirmed Yin GPT-3.5 MMLU cells are given as exact decimals
  (60.02 / 59.44 / 51.93); the GPT-4 and Llama-2 results are stated
  qualitatively (flat vs proportional), as the record marks them.
- The Bsharat GPT-4 gains are given as direction only ("rose with model size,
  largest on GPT-4"); the summary-sourced ~57.7 / ~36.4 decimals are not
  presented as exact.
- EmotionPrompt's 115% is used but flagged in prose as a relative gain drawn
  against a best-case aggregation, and both steelman papers are marked as
  2023-era or smaller models. Reported fact, the inflation estimate, and the
  synthesis (effect shrinks as models improve) are kept distinct.

## Open questions

None for evidence or voice. The article does not use a chart or source asset:
the one visual the record proposes (Yin Figure 3, flat-vs-steep curves) needs
the GPT-4 and Llama per-cell numbers, which the record confirms only
qualitatively, so a faithful chart is not buildable from the verified series and
the contrast is carried in prose and the comparison table instead.

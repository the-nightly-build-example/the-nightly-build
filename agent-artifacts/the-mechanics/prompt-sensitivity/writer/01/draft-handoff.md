# Writer handoff: the-mechanics/prompt-sensitivity (01)

## Original-work sentence

The article turns a set of prompt-sensitivity measurements and their one live
contradiction into a single reader-usable diagnostic: it walks one colon-to-space
swing on 1-shot LLaMA-2-7B back to token-level conditioning to fix the mechanism
as settled, then splits every reported score move into three distinct causes (a
genuinely worse model, a surface form that changed the input, and a grader that
missed a correctly phrased answer) so the reader can tell which one a given
number reflects. That three-way split and the settled-mechanism / open-magnitude
boundary are synthesis the evidence record states nowhere as such.

## Proof result

`./nb check ... --series the-mechanics --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped
words=1984, reading_minutes=9, sources=8.

No warning left standing. Two W-SENTENCE-DENSITY warnings during iteration were
resolved by splitting the opener's three-case sentence and tightening it, not by
suppression.

## Angle fidelity (for the editor's spot-check)

- The worked example (colon vs space, 0.043 -> 0.826) is attributed to 1-shot
  LLaMA-2-7B, task280, Sclar et al. Table 1. It is kept separate from the 76-point
  figure, which is named as LLaMA-2-13B. The two are never merged.
- Large magnitudes are all attributed to 2021-2023 open models (LLaMA-2, GPT-2/3)
  under probability-ranking or exact-match scoring, and the scoring regime is
  stated in the reformatting section.
- The frontier-model magnitude is marked open: Sclar/Su (does not shrink with
  scale, +/-23% on current families) are steelmanned, then Hua et al. show much
  of the modern spread is a scoring artifact that collapses under an LLM judge.
  The mechanism is marked settled at the mechanism section; the magnitude is
  marked open at the grader section.
- Three cases are held distinct throughout and crystallized in the note. The
  Webson & Pavlick nuance (scrambled meaning is near a no-op, answer tokens are
  not) is carried, not flattened to "surface form matters."
- Series "No code": format variants appear only as inline `<code>` data strings;
  there is no runnable harness, script, or chart.

## Decisions the editor may want to know

- All eight sources in the evidence record are cited. The series floor is 8
  sources with at least one secondary; the Hugging Face blog is the only
  secondary the researcher opened, so it is cited (s4) for the accessible MMLU
  demonstration, and Mizrahi et al. (s5) carries the cross-model breadth and the
  ~21-point single-prompt overstatement.
- Display-text rounding: the dek's "4% and 83%" are 0.043 and 0.826 from Table 1,
  rounded to whole percents; the exact fractions appear in the body and the
  furniture table.
- Furniture: one table (the three atomic-change format pairs, Sclar Table 1) and
  one note (the three ways a score can move). No source asset was captured; the
  argument's need was the exact format strings and paired accuracies, which the
  table carries as inline data without an external image.
- The dek was recast off the "[do X] and [Y happens], because [mechanism]"
  construction after checking it against the recent the-mechanics deks (the
  memorization dek uses that mold).
- The Hugging Face blog also appears as a Go-deeper row, reframed to its proposed
  mitigation so it does not restate the body's 22.9%/51.2% figure.

## Open questions

None blocking. No evidence gap was hit; no voice-guide ambiguity forced a
judgment call the guide did not already settle.

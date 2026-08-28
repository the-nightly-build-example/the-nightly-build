# writer brief: the-instruments/word-error-rate (01)

Inputs:
- editorial-direction.md   (house standard, paper voice, series prompt, template identity)
- writing-coach/01/voice-guide.md   (how this piece should sound; read before drafting)
- researcher/01/evidence.md   (the complete claim set; read its Contradictions closely)
- the initialized article at library/the-instruments/word-error-rate.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-instruments/word-error-rate/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/word-error-rate/library/the-instruments/word-error-rate.html --series the-instruments

Corrections the research demands (the commission's framing was slightly off):
- Do NOT write that WER "barely penalizes" hallucination. Hallucinated words ARE
  scored as insertions/substitutions and DO raise WER on the affected segment
  (often above 100%). The defensible, primary-supported point is narrower and
  still sharp: (a) a corpus-level WER AVERAGES catastrophic segments away, so a
  low headline WER can hide segments that are badly wrong; and (b) WER is
  MEANING-BLIND — it scores a fluent fabrication identically to an audible
  mishearing of equal length, and weights a dropped "not" the same as a filler
  "uh." Make that the thrust.
- "Human parity" is a story of BASELINE SOFTNESS and CORPUS DEPENDENCE, not a
  hollow result: it HELD on the clean Switchboard subset (Microsoft's 2017 system
  reached 5.1%, matching IBM's best human), but did NOT generalize — on the harder
  CallHome set the human baseline itself moved from Microsoft's 11.3% to IBM's
  more careful 6.8%. Microsoft conceded human performance "falls within a range
  depending on the level of effort expended." Report both, and let the softness of
  the human number carry the lesson.
- Steelman you must answer, not skip: Microsoft's error analysis found humans and
  machines making the same function-word errors on the same hard speakers, and
  judges could not tell the transcripts apart. Address this before weighing it.
- Blind spots to use (sourced): noise (Whisper Fig. 5), accents/dialect (Koenecke
  et al. 2020, PNAS), informal/overlapping multi-speaker audio (the CallHome-vs-
  Switchboard gap). Do NOT claim degradation on CHILDREN'S speech — it is not
  sourced in the record; omit it.
- Give the verified worked S/D/I micro-example from the record (a short reference
  vs hypothesis with the substitution/deletion/insertion counts and the fraction),
  and note WER can exceed 100%.

Continuity (link, do not overlap): the-instruments/bleu and rouge share the
overlap/edit-distance idea for different tasks — link for "a metric misses
meaning," keep this on speech. the-evidence/whisper is the hook for a low-WER
system that still fabricates fluent text — link it, do not re-teach.

Furniture: a table or worked example for the S/D/I alignment; a stat strip for the
Switchboard/CallHome human-vs-system WER figures if it aids the reader; a chart
only if a comparison is genuinely the point and the series is verified in the
record. No verdict block in the body — the takeaway bookend lands the judgment.

Recent shapes in The Instruments to break: avoid the "same model two numbers" and
"The [score] does a surprising thing" builds by reflex; avoid banned dek molds and
the comma-plus-"and" heading join.

nb-meta you own: date 2026-08-28; harness "Claude Code"; model "claude-opus-4-8".

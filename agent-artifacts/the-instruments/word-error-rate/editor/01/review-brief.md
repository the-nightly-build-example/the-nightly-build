# editor review-brief: the-instruments/word-error-rate (01)

Inputs:
- editorial-direction.md   (house standard, slop/headline specs, paper voice, template identity)
- commission.md            (the assignment, its boundaries, the reader's situation)
- writer/01/brief.md        (the exact writer brief incl. corrections — check for leaks against it)
- writing-coach/01/voice-guide.md   (read first; how the piece should sound; check for borrowed phrasing)
- researcher/01/evidence.md   (the claim set; reread cited passages for what breaks each claim)
- writer/01/draft-handoff.md   (open its original-work sentence only on the third read)
- the drafted article at library/the-instruments/word-error-rate.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-instruments/word-error-rate/editor/01/editorial-review.md
Proof (orchestrator stamps and runs after your edits): ./nb check .nb-work/the-instruments/word-error-rate/library/the-instruments/word-error-rate.html --series the-instruments

Recent-pattern notes (check the draft against these library habits):
- The Instruments headlines lean on "The [score] does a surprising thing" and same-model-two-numbers builds.
  Flag a rote clone of the most recent two.
- Banned dek molds: comma-triad, semicolon reversal, suspended question. Heading habit to break: comma + "and".
- Bookend openers must hold to this lesson's particulars, not generic importance.

This round's focus (verify against the evidence record):
- The metric-vs-hallucination framing must NOT say WER "barely penalizes" hallucination. Hallucinated words ARE
  scored (insertions/substitutions) and raise segment WER (often >100%). The correct thrust is (a) corpus-level
  WER AVERAGES catastrophic segments away, and (b) WER is MEANING-BLIND (a fluent fabrication scores the same as
  an equal-length mishearing; a dropped "not" = a filler "uh"). If the draft overclaims, fix or route.
- "Human parity" must read as BASELINE SOFTNESS + CORPUS DEPENDENCE, with BOTH readings: it held on clean
  Switchboard (Microsoft 2017 5.1% matching IBM's best human) but did NOT generalize (CallHome human baseline
  moved 11.3% -> IBM's 6.8%); Microsoft conceded human performance "falls within a range depending on the level
  of effort expended." Verify both are present and correctly attributed.
- The steelman (humans and machines made the same function-word errors on the same hard speakers; judges could
  not tell the transcripts apart) must be stated in full and then weighed, not skipped.
- NO children's-speech blind-spot claim (unsourced). Blind spots used should be noise (Whisper Fig. 5),
  accents/dialect (Koenecke 2020 PNAS), and the CallHome/Switchboard gap.
- Check the worked S/D/I example and the "WER can exceed 100%" note, and every Switchboard/CallHome figure,
  against the record. Check primary/secondary data-nb-kind (note IBM renumbered to s5, Microsoft 2017 to s6).

Note on internal links: prose/Background links to the-evidence/whisper, the-instruments/bleu, and
the-instruments/rouge use CORRECT real published slugs and resolve on the library branch, not this workspace —
do not treat as broken. No verdict block in the body — the takeaway bookend lands the judgment.

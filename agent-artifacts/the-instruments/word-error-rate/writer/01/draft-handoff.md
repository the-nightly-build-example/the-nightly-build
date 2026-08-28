# Draft handoff: the-instruments/word-error-rate (01)

## Original-work statement
This article turns a scattered evidence set into a single teaching arc that
reframes "human parity" as a story about a movable human baseline and a
meaning-blind metric, then converts that story into three concrete questions
(measured on which speech, against whose reference, normalized how) a reader can
ask of any speech-recognition score.

## Proof result
`./nb check ... --series the-instruments` (links included): **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. Stamped at words=2200 (band 1200-2200), reading_minutes=10,
sources=8. No warnings intentionally left.

The local proof runs without `--library`, so its note reports open-mode dedupe and
commission checks were skipped, and it does not resolve the three internal
continuity links (the-evidence/whisper, the-instruments/bleu, the-instruments/rouge);
those resolve against the published library, not this isolated workspace.

## How the brief's corrections were met
- Hallucination framed as the defensible narrow point: WER is meaning-blind
  (scores a fluent fabrication like an equal-length mishearing; weights a dropped
  "not" like a filler "uh") and a corpus-level average hides catastrophic segments.
  Nowhere does the piece say WER "barely penalizes" or fails to count hallucinated
  words.
- Human parity told as baseline softness plus corpus dependence: Switchboard parity
  held (2017 system 5.1% = IBM best human 5.1%); CallHome human moved 11.3% -> 6.8%
  under IBM's careful protocol; Microsoft's own concession quoted.
- Steelman answered before it is weighed: Microsoft's error analysis (same
  function-word errors, judges could not tell the transcripts apart) is stated in
  its strongest form, then the softness of the human baseline is what the piece
  pushes on.
- Blind spots sourced: noise (Whisper), accents/dialect (Koenecke PNAS 0.35 vs
  0.19), informal/overlapping speech (the CallHome-vs-Switchboard gap). No
  children's-speech claim.
- Verified worked S/D/I micro-example included as a table (REF "the quick brown fox
  happily jumps" vs "the slow brown fox jumps now": 1S/1D/1I over 6 = 50%), with the
  sclite 0/3/3/4 weighting shown to make that split the unique minimum, and the
  >100% case ("hello" -> "hello there my friend" = 300%).

## Furniture
Annotated WER equation (S/D/I/N legend), the worked S/D/I table, a four-figure stat
strip for the Switchboard/CallHome human-vs-system numbers, and one quotation note
carrying Microsoft's concession. No chart (the parity data is a small discrete
comparison the stat strip and prose carry; no trend is the point). No source asset
captured. Verdict block deliberately omitted from the body; the takeaway bookend
lands the judgment.

## Open questions
None blocking. Flag for the editor: the three internal continuity links depend on
those lessons existing in the published library at build time.

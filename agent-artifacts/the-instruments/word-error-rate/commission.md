# Commission: the-instruments/word-error-rate

## The measurement
Word Error Rate (WER): the standard score for speech recognition. Align a
system's transcript to a reference transcript by minimum edit distance, count the
substitutions, deletions, and insertions, and divide by the number of words in
the reference. It is the number behind every "our speech recognition is as good
as a human" claim.

## Why this measurement, now
The reader meets speech-to-text everywhere (voice assistants, captions, medical
and legal transcription) and meets the claim that machines now transcribe "at
human parity." The Instruments teaches how WER is computed and what it can and
cannot support. WER is worth a lesson because the "human parity" milestone rested
entirely on it, and WER hides exactly the things that matter: it weights a dropped
"not" the same as a filler "uh," it is not comparable across datasets, and a
score measured on clean benchmark speech collapses on accents, noise, children,
and overlapping talk. A single WER percentage looks like a thermometer and is
really a count of word edits on one particular corpus.

## The angle (how the number is made, then where it misled)
1. Where the number comes from, step by step: the reference transcript, the
   alignment by edit distance, the three error types, the denominator, and why
   WER can exceed 100%. A short worked example (a one-sentence reference and a
   system output, with the S/D/I counts) makes it concrete.
2. What WER can support: relative comparison of systems on the SAME test set with
   the SAME reference and text-normalization rules.
3. What it cannot, with the real "human parity" case and its cost. The candidate
   the researcher should verify and lead with: Microsoft's 2016-2017 "human
   parity in conversational speech recognition" result (Xiong et al.) reporting
   ~5.9% then ~5.1% WER on the Switchboard benchmark and claiming parity with
   professional transcribers — and the pushback (IBM's contemporaneous
   measurement of the human WER; the fact that parity held on Switchboard/CallHome
   telephone speech and not on harder conditions). Teach WHY WER made the claim
   possible: all errors weighted equally, one corpus, a human baseline that is
   itself a measured number. Bring in how a modern system (e.g., Whisper, taught
   in this course) can post a low WER and still hallucinate fluent text a human
   never said — a failure WER barely penalizes.

## Boundaries and continuity
Differentiate from published Instruments lessons and link rather than overlap:
the-instruments/bleu and rouge (text-overlap metrics for translation/summaries)
share the edit-distance/overlap idea but score different tasks — link them for the
"a metric can be gamed / misses meaning" point, and keep this lesson on speech.
the-evidence/whisper is a strong hook for the low-WER-but-hallucinating failure —
link it, do not re-teach it. No verdict block in the body; the takeaway lands the
judgment.

## Template, furniture, policy
- Template: lesson. A small table or worked example for the S/D/I alignment fits
  well; a stat strip for the parity figures (human WER vs system WER on
  Switchboard/CallHome) if verified; a chart only if a trend is genuinely the
  point. Inline <code> only where a reader must preserve an exact token string.
- Source policy: >=8 sources, >=4 primary, >=1 secondary. Primary = the Microsoft
  human-parity paper(s), IBM's response (Saon et al.), the NIST/Switchboard
  scoring definitions or the sclite/WER standard, the Whisper paper for the
  robustness/hallucination point, and any paper documenting WER's blind spots.
  Secondary = reporting/context.
- Production policy (balanced): researcher high/capable, coach low/capable,
  writer medium/capable, editor high/capable. No `required` directives.

## Recent shapes in this series to break
Avoid the "same model, two numbers" and "The [score] does a surprising thing"
builds by reflex; avoid the banned dek molds (comma-triad, semicolon reversal,
suspended question) and the comma-plus-"and" heading join.

## What this article must add
The reader should be able to say what a WER percentage measures, why "human
parity" was a claim about one benchmark and one way of counting, and what to ask
before trusting a speech-recognition score ("measured on which speech, against
whose reference, normalized how").

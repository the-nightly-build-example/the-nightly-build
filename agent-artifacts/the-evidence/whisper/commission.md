# Commission: the-evidence/whisper

## Assignment

One lesson on the document *Robust Speech Recognition via Large-Scale Weak
Supervision* (Radford, Kim, Xu, Brockman, McLeavey, Sutskever; OpenAI; released
September 2022 with the Whisper models). The Evidence reads a famous AI document
so the reader learns what it actually says. The reader is smart, widely read, and
new to speech recognition. Teach the terms the field takes for granted (word
error rate, supervised vs weakly supervised training, zero-shot / out-of-
distribution evaluation) at first use.

## Why this document, now

Whisper is the speech-to-text model most people and products actually run, and in
October 2024 an Associated Press investigation reported that it invents text that
was never spoken, including in medical transcription. The paper's own headline
claim is robustness: that training on a very large, messy, weakly labeled corpus
buys generalization to audio the model never trained on. The present-day failure
sits directly on top of that claim. That tension is the lesson.

## Angle

The paper's result is not "most accurate transcriber." On clean benchmarks,
specialized supervised models still match or beat it. The paper's actual claim is
that scale of weak supervision buys *robustness*: smaller gaps between in- and
out-of-distribution audio, approaching the spread a human shows. Show the reader
the size of the foundation under that claim (how many hours, how weak the labels,
what "zero-shot" evaluation means and why it makes the comparison fairer to
Whisper and harder for the supervised baselines), then bring it to the present:
the same design that makes it robust also makes it hallucinate fluent text
through silence and noise, because it is a sequence model trained to always
produce plausible transcript tokens. State plainly where today's usage (verbatim
medical/legal transcription) does not match what the paper measured.

## What to teach (short, complete)

1. What word error rate is, in plain terms, with a small worked example, and why
   "robustness" here means the gap between clean and messy audio, not a single
   accuracy number.
2. The scale and the weakness of the supervision: ~680,000 hours of labeled audio
   collected from the web (the paper's figure), including ~117,000 hours across
   ~96 other languages and ~125,000 hours of translation data; labels are
   whatever text accompanied the audio, filtered to remove machine-generated
   transcripts. Contrast with the thousand-hour scale of prior supervised sets.
3. Zero-shot / out-of-distribution evaluation: Whisper is tested on datasets it
   never trained on, so it cannot overfit a benchmark's quirks; supervised
   baselines are usually tested on held-out data from the same distribution they
   trained on. This is why the paper reports Whisper closing the human-vs-machine
   robustness gap even when a supervised model has a lower number on its home
   benchmark.
4. The present: the same always-emit-a-token design produces hallucinated spans
   during non-speech; cite the paper's own acknowledgment of hallucination plus
   the 2024 reporting and any peer-reviewed measurement. This is where findings
   meet real deployment.

Keep the list to what fits 1200-2200 words completely. Cut an idea rather than
shrink it.

## Boundaries and non-overlap

- This is the first speech-recognition document in the library. Neighboring
  Evidence pieces read one document each and often land on "the famous claim is
  not what the paper measured" (gpt-2, batch-normalization, foundation-models).
  That family framing is fine; the specific finding here (robustness via weak
  supervision, undercut by hallucination) is the article's own and must be earned
  from the paper, not asserted as a house move.
- Word error rate, weak supervision, and zero-shot evaluation are taught here.
  Anything already taught elsewhere gets a plain prose link at first use, not a
  re-teach. The researcher should surface whether the library already teaches WER
  or zero-shot evaluation so Background can link rather than repeat.
- Work from the paper (arXiv 2212.04356) and the model/data details in OpenAI's
  released materials, not from coverage. Coverage (AP) is admissible only for the
  present-day deployment failure, and the underlying hallucination claim needs
  the primary account plus independent confirmation.

## Source policy

Lesson in The Evidence: at least 6 sources, at least 3 primary and at least 1
secondary. Primary here: the Whisper paper, the model card / repository, any
peer-reviewed hallucination study, benchmark datasets cited for numbers. The AP
investigation is secondary for the deployment claim and needs a second
independent confirmation for any accusation of harm.

## Habits to avoid (break these, from the recent record)

- Do not open the dek with "The Whisper paper ..." or "The [document] ...". The
  last several Evidence deks lead with "The X paper/report [surprising verb]"
  (batch-normalization, GANs, knowledge-distillation, gpt-2). Write a dek that
  leads with the concrete finding in Whisper's own nouns (hours, error rates,
  hallucination) instead.
- Vary the orientation heading away from the recent "What 'X' actually names" /
  "The number on the model card" definitional openers.
- Do not stack furniture. A stat strip for the scale figures or a small WER table
  earns its place only if it changes understanding.

## This run's neighbors (for coherence, not cross-reference)

Four other lessons publish tonight: the-instruments/imagenet-top-5-accuracy,
the-mechanics/overused-words, what-could-go-wrong/value-lock-in,
when-ai-breaks/itutorgroup-age-discrimination. Keep the register consistent with
one paper; do not converge on the same dek shape or the same opening move.

## Production record

- Harness: claude-code-routine. Writer model: claude-opus-4-8 (the run's serving
  model; production policy asks for "capable", not a pinned model, so no deviation).
- Roles and effort per production policy (balanced): writing-coach low,
  researcher high, writer medium, editor high. No role is `required`.
- Template: lesson. Source floor and kind mix as above.

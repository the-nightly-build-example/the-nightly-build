# Commission: the-mechanics/speech-to-text-hallucination

## Assignment
Explain the observed behavior: an AI transcription tool sometimes prints whole
sentences that were never spoken, most often over silence, background noise, or a
pause. One lesson on the Mechanics desk. Template: lesson. Publication date:
2026-09-13.

## Why this behavior, now
The reader has met text hallucination in chatbots (`the-mechanics/hallucination`),
but automatic speech recognition is a different modality with a distinct trigger,
and it is now embedded in medical scribes, captions, and note-takers people
cannot easily check against the audio. It is a clean case of a general mechanic
the course wants the reader to own: a system whose output stage is a language
model will emit fluent, plausible text even when its input carries nothing to say.

## The behavior to open on
A concrete, sourced instance of a modern transcription system inventing text:
non-speech audio or silence turning into a fluent, confident sentence, ideally one
with real consequences (a clinical or captioning setting). Name the system, the
study or report, and the numbers (how often, and how often the invented text was
harmful).

## Work backward to the cause (the desk's arc)
Each step names a real part of the system and what it does, with a small concrete
example, going down until nothing below would change the answer, marking which
steps are settled engineering and which are open:
1. What the tool was built to do and how it is used (a scribe that drops the
   original audio once the transcript exists, so the invented line has no source
   to check against).
2. The shape of the system: an audio encoder feeding an autoregressive text
   decoder that is itself a language model trained to produce well-formed text.
3. Why silence or noise yields fluent invention: with little or nothing in the
   audio to condition on, the decoder falls back on its language prior and
   generates the most probable continuation, which is a grammatical sentence, not
   a blank. Contrast with an older word-by-word recognizer that could only emit
   what it heard.
4. Why the invented text is confident and plausible (it is drawn from the same
   distribution as real transcripts) and why training data (e.g., trailing
   captions, boilerplate) can seed specific recurring inventions.
5. Ground: what is settled (the decoder is a generative language model; empty
   input still produces output) versus open (exactly which inputs trigger it, how
   much better data or decoding rules fix it, vendor-specific rates).

## What the reader already holds — do not re-teach, link instead
- Autoregressive next-token generation and that a decoder predicts likely text:
  link `the-mechanics/autoregressive-generation` and/or `the-mechanics/hallucination`.
- Word Error Rate as the accuracy number for transcription: link
  `the-instruments/word-error-rate` if a Background row helps.
- The model behind many of these tools: link `the-evidence/whisper` for what the
  system is, rather than re-teaching it.
Define "encoder" and "decoder" in one plain line each where first used.

## Research directions (researcher owns depth)
1. A primary study measuring transcription hallucination and its rate and harm
   profile (for example, the peer-reviewed work on OpenAI's Whisper hallucinating
   on non-speech audio, with the share of segments affected and the share of those
   that were harmful). Read the paper, not the news write-up, for every figure.
2. The model's own description of its architecture and known failure on
   non-speech / long silence (e.g., the Whisper paper and model card, and any
   vendor documentation of the behavior in a deployed scribe).
3. A deployment where this matters and what the operator did (a medical
   transcription tool used across many clinicians; whether it retained or dropped
   the source audio; any response). Names, dates.
4. The mechanism confirmation: sources establishing that the decoder is an
   autoregressive language model and that its language prior drives output when
   the acoustic signal is weak.

## Contradictions to probe
Whether the invented text is truly "from nothing" versus mis-heard faint speech;
how much is fixed by voice-activity detection or decoding constraints versus
inherent to the generative decoder; vendor disagreement about rates. Record it.

## Sources
Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primary: the
measuring study, the model paper/card, vendor or operator documentation. Contested
figures need the primary that owns them.

## Boundaries
No code. Teach the mechanism, not a product review. This is not a "when AI breaks"
incident piece: the failure is the way in; the lesson is why that kind of system
fails that way. Do not overlap the chatbot-hallucination lesson: keep the focus on
the audio-to-text modality and the empty-input trigger.

## Production policy (balanced; none required)
writing-coach capable/low; researcher capable/high; writer capable/medium; editor
capable/high. "capable" served by the run's default subagent model (Opus-class);
record the actual writer model in nb-meta.

## Neighbors in this run
the-evidence/mamba, the-instruments/bertscore,
what-could-go-wrong/capability-elicitation, when-ai-breaks/retinopathy-field-study.
No overlap.

## Habits from the recent record not to inherit
- Mechanics headlines often use the imperative "Ask [system] for X and it Y" mold
  and the "A model can X and still Y" mold. Find this piece's own headline.
- Keep the work-backward arc but name sections for this behavior, never with stock
  labels, and do not reuse a prior mechanics piece's section shape.

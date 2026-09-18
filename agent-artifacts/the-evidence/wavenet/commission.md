# Commission: the-evidence/wavenet

## The assignment

Teach the reader what the WaveNet paper actually did. The document is the DeepMind
paper "WaveNet: A Generative Model for Raw Audio" (van den Oord et al., 2016). One
lesson, one document, on the lesson template.

The reader is the paper's declared reader: smart, widely read, no time in a
codebase. Assume no prior audio-modeling knowledge. Algebra and probability are
the only background you may assume; teach or link everything else at first use.

## Why this document, tonight

The Evidence has taught the generative-model lineage for images and text
(variational-autoencoder, gans, denoising-diffusion, latent-diffusion) and the
speech-recognition side (whisper), but nothing on generating raw audio. WaveNet is
the document that made neural audio generation work and reset the quality bar for
text-to-speech; its lineage runs to the voices in today's assistants and to later
neural vocoders. It is a real empirical paper with data, a method, and reported
numbers, which the beat requires.

## The angle

WaveNet's fame is "human-level" or near-human speech, but the paper earns that
claim on a specific, narrow measurement, and its original method was famously slow.
Center the lesson on the gap between what the paper measured and how the result is
remembered:

- What the model is: an autoregressive model over raw audio samples, predicting one
  sample at a time from the samples before it. Explain why modeling raw waveform
  samples (thousands per second) was considered infeasible before this, and what
  dilated causal convolutions changed. Teach "autoregressive" and "dilated causal
  convolution" in plain words at first use; link the-mechanics/autoregressive-generation
  if it helps rather than re-teaching.
- What it actually did: the tasks (text-to-speech in English and Mandarin, music,
  speech recognition as a secondary probe), the data scale, and the evaluation. The
  headline evidence is a mean opinion score (MOS) comparison against the previous
  best parametric and concatenative systems. Report the actual MOS figures and the
  gap to natural human speech, and be honest that the reader cannot scale a raw MOS,
  so anchor it (the paper measures MOS on a 5-point scale; give the numbers and the
  human baseline). The reader has a lesson on mean opinion score
  (the-instruments/mean-opinion-score) that says MOS does not travel between tests;
  link it and do not re-teach it, and let it sharpen the honesty about the headline.
- The honest scale and the catch: the original WaveNet generated one sample at a
  time and was far too slow for real-time synthesis. This is central, not a footnote.
  Report what the paper and its follow-ups say about generation cost.
- Present tense: what later work confirmed, corrected, or replaced. Parallel WaveNet
  (van den Oord et al., 2017) made it fast enough to deploy in Google Assistant; the
  wider field moved toward other neural vocoders and later end-to-end and diffusion
  approaches. Say plainly where the raw 2016 method stands now versus how "WaveNet"
  is invoked today.

State plainly, where the evidence supports it, that the durable contribution was the
autoregressive-raw-audio approach and the quality jump, while the specific 2016
architecture was superseded on speed.

## Boundaries

- Claims about the model come from the paper itself, and deployment/cost claims from
  the primary follow-ups (Parallel WaveNet, Google's own writeups). Coverage is
  context only.
- Do not turn this into a general history of speech synthesis or of DeepMind. One
  document.
- No code. The reader has no codebase. Explain the mechanism in words and, if a
  figure from the paper carries the argument better than prose (for example, the
  dilated-convolution stack diagram or the MOS bar chart), the researcher should
  flag it as a source asset for the writer to consider.

## Neighbors in this run

Four other lessons publish alongside this one (the-instruments/mean-average-precision,
the-mechanics/typo-robustness, what-could-go-wrong/power-seeking-ai,
when-ai-breaks/sports-illustrated-ai-authors). No overlap in subject; no coordination
needed beyond not reusing a headline or heading mold another lesson lands on.

## Recent habits not to inherit

From the last several published Evidence lessons (gpt-1, flashattention,
computing-machinery-and-intelligence, imagenet-database, mamba):

- The headline mold "X beat Y on nine of twelve datasets" and the reversal headline
  "X did A. Its authors did B." recur. Find this piece's own headline.
- Deks that open "Author-and-year's paper does X, and Y" are the standing shape.
  Write a dek that identifies WaveNet by a detail only it carries; do not copy that
  clause rhythm.
- The heading mold "The [noun] that [verb]" ("The half that survived") recurs across
  the desk. Vary how headings are built and keep each in this piece's own nouns.

## Source policy

Series/template floor: at least 6 sources total, at least 3 primary and at least 1
secondary. Primary here means the WaveNet paper, Parallel WaveNet, and DeepMind's or
Google's own first-party writeups and audio samples; the MOS methodology as the paper
states it. Meet the floor with sources that change the interpretation, not padding.

## Production record

- Template: lesson. Series: the-evidence (open mode; no commissioned tag).
- Word band: 1200-2200.
- Model/effort actuals (production-policy resolved "capable"/non-required for every
  role): all roles run on the available capable model, Claude via isolated
  subagents. writing-coach at low effort, researcher at high, writer at medium,
  editor at high. No required directive; nothing traded down.
- Checkout revision: df69fc11a5d7fcdfdbc7eda5eb8a8d178b6d6a17.

# Writer handoff: the-mechanics/text-to-speech-pronunciation (01)

## Original work

The article takes two real deployed mispronunciations a reader could plausibly
have heard (Siri's "Mobile, Ala." and "Des Moines," both from the NPR source),
traces each one backward through the named pipeline steps to the exact stage
that produced it, and distills that backward trace into an explicit,
reusable diagnostic the evidence record does not itself state: a written form
that comes out as no correct pronunciation of that word at all is a
normalization/G2P failure (the right sound was never generated), while a
written form that comes out as a real, correct pronunciation, just the wrong
one for the sentence, is a homograph failure (the right sound existed and the
front end assigned it to the wrong sense). That test is rendered as its own
labeled component ("Which failure you just heard") and resolves both running
examples set up in the opening section.

## Proof result

- `./nb stamp .nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html`
  → `words=2198 reading_minutes=10 sources=8`
- `./nb check .nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html --series the-mechanics` (final run, with link checking on, no `--no-check-links`)
  → `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.
- Iterated several rounds with `--no-check-links` first (initial draft was
  2774 words, over the 1200-2200 band, and carried six `W-SENTENCE-DENSITY`
  warnings) to trim and split sentences down to 2198 words with zero warnings,
  then ran the final proof with links included, which passed clean. No
  warning was left standing; none needed to be.

## Notes

- Source floor met exactly at the required minimum: 8 sources, 7 primary
  (WaveNet, Sproat & Jaitly, Rao et al., Gorman et al., Nicolis & Klimkov,
  Shen et al./Tacotron 2, AWS Polly docs), 1 secondary (NPR).
- Honored this round's attributions: the vivid £900m/2mA normalization errors
  are presented as an experimental RNN's output with the production FST
  filter noted alongside, not as something a shipping voice says; the ~99%
  homograph figure is scoped to the located-homograph benchmark with its
  85.0% no-context baseline given as context; "almost always a front-end
  error" is marked as the classic-pipeline claim and Tacotron 2's 23/100
  unnatural-prosody sentences are named as a distinct back-end failure once
  front end and back end stop being separate boxes.
- Orientation introduces WaveNet's front-end/back-end split without yet
  using the word "phoneme," holding that term for the grapheme-to-phoneme
  section where it gets a concrete build-up first (voice guide's Lee &
  Trott model). The substance the brief named — WaveNet's back end working
  only from what the front end already decided, i.e. a phoneme string — is
  still carried, just assembled across the piece rather than stated in one
  place; flagging this as a deliberate sequencing choice rather than a gap,
  in case a later round wants it stated more explicitly up front.
- speech-to-text-hallucination is linked (not re-taught) as the primary
  Background item, per the boundary; text-in-images is the second Background
  link for the structural parallel the researcher flagged. No code appears
  anywhere in the piece.
- No chart or source asset used. The evidence record's own asset notes call
  the normalization and homograph figures small enough for prose/table
  treatment rather than a rendered chart, and no primary offered a
  photograph or diagram worth lifting; both numeric comparisons are given as
  `nb-table` furniture instead.

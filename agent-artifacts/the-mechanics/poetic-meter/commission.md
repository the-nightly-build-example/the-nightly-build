# Commission: the-mechanics/poetic-meter

## Assignment
Answer one behavior anyone who has asked a chatbot for a poem has met: it can
rhyme passably yet botches meter, syllable counts, and strict forms (a limerick's
beat, a haiku's 5-7-5, iambic pentameter). Work backward from that behavior to
its cause, step by step, marking what is settled engineering and what is still
open. No code.

## The behavior to open on
A concrete, reproducible failure: ask for a fixed-form poem with a countable
constraint (syllables per line, a metrical foot) and the output reads fluently,
often rhymes, but does not scan or miscounts syllables. Center the lesson on the
metrical/syllabic failure, which is real and un-taught, not on rhyme, which
models often get right.

## The chain to the cause
- The model reads sub-word tokens, not letters, phonemes, syllables, or stress.
  Syllable boundaries and stress are not represented in the input at all. Build
  this from tokenization, which is taught.
- To hold meter a writer must count syllables and place stress. The model has no
  direct access to either; whatever phonology it has is inferred statistically
  from text, and English spelling is an unreliable guide to sound.
- Contrast the parts it does better: end-rhyme in common English is frequent in
  training text and partly planned ahead (interpretability work has shown models
  activating a candidate rhyme before writing toward it). Rhyme success and meter
  failure have the same root: sound is not in the representation, so the model
  leans on surface statistics that carry rhyme better than scansion.
- Go down to ground: a step where nothing below changes the answer (there is no
  phonological or metrical representation the decoder consults). Mark clearly
  what is settled (no explicit syllable/stress input; tokenization hides sound)
  and what is open (how much phonological structure is latent in learned
  representations; why some models scan better than others).

## Boundaries: link, do not re-teach
- the-mechanics/autoregressive-generation already covers the rhyme-planning
  interpretability finding. Link it for the rhyme half; do not re-explain
  forward planning as this lesson's subject.
- the-mechanics/counting-letters already teaches that tokenization hides spelling
  and names rhyme as a same-cause failure. Link it; extend to sound/meter rather
  than repeat the spelling case.
- transformers-first-principles/tokenization is the taught source for tokens.
  Link at first use; do not re-teach tokenization from scratch.
- the-mechanics/text-to-speech-pronunciation covers grapheme-to-phoneme and
  prosody inside a speech pipeline. That is a different system (synthesis from
  text). Do not conflate it with a text model generating verse.

## Neighbors this edition
No overlap with tonight's other pieces. Keep this one strictly on the generation
mechanism.

## Sources
Lesson floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary: papers and technical reports whose findings you cite firsthand
(tokenization/BPE, studies measuring LLM phonology or poetic-form performance,
the interpretability work on rhyme planning). Secondary: outside explanation for
context. A reproducible demonstration you generate is not a citation; ground
every claim in a read source.

## Production record
- Profile: balanced. Roles run as isolated Claude subagents (capable tier).
- Effort by stage: writing-coach low, researcher high, writer medium, editor high.
- Writer records the actual writer model in nb-meta `model`, sets `harness` to
  `claude-code`. Article date: 2026-09-17.

## Recent habits to break
- the-mechanics/text-to-speech-pronunciation used "for one of two different
  reasons" in its headline; do not reuse that mold.
- Do not copy watermarks-in-generated-images' dek tail ("a mechanism distinct
  from the rarer case where...").
- Vary heading construction; do not make every subhead a full declarative
  sentence in the same rhythm.
- The takeaway bookend lands the judgment; no Verdict block.

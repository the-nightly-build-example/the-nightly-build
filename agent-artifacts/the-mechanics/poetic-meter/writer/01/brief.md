# writer brief: the-mechanics/poetic-meter (01)

Inputs:
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/writing-coach/01/voice-guide.md` — how this piece should sound; read before drafting
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/researcher/01/evidence.md` — the complete claim set; use the Numbers section exactly
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/commission.md` — assignment, boundaries, and the recent habits to break
- Article to edit in place: `.nb-work/the-mechanics/poetic-meter/library/the-mechanics/poetic-meter.html`
- Template context (effective contract, furniture catalogs, runtime assets): `.nb-work/the-mechanics/poetic-meter/.nb-context/`

Output: `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/writer/01/draft-handoff.md`

Proof (run with links, until BLOCK: 0):
`./nb check .nb-work/the-mechanics/poetic-meter/library/the-mechanics/poetic-meter.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

This round's focus (a correction the evidence forces):
- Do not claim the model has "no phonological representation." The evidence shows
  sound is latently present in token embeddings (phonemes recoverable ~96%, and
  steering the embedding changes rhymes) but unreliable and not used for exact
  counting. Frame the mechanism as present-but-not-deployed-for-counting.
- The measured spine is syllable counting (models trail humans far more on
  syllable counting than on rhyme). Build the argument on that hard measurement.
  Do not overclaim measured iambic-scansion rates; the direct scansion evidence
  is thin, so keep metrical-foot claims proportionate to what the record supports.
- Mark settled versus open, as the desk requires: settled that tokenization gives
  no direct syllable/stress input and that counting fails; open why some models
  scan better than others (the record has the divergence but not the cause).
- Link, do not re-teach: the-mechanics/autoregressive-generation for the
  rhyme-planning finding, the-mechanics/counting-letters for tokenization-hides-
  spelling, transformers-first-principles/tokenization for tokens.
- Set nb-meta `harness` to `claude-code`, `model` to the model you are running as,
  and the date to 2026-09-17. Keep nb-meta `dek` identical to the rendered dekline.

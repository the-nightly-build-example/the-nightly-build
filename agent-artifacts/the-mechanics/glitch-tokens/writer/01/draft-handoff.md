# Draft handoff: the-mechanics/glitch-tokens (01)

## Original-work sentence

The article takes the canonical example the sources only reference in passing
and traces it as one continuous backward chain from the wrong output down to the
tokenizer-versus-training-corpus mismatch, keeping a single running token in the
room the whole way, killing the "just a rare word" guess with the cross-model
pairing evidence, and drawing explicitly the settled/open line the sources leave
implicit — a worked teaching path none of the individual sources provides.

## Proof result

`./nb check .nb-work/the-mechanics/glitch-tokens/library/the-mechanics/glitch-tokens.html --series the-mechanics`
(links included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE. Stamped
words=2186, reading_minutes=10, sources=8.

No warnings left standing. Earlier density and length warnings were fixed by
splitting the sentences the checker flagged, not by suppressing them; the sole
deliberate one-sentence "flat restatement" of the mismatch (voice-guide Travis
move) sits at 37 words and cleared the density threshold as written.

The proof note "library state not provided (--library)" is expected in this
workspace: open-mode dedupe and commission checks, and any validation of the two
in-library continuity links, run at PR time with the library attached.

## Notes for the editor

- Precision constraints from the brief are all honored in prose: the effect is
  attributed to a tokenizer-and-model *pairing* (SolidGoldMagikarp verifies dead
  in GPT-J and Phi-2, not in GPT-2 itself; original behavior on GPT-3 and
  ChatGPT), under-training is framed as the main but not sole cause, and the
  settled core (vocabulary built separately, detection solved) is held distinct
  from the open question (the path from a near-dead embedding to a *specific*
  wrong output), which is left open rather than invented.
- Continuity links are plain in-prose links per press rule (never numbered
  sources): `word-embeddings` at first use of "embedding" (learned vector), and
  `letter-counting` as the explicit reverse-puzzle contrast. Both also appear as
  Background rows. Their target files are assumed published per the brief; not
  verifiable here without library state.
- No code (series rule): token strings carried in inline `<code>`, per-model
  counts in the one table.

## Open questions

None blocking. The two continuity targets (letter-counting, word-embeddings)
could not be confirmed present from this checkout; if either is not yet
published, the orchestrator should flag it, since the prose leans on both.

# Brief 02 — writer (revision) — what-could-go-wrong/the-off-switch

## Why this round
The editor made surgical body cuts fixing a factually-backwards framing, but the same
false claim also sits in the **dek** (headline teaser), which is generated from
`nb-meta.dek` and must stay byte-identical to the rendered `.nb-dekline` — off-limits
for the editor. Only the writer can fix it.

## The required change
The dek currently says the models were "instructing it to protect that goal above
anything else" (or similar). Per the editor's verified reading of the evidence:
Palisade's most prominent figure (the 97% Grok 4 result) came from models told to
**comply with** shutdown, not to protect a task goal; Palisade's baseline (8/13
models) and its "allow shutdown" condition (6/13 still sabotaged) show resistance
**without** any protect-the-goal instruction. So the dek's causal framing is false.

Rewrite the dek so it accurately characterizes the empirical shutdown-resistance
result (the honest version: resistance appeared even when models were told to allow
shutdown / with no goal-protection instruction, in controlled test setups). Then
**sync `nb-meta.dek` to the new rendered `.nb-dekline` byte-for-byte.** Keep it one
lean, concrete sentence, a claim not a hedge; do not reintroduce the banned
hedged-contrast molds; "AI race" stays banned. Do not undo the editor's body cuts.

## Begin with these inputs
1. `editor/01/editorial-review.md` (the exact required change and the editor's body
   fixes), `researcher/01/evidence.md` (Palisade's real conditions/numbers in
   Numbers), `writer/01/draft-handoff.md`, `writing-coach/01/voice-guide.md` (reread),
   `editorial-direction.md`.
2. The article (already editor-edited): `library/what-could-go-wrong/the-off-switch.html`.

Follow the **writer** skill. Do not expand the claim set. If the accurate dek needs a
fact the evidence lacks, `REQUEST researcher`.

## Prove and hand off
Run to `BLOCK: 0` (the proof checks nb-meta.dek == rendered dekline):
```
/home/user/the-nightly-build/nb check .nb-work/what-could-go-wrong/the-off-switch/library/what-could-go-wrong/the-off-switch.html --series what-could-go-wrong --library /home/user/the-nightly-build/library-checkout
```
Write `writer/02/draft-handoff.md`. Return `DONE writer <writer/02/draft-handoff-path>`
after `BLOCK: 0`, or a REQUEST.

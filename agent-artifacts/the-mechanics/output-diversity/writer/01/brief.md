# writer brief: the-mechanics/output-diversity (01)

Inputs (artifact root is this file's grandparent directory):
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity
- ../../commission.md — the assignment and its boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete claim set; treat as evidence, not prose
- The initialized article: /home/user/the-nightly-build/.nb-work/the-mechanics/output-diversity/library/the-mechanics/output-diversity.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/output-diversity/.nb-context/

Output: draft-handoff.md (this directory)

Proof (run from /home/user/the-nightly-build; iterate with `--no-check-links`, run `nb stamp` before the final pass, then run with links until `BLOCK: 0`):

```
./nb check .nb-work/the-mechanics/output-diversity/library/the-mechanics/output-diversity.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/6299876f-cc26-50aa-a765-ad85a93ca3c3/scratchpad/library-checkout
```

This round's focus:
- Publication date is 2026-09-19. Set nb-meta `date` to it, `harness` to "claude-code", and the writer `model` to the exact model you run as (e.g. `claude-opus-4-8`).
- Correctness the evidence record insists on:
  - Claim the narrow thing: alignment narrows word- and structure-level (lexical/syntactic) variety and concentrates modes. Do NOT claim it reduces every measure of diversity — Shypula et al. found preference-tuned models score *higher* on "effective semantic diversity" among high-quality outputs. State this honestly; it sharpens the lesson rather than breaking it.
  - Attribute the narrowing to reward maximization under a KL constraint, not to the KL penalty itself (Kirk found a larger KL penalty lowered diversity further, so the penalty is a leash, not the narrowing force).
  - Use the measured numbers from the sources that own them (Padmakumar & He on inter-author similarity; Wu et al.'s sentiment-bin collapse 2.8%/5.9%/82.1%/100%; the temperature-mitigation limits). Kirk et al.'s diversity figures have broken y-axes — do not quote an exact number from it; use it for the qualitative "across-input mode collapse" point. Mohammadi's exact entropy values are not quotable (only the direction and the ~2.32-bit ceiling).
  - Present the recurring-name ("Elara") tendency as documented but inconsistent across model versions, not a universal constant.
- No code, per the desk. Link (don't re-teach) the sampling-temperature lesson for the temperature-vs-narrowed-distribution distinction.

Recent shapes to break (do not inherit from the recent library):
- Deks compressed into one long causal "so" sentence.
- Headings that pose a question or lead with a number every time; vary construction.
- The recurring furniture stack (nb-stat-strip, nb-table, nb-note, nb-holdsup). Plan furniture from the supplied catalog for this piece.

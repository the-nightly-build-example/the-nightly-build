# writer brief: when-ai-breaks/amazon-rekognition-congress (01)

Inputs (artifact root is this file's grandparent directory):
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity
- ../../commission.md — the assignment and its boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete claim set; treat as evidence, not prose
- The initialized article: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-rekognition-congress/library/when-ai-breaks/amazon-rekognition-congress.html
- Template context: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-rekognition-congress/.nb-context/

Output: draft-handoff.md (this directory)

Proof (run from /home/user/the-nightly-build; iterate with `--no-check-links`, run `nb stamp` before the final pass, then run with links until `BLOCK: 0`):

```
./nb check .nb-work/when-ai-breaks/amazon-rekognition-congress/library/when-ai-breaks/amazon-rekognition-congress.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/6299876f-cc26-50aa-a765-ad85a93ca3c3/scratchpad/library-checkout
```

This round's focus:
- Publication date is 2026-09-19. Set nb-meta `date` to it, `harness` to "claude-code", and the writer `model` to the exact model you run as (e.g. `claude-opus-4-8`).
- Correctness the evidence record insists on: the demographic-gap figures (Gender Shades 34.7% vs 0.8%; Rekognition 31.37% vs 0.0%) measure gender *classification*, a different task from the one-to-many face *matching* behind the 28 congressional matches. Use them only to establish that measured gaps exist; NIST's demographic study carries the matching gap in general but did not test Rekognition (Amazon declined to submit). Never present a classification error rate as Rekognition's match-error rate. The ACLU's 28-match demographic skew is a description of those 28 matches, not a calibrated per-group rate.
- The threshold story is well sourced (default 80% vs Amazon's recommended 99%, and Amazon's own numbers shifting 85%/95%/99%); the gallery was ~25,000 photos over 535 members of Congress. Keep the July 2018 date (MIT Technology Review misdates it to 2019 — do not follow it).

Recent shapes to break (do not inherit from the recent library):
- Deks that name actor and harmed party in one loaded sentence in the recent house shape; keep the dek's work but find its own form.
- Headings that lead with a number or use the comma-and contrast; vary construction.
- The recurring furniture stack (nb-note, nb-figure, nb-stat). The threshold/gallery-size point may earn a small table or figure; plan furniture from the supplied catalog rather than by reflex.

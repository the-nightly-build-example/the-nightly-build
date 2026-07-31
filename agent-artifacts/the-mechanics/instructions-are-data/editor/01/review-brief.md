# Review brief 01 — editor — the-mechanics/instructions-are-data

## Begin with these inputs
- this brief; `editorial-direction.md`; the exact writer brief `writer/01/brief.md`;
  `writing-coach/01/voice-guide.md`; `researcher/01/evidence.md`;
  `writer/01/draft-handoff.md` (original-work sentence at third read only);
  article `library/the-mechanics/instructions-are-data.html`; `.nb-context/`.

Follow the **editor** skill (Skill: `editor`; fallback file). Three ordered reads;
surgical edits only.

## Watch especially for this piece
- **Skeptic:** this is a mechanistic claim, so test the *mechanism*, not just
  citations: is each step true and in the right order (one flat token stream → no
  architectural instruction/data boundary → obedience is trained → therefore
  injection)? Confirm the "who coined prompt injection and when" (Simon Willison,
  Sept 2022) and that the instruction-hierarchy paper is described as a mitigation,
  not a guarantee. Confirm **settled vs open** is marked honestly. Audit
  `data-nb-kind`.
- **Cut:** verify **no code** and no manufactured statistic. The assembled-prompt
  example is illustration — keep it if it carries the mechanism, cut if decorative.
  Cut any drift into the Gemini incident beyond one glancing sentence. No
  colon-subtitle headline.
- **Reader:** does the reader leave able to predict where a model can be steered by
  text it was only meant to read (the promised contribution)? Compare to original-work
  sentence. `machinery` is banned — flag any use.

## Output
`editor/01/editorial-review.md` (Skeptic/Cut/Reader, edits, required work, decision).
Return `DONE editor <path>` or a REQUEST.

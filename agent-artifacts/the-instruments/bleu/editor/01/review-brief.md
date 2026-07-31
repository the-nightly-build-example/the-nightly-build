# Review brief 01 — editor — the-instruments/bleu

## Begin with these inputs
- this brief; `editorial-direction.md`; the exact writer brief `writer/01/brief.md`;
  `writing-coach/01/voice-guide.md`; `researcher/01/evidence.md`;
  `writer/01/draft-handoff.md` (original-work sentence at third read only);
  article `library/the-instruments/bleu.html`; `.nb-context/`.

Follow the **editor** skill (Skill: `editor`; fallback file). Three ordered reads;
surgical edits only; never touch markup/scripts/styles.

## Watch especially for this piece
- **Skeptic:** re-derive the worked BLEU example yourself from the evidence record's
  Numbers — recompute the clipped n-gram precisions, brevity penalty, and final
  score, and confirm the article's numbers match the owning primary (Papineni 2002).
  Verify the 28.4 EN-DE figure against Vaswani 2017. Verify the Callison-Burch
  misranking claim's exact direction. Audit `data-nb-kind` (Papineni, Callison-Burch,
  Post, Vaswani are primary).
- **Cut:** the desk over-opens on a shocking swing; if the writer forced that shape,
  cut it. No colon-subtitle headline; dek is a claim. Check the n-gram counts live in
  a table/listing, not packed into prose.
- **Reader:** does the reader leave able to ask "measured how, against what
  references?" — the piece's promised contribution? Compare to the original-work
  sentence.

## Output
`editor/01/editorial-review.md` (Skeptic/Cut/Reader lines, edits, required work,
decision). Return `DONE editor <path>` or a REQUEST.

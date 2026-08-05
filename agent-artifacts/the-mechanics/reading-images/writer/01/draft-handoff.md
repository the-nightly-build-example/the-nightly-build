# Draft handoff: the-mechanics/reading-images (01)

## Original work

The article threads eight separate primaries into one unbroken descent from a
pasted photo down to the patch grid, and at the bottom it refuses the causal
punchline its sources invite: it holds the vendor-documented failures apart
from the patch mechanism and marks the link between them as an open question,
rather than fusing them into "the grid is why it miscounts." That move is
visible in the structure (the trace) and in the "Open question" note at the
foot of the last section.

## Proof

`./nb check ... --series the-mechanics --library /home/user/library-checkout`
(final pass, links included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE.
No warnings intentionally left standing. Word count landed at 2200, the top of
the lesson band.

## How the round's three corrections were honored

- **No patchify-causes-failure claim.** The failures are reported as empirically
  documented by the GPT-4V system card. The grid is framed as a bounded budget,
  not a ceiling (LLaVA-NeXT tiles for more detail; OpenAI's high/low-detail
  lever), and the resolution-improves-accuracy result is called a direction, not
  proof. The causal question is marked open in its own note.
- **196 is illustrative.** Stated plainly as "a teaching number, not what your
  chatbot actually runs," with the real range and OpenAI's own accounting
  (85 base + 170 per 512px tile; 1024x1024 = 765 tokens) as the checkable figure.
- **Closed models are undisclosed.** A dedicated caution paragraph: the system
  card discloses no encoder, patch size, or token count, so patchify-project-
  attend is taught as the field's documented method, not asserted of GPT-4o/
  Claude/Gemini.

## Open evidence or voice questions

- None blocking. The genuine open item (why the failures happen at the patch
  level) is the lesson's content, marked open per the series rule, not a hole in
  the evidence. The evidence record supplied everything the piece needed; no
  researcher request was raised.
- One editorial judgment to sanity-check: the closing ties this lesson's
  "coarse grid loses detail" to the earlier letter-counting lesson as an
  analogy (both are counting failures that follow from chunking). It is offered
  as a course tie-in, not a causal claim, and carries no citation; flagged here
  in case the editor reads it as reaching.
- Furniture is deliberately light for a 2200-word lesson: one source asset (ViT
  Figure 1, the patchify schematic, cropped to the patch-to-projection portion
  per the evidence record's crop note) and one "Open question" note. Both were
  chosen to carry the two loads the voice guide names (watch the mechanism;
  mark settled vs open).

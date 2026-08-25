# Commission: the-evidence/clip

## Assignment
Read the CLIP paper for the reader: Alec Radford, Jong Wook Kim, and
colleagues at OpenAI, "Learning Transferable Visual Models From Natural
Language Supervision" (2021). One lesson, one document. State what CLIP is,
who built it, and why it became famous. Walk through what it actually did:
the 400-million image-text pairs it trained on, the contrastive objective
that paired an image with its caption, and the numbers it reported. Then
bring it to the present: how "CLIP" is invoked today (as an image-text
embedding, as a zero-shot classifier, as the text tower inside image
generators and retrieval systems) and where today's usage matches or
outruns what the 2021 paper measured.

## The angle this lesson owns
The famous headline is CLIP's "zero-shot" transfer: matching a supervised
ResNet-50 on ImageNet with no ImageNet training labels. The lesson's job is
to show the reader the foundation under that claim honestly. Three things
the shorthand drops:
- The zero-shot ImageNet number depended on prompt engineering and
  ensembling (the "a photo of a {label}" templates), worth several points;
  the bare label prompt scored lower.
- The training set (WIT, 400M pairs) was proprietary and never released, and
  its scale, not a new idea, is much of what made CLIP work; contrastive
  image-text learning predates it.
- CLIP's robustness and zero-shot strength are uneven across tasks: strong on
  some distribution shifts and natural-image classification, weak on abstract,
  systematic, or fine-grained tasks (counting, satellite imagery, specialized
  medical/aerial classes) the paper itself reports.
Decide the short teach list from the evidence; do not force all three if the
piece teaches two of them completely.

## Boundaries
- Teach the document, not the field. Do not turn this into a survey of
  multimodal models.
- Neighbor tonight (do not overlap, do not hard-link across the edition):
  `the-mechanics/text-in-images` runs the same night and will explain why
  image generators can't spell, touching text encoders. This lesson stays on
  the 2021 CLIP document and its own numbers. Do not drift into image
  generation, diffusion, or embedding-leaderboard territory.
- Reader profile is the course reader: smart, widely read, no time in a
  codebase. `word-embeddings` and `reading-images` are already taught in
  the-mechanics; link them in Background rather than re-teaching vectors or
  how a model reads an image.

## Required contribution
The article must do something to the evidence the evidence does not do
itself: hold CLIP's most-cited number (zero-shot ImageNet parity) against the
exact conditions the paper reports it under, so the reader can tell what
"zero-shot" bought and what it borrowed.

## Sources (researcher obligation)
Series/template floor: at least 6 sources, of which at least 3 primary and at
least 1 secondary. Primary here is the CLIP paper itself and its
appendices/figures; later primary work that confirmed, corrected, or extended
the zero-shot and robustness claims (for example follow-ups on prompt
sensitivity, dataset contamination, or reproductions such as OpenCLIP/LAION)
counts as primary for its own claim. Read the paper's own numbers from the
paper, not from coverage.

## Recent shapes to break (the-evidence)
The section verified against recent library structure and prose:
- Recent evidence pieces open the body with a "the shorthand vs the reality"
  split, then a "What <authors> actually built" section, then a numbers
  table, then a "what inherited the name / what changed" section. Do not copy
  this shape by default; let CLIP's own argument set the sections.
- Avoid the heading mold "What <X> actually built/did/proved"; it recurs.
- Avoid the takeaway closer mold "When a claim about X reaches for Y, ask
  which of the two is really being described" and its cousins ("next time you
  hear X, ask Y"). It has recurred across recent editions.
- Deks: no comma-triad (three clauses joined with commas and "and"), no
  semicolon reversal, no suspended-question mold. Check recent deks.

## Production record
Harness: Claude Code subagents (isolated where available), orchestrated from
the scheduled run. Model/effort actually used, following the balanced
production policy (all stages "capable", not required):
- writing-coach: Claude Sonnet, low effort
- researcher: Claude Opus, high effort
- writer: Claude Opus, medium effort
- editor: Claude Opus, high effort
No required model/effort directive existed to trade down.

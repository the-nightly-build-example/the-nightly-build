# writer brief: the-evidence/gpt-2 (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- ../../commission.md — the document, the angle, source direction, nb-meta values.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only from it.
- ../../../../.nb-context/ — the effective template contract and runtime assets.
- ../../../../library/the-evidence/gpt-2.html — the initialized article to edit in place.

Output: ./draft-handoff.md (the original-work sentence, the proof result with any
warning intentionally left, and any open evidence/voice question).

Proof (run from repo root, iterate with --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/the-evidence/gpt-2/library/the-evidence/gpt-2.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/53d4ed2b-ac4b-53e6-97a0-447483501c29/scratchpad/library-checkout --no-check-links`
- Final: same command WITHOUT `--no-check-links`, plus `./nb stamp` first, until `BLOCK: 0`.

nb-meta to fill: date `2026-08-11`, harness `claude-code-routine`, model
`Claude Opus 4.8`, and three descriptive tags (this open series configures no tag
fragments, so set sensible topical tags in nb-meta directly, e.g. gpt-2, the
language-model lineage, and the release decision). Keep nb-meta `dek` identical to
the rendered dekline.

This round's focus: hold the paper's measured results and its fame apart. The body
teaches what the document actually did (WebText, the model sizes, which numbers
are zero-shot language modeling and which are weak downstream results) with honest
scale, then what the release documents claimed and what the six-month follow-up
found. Link `the-evidence/gpt-3-few-shot` and `the-evidence/scaling-laws-kaplan`
in Background rather than re-teaching them; do not re-explain in-context learning
or the transformer. Link only already-published library pages — do NOT link
tonight's sibling articles.

Habits not to inherit (these are house formulas the last three articles per desk
all share; a reader flipping two pieces sees the scaffolding):
- Do not end the "Why this matters" opener with a "By the end you will be able
  to..." promise, nor lead it with "This lesson shows/builds/takes apart...".
- Do not land "The takeaway" on a second-person "next time you meet one, ask
  [N questions]" portable checklist. Find this lesson's own resolution.
- Do not make the final move the "demonstrated-vs-unproven / settled-vs-open"
  sort, and never write "still an open question, and more than one serious answer
  is on the table" or a "which of the two you are looking at" line.
- Do not use "this desk" as self-reference anywhere; the body narrates no one.
- The-evidence's recent dek mold is "[names] reported X in [year], and later
  analyses found Y" (a concessive second clause that reverses the first). Write a
  dek that is not built that way. Vary headings away from the desk's "The X that
  Y" relative-noun-phrase and the "noun, the appositive" comma mold.

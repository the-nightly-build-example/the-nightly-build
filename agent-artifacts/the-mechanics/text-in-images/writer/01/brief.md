# writer brief: the-mechanics/text-in-images (01)

Inputs:
- editorial-direction.md (artifact root): house standard, voice, lesson
  template rules, the-mechanics series prompt.
- commission.md (artifact root): the causal chain to walk, boundaries, and
  the "Recent shapes to break" notes.
- writing-coach/01/voice-guide.md: how this piece should sound.
- researcher/01/evidence.md: the complete claim set. Use its Numbers section
  exactly; address every item in its Contradictions in the prose.
- The initialized article to edit in place:
  .nb-work/the-mechanics/text-in-images/library/the-mechanics/text-in-images.html
- Template contract and furniture under
  .nb-work/the-mechanics/text-in-images/.nb-context/

Output: agent-artifacts/the-mechanics/text-in-images/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build; iterate with --no-check-links, then
final with links):
  ./nb check .nb-work/the-mechanics/text-in-images/library/the-mechanics/text-in-images.html \
    --series the-mechanics \
    --library /tmp/claude-0/-home-user-the-nightly-build/795ad1d0-7e30-55f8-9f00-32962f849f5d/scratchpad/library-checkout
Drive to BLOCK: 0. Run `./nb stamp <article>` before the final check.

This round's focus (do not overclaim the keystone):
- The failure is set at the text encoder before any pixel is drawn — that is
  the lesson's spine. But hold two qualifications the evidence records: the
  encoder governs whether the model KNOWS the letters, while the diffusion
  decoder governs whether it can SHAPE and PLACE them (this is the settled-vs-
  open line the series wants); and a character-blind model at very large scale
  can recover near-perfect spelling, so the letters are degraded and expensive
  to reach, not literally erased.
- Keep two distinct levers distinct: encoder SIZE (Imagen's large T5) and
  encoder TYPE (character-aware ByT5). Do not conflate them.
- Background links point only to already-published lessons (`image-generation`,
  `letter-counting`, `word-embeddings`, `reading-images`). Do not link
  tonight's unpublished `the-evidence/clip`; CLIP may be named inline and
  cited as a source only.
- No code (series rule).

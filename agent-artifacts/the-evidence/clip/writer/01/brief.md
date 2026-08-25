# writer brief: the-evidence/clip (01)

Inputs:
- editorial-direction.md (artifact root): house standard, voice, lesson
  template rules, the-evidence series prompt.
- commission.md (artifact root): the angle, the teach list, boundaries, and
  the "Recent shapes to break" notes for the-evidence.
- writing-coach/01/voice-guide.md: how this piece should sound.
- researcher/01/evidence.md: the complete claim set. Use its Numbers section
  exactly; address every item in its Contradictions in the prose.
- The initialized article to edit in place:
  .nb-work/the-evidence/clip/library/the-evidence/clip.html
- Effective template contract and furniture catalogs under
  .nb-work/the-evidence/clip/.nb-context/

Output: agent-artifacts/the-evidence/clip/writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links,
then final with links):
  ./nb check .nb-work/the-evidence/clip/library/the-evidence/clip.html \
    --series the-evidence \
    --library /tmp/claude-0/-home-user-the-nightly-build/795ad1d0-7e30-55f8-9f00-32962f849f5d/scratchpad/library-checkout
Drive it to BLOCK: 0. Run `./nb stamp <article>` before the final check.

This round's focus (decisions the inputs leave to you):
- The evidence credits two findings that cut against a purely deflationary
  read: CLIP's genuine robustness to natural distribution shift, and its own
  train/test contamination audit showing near-zero effect. Credit both in the
  prose; the piece must not read as "it was only prompts and scale."
- Background links point only to already-published lessons (e.g.
  `word-embeddings`, `reading-images`). Do not link tonight's unpublished
  sibling lessons.

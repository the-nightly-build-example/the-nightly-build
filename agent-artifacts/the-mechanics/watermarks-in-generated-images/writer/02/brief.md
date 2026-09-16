# writer brief: the-mechanics/watermarks-in-generated-images (02, revision)

Inputs:
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/editor/01/editorial-review.md` — apply every required item; the editor's direct edits are already in the article
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/editorial-direction.md`
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/writing-coach/01/voice-guide.md`
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/researcher/03/evidence.md` — the current evidence record (adds the SD model-card filtering facts and the Somepalli et al. eighth source; supersedes researcher/01 and 02)
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/commission.md`
- `.nb-work/the-mechanics/watermarks-in-generated-images/library/the-mechanics/watermarks-in-generated-images.html` — the editor-edited article to revise in place
- `.nb-work/the-mechanics/watermarks-in-generated-images/.nb-context/`

Output: `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/writer/02/draft-handoff.md`

Proof: `./nb check .nb-work/the-mechanics/watermarks-in-generated-images/library/the-mechanics/watermarks-in-generated-images.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`
(iterate with `--no-check-links`; final with links to `BLOCK: 0`.)

Required items to apply (from the editorial review, all now supported by
researcher/03's evidence):
1. Correct the false "never filtered / nothing removing it / absence of any
   filter" claim. The evidence record now carries the staged account from Stable
   Diffusion's own model card: the base checkpoint trained on unfiltered
   LAION-2B-en, later checkpoints used an aesthetics subset filtered to an
   estimated watermark probability below 0.5, but every later checkpoint resumed
   from that unfiltered base, and 0.5 is a permissive, probabilistic threshold.
   Rewrite the relevant sentences so the mechanism reads correctly: filtering was
   partial in scope, permissive, and probabilistic, which is exactly why a
   low-frequency ghost watermark survives, rather than "no filter at all."
2. Rewrite the leaked sentence "Nothing below that level changes the answer" in
   the article's own terms (it lifts the commission's phrasing).
3. Cite the eighth primary the record now supports (Somepalli et al., CVPR 2023)
   where it belongs, clearing the source-floor warning; number sources in
   first-citation order and set its data-nb-kind honestly.

Preserve all settled work and the editor's direct edits (the corrected source-4
author and the rewritten bookend opener). Keep the two mechanisms distinct and the
Getty allegation attributed to Getty. Do not expand the claim set beyond the
record. Rerun the full proof to BLOCK: 0 and nb stamp if counts shift.

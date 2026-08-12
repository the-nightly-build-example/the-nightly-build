# writer brief: the-mechanics/image-generation (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/editorial-direction.md
  — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/commission.md
  — the behavior, the angle, source direction, nb-meta values.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/writing-coach/01/voice-guide.md
  — how this piece should sound; read before drafting and before every revision.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/researcher/01/evidence.md
  — the complete claim set; cite only from it.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/.nb-context/
  — the effective template contract, runtime assets, and furniture catalogs.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/library/the-mechanics/image-generation.html
  — the initialized article to edit in place.

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/writer/01/draft-handoff.md
(the original-work sentence, the proof result with any warning intentionally left, and any open evidence/voice question).

Proof (run from repo root /home/user/the-nightly-build, iterate with --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/the-mechanics/image-generation/library/the-mechanics/image-generation.html --series the-mechanics --library /home/user/library-checkout --no-check-links`
- Final: the same command WITHOUT `--no-check-links`, and run `./nb stamp .nb-work/the-mechanics/image-generation/library/the-mechanics/image-generation.html` first, until `BLOCK: 0`.

nb-meta to fill: date `2026-08-12`, harness `claude-code-routine`, model
`Claude Opus 4.8`, and three descriptive tags (this open series configures no tag
fragments; set sensible topical tags directly, e.g. diffusion, image-generation,
denoising). Keep nb-meta `dek` identical to the rendered dekline.

This round's focus: the spine is that the picture is built by removing noise, not
by drawing, and every step earns its place by serving that. Work backward from the
finished image as the voice guide directs. Teach, in order the reader needs them:
what comes out and the noise underneath; that the model was trained to predict the
noise added to an image; that generation starts from pure noise and applies the
denoiser over many small steps; how the encoded prompt steers each step and what
the guidance control does; and the latent-space efficiency step. Hit ground at
"the network only ever learned to predict noise," and mark settled steps apart
from open ones (why text-in-images and spatial-relation failures happen is a
hypothesis in the sources, not settled).

Two refinements from the evidence record you must not flatten (both are in its
Contradictions/Numbers sections):
- Latent-versus-pixel is a real fork. Denoising in a compressed latent space is
  Stable Diffusion (Latent Diffusion); Imagen and DALL-E 2 denoise in pixel space
  with a resolution cascade. The text encoder likewise varies (a BERT-style
  encoder in the Latent Diffusion paper, CLIP in released Stable Diffusion, a
  frozen T5-XXL in Imagen). Teach the latent step as one common design, not as
  what every system does.
- Paper numbers are not product numbers. DDPM's T=1000 steps is not the ~50 of a
  deployed run, and the classifier-free-guidance weight w is offset by one from a
  product's guidance_scale (default 7.5 in Stable Diffusion). If you give a step
  count or a guidance number, say whether it is the paper's or a product's, and do
  not equate them.

Link `the-mechanics/reading-images` in Background (how a model reads an image it
is given) and, if useful for contrast, `the-evidence/gans` (the earlier
adversarial approach). Do not re-teach either. Link only already-published library
pages — do NOT link tonight's sibling articles.

Furniture: plan prose and furniture together from the catalogs under `.nb-context`.
A numbered-steps or figure component may suit the denoising loop if it earns its
place; use documented markup only, and add nothing that has no clear purpose. If a
chart would help, note that the evidence record has no digitized numeric series
for one, so do not invent data.

Habits not to inherit (house formulas the recent library shares across desks; a
reader flipping two lessons sees the scaffolding):
- Do not open "Why this matters" on a nostalgic or second-person recall ("If you
  have heard one thing about...", "You may remember when..."), and do not pivot the
  opener on "This lesson shows/reads/follows...". The bookends may address the
  reader; find a fresh way in.
- Do not close the opener on a "set the two things side by side" line, and do not
  land "The takeaway" on a "So next time you [see/meet] one..." portable rule.
  Find this lesson's own resolution.
- Do not use "this desk" or any self-reference in the body; the body narrates no
  one.
- The-mechanics recent dek mold is "To [do everyday thing], [mechanism], the fact
  underneath [two familiar phenomena]" (and the bare "To [verb], [mechanism]"
  opener). Write a dek not built that way. Vary section headings away from the
  "The X that Y" relative-noun-phrase mold and the "noun, the appositive" comma
  mold; each heading is a step in this lesson's own nouns, no scaffolding slots
  ("How it works", "Background", "Why it matters").

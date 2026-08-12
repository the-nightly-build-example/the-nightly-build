# editor review-brief: the-mechanics/image-generation (01)

Inputs (read in the order your skill names):
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/writing-coach/01/voice-guide.md — read first.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/commission.md — the assignment, its boundaries, the reader's situation.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/writer/01/brief.md — the exact writer brief (to catch leakage and habits).
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/researcher/01/evidence.md — open when the first read calls for it.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/writer/01/draft-handoff.md — original-work sentence, open only on the third read.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/library/the-mechanics/image-generation.html — the article to edit in place.
- template context under /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/.nb-context/.

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/editor/01/editorial-review.md

After any direct edits you make, the orchestrator runs `nb stamp` and `nb check`
before the PR; you do not run the proof. Route to the writer only what needs new
reporting or a redraft.

## Recent-pattern notes (catch formula against these; one article cannot show it)

Cross-desk house formulas this run is deliberately breaking — flag any that survived:
1. "Why this matters" opening on a nostalgic or second-person recall, or pivoting
   on "This lesson shows/explains/takes apart...".
2. The opener closing on a "set the two things side by side" line.
3. "The takeaway" landing on a "So next time you [see/meet]..." portable rule.
4. "this desk" or any body self-reference; the body narrates no one.

the-mechanics-specific molds: the recent dek mold is "To [do everyday thing],
[mechanism], the fact underneath [two familiar phenomena]" (and the bare "To
[verb], [mechanism]" opener); recent headings lean on "The X that Y"
relative-noun-phrases and the "noun, the appositive" comma mold. A dek or heading
built like those is a formula even if sharp.

## Round focus

Verify the piece is a mechanism worked backward from the behavior, that it hits
ground (the network only ever learned to predict noise), and that it marks settled
steps apart from open ones. Check these evidence-record boundaries survived:
- Latent-versus-pixel is a real fork: denoising in a compressed latent space is
  Stable Diffusion (Latent Diffusion); Imagen and DALL-E 2 denoise in pixel space
  with a resolution cascade, and the text encoder varies (BERT-style in the Latent
  Diffusion paper, CLIP in released Stable Diffusion, frozen T5-XXL in Imagen). The
  draft must teach the latent step as one common design, not as universal.
- Paper numbers are not product numbers: DDPM's T=1000 is not a deployed run's ~50,
  and the classifier-free-guidance weight is offset by one from a product's
  guidance_scale (default 7.5). Any step count or guidance number must say whether
  it is the paper's or a product's and not equate them.
- The causes of failures like garbled in-image text or muddled spatial relations
  are offered by the sources as hypothesis, not settled mechanism; the draft must
  mark them open.
"No code" is a hard series rule; flag any code or pseudocode. Audit every
data-nb-kind (each method paper's authors are primary for their own method).
Confirm the three ordered reads, edit directly what is yours, route only what needs
reporting, and record every change.

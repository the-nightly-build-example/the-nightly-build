# researcher brief: the-mechanics/image-generation (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/editorial-direction.md
  — citation standard, series territory, declared reader.
- /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/commission.md
  — the behavior, the angle, and the named sources to read first.

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/image-generation/agent-artifacts/the-mechanics/image-generation/researcher/01/evidence.md

Proof of your own record: every URL you record must resolve to the source's own
page (arXiv abstract or PDF, proceedings page), not a fetch endpoint; every claim
the mechanism rests on must be traced to the paper that owns it; nothing may
appear that you did not open. The writer and editor will cite only from this
record.

This round's focus: the lesson is a mechanism explained backward from the
behavior, so the evidence must let the writer name each real step and mark it
settled or open. Establish firsthand, from the primary papers: (1) the training
objective, that the model is trained to predict the noise added to an image
(equivalently a denoising target), and how the amount of noise is parameterized
over steps; (2) the generation procedure, starting from pure noise and applying
the learned denoiser over many small steps; (3) how text conditioning enters the
denoiser at each step, and what the guidance control does (classifier-free
guidance); (4) latent-space diffusion, denoising in a compressed space and
decoding to pixels. For each, record what the source states plainly and, where
relevant, a real number (typical step counts, resolution, latent downsampling
factor). Note honestly which steps the sources treat as settled and where they
name open problems (for example why text rendering or spatial relations fail).
Record differences between systems (pixel-space DDPM versus latent diffusion; CLIP
versus a large text encoder) rather than flattening them.

Do not cite tonight's sibling articles; link targets for the writer must be
already-published library pages only.

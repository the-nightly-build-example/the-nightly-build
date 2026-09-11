# writer brief: the-evidence/latent-diffusion (01)

Inputs:
- editorial-direction.md (house standard, slop/headline rules, press voice, lesson identity, The Evidence prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; read before drafting)
- researcher/01/evidence.md (the complete claim set; use its Numbers section exactly; address its Contradictions)
- commission.md (assignment, boundaries, original-contribution target)
- the initialized article at library/the-evidence/latent-diffusion.html (edit in place; keep chrome exact)
- effective template contract and furniture catalogs under .nb-context/

Output: writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build):
  ./nb stamp .nb-work/the-evidence/latent-diffusion/library/the-evidence/latent-diffusion.html
  ./nb check --series the-evidence --library /home/user/library-checkout .nb-work/the-evidence/latent-diffusion/library/the-evidence/latent-diffusion.html
(iterate with --no-check-links; final proof with links, to BLOCK: 0)

This round's focus (from the researcher's report; detail in the evidence file):
- The cost reduction is architectural and relative. The paper's "hundreds of GPU-days" is a
  pixel-space baseline; Stable Diffusion itself still trained on 256 A100s. State the gain as
  the relative, latent-space saving it is; do not imply image generation became cheap in
  absolute terms.
- Keep the paper and the product distinct. The CVPR paper (CompVis) ran its own experiments
  (e.g., the LAION-400M text-to-image model); Stable Diffusion (the Aug 2022 release) is the
  product. The CSAM finding attaches to LAION-5B / Stable Diffusion 1.5, NOT to the paper's
  own LAION-400M experiments. Do not blur these.
- Litigation is not settled infringement. The UK High Court (Nov 2025) rejected the
  copying/storage theory (the weights do not store the training images); Getty's US complaint
  is an allegation. Report the state of the disputes precisely; claim no verdict the evidence
  does not carry. (The UK judgment is sourced via secondary analysis in the record; attribute
  accordingly.)
- CLIP has NO lesson in this library. Define the CLIP/text-encoder idea in plain words inline
  where the reader first needs it; do not link it as Background. Background links that DO
  exist: the-evidence/denoising-diffusion (the diffusion mechanism — link, do not re-teach),
  the-evidence/attention-is-all-you-need (attention/cross-attention), the-evidence/gans.
- FID table values were read via the ar5iv HTML mirror (PDF was gated); treat them as the
  record gives them.

Recent library shapes to break (keep required content):
- Dek: avoid the two-clause "claim, and/so the twist" mold (deepseek-r1's
  "...and the $5.6 million price tag belongs to a different model"), the comma-triad, and the
  "The [thing] that..." opener.
- Closing body heading: recent evidence pieces end on a terse verdict-of-reach heading; vary
  the build of your "how it holds up / what usage outran" heading, and avoid "The line the
  paper drew itself" (chain-of-thought used it).
- Orientation heading is its own concrete step, not a paraphrase of the headline.
- Furniture: a cost or FID comparison may genuinely want a small nb-stat-strip or nb-table;
  earn it rather than adding by reflex.

nb-meta: harness "claude-code"; model = the model you are actually running as (report it).
No charts or source assets unless the evidence record names an exact visual the argument spends.

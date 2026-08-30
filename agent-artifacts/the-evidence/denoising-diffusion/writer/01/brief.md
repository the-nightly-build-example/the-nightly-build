# writer brief: the-evidence/denoising-diffusion (01)

Inputs:
- editorial-direction.md (house standard, the paper's voice, The Evidence prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; exemplar passages)
- researcher/01/evidence.md (the complete claim set; use the Numbers section exactly)
- library/the-evidence/denoising-diffusion.html (the initialized article to edit)
- .nb-context/ (effective template contract, runtime assets, furniture catalogs)

Output: writer/01/draft-handoff.md
Article: /home/user/the-nightly-build/.nb-work/the-evidence/denoising-diffusion/library/the-evidence/denoising-diffusion.html
Proof: ./nb check .nb-work/the-evidence/denoising-diffusion/library/the-evidence/denoising-diffusion.html --series the-evidence --library /home/user/library-checkout

## This round's focus
Hold the article's one job: draw the exact line between what the 2020 DDPM paper
measured (unconditional or class-conditional, pixel-space, ~1000 sequential
sampling steps, the reported CIFAR-10 scores) and what the reader's picture of "a
diffusion model" (text-to-image, fast, photorealistic) actually owes to later
papers. The evidence record's Contradictions section carries a framing caution:
DDPM did not invent diffusion (Sohl-Dickstein 2015; Song & Ermon 2019), so
"founding document" must mean the modern image-generation wave, not the invention
of the method. Honor that precisely in the prose.

Link the-mechanics/image-generation and the-evidence/gans in Background at first
use rather than re-teaching them.

## Recent habits to break (do not inherit these from recent pieces)
- Do not end the "Why this matters" opener by telling the reader "By the end you
  will know / be able to …" — that syllabus-line closer recurs across recent
  articles. Let the takeaway resolve what the opener sets up instead.
- Do not open on a generic second-person everyday scene as a reflex; find this
  paper's own way in.
- Check the dek against spec/headlines.md's banned molds: no two-clause "and"
  contrast, no comma-triad ("A, B, and C"), no colon subtitle where the right
  half is atmosphere.
- Avoid the recent the-evidence headline shape "Tested on X…, Y now Z" (the
  then/now template) and a generic "The paper convinces without proving"-style
  heading. Write headings in this paper's own nouns; a reader skimming only the
  headings should reconstruct THIS argument.
- Vary heading construction; do not stack full declarative sentences all built
  the same way, and never join two clauses with comma+"and" as a house tic.

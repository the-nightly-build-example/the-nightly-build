# Writer handoff: the-evidence/denoising-diffusion (01)

## Original work
The article turns the evidence record's flat claim set into one argued line:
it traces each capability a reader attributes to "a diffusion model" (a typed
prompt, fast sampling, high resolution on modest hardware, photoreal
text-to-image) back to the specific later paper that added it, and uses DDPM's
own contribution quote to fix the "founding document" label to the modern
image-generation wave rather than to diffusion itself — a separation the
evidence supplies the parts for but does not itself draw.

## Proof result
Full `nb check` with links (`--series the-evidence --library
/home/user/library-checkout`): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
No warnings intentionally left. (Six W-SENTENCE-DENSITY warnings surfaced
mid-draft and were all resolved by splitting the long sentences; the final run
is clean.) Zero em-dashes; no banned-term counts triggered. Stamp:
words=1873, reading_minutes=8, sources=9 (8 primary arXiv papers, 1 secondary
Wikipedia entry for the Stable Diffusion release fact).

## Display-text self-test
- Headline, dek, and all four section headings check out against the evidence
  record (Ho/Jain/Abbeel, 2020, 32x32 CIFAR-10, state-of-the-art FID 3.17,
  T=1000). Every display-text claim is DDPM's own and attributed to source 1.
- nb-meta `dek` is byte-identical to the rendered dekline.
- Headline: single clause, actors carried into the dek, no colon/triad/
  question, distinct in content from the sibling GANs piece (its surprise is
  the prompt/conditioning gap, not blur). Dek: one sentence, no banned mold
  (name-list commas only, no clause triad, no two-clause "and" contrast).
- Recent-habit checks: no "by the end you will know" syllabus closer; opener
  leads on the paper's own surprising pictures, not a generic second-person
  scene; headings avoid the then/now "Tested on X, Y now Z" mold and the
  generic-verdict mold, and vary construction (declarative / noun phrase /
  negation / prepositional). Body carries no second-person address (the two
  bookends do, as the template allows).

## Open questions for the editor
- **Author affiliation** ("UC Berkeley," orientation): the evidence flags this
  as taken from the paper's title block but not re-fetched from the PDF in the
  research pass. Used as stated in the brief and evidence; low risk, worth a
  glance if the editor wants it airtight.
- **Classifier-free guidance date**: I used "2022" (arXiv posting, matching the
  brief's citation). The evidence notes the work first appeared at a NeurIPS
  2021 workshop; I left the workshop origin out for concision. Flagging in case
  the editor prefers the earliest-public-date gloss.

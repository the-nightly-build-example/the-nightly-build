# Editorial review: the-evidence/denoising-diffusion (editor/01)

## Skeptic

Thesis: the 2020 DDPM paper's real contribution was narrow and exact, the first
demonstration that a diffusion model generates high-quality images, done
unconditionally, in pixel space, at 32 by 32, over a thousand sequential steps,
and every capability a reader now files under "diffusion model" (a typed prompt,
speed, resolution, photorealism) arrived later, each from a named successor
paper. The piece stands on four claims.

1. DDPM was unconditional and could not take a prompt. Confirmed against the
   paper's own abstract ("the unconditional CIFAR10 dataset") and the evidence
   record, which searched for and found no conditional, latent, or few-step
   result inside the 2020 paper. The headline's surprise holds.

2. The headline numbers: state-of-the-art FID 3.17 and Inception 9.46 on CIFAR-10,
   with StyleGAN2+ADA at 9.74 / 3.26 and NCSN at 8.87 / 25.32 for scale; 1,000
   steps; ~300s per batch of 128, ~2.3s an image; 35.7M weights; 256x256 LSUN
   FIDs of 4.90 / 7.89 / 19.75. I opened the DDPM abstract and confirmed the 3.17
   / 9.46 sentence verbatim; every other figure matches the evidence record's
   Numbers section exactly. Arithmetic checks (300 / 128 = 2.34; 25.32 vs 3.17 is
   ~8x, and the article gives both figures so the reader can scale it). The FID
   figures carry their denominators (unconditional, 32x32 or 256x256, lower is
   better) and the Imagen 7.27 is correctly labeled a zero-shot COCO FID on "the
   same lower-is-better scale," not equated to the CIFAR-10 number.

3. The "founding document" framing is fixed to the modern image-generation wave,
   not the invention of diffusion. This is the article's whole value and it is
   handled precisely: "It founded something narrower, and said so," Sohl-Dickstein
   2015 credited for the idea, Song & Ermon 2019 for the score-matching footing,
   and the closing "fair for the modern wave of image generation. It is wrong for
   diffusion itself." Matches the evidence record's Contradictions caution word
   for word in substance.

4. The successor attributions. I opened all nine citation hrefs as the article
   prints them; each lands on its own source and supports its exact claim: DDIM
   (10x-50x faster, Oct 2020, four months after DDPM), Latent Diffusion (latent
   space + cross-attention text conditioning), classifier-free guidance (joint
   conditional/unconditional training), DALL-E 2 (CLIP-embedding prior + diffusion
   decoder), Imagen (frozen T5 encoder, COCO FID 7.27), Stable Diffusion release
   date and 2.4 GB VRAM from Wikipedia (secondary, correctly labeled). The
   evidence's caution that DDIM is a months-later successor, not a years-later
   one, is honored directly in the prose.

Display text: headline, dek, and all four subheads verified descriptor by
descriptor against the owning primary. Every `data-nb-kind` matches the evidence
record (eight primary arXiv papers by their own authors; the one Wikipedia entry
marked secondary and used only for a product-timeline fact). Both Background
links resolve to real library articles (the-mechanics/image-generation,
the-evidence/gans) whose subjects match their row descriptions.

Open question 1 (UC Berkeley affiliation, flagged as not re-fetched from the PDF):
it appears in body prose, not display text, and no argument rests on it. I
verified it rather than route it, the arXiv PDF title block and the BAIR
provenance both give all three authors at UC Berkeley. Claim holds; no change.

Open question 2 (classifier-free guidance dated 2022): the arXiv posting is July
2022 and the concept first appeared at a December 2021 workshop. The article
hangs nothing on 2022 being the earliest date, its only timeline claim is that
these capabilities arrived "over the two years that followed," which both dates
satisfy, and the conceptual ordering (guidance before the 2022 text-to-image
systems that use it) is correct on the 2021 origin. The earliest-public-date
gloss is not needed for honesty. Left as the writer set it.

No break found in any claim. No item routed.

## Cut

One slop pass sentence by sentence, then the edges, then the delete test. Three
sentences were touched; the piece is otherwise clean and disciplined, zero
em-dashes, colons only where they introduce a list or definition.

- Body self-reference. The orientation section closed on "and the distance
  between the two is the subject of this lesson." The lesson template permits
  self-reference only in the two bookend cards; the body speaks to no one and
  never names the lesson. Cut the clause; the sentence keeps its fact ("Almost
  everything else people now attach to the phrase 'diffusion model' came later,
  from other papers").

- Empty assessment at a paragraph edge. The 256x256 paragraph closed on "The
  paper's reach was real, and its ceiling was 256 pixels on a side, one class of
  image at a time." "Reach was real" is the empty-conclusion shape (idea +
  linking verb + assessment), and the reach was already stated at the paragraph's
  head. Cut to the concrete ceiling.

- Consistency, not slop. The 256x256 intro named "bedrooms, churches, and faces"
  but the FID line reports bedrooms, churches, and cats, leaving the cat figure
  without a category and faces without a number. Added "cats" to the intro list
  (the paper generated all four; the takeaway's "bedrooms and faces" needs faces
  to stay). Now every reported FID has a named home.

Checked but kept: "Fast sampling was not a later era. It arrived almost at once"
is earned negative parallelism, it corrects a real misconception the piece's own
timeline theme raises (that fast sampling was a distinct later wave) and carries
the four-month fact. "Rather than have the network predict the cleaned-up image
... predicts the noise" contrasts a genuine design alternative the paper itself
weighs, not an invented strawman. The stat strip, the "in the paper's words"
note, and the CIFAR-10 table each earn their place as deliberate emphasis or as
the right form for a comparison; none reads as a stacked block. No borrowed
phrasing from the Olah/Karpathy/Willison exemplars, and no prompt leakage, the
"typed prompt, fast render, photoreal face" framing reports the reader's own
situation, which the commission states and which is not a leak.

Edges, deks, and headings against the recent-pattern notes: the "Why this
matters" opener resolves into the thesis rather than a "by the end you will know"
syllabus line; it leads on the paper's own surprising pictures, not a generic
second-person scene. The dek is a single claim with no banned mold (no two-clause
"and" contrast, no comma triad, no atmosphere colon). The four headings vary in
construction, sit in the paper's own nouns, and reconstruct the argument when
skimmed. None matches the series' then/now or generic-verdict shapes.

## Reader

Read straight through as the paper's declared reader, someone smart and widely
read who keeps meeting "diffusion model" and cannot check it: what I have that
the sources alone would not give me is the exact seam between Ho, Jain, and
Abbeel's one result and the four or five later results my mental picture actually
runs on, each capability handed to the paper that added it, with dates that show
how fast the wave moved. No single source draws that line; it took reading DDPM
against seven successors. The draft-handoff's original-work sentence claims the
same thing, and the article delivers it. Both answers survive, so this is not a
restatement of its sources. The prose sits close to the voice-guide exemplars,
Karpathy's specific figures (3.17, 25.32, 300 seconds, 35.7M) and Willison's
marked correction of what "diffusion" has come to mean, not a median summary. The
headline reads true as the largest claim: the paper behind today's image
generators could not take a prompt.

## Edits

- Cut the clause "and the distance between the two is the subject of this lesson"
  from the orientation section (body self-reference, disallowed outside the
  bookends).
- Added "cats" to the 256x256 category list ("bedrooms, churches, cats, and
  faces") so the reported cat FID has a named category.
- Cut "The paper's reach was real, and its" from the 256x256 paragraph's closing
  sentence, leaving "The ceiling was 256 pixels on a side, one class of image at
  a time" (removed an empty-assessment edge, no fact lost).

## Required work

None. No item routed to researcher, writer, or orchestrator. The orchestrator
stamps the article after these edits (word count dropped slightly; nb-meta will
re-stamp).

## Decision

approve. Every claim verified against the opened primaries, the "founding
document" framing is correctly narrowed to the modern image-generation wave, and
the three issues found were fixable in place.

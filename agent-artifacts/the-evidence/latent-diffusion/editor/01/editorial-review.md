# Editorial review: the-evidence/latent-diffusion (editor/01)

## Skeptic

Thesis: the Rombach et al. paper made high-resolution diffusion affordable by
moving the denoising loop out of pixel space into the compressed latent space of
a once-trained autoencoder, and that academic method must be kept separate from
the Stable Diffusion product, to which the dataset and copyright troubles
actually attach. The piece states this cleanly and the headline, dek, and
section subheads each carry a real claim, not a label about the article's own
method.

Claims it stands on, and how each held:

- **Denoising ran over every pixel, and that was the cost.** Supported by the
  paper's own "hundreds of GPU days" line (s1, Sec. 1; confirmed on the arXiv
  abstract, which words it "consumes" while the Sec. 1 body the article quotes
  reads "takes"). The pixel arithmetic checks: 512 x 512 = 262,144 pixels, x 3
  channels = 786,432, so "more than 780,000 numbers" holds.
- **The autoencoder shrinks the image and the diffusion runs on the latent.**
  Supported by s1 (Sec. 3.1-3.2). f = 8 gives 64x fewer grid positions (8 squared);
  correct. The useful range "roughly four through sixteen" matches the record's
  LDM-{4-16} finding, and the ~38-point FID gap between f = 1 and f = 8 after 2M
  steps matches the Numbers section. The article keeps the paper's own caveats
  (reconstruction bottleneck, sampling slower than a GAN), so the efficiency
  claim is not overstated.
- **The prompt reaches the picture through cross-attention over an encoded
  prompt.** Supported by s1 (Sec. 3.3). The text-encoder identity (CLIP) is
  correctly attributed to the product's model card (s2), not to the paper.
- **The model people ran was a separate, larger training.** The 1.45B-parameter
  LAION-400M academic model (s1) versus SD v1.4 on 256 A100s, 225,000 steps at
  512px, LAION-5B subsets (s2). 512 / 8 = 64, so the "64-by-64 grid" is right. This
  is the spine of the lesson and it holds.
- **The troubles attach to the product's data.** The CSAM finding (3,226
  suspected entries, SD 1.5 named, LAION took the set down) is cited to the
  Stanford report (s4) and explicitly pinned to LAION-5B, not the paper's
  LAION-400M experiments. The copyright state is precise: Getty's US complaint is
  labeled an allegation (s5), and the UK High Court's November 2025 rejection of
  the secondary-infringement claim and the "weights do not store the images"
  finding are attributed "as reported" to the Latham & Watkins secondary
  analysis (s6), with a data-nb-note flagging para. 600 as reported rather than
  read. This is the round-focus item and it is handled correctly.

Cost discipline: no sentence claims image generation became cheap in absolute
terms. The paper-vs-product section and the takeaway both state the saving is
relative and that the product still took 256 high-end GPUs. The unsourced
"runs on a consumer/gaming GPU" capability is correctly absent; I did not add it
(it would need researcher evidence and is not publication-blocking).

Citation hrefs: I opened all seven as the article prints them. s1 (arXiv LDM),
s2 (SD v1-4 model card), s3 (Stability release announcement, Aug 22 2022), s4
(Stanford PURL record for the CSAM report), s6 (L&W analysis), and s7 (SDXL
arXiv) each land on the source itself and support the cited claim. s5 resolves
to the actual Getty complaint PDF (a ~1MB document); the fast reader could not
parse the binary, but the link lands on the source document and the evidence
record documents the "more than 12 million photographs" quote from it. The
data-nb-kind labels are correct: six primary, one secondary (s6), which is the
right call since s6 reports a judgment it did not itself issue. Source floor met
(7 sources, 6 primary, 1 secondary).

One correction made within scope: the FID table caption called MS-COCO and
ImageNet "the prompted rows," but ImageNet is class-conditional, not
text-prompted. Fixed to name the two rows plainly without altering any figure or
what is cited.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

The draft is already lean and mostly free of slop; the slop pass turned up a
small number of edge-sentence weaknesses rather than a pattern.

- Opener bookend: "Its one idea is easy to state and worth understanding" graded
  the idea before the colon delivered it. Cut "and worth understanding"; the
  payoff after the colon carries the sentence.
- Takeaway opener: "The whole of it is this." is an empty lead-in announcing a
  summary (the "here's the essence" family). Cut it; the takeaway now opens on
  the mechanism, which is stronger.
- Required CLIP fix (see Edits): the inline paragraph re-taught how CLIP is
  trained. Trimmed to the one clause the argument needs and replaced the
  re-teaching with a plain prose link to the-evidence/clip.

Two "X, not Y" constructions survive the negative-parallelism check because each
corrects the real, named misconception the lesson exists to fix: "belong to the
product... not to the paper itself" and "comes from the data the product was
trained on, not from the paper's way of making pictures." The paper-vs-product
confusion is the piece's subject, so these are earned, not reflex.

Formula check against the recent-pattern notes: the dek is an appositive, not
the flagged two-clause claim-and-twist mold, the comma-triad, or the "The
[thing] that..." opener. The closing heading "What the open weights set loose"
is a concrete consequence step, not the terse verdict-of-limits stamp to avoid,
and it is not "The line the paper drew itself." The orientation heading "Every
denoising step ran over every pixel" is its own concrete step, not a paraphrase
of the headline. Furniture is disciplined: one FID table that earns its place by
laying out four benchmark numbers the prose does not, and no reflex
nb-note/nb-stat-strip. The three other Background links (denoising-diffusion,
attention, gans) are used as prose links and are not re-taught.

No prompt leakage: the commission's "separate what the paper proved from what the
public release set loose" is present only as reworded reporting about the
subject, not as a lifted planning label. No borrowed phrasing from the
voice-guide exemplars; the grounding moves (262,144 pixels, 64x fewer positions)
are the article's own. Grammar and punctuation are clean; the caption fix also
removed two semicolons where periods belong.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: a single worked model of why latent-space
diffusion is cheaper (compress by f, denoise a 64x-smaller grid, decode once,
pay for the compressor only once) welded to a clean separation of the academic
method from the Stable Diffusion product, so I can place the CSAM finding and the
copyright fights on the product's LAION-5B data and read the legal record as
unresolved-and-partly-adverse rather than as proven infringement. The
original-work sentence in the handoff claims exactly this distinction as the
contribution, and it survives: the evidence record holds these as scattered
claims, and the article is where they become one usable idea. The prose sits
closer to the voice-guide exemplars than to a median summary, plain claims and
concrete anchors, feeling earned after the example rather than asserted.
Headline as the largest claim: "Stable Diffusion does its denoising on a
compressed grid, not the full image" is true (SD works on a 64x64 latent) and
concrete, and the contrast corrects the natural assumption that an image model
builds the full picture.

## Edits

- Conditioning section: replaced the inline CLIP re-teaching ("trained by
  matching captions to the images they describe... land near its numbers for a
  matching picture") with a plain prose link to the-evidence/clip and the single
  clause the argument needs ("a text encoder trained beforehand that turns a
  sentence into a list of vectors"); kept the s2 citation on the fact that Stable
  Diffusion uses CLIP.
- Why-this-matters Background band: added row 04 linking the-evidence/clip
  ("Prompt engineering lifted CLIP's zero-shot ImageNet score by nearly five
  points") with a one-line note that it is the text encoder turning the prompt
  into the vectors cross-attention reads.
- FID table caption: "The prompted rows, MS-COCO and ImageNet" changed to name
  the two rows without the "prompted" mislabel (ImageNet is class-conditional);
  replaced two semicolons with periods per house punctuation. No figure changed.
- Why-this-matters opener: cut "and worth understanding" from "Its one idea is
  easy to state and worth understanding."
- Takeaway opener: cut the empty lead-in "The whole of it is this."

## Required work

None blocking.

- writer/orchestrator: none required. The consumer/gaming-GPU capability line
  raised in the draft handoff stays out; adding it would need a primary or
  secondary VRAM source from the researcher, and it is not needed to publish.
- orchestrator: my edits change the word count and add an internal link, so the
  article needs a fresh stamp and link-check re-run before the PR. No content
  fix is pending; this is the routine post-edit proof.

## Decision

approve. The required CLIP fix and the round-focus checks (paper-vs-product,
cost discipline, precise legal state, verified numbers and hrefs) are all
satisfied; the only remaining step is the orchestrator's fresh proof over my
direct edits.

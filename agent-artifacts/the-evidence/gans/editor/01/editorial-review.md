# Editorial review: the-evidence/gans (editor/01)

## Skeptic

Thesis: the 2014 paper "Generative Adversarial Nets" invented adversarial
training, a real and lasting idea, but the object it actually produced was
small and blurry, judged by a metric its own authors disclaimed; the photoreal
faces its reputation evokes arrived three to five years later from other labs,
and GANs have since been overtaken by diffusion. The reader is meant to hold
the small 2014 object and the large 2026 reputation in one frame and separate
origin-of-technique (true) from origin-of-photoreal-images (false).

The load-bearing claims and how they held:

- **The origin distinction.** The piece keeps origin-of-technique and
  origin-of-photoreal cleanly apart and never lets "GANs made deepfakes" stand
  unqualified. "The 2014 paper is the correct origin of the technique. It is
  not the origin of the images people picture" states it in the body, and the
  takeaway repeats the qualification ("the accurate version is narrower: it
  made the training idea that, several inventions later, made them possible").
  The DCGAN(2015)->ProGAN(2017)->StyleGAN(2018/2019) lineage is presented as
  genuine GAN descent, matching the evidence record. Held.

- **Diffusion supersession.** "The leading image generators today are diffusion
  models, not GANs" is supported by s8 (DDPM 2020, "matched the best GANs") and
  s9 (title "Diffusion Models Beat GANs," FID 2.97 on ImageNet 128). The
  directional claim matches the source's own direction (its title says "Beat").
  Held. I checked "beating BigGAN-deep" against the evidence record's softer
  "matching"; the paper's title and FID comparison carry "beat," so the article
  is within the source's direction.

- **The numbers.** Title is "Nets," used correctly throughout (arXiv HTML
  mislabels it "Networks"; the article does not follow the mislabel). Parzen
  scores reproduced exactly: adversarial nets 225+/-2 on MNIST (first) and
  2057+/-26 on TFD (second, behind Stacked CAE 2110+/-50). The article states
  the TFD loss plainly ("came second, behind Stacked CAE"), which is the
  thin-foundation detail the brief wanted preserved. -log 4 = -1.386 checks.
  CIFAR-10 is correctly attributed to the dataset (32x32, cited to the dataset
  owner s4), and no resolution is attributed to the paper's own text; the
  article says outright CIFAR "received no score at all." Citation count is
  presented as order-of-magnitude (~97,000, Google Scholar, dated). All held.

- **Theory/practice gap.** Rendered in the paper's own terms: the optimum is
  stated as holding "in the space of probability density functions" (infinite
  capacity), the paper's concessions "introduces multiple critical points" and
  "no theoretical guarantees" are quoted, and the "Helvetica scenario" collapse
  is named. Held.

One break found and fixed. The orientation claimed the paper "ran eight pages
in the proceedings of the NIPS 2014 conference," but its own cited source (s3,
dblp) gives pp. 2672-2680, which is nine pages inclusive. I verified the page
range against dblp directly. This is a display-adjacent factual figure whose
cited source contradicts it, so I corrected both occurrences of "eight" to
"nine."

Display text audited descriptor by descriptor: headline, dek, all five
subheads, the figure caption, and the table caption. Goodfellow "and seven
coauthors" (eight authors) matches; "University of Montreal" is the English
name of Universite de Montreal; NIPS 2014 is the venue name as of 2014. The
figure caption's yellow-column claim ("the nearest real training image, printed
to show the model was not copying") matches both the paper's Fig. 2 caption and
the rendered image I inspected. data-nb-kind labels match the evidence record's
classes for all nine sources (7 primary, 2 secondary); the Google Scholar and
dblp entries are correctly secondary, and s4 uses the live cave.cs.toronto.edu
home rather than the redirecting address.

## Cut

Three direct changes, all cuts or a grounded factual correction, none crossing
into rewrite.

- **Self-narration that also announced the theme.** The orientation closed
  "...fits in those eight pages, and this lesson is about the distance between
  the two." The trailing clause both narrates the piece and announces the
  distance the voice guide explicitly says to let the facts carry "without the
  prose ever announcing the distance." Cut the clause; the sentence now lands on
  the concrete page count.

- **A self-grading, restating paragraph ending.** The proof section closed "It
  is a satisfying result: the method has a provable target, and the target is
  the truth." "It is a satisfying result" grades the material, and "the target
  is the truth" restates what the preceding sentences already stated ("follow
  the same distribution as the real data, matching it everywhere"). The concrete
  "minus log four, about minus 1.386" is the stronger close and is exactly the
  register the voice guide asks for. Cut the whole sentence.

- **Page count** corrected to "nine" in both places (recorded above under
  Skeptic).

The worst tell in the draft was the announced-distance clause: the one place
the prose reached to say the thing the voice guide wants shown. No repeated
structural formula surfaced. Section headings are five distinct argument steps
with no comma-and pair, no colon subtitle, and no scaffolding slot; the headline
avoids the "won on N GPUs" / "X on N of M" shape; the dek makes a claim about
the world and is not a "the real X was Y" reveal. The recent-pattern notes are
satisfied. Two semicolons appear ("catch fakes; the generator...", "no score at
all; it was shown..."); both are valid tight-parallel uses, not chains, so I
left them. The licensed forms clear their bars: the deadpan "Only one of them
assumes infinite room" and the authors' verbatim caveat both let a flat fact do
the deflating, and the direct-address moments ("The panel of faces is the one to
pause on") point at a specific described object. Furniture earns its place: the
asset carries the blurry-output argument prose cannot, the table carries the
TFD loss, and the note carries the metric caveat.

## Reader

Read straight through as the paper's declared reader, someone who has met the
GAN reputation everywhere and never opened the paper: what I have that the
sources alone would not give me is the paper's actual 2014 output (the blurry
Figure 2 panels, the two Parzen scores, the second-place finish on faces) set
directly beside the later photoreal dates and the 2021 diffusion result, so I
can size the fame against the evidence and separate the technique's origin from
the images' origin. The original-work sentence in the draft handoff claims
exactly this, and it survives the read. Both answers hold. The prose sits
clearly closer to the voice-guide exemplars than to a median summary: it grants
the achievement in full before sizing it, states the clean result and the messy
reality each at full strength, and anchors every magnitude to something the
reader can feel (an app icon, a thousand times the pixels, a thumbnail). The
headline, read last as the largest claim, commits to what the piece defends.

## Edits

- Corrected "The paper ran eight pages in the proceedings" to "nine pages" (s3 gives pp. 2672-2680 = 9 pages, verified against dblp).
- Corrected "fits in those eight pages" to "nine pages" and cut the trailing clause "and this lesson is about the distance between the two."
- Cut the sentence "It is a satisfying result: the method has a provable target, and the target is the truth." from the proof section.
- Ran `nb stamp`: words 1900, reading_minutes 8, sources 9.

## Required work

None. All findings were resolved within editor authority; no researcher, writer,
or orchestrator work remains.

## Decision

approve. Every load-bearing claim holds, the origin-of-technique vs
origin-of-photoreal distinction is stated and qualified, the numbers, labels,
sourcing, and asset all check against the evidence, and the remaining defects
were surgical cuts and one source-supported factual correction.

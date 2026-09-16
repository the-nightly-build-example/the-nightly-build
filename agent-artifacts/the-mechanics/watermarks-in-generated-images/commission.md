# Commission: the-mechanics/watermarks-in-generated-images

## The behavior

Ask an image generator for an ordinary scene and a ghostly, garbled stock-photo
watermark sometimes appears across it, a smear where a Getty Images or
Shutterstock mark would sit. The lesson works backward from that behavior to what
produces it. The researcher confirms the mechanism and every cited figure or
exhibit before the writer uses them.

## Why this behavior, now

It is one of the most-noticed and most-misunderstood things image models do.
People read the ghost watermark as proof the model "pasted in" or "stole" a
specific photo. That is the wrong mechanism, and the right one teaches something
the reader can carry to every generated image: these models learn the statistics
of their training pictures and reproduce the regularities in them, and a
watermark stamped across millions of stock photos is exactly such a regularity.
The behavior is a visible window onto how a diffusion model relates to its
training data.

## The declared reader and the fit

The reader is smart and has never trained a model. Build up every part named:
what a diffusion image model is doing when it generates (denoising toward the
kind of image it was trained on), what the training data is and where it came
from, and what "learning the distribution" means, each in plain words at first
use. No code.

## What the lesson teaches (work backward, each step a real part)

Keep it a short chain, each step naming a real part and what it does, with a
concrete example, and marking which steps are settled and which are open.

1. Start at the behavior: the ghost watermark, where it tends to appear, and what
   it looks like (a texture resembling a mark, usually not legible text). Draw the
   line to the covered lesson on why letters come out wrong in images: this is a
   different question. This lesson is about why a watermark-like pattern is there
   at all, not why its letters are garbled. Link that lesson rather than
   re-teaching it, and confirm its slug.
2. Up one step: what the model was trained on. Large image-text datasets scraped
   from the web contain enormous numbers of watermarked stock photos. Give the
   real scale of such a dataset and, if the record supports it, an estimate of how
   much of it carries watermarks.
3. Up one step: what training does with that. A diffusion model is trained to
   produce images that match the distribution of its data. A mark that co-occurs
   with a whole class of images is part of that distribution, so the model learns
   to produce the mark as part of producing that kind of image. This is
   distributional learning, and it is distinct from copying one image. Mark it
   settled.
4. The nearby, distinct mechanism: verbatim memorization. Diffusion models can
   also reproduce specific training images closely, shown by extraction work.
   Explain how this differs from the distributional story, and mark honestly what
   is settled (both happen) and what is open (for a given output, which one
   produced it).
5. Ground and present day: the objective plus the data plus the absence of
   filtering are enough to explain the behavior; nothing below changes the answer.
   Then where the same weakness lives now: any model trained on unfiltered web
   data carries its data's regularities, watermarks are just the visible tip, and
   dedup and watermark filtering reduce but do not remove it. Use the documented
   real case (the stock-agency litigation whose exhibits show a distorted
   watermark in generated output) as the concrete anchor for how this surfaced.

The original work: separating the two mechanisms (a learned distribution versus a
copied image) so the reader stops reading every ghost watermark as theft of one
photo, and can say which claim the evidence actually supports.

## Sources plan

Template and series floor: eight sources, at least four primary and one
secondary. Primary: the paper describing the training dataset and its contents,
the paper describing how the image model is trained, the training-data-extraction
work on diffusion models, and the litigation filing whose exhibits show the
watermark in output. Add a primary source on watermark prevalence or the effect
of deduplication if one exists. Secondary reporting is context only. Every figure
carries its scope.

## Continuity and neighbors

The letter-rendering lesson and any general diffusion or image-generation lesson
are in the library; link, do not re-teach, and confirm slugs. Tonight's other
generative-output lesson is on a speech-quality measurement; keep this piece
strictly about the image model's relationship to its training data, with no
shared framing.

## Recent shapes to break

The Mechanics has lately used a second-person observation as the opening move and
a callback heading to close ("So look again ..."). Do not copy either by reflex.
Vary heading construction from the recent run.

## Production record

Roles run on a capable-tier model (Claude Sonnet) via isolated subagents.
Effort per the balanced profile: researcher high, writer medium, editor high,
writing-coach low. No required directive was traded down.

# Commission: the-evidence/segment-anything

## Assignment

Read the Segment Anything paper (Kirillov et al., Meta AI Research, 2023) and
teach the reader what it actually built and what it did not. This is one lesson
on the lesson template for The Evidence: one famous document, read for what it
says rather than how it is cited.

## The document and the angle

The paper introduces three things at once, and the lesson should keep them
distinct: a task (promptable segmentation), a model (SAM), and a dataset built
by a model-in-the-loop data engine. The reader should come away able to say what
SAM takes in, what it puts out, and where the masks in its training set came
from.

The angle to pursue and let the evidence confirm or break: the document's
contribution is a segmentation foundation built on a data engine, not a system
that recognizes what it segments. SAM outputs masks, not labels. Investigate and
report honestly:

- What promptable segmentation is, and what a "prompt" is here (a point, a box,
  a rough mask), as opposed to a text prompt.
- The scale actually reported: the number of masks and images in the released
  set, and how many of those masks a human drew versus how many the model
  proposed and a human only checked or the model generated fully automatically.
  The data-engine stages are the heart of the scale story; get the per-stage
  counts and what each stage automated.
- What the paper claims for zero-shot transfer, on which segmentation tasks, and
  by which metric, with the honest size of each of those evaluations.
- The boundary the paper itself draws: what SAM does not do (it does not name or
  classify the object; semantic meaning is not its output), stated where the
  paper states it.

Then bring it to the present, as the desk requires: how the document is cited
now ("foundation model for vision," "segmentation is solved"), where adaptation
has actually gone (for example medical-imaging fine-tunes), and where zero-shot
SAM is reported to fall short of a task-specific model. If today's usage overers
what the paper showed, say exactly how. SAM 2 (2024) extended the approach to
video; the researcher may record it as context, but this lesson reads the
original document, not its successor.

## Boundary against the published course

The Evidence and the wider library already teach neighboring vision documents.
Do not re-derive them; link them where the reader needs the background:

- `clip` — zero-shot classification learned from captions. Different output
  (a class from text) and different training signal. Contrast, do not repeat.
- `vision-transformer` — the architecture-plus-data-scale story for
  classification. SAM's image encoder is a ViT; treat that as a Background link,
  not a re-teaching.
- `denoising-diffusion` and the mechanics image-generation lessons — generative
  image models. SAM is discriminative segmentation; keep the line sharp.

No published the-evidence lesson covers segmentation or a model-in-the-loop data
engine, so the contribution here is genuinely new ground for the course.

## Tonight's neighbors

Four other lessons run tonight, each on a distinct beat: a proof-graded math
benchmark number (The Instruments), why a model degrades when served in fewer
bits (The Mechanics), an alignment argument about training (What Could Go
Wrong), and a deployed-system failure (When AI Breaks). No overlap in subject;
the only shared discipline is that all five read as one paper.

## Template, sources, production

- Template: lesson. Word band 1200–2200. Bookends `why` and `takeaway` are
  citation-exempt apparatus; every body section carries its own citations.
- Source policy: at least 6 sources, at least 3 primary and at least 1
  secondary. The SAM paper, the SA-1B dataset material, and the Meta AI release
  are primary; independent reporting and independent benchmark comparisons are
  secondary. A contested or headline figure needs the primary that owns it.
- Production policy (balanced profile, model tier "capable", nothing marked
  `required`): researcher effort high, writing-coach effort low, writer effort
  medium, editor effort high. Roles run as isolated subagents on the runtime's
  default capable-tier model. No `required` directive exists, so no deviation is
  recorded.

## Recent shapes to break

The last several The Evidence lessons open their first body section on "the
paper that..." or "what X is counting" and close on a bare assessment heading.
Recent deks state a finding with one number. Do not inherit either the opener
mold or a closer that only grades the piece; headings are concrete, in this
lesson's own nouns, and varied in construction. These are habits to avoid, not
required furniture: the bookend bands and the Sources heading are mandatory.

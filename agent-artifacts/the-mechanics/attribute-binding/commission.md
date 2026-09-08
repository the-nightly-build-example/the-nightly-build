# Commission: the-mechanics/attribute-binding

## The behavior

Ask an image generator for "a red cube on top of a blue sphere" and it hands back
a blue cube on a red sphere, or two red objects, or ignores "on top of"
entirely. The colors, textures, and positions the prompt assigned to specific
objects come out attached to the wrong objects or smeared across the scene.
Anyone who has typed a two-object prompt with adjectives has seen it. This desk
explains what produces it.

## Why this behavior now

Text-to-image tools are everywhere and their most reliable failure is the one a
user hits on the second prompt: the model gets the objects and the general vibe
right and puts the wrong adjective on the wrong noun. The course already explains
neighboring image-model failures (counting in `../the-mechanics/counting-objects-in-images.html`,
clock hands in `../the-mechanics/clock-faces.html`, negation in
`../the-mechanics/negation.html`) and the attention operation
(`../the-mechanics/attention.html`). This lesson names the specific mechanism
behind wrong-attribute and wrong-relation images and marks what is settled and
what is still open.

## The angle

The prompt is not read as a sentence with structure; it is encoded closer to a
bag of concepts, and nothing downstream reliably re-attaches each attribute to
its own object. Work backward from the wrong image to the cause: the text encoder
(the CLIP-style encoder most systems use) produces token representations that mix
neighboring words, so "red" and "blue" and "cube" and "sphere" arrive at the
image model without a firm binding of which adjective belongs to which noun; the
cross-attention that lets the image attend to the prompt then lets an attribute
"leak" onto the wrong region. Composition of unfamiliar combinations is worse
than either object alone, which is why "red cube on a blue sphere" fails where
"red apple" does not. Mark the settled part (binding failures are real,
measured, and reproduce across systems) and the open part (the exact division of
blame between encoder and cross-attention, and whether fixes generalize).

## What to teach (short list, in order)

1. The behavior, shown concretely with a real tested prompt and result. Establish
   that it is systematic, not a one-off, with a benchmark number.
2. How a text-to-image system turns words into a picture, at the level this needs:
   the prompt goes through a text encoder into a set of vectors; the image model
   generates while attending to those vectors through cross-attention. Define text
   encoder and cross-attention in plain words at first use; link
   `../the-mechanics/attention.html` rather than re-teaching attention.
3. Why binding breaks: the encoder's representations mix adjacent words so the
   adjective-to-noun link is weak, and cross-attention can attach an attribute to
   the wrong object's region. Ground each step in a real finding (e.g., studies
   that swap or measure attribute binding, and methods like Attend-and-Excite or
   Structured Diffusion that improve it by intervening on exactly these parts,
   which is evidence for where the fault lives).
4. What is settled vs open: reproducible failure and the general location of the
   cause are settled; the precise mechanism and whether fixes hold across prompts
   are open. Note where the reader hits ground: the model was never given the
   sentence's structure, so nothing below that would change the answer.

No code. Keep to these ideas; cut rather than compress.

## Template, bands, sources

- Template: lesson. Word band 1200-2200. Sections: why, orientation, 0-4 flex,
  takeaway, sources.
- Source floor (the-mechanics/lesson): at least 8 sources, at least 4 primary and
  at least 1 secondary. Primary: the papers that own each claim (a compositional
  text-to-image benchmark such as Huang et al. T2I-CompBench; relational/attribute
  studies such as Conwell & Ullman 2022; method papers that localize the cause,
  e.g., Chefer et al. Attend-and-Excite 2023 and Feng et al. Structured Diffusion
  2022; the CLIP paper `../the-evidence/clip.html` is in the library, but cite the
  primary CLIP/text-encoder source for the encoder claim; a Stable Diffusion /
  latent diffusion primary for how the pipeline is built). Reproducible model
  outputs you actually generate or that a paper reports are primary observations.

## Source assets

A side-by-side of a prompt and the wrong image it produced, taken from a cited
paper's figure, could carry the behavior better than prose. Only if the evidence
record identifies an exact figure from a cited primary; capture with `nb asset`,
caption factually with the source. Never an external image URL, never a
decorative image.

## Production policy (resolved)

Profile balanced. writing-coach low/capable, researcher high/capable, writer
medium/capable, editor high/capable. None required. Writer records actual harness
and model in nb-meta.

## Background links available (verify and link, do not re-teach)

`../the-mechanics/attention.html`,
`../the-mechanics/counting-objects-in-images.html`,
`../the-mechanics/clock-faces.html`, `../the-evidence/clip.html`,
`../the-evidence/denoising-diffusion.html`. Use only those the reader needs.

## This run's neighbors (for coherence, not overlap)

Publishing tonight: the-evidence/alphazero, the-instruments/auroc,
what-could-go-wrong/encoded-reasoning, when-ai-breaks/waymo-recall. No overlap;
keep the shared voice.

## Habits not to inherit (voice and shape)

The mechanics desk is heavy on image-generation pieces; do not echo their
openers or headings. Recent openers lead with a confident-wrong-output line
("A confident move the board doesn't allow"); find this piece's own opening.
Recent deks use the comma-and mold. Vary heading construction. No colon-subtitle
headline. Do not reuse the clock-faces or counting-objects framing of "the model
never X before it draws a pixel" as a template, even though the mechanism rhymes.

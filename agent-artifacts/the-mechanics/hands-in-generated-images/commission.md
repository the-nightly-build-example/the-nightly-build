# Commission: the-mechanics/hands-in-generated-images

## Assignment

Start from a behavior almost everyone who has used an image generator has seen: it
draws a hand with six fingers, or fingers that melt into each other. Work backward
to what produces it, step by step, until the reader hits ground. By the end the
reader can explain why hands in particular come out wrong, and can tell when an
explanation stops short.

## Angle and boundaries

The causal chain, each step a real part of the system:
1. The generator is a diffusion model. It starts from noise and removes it a little
   at a time toward an image that looks plausible under the prompt. Link the
   existing lesson the-mechanics/image-generation for the denoising mechanism
   rather than re-teaching it; take it as given here.
2. Nothing in that process counts fingers or holds a model of anatomy. The
   objective rewards an image that looks locally like real texture and globally
   coherent, with no step that verifies "a hand has five fingers."
3. Hands are the worst case for this: they are small in the frame (little signal),
   and they appear in training images in a huge range of poses, angles,
   occlusions, and grips, so the learned distribution over "hand" pixels is diffuse.
   The model interpolates to something hand-shaped and plausible, which lands on the
   wrong finger count often.
4. Ground the reader here, and mark what is settled versus open: the reasons hands
   are hard are reasonably understood; whether the problem is "solved" is a moving
   target improved by scale, better data, and hand-specific fixes (e.g. pose or
   mesh guidance), not a settled result. No code.

## Sources

Policy: at least 8 sources, at least 4 primary, at least 1 secondary. The
mechanism's primary base is the diffusion literature (e.g. DDPM, latent diffusion)
plus primaries that study or fix generative hand/anatomy failures (e.g. a
hand-refinement paper) and text-encoder limitations. The researcher owns the set,
must ground every mechanism claim in a primary that owns it, and must record what
is genuinely established versus practitioner explanation. If the anatomy-specific
literature is thin, ground the mechanism in the diffusion primaries and say where
the hand-specific claim rests on softer evidence.

## Production policy (balanced profile)

- researcher high, writing-coach low, writer medium, editor high; capable model.
- nb-meta harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
  series `the-mechanics`, slug `hands-in-generated-images`. No `required` directive.

## This edition's siblings (keep each piece distinct)

Publishing with lessons on the adversarial-examples paper, the toxicity score, the
AI-boxing argument, and AI writing-detector failures. This piece owns the
hands-in-image-generation behavior. It builds on the-mechanics/image-generation
(link it) and must not re-teach diffusion from scratch, and it is not the vision
lesson the-mechanics/reading-images (that is image input, not generation).

## Recent-pattern notes (habits not to inherit)

Recent the-mechanics deks/headlines, not to echo in mold:
- "Ask a chatbot for a random number and it says 7"
- "'No onions' gets onions, 'no elephant' gets an elephant"
- "The token a model can't repeat back"
- "A model can spell strawberry and still miscount its letters"
- "A strict output format can block the reasoning a model needs to be right"
The most recent piece (random-numbers) opened with an nb-figure and ran five short
sentence-headings; vary the shape. Only the two bookends address the reader. No
Verdict block at the body's close.

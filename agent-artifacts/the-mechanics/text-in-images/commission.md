# Commission: the-mechanics/text-in-images

## Assignment
Answer "how does it actually do that" for one behavior everyone who has used
an image generator has seen: the text in generated images comes out garbled —
warped letters, invented characters, near-words on signs and storefronts.
Work backward from that behavior to its cause, step by step, each step naming
a real part of the system in plain words with a small concrete example. Keep
going down until the reader hits ground: the step below which nothing would
change the garbling. Mark which steps are settled engineering and which are
still open. No code. By the end the reader can explain why the letters come
out wrong, and can tell when someone else's explanation skips a step.

## The chain to walk (the researcher pins the evidence; the writer orders it)
Candidate steps, from behavior down to cause:
- The generator does not draw letters as glyphs; it produces pixels, and text
  is just more texture to reconstruct. Diffusion models learn to remove noise
  a little at a time (already taught in `image-generation`); nothing in that
  loop knows the alphabet.
- The prompt reaches the image model through a text encoder. Early and many
  current systems used a CLIP-style text encoder that represents whole
  words/tokens, not their spelling, so the model never receives the letters of
  a word in order. This is where the character information is lost.
- Tokenization: the word the user typed is split into subword tokens, and the
  model sees token IDs, not characters — the same reason models miscount
  letters (`letter-counting` is taught).
- What fixed it, and how far: character-aware text encoders and larger
  text encoders (the "Character-Aware Models Improve Visual Text Rendering"
  result), plus scale and better training, sharply improved short-string
  rendering; long or unusual strings still fail. Name what is settled (the
  cause of the failure and why character-aware encoders help) versus open (the
  exact limits of current best systems, and why some still fail on long text).

## Boundaries
- Teach the behavior's cause, not diffusion in general. `image-generation`
  already taught the denoising loop; link it, do not re-teach it.
- Neighbor tonight: `the-evidence/clip` covers the CLIP paper the same night.
  This lesson may name CLIP's text encoder as the character-blind link and
  cite the CLIP paper as a source, but must NOT re-teach what CLIP is, and
  must NOT place a Background link to tonight's unpublished clip lesson (link
  only already-published lessons to avoid a broken internal link). Refer to
  the encoder concept via the published `word-embeddings` and `reading-images`
  lessons where a link helps.
- No code (series rule). Plain words and small examples only.

## Required contribution
Give the reader the one causal step most explanations skip: that the failure
is set before any pixel is drawn, at the text encoder that hands the image
model word-level features with the spelling already thrown away — and show why
character-aware encoders are the fix that follows from that diagnosis.

## Sources (researcher obligation)
Floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary: the papers that own the mechanism and the fix — e.g. the latent /
diffusion text-to-image papers whose text encoder choice matters (Stable
Diffusion / latent diffusion using CLIP text encoder; Imagen using a large T5
text encoder and reporting text rendering), the "Character-Aware Models
Improve Visual Text Rendering" paper, DeepFloyd IF's design notes, and a
current system's own documentation (DALL·E 3 / a 2024–2025 model) on text
rendering. Read each source's own account of why text renders or fails.

## Recent shapes to break (the-mechanics)
Verified against recent library structure and prose:
- Recent mechanics pieces open the body by naming the everyday behavior, then
  decompose into named parts ("The wait ... has four parts", "the tone stays
  the same"). Vary the opener; do not default to "The X has N parts."
- The takeaway often ends by enumerating the parts again ("Any TTFT figure a
  reader sees carries four separate costs"). Avoid a closer that just relists
  the steps; land the judgment instead.
- Section headings are concrete and in the piece's nouns; keep that, but avoid
  copying prior heading rhythms.
- Deks: no comma-triad, no semicolon reversal, no suspended question.

## Production record
Harness: Claude Code subagents, scheduled run. Balanced policy, no required
directives. Models/effort used:
- writing-coach: Claude Sonnet, low effort
- researcher: Claude Opus, high effort
- writer: Claude Opus, medium effort
- editor: Claude Opus, high effort

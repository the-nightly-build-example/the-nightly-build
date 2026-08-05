# Commission: the-mechanics/reading-images

## The behavior

You paste a photo into a chatbot and ask "what's in this?" and it answers. This
lesson works backward from that behavior to what produces it, one step at a
time, until the reader hits ground.

## Why this behavior, why now

Multimodal input is now the default in consumer chatbots, and the course has
never taught how a language model "sees." The reader has the prerequisites:
word-embeddings, attention, tokenization (letter-counting), and hallucination
are all published in this desk. Vision is the missing piece that those lessons
were building toward, and it explains a whole class of failures the reader has
hit (miscounting objects, misreading small text, confidently inventing details).

## The angle

Thesis for the writer to prove: a model reads an image by cutting it into a few
hundred fixed patches, turning each patch into the same kind of vector it uses
for a word, and letting the question's tokens attend to them. It never gets more
detail than the patch grid captured, which is exactly why it miscounts and
misreads small text.

## What this lesson teaches (2-3 ideas), no code

1. An image becomes tokens, from patches. The model cannot read pixels
   directly. A vision encoder cuts the image into a grid of fixed-size patches
   (for example 16x16 pixels), flattens each patch, and a learned linear step
   maps each patch to a vector in the same space as word-embeddings (link
   the-mechanics/word-embeddings). Worked count: a 224x224 image at 16x16 patches
   is a 14x14 grid, so 196 patches, so about 196 image tokens. This is where the
   reader learns why an image costs hundreds of tokens.
2. Image tokens flow through the same transformer, and the question attends to
   them. Link the-mechanics/attention: the text tokens of "what's in this photo"
   read the image tokens by attention, and that is the whole of how the answer
   gets built. Name plainly the two common arrangements without turning it into
   an architecture survey: patches fed straight into one model (native
   multimodal), versus a separate vision encoder whose patch vectors are
   projected in (the CLIP/ViT-plus-projector arrangement, as in LLaVA). Name ViT
   as the settled patch-embedding idea.
3. Where the reader hits ground, and what is open. Settled engineering:
   patchify, project into the token space, attend. What is open even to builders:
   how faithfully that representation grounds fine spatial detail, and why
   specific failures happen. The model can attend only to what the patch grid
   encoded, so small text and exact counts are lost, and it then fills the gap by
   confident generation (link the-mechanics/hallucination). Mark clearly which
   steps are settled and which are open.

## Ground rule from the series

Keep going down until nothing below would change the answer, and mark each step
as settled engineering or open question. No code. The only arithmetic is the
patch count, which is fine because it is counting.

## Boundaries (do not repeat; link instead)

- word-embeddings, attention, letter-counting (tokenization), hallucination are
  all taught. Link at first use; do not re-teach any of them.
- Do not teach how image *generation* works (diffusion). This lesson is about
  reading an image, not making one. Image generation can be its own lesson.
- Do not drift into a benchmark or model-comparison piece; the behavior and its
  mechanism are the subject.

## Source obligations

Floor: at least 8 sources; primary >= 4, secondary >= 1. Primaries: the Vision
Transformer paper (Dosovitskiy et al. 2020, "An Image Is Worth 16x16 Words"),
CLIP (Radford et al. 2021), LLaVA (Liu et al. 2023), Flamingo (Alayrac et al.
2022), the GPT-4V system card (OpenAI 2023), and a current model's own
documentation of how many tokens an image costs (for example a vision pricing or
model-card page that states the patch/tile-to-token accounting). Every count and
architectural claim must come from a paper or card that owns it. Secondary
explainers for context only.

## Production policy (balanced; none required)

coach low, researcher high, writer medium, editor high; model capable, none
required. Recorded run: harness claude-code-routine, model claude-opus-4-8.

## Recent library shapes to break

Recent the-mechanics deks are single vivid declaratives ("A chatbot quotes your
PDF without learning a word of it"; "reads your whole prompt at once but writes
its reply one word at a time"). That register is right for the desk, so match the
plainness but do not echo the "reads/writes" antithesis structure. Vary heading
cadence from the recent comma-and-clause pattern.

## Neighboring articles this run

the-evidence/atari-dqn, the-instruments/parameter-count,
what-could-go-wrong/mesa-optimization, when-ai-breaks/ai-overviews. No overlap.

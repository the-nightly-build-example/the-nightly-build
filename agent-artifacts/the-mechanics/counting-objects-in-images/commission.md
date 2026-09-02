# Commission: the-mechanics/counting-objects-in-images

## The behavior

Ask an image generator for "exactly six apples" or "three dogs" and it hands back
five, or seven, or an improvised pile. Everyone who has used one of these tools
has seen it. The lesson works backward from that behavior to what produces it,
step by step, until the reader hits ground. No code.

## What the lesson must do

Trace the pipeline from prompt to pixels, naming a real part at each step and
what it does, with a small concrete example where it helps:

1. The prompt is turned into an embedding by a text encoder (the CLIP-style
   encoder most systems use). Establish the key fact: these encoders behave close
   to a bag of concepts — they register that "apple" is present far more reliably
   than they register "six," and word order and exact quantity are weakly encoded.
   Ground this in the documented bag-of-words behavior of CLIP-style encoders.
2. A diffusion model starts from noise and denoises toward an image, steered by
   that embedding through cross-attention, which spreads a concept across the
   canvas rather than placing a counted set of discrete objects.
3. There is no step that holds a running count or checks the finished image
   against the requested number. The count that comes out is whatever the
   training data made statistically likely, and exact counts are rare and
   skewed-small in web caption data.

Mark what is settled engineering (no component counts; the encoder is quantity-
weak) and what is open (how far better captioning, scaling, or added guidance
methods actually fix counting). By the end the reader can explain why the number
is wrong, not just that it is, and can catch an explanation that skips the "no
counter anywhere" step.

## Required contribution

The reader leaves able to locate the failure in the pipeline — it is upstream, in
how the prompt is represented and how diffusion paints, not a rendering glitch —
and able to tell a real mechanism story from a hand-wave. The article's work is
assembling the standing pieces (CLIP bag-of-words, diffusion via cross-attention,
caption statistics) into the specific causal chain for counting, which no single
source does for a newcomer.

## Boundaries and continuity

- Image generation and its failure modes are partly taught: the-mechanics/
  image-generation, the-mechanics/hands-in-generated-images, the-mechanics/
  reading-images, the-mechanics/text-in-images. hands-in-generated-images already
  makes the point that "nothing in the process counts fingers" — this lesson must
  not restage the fingers piece. Its distinct subject is discrete object count
  and its distinct cause is the text-encoder representation of quantity plus
  caption statistics, not anatomy. Link the taught pieces in Background; do not
  re-teach diffusion from zero, but do name the one or two steps this argument
  rests on.
- No code. Keep the mechanism in plain words.

## This run's neighbors

Four other lessons publish tonight on other desks. hands-in-generated-images is
prior published work, not this run — but it is the closest neighbor in the
library, so the risk to manage is overlap with it. Keep this lesson on counting
of distinct objects and the encoder/caption cause.

## Source policy

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Candidate
primaries: CLIP paper (Radford et al., 2021, 2103.00020); a paper documenting
CLIP-style bag-of-words / compositional failure (e.g. Yuksekgonul et al., "When
and why vision-language models behave like bags-of-words," ICLR 2023, 2210.01936);
latent diffusion (Rombach et al., 2022, 2112.10752); an official text-to-image
system report acknowledging counting/compositional limits (DALL-E 3 system card,
or the Imagen paper 2205.11487 with DrawBench); a compositional/counting benchmark
or method paper (T2I-CompBench, Huang et al. 2023; or a counting-specific paper
such as "Make It Count," 2406.10210). Secondary: reporting. The researcher
confirms kind and count and, crucially, that the "no counter / quantity-weak
encoder" causal claims are each backed by a source that owns them.

## Production policy (recorded)

profile balanced. writing-coach low, researcher high, writer medium, editor high.
Model "capable" for every role, none required; roles run on this harness's
default capable model. Record actual models in handoffs.

## Recent patterns to break (habits, not rules)

- Deks recur as a two-clause ", and"-twist or a comma triad (banned). The
  mechanics desk's recent deks state the mechanism and its cost in one breath
  (quantization, hands). Say this lesson's mechanism plainly without copying that
  shape.
- Headlines default to a negative-fact reveal, and hands-in-generated-images
  already used exactly that ("An image generator never counts the fingers it
  draws"). Do not echo it. Find this lesson's own headline about count.
- The present-day/closing section keeps getting a "Where X still Y" heading;
  vary it.

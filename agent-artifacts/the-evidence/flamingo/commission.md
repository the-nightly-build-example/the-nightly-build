# Commission: the-evidence/flamingo

## The document

Alayrac et al., "Flamingo: a Visual Language Model for Few-Shot Learning"
(DeepMind, 2022). Chosen after a full scan of The Evidence back-catalogue: the
desk has read CLIP, the Vision Transformer, and Segment Anything, but nothing on
the model that brought GPT-3-style few-shot, in-context learning to vision — the
line that leads to today's multimodal chat assistants. It is the clearest
multimodal gap in the section and a document still cited as the template for
"show the model a few image-text examples and it adapts."

CONFIRMED not previously published (checked against the full the-evidence slug
list). Distinct from the published clip (contrastive image-text matching),
vision-transformer (image classification), and segment-anything (masks) lessons —
link them rather than re-teaching.

## The angle

Read the paper as the paper, in the desk's order.

1. What Flamingo is and why it became famous. A single model that takes
   interleaved images (and video) and text and produces text, and that learns a
   new visual task from a few examples placed in its prompt, without any weight
   updates — few-shot in-context learning, but multimodal. Establish plainly:
   in-context learning (the model adapts from examples in the prompt, not from
   training) and why doing it across images and text was the news. Name the two
   pieces it bolts together: a frozen pretrained vision encoder and a frozen
   pretrained language model, joined by new trainable components (the Perceiver
   Resampler and gated cross-attention layers) so the language model can attend to
   images. Keep this to what a non-coder needs.

2. What it measured, at what scale. This is the teaching core, honest about size.
   Flamingo was trained largely on image-text and video-text scraped from the web
   (including a large interleaved-webpage dataset). The headline claim: with only
   a handful of examples it beat the prior fine-tuned state of the art on several
   vision-language benchmarks. Report the actual numbers the paper gives (the
   specific benchmarks where few-shot Flamingo beat prior fine-tuned SOTA, the
   parameter count of the biggest model, the number of shots), and show the scale
   of the foundation: how many benchmarks, how the "few-shot beats fine-tuned"
   claim is bounded (on which tasks it held and where fine-tuned systems still
   won). Small, careful reading of what "state of the art on 6 of 16 tasks with
   32 examples" actually means.

3. How it is used today versus what it showed. Flamingo is cited as the ancestor
   of interleaved multimodal LLMs. Say plainly what the paper did and did not
   establish: it was not open (weights not released; OpenFlamingo later
   reproduced it on open data — a useful primary/secondary to note), it still
   hallucinated and had the known failure modes the paper documents, and the
   frozen-backbones design was later changed. Where today's "multimodal" claims
   outrun what Flamingo showed, say so.

Anchor fact to foreground: Flamingo's surprise was not a new benchmark record for
its own sake but that a few examples in the prompt, with the vision and language
backbones frozen, could beat systems fine-tuned on thousands of labelled
examples — and the paper is careful about exactly which tasks that held for.

## Boundaries

- One document: the 2022 Flamingo paper (plus its own materials and the
  OpenFlamingo reproduction as a directly relevant follow-up). Not a history of
  multimodal models.
- Link, don't re-teach: CLIP, Vision Transformer, GPT-3 few-shot / in-context
  learning, Segment Anything — all published lessons.
- No code. Explain the Perceiver Resampler and gated cross-attention only as far
  as needed to understand "frozen backbones, few new parts, images fed into a
  language model."

## Required contribution

The reader should finish able to say what Flamingo actually reported (few-shot,
in-context multimodal learning that beat fine-tuned SOTA on a bounded set of
tasks), how it was built (frozen vision + frozen language, joined by small
trainable bridges), and where it has been outgrown or where "multimodal" claims
now outrun it. They should be able to catch someone citing Flamingo as if it were
a general multimodal intelligence.

## Source and production policy

- Sourcing floor (nb source-policy): minimum 6 sources, at least 3 primary, at
  least 1 secondary. Primary = the Flamingo paper; the OpenFlamingo paper/report;
  and other documents that own their claims (e.g. the datasets, a directly
  relevant predecessor). Read the paper's tables.
- Production policy (balanced, no `required` directive): editorial roles run on a
  capable model (Claude Sonnet class) in isolated subagents; effort follows policy
  (coach low, researcher high, writer medium, editor high). No directive traded down.

## Recent-pattern notes (habits not to inherit)

From a read of the recent library and the full section:
- Opener habit: the "Why this matters" card ending on a "By the end you will know
  how X, why Y, and Z" triad, and opening on a temporal generality. Break it.
- Takeaway habit: tidy two-part balance closers ("Both things are true"; "X is a
  real result told slightly wrong"). End on this lesson's own point.
- Heading habits over-used across The Evidence: "How a X becomes a Y", "From X to
  Y", "The name outlived the architecture" (The X outlived the Y), "The recipe
  reproduced on open data" / "The condition was the recipe, not the architecture"
  (note vision-transformer and clip both end on a reproduced-on-open-data beat —
  do not reuse that closer shape even though OpenFlamingo invites it). Vary
  construction; do not default to the nb-holdsup block.
- Dek habit: long comma-splice / comma-triad deks. `spec/headlines.md` bans the
  comma triad. Keep the dek lean and committing.

## Neighbouring articles in tonight's edition

- the-instruments/brier-score (how the Brier forecasting score is made)
- the-mechanics/familiar-pattern-override (why modified classic riddles break models)
- what-could-go-wrong/companion-dependency (the AI-companion-harm argument)
- when-ai-breaks/predpol-predictive-policing (the PredPol/Geolitica failure)
No overlap. This is tonight's foundational-document lesson.

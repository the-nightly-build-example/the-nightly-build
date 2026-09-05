# Commission: the-mechanics/clock-faces

## Assignment
Start from a behavior anyone who has used an image generator can reproduce: ask
one for "a clock showing 3:15" or "a watch at 7:20" and it hands back a clock or
watch reading about 10:10. Ask a vision-language model to read the time off a
photo of an analog clock and it often gets that wrong too. Work backward from the
behavior to its cause, step by step, naming a real part of the system at each
step, until the reader hits ground.

The chain to teach, in the reader's order of need:
1. What the model is actually doing when it "draws a clock": a diffusion image
   generator produces pixels that match the statistics of its training images,
   not a drawing built from a rule that hands encode a time.
2. What is in the training data: watches and clocks in product and stock photos
   are overwhelmingly posed at about 10:10 (a longstanding marketing
   convention), so "clock" and "hands near 10 and 2" are bound together in what
   the model learned. The model reproduces the most common arrangement it saw.
3. Why a text prompt for a specific time does not override that: the model has no
   step that converts "3:15" into two hand angles, because nothing in training
   rewarded it for placing hands to encode a requested time.
4. The reading side, briefly: a vision-language model was not trained to compute
   angle-to-time either, so reading an arbitrary clock face is the same missing
   step seen from the other direction.

Mark which steps are settled engineering (diffusion models reproduce dataset
statistics; the 10:10 convention in training imagery) and which are open or
model-specific (how much targeted data or tooling closes the gap, and whether
newer systems that plan or use tools do better). No code.

## Angle
The clock is a clean case of a general rule: an image generator renders the most
likely appearance, and where the correct output depends on a rule the data did
not teach (hands encode a time), the most likely appearance wins. The reader
should leave able to predict where else this bites, and able to tell a real
mechanism ("the training data is posed at 10:10 and nothing taught the rule")
from a hand-wave ("the AI is bad at clocks").

## Template and form
Lesson template. Body first, then both bookends. 1200–2200 words. No code.
Sections named for this behavior.

## Sources
Series floor is 8 sources, at least 4 primary and at least 1 secondary. Primary
candidates: research papers that test analog-clock reading in vision-language
models (they own their findings); any study or documented systematic test of
image-generator clock/time rendering; a primary on how diffusion models model the
data distribution (link the paper's own statement of the objective); a
dataset/marketing primary establishing the 10:10 convention (a watch brand's own
statement, or a documented analysis of watch imagery). Secondary: reputable
reporting or demonstrations of the 10:10 behavior. Verify each claim against the
source that owns it; a demonstration in an article is secondary. If the honest
source base cannot support one of the four chain steps, the researcher records
the gap and the writer scopes the claim to what is shown.

## Tags
Open item, no commissioned tags. Writer sets `tags` from the subject.

## Production policy (balanced profile)
researcher capable/high; writer capable/medium; editor capable/high;
writing-coach capable/low. None `required`. Actual harness: Claude Code Task
subagent, model `claude-opus-4-8`.

## This run's neighbors (keep distinct)
Publishing alongside: llama-3-herd-of-models, livecodebench, automation-bias,
grok-antisemitic-outputs. No overlap of subject, but this piece and the diffusion
mechanism connect to already-published the-mechanics lessons
(hands-in-generated-images, image-generation, text-in-images): those cover other
diffusion failures. Link them at first use for the shared machinery; do not
re-teach how diffusion works from scratch, and keep this lesson on the specific
clock case (the dataset prior and the missing rule), not a general "diffusion is
bad at details" piece.

## Do not repeat (recent the-mechanics coverage)
- irrelevant-context (2026-09-04): closing on a live dispute ("Where this leaves
  the reasoning question"); do not clone that "where this leaves X" closer.
- option-order-bias, counting-objects-in-images, quantization,
  hands-in-generated-images, random-numbers are recent.
  counting-objects-in-images and hands-in-generated-images are the closest
  neighbors (both image-generation failures); this lesson must add the distinct
  point that the failure is a *learned convention plus a missing rule*, not just
  "counting/parts are hard." random-numbers taught "model draws from a learned,
  lopsided distribution" — the clock case is a sharper version (a single
  dominant mode), so make the contrast, do not restate it.

## Required contribution
By the end the reader can explain why an image generator draws 10:10, name the
two causes (a lopsided training prior and no step that turns a requested time
into hand angles), and use that to predict other places the "most likely
appearance" beats the correct one.

# Editorial review: the-mechanics/image-generation (editor/01)

## Skeptic

Thesis: a text-to-image generator builds a picture by removing noise, not by
drawing or searching; the network learned exactly one skill, predicting the
noise added to an image, and generation, steering, the latent shortcut, and the
open failures all follow from that one skill.

Claims it stands on, and how each held:

- The network is trained to predict the noise added to an image. Held. DDPM
  (s1) owns it; the article's training walk matches Eq. 14 (add known noise,
  train the network to output that noise, score against the known truth).
- Generation starts from pure noise and applies the denoiser over many small
  steps. Held (s1, Algorithm 2). The "no canvas, no object list" framing is
  faithful.
- The prompt is encoded by a separate model and read at every pass. Held (s3,
  cross-attention conditioning). "Rides every pass" is accurate.
- Guidance is a dial trading prompt-adherence against variety. Held (s7). The
  plain-language account of Eq. 6 (difference between the with-prompt and
  without-prompt estimates, walked further) is correct.
- Latent space is one design, not universal. Held and correctly forked: Stable
  Diffusion denoises in latent space (s3), Imagen and DALL-E 2 in pixels with a
  cascade (s4, s5).
- The open failures' causes are unsettled. Held (s5): the article states the
  DALL-E 2 CLIP-embedding account as the builders' hypothesis, not a
  demonstrated cause, exactly as the source frames it.

Round-focus boundaries all survived. The mechanism is worked backward from the
behavior; it hits ground ("It only ever looks at a noisy image and estimates the
noise in it"); settled steps are marked apart from open ones. Paper-vs-product
numbers are kept distinct and explicit: T=1000 is labeled the training-time
design and ~50 the deployed run ("They are not one number measured two ways"),
and the guidance-weight offset (paper's zero-based w vs a product slider
defaulting near 7.5) is stated with both conventions kept separate. The
text-encoder fork (BERT-style in the LDM paper, CLIP in released Stable
Diffusion, frozen T5 in Imagen) is preserved. No code or pseudocode anywhere;
equations are carried in prose.

Numbers spot-checked against the record: 1000 steps (s1), ~50 default (s2), CLIP
400M pairs (s6), guidance 7.5 (s2/s8), Imagen 64->256->1024 cascade (s4). All
match.

data-nb-kind audit: s1/s3/s4/s5/s6/s7 primary (each paper's own authors reporting
their own method), s2/s8 secondary (deployed-system descriptions). Correct. Six
primary, two secondary meets the 8/4/1 floor. arXiv IDs resolve to the named
papers.

One break with the evidence, fixed directly: the sentence "The released version
of Stable Diffusion uses CLIP..." cited only s6 (the CLIP paper), which owns what
CLIP is but not the fact that Stable Diffusion uses it. That fact is owned by s2
(Hugging Face), already in the article and in the comparison table. I attached
s2 to the "uses CLIP" claim, leaving s6 on the CLIP description that follows.

No central claim broke. Nothing routed to the researcher.

## Cut

Slop pass, edges pass, delete test, leakage check, and formula check against the
recent-pattern notes. Four sentences failed and were cut or repaired; the body
was otherwise clean.

- Throat-clearing removed: "It is worth being blunt about what that skill is and
  is not." announced emphasis without reasoning; the concrete sentences after it
  and the ground statement carry the point.
- Body self-reference removed: "That is the ground this whole lesson stands on"
  had the body narrate itself (recent-pattern note 4; template rule that the body
  never mentions the lesson). Recast to fold into the next sentence as "That
  single ability is the ground everything the system does later is built on,"
  which also cut a redundant repeat.
- Empty assertion removed: "and the choice is not cosmetic" asserted the encoder
  matters right before the Imagen scaling finding demonstrates it.
- Paragraph closer removed: "The particular encoder is a real difference, not a
  footnote" restated the invariant just stated ("The shape is always the same...")
  and echoed the evidence record's own framing ("a real difference"), a
  negative-parallelism tell with "footnote" as an invented strawman.
- Unsupported clause removed: "and more prone to artifacts" (guidance dial) is
  not established by s7, which records fidelity-up/variety-down, not quality loss.
  The core trade-off stays fully cited.

Formula check: the "Why this matters" opener does not open on nostalgic or
second-person recall and does not pivot on "This lesson shows"; it does not close
on a side-by-side line. "The takeaway" lands on the thesis, not a "so next time
you..." rule. No body self-reference survives after the fix. The dek is not built
on the "To [do everyday thing], [mechanism]" mold. No heading uses the "The X
that Y" or "noun, the appositive" molds; each is a step in the lesson's own
nouns. No borrowed phrasing from the voice-guide exemplars. No em-dashes.
Punctuation is plain; colons introduce payoffs correctly.

## Reader

Read straight through as the paper's reader, the surviving piece gives one thing
the five method papers alone would not: a single mental model in which
generation, text steering, the latent efficiency step, and the two familiar
failures all fall out of the one skill the network has. The sources are five
separate results; the article threads them backward from the behavior into one
account and marks where the builders' own knowledge stops. That synthesis is what
the reader keeps, and it matches the original-work sentence in the draft handoff.
The prose sits closer to the voice-guide exemplars (Ciechanowski's build-up,
Evans's flat correction of a wrong model) than to a median summary. The headline,
read as the largest claim, is one the piece defends.

Visual evidence: the writer left the lesson prose-led with one comparison table
and no source figure, flagging DDPM's progressive-generation figure as an
optional anchor for the denoising loop. I inspected that call. The figure would
illustrate "many small steps" but would not let the reader test the central
argument better than the prose already does, and the licensed asset is
low-resolution CIFAR that reads as unimpressive blur to a reader who has seen
modern outputs. The prose ("coarse shapes settle first and fine detail arrives
late") carries the point. With the article at the top of the word band, adding
it is not warranted. Left out. The one table earns its place: it is the single
spot where three systems are compared across two axes, which prose would tangle.

## Edits

- Cut "It is worth being blunt about what that skill is and is not." (training section).
- Rewrote "That is the ground this whole lesson stands on. Everything the system does later is built from this one ability." to "That single ability is the ground everything the system does later is built on." (removes body self-reference and a redundant repeat).
- Cut "and the choice is not cosmetic" from the text-encoder paragraph.
- Attached source 2 to the "released version of Stable Diffusion uses CLIP" claim (miscitation fix; s2 already in the article owns the fact).
- Cut "The particular encoder is a real difference, not a footnote." (restatement plus negative-parallelism tell).
- Cut "and more prone to artifacts" from the guidance-dial sentence (claim not supported by s7).

## Required work

None. Every fix was the editor's and is applied. Nothing needs new reporting, a
recrop, chart provenance, or a redraft. Word count moves down slightly from the
cuts; the orchestrator's `nb stamp` will refresh the count and byline, then
`nb check`.

## Decision

Approve. The mechanism is worked backward to ground with the settled/open line
and every evidence-record fork intact; the remaining defects were slop, one body
self-reference, and one miscitation, all fixed directly.

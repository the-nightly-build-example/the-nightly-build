# Commission: the-mechanics/quantization

## Assignment

Start from a behavior the reader has met: the cheaper, faster, or on-device
version of a model gives noticeably weaker answers than the full one, though it
is described as the same model. Work backward to what produces that, step by
step, down to ground. One lesson on the lesson template for The Mechanics. No
code.

## The behavior and the causal chain

The word attached to the weaker version is "quantized." The lesson explains what
that does to the model and why it sometimes barely matters and sometimes matters
a lot. Each step names a real part of the system in plain words, with a small
concrete example, and marks whether it is settled engineering or an open
question. Pursue this chain and let the evidence set the details:

- A model's learned behavior lives in its weights, which are numbers. By default
  each is stored in a 16-bit floating-point format. Link where "weights" was
  already taught rather than re-teaching it.
- Quantization stores each weight in fewer bits, for example 8-bit or 4-bit
  integers, so the model fits in less memory and runs cheaper. Give the concrete
  size drop for a real model (bits per weight times parameter count).
- Fewer bits means a coarser grid of representable values, so each weight is
  rounded to the nearest allowed value. The per-weight error is tiny; there are
  billions of weights.
- Why it usually costs little: measured degradation (perplexity, task accuracy)
  is small down to 8-bit and modest at 4-bit under good schemes. Give the real
  measured numbers.
- Why it sometimes costs a lot: a small number of outlier values carry outsized
  magnitude, and naive rounding damages them out of proportion. This is the
  outlier-feature finding; report it from the primary that established it, and
  name what the better schemes do to protect those values (higher precision for
  outliers, per-group scales).
- Ground: the reader should end able to say that the numbers are rounded to a
  coarser grid and that the large-magnitude values are what rounding most
  endangers. Mark what is settled (8-bit is near-lossless; outliers matter) and
  what is still open (why outlier features arise; the accuracy floor at very low
  bit-widths).

## Boundary against the published course

Keep the line sharp against neighboring mechanics lessons and link, do not
re-teach:

- `sampling-temperature`, `random-numbers`, `nondeterminism` — these are about
  the sampler and decoding, not the weights. This lesson is about the weights
  themselves. Do not let it drift into a decoding story.
- `parameter-count` (The Instruments) — how many weights there are. Quantization
  is bits per weight. Complementary; link if the reader needs the count concept.
- `knowledge-distillation` (The Evidence) compresses by retraining a smaller
  network; quantization keeps the same network at lower precision. One contrast
  line at most.

No published mechanics lesson covers precision or quantization, so this is new
ground.

## Tonight's neighbors

Four other lessons run tonight on distinct beats: a vision research paper (The
Evidence), a proof-graded benchmark number (The Instruments), an alignment
argument (What Could Go Wrong), and a deployed-system failure (When AI Breaks).
No subject overlap; all five read as one paper.

## Template, sources, production

- Template: lesson. Word band 1200–2200. Bookends are citation-exempt; every
  body section carries its own citations. No code listings anywhere.
- Source policy: at least 8 sources, at least 4 primary and at least 1
  secondary. The papers that established outlier-aware 8-bit inference and the
  4-bit post-training methods are primary, as are the maintained measurements
  from the tooling that ships these schemes. Explainer write-ups are secondary.
  Every measured degradation figure needs the primary that owns it.
- Production policy (balanced, model tier "capable", nothing `required`):
  researcher high, writing-coach low, writer medium, editor high. Roles run as
  isolated subagents on the runtime's default capable-tier model. No deviation
  recorded.

## Recent shapes to break

Recent The Mechanics lessons open on a flat statement of the mechanism and close
on a "the gap keeps closing" assessment; several string four or five short body
sections in a row. Do not inherit the closing-assessment mold or a uniform run
of same-length sections; vary section construction and let some sections carry a
worked number or a table. Headings are concrete, in this lesson's own nouns. The
bookend bands and the Sources heading are the only mandatory fixtures.

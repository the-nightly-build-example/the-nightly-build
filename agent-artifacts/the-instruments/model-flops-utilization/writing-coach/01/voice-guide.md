# Voice guide: the-instruments / model-flops-utilization

The press voice, applied to this one measurement. Short by design. The writer
holds the house standard already; this only says how MFU in particular should
sound.

## The register for this piece

Write it the way Matt Yglesias would explain a ratio he understands cold: plain
claims, concrete stakes, no fuss. MFU is arithmetic the reader can follow, so
show the arithmetic. When a sentence could be short or clever, be short. The
reader is smart and has never divided achieved FLOPs by peak FLOPs before. Teach
the division, not your feelings about it.

## What this measurement demands

- **One idea before the next.** MFU is a fraction. Teach the top (the model's
  own FLOPs) fully, then the bottom (the chip's peak), then what the fraction
  does and does not mean. Never introduce the sparsity catch before the reader
  can compute a plain MFU.
- **Define the primitives in plain words, once.** "FLOP" and "peak FLOPs" get a
  plain-language definition in the sentence they first appear, then are reused by
  those exact names. Do not re-teach a parameter or total training compute: link
  the earlier lessons (`parameter-count`, `training-compute`) in prose and move
  on.
- **Every number is a real number from a real run.** PaLM's 46.2%, its 238,300
  tokens per second, the H100's spec-sheet lines. Reproduce the reported figure
  from the parts so the reader sees the machinery is honest, then show where the
  same parts, divided differently, stop being comparable.
- **The catch is the denominator, and it is concrete.** "Peak FLOPs" is a
  spec-sheet choice: which precision, sparsity or not. Show the H100's own
  numbers moving fourfold. Do not gesture at "it depends"; put the two numbers
  side by side and divide.

## What to avoid

- The desk's headline habits: no "The number that ...", no "X is a Y that pays
  out for Z." Commit the headline to one concrete surprise about MFU and stand
  behind it.
- The dek habit: no "X is [definition], and [limitation]" mold (auroc,
  calibration-error already used it). No semicolon reversal, no comma-and triad.
- No final heading of the form "How far the X reaches." Vary how the headings
  are built; do not chain two clauses with a comma and "and."
- Slop at the edges. The body speaks to no one and never mentions the lesson.
  Only the two bookends address the reader. The last sentence of the body is the
  likeliest place to write something that grades the argument instead of
  continuing it. Cut it if it does.
- No hype. MFU is not a triumph or a scandal. It is a ratio with a soft floor.
  Let the numbers carry the weight; reach for no grand word the arithmetic has
  not earned.

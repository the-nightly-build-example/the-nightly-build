# Draft handoff: the-mechanics/formatting-defaults (01)

## Original work

The article threads the evidence record's separate measurements into one backward
walk from the visible bulleted answer down to its cause, marking each link
settled or open, so a reader gets an auditable causal chain rather than a pile of
independent findings about length, formatting, and reward bias.

## Proof result

`./nb check ... --series the-mechanics --library <checkout>` (links included):
**BLOCK: 0, WARN: 1**, verdict PUBLISHABLE.

Warning intentionally left:

- **W-CITE-DENSITY, section `tokens`** — the token/pretraining step carries no
  inline citation on purpose. The evidence record states the pretraining
  contribution has no dedicated primary and must be treated as background,
  "marked open, not a cited finding." The section says so in the prose (direction
  clear, size unmeasured, "the first open link in the chain") and links the prior
  `autoregressive-generation` lesson in prose, which the press rule forbids
  turning into a numbered source. Adding a citation here would mean fabricating or
  padding one, which `spec/editorial.md` bars. The step is a real link in the
  backward walk, so it was kept as its own section rather than folded away to
  silence the warning.

## Notes for the editor

- Second person is used only in the two bookends; the body speaks to no one, per
  the lesson template's identity rule. The voice guide's Evans/Ciechanowski "you"
  passages were read for rhythm and register, not carried into body address.
- One chart (`chart-1.png`, LMSYS style coefficients, both length and markdown
  controlled) is built from the Numbers block via `nb chart`; its `chart-1.py`
  carries the data as provenance. It was inspected after rendering and shows
  length towering over the three markdown features. The entanglement figure
  (lists 0.111 when length is free) is handled in the caption and body prose.
- The length-vs-markdown precision is framed as structure-and-length together
  with length the heavier half, and the content-independence claim is written as
  "substantially independent... not wholly," carrying LMSYS's own observational
  caveat and Singhal's dataset-varying split.

## Open questions

None blocking. The two thin links the brief named (pretraining share, and the
formatting makeup of instruction-tuning demonstrations) are genuinely
undisclosed in the public record and are marked open in the piece; neither
requires a new researcher request.

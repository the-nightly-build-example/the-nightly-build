# Draft handoff: the-evidence/llama-3-herd-of-models (01)

## Original work

The article reads Meta's own benchmark table (Table 2) and its own
contamination table (Table 15) against each other to establish that the report
cannot certify the very scores that made it famous. The evidence record holds
both tables and the reason the four cells are blank, but never puts the two
side by side to reach that conclusion; the article does.

## Proof

- Command: the exact `nb check ... --series the-evidence --library <checkout>`
  from the brief, links on.
- Result: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
- No warnings left standing. An earlier `--no-check-links` pass raised one
  W-SENTENCE-DENSITY on a 52-word sentence in the orientation; I split it into
  two, and the warning cleared.
- `nb stamp`: words 2144, reading_minutes 9, sources 7 (5 primary, 2
  secondary). `nb preview` builds the article with the stat strip, both tables,
  and the OSI position card present in the output.

## How the brief's precision points landed

- Llama 3 vs 3.1 named exactly in the orientation, using Table 1's own line.
- License framed as "open weights under a conditional community license";
  "open source" carried as Meta's label (s5) against the OSI's rejection (s6),
  not adopted as fact.
- The Llama 2 misconception is corrected directly: the 3.1 license requires
  renaming derived models, it does not ban training competitors on outputs.
- Table 15's four dashed benchmarks (MMLU, MMLU-Pro, HumanEval, MBPP) are the
  climax section; the piece spends the visual by lining those four against the
  headline benchmarks in Table 2.

## Furniture

Stat strip (scale/compute), a Table 2 subset (self-scored comparison), a Table
15 subset (the four blanks, rendered as "no estimate" rather than em-dash
glyphs to stay under the em-dash count), and an OSI position card for the
open-source rejection. No chart or source asset: every figure the argument
needs is in the verified Numbers, and Table 15's blanks read as clearly in a
built table as in a screenshot.

## Open questions

None blocking. The evidence record supplied every claim the piece rests on. The
LMArena result is used only as context (preference, not accuracy), matching the
researcher's caution, not as a refutation of Meta's table.

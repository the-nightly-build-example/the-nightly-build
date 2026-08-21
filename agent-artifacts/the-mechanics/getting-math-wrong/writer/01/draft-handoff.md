# Draft handoff: the-mechanics/getting-math-wrong (01)

## Original-work statement

This lesson threads twelve separately-sourced findings into one backward chain
from a single documented wrong product down to the point where the researchers
disagree, placing each mechanism where the reader first needs it and marking in
prose where settled engineering gives way to the live interpretability dispute,
so a reader can see which part of the system owns each part of the failure.

## Proof result

`./nb check ... --series the-mechanics --library <scratch>/library-checkout`
run links-on (no `--no-check-links`): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
No warnings left standing. (An earlier links-off pass raised three
W-SENTENCE-DENSITY notes on long sentences in the two bookends and the carry
step; all three were split and cleared.) Stamped words=2043 (band 1200-2200),
reading_minutes=9, sources=12 (10 primary, 2 secondary).

## Scoping decisions carried out (per brief)

- Whole lesson scoped to the raw, no-tool, no-scratchpad path; the "modern
  products get it right via step-3 fixes, not a new arithmetic unit" caveat is
  stated in the opener and again in the carry step.
- Tokenization cause scoped to OpenAI-style tokenizers (`\p{N}{1,3}`); the
  single-digit-tokenizer models (LLaMa, PaLM) are named as the exception, with
  their failure routed to the carry step instead.
- Step 4 kept open in prose (bag-of-heuristics vs helix/Clock as the live
  disagreement; Nanda's modular-addition circuit flagged as a toy, not the
  explanation of real multiplication). Settled/open marked in prose, no stock
  heading, and without leaning on the word "unsettled."

## Judgment calls worth an editor's eye (no decision needed)

- Furniture: two `nb-table`s (the worked anchor; the accuracy fall-off). No
  chart — the fall-off is three points, and the evidence record says not to
  force one; the table carries the trend honestly.
- The broader single-digit-tokenizer landscape is scoped via Singh & Strouse
  (LLaMa, PaLM) alone; Millidge (Mistral/Gemma/DeepSeek) was left out to keep
  the source set lean, since the scope claim only needs one owner.

## Open question

None blocking.

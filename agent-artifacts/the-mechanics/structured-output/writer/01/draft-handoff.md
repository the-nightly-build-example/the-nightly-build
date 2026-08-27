# Draft handoff: the-mechanics/structured-output (writer 01)

## Original-work sentence

This lesson threads four separate literatures (two constrained-decoding
implementations, the Tam et al. study, and the dottxt rebuttal) into one causal
chain that locates the accuracy cost in the reasoning room a schema can
foreclose rather than in the mask itself, and it shows the headline
disagreement over the penalty's size is really a disagreement about whether the
schema asks for the answer before the reasoning. The evidence record holds
those pieces side by side; the article is where they become one argument, with
the answer-before-reason field order as the hinge that reconciles Tam and
dottxt. The work is visible in the "disputed size" section (the two-row-camp
table plus the reconciliation) and the "let the model reason before it fills
the form" close.

## Proof result

- Command: `./nb check .nb-work/the-mechanics/structured-output/library/the-mechanics/structured-output.html --series the-mechanics --library /home/user/library-checkout`
- Links included: BLOCK: 0, WARN: 0, verdict PUBLISHABLE.
- Stamp: words 1924, reading 8 min, sources 8.
- No warnings intentionally left. Two W-SENTENCE-DENSITY warnings during
  iteration were fixed by splitting the flagged sentences, not waived.

## Source and citation notes

- 8 sources, first-citation order: 1 Tam et al. (primary), 2 Willard & Louf
  (primary), 3 XGrammar/Dong et al. (primary), 4 Let's Data Science
  (secondary), 5 Willison (secondary), 6 OpenAI docs (primary), 7 dottxt
  (primary), 8 Aidan Cooper (secondary). Five primary, three secondary; clears
  the series floor (8 / 4 primary / 1 secondary) with headroom.
- The reasoning-room rung (Wei et al.; Merrill & Sabharwal in the evidence
  record) is taught ground from thinking-out-loud, so it is linked in prose per
  press editorial policy, not carried as a numbered source. That is why those
  two primaries from the evidence record are not in the source list.
- Quarantine respected: the gated OpenAI announcement and its 100% / under-40%
  eval figures are not cited or quoted anywhere. OpenAI's mechanism and the
  JSON-mode-vs-Structured-Outputs distinction come from the openable docs page
  (6) and Willison (5).
- Terminology collision handled explicitly in the mask section: "JSON mode" is
  reserved for OpenAI's weaker feature; the hard-constrained thing is called
  constrained decoding throughout. The piece flags that Tam uses "JSON mode" in
  the opposite (hard-constrained) sense.
- Tam's contested figures are presented as one camp's contested measurement in
  a clearly captioned table, never as the settled cost of formatting; the
  caption and prose state that the two camps constrained the task differently.

## Furniture

- One nb-table (the Tam vs dottxt comparison) and one nb-note ("In plain
  language", carrying Let's Data Science). Rendered and inspected via
  `nb preview`; the bare table is dressed by the runtime into the data-block
  card as designed.

## Open questions

None blocking. One judgment call for the editor to confirm: the disputed-size
table caption uses a single semicolon to pair the two camps' setups ("Tam's
schema put the answer before the reasoning; the Outlines team kept the
reasoning..."). It reads as one tightly bound contrast and passed the proof, but
it is the one semicolon in the piece if the desk prefers none.

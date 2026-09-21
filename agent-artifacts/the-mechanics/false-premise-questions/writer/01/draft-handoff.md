# Draft handoff: the-mechanics/false-premise-questions (01)

## Original work

The article threads ten separate findings into one downward causal chain, from the
observed behavior to the training objective, holding the *detection*-versus-*verification*
split distinct at each level and marking exactly where settled engineering ends and the
open questions begin, so the reader can name the step any glib explanation skips.

## Proof result

`nb check … --series the-mechanics --repo …` (links included): **BLOCK: 0, WARN: 0,
PUBLISHABLE**. Stamped words=2200 (top of the 1200-2200 band), reading_minutes=10,
sources=10 (9 primary, 1 secondary; floor is 8/4/1). No warning left standing.

## Decisions the editor should know

- **Flagged examples not printed.** The brief flagged "When did Marie Curie discover
  Uranium?" and "How many eyes does the sun have?" for exact-wording confirmation. The
  evidence record carries them only as unverified candidate assets, and I could not confirm
  their wording against the owning papers, so I did not quote either. The grounding example
  is a generic, recognizable false-premise scenario ("why a novel that was never written
  stirred controversy") presented as illustration, not attributed to any dataset.
- **Taught ground linked, not re-taught.** Next-token prediction links
  `autoregressive-generation`; RLHF/preference tuning links `sycophancy`. GPT-3 (s3) and
  InstructGPT (s6) are still cited as the primary sources for the two settled claims the
  descent rests on (the objective; that post-training optimizes helpfulness, not
  premise-rejection), which is sourcing specific facts rather than re-teaching the concepts.
  `hallucination` and `sycophancy` are linked at first use to mark the boundary, per commission.
- **Indirect-strength step stated as such.** The "training text answers rather than corrects"
  step is explicitly marked as inferred from behavior (models hold the knowledge yet default
  to answering; FalseQA's 256-example fix), not from a corpus count.
- **Recent shapes broken.** No "presses X into its probabilities" dek; no reflexive "the fix
  doesn't work" penultimate section — the closer is a genuine open-questions section ending on
  the understanding-vs-pattern question. Dek and headings checked against the recent library.
- **Furniture: one table.** The Cancer-Myth per-model correction table carries the
  generation-over-generation rates. A CREPE-authors quote note was drafted and then cut during
  length trimming; the detection/verification point it reinforced is fully carried in prose.
  Length was trimmed hard from 2652 to 2200 to land inside the band. If the editor wants the
  CREPE quote or a fuller Sieker (s9) generality beat restored, the piece will run over 2200.

## Open questions

None blocking. The evidence record was sufficient; no researcher request is needed.

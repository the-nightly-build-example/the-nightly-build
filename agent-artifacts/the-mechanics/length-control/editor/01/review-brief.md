# review brief: the-mechanics/length-control (editor/01)

Inputs (all under the artifact root .../agent-artifacts/the-mechanics/length-control/, plus the article and template context in the workspace):
- editorial-direction.md — the standard
- commission.md — the assignment, boundaries, the no-code rule, neighbors to link
- writer/01/brief.md — the exact writer brief
- writing-coach/01/voice-guide.md (reused from a same-series sibling — judge craft, not subject)
- researcher/01/evidence.md
- writer/01/draft-handoff.md — original-work sentence and open items
- Article: /home/user/the-nightly-build/.nb-work/the-mechanics/length-control/library/the-mechanics/length-control.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/length-control/.nb-context/

## Recent-pattern notes

Established library of 130+ lessons; NOT an inaugural edition. Two cross-check sets.

1. The published series record. Query it: `nb history --library
/home/user/library-checkout --series the-mechanics --limit 8` for recent deks, and
`--structure the-mechanics/<slug>` for a neighbor's headings. The house dek is one
concrete sentence, usually two clauses with a VARIED connector, not always "and".
Headlines are sentence-case declarative findings. Headings are concrete and
piece-specific. Flag any dek/heading repeating a shape the recent series record
already leans on.

2. Tonight's five sibling lessons (published together):
   - the-evidence/foundation-models — H: "The report that coined 'foundation models' ran no experiment"
   - the-instruments/tau-bench — H: "GPT-4o clears 61% of τ-bench tasks once and under 25% of them eight times in a row"
   - the-mechanics/length-control — H: "A model can't count the words it's writing"
   - what-could-go-wrong/model-collapse — H: "Generative models fed only their own output collapse within nine generations"
   - when-ai-breaks/biden-deepfake-robocall — H: "The FCC's $6 million fine over the Biden robocall survived Steve Kramer's acquittal"
   Dek connectors vary across the edition; headlines are all sentence-case declaratives.

## Round focus

- Confirm the compounding of trained-in length bias with the no-counter architecture
  is presented as the writer's clearly labeled synthesis, NOT a single measured chain
  (the RLHF length-bias study measured behavior with no length instruction present).
- Confirm IFEval's pooled 76.89% is not quoted as a length-following number; the
  length-specific figures (e.g. GPT-4 Turbo's 49.3% miss, LIFT) are the ones used.
- Confirm the settled/open split is honest (settled: token-by-token, no counter,
  tokens≠words; open: hidden-state length signal vs self-report failure, held unresolved)
  and that autoregressive-generation, letter-counting, and formatting-defaults are
  LINKED, not re-taught. No code anywhere; the token point is prose/table only.

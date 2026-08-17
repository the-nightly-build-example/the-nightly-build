# review brief: the-instruments/tau-bench (editor/01)

Inputs (all under the artifact root .../agent-artifacts/the-instruments/tau-bench/, plus the article and template context in the workspace):
- editorial-direction.md — the standard
- commission.md — the assignment, boundaries, neighbors to link
- writer/01/brief.md — the exact writer brief
- writing-coach/01/voice-guide.md (reused from a same-series sibling — judge craft, not subject)
- researcher/01/evidence.md
- writer/01/draft-handoff.md — original-work sentence and open items
- Article: /home/user/the-nightly-build/.nb-work/the-instruments/tau-bench/library/the-instruments/tau-bench.html
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/tau-bench/.nb-context/

## Recent-pattern notes

Established library of 130+ lessons; NOT an inaugural edition. Two cross-check sets.

1. The published series record. Query it: `nb history --library
/home/user/library-checkout --series the-instruments --limit 8` for recent deks, and
`--structure the-instruments/<slug>` for a neighbor's headings. The house dek is one
concrete sentence, usually two clauses with a VARIED connector (and / then / but /
not / which / participial), not always "and". Headlines are sentence-case
declarative findings. Headings are concrete and piece-specific. Flag any dek/heading
repeating a shape the recent series record already leans on.

2. Tonight's five sibling lessons (published together):
   - the-evidence/foundation-models — H: "The report that coined 'foundation models' ran no experiment"
   - the-instruments/tau-bench — H: "GPT-4o clears 61% of τ-bench tasks once and under 25% of them eight times in a row"
   - the-mechanics/length-control — H: "A model can't count the words it's writing"
   - what-could-go-wrong/model-collapse — H: "Generative models fed only their own output collapse within nine generations"
   - when-ai-breaks/biden-deepfake-robocall — H: "The FCC's $6 million fine over the Biden robocall survived Steve Kramer's acquittal"
   Dek connectors vary across the edition; headlines are all sentence-case declaratives.

## Round focus

- The illustrative phrase in the Why-this-matters card ("Our agent handles 58% of
  customer requests") is an unattributed example, not a sourced quotation. Confirm it
  cannot read as a real quote; reword if it can.
- Three section headings open with "One..." (One conversation / One try / One chart),
  an anaphora forming a within-article formula. Vary at least one.
- Confirm the paper's internal 35.2%/33.2% discrepancy is flagged rather than silently
  resolved; the o1 figures are attributed only to Anthropic's reporting (not
  independently verified); and the "often, not always" framing on bare-number quoting
  holds (the Automation Anywhere counter-example). The reliability collapse is carried
  by a stat strip, not a fabricated pass^k chart — confirm the figures match the paper
  and no intermediate k values were invented.
- Confirm the llm-as-a-judge link uses the narrow, evidence-specified distinction
  (τ-bench's reward is rule-based; the simulated user only generates the conversation).

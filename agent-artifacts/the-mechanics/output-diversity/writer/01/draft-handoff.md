# Draft handoff: the-mechanics/output-diversity (01)

## Original-work sentence

The article assembles six separate research findings into one backward causal
chain from a behavior readers have seen (the recurring Elara) to its mechanism,
and in doing so isolates the reader's instinctive fix, temperature, as powerless
against a narrowing that happens at training time rather than at the draw, a
line none of the sources draws on its own.

The work is visible in the "reward-narrowing" section (where the InstructGPT
objective separates the reward term that narrows from the KL leash that only
bounds drift) and the "temperature" section (where Mohammadi's T=1 attractors
and Wu's 82.1%→58.1% sweep are joined to the sampling-temperature lesson to show
why a hotter knob samples a narrowed distribution rather than widening it).

## Proof result

`./nb check … --series the-mechanics --library <checkout>` with links:
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warnings left standing. (Three
W-SENTENCE-DENSITY notes and one W-CITE-ORDER note were raised during iteration
and all fixed by splitting sentences and renumbering sources into first-citation
order.)

## Open evidence / voice questions

- **Equation weight, for the editor's judgment.** I included the InstructGPT
  objective as an annotated equation because it is the cleanest anchor for the
  reward-maximization-vs-KL-leash distinction the round insists on. It is also
  the heaviest element for a reader with no codebase. It reads correctly if
  skipped (the surrounding prose carries the mechanism), but the editor may want
  to weigh whether it earns its place against prose alone.
- **Rendering not Chrome-verified.** The sentiment table and the KaTeX equation
  use the engine's documented furniture markup and survived the full `nb preview`
  site build intact, but `nb render-check` needs a served-site path plus Chrome
  and I could not complete a visual probe here. Worth a rendered look before
  publish, especially the annotated equation's colored terms in both schemes.
- No open evidence gaps: every claim comes from the evidence record. Kirk's
  broken-axis figures are used only qualitatively (across-input mode collapse),
  and Mohammadi's entropy is used by direction only (no exact value or the
  2.32-bit ceiling quoted), per the round's caveats.

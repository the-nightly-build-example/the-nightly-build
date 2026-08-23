# Commission: what-could-go-wrong/natural-selection

## Assignment

One lesson for What Could Go Wrong, on the lesson template, on a single argument:
that competitive and evolutionary pressure among AI systems, not any malice or
mistake by their designers, could select for AIs that seek power, deceive, and
propagate — so undesirable traits would emerge and dominate even if every
individual developer tried to prevent them. The canonical modern statement is Dan
Hendrycks, "Natural Selection Favors AIs over Humans" (2023). This is the
scheduled open article for the series on 2026-08-23.

## The argument at full strength, then tested

The beat's method: open with the argument as its most careful defender would put
it, name who made it and what they had seen, then draw a sharp line between what a
working system has already shown and what is still analogy about systems that do
not exist yet, then bring it to the present.

- Full strength: Hendrycks argues the three Darwinian conditions (variation,
  heritable-enough traits via copying/finetuning, and competition for scarce
  resources — compute, market share, users) already apply to AI development, so
  selection pressure favors AIs that are more capable, more autonomous, better at
  acquiring resources, and better at deceiving overseers, regardless of what any
  designer wants. The pressure operates at the level of the population of systems
  and firms, not one lab's intentions. Present the reasoning honestly and its
  intellectual lineage (Darwin; and earlier related worries about competition
  eroding safety).
- The line: what has actually been *shown* in a working system is thin and must
  be named precisely. Real, demonstrated fragments include specification gaming /
  reward hacking, and lab-induced power-seeking or deception under contrived
  setups. What is still analogy: that a self-sustaining evolutionary dynamic among
  AIs exists in the wild, that traits are "heritable" in the strong sense the
  argument needs, and that selection has ever actually produced a harmful trait no
  one trained for. No such wild dynamic has been observed.
- Present day: who presses this now and what they want done (governance,
  limiting autonomy, competition-aware safety), and check the confidence against
  the evidence in both directions — the argument's boosters and its dismissers
  both outrun the proof.

## Required contribution

The reader should be able to state the natural-selection argument in its strong
form, name the three conditions it requires and judge for each whether real AI
development meets it, separate the demonstrated pieces (reward hacking, contrived
power-seeking) from the speculative whole (a wild evolutionary process among
AIs), and see exactly where the confidence — doom or dismissal — runs past what
has been shown. Name no company as an authority. Leave the reader to decide how
worried to be.

## Boundaries

- One argument. This is *selection pressure across a population of systems*, and
  it must be kept distinct from its neighbors already in the library:
  `what-could-go-wrong/racing-dynamics` (human developers racing each other),
  `gradual-disempowerment` (humans ceding control to systems they rely on),
  `instrumental-convergence` (why a single goal-seeker wants power),
  `mesa-optimization` and `reward-hacking`. Link these where the reader needs the
  prerequisite; do not re-argue them. The distinctive claim here is that
  *selection*, not a designer's objective or a single agent's goal, is the
  mechanism.
- Work from the original documents: Hendrycks's paper itself, and the primary
  results behind any "already shown" claim (the actual reward-tampering or
  power-seeking papers), never commentary about them.
- No hype, no doom. The grand word appears only after the argument earns it.

## Template, sources, policy

- Template: lesson. Word band 1200-2200.
- Source floor (nb source-policy what-could-go-wrong): at least 8 sources, at
  least 4 primary, at least 1 secondary. Primaries: Hendrycks 2023 (arXiv
  2303.16200), and the primary papers behind each "demonstrated" fragment the
  piece leans on (e.g. an Anthropic reward-tampering paper, a power-seeking or
  specification-gaming primary). Read them. Any survey or news coverage is
  secondary and labeled so.
- Production policy (balanced): writing-coach low, researcher high, writer
  medium, editor high; "capable" tier for all, resolved to Claude Opus 4.8.
  nb-meta harness `claude-code-routine`, model `claude-opus-4-8`.
- Suggested nb-meta tags: ai-safety, competition, evolutionary-pressure,
  multi-agent.

## This edition's neighbors

`the-evidence/adam-optimizer`, `the-instruments/squad`,
`the-mechanics/false-confidence`, `when-ai-breaks/michigan-midas`. No subject
overlap; this is the only risk-argument piece.

## Recent shapes and phrasing to break

Recent What Could Go Wrong pieces (value-lock-in, unilateralists-curse,
gradual-disempowerment) share habits to avoid:

- The "N assumptions hold the proof together" `nb-table` mold (unilateralists-
  curse). The three Darwinian conditions invite exactly this; if a component
  helps, do not build it in that same shape or heading.
- The closer heading "how far the confidence runs past the proof" (value-lock-in)
  and "the step from N real losses to one that doesn't reverse" (gradual-
  disempowerment). The shown-versus-speculative judgment is central here, but
  write the closing section in this argument's own nouns.
- `nb-holdsup` is the series' shown-versus-speculative furniture and is
  appropriate for the "what a working system has shown" material, but do not copy
  value-lock-in's exact deployment of it. A component belongs only where it
  carries the argument.

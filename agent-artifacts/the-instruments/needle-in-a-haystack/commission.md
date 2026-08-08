# Commission: the-instruments/needle-in-a-haystack

## Authorization
Scheduled run for 2026-08-08 (Sat). `nb duty` returned the-instruments as an open
section: choose a topic within the beat, do not repeat a published slug. Verified
against the FULL published shelf (21 slugs); `needle-in-a-haystack` is not among
them. It is distinct from `context-window` (the raw number): NIAH is the eval used
to claim that number is usable. One article only. Template `lesson`.

## Subject
The needle-in-a-haystack (NIAH) test: the retrieval eval behind "1M-token context
with near-perfect recall" claims. A fact (the "needle") is inserted at some depth
inside a long filler text (the "haystack"), the model is asked to retrieve it, and
accuracy is scored across many depths and context lengths, usually shown as a
colored grid.

## Angle (the desk's shape: where the number comes from, then what it can and cannot support, with a real case where it misled)
- Where it comes from, step by step: who produced the popular version (Greg
  Kamradt's 2023 "Needle In A Haystack - Pressure Testing LLMs"), the construction
  (one planted sentence, e.g. the San Francisco / Pinterest "best thing to do" line,
  buried in Paul Graham essays), the sweep over document depth x context length, and
  how the green/red grid is read. Labs adopted and reported it in model releases
  (e.g. Anthropic's Claude 2.1 result and the "add one sentence" prompt fix; Gemini
  1.5's near-perfect NIAH numbers). Report the actual numbers from primaries.
- What the number can and cannot support: it measures verbatim retrieval of a single
  out-of-place fact, which is close to a lexical lookup, not comprehension or
  reasoning across the whole context. A near-100% NIAH score does not show the model
  can use long context for multi-fact reasoning. Cite the primary critiques that
  built harder successors: RULER (Hsieh et al. 2024) and multi-needle / reasoning
  variants, which show scores collapse when the task needs more than one fact or any
  aggregation.
- At least one real case where it misled, with the cost: models advertised with
  near-perfect NIAH yet failing on realistic long-context tasks (the "lost in the
  middle" degradation, or the multi-needle drop) - use a documented instance where a
  strong NIAH number oversold real long-context ability. Keep every specific to a
  primary.

## Required contribution
The reader can explain how a NIAH score is produced and read, why a single-needle
retrieval score says little about long-context reasoning, and can spot when a
"perfect recall at N tokens" claim rests on NIAH alone. Reported fact (construction,
numbers) stays distinct from synthesis (why retrieval != reasoning).

## Sources and policy
Source policy (lesson/the-instruments): min 8 sources; primary >= 4, secondary >= 1.
Primaries: Kamradt's original NIAH repo/thread; a lab report using NIAH (Anthropic
Claude 2.1 long-context post and/or Gemini 1.5 technical report); RULER
(arXiv:2404.06654) and/or a multi-needle primary; a "lost in the middle" primary
(Liu et al., arXiv:2307.03172) for the reasoning-vs-retrieval contrast. Read methods
sections. Secondary only for context.

## Boundaries
Link, do not re-teach, the raw context-window number (the-instruments/context-window)
and any tokenization already taught. This is a measurement lesson about an eval, not
a long-context tutorial. Probability/algebra assumed.

## Neighboring articles this edition
the-evidence/word2vec, the-mechanics/why-replies-stop,
what-could-go-wrong/data-poisoning, when-ai-breaks/optum-health-algorithm. This
piece owns the long-context retrieval eval; keep it to how that number is made.

## Habits not to inherit (recent the-instruments shapes)
Recent pieces (hallucination-rate, glue, tokens-per-second) open by naming the
leaderboard/company, run a "From <raw> to one <number>" heading, and lean on
nb-stat-strip. Do not reuse that heading mold or default to a stat-strip; the NIAH
grid itself may motivate a source-asset figure or a small table - choose from this
eval's needs. Name headings from the eval's own construction.

## Harness and model
harness `claude-code-routine`; model `claude-opus-4-8` for every role. Balanced
production policy; per-role effort not independently settable in this harness
(mechanism deviation only, model unchanged).

# Commission: the-evidence/mamba

## Assignment
Read the 2023 paper "Mamba: Linear-Time Sequence Modeling with Selective State
Spaces" by Albert Gu and Tri Dao (arXiv:2312.00752) as one lesson on the
Evidence desk. Template: lesson. Publication date: 2026-09-13.

## Why this document, now
The course has taught the transformer and attention in depth: the-evidence
`attention-is-all-you-need`, the-mechanics `attention`, and the archived
`transformers-first-principles` series. It has never read the most-cited
document proposing a different way to model a sequence. Readers meet Mamba in
every "the transformer's reign is ending" argument. The lesson is readable now
precisely because the reader already knows what attention costs: Mamba's whole
pitch is a reply to that cost.

## The angle (the desk's arc)
State what the paper is, who wrote it, and why it became famous. Walk through
what it actually did: the mechanism (a state-space model whose update is chosen
by the input), the tasks and model sizes it ran, the throughput and
perplexity numbers it reported. Show the scale honestly: the headline results
were at small-to-mid model sizes, not frontier scale, and some benchmarks were
never run. Then bring it to the present: Mamba is invoked as proof the
transformer is finished, and later work both extended it (hybrids, Mamba-2) and
found real limits (copying and in-context retrieval). Say plainly where today's
"transformers are over" usage outruns what the paper showed.

## What the reader already holds — do not re-teach, link instead
- What a transformer and attention are, and that attention compares every token
  with every other: link `the-evidence/attention-is-all-you-need` (and/or
  `the-mechanics/attention`) in Background rather than re-teaching attention.
- Why cost grows with sequence length / long prompts: `the-mechanics/lost-in-the-middle`
  is available if a Background row helps.
Algebra and probability need no introduction. Everything else (state, recurrence,
perplexity as a measure) gets taught in plain words on the spot, briefly.

## Research directions (researcher owns depth)
1. The paper's own claims and scale: the selective state-space mechanism
   (input-dependent parameters; a compressed state carried forward instead of
   re-reading the whole sequence), the hardware-aware scan, model sizes tested,
   the equal-parameter comparisons against strong transformers on language
   modeling, the throughput and linear-scaling-in-length claims. Read the paper
   itself, not coverage.
2. Scale honesty: largest sizes actually trained, which benchmarks were and were
   not run, and any limits the authors state themselves.
3. Lineage: the S4 / structured state-space line the paper builds on
   (arXiv:2111.00396) and the older RNN/state-space idea, only as far as the
   lesson needs to make the mechanism land.
4. Present: how the paper is used in argument today; what later work did —
   hybrids that mix attention and state-space layers (e.g., Jamba,
   arXiv:2403.19887), Mamba-2 (arXiv:2405.21060), and findings of real limits at
   copying / in-context retrieval (e.g., "Repeat After Me", arXiv:2402.01032, and
   related state-space-limitation results). Whether pure state-space models
   displaced transformers at the frontier (they have not; record what did happen).
5. One concrete worked example that teaches the core contrast: a state-space
   model carrying a running compressed state forward versus attention re-reading
   every earlier token, and what "selective" adds (keeping or discarding a token
   by its content).

## Contradictions to probe
Whether Mamba truly "matches" transformers (equal-parameter perplexity versus
downstream and long-context retrieval tasks; the copying weakness), and whether
the throughput advantage holds outside the paper's setup. Record the strongest
evidence against the "transformer is finished" reading.

## Sources
Floor: at least 6 sources, at least 3 primary, at least 1 secondary. Primary:
the Mamba paper and the relevant follow-on/limitation papers it should be weighed
against. Secondary: reputable technical context only where a primary does not own
the point. Contested figures need the primary that owns them.

## Boundaries
No code. Teach the mechanism only as deep as a smart no-code reader needs. Do not
dump a benchmark table; the desk's point is honest scale plus how the document is
used in arguments now. One article, one document.

## Production policy (balanced profile; none required)
- writing-coach: model capable, effort low
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model capable, effort high
Runtime mapping: "capable" is served by the run's default subagent model
(Opus-class). Record the actual writer model in nb-meta. No required directive to
trade down.

## Neighbors in this run (keep the edition coherent, non-redundant)
the-instruments/bertscore, the-mechanics/speech-to-text-hallucination,
what-could-go-wrong/capability-elicitation, when-ai-breaks/retinopathy-field-study.
No topical overlap with any of them.

## Habits from the recent record not to inherit
- The Evidence deks and orientations often open by naming authors and year
  ("X et al.'s 2023 paper..."). Vary the entry into the piece.
- Recent deks lean on comma-joined clause chains and the "A [noun], whose
  [twist]" mold. Find this piece's own dek.
- Keep the desk's arc (what it is / method and scale / present) but name sections
  for this document, never with stock labels.

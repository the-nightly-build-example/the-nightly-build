# Draft handoff: the-mechanics/irrelevant-context (01)

## Original-work sentence

The evidence record lists both the settled behavior and the one contested
number side by side; this article sequences them into a single settled-then-open
argument, isolating the GSM-NoOp "up to 65%" drop as the lone contested link and
building the settled mechanism on the four clean perturbations (added-sentence
GSM-IC, name/number regeneration, the Alice puzzle, the counterfactual-task
suite), so a lay reader can see exactly where the "models cannot reason" claim
outruns its test.

## Proof result

`./nb check ... --series the-mechanics` (links included): **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. Stamped words=2187 (band 1200-2200), reading 10 min,
sources=8 (6 primary, 2 secondary).

No warnings intentionally left. The four W-SENTENCE-DENSITY notes from the first
pass were all resolved by splitting the dense sentences rather than recording an
exception. The proof's closing note ("library state not provided") is expected:
the brief's proof command omits `--library`, so open-mode dedupe and commission
checks are the orchestrator's to run, not blocked here.

## Decisions worth flagging to the editor

- Settled/open split handled per the brief: the strong claim rests on the clean
  perturbations; GSM-NoOp's 65% is presented as the contested part, attributed
  to Mirzadeh et al. and steelmanned against the Sturb 2026 re-analysis (117 of
  945 clauses unambiguous; filtered-set drop 0-2 points). The o1-preview vs
  GPT-4o vs Gemma2-9B table carries the "reasoning-tuned models resist more"
  contradiction. AIW is framed as a mid-2024 result, not a current ceiling.
- Tokens and attention are linked in prose (tokenization, attention lessons),
  never as numbered sources, per press policy. getting-math-wrong and
  prompt-sensitivity are linked in prose where the piece distinguishes itself
  from them. in-context-learning is not linked: the argument does not lean on it,
  so per "link any you lean on" it was left out rather than forced in.
- Sturb (LessWrong re-analysis) is carried as data-nb-kind="secondary". The
  evidence record's Kind line leads with "secondary" (primary only for its own
  rerun); marking it secondary also keeps the composition at 6 primary / 2
  secondary. The contested figure it addresses (the 65% drop) has its primary
  source in Mirzadeh (s3), satisfying "contested figures need a primary source."
- The GSM-NoOp per-model table figures are the paper's Table 1 values as read
  from the HTML rendering (evidence flagged them as not independently recomputed);
  the caption cites s3 with data-nb-locator="Table 1", which the evidence supplies.

## Open evidence or voice questions

None. The named inputs settled every claim and structural decision; no researcher
or writing-coach follow-up is needed.

# Researcher brief 02 — what-could-go-wrong/jailbreaks (evidence gap)

Load the `researcher` skill. Invocation 02: a targeted addition. Read ONLY your
prior `../01/evidence.md` and the new sources you open here. Write a complete new
`researcher/02/evidence.md` preserving all still-valid 01 work; do not overwrite 01.

## The gap the editor found (must fill)
The commission requires steelmanning the counter-argument that jailbreak risk is
OVERSTATED because the harmful information a jailbroken model would produce is
already publicly accessible, so the marginal capability a jailbreak adds is small.
Your 01 record and the draft lack a genuine, developed, attributable source for
this position. A thin blog comment or a discarded aside will not do.

## What to find (read firsthand, verify, classify)
Find at least one credible, named source that actually makes the "marginal risk /
already-public information" argument in the context of LLM misuse or dual-use
capability. Strong candidates to check first (verify they say what we claim):
- Sayash Kapoor, Rishi Bommasani, Arvind Narayanan et al., "On the Societal
  Impact of Open Foundation Models" (2024) — develops the MARGINAL-RISK framework
  (assess risk relative to pre-existing technology such as web search and already-
  available information). PRIMARY for that argument (the authors own the framework).
- The RAND red-team bioweapon study (Mouton et al., 2024) — found no statistically
  significant uplift from LLM access over internet-only baselines. PRIMARY for the
  empirical "no measurable marginal uplift" result. (Note: this paper's neighbor
  what-could-go-wrong/bioweapon-uplift already covered RAND — cite it for the
  marginal-uplift point here, but do NOT re-teach it; the writer will link.)
- If neither fits precisely, find another credible primary/secondary (a named
  researcher's paper, congressional testimony, or a serious outlet) making the
  already-public / marginal-capability argument specifically.
Also record the strongest REBUTTAL to the marginal-risk view (e.g., that
convenience/scale/synthesis is itself an uplift, or that "already public" understates
aggregation) so the writer can weigh it, not just assert it.

## What to do
Add the new source(s) to Sources with primary/secondary classification and reason,
add any load-bearing figure to Numbers, and note the marginal-vs-absolute-risk
tension in Contradictions. Keep counts honest; do not pad other rows. Confirm every
new URL resolves.

Return exactly one line: `DONE researcher <path to researcher/02/evidence.md>`,
or `BLOCKED researcher <reason>`, or `REQUEST orchestrator <need>`.

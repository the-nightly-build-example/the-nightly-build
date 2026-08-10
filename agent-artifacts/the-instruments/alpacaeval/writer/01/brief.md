# writer brief: the-instruments/alpacaeval (01)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the-instruments prompt, template identity.
- writing-coach/01/voice-guide.md — how this lesson should sound, with exemplar passages.
- researcher/01/evidence.md — the complete claim set: verified figures, versions, contradictions, source kinds.
- The initialized article at library/the-instruments/alpacaeval.html and its .nb-context/ contract.

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/alpacaeval/library/the-instruments/alpacaeval.html --series the-instruments --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --series is required in local mode; use --no-check-links while iterating, links included until BLOCK: 0)

Set nb-meta the engine cannot compute: date 2026-08-10, harness claude-code-routine, model
"Claude Opus 4.8", and tags ["evaluation", "win-rate", "llm-as-judge"]. nb stamp writes the counts.

Handle these from the evidence with care:
- Keep two things distinct throughout: a model genuinely preferred, and a model winning by length under a
  biased judge. Always name which version (1.0 vs 2.0), judge, and reference a number belongs to, because
  the same model reads very differently across them (the evidence gives Zephyr at 90.60% on 1.0 versus about
  13% LC / 11% raw on 2.0).
- Do not present length control as a complete fix. The evidence's null-model result shows a constant
  off-topic answer scoring about 86% length-controlled; state that LC reduces verbosity gaming without
  closing it.
- Cite the correlation as 0.94 to 0.98 (the paper owns the regression); the repo's 0.93 is rounding, note it
  only if useful.
- Run-environment caveat: an upstream automated read fabricated a win-rate figure before the researcher
  caught it against the real table. Before you commit any exact decimal in display text or a load-bearing
  figure, confirm it against the cited table in the evidence record; do not use the judge's human-agreement
  digit (the evidence has two conflicting reads) unless you reopen and confirm it.

Recent habits to break (from the-instruments and the house record; the voice guide does not carry these):
- Do not reach for the desk's "two measures disagree / both are true" headline reveal (fid,
  tokens-per-second, energy-per-query). State AlpacaEval's own surprise plainly.
- Do not end the opener with an enumerated roadmap. State stakes without touring the sections.
- Do not open the takeaway on a bare restated definition. Resolve what the opener set up.
- If you earn a "where it holds" section, do not copy fid's "Where the number keeps its word"; name it in
  AlpacaEval's own nouns.

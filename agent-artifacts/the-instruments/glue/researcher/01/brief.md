# researcher brief: the-instruments/glue (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the exact subject, angle, and required contribution

Output: ./evidence.md

Primary sources to read firsthand:
- GLUE paper: Wang, Singh, Michael, Hill, Levy, Bowman, "GLUE: A Multi-Task
  Benchmark and Analysis Platform for Natural Language Understanding" (2018,
  arXiv 1804.07461). Read the nine tasks, how the overall score is aggregated,
  and the human-baseline construction and number.
- SuperGLUE paper: Wang et al. 2019 (arXiv 1905.00537). Read why GLUE was
  retired ("performance surpassed the level of non-expert humans"), the new tasks,
  and the new human-baseline number.
- The artifact/shortcut evidence: Gururangan et al. 2018 "Annotation Artifacts in
  Natural Language Inference Data" (hypothesis-only baselines) and/or Poliak et
  al. 2018; and any GLUE/SuperGLUE-specific artifact analysis. Read the actual
  reported shortcut accuracies.
- The leaderboard record showing when models passed each human baseline (dates
  and which model). Use the official GLUE/SuperGLUE leaderboard or the papers'
  own reporting; verify the surpass dates as precisely as the record allows.

Verify every figure against its owner: the human-baseline scores, the surpass
dates, the hypothesis-only shortcut accuracies. For contested framing ("solved
understanding"), steelman the benchmark authors' intent (they built it to be
retired) and the critics'. Record disagreements in Contradictions.

Also useful (label primary/secondary honestly): a source documenting that
SuperGLUE too was surpassed, and any critique that benchmark saturation does not
equal understanding (this may connect to stochastic-parrots-style arguments;
cite the primary, not commentary).

Source policy: at least 8 sources, at least 4 primary, at least 1 secondary.
Primary = the party that owns the claim (benchmark authors, the artifact-study
authors, the leaderboard).

Environment: fetches go through a proxy; on 403/paywall retry with a
browser-style request first, and record each source's own canonical URL.

Sanity check: the full published the-instruments slug list is in the
commission's Boundaries. Do not build the record around a duplicate angle.

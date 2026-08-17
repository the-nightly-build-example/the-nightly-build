# researcher brief: the-instruments/tau-bench (01)

Inputs:
- editorial-direction.md — citation standard, series territory, declared reader (at the artifact root)
- commission.md — the measurement, the angle, and the source policy (at the artifact root)

Output: researcher/01/evidence.md

Read the τ-bench paper first (arXiv:2406.12045): establish who built it and at
what organization, the domains it covers, how a task is set up (the tools/mock
database, the simulated user played by a language model), and exactly how success
is scored (final database/state match, and any info-check component). Capture one
concrete task the reader can be walked through. Record the exact pass@1 figures
the paper reports and, crucially, the pass^k reliability figures and how far they
fall from pass@1, with the value of k. Read any follow-up (τ²-bench) and at least
one model report (2025 vintage) that states a τ-bench number in public use.
Establish the benchmark's own stated limitations (simulated-user fidelity,
verifier scope). Verify every figure against the source that owns it, classify
each source primary or secondary with the reason, and record contradictions or
disputed numbers. Note whether a pass@1-versus-pass^k comparison would be an
honest chart (build only from figures the paper reports). Use
`nb history --library /home/user/library-checkout` to find the exact slugs/titles
of published the-instruments neighbors the writer should link (swe-bench,
llm-as-a-judge, alpacaeval) and record them. Meet the source policy in
commission.md (min 8 sources, >=4 primary); no padding.

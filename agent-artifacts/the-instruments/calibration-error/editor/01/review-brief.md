# editor review-brief: the-instruments/calibration-error (01)

Inputs (read all):
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/editorial-direction.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/commission.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/writer/01/brief.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/writing-coach/01/voice-guide.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/researcher/01/evidence.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/writer/01/draft-handoff.md
- Article: .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html
- Template context dir: .nb-work/the-instruments/calibration-error/.nb-context/

Output:
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/editor/01/editorial-review.md

Proof (read-only if you want to confirm your edits; orchestrator stamps before PR):
- ./nb check .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html --series the-instruments --library /home/user/library-checkout

Round focus: verify the metric is taught correctly and the two pitfalls stay
distinct. Confirm: one ECE formula used consistently (Guo acc/conf, Naeini
credited); the worked table and reliability-diagram chart are labeled ILLUSTRATIVE
(constructed, not source data) with arithmetic checkable; the Brier convention is
stated; GPT-4's "confidence" is defined as logprob over answer choices with the
missing-bin-count caveat; and CRUCIALLY that "binning can flatter ECE" (a metric
flaw) is kept explicitly separate from "RLHF degraded GPT-4's calibration" (a
substantive finding OpenAI reported with its own binning) — the piece must not
present the GPT-4 numbers as binning manipulation. Inspect the chart's committed
provenance (chart-1.py) and read the rendered image for honest axes/labels; the
chart is the writer's to correct if wrong. Confirm the-mechanics/false-confidence
is linked, not re-taught.

Recent-pattern notes (compare deks, headings, openers, closers, furniture; one article cannot show these):
- Deks: number-first is house style; cut machine molds (comma-triad, semicolon-reversal, negative-parallelism, suspended question).
- Headings: full-sentence claims are house style; break any negative-closer ("No X travels without Y") or comma-and heading and any shape reused from neighbors (hallucination-rate, perplexity, truthfulqa).
- Catchphrase/self-grading tells and decorative "underscoring/highlighting" verbs: cut.
- Press voice: the takeaway must not restate the finding as a verdict block; body addresses no one.

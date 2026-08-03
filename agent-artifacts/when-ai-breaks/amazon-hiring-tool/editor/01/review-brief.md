# review-brief: when-ai-breaks/amazon-hiring-tool (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writer/01/brief.md — exact writer brief (instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/researcher/02/evidence.md — CURRENT evidence (round 02; source [6] is now an archived EEOC copy). researcher/01 is superseded for [6] only.
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writer/01/draft-handoff.md
- Article: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/library/when-ai-breaks/amazon-hiring-tool.html
- Template context dir: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/editor/01/editorial-review.md

Recent-pattern notes (this series): break the "in about N hours/weeks" duration
headline mold and comma-triad / semicolon-reversal deks. Check headline, dek,
headings.

This round's focus:
- FURNITURE ALERT: the body carries a `nb-note nb-note-strong` block labeled
  "Verdict" (around line 204). `press/editorial.md` names a "Verdict note" as a
  banned retired-template leftover — the takeaway bookend is where a lesson lands
  its judgment, and no body block may restate the finding. Judge this block hard:
  if it restates the finding or duplicates the takeaway's job, CUT it (furniture
  removal is within your authority). Keep it only if it does real, non-restating
  work no other element does — and be skeptical that it clears that bar.
- Single-origin sourcing must stay VISIBLE: every Amazon-incident specific
  (~500 models, 1–5 stars, the "women's" penalty, the two colleges, disbandment)
  rests on one 2018 Reuters investigation citing five anonymous people. Confirm
  attribution is in-clause, not laundered into fact.
- The Reuters-vs-Amazon contradiction (sources say recruiters "looked at the
  recommendations"; Amazon says "never used to evaluate candidates") must be
  carried and weighed, landing on the bounded-harm point both share — NOT
  resolved beyond the record. Confirm no claim implies the tool rejected
  applicants at scale.
- Do not accept the later-retelling embellishments the evidence flags as
  unsupported (no team headcount, no Edinburgh location) or the "83%/99%"
  marketing prevalence stats. "Lives today" should rest on EEOC four-fifths,
  NYC Local Law 144, and the 2024 UW study.
- Source [6] is now `web.archive.org/.../eeoc.gov/...select-issues...` — an
  archived capture of the EEOC's own page (eeoc.gov bot-gates the canonical URL
  with a 404). Confirm the data-nb-note is factual and the data-nb-kind
  (primary) is defensible for an archived copy of the agency's own document.
  You do not need to re-open eeoc.gov (it is bot-gated); the archived text was
  verified firsthand in researcher/02.
- Byline reads "8 min read"; nb-meta reading_minutes is 8 — confirm they match.
  If you make cuts, run ./nb stamp; if reading_minutes changes, flag that the
  byline must be reset to match (orchestrator will gate it before PR).

# writer brief: when-ai-breaks/chatgpt-defamation (01)

Inputs:
- editorial-direction.md (house standard, slop/headline rules, press voice, lesson identity, The When AI Breaks prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; read before drafting)
- researcher/01/evidence.md (the complete claim set; use its Numbers section exactly; address its Contradictions)
- commission.md (assignment, boundaries, original-contribution target)
- the initialized article at library/when-ai-breaks/chatgpt-defamation.html (edit in place; keep chrome exact)
- effective template contract and furniture catalogs under .nb-context/

Output: writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build):
  ./nb stamp .nb-work/when-ai-breaks/chatgpt-defamation/library/when-ai-breaks/chatgpt-defamation.html
  ./nb check --series when-ai-breaks --library /home/user/library-checkout .nb-work/when-ai-breaks/chatgpt-defamation/library/when-ai-breaks/chatgpt-defamation.html
(iterate with --no-check-links; final proof with links, to BLOCK: 0)

This round's focus (from the researcher's report; detail and Contradictions in the evidence file):
- The central guardrail: Walters v. OpenAI leaves civil liability UNSETTLED and largely
  UNTESTED. It is a trial-level Georgia state summary-judgment order (Judge Tracie Cason,
  Gwinnett County, May 19 2025) that OpenAI's counsel drafted and the court adopted "as
  edited," resting on three fact-specific grounds: a sophisticated user (journalist Fred
  Riehl) who never believed the output, no actual damages claimed, and no retraction
  requested. Do NOT frame it as "AI beats defamation" or as settling the question in
  OpenAI's favor. Turley never sued; Hood never filed (dropped Feb 2024 after OpenAI
  filtered the outputs, per secondary sourcing); the 2025 Holmen matter is a GDPR complaint,
  not defamation. Say the doctrine is open and mostly untested.
- A filed amicus (NYU/UGA clinics) and named scholars (Volokh, Andersen Jones) argue against
  the court's disclaimer reasoning. Steelman that side where you report the ruling.
- Label OpenAI's counsel victory statement and the Terms-of-Use disclaimer as
  primary-to-OpenAI (interested). No direct OpenAI corporate quote is available; do not
  invent one.
- Keep fact, allegation, and holding visibly distinct throughout. Sober, exact, no lurid
  detail; convey the named people's harm in concrete facts, not heightened ones.
- The Walters primary documents are cited at their publicly resolvable homes (Reason,
  CourthouseNews, MLRC, UGA First Amendment Clinic) because the court e-filing portal is
  gated. Hood and the Turci/Turley WaPo detail rest partly on secondary; attribute as the
  record does.
- Link, do not re-teach: the-mechanics/hallucination for the confabulation mechanism. Spend
  the lesson on the defamation-of-a-named-person angle and the liability question, which the
  hallucination-citation pieces (mata, deloitte, air-canada) did not cover.

Recent library shapes to break (keep required content):
- Dek: avoid the two-clause "claim, and/so the twist" mold and the comma-triad; do not copy
  the air-canada/mata "when X did Y, a judge/tribunal did Z" dek shape.
- Closing body heading: when-ai-breaks pieces close on a "the same setup is running right now"
  heading (air-canada). Keep the where-it-lives-today content; build the heading differently.
- Orientation heading is its own concrete step, not a paraphrase of the headline.
- Furniture: nb-note and nb-stat-strip recur by reflex; a defamation piece may not need a stat
  strip at all. Use only what the material calls for.

nb-meta: harness "claude-code"; model = the model you are actually running as (report it).
No charts or source assets unless the evidence record names an exact visual the argument spends.

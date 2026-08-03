# writer brief: when-ai-breaks/amazon-hiring-tool (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/commission.md — assignment, angle, boundaries
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writing-coach/01/voice-guide.md — register and licensed forms
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/researcher/01/evidence.md — the complete claim set; use its Numbers exactly
- Article to edit: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/library/when-ai-breaks/amazon-hiring-tool.html
- Template context dir: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writer/01/draft-handoff.md

Proof: run from repo root /home/user/the-nightly-build using the checkout's nb.
  Iterate: ./nb check --series when-ai-breaks .nb-work/when-ai-breaks/amazon-hiring-tool/library/when-ai-breaks/amazon-hiring-tool.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout --no-check-links
  Final (BLOCK: 0, links included): same without --no-check-links. Run ./nb stamp before the final check.

This round's focus (decisions the inputs do not fully carry):
- Single-origin sourcing is central and must be VISIBLE in the prose. Every
  Amazon-incident specific (~500 models, 1–5 stars, the "women's" penalty, the
  two all-women's colleges, disbandment) traces to one 2018 Reuters
  investigation citing five anonymous people. Attribute it as such in the text;
  do not launder it into unattributed fact.
- Carry the genuine contradiction the evidence records: Reuters' sources say
  recruiters "looked at the recommendations"; Amazon says the tool was "never
  used to evaluate candidates." Weigh it in the prose; do not resolve it beyond
  what the record supports.
- Bounded harm: the tool was experimental and never the sole screen. Do NOT
  write or imply it rejected real applicants at scale. Say exactly what the
  record supports.
- Do NOT use the later-retelling embellishments the evidence flags as
  unsupported by the origin (no team headcount, no Edinburgh location). Do NOT
  use the "83%/99%" prevalence marketing figures. For "the weakness lives
  today," lean on the primaries: EEOC four-fifths guidance, NYC Local Law 144,
  and the 2024 UW resume-screening study (white-associated names 85% vs 9%;
  male-associated 52% vs 11%).
- The proxy / redundant-encoding mechanism is owned by Barocas & Selbst 2016 and
  Dwork et al. 2012 — cite those as the mechanism's primaries. Teach the term
  only after its concrete stand-in (a word, a verb, a college) is on the page,
  per the voice guide.
- Neighboring library lessons may be LINKED, not re-taught: the reader can be
  sent to ai-in-the-world/nyc-hiring-bias-audits for the regulatory response and
  to the-mechanics pieces on training if useful. Keep COMPAS and the Dutch/UK
  public-sector cases walled off — do not blur this hiring case into them.
- Headline/dek: avoid this series' "in about N hours/weeks" duration mold and
  the comma-triad / semicolon-reversal dek. A number-led headline is fine only
  if the number is truly this story's and single-origin-safe.
- nb-meta: date 2026-08-03, harness, writer model you ran as; tags array empty.

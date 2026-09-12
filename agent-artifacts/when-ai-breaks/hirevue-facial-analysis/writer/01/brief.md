# writer brief: when-ai-breaks/hirevue-facial-analysis (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writing-coach/01/voice-guide.md (how this piece should sound)
- ../../researcher/01/evidence.md       (the complete claim set; do not exceed it)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/when-ai-breaks/hirevue-facial-analysis/library/when-ai-breaks/hirevue-facial-analysis.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/when-ai-breaks/hirevue-facial-analysis/.nb-context/

Output: ./draft-handoff.md

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then
full including links until BLOCK: 0):
  ./nb check .nb-work/when-ai-breaks/hirevue-facial-analysis/library/when-ai-breaks/hirevue-facial-analysis.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/f68f1d9c-d5c2-58e1-960b-5ffb60cad58d/scratchpad/library-checkout
Run `nb stamp` before the final check.

This round's focus and decisions the inputs do not carry:
- Attribute the "scientifically baseless" judgment to the independent science
  (Barrett et al.) and to EPIC, never as a HireVue admission. HireVue never
  conceded invalidity or bias; it framed the 2020/2021 removal as a proactive value
  decision (its language analysis had improved and the visual signal "no longer
  significantly added value"). Report the company's framing as its framing.
- Present the facial-analysis weighting as a dated, unresolved conflict: 2019
  executives put it at 10-30% of a score (or up to 29% for facial action units);
  HireVue in 2021 said the visual signal added about 0.25% (up to 4%) of predictive
  power. These may not measure the same thing. Give both with dates; never say
  facial analysis "determined" outcomes.
- Keep the two deployment-scale figures dated and separate: 2019 (EPIC: 100+
  companies, 1M+ applicants) and 2021 (HireVue: 700+ customers, 18M+ interviews).
  Do not merge them.
- Be exact on the science: Barrett et al. refutes reliable inference of emotion
  from facial configurations; HireVue claimed to infer traits and job competence, a
  further step, so the review removes the precondition rather than running a
  job-performance study. Say it that way.
- The ORCAA audit does not support HireVue's broad validity claim: it examined one
  early-career assessment, did not evaluate the tool's technical design, sits behind
  an NDA, and did not test construct validity. Do not let it stand for more.
- There is no public FTC enforcement outcome in the record; the record supports
  only that HireVue removed visual analysis, not that the FTC ordered it. Do not
  imply an order. Cite the Illinois statute as 820 ILCS 42 / Public Act 101-0260.
- Link amazon-hiring-tool, workday-hiring-screening, and itutorgroup-age-
  discrimination in Background; the distinct contribution here is invalid
  measurement, not training-data bias, so do not re-run their angle. No
  possessive-actor-verb-object headline reflex, no negative parallelism in
  headline/dek, no "Today's..." closer. Fill `nb-meta` harness "Claude Code",
  model "claude-opus-4-8". Handle a sensitive accountability story soberly, from the
  record, with no outrage.

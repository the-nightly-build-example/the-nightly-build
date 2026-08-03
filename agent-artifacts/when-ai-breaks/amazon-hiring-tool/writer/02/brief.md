# writer brief: when-ai-breaks/amazon-hiring-tool (02) — single-source URL swap

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writer/01/draft-handoff.md — your prior handoff; the draft is otherwise BLOCK 0 (no-check-links) and clean
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/researcher/02/evidence.md — the updated evidence; source [6] now carries a resolving archived URL
- Article to edit: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/library/when-ai-breaks/amazon-hiring-tool.html
- Template context dir: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/writer/02/draft-handoff.md

Proof: run from repo root /home/user/the-nightly-build.
  Final (BLOCK: 0, links included): ./nb check --series when-ai-breaks .nb-work/when-ai-breaks/amazon-hiring-tool/library/when-ai-breaks/amazon-hiring-tool.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout
  Run ./nb stamp before the final check.

The ONLY change this round:
- Update source [6]'s href (the EEOC "Select Issues: Assessing Adverse Impact in
  Software, Algorithms, and Artificial Intelligence..." guidance) to the
  resolving archived address recorded in researcher/02/evidence.md:
  https://web.archive.org/web/20250125163154/https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial
  Keep its data-nb-kind and the anchor/publisher text as they were (it is the
  EEOC's own document; an archived copy of a primary). If a data-nb-note is
  warranted, keep it factual and short per the evidence record. Do not touch any
  other source, any prose, the byline, or nb-meta counts beyond what stamp
  recomputes.
- Confirm the byline already reads the real "N min read" figure (not the literal
  placeholder). If it still shows "N min read", set it to match nb-meta
  reading_minutes.

Then stamp and run the links-included proof to BLOCK: 0. The archived host may
return 403/restricted or be unreachable from this session's egress; neither is a
404/410, so it must not block. If the proof still blocks on [6], stop and report
the exact code — do not swap in a different URL on your own.

Update draft-handoff (02): one line confirming the [6] swap and the final proof
result. Everything else in writer/01 stands.

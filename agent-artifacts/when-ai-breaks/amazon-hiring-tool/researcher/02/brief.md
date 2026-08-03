# researcher brief: when-ai-breaks/amazon-hiring-tool (02) — single-source URL repair

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/researcher/01/evidence.md — your prior evidence record; preserve all still-valid work
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/editorial-direction.md — citation standard

Output: /home/user/the-nightly-build/.nb-work/when-ai-breaks/amazon-hiring-tool/agent-artifacts/when-ai-breaks/amazon-hiring-tool/researcher/02/evidence.md
(a complete new evidence.md preserving still-valid entries and recording the one fix)

The one fix — nothing else changes:
Source [6], the EEOC "Select Issues: Assessing Adverse Impact in Software,
Algorithms, and Artificial Intelligence Used in Employment Selection Procedures
Under Title VII of the Civil Rights Act of 1964" (technical assistance, May
2023), currently prints the eeoc.gov URL. That URL hard-404s to an automated
fetch, and the deterministic proof (`nb check --check-links`) BLOCKS on a 404.
Confirmed here: eeoc.gov bot-gates its entire /laws/guidance/ and /newsroom/
tree — even the live 2022 ADA/AI guidance and the 2023 press release return 404
to a bot — so NO eeoc.gov address will pass the link check. The proof does NOT
block on 403/paywall/restricted or on a slow/unreachable host; it blocks only on
404/410 or a domain that does not resolve.

Supply ONE link-resolvable address for this identical, already-verified document
and record it as source [6]'s address, with the reason noted:
- Preferred: a web.archive.org (Wayback Machine) snapshot of the exact EEOC
  document. Verify the snapshot shows the correct guidance (the four-fifths /
  adverse-impact discussion you already read), and confirm the snapshot URL does
  NOT return 404/410 to an automated fetch (a 403/restricted or a 200 is fine —
  both are non-blocking; a 404 is not). Record it deliberately as an archived
  copy of the EEOC primary, with a one-line reason (eeoc.gov bot-gates the
  original with a 404).
- Acceptable alternative only if no working Wayback snapshot exists: a different
  address on a domain that returns non-404 and hosts the same EEOC document
  verbatim, classified honestly (an archived/hosted copy of a primary is still
  reporting the EEOC's own text; keep the Kind/《why》 precise).

Do NOT invent an eeoc.gov `/sites/default/files/` PDF path, and do NOT relabel a
third-party advocacy mirror as the government primary. Keep the source count at
or above the series floor of 8 (>=4 primary, >=1 secondary). Everything else in
researcher/01 stands unchanged — copy it forward faithfully and change only the
[6] address (and its locator/note if needed).

Report: the new evidence path, the exact replacement URL for [6], its verified
fetch status (the code an automated GET returns), and confirmation it shows the
right document.

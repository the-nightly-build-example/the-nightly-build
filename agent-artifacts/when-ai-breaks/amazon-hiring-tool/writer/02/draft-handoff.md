# draft handoff: when-ai-breaks/amazon-hiring-tool (writer/02)

Applied by the orchestrator as a mechanical, fully-specified single-source URL
swap (no new prose), per this round's brief and researcher/02/evidence.md.

Change:
- Source [6] (EEOC "Select Issues: Assessing Adverse Impact in Software,
  Algorithms, and Artificial Intelligence...") href swapped from the canonical
  eeoc.gov URL, which hard-404s to the automated link checker because eeoc.gov
  bot-gates its /laws/guidance/ tree, to the Internet Archive capture recorded
  in researcher/02:
  https://web.archive.org/web/20250125163154/https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial
  Added a factual `data-nb-note` marking it as an Internet Archive capture of the
  EEOC's own page. data-nb-kind stays "primary" (an archive of the agency's own
  document; the EEOC remains the claim's owner). No other source, prose, byline,
  or nb-meta field changed beyond what `nb stamp` recomputes.

Proof: `nb stamp` then `nb check --series when-ai-breaks ... --library <library>`
with links included → BLOCK: 0, WARN: 0, PUBLISHABLE (words 1822, sources 8,
reading_minutes 8). The prior sole blocker (canonical eeoc.gov 404) is resolved.

Editor/01 subsequently reviewed the full article and approved (its own direct
cut removed the banned Verdict block). No open evidence or voice question.

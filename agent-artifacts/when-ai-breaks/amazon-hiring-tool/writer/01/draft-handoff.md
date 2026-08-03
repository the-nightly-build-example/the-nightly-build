# Draft handoff: when-ai-breaks/amazon-hiring-tool (writer 01)

## Original work (one sentence)
This lesson pulls apart the two things the Amazon story is usually told as
one — the single, anonymously sourced 2018 Reuters incident and the mechanism
behind it — and shows on the page that the teaching survives even if every
Reuters-sourced specific were wrong, because Barocas & Selbst (2016), Dwork et
al. (2012), and the 2024 University of Washington screening study establish the
same failure without leaning on Reuters at all.

That act is visible in the "What holds up / What to be careful about" grid and
its Verdict in the second section, and in the takeaway's closing line ("The
Amazon story may rest on five people. The lesson does not rest on them at all.").

## Proof status
NOT at BLOCK: 0. One blocker stands, and it is a source-URL/evidence problem, not
a prose or structure problem.

- `nb check ... --no-check-links`  → **BLOCK: 0, WARN: 0** (clean).
- `nb stamp` run before the final check: words 1860, sources 8, reading_minutes 8.
- Final `nb check` **with links** → **BLOCK: 1**:
  - `B-SOURCE-DEAD  https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial`

This is source [6], the EEOC's 2023 Title VII AI technical assistance — one of
the three "weakness lives today" primaries the brief names (EEOC four-fifths,
NYC Local Law 144, UW 2024 study).

### Why it blocks and what I ruled out
- The researcher's evidence entry already flags this: the canonical page
  "returns HTTP 404 to automated fetch (bot-gated), text verified from the
  EEOC-hosted PDF." The evidence record supplies **no resolving URL** for that PDF.
- I verified the 404 is a hard 404, not user-agent gating: `curl` returns 404
  under both a default and a full desktop-Chrome UA, while `eeoc.gov/` root
  returns 200. So the link checker will always trip on this path.
- I searched for an EEOC-hosted resolving copy: the EEOC publications page links
  only the same bot-gated canonical URL; the EEOC newsroom release for the
  guidance also 404s; web search surfaces the document only as third-party
  mirrors (data.aclum.org, naacpldf.org) and one unrelated EEOC one-pager
  ("What is the EEOC's role in AI?", which does not contain the four-fifths
  worked example or the vendor-liability Q&A the article cites).
- I did **not** invent a `/sites/default/files/` PDF path, and I did **not**
  swap in an advocacy-org mirror for a government primary — either would be a
  fabricated or unvetted citation, and re-hosting an EEOC primary on an advocacy
  domain while labeling it `data-nb-kind="primary"` would misrepresent it. Both
  are sourcing decisions above the writer's authority.
- I did not route around the hole by dropping the EEOC citation: it is a
  brief-required primary, and removing it would also drop the source count from
  8 to 7, below the series minimum of 8 (primary ≥ 4).

### What is needed, and its owner
**Owner: researcher / orchestrator.** Supply a link-resolvable URL for the EEOC
"Select Issues: Assessing Adverse Impact..." guidance — either the exact
`eeoc.gov` PDF the researcher read (confirmed to return 200 to automated fetch),
or explicit authorization to cite a specific archived/mirror copy for source
[6]. With that one URL swapped into `#s6`, the final links-included proof should
reach BLOCK: 0; nothing else is outstanding. Every other source resolved,
including the Reuters origin (HTTP 401, gated, correctly non-blocking).

## Open evidence / voice questions
- **Contradiction, carried not resolved (as instructed):** the piece states both
  Reuters' sources ("recruiters looked at the recommendations ... but never
  relied solely") and Amazon's later position ("never used ... to evaluate
  candidates"), and lands only on the point both share (the ratings were never
  the sole basis for a hire; the tool was experimental). Confirm the editor is
  content that the two are left in tension rather than reconciled.
- **Single-origin attribution** is kept visible in the prose throughout, plus the
  holds-up grid and Verdict note; the headline states Reuters' reported finding
  and the dek immediately names its evidentiary basis (one 2018 Reuters
  investigation, five anonymous sources).
- **Furniture:** holds-up grid + Verdict (single-origin landing), a "Redundant
  encoding" definition note, and one chart (Fig. 1) rebuilt honestly from the UW
  study's reported percentages (85 / 9 / 52 / 11), with `chart-1.py` committed
  beside the article as provenance. No source asset was captured — the Reuters
  origin carries no internal figure, and the EEOC four-fifths example is rendered
  as prose numbers rather than a lifted image.
- **Excluded per brief:** no team headcount, no Edinburgh location, no 83%/99%
  prevalence figures. Neighboring COMPAS/Dutch/UK lessons are kept walled off;
  nyc-hiring-bias-audits is linked in prose (not as a numbered source) and in the
  Background band.

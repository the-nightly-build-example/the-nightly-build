# writer brief: what-could-go-wrong/lethal-trifecta (01)

Inputs:
- editorial-direction.md (house standard, slop/headline rules, press voice, lesson identity, The What Could Go Wrong prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; read before drafting)
- researcher/01/evidence.md (the complete claim set; use its Numbers section exactly; address its Contradictions)
- commission.md (assignment, boundaries, original-contribution target)
- the initialized article at library/what-could-go-wrong/lethal-trifecta.html (edit in place; keep chrome exact)
- effective template contract and furniture catalogs under .nb-context/

Output: writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build):
  ./nb stamp .nb-work/what-could-go-wrong/lethal-trifecta/library/what-could-go-wrong/lethal-trifecta.html
  ./nb check --series what-could-go-wrong --library /home/user/library-checkout .nb-work/what-could-go-wrong/lethal-trifecta/library/what-could-go-wrong/lethal-trifecta.html
(iterate with --no-check-links; final proof with links, to BLOCK: 0)

This round's focus (from the researcher's report; detail and Contradictions in the evidence file):
- Draw the demonstrated-vs-speculative line cleanly, the move the desk asks for. The four 2025
  disclosures against shipped products (Microsoft 365 Copilot / EchoLeak, CVE-2025-32711;
  GitLab Duo; GitHub's MCP server; ChatGPT connectors / "AgentFlayer") each show real
  private-data exfiltration via injected text, but all four are researcher proof-of-concept,
  NONE reported exploited in the wild, and Microsoft's CVE marks exploit code "unproven."
  State that plainly. The leap from demonstrated exfiltration to "autonomous agent
  catastrophe" has no demonstrated basis; name that as the speculative end.
- Be honest about the one gap: there is no measured figure for how common the vulnerable
  three-leg configuration is; the worry rests on vendors shipping it on by default. Do not
  imply a prevalence number the evidence does not have.
- Willison's June 2025 post is the origin of the "lethal trifecta" framing; cite it as that.
  Aim Labs' own EchoLeak writeup was unreachable (Cloudflare 403); the EchoLeak facts come
  from Microsoft's CVE record plus Willison quoting Aim, so do not attribute Aim's exact
  "LLM Scope Violation" phrasing as if read firsthand.
- Link, do not re-teach: the-mechanics/instructions-are-data (why a model cannot separate
  instructions from data) and what-could-go-wrong/jailbreaks. This lesson owns a different
  failure surface: a deployed agent exfiltrating private data via injected instructions at
  inference time. Do NOT drift into "the model wants to betray you"; this is a security
  argument, not an alignment one.
- Name no company as an authority. No working injection payloads or reproducible exploit
  recipe; explain the threat model and the mitigation (deny one leg of the trifecta), not a
  how-to.

Recent library shapes to break (keep required content):
- Dek: avoid the two-clause "claim, and/so the twist" mold (recent wcgw deks lean on the
  comma-and twist), the comma-triad, and the "The [thing] that..." opener.
- Closing body heading: recent wcgw pieces close on a "the confidence outruns the proof"
  verdict heading ("The doom and the dismissal both outrun the evidence"). Keep the
  present/gap content; build the heading differently.
- Orientation heading is its own concrete step, not a paraphrase of the headline.
- Furniture: a holds-up grid (nb-holdsup) or position card fits a for/against argument if the
  material wants it; nb-note and nb-stat-strip recur by reflex. Earn each; do not stack blocks.

nb-meta: harness "claude-code"; model = the model you are actually running as (report it).
No charts or source assets unless the evidence record names an exact visual the argument spends.

# Researcher brief 01 — what-could-go-wrong/jailbreaks

Load the `researcher` skill and follow it. This is invocation 01.

## Exact inputs (begin here; do not tour the repo)
- Commission: `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/commission.md` (the assignment, angle, and the required/
  starting source list — read it fully; it names every source obligation).
- Editorial direction: `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/editorial-direction.md` (house + series standards).

## Exact output (write only this)
- `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/researcher/01/evidence.md` — the evidence record, in the skill's
  stable sections (opening paragraph; Sources; Contradictions; Numbers; Source
  assets; Discarded).

## Source policy for this article (what-could-go-wrong)
- Minimum sources and primary/secondary bands are in the commission's "Source
  obligations". Read every REQUIRED primary firsthand. Verify every number against
  the primary that owns it. Classify each source primary/secondary with a reason
  (authorship and stake, not domain). Seek contradictory evidence explicitly.
- You have web access. Confirm every recorded URL resolves; a 403/paywall is
  gated, not dead — try a real browser fetch before giving up. Never record an
  unverified URL. Cite only what you actually opened.

## Tools
- nb executable: `/home/user/the-nightly-build/nb` (run commands with the main checkout as CWD:
  `cd /home/user/the-nightly-build`). Continuity check if useful:
  `/home/user/the-nightly-build/nb history --library /home/user/library-checkout --series what-could-go-wrong --limit 20`.
- Do not read prior articles as background; use `nb history` only for a specific
  continuity question the commission raises.

## Unresolved / owner
If the brief or commission is missing something you need, return
`REQUEST orchestrator <one-sentence need>`. Do not invent sources to hit a count.

Return exactly one line: `DONE researcher .nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/researcher/01/evidence.md`,
or `BLOCKED researcher <reason>`, or `REQUEST orchestrator <need>`.

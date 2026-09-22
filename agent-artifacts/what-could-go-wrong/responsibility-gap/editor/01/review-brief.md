# editor review-brief: what-could-go-wrong/responsibility-gap (01)

Inputs:
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/editorial-direction.md — the standing standards.
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/writing-coach/01/voice-guide.md — read first.
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/commission.md — assignment, boundaries, recent-pattern notes.
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/writer/01/brief.md — the exact writer brief (for leak detection).
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/researcher/01/evidence.md — open when a concern calls for it; it owns every figure and quote.
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/writer/01/draft-handoff.md — the writer's original-work sentence and two flagged items.
- .nb-work/what-could-go-wrong/responsibility-gap/library/what-could-go-wrong/responsibility-gap.html — the drafted article (a table separating legal-held vs fault-named across three cases).
- .nb-work/what-could-go-wrong/responsibility-gap/.nb-context/ — the contract and furniture catalogs.

Output: .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/editor/01/editorial-review.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/what-could-go-wrong/responsibility-gap/library/what-could-go-wrong/responsibility-gap.html --series what-could-go-wrong --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where you need a fact nobody gathered, ask me (the orchestrator) and keep working.

Two items the writer raised — resolve both, hardest on the first:
1. HEADLINE. "So far, a human has answered for every automated-driving death." Test that universal claim against the record. In the 2016 Tesla Williston case the driver (Joshua Brown) died and NTSB assigned cause partly to him and partly to the truck driver, who was not charged — so did a human "answer" for that death in the accountability sense the piece means? If the record does not support "every," the headline overclaims and is yours to fix (rewrite it to what the record supports — e.g. scope it to the cases where someone was actually held, or reframe around the supervised-vs-autonomous line). The headline is the article's largest claim; do not approve an unsupported one. Reread it last, as the skill directs.
2. Two facts (Uber not criminally charged; the AI Liability Directive withdrawn in 2025) rest on secondary reporting (NPR, IAPP) standing in for documents the researcher could not open. Confirm each is cited to a source classified data-nb-kind="secondary" and phrased as reported, not asserted from a primary the piece does not have. Audit every data-nb-kind: 9 primary / 2 secondary claimed — verify the primaries are the authoring documents (Matthias, Sparrow, the NTSB/NHTSA reports, the court records, the EU instruments, Tigard) and open every citation href as printed.

Watch especially:
- The corrected angle must be intact: the deployed cases are supervised by design (Uber developmental + safety driver; Tesla Level 2 + driver as responsible operator), so they refute the strong "no one can be held" claim only for SUPERVISED systems; the fully-autonomous case must be stated as untested, not quietly treated as refuted. Legal and moral responsibility kept separate (the record closes the legal question more firmly; Tigard concedes the moral gap is less easily resolved). AILD withdrawn; PLD applies only from Dec 2026 and only to "products."
- Fairness: Matthias's and Sparrow's arguments must be stated at full strength in their own words before being tested (recompute the quotes against the record). No company named as an authority.
- The table: verify each row (who was legally held vs the fault the record named) against the record; caption factual; the table earns its place.

Recent-record comparison (formula/leak detection): the desk names originator+year (fine) and closes on a gap sentence (companion-dependency, negative-side-effects) — confirm the closing gap (the untested fully-autonomous case) is in this lesson's own terms, not that mold. Flag any semicolon-reversal or comma-triad dek and any "clause, and clause" heading.

Decide approve or redraft per the skill. Redraft only if the piece needs a different argument; the headline and everything else are yours to fix directly. After any direct edit, re-run nb stamp and the exact nb check above until BLOCK: 0, then write the review. Note whether you left the article at BLOCK: 0, whether a writer round is owed, and how you resolved the headline.

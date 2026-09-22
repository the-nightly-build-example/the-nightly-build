# editor review-brief: when-ai-breaks/iruda-chatbot (01)

Inputs:
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/editorial-direction.md — the standing standards.
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/writing-coach/01/voice-guide.md — read first.
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/commission.md — assignment, boundaries, recent-pattern notes.
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/writer/01/brief.md — the exact writer brief (for leak detection).
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/researcher/01/evidence.md — open when a concern calls for it; it owns every figure.
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/writer/01/draft-handoff.md — the writer's original-work sentence and two open questions.
- .nb-work/when-ai-breaks/iruda-chatbot/library/when-ai-breaks/iruda-chatbot.html — the drafted article (includes a timeline component).
- .nb-work/when-ai-breaks/iruda-chatbot/.nb-context/ — the contract and furniture catalogs.

Output: .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/editor/01/editorial-review.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/iruda-chatbot/library/when-ai-breaks/iruda-chatbot.html --series when-ai-breaks --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where you need a fact nobody gathered, ask me (the orchestrator) and keep working.

Two open items the writer raised — resolve both:
1. Source 9 (the 2025 Seoul Eastern District Court civil judgment) is marked data-nb-kind="primary" but the writer did not open the judgment text; the facts came from koreanbar/fnnews reporting. Audit it per your data-nb-kind duty: open the citation's href as printed. If it lands on the court's own judgment document, primary is defensible by authorship; if it lands on reporting about the judgment, change data-nb-kind to "secondary" and confirm the piece still meets the policy (>=8 sources, >=4 primary, >=1 secondary — the record has other primaries, so a downgrade is safe). Decide it; do not leave it ambiguous.
2. The full article-by-article list of the eight PIPA violations is off the record (the PIPC decision HWP/PDF would not download). The piece says "eight violations" and numbers only Article 28-2(2). That is correct and honest as written; confirm the article does not attach any other article number.

Watch especially, on this piece (correctness first — this is an incident with named people and exact figures):
- Every figure against the record: 9.4 billion messages; the 103.3 million won fine (55.5M penalty surcharge + 47.8M administrative fine), decided 28 April 2021; the class-action award (100k/300k/400k won, 246 plaintiffs, case 2021가합104007, under appeal). Do NOT let "1.033 billion" or "~10 billion" slip in.
- The privacy/enforcement angle is the spine: the eight violations are about data; the hate speech was only the investigation trigger. Confirm the piece keeps that split and does not present the slurs as the punished offense.
- The leakage claim must sit at PIPC's confirmed scope (real names, place names, gender, relationship in the released set; untreated names/phone numbers/addresses in the corpus; Scatter Lab's admitted "bank names"). No surfaced bank-account number may be asserted as an established PIPC finding.
- Hangul and romanization exact (Iruda 이루다 / "Lee Luda", Scatter Lab, "Science of Love" 연애의 과학, PIPC full name). Everyone sees a wrong name in the display text.
- Open every citation href as printed; audit each data-nb-kind (a different outlet retelling is not an independent primary).

Recent-record comparison (formula/leak detection): this desk closes on "where the same weakness lives today / the same flaw wherever X" (chatgpt-data-leak, predpol) — confirm the closer is in this incident's own terms. Flag any comma-triad or semicolon-reversal dek and any "clause, and clause" heading. Keep it distinct from microsoft-tay (linked, not re-run).

Decide approve or redraft per the skill. Redraft only if the piece needs a different argument; everything else is yours to fix directly. After any direct edit, re-run nb stamp and the exact nb check above until BLOCK: 0, then write the review. Note whether you left the article at BLOCK: 0 and whether a writer round is owed.

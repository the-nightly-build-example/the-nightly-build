# writer brief: when-ai-breaks/iruda-chatbot (01)

Inputs:
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/editorial-direction.md
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/commission.md
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/writing-coach/01/voice-guide.md
- .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/researcher/01/evidence.md — the complete claim set; treat it as the only claims available.
- .nb-work/when-ai-breaks/iruda-chatbot/library/when-ai-breaks/iruda-chatbot.html — the article to edit.
- .nb-work/when-ai-breaks/iruda-chatbot/.nb-context/ — the template contract and furniture catalogs. Documented markup only.

Output: .nb-work/when-ai-breaks/iruda-chatbot/agent-artifacts/when-ai-breaks/iruda-chatbot/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/iruda-chatbot/library/when-ai-breaks/iruda-chatbot.html --series when-ai-breaks --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where something you need is missing, ask me (the orchestrator).

Corrections from the evidence you MUST honour (do not use the commission's round numbers where these differ):
- Message count is 9.4 billion (94억여 건, owned by PIPC), NOT "~10 billion."
- The fine is 103.3 million won, decided 28 April 2021 (55.5M penalty surcharge + 47.8M administrative fine). Do not write "1.033 billion" — a secondary mis-stated it; the primary owns 103.3M.
- PIPC found eight PIPA violations, all about data handling; the hate speech was named only as the trigger for the investigation, not a punished violation. That split is the spine of the piece and the one-sentence contribution: the privacy breach, not the slurs, is what the regulator punished, and this was Korea's first data-enforcement action against an AI company.
- Only PIPA Article 28-2(2) is cited by number in the public record. Do NOT attach other article numbers; say "eight violations" and cite 28-2(2) where the record supports it.
- The account-number leakage is a filtered risk category and a plaintiff allegation, NOT a confirmed PIPC finding. Do not assert a surfaced bank-account number as established. PIPC's confirmed exposed categories: real names, place names, gender, relationship status (in the GitHub-released model/data set), plus untreated names, phone numbers and addresses left in the training corpus. Write the leakage exactly at that confirmed scope.
- Class action: Seoul Eastern District Court, tiered award 100k/300k/400k won across 246 plaintiffs, case 2021가합104007, under appeal. Use exactly.
- Names must be exact in Hangul with romanization as the record gives them (Iruda 이루다 / "Lee Luda", Scatter Lab, "Science of Love" 연애의 과학, PIPC full name).

Structure (series form): tell it in order — what Iruda was built to do; what it actually did (both failures); who it affected and what Scatter Lab did (shutdown, apology, class action, PIPC ruling); then why this kind of system fails this way (training a fluency-tuned model directly on real chat logs lets it memorise and surface private strings and inherit toxic text with no safety layer — teach the piece the reader needs); then where the same weakness lives today. Link the-mechanics/memorization and the-mechanics/hallucination only where they help; do not re-teach them.

Boundaries: when-ai-breaks/microsoft-tay is the cousin — link it in Background and keep Iruda's distinct angle (training-data privacy + the regulator's enforcement) as the spine, not a second Tay. Where a figure or cause is disputed, give the strongest account of each side and say what would settle it.

Recent shapes to break: this desk closes on "where the same weakness lives today / the same flaw, wherever X" (chatgpt-data-leak, predpol) — write that closing beat in this incident's own terms. Deks that widen scope in a second sentence are fine only if the second sentence carries a specific fact. Avoid comma-triad and semicolon-reversal deks; vary heading construction, no "clause, and clause" headings.

Process reminder: body first, then both bookends; number sources in first-citation order with correct data-nb-kind (PIPC decision/press, Scatter Lab statements, the court judgment are primary; reporting is secondary — do not label a different outlet's retelling as an independent primary); add data-nb-locator where the record gives one; a timeline component is natural for the ordered incident if the catalog supports it, built only from verified dates; fill nb-meta (date 2026-09-22, harness "Claude Code", model = the model you run as); iterate with --no-check-links, then nb stamp and the exact nb check above until BLOCK: 0; put your one-sentence original-work statement in draft-handoff.md.

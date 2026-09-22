# editor review-brief: the-mechanics/answer-length-bias (01)

Inputs:
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/editorial-direction.md — the standing standards.
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/writing-coach/01/voice-guide.md — read first.
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/commission.md — the assignment, boundaries, and recent-pattern notes.
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/writer/01/brief.md — the exact writer brief (for leak detection).
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/researcher/01/evidence.md — open when a concern calls for it.
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/writer/01/draft-handoff.md — the writer's original-work sentence and notes.
- .nb-work/the-mechanics/answer-length-bias/library/the-mechanics/answer-length-bias.html — the drafted article.
- .nb-work/the-mechanics/answer-length-bias/.nb-context/ — the contract and furniture catalogs.

Output: .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/editor/01/editorial-review.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-mechanics/answer-length-bias/library/the-mechanics/answer-length-bias.html --series the-mechanics --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where you need a fact nobody gathered, ask me (the orchestrator) and keep working.

Watch especially, on this piece:
- The single hardest correctness point: the measured length-share fractions (2.0/27.2/53.4% non-length; ~98/73/47% length; correlations 0.72/0.55/0.67) are Llama-7B LoRA measurements scored by a GPT-4 simulator. The article must NOT present them as figures for frontier assistants, and must say no source decomposes a frontier model. Verify the piece keeps that scope in the prose, not only in a caption.
- The honest framing is that RLHF amplifies a real, modest human preference (62%, AlpacaFarm) — not that length is purely spurious. Check the piece does not overclaim spuriousness. Confirm the setting-specific qualifier (Stack: over half the gain is not length; harmlessness reward model negative correlation) survived.
- The length-vs-thoroughness question is genuinely open; confirm it is presented as open, not resolved.
- Confirm the-mechanics/length-control is distinguished (default pull toward length vs hitting a target count) and linked, not re-covered; and that taught RLHF lessons are plain-prose links, not numbered sources.

Recent-record comparison (for formula/leak detection — the piece must not repeat these): recent mechanics deks lean on "the cause sits one level below the answer"; recent closers are literally named like "What the builders haven't settled" (false-premise-questions). Recent outlines used table-of-examples layouts. Flag any heading/dek/closer that echoes the recent record, and any "clause, and clause" heading.

Decide approve or redraft per the skill. Redraft only if the piece needs a different argument. Everything else — including sentences that merely read flat or hard — is yours to fix directly (rewrite, recast, retitle, narrow a claim to the record, adjust furniture). After any direct edit, re-run nb stamp and the exact nb check above yourself until BLOCK: 0, then write the review. Note in the review whether you left the article at BLOCK: 0 and whether a writer round is owed (only if new prose is needed for a failing proof).

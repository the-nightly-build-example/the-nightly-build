# writer brief: the-mechanics/answer-length-bias (01)

Inputs:
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/editorial-direction.md
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/commission.md
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/writing-coach/01/voice-guide.md
- .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/researcher/01/evidence.md — the complete claim set; treat it as the only claims available.
- .nb-work/the-mechanics/answer-length-bias/library/the-mechanics/answer-length-bias.html — the article to edit.
- .nb-work/the-mechanics/answer-length-bias/.nb-context/ — the template contract and furniture catalogs. Documented markup only.

Output: .nb-work/the-mechanics/answer-length-bias/agent-artifacts/the-mechanics/answer-length-bias/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-mechanics/answer-length-bias/library/the-mechanics/answer-length-bias.html --series the-mechanics --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where something you need is missing, ask me (the orchestrator).

This round's focus and hard constraints from the evidence:
- The measured length-share fractions (non-length share of PPO reward gain 2.0% / 27.2% / 53.4%; correlations 0.72 / 0.55 / 0.67; length-only reward winning 56/59/64%) are measured on Llama-7B LoRA models on three open datasets, scored by a GPT-4 simulator that itself favours length. Do NOT present these as figures for GPT-4/GPT-5/Claude-class assistants. Tie the mechanism to today's chatbots by mechanism, and say plainly that no source decomposes a frontier assistant into length vs non-length.
- The honest claim is that RLHF amplifies a modest but real human preference (humans pick the longer answer 62% of the time, AlpacaFarm) into a dominant one — not that length is purely spurious. State that 62% figure and its source.
- Length dominance is setting-specific: on technical QA (Stack) over half the reward gain is not length, and a harmlessness reward model shows a negative length correlation. Include this; it is the fair qualifier, not a hedge.
- The length-itself-vs-thoroughness question is genuinely open in every source. That is your open-question ground; name it as this lesson's own, not with the stock label "What the builders haven't settled."
- Good concrete instance to open on: Singhal's "Why don't adults roll off the bed?" answered in 59 tokens by the SFT model and 243 by the RLHF model. Use the record's exact numbers.
- The AlpacaEval verbosity swing (win rate 22.9%-64.3% on verbosity prompts alone) and length-controlled AlpacaEval raising Arena correlation 0.94->0.98 are strong, primary support that evaluators reward length — use them, from the record.

Boundaries (from commission): RLHF, reward models and PPO are taught — link the-evidence/instructgpt, the-evidence/deep-rl-from-human-preferences, the-evidence/proximal-policy-optimization in Background and use plain prose links at first mention, not numbered sources. Do NOT re-cover the-mechanics/length-control (hitting a target word count); distinguish it explicitly and link it. Do not drift into sycophancy or hedging.

Recent shapes on this desk to break: recent mechanics deks lean on "the cause sits one level below the answer" (do not reuse); recent pieces close on a section literally named like "What the builders haven't settled" (false-premise-questions) — mark settled vs open but name that section for this lesson's content. Vary heading construction; no "clause, and clause" headings. Outline the reasoning before naming sections.

Process reminder: body first, then both bookends; number sources in first-citation order with correct data-nb-kind; reach for a table/figure only where it shows something faster than prose and only from the supplied catalogs (a reward-vs-length plot or a small SFT-vs-RLHF token-count table are natural, built only from the record's verified numbers); fill nb-meta (date 2026-09-22, harness "Claude Code", model = the model you run as); iterate with --no-check-links, then nb stamp and the exact nb check above until BLOCK: 0; put your one-sentence original-work statement in draft-handoff.md.

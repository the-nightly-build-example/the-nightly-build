# writer brief: what-could-go-wrong/ai-control (01)

Inputs:
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/editorial-direction.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/commission.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/writing-coach/01/voice-guide.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/researcher/01/evidence.md
- Article to edit: .nb-work/what-could-go-wrong/ai-control/library/what-could-go-wrong/ai-control.html
- Template context dir: .nb-work/what-could-go-wrong/ai-control/.nb-context/

Output:
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/writer/01/draft-handoff.md

Proof:
- ./nb stamp .nb-work/what-could-go-wrong/ai-control/library/what-could-go-wrong/ai-control.html
- ./nb check .nb-work/what-could-go-wrong/ai-control/library/what-could-go-wrong/ai-control.html --series what-could-go-wrong --library /home/user/library-checkout
  (iterate --no-check-links; final proof with links, to BLOCK: 0)

nb-meta: harness="Claude Code", model="claude-opus-4-8". Tags e.g. ai-control, ai-safety, scheming, control-evaluations, redwood-research.

This round's focus: open the control argument at full strength (safety from an untrusted model via protocols, measured by a control evaluation where a red team builds the model to subvert), report the original APPS experiment concretely, then test it against what the experiments show and name where confidence outruns proof.

Numbers discipline (use the evidence record's Numbers section exactly; every figure carries its setup and audit budget):
- Original APPS results at 2% audit over 5,000 problems: trusted editing 92% safety / 94% usefulness; trusted monitoring 62% / 97%; untrusted monitoring 79% / 96%; baselines 100%/2% and 15%/100%.
- Agentic (Ctrl-Z, BashBench, 1% audit): 58% → 7% figure per the record.
- These four papers' numbers are NOT comparable to each other (different tasks, models, audit budgets); do not put them in one ranking.

Refinement to carry (from the evidence record): the skeptical half arrives earlier than "once models are superhuman." Control degrades badly even at human-level settings: Control Tax finds no robust worst-case safety at realistic low audit budgets (<=5%) even with the best monitors (monitor AUC ~0.92-0.96), and an adaptive prompt-injection attack drove a backdoor-discriminating monitor to a suspiciousness score of 0 on all 375 injected samples, collapsing the safety-usefulness frontier to plain upfront auditing. Present the proponents' own stated limits from their own words. The "control tax" has no single headline dollar figure — do not invent one.

Link neighbors in Background where useful (deceptive-alignment as the threat control assumes; cot-monitorability; scalable-oversight; ai-boxing) — all exist in the library. Do not restate them.

Habits not to inherit (from commission): do not copy recurring wcgw dek phrasings ("None has yet", "feasible on paper and unshown", "so far only in simulation"); avoid comma-triad and negative-parallelism deks; vary heading construction; do not reproduce the "full strength / opposite mistake / what studies can and cannot show" heading set.

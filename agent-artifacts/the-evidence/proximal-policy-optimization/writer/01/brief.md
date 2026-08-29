# writer brief: the-evidence/proximal-policy-optimization (01)

All paths are relative to the repo root /home/user/the-nightly-build.
Let AR = .nb-work/the-evidence/proximal-policy-optimization/agent-artifacts/the-evidence/proximal-policy-optimization

Inputs:
- $AR/editorial-direction.md — house standard, paper voice, series prompt, template identity, furniture
- $AR/writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting and before every revision
- $AR/researcher/01/evidence.md — the complete claim set available to you
- $AR/commission.md — subject, angle, the distinct contribution to make visible
- Article to edit: .nb-work/the-evidence/proximal-policy-optimization/library/the-evidence/proximal-policy-optimization.html (initialized from the lesson template)
- Template contract and furniture catalogs: .nb-work/the-evidence/proximal-policy-optimization/.nb-context/

Output: $AR/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/proximal-policy-optimization/library/the-evidence/proximal-policy-optimization.html --series the-evidence --library /home/user/library-checkout
(run from /home/user/the-nightly-build; use --no-check-links while iterating, then the full command with links to BLOCK: 0)

Recent habits on this desk to break (do not inherit):
- Dek mold "The <year> <org> paper that <did X> reported <limitation> only <where>" has run repeatedly (lora, seq2seq, clip, rag). Write a different dek build.
- Recent lessons close on a present-tense "how it's used today" section titled to that mold. The present-day turn (PPO now, DPO/GRPO) is required content, but title the section for this piece's own particulars.
- nb-note + one nb-table is the reflex furniture. The clipped surrogate objective likely wants an equation (nb-math); use furniture only where it changes understanding.

This round's focus: teach the clipped objective with one concrete worked example a
newcomer can follow, keep the scale of the paper's actual experiments honest
(2017 RL benchmarks, not language models), and make the distinct contribution
visible — the gap between what the paper proved and what the field now trusts PPO
for was bridged by later work. Link the published RLHF lessons in Background
rather than re-teaching them.

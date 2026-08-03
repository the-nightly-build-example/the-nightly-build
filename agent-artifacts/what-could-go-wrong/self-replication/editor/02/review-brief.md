# review-brief: what-could-go-wrong/self-replication (editor/02) — confirm required fixes

Inputs:
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/editor/01/editorial-review.md — your prior review and its required work
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writer/02/draft-handoff.md — what the writer changed this round
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/researcher/01/evidence.md — the METR o1-preview entry (source s9) owns the harness fix
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writing-coach/01/voice-guide.md
- Article: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/library/what-could-go-wrong/self-replication.html
- Template context dir: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/editor/02/editorial-review.md

This is a confirmation round scoped to your editor/01 required work. Do not
reopen settled matters or introduce a new standard late.

Confirm:
1. The METR o1-preview (~35 min) figure now carries its TRUE harness condition —
   the heavier "advisor" scaffold, not the bare harness — and it checks against
   the METR entry (s9) in the evidence. The bare harness should now carry only
   GPT-4o's ~30-min result. This is the load-bearing fix; verify the direction
   (o1-preview needed MORE scaffolding) is stated correctly and sourced.
2. The figcaption no longer overstates the Qwen gap and reads honestly for both
   models (Qwen 100/100/90, Llama 100/70/50).
3. No regression: the four headline numbers are still never stacked, the
   end-to-end ARA gap is still named, and no new tell or broken sentence entered
   with the edit.

If all three hold, approve. If you make any direct cut, run ./nb stamp and
report the final reading_minutes so the orchestrator can set the byline (the
byline currently reads "8 min read" and must be reset to match the final
reading_minutes before PR — that reset is the orchestrator's, not yours).

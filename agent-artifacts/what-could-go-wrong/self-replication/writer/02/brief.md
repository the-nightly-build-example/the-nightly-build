# writer brief: what-could-go-wrong/self-replication (02) — apply editor/01 required fixes

Inputs:
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/editor/01/editorial-review.md — the required work to apply
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/researcher/01/evidence.md — the claim set; use the METR entries exactly
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writing-coach/01/voice-guide.md — hold the register/licenses
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writer/01/draft-handoff.md — your prior handoff
- Article to edit: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/library/what-could-go-wrong/self-replication.html
- Template context dir: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/what-could-go-wrong/self-replication/agent-artifacts/what-could-go-wrong/self-replication/writer/02/draft-handoff.md

Proof: run from repo root /home/user/the-nightly-build.
  Final (BLOCK: 0, links included): ./nb check --series what-could-go-wrong .nb-work/what-could-go-wrong/self-replication/library/what-could-go-wrong/self-replication.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout
  Run ./nb stamp before the final check.

Apply exactly the editor/01 required items — no other changes:
1. (BLOCKING, load-bearing) The METR o1-preview (~35 min) figure is attributed
   to the "bare harness" alongside GPT-4o, but METR's o1-preview result used a
   heavier "advisor" scaffold. Correct the harness clause so this number carries
   its TRUE condition, per the METR entry in researcher/01/evidence.md. Read that
   entry and state the actual scaffold; do not understate the help. If the
   evidence does not pin the scaffold precisely, state it conservatively to match
   what the evidence supports and note the limit — do not invent a condition.
2. (minor) The figcaption "far more often than they finish" overstates the Qwen
   gap (Qwen 90% finish vs 100% agree). Tighten it so it fits BOTH models
   (Qwen 100/100/90, Llama 100/70/50) honestly.
3. Do NOT touch the byline this round — the orchestrator sets it to match the
   final reading_minutes after your proof. Leave nb-meta counts to stamp.

Preserve all settled work; change only what these items require. Then stamp and
run the links-included proof to BLOCK: 0. Update draft-handoff (02) with one line
per item resolved and the final proof result.

Report: the draft-handoff path, the final proof status (confirm BLOCK: 0), the
corrected o1-preview harness condition you wrote and the evidence locator it
rests on, and the final stamped reading_minutes (so the byline can be set).

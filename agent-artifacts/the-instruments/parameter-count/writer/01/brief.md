# writer brief: the-instruments/parameter-count (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/editorial-direction.md — house standard, paper voice, series prompt
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/commission.md — subject, angle, the ideas to teach, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/writing-coach/01/voice-guide.md — the craft standard for this piece
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/researcher/01/evidence.md — the complete, verified claim set (use its Numbers section exactly)
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/library/the-instruments/parameter-count.html — the initialized article to edit in place
- /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/.nb-context/ — the effective template contract and runtime assets

Output: /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/agent-artifacts/the-instruments/parameter-count/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-instruments/parameter-count/library/the-instruments/parameter-count.html --series the-instruments --library /home/user/library-checkout
(iterate with --no-check-links; final pass with links, until BLOCK: 0)

nb-meta to fill: date 2026-08-05, harness claude-code-routine, model claude-opus-4-8. Run nb stamp for the counts.

This round's focus — two overclaims the evidence record forbids, honor both:
- Active parameters track compute and speed per token, NOT memory: an MoE must
  hold all of its total parameters in VRAM, so deployment/memory cost tracks the
  total (46.7B, 671B), not the active fraction. Do not write that active params
  are simply "the real cost."
- Chinchilla shows compute-optimal allocation, not that parameters are
  irrelevant. Within a fixed recipe, more parameters did raise capability. Do
  not write that the parameter count "tells you nothing."

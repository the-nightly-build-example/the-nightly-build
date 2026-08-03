# writer brief: the-instruments/cost-per-token (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/commission.md — the assignment, angle, boundaries
- /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
- /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/writing-coach/01/voice-guide.md — register and licensed forms
- /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/researcher/01/evidence.md — the complete claim set; use its Numbers and worked example exactly
- Article to edit (initialized from the lesson template): /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/library/the-instruments/cost-per-token.html
- Template context dir (effective contract, furniture catalogs): /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/writer/01/draft-handoff.md

Proof: run from the repo root /home/user/the-nightly-build using the checkout's nb.
  Iterate: ./nb check --series the-instruments .nb-work/the-instruments/cost-per-token/library/the-instruments/cost-per-token.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout --no-check-links
  Final (must reach BLOCK: 0, links included): same command without --no-check-links
  Run ./nb stamp on the article before the final check.

This round's focus (decisions the inputs do not fully carry):
- The misuse section is a PATTERN, not a single dollar-loss incident. The
  evidence's Kimi K2 vs GPT-5.1-class case CONVERGES (near-parity despite a
  half sticker), it does not dramatically reverse. Do not overclaim a flip.
  The honest teaching is "the sticker is an unreliable predictor of real cost,"
  shown by the output-token premium, caching/batch, tokenizer differences, and
  hidden reasoning tokens. Say plainly it is a pattern.
- Every price is dated and volatile (Sonnet 5's $2/$10 is introductory and
  reverts 2026-09-01). Carry the date with the number; do not print a price as
  if permanent.
- Use the researcher's worked example (fixed 10k-in / 2k-out task) with its
  exact recomputable arithmetic. One small table is licensed by the voice guide;
  do not let it repeat figures the prose already states.
- Headline/dek: avoid this series' "two numbers both true" twin mold and the
  comma-triad / semicolon-reversal dek (see editorial direction and voice guide
  do-not-reuse). Tokenizer-dependence rests on Anthropic's first-party "~30%"
  figure across two Anthropic tokenizer generations, not a controlled
  cross-vendor fixed-string count — state it as the evidence supports, no more.
- nb-meta: set date 2026-08-03, harness, and the writer model you ran as. Tags
  array stays empty (no configured tag fragments).

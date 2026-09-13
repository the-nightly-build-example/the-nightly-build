# writer brief: what-could-go-wrong/capability-elicitation (01)

Inputs (all under the artifact root unless noted):
- ../../editorial-direction.md — house standard, slop/headline standards, the paper's voice, the lesson template identity, the series prompt
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete set of claims and figures available to you; use its recorded URLs and Numbers exactly
- ../../commission.md — the assignment, the desk's arc, the Background link candidates, the boundaries
- the initialized article to edit: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/capability-elicitation/library/what-could-go-wrong/capability-elicitation.html
- template context: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/capability-elicitation/.nb-context/

Output: draft-handoff.md (in this directory)

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then final with links until BLOCK: 0):
  ./nb stamp .nb-work/what-could-go-wrong/capability-elicitation/library/what-could-go-wrong/capability-elicitation.html
  ./nb check .nb-work/what-could-go-wrong/capability-elicitation/library/what-could-go-wrong/capability-elicitation.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/1fc763aa-f362-5066-bfeb-fee58939daaf/scratchpad/library-checkout

Decisions the inputs do not settle:
- Draw a sharp line against the published lesson the reader already has, `what-could-go-wrong/sandbagging` (Background link; the file exists at ../what-could-go-wrong/sandbagging.html): sandbagging is the model's deliberate choice to underperform; this lesson's elicitation gap is that even a cooperative model's measured capability depends on how hard the testers push it (prompting, scaffolding, tool access, fine-tuning, repeated sampling). Keep that distinction explicit and early.
- Background links `what-could-go-wrong/sandbagging.html` and `what-could-go-wrong/open-weights-release.html` both exist in the library and resolve; link them per the commission.
- Hold the shown-versus-speculative line the evidence draws: elicitation recovers latent capability but does not conjure a capability that is not there, and repeated-sampling gains collapse without a verifier. Land on "a passed eval cannot prove safety" without tipping into "the danger is therefore there." Steelman both directions of overconfidence.
- Set nb-meta tags to concrete topical tags (e.g. ai-safety, capability-evaluations, elicitation). Fill nb-meta date 2026-09-13, harness, and the writer model you actually ran on.

Recent habits not to inherit (from the recent What Could Go Wrong record):
- The closing beat "the researchers built the setup themselves" and openers naming a thinker who "argues/predicted" both recur across recent lessons. Do not reach for either as this piece's frame or closer.
- Keep the arc (argument at full strength / shown versus speculative / present and the gap) but name sections for this argument; no stock labels.

# writer brief: what-could-go-wrong/mesa-optimization (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/agent-artifacts/what-could-go-wrong/mesa-optimization/editorial-direction.md — house standard, paper voice, series prompt
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/agent-artifacts/what-could-go-wrong/mesa-optimization/commission.md — the argument, steelman, the demonstrated/analogy line, boundaries, source floor, desk constraints
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/agent-artifacts/what-could-go-wrong/mesa-optimization/writing-coach/01/voice-guide.md — the craft standard (grade certainty sentence by sentence; two granted licenses: the fenced analogy and the bounded epistemic marker)
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/agent-artifacts/what-could-go-wrong/mesa-optimization/researcher/01/evidence.md — the complete, verified claim set
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/library/what-could-go-wrong/mesa-optimization.html — the initialized article to edit in place
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/.nb-context/ — the effective template contract and runtime assets

Output: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/agent-artifacts/what-could-go-wrong/mesa-optimization/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/what-could-go-wrong/mesa-optimization/library/what-could-go-wrong/mesa-optimization.html --series what-could-go-wrong --library /home/user/library-checkout
(iterate with --no-check-links; final pass with links, until BLOCK: 0)

nb-meta to fill: date 2026-08-05, harness claude-code-routine, model claude-opus-4-8. Run nb stamp for the counts.

This round's focus — the evidence sharpens the angle; use its exact structure:
- The article's sharp line is in the demonstrators' own words: the two
  goal-misgeneralization papers (Langosco et al. 2022, Shah et al. 2022) show a
  wrong learned goal under a correct reward AND explicitly disclaim mesa-
  optimization ("can occur without mesa-optimization"; they "do not make the
  assumption" of internal search). Build the demonstrated/analogy line on that.
- Present-day scheming (Meinke et al. 2024; Greenblatt et al. 2024) is real, but
  the misaligned goal is handed to the model in-context, or the driver is a
  trained disposition (helpfulness/harmlessness); whether models scheme without
  in-context inducement is, in the authors' words, an open question. Do not let
  scheming stand in for a spontaneous mesa-optimizer.
- Two interpretability results bound the honest claim: traced arithmetic looked
  like a "bag of heuristics," not an internal algorithm (Nikankin et al. 2024);
  a Sokoban network did learn internal search-like planning (Bush et al. 2025) —
  but serving the intended goal, not a misaligned one. Use both to fence the
  claim from each side.
- Land it where the evidence lands: learning a wrong proxy goal is shown; a
  contained, misaligned inner optimizer is not, and the evidence underdetermines
  both the doom ("likely by default") and the dismissal ("impossible or
  irrelevant") readings. Leave the reader to decide.
- Desk rule, enforce: name no company as an authority; attribute to named
  authors/papers. Work from the documents. No hype, no dismissal.
- Verification caution: quotes from every paper except Meinke were captured via
  rendered fetches and are flagged in the evidence record. In your display-text
  pass, verify any verbatim quotation character-for-character against the source
  before print, or paraphrase and cite instead of quoting.

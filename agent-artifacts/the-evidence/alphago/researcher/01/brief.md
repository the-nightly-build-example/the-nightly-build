# Researcher brief: the-evidence/alphago

## Inputs (begin here)
- This brief and `commission.md` (same artifacts folder).
- `editorial-direction.md` for standards.
Do not tour the repo or archive. Use `nb history` only for a specific continuity
question.

## Output (write only this)
`.nb-work/the-evidence/alphago/agent-artifacts/the-evidence/alphago/researcher/01/evidence.md`
Follow the researcher SKILL sections exactly: opening paragraph, Sources,
Contradictions, Numbers, Source assets, Discarded.

## Source policy
the-evidence lesson: **min 6 sources; primary ≥ 3, secondary ≥ 1.** Classify
each source primary/secondary with a reason (authorship and stake, not domain).

## Required primary documents (read the actual text, not coverage)
1. **Silver et al., "Mastering the Game of Go with Deep Neural Networks and
   Tree Search," *Nature* 529:484–489 (2016), DOI 10.1038/nature16961.** Find a
   readable full text (Nature landing, Google Research copy, or an author/host
   PDF). Read the methods. This owns every claim about AlphaGo's architecture,
   training, scale, and the Fan Hui match.
2. **Silver et al., "Mastering the game of Go without human knowledge,"
   *Nature* 550:354–359 (2017), DOI 10.1038/nature24270** (AlphaGo Zero). Owns
   the claim that removing human data still surpassed the 2016 system, and the
   100–0 result.

## Research questions to answer with exact readings
- Architecture: what a policy network and a value network each do in this
  paper; how MCTS uses them (the paper's own description). Capture verbatim the
  sentences defining each.
- Training pipeline and scale: how the SL policy network was trained and on how
  many positions/games (the KGS dataset size — verify the exact number, e.g.
  ~30 million positions from ~160,000 games); the RL self-play stage; how the
  value network was trained (self-play positions). Verify hardware (e.g. number
  of CPUs/GPUs, the distributed vs single-machine versions).
- Results in the 2016 paper: win rate vs other Go programs (e.g. 99.8%); the
  **Fan Hui** match — exact date (Oct 2015), score (5–0 formal games), and
  Fan Hui's exact title/rank (European champion; professional dan rank —
  record precisely). Confirm the Lee Sedol match is NOT reported in this paper.
- Lee Sedol match (secondary source of record): date (9–15 March 2016), final
  score (AlphaGo 4, Lee 1), and that game 4 was Lee's single win. Verify.
- AlphaGo Zero (2017): confirm no human game data used, the self-play-only
  training, and the result against the 2016 version (100–0). Record any nuance
  (which version it beat, "AlphaGo Lee" vs "AlphaGo Fan").
- Present-day usage: find at least one credible source where AlphaGo's
  "search + self-play" is invoked in 2024–2025 reasoning-model discussion, and
  note honestly whether the analogy is qualified (perfect-information game with
  a free win/loss reward vs open-ended tasks). Flag any overstatement.

## Contradictions to hunt
- Popular claim vs paper: "AlphaGo beat the world's best" (Fan Hui was European
  champion, not world #1; Lee Sedol was top-tier but that match is a separate,
  later event). Document the gap precisely.
- "AlphaGo learned Go from scratch / from nothing" — this describes AlphaGo
  **Zero** (2017), not the 2016 paper, which bootstrapped on human games. Nail
  the distinction with citations.

## Numbers section
Every figure the argument needs: KGS training-set size (games and positions),
any win-rate percentages, Fan Hui score and date, Lee Sedol score and date,
Zero's margin vs the 2016 version, hardware counts. Give unit, exact reading,
and owning primary for each.

## Source assets
Consider one exact visual from a cited primary that would let the reader test a
central claim (e.g. a figure from the 2016 paper illustrating the
policy/value/MCTS pipeline, or the results table). Record its location and what
a crop must retain, or write `None found`. Do not prescribe coordinates.

## Control
Return `DONE researcher <evidence-path>`; `BLOCKED researcher <reason>` if a
required primary cannot be opened after a real browser attempt (a paywall is
gated, not dead — try the Google Research / author copy first).

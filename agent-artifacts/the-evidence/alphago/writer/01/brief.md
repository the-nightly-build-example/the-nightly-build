# Writer brief: the-evidence/alphago (round 01)

## Inputs (begin here; reread the voice guide before drafting)
- Commission: `../../commission.md`
- Editorial direction: `../../editorial-direction.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`  ← your complete claim set
- Initialized article (edit in place):
  `/home/user/the-nightly-build/.nb-work/the-evidence/alphago/library/the-evidence/alphago.html`
- Template context: `/home/user/the-nightly-build/.nb-work/the-evidence/alphago/.nb-context/`
  (template-contract.yaml, runtime-assets.yaml, furniture/{engine,press,template}.md)

## Output
- Fill the article HTML above.
- Write `draft-handoff.md` in this folder (`writer/01/draft-handoff.md`).

## What to write
A `lesson` for The Evidence desk. Teach the three ideas the commission fixes,
completely and in order:
1. The architecture: two networks (policy proposes moves, value judges who is
   winning) guiding Monte Carlo Tree Search. Teach MCTS concrete-first per the
   voice guide (one position, a branch count, a probability), name the term
   after the concrete case, then reuse it exactly.
2. The training pipeline and honest scale: supervised learning on 29.4M human
   positions from 160,000 KGS games (main text rounds to "30 million"), then RL
   self-play, then the value network on self-play positions. Give the Fan Hui
   result and its real weight.
3. What later work changed: AlphaGo Zero (2017) trained with no human data and
   still won; then the honest present-day note.

## Decisions fixed for you (do not drift from the evidence)
- **Name the systems precisely.** The 2016 *Nature* paper's system beat **Fan
  Hui** (professional 2 dan, European champion), 5–0, Oct 2015. The **Lee
  Sedol** 4–1 match (March 2016) is NOT in that paper — attribute it to the
  secondary sources. AlphaGo Zero's **100–0** win was against **AlphaGo Lee**
  (the version that beat Lee Sedol), not the Fan Hui system — say "AlphaGo Lee",
  never "the 2016 system" or "the original AlphaGo", when reporting 100–0.
- **The two myths to retire, by fact not by rhetorical reversal:** "AlphaGo beat
  the world's best" (the paper only claims play "at the level of the strongest
  human players"; Fan Hui was the European champion) and "AlphaGo learned Go
  from nothing" (that is AlphaGo **Zero**, 2017; the 2016 system bootstrapped on
  human games). Use the "not X but Y" shape at most once in the whole piece.
- **Present-day section — follow the evidence, do not manufacture a foil.** The
  strongest citable primary (DeepSeek-R1, Jan 2025) invokes AlphaGo/AlphaGo Zero
  and then explains *why the search-plus-self-play recipe did not transfer* to
  language (exponential token search space, no easy fine-grained value model).
  Report that honestly: the sharpest present-day use of AlphaGo is a lab marking
  where the analogy breaks. You may note that looser overreach lives in informal
  commentary, but do not invent or quote a strawman.

## Source handling
- Number sources in first-citation order. Kinds from the evidence record:
  Nature 2016 (primary), Nature 2017 Zero (primary), DeepSeek-R1 (primary);
  Wikipedia, People's Daily, Google blog (secondary). Set `data-nb-kind`
  accordingly. Six sources meets policy (min 6; primary ≥3; secondary ≥1).
- Add `data-nb-locator` only where the evidence supplies a locator (it does for
  most — e.g. "Nature 2016, p. 488"). Never invent one.
- Every number carries a comparison the reader already holds (voice guide).

## Furniture
- Plan furniture with the prose. A `nb-stat-strip` of the numbers that carry the
  thesis is a natural fit (e.g. 99.8% win rate vs other programs; 29.4M human
  positions behind the "from scratch" myth; 100–0 AlphaGo Zero vs AlphaGo Lee) —
  each stat must be cited in nearby prose. Use only documented furniture from the
  catalogs. Do not add a component without a communicative purpose.
- A chart or source asset is **optional**. If a comparison is genuinely the
  point (e.g. the Elo ladder Fan/Lee/Master/Zero, all in the evidence Numbers
  table), you may build ONE `nb chart` from those verified numbers and commit its
  provenance; inspect the image. The evidence also flags Figure 4 of the 2016
  paper as a strong source asset (shows Fan Hui's rank on the dan scale) — only
  capture it with `nb asset` if it is clean to do; prose + a stat strip is
  acceptable and lower-risk. Do not hotlink external images.

## Bookends (write last, after the body)
- "Why this matters" and "The takeaway" per the lesson identity: this lesson's
  particulars only, resolve what the opener sets up, teach nothing new in the
  takeaway. No verdict block.
- Background rows: link `the-evidence/the-bitter-lesson` (AlphaGo is Sutton's
  central example) and one useful outside item. Go deeper rows: always beyond
  this paper.
- Reading rows point: Background `../the-evidence/the-bitter-lesson.html`.

## Headline / dek / headings
- Headline: state the finding with actors named; no colon-subtitle, no
  comma-triad, no question unless answered. A candidate angle the piece can
  defend: the gap between what the 2016 paper measured (Fan Hui, human-trained)
  and the popular memory. Find the sharpest true line.
- Dek: adds what the headline omits; no banned dek molds; check recent library
  deks first.
- Section headings: argument steps in the piece's own nouns; vary shape; do NOT
  open with "The number X published about itself"; avoid comma-triad headings.

## Constraints
- Word band 1200–2200. Banned terms enforced by the proof: em-dash ≤4,
  leverage ≤1, load-bearing 0, revolutionary/transformative/game-changing 0,
  "AI race" 0, machinery 0. Prefer plain words.
- nb-meta: fill actual values. `mode` open, `order` null, `date` 2026-08-02,
  `template` lesson, `series` the-evidence, `slug` alphago,
  `harness` "claude-code-routine", `model` "claude-sonnet-5",
  `tags` ["reinforcement-learning","self-play","monte-carlo-tree-search","deepmind"].
  `sources`, `words`, `reading_minutes` measured, not inflated.

## Original work
Name, in `draft-handoff.md`, the piece's one visible act of original work: the
ledger separating what each cited document actually establishes (2016 paper /
2017 Zero paper / the Lee Sedol record) from the fused popular memory. It must be
visible in the article.

## Prove and hand off
Run to `BLOCK: 0`:
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series the-evidence \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/the-evidence/alphago/library/the-evidence/alphago.html
```
Treat warnings as revision notes: fix or record why each stands. Use `nb
preview` if you add a chart/asset, and inspect the render. Write
`draft-handoff.md` (original-work sentence; paths changed; proof result +
warnings left; remaining evidence/voice questions). Return `DONE writer
<draft-handoff-path>` after BLOCK: 0, or a REQUEST line if evidence/voice is
missing.

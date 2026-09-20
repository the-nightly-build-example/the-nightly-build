# Editorial review: the-instruments/brier-score (editor/01)

## Skeptic

Thesis: a Brier score is a legitimate, gameable-only-by-honesty scoring rule,
but two Brier scores are comparable only when they cover the same questions,
the same period, and the same scale convention — and the 2023-2024 "AI
approaches human-level forecasting" claim fails on exactly those grounds when
its own cited numbers are read plainly.

Claims tested:

1. **The worked definition and the 0.25/0.42/0.44 baseline figures.**
   Recomputed by hand: the four-row table sums to 1.08/4 = 0.27 as printed;
   the always-0.5 baseline is exactly 0.25 ((0.5−1)²=(0.5−0)²=0.25); Brier's
   own 0.42/0.44 figures match his Table 1 text exactly. Held.
2. **The halving is a convention, not a skill change.** Ran GJOpen's own
   70%-rain example (0.18, two-term) through the halved formula and got 0.09,
   matching Halawi's one-term convention exactly. The article states both
   numbers "describe the same forecast and the same result," which is the
   convention framing the brief asked for. Held.
3. **The base-rate trap via Murphy's uncertainty term.** Recomputed the
   always-10%-forecaster case: reliability 0 (matches base rate), resolution
   0 (never varies), uncertainty = 0.1×0.9 = 0.09 — matches the article's
   figure and correctly shows the trap growing as the base rate moves off
   50%. Sourced via Ferro & Fricker as the brief required, not Murphy's gated
   original. Held.
4. **Halawi et al.'s headline vs. full-test result.** Fetched and reread the
   primary (Section 6.1/Table 4): system 0.179, crowd 0.149, a loss; the
   "surpasses" claim survives only on the 0.3–0.7 subset at 0.238 vs. 0.240,
   an order of magnitude below the paper's own ">.02" bar for a "large"
   margin. Correctly and carefully attributed the extension of that ">.02"
   bar to the critique as an inference, not something Halawi's team said.
   Held.
5. **The Lu 2025 o3-vs-experts comparison.** This one broke. I fetched the
   full paper. The draft called the 157-question expert panel "a comparable
   set of questions" to o3's 334-question score. Lu's own paper states the
   157 questions are 47% of the 334 — a subset, not a matched set — and the
   paper's own Section 5.1 says plainly that "Brier scores are not directly
   comparable across different question sets." The lesson was about to
   commit its own central sin without saying so. Fixed directly (see Edits):
   named the 157/334 subset relationship and quoted Lu's own caveat, turning
   a false "comparable" claim into an honest second instance of the very
   trap the lesson teaches.
6. **The ForecastBench stat strip.** This one also broke, more seriously.
   Fetched the primary (Section 5.2): superforecasters (0.096) significantly
   beat both the general public (0.121, p<0.001) and the top LLM (0.122,
   p<0.001) — but the draft's prose claimed "the best language-model
   configuration edged out the public." That is backwards: 0.122 is worse
   than 0.121 (lower is better), and the paper reports no significant
   difference between the model and the public at all, only that
   superforecasters beat each of them separately. Fixed directly: the model
   now "scored about the same as the public," and the significance claim is
   attached to both comparisons superforecasters actually won.
7. **Murphy's title.** "The statistician Allan Murphy" is not what his own
   record supports: B.S. in meteorology (MIT), Ph.D. in atmospheric and
   oceanic science, Fellow of the American Meteorological Society, published
   in the Journal of Applied Meteorology. Corrected to "the meteorologist
   Allan Murphy," which also now parallels "the meteorologist Glenn Brier."
8. **Citations open cleanly.** Opened all eight printed hrefs directly
   (curl, 200 on each): the two arXiv abstract pages, the Internet Archive
   Brier scan, Wikipedia, the Ferro & Fricker PDF (fetched and confirmed
   159 KB, readable), GJOpen's FAQ (confirmed the 0.18 quote is on the live
   page), the AI Alignment Forum post, and Lu's arXiv page. Every href lands
   on the source itself, not a gate or a mirror. `data-nb-kind` labels all
   check out against the primary/secondary test, including the two Halawi
   co-authorships (s1, s5) being disclosed in prose rather than hidden.

No central claim broke. Both breaks were supporting figures inside sections
that survive the correction — the Lu fix actually strengthens the lesson's
argument, and the ForecastBench fix makes an already-strong finding
(superforecasters win) accurate about the runner-up comparison too. Neither
needed new reporting; both were fixable by rereading the primary already at
hand.

## Cut

Ran the slop test on every edge sentence, the delete test on the article, and
checked structure against the press's own standing rules.

- **Removed the body's `nb-note-strong` "Verdict" block** (end of the last
  numbered section, before the takeaway). `press/editorial.md` states this
  exactly: "Do not close the body with a Verdict note, or any block that
  restates the finding... It is a leftover, not a model to copy." The block
  also failed the delete test on its own terms — it restated, almost
  verbatim, ground the takeaway bookend was already going to cover two
  paragraphs later. The section now ends on its strongest sentence (the
  ForecastBench significance line), which states a finding rather than
  grading one.
- **Fixed a banned heading mold.** "Two kinds of low score, and only one
  means anything" joins two clauses with a comma and "and" — the exact
  pattern `spec/headlines.md` names as a stamped-looking construction.
  Rewrote to "The low score you get without looking," which also pulls
  forward the section's own phrase ("never looks at a question's
  specifics") instead of coining new language.
- **Fixed a formula echo against the recent record.** The why-card's third
  sentence ("This lesson works out what that grade counts...") is close
  enough in shape to auroc.html's why-card ("This lesson shows what the
  figure actually counts...") to read as the same mold once a reader has
  seen both. Rewrote to lead with the anchor fact (two cheap tricks) instead
  of a lesson-shows-X construction.
- **Date precision.** "A few months later" undercounted the seven months
  between Halawi et al. (Feb. 2024) and the AI Alignment Forum critique
  (Sept. 12, 2024); a paper with the exact date already in the evidence
  record should give the figure, not the magnitude. Changed to "seven
  months later."
- Checked every paragraph, section, and the article's edges in isolation:
  no dangling referents, no empty conclusions, no vague attribution, no
  unearned punchlines. The one negative-parallelism construction I pushed on
  hardest — "not whether the stated numbers are true, but whether the
  forecaster tells cases apart at all" — earns its place: it names the
  calibration/resolution split that is this lesson's central distinction,
  not a strawman.
- Checked the recent-pattern notes from the commission and the review brief
  directly: no "By the end you will know" opener, no temporal-generic first
  sentence, no two-part-balance takeaway closer, no "Reading X as Y" closer,
  no other "How a X becomes a Y" heading, no nb-holdsup pairing, no
  comma-triad or comma-splice dek. One heading mold recurred (above, fixed)
  that wasn't on the named list but matched `spec/slop.md`'s general Formula
  entry once checked against the sibling articles directly.
- Punctuation: 3 em-dashes and a small number of semicolons, all under the
  `spec/banned-terms.yaml` cap (max 4) and each tightly binding two clauses
  a period would over-separate. Left them as found rather than manufacture
  churn.

## Reader

Read straight through as the declared reader. What I have that the sources
alone would not give me: a single worked case run through the same
mechanism twice (Murphy's uncertainty term explaining the base-rate trap,
then the same underlying two-term/one-term arithmetic explaining the scale
trap on one real GJOpen forecast), and a claim's rise and fall tracked
across four independent papers read in the primary rather than asserted.
The original-work sentence in `draft-handoff.md` matches what the article
actually does. The prose sits closer to the voice-guide exemplars than to a
median AI summary: verdicts are stated once and left ("the system lost,"
"that is backwards" territory now fixed into the prose itself), mechanism
comes before judgment throughout, and the base-rate and scale traps are
demonstrated with arithmetic the reader can rerun rather than asserted.
Reread as the largest claim, the headline states a real, specific, checkable
number and flags its own scope ("on a subset of the questions"), so a
reader who stops there is not misled — the dek does the correcting work a
scanning reader still needs.

## Edits

1. Removed the `nb-note-strong` "Verdict" block that closed the body,
   per `press/editorial.md`'s explicit ban on a Verdict note closing the
   body; its content was already duplicated in the takeaway.
2. Rewrote the heading "Two kinds of low score, and only one means
   anything" to "The low score you get without looking" (banned comma-and
   heading mold) and updated its `data-nb-section`/`id` to match.
3. Rewrote the why-card's third sentence to remove a formula echo of
   auroc.html's why-card ("This lesson shows what the figure actually
   counts...").
4. Changed "the statistician Allan Murphy" to "the meteorologist Allan
   Murphy" (title correction against his actual record).
5. Changed "a few months later" to "seven months later" (Halawi Feb. 2024
   to the AI Alignment Forum critique Sept. 2024 — give the figure).
6. Rewrote the Lu 2025 paragraph: removed the false "a comparable set of
   questions" characterization of the 157-question expert panel, named it
   as a 157-of-334 subset, and added Lu's own quoted caveat that "Brier
   scores are not directly comparable across different question sets" —
   corrects a claim the primary source does not support and turns it into a
   second, honest instance of the lesson's own point.
7. Rewrote the ForecastBench closing sentence: removed the claim that "the
   best language-model configuration edged out the public" (backwards —
   0.122 is worse than 0.121, and the paper reports no significant
   model-vs-public difference), replaced with "scored about the same as the
   public," and attached the paper's p<0.001 significance finding to both
   comparisons superforecasters actually won.

Net effect on length: the cuts (mainly the Verdict block) outweigh the
additions; the article is now under its prior 2194-word stamp, comfortably
inside the 1200–2200 band.

## Required work

- **Orchestrator:** re-run `./nb stamp` and then `./nb check
  .nb-work/the-instruments/brier-score/library/the-instruments/brier-score.html
  --series the-instruments --library .nb-work/library` (links included)
  before preparing the PR. Word count and reading-minutes in `nb-meta` are
  now stale after these edits; `./nb check` passes as-is (BLOCK: 0, WARN: 0)
  but the stamped counts should reflect the edited text before publication.
- No outstanding items for the researcher or the writer. Both breaks found
  in this round were fixed directly from primary sources already cited in
  the evidence record or opened fresh in this review; neither required new
  reporting.

## Decision

**Approve**, after direct cuts — the article's central claims all held under
recomputation and reread; the two claims that broke (the Lu 2025 subset
mischaracterization and the backwards ForecastBench model-vs-public claim)
were fixed in place from sources already in hand, along with one banned
heading mold, one formula echo against the recent library, a body Verdict
block the press explicitly forbids, and two minor accuracy fixes. The
orchestrator must re-stamp and re-check before the PR.

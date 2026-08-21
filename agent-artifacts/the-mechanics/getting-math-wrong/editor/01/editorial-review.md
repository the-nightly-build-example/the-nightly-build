# Editorial review: the-mechanics/getting-math-wrong (editor/01)

## Skeptic

Thesis: a chatbot returns a confident, near-right wrong answer to a large
multiplication because no part of the raw model multiplies anything; it predicts
the next digit, and three separate failures (chunked tokenization that loses
place value, a forward pass with nowhere to hold a carry, and an internal
number representation that is only partly mapped) explain why small common sums
come out exact and large rare ones come out plausible and wrong.

The claims it stands on, and how each held:

- **The anchor: 57,897 x 12,832 returned as 742,021,104, true product
  742,934,304, miss 913,200 (~0.12%).** Recomputed independently: 57,897 x
  12,832 = 742,934,304; 742,934,304 - 742,021,104 = 913,200; 913,200 / 742,934,304
  = 0.1229%. All three figures in the headline, table, and prose are exact. The
  source (s1, TechCrunch/Wiggers) prints the same transcript verbatim
  ("ChatGPT gave me the answer 742,021,104; the correct one is 742,934,304").
  Both operands are five digits, so the headline's "two five-digit numbers" and
  the body's placement of the case in the "5-digit x 5-digit" row are correct.

- **Accuracy fall-off: GPT-4 zero-shot 59% / ~4% / ~0% at 3/4/5-digit.** Opened
  s2 (Dziri arXiv) and s3 (Ai2 blog). The Ai2 post states 59% at 3-digit and 4%
  at 4-digit in those words; the arXiv paper owns the "reduces to linearized
  subgraph matching... performance rapidly decays with complexity" claim and the
  collapse toward zero as size grows. The 5-digit "~0%" is not printed as a
  discrete number in either venue; it rests on the paper's documented
  degradation-to-zero curve. The article marks it "~0%" with a tilde and cites
  the study that shows the curve, so the approximation is honestly labeled rather
  than overstated. s2 and s3 are the same team's study in two venues (arXiv paper
  and lead author's own blog), both correctly labeled primary; citing both for
  the table is one study reported twice, not a false claim of independent
  confirmation.

- **Tokenization: OpenAI tokenizers cap a numeric token at three digits
  (`\p{N}{1,3}`), scoped away from single-digit-tokenizer models.** Opened s4
  (tiktoken source): the `\p{N}{1,3}` digit component is present in the o200k_base
  pattern and, as `\p{N}{1,3}+` (possessive quantifier, still a three-digit cap),
  in cl100k_base. The article prints the literal as `\p{N}{1,3}` and says it is
  "the same in cl100k_base and o200k_base"; the cap of three holds in both, and
  the possessive `+` in cl100k does not change the cap. Opened s5 (Singh &
  Strouse): confirms LLaMa and PaLM use single-digit tokenization while GPT-3.5/4
  give separate tokens to 1-, 2-, and 3-digit numbers, and that comma-separated
  right-to-left rewriting improves GPT-3.5/4. The 380/381 example (s1) is stated
  in TechCrunch as an illustration ("a tokenizer might treat 380 as one token but
  381 as 38 and 1"); the article states it as fact, which the underlying
  tokenizer behavior supports.

- **Carry has nowhere to live; external fixes recover accuracy.** Opened s6 (Bai
  et al.): confirms standard fine-tuning "converges to a local optimum that lacks
  the required long-range dependencies" and that success comes from caching and
  retrieving pairwise partial products, exactly the article's rendering. Opened
  s7 (TechXplore): confirms <1% for standard fine-tuning on 4-digit
  multiplication vs 100% for implicit chain-of-thought, and that the report
  attributes the jump to training method, not to reasoning models solving
  multiplication on their own. Nye (s8, scratchpad) and Toolformer (s9,
  calculator API) are used within their established findings.

- **Step 4 left open; heuristics-vs-helix dispute named; Nanda flagged as a
  toy.** Opened s10 (Nikankin): confirms the "bag of heuristics" of sparse
  pattern-firing neurons with no general algorithm. Opened s11 (Kantamneni &
  Tegmark): confirms the generalized-helix representation and the "Clock"
  rotation for addition; the two-digit [0,99] range and mid-size open models
  (GPT-J, Llama-3.1-8B) are stated in the evidence record's locators and the
  article reports them accurately. Opened s12 (Nanda): confirms a small
  transformer on modular addition, reverse-engineered to a Fourier/trig circuit
  converting addition to rotation on a circle. The article correctly presents
  this as a toy and warns against offering it as how ChatGPT multiplies.

Display text checked descriptor by descriptor. Headline: subject/verb/surprise
up front, every quantity true. Dek: a claim about the world, adds the mechanism
the headline omits, does not grade the article's method. Table captions: the
worked figures and the "by operand size" label match the cited primaries. No
named person carries a title in display text to check. Every `data-nb-kind`
label is correct against the primary/secondary test (three secondary reports —
s1, s7; s3 is a same-author restatement correctly kept primary; the rest are the
owning documents). Every citation href was opened as printed and lands on the
source itself; all twelve resolve.

The three scopings hold and are not overstated: the raw no-tool/no-scratchpad
framing is stated in the opener and reasserted in the carry step and takeaway, so
a reader watching a current product multiply correctly cannot falsify it; the
"chunks, not clean digits" cause is explicitly bounded to OpenAI-style
tokenizers with LLaMa/PaLM named as the single-digit exception; step 4 is left
open in prose, with the live disagreement named and Nanda's circuit flagged as a
toy rather than the explanation. No broken central claim, no missing evidence, no
sourcing failure. Nothing routed to the researcher.

## Cut

The prose is mostly clean and concrete. The slop pass turned up a small set of
edge and furniture failures, all fixable in place:

- One self-grading signpost in the orientation ("That near-rightness is the
  strange part"): an "X is the Y" assessment that announces strangeness before
  the reasoning that follows does the work. Failed the delete test. Cut.
- Two uses of "honest" as a virtue word, which the recent-pattern notes flag as a
  the-mechanics diction tic: "One caution keeps this honest" (also a signpost
  framing) and "no honest account of the failure pretends otherwise" (a clause
  that grades other accounts rather than continuing the argument). Rewrote the
  first to a plain declarative and cut the second clause.
- Prompt leakage: "Both wrap a step-3 fix around the same next-token core." The
  reader has no numbered "step 3"; the numbering is the commission's spine.
  Replaced with "an external fix."
- Body self-reference: "The behavior this lesson explains is the model with all
  of that turned off." The lesson template confines self-reference to the two
  bookends; the body speaks to no one and never mentions the lesson. Recast as
  "The failure at issue is the raw model with all of that turned off."
- Body first-person: "our example." Recast to "the example above" to match the
  third-person register and the table caption's own "the anchor problem above."

Edges and headings compared against the recent-pattern notes: the dek avoids the
mechanism-as-subject-resolving-on-a-flat-declarative mold; no heading is
imperative/second-person, subject-dropped past-participle, or the retired
"What's settled, and what's still open" stock heading; the opener is "Someone
asked ChatGPT..." not the banned "Ask a model to..."; the closer is not the terse
"The next time..." kicker. The settled/open split is marked in prose
("established" / "genuinely unresolved") with no stock heading and without
leaning on "unsettled." Differentiation from `letter-counting` is explicit and
sharp (characters hidden inside a token, versus digit-token boundaries that miss
place value), and `thinking-out-loud` and `tool-use` are linked as the fixes,
not re-taught. Compared distinctive phrasing against the voice-guide quotations;
no borrowed clause. No banned-term or punctuation tell noticed beyond the two
"honest" uses handled above (the proof counts the merged list). Furniture: two
tables, both earning their place (the worked anchor; the fall-off trend); the
writer's decision not to force a chart on three data points is sound. The two
bookends address the reader within their documented allowance and each sentence
says something.

Roughly five sentences/clauses failed the slop or scope test; all were repaired
or cut directly, no repeated structural pattern beyond the "honest" diction tic.

## Reader

What the piece gives beyond its sources: a single backward causal chain from one
documented botched multiplication down to the point where interpretability runs
out, threading twelve separately-sourced findings (tokenizer source code, an
accuracy curve, a reverse-engineering of why multiplication fails, the
heuristics-vs-helix dispute, a modular-addition toy) so the reader can see which
part of the system owns each part of the failure, scoped honestly to the raw
model. No single source supplies that synthesis; the draft-handoff's
original-work statement claims exactly this and it holds. The prose sits closer
to the voice-guide exemplars than to a median summary: plain declaratives, the
small arithmetic done out loud (0.12%, 742 million), the true and wrong products
set side by side, and the limit of knowledge marked flatly in the third person
in the Karpathy manner. The headline as the largest claim is defended by the
body.

## Edits

- Cut the self-grading signpost "That near-rightness is the strange part" from
  the orientation section.
- Changed "our example, a five-digit case" to "the example above, a five-digit
  case" (removed body first-person).
- Rewrote "One caution keeps this honest: chunked digits are a fact about
  OpenAI-style tokenizers, not about every model." to "Chunked digits are a fact
  about OpenAI-style tokenizers, not every model." (removed virtue-word "honest"
  and signpost framing).
- Changed "Both wrap a step-3 fix around the same next-token core" to "Both wrap
  an external fix around the same next-token core" (removed commission
  step-numbering leakage).
- Changed "The behavior this lesson explains is the model with all of that turned
  off." to "The failure at issue is the raw model with all of that turned off."
  (removed body self-reference to the lesson).
- Cut the clause "and no honest account of the failure pretends otherwise" from
  the how-it-adds section (virtue-word "honest" plus a grading signpost).

## Required work

- writer: run the proof again on the edited article; the direct edits removed a
  sentence and two clauses, so the stamped `words` (currently 2043) and reading
  time need refreshing. No reporting, redraft, asset, or chart work is required.
- orchestrator: re-stamp the article after the fresh proof before preparing the
  PR.
- researcher: none.

## Decision

approve — every claim is sourced and verified, the arithmetic and display text
are exact, the three scopings hold without overstatement, and the remaining slop
was minor and fixed in place; the article needs only a fresh proof and re-stamp
after these edits.

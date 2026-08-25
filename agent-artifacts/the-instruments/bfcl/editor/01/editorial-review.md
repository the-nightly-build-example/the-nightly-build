# Editorial review: the-instruments/bfcl (editor/01)

## Skeptic

**Thesis.** A Berkeley Function-Calling Leaderboard score grades one proposed
tool call against a known-correct answer, mostly by parsing the call rather than
running it, so a high function-calling number shows single-call skill and not
multi-step agent reliability.

**Claims it stands on, and how each held.**

1. *The cited headline is 66.4%, and it is the top model on the paper's board.*
   Verified against the ICML/PMLR v267 PDF (read firsthand via extraction): the
   Table 1 top row is `gpt-4o-2024-11-20 (Prompt) 66.4`, with single-turn cells
   in the high-80s to 100. Holds. The landing page at proceedings.mlr.press
   resolves to the paper with the correct author list and venue.

2. *Grading is parse / run / decline, and parsing dominates.* The AST rule quote
   ("if the function name matches exactly and if all parameter values fall within
   their respective possible answers") and the execution quote ("Execution
   involves running the specified function and examining its output") both verify
   verbatim against the sources they cite (s1 PDF; s3 v1 blog). v1 ran ~300 of
   ~2,000 cases and the live 2,251 set is AST-only — both confirmed against the
   v1 and v2-Live blogs. Holds.

3. *AST grading is faithful, not loose.* The paper's strong AST-vs-execution
   correlation (Figure 3) verifies in the PDF ("strongly correlated"). This is
   the honest counterweight and the article carries it. Holds.

4. *Single-call skill does not equal multi-step reliability.* The τ-bench
   contrast (≈61% retail pass^1, pass^8 <25%) verifies: the arxiv abstract and
   the evidence record carry pass^8 "<25% in retail," and the article correctly
   scopes the 61% to retail. The authors' own limit quote ("while
   state-of-the-art LLMs excel at single-turn calls, memory, dynamic
   decision-making, and long-horizon reasoning remain open challenges") is an
   exact match to the PDF. Holds.

5. *The board rewrote its own answer key.* The 2024-10-16 [#661] changelog entry
   (547 live_multiple, 104 live_simple, among others) verifies against the raw
   CHANGELOG; 547 of the ~1,053-case live "multiple" category is more than half,
   as stated. Holds.

**Breaks found.**

- **False label in the dek (fixed).** The dek called the 66.4% "a single-turn
  number." It is not: 66.4% is the overall unweighted average across every
  sub-category, and the article's own body says it is "already dragged down from
  the near-perfect single-call numbers" by the near-zero agentic/memory cells. A
  single-turn number would be *higher* than 66.4%, not equal to it. The label was
  false and internally contradicted the body. Fixed in place (meta block and
  visible dek both) to "mostly reflects single calls," which matches the body's
  "still mostly the score of one call" and alters no number, name, or the dek's
  claim.

- **Miscitation on the metric-overhaul clause (fixed).** "Its scoring metric was
  overhauled six weeks after it launched" was cited to s7, the v3 blog. That blog
  presents state-based and response-based scoring as v3's original design and
  does not document the later overhaul or its timing. The 2024-10-30 [#725/#733]
  change (a response-based checker added alongside the state-based one) is owned
  by the changelog, s8, which is already in the article. Split the citation: s7
  stays on the multi-turn set's size, s8 now carries the overhaul. First-citation
  order is preserved (s8 still follows s7).

- **Secondary source does not confirm the framing it is cited for (routed).**
  s5 (Emergent Mind) is cited once, for "An outside overview of the board lands
  on the same shape: the top models ace the one-shot questions and stumble once
  they must remember context, manage a long conversation, or decide not to act."
  Two targeted reads of that page confirm it supports the five single-turn
  category types, but could not find the single-turn-strong / multi-turn-weak
  "stumble" framing; the page instead emphasizes perturbation/robustness and
  notes multi-turn performance is *improving*. The underlying claim is not in
  danger — the primary paper (s1), cited in the same paragraph and in the note
  quote right after, owns it fully. But a cited source must support the specific
  claim it is attached to, and this is the article's only secondary, so it cannot
  simply be cut without breaching the commission's >=1-secondary floor. Routed to
  the researcher. (The writer's own handoff flags this exact line.)

**data-nb-kind audit.** Eight sources: s1 s2 s3 s4 s6 s7 s8 primary, s5
secondary. Every label matches the evidence record's designation. The lone
secondary is used once and the seven primaries clear the composition floor, as
the brief's focus predicted. The one caveat is the s5 support question above,
which is an accuracy issue, not a label issue.

**Minor, not blocking.** "The fourth adds agentic tasks such as memory and
search" is cited to s7, whose v3 blog points forward to the V4 blog but does not
itself enumerate the agentic categories; s1 (in the article) owns that fact and
s2 confirms V4. Left as-is because s7 does reference V4's existence and the fact
is true and supported elsewhere in the piece; the writer may add s1 or s2 there
if re-touching the paragraph.

## Cut

A dedicated slop pass, then the edges, then the delete test.

- **Banned-term counts.** Em-dashes: 0 (budget 4). En-dashes: 0. "leverage" /
  "load-bearing": 0. No filler tells ("the number that matters most", "worth
  knowing", elaborate copula, decorative -ing clauses).
- **Negative parallelism.** Three "rather than" / "not whether" constructions,
  each a genuine, named distinction central to the mechanics (parsing vs.
  running; a set of allowed values vs. a single one; expose the gap vs. close
  it). None is an invented strawman. All stay.
- **Edges.** First and last sentences of every paragraph and section read
  clean: each closer carries a fact or a reasoning step, not a signpost. The
  section closer "A faithful grade of one call is still a grade of one call, and
  an agent is never asked to make exactly one" is the earned accuracy-to-reach
  pivot the voice guide calls for (the Gladwell repetition move), and it survives
  the delete test — removing it loses the turn from "is the grade right" to "is
  one grade enough." Kept.
- **Takeaway closer.** "Read a high function-calling score as what it is, a
  strong single call, and ask separately whether the model can string many of
  them together" states the conclusion the argument built and does not fall into
  the flagged "a very low score rules X out; a very high one does not rule it in"
  mold. Kept.
- **Formula check.** The section order loosely tracks the desk's recurring
  mold (claim -> what the score is -> internals -> what it never measured ->
  the correction), but the internals surprise is a worked example (get_weather)
  and a table, not the mold's usual code snippet, and the "faithful" section is
  an honest counterweight that interrupts the march. Headings are in the piece's
  own nouns and reconstruct the argument. Not a formula finding.
- **Leakage.** No planning labels, selection rules, or assignment-fulfilled
  claims in the body. The bookends address the reader and name the lesson, which
  the lesson template expressly allows, and they say something specific to this
  subject. No lifted commission/brief phrasing.
- **Furniture.** The parse/run/decline table earns its place (three shapes the
  reader must compare). The authors'-limit note and the τ-bench pull quote both
  sit in the chaining section; the pull quote restates the body sentence just
  above it, which is standard scannable emphasis of the pivotal contrast, so it
  stays, though it is the one component a reader could lose without losing an
  argument.

No sentences were cut: none failed the slop test outright, and the edges all
carry weight.

## Reader

Read straight through as the course reader, the article gives something the
sources alone do not: a plain, job-by-job account of which parts of "agent
reliability" a function-calling number measures (the single call, graded
faithfully) and which it never reaches (chaining, error recovery, memory,
declining to act), tied to the τ-bench collapse as the reliability reality and
to BFCL's own answer-key rewrites as the concrete cost. No single source makes
that connection: the paper reports the numbers, τ-bench reports its own, the
changelog lists fixes. The original-work sentence claims exactly this assembly,
and it survives. The prose sits closer to the voice-guide exemplars (Evans/Silver
plainness, exact technical words, the worked example a reader can check without
the leaderboard) than to a median summary. The headline, reread as the largest
claim, is a finding the piece defends: the score grades one call and usually
never runs it.

## Edits

- Dek (meta block): "is a single-turn number" -> "mostly reflects single calls".
- Dek (visible dekline): same change, kept in sync with the meta block.
- Chaining paragraph: split the trailing s7 citation — s7 now sits on the
  multi-turn set's size, and s8 now carries "its scoring metric was overhauled
  six weeks after it launched," the claim the changelog owns.

## Required work

- **researcher:** Confirm whether Emergent Mind
  (https://www.emergentmind.com/topics/berkeley-function-calling-leaderboard-v4-bfclv4)
  actually supports the single-turn-strong / multi-turn-weak "stumble" framing
  the article attaches to s5, and supply the exact passage. If it does not,
  re-source that sentence: either re-point s5 to what it does support (the five
  single-turn category types) and recast the sentence's claim accordingly, or
  supply a different secondary source that genuinely carries the
  single-vs-multi-turn framing. Because s5 is the article's only secondary, the
  resolution must keep a legitimate secondary source so the >=1-secondary
  composition floor still holds.
- **writer (after the researcher resolves the source):** Apply the resulting
  citation and prose change to the "An outside overview of the board lands on
  the same shape" sentence, then re-run `./nb check` and `./nb stamp` to a clean
  proof.

## Decision

revise — a false "single-turn number" label in the dek and a metric-overhaul
miscitation were fixed in place, but the article's only secondary source (s5)
could not be confirmed to support the framing it is cited for, and that sourcing
gap must be closed by the researcher (then applied by the writer) before publish.

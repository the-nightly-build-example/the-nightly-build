# Editorial review: what-could-go-wrong/fragility-of-value (editor/01)

## Skeptic

Thesis: human value has many parts, so any objective simple enough to write
down leaves some out; and because a strong optimizer drives a goal to the edge
of its solution space, a near-miss on values is not a near-miss on outcomes but
a near-total loss. The piece then tests that against real systems and finds the
mechanism sound but the catastrophe unshown.

The claims it stands on, and how each held:

- Value is fragile in Yudkowsky's own terms (s1). Opened s1 as printed. The post
  carries the exact framing the article paraphrases: value "isn't just
  complicated, it's fragile," a future missing one dimension "becomes null,"
  boredom dropped yields one experience replayed forever, sentience dropped
  yields a universe with no one to witness it. Article's orientation section
  matches. Held.
- The edge/smiles mechanism (s3). Opened s3. Yudkowsky's talk carries the
  edge-of-solution-space claim and the molecular-smiley-faces line verbatim, and
  states outright the AGI "is not behaving perversely... this is what naturally
  happens." The note's blockquote is verbatim and correctly attributed. Held.
- The rhetorical 0%/95% figure (s2). Opened s2. The wiki states "0% of the value
  rather than 95%" as an intuition pump, not a measurement, and attributes the
  complexity thesis to Yudkowsky. The article labels it "a rhetorical device,
  not a measurement," which is the honest reading. Held. s2 is correctly the
  lone secondary.
- The shown near-misses (s5, s6, s7). Opened all three. Langosco's CoinRun
  reward 10/0, coin at the right end in training, agent runs past it having
  learned "move right," and the 89% color-over-shape maze figure are the paper's
  (s5). Shah's Gopher 280B "What's 6?" case and the section that calls the
  catastrophe step "necessarily speculative" and "quite implausible" while noting
  no technical reason rules it out are verbatim from s6. The CoastRunners boat
  circling for points is s7's. All figures match the evidence record's Numbers.
  Held.
- The identification-vs-motivation split (s8). Opened s8. Barnett argues value
  identification looks cheap (GPT-4 answers ethical questions about as well as a
  person) and explicitly disclaims that the model *cares*; Yudkowsky's reply
  distinguishes getting a shape into the predictive model from getting it into
  preferences. The article carries both halves. Held.

Two correctness traps from the brief, pushed on hardest:

- The RLHF/value-fluency trap. The piece does not present preference learning as
  a clean refutation. It reports Barnett's claim, then names the boundary through
  Barnett's own disclaimer and Yudkowsky's predictive-model-vs-preferences reply,
  and states plainly that the critique answers "only half of it." The section
  heading itself — "Today's models can describe our values without wanting them"
  — carries the distinction. Trap named, not fallen into.
- The Bostrom citation (s4). Opened s4 as printed: it resolves to the Oxford
  University Press catalog page for *Superintelligence*, which carries no chapter
  text and no perverse-instantiation passage. The researcher could not open the
  book and worked from two secondary reproductions (Danaher; the LessWrong
  reading group). I judge the book citation acceptable as the idea's owner: the
  href resolves to the book itself, the article quotes nothing from Bostrom and
  only paraphrases, and the paraphrase is independently corroborated by the two
  reproductions in the evidence record. This is the first resolution the
  review-brief authorizes. No verbatim Bostrom claim reaches the reader, so
  nothing here needs the passage the catalog page lacks. No change; no routing.

data-nb-kind audit: s2 secondary, the other seven primary. Each source owns the
claim it is cited for (Yudkowsky's posts, Bostrom's book, the four empirical
papers/blog, Barnett's post and Yudkowsky's reply in its thread). No mislabel and
no hidden missing-independent-source. The four Background cross-links
(orthogonality, goal-misgeneralization, reward-hacking, mesa-optimization) all
resolve in the published library. No broken central claim, no evidence gap.

## Cut

The prose sits close to the voice guide's register already, so the cut was
narrow. One sentence failed the slop test outright and was removed; two carried
briefing language and were rewritten to the article's own terms; one furniture
markup error was corrected.

- Removed a signpost that also broke the lesson template's rule that only the
  bookends refer to the lesson: "This is where the lesson has to be careful,
  because a trap sits inside that objection." It graded the argument instead of
  advancing it, and the paragraph is stronger springing the trap through
  Barnett's own disclaimer than announcing it. Delete test: the following
  sentence carries the content unaided.
- Rewrote the present-day opener, which lifted the series prompt's instruction
  ("Bring the argument to the present") and the commission's own sentence
  ("imperfectly but ... aligned to messy human preference ... the strongest form
  of the argument did not obviously predict"). Recast in the article's terms
  around the sourced fact (models answer ethical questions about as sensibly as a
  person) that leads into Barnett. The point underneath is Barnett's and is kept.
- Rewrote "the side of the series' line where something has actually been shown,"
  which named the desk's method rather than reporting. Replaced with the shown-
  versus-projection contrast in the article's own words.
- Corrected furniture markup: the body rendered the model's utterance as
  `<code>What's 6?</code>`, but a quoted dialogue line is not a literal string to
  type or match, and the summary table already renders it as a quotation.
  Harmonized the body to `<q>What's 6?</q>`.

Edges, headings, and dek checked against the recent record. The dek is a single
subject-verb claim with a concrete image, not the two-clause "and/but" default
and none of the three banned molds. The present-day section is named in the
piece's own nouns, avoiding the desk's recurring "Who makes the case now" closer.
The shown-versus-projection spine is present, as sanctioned, but the headings and
dek do not echo the neighboring safety pieces. No formula found. The one note
(Yudkowsky's smiles quote) and the one pull quote each do deliberate work; the
table is the right form for three near-misses of one shape. No furniture is
decorative.

## Reader

Read straight through as the declared reader — sharp, widely read, new to how
alignment researchers reason — the piece leaves me able to state the argument at
full strength, see the three near-misses and that each was caught cheap, know
that the researchers who ran them call the leap to catastrophe speculative, and
hold the one distinction that keeps the strongest objection from settling the
matter: describing values is not wanting them. What I have beyond the sources is
their convergence: three independent strands laid on one seam, so the argument's
whole remaining force sits in a single untested region. No source assembles that.
The draft-handoff's original-work sentence claims exactly this synthesis, and it
survives the read. The prose sits closer to the voice-guide exemplars than to a
median summary: plain claims, worked concrete cases, the shown/projected line
held sharp, and a cool verdict that inflates in neither direction. The headline,
read as the largest claim, is earned and kept conditional ("can miss by
everything"), matching the takeaway's "neither proven nor refuted."

## Edits

- Rewrote the present-day section opener to drop lifted series-prompt and
  commission language while keeping the sourced Barnett lead-in.
- Cut the signpost sentence "This is where the lesson has to be careful, because
  a trap sits inside that objection."
- Rewrote "the side of the series' line where something has actually been shown"
  as the shown-versus-projection contrast in the article's own terms.
- Changed `<code>What's 6?</code>` to `<q>What's 6?</q>` in the Gopher paragraph
  to fix the literal-string markup and match the table's rendering.

## Required work

None. All findings were editor-fixable and are fixed. The proof runs BLOCK 0 /
WARN 0 / PUBLISHABLE after the edits.

## Decision

Approve. The argument is steelmanned fairly, both correctness traps are handled,
every citation resolves and supports its claim, and the four edits removed the
briefing residue and one markup error without touching the reporting.

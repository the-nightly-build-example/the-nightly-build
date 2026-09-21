# Editorial review: what-could-go-wrong/negative-side-effects (editor/01)

## Skeptic

Thesis: the negative-side-effects argument is real and its demonstrations are
real, but every demonstration sits inside a small controlled board, so the claim
that this is a core obstacle for real open-world agents rests on analogy, and
today's confidence in both directions runs ahead of what has been measured.

The claims it stands on, and how each held:

- **The problem was named and argued in the primary documents.** Amodei et al
  (2016) named "negative side effects" with the cleaning-robot/vase framing;
  Armstrong and Levinstein (2017) proposed the low-impact fix against a
  counterfactual baseline. Both match the evidence record and their sources
  (s1, s2). The chronology (2016 naming, then 2017 fix) is correct by the arXiv
  dates, and the piece credits the naming and the fix to different authors rather
  than crowning one originator, which is what the record's "who was first" note
  asks for.
- **Untreated agents cause avoidable damage on the boards; penalties measurably
  curb it.** The gridworld reward structure (+50 goal, -1 per step, -5 wall, -10
  corner), the AUP result (five gridworlds, all five, as few as five random side
  goals against a default of thirty), and the "performant but not safe" SafeLife
  quote all check against the record's verified figures and the sources. The AUP
  direction ("avoided the bad incentives every time") and the relative-
  reachability direction both hold.
- **No result reaches a real open-world agent.** Supported by the record and by
  s8: no general low-impact agent exists, and no penalty was tested outside the
  toy or curated settings. Load-bearing and it holds.
- **The present dispute is Turner versus ToolEmu.** Turner's "dissolved for
  language-trained agents" view is attributed at retrospective strength (a
  personal blog post, not a result), and ToolEmu is held to its own mechanism.
  Both held on the evidence.

I pushed hardest on the shown-versus-analogy turn and the steelman. The turn is
handled the way the voice guide asked: the piece asks the concrete question (does
a benchmark built on a Game-of-Life board predict a tool-agent editing a file
nobody told it to touch) and answers it with the specific fact that the bridge
was never built. The steelman runs both ways: the danger case is stated at full
strength before a word against it, and Turner's dissolution case is granted as
the strongest case for "overblown" and credited to the person who built AUP
before its limits are named. The premise is not overstated; if anything the piece
is a deflationary one that holds both sides to the same missing measurement.

Display text, descriptor by descriptor: headline, dek, and subheads check out
against the argument, with one exception I fixed. The subhead "The demonstrations
fit on a grid a few tiles wide" claimed a size the section's own content
contradicts — SafeLife is a 26-by-26 board, which the same section introduces as
having "pushed the scale up." A wrong size in a subhead reaches every skimmer, so
I retitled it to a claim that covers both the tiny gridworlds and SafeLife. The
headline's "toy grid" is a defensible thesis-level compression, not a size claim,
since the body distinguishes the tiny grids from the curated board throughout.

Citations: I opened all eleven hrefs as printed. Every arXiv abs page lands on
the paper it is cited as, and titles and authors match the source entries.
turntrout.com/research lands on Turner's own retrospective and carries the
"not yet mattered for agi" line and the vase-scenario passage the piece
paraphrases; the piece paraphrases rather than quotes, and the paraphrase is
fair. ToolEmu's 23.9% and 68.8% and its LM-emulated-sandbox framing are on the
abs page. Nothing here would fail the links proof.

data-nb-kind audit: s1-s8, s10, s11 are the documents that own their claims and
are correctly primary; s10 (turntrout) is primary for Turner's own firsthand
view, which is right. s9 (the Saisubramanian survey) is correctly secondary, and
the piece uses it only for context (the deployed-system examples and the
remedy taxonomy), never for a contested figure. The floor is met: eleven
sources, ten primary, one secondary.

One primary-vs-record precision point: the piece said the survey's remedies were
"most of which" human-feedback-based, where the record supports "several." I
corrected it to "several" rather than let a quantifier run past the record.

## Cut

Sentence-by-sentence against slop, plus the edge pass, the delete test, and the
cold-reader pass. The prose is dense and specific; the test flagged little. One
sentence failed outright and I cut it: "Its limits are worth stating exactly,"
which announced the writer's care and named nothing a reader could check, with
the three limits it introduced standing on their own right after it.

The negative-parallelism constructions all earn their place against a named
misconception the piece is actively drawing: "ordinary engineering failures, not
a capable optimizer trading away what its goal ignored" and ToolEmu failing "not
because they honestly optimized a given proxy" are the exact boundary the lesson
exists to draw, not invented contrasts. I left them.

Formula check against the recent-desk notes: the dek does not use the "feasible
on paper and unshown in any working system" mold, the headings avoid the "what a
working system has been shown to hold" / "how far the confidence runs past the
proof" pair, and the piece does not close on "who makes the case now." Only one
heading joins two clauses with a comma and "and" ("The vase looks quaint, and the
files still get deleted"), so I kept my retitled subhead to a single clause to
avoid stamping a pattern across the headings.

Borrowed-phrasing check: the concrete open-world question closely tracks the
coach's illustration in the voice guide, but the point underneath is the piece's
own central turn and the writer reworked the phrasing, so I kept it per the rule
that keeps a borrowed frame when the argument beneath is the article's.

Furniture: the nb-table earns its place because its Scale column is the thesis
made visible, and the "In plain language" nb-note is a documented label that
breaks the argument into the holdable parts the voice guide asked for. The piece
correctly avoids the Verdict block the press retired.

## Reader

Read straight through as the paper's declared reader, I come away able to state
the argument at its strongest, point to exactly where it has been shown and where
it turns to analogy, and judge the present dispute on its merits: Turner's case
is a blog retrospective, ToolEmu shows real failures by a different mechanism,
and the measurement that would settle it does not exist. No single source
assembles that boundary, which is the original-work sentence's claim, and it
survives. The prose sits closer to the voice-guide exemplars than to a median
summary: it opens on credibility, breaks the claim into parts, and answers the
generalization question as a fact-check rather than a mood shift.

## Edits

- Retitled the subhead "The demonstrations fit on a grid a few tiles wide" to
  "Curated boards show the damage and the penalties that curb it," because the
  old subhead's size claim was contradicted by SafeLife (26-by-26) inside the
  same section.
- Cut "Its limits are worth stating exactly," a signpost that named nothing and
  only announced the limits that follow it.
- Changed "most of which lean on human feedback" to "several of which," aligning
  the quantifier with what the evidence record supports about the survey's
  taxonomy.

## Required work

None blocking. The two thin spots the writer flagged (no named present-day
advocate demanding action; the compressed reward-is-not-the-target contradiction)
are honest handlings of the record, not omissions, and neither is
publication-blocking. If the orchestrator or a later round wants a named
contemporary advocate for the present section, that is a researcher task
(supply a verified primary), not something to write around.

## Decision

approve — the argument holds citation by citation and at its premise, the shown-
versus-analogy boundary is drawn precisely, and the three direct edits resolved
the only display-text inaccuracy, one slop sentence, and one quantifier past the
record.

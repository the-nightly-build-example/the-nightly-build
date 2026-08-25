# Editorial review: the-instruments/bfcl (editor/02)

Confirming read after a single-owner repair. The only change since editor/01 is
the secondary-source citation fix (writer took researcher option b). This review
confirms the one blocking item and re-runs the slop and display checks on the
changed sentence and its paragraph only. Settled matters from editor/01 (the dek
label, the s7/s8 overhaul split, the furniture, the closer, the banned-term
counts) were not reopened, and no new standard was introduced.

## Skeptic

The thesis and its supporting claims are unchanged from editor/01 and were not
re-litigated. The repair touched exactly one citation relationship, so the check
was scoped to it.

**The editor/01 blocking item is resolved.** editor/01 routed the framing
sentence because its lone secondary (Emergent Mind, then s5) was cited for a
single-turn-strong / multi-turn-weak "stumble" framing that three firsthand
reads could not find on that page. The repair moved the framing's citation off
the secondary entirely and onto the primary that owns it, and moved the
secondary onto a claim it genuinely supports.

- *The framing now rests on the primary.* The sentence "The board's results show
  the same shape: the top models ace the one-shot questions and stumble once they
  must remember context, manage a long conversation, or decide not to act" now
  cites s1 only. I opened s1's href as printed
  (`https://proceedings.mlr.press/v267/patil25a.html`): it resolves to the ICML
  2025 / PMLR v267 BFCL paper (Patil, Mao, Yan, Ji, Suresh, Stoica, Gonzalez),
  and its abstract states the framing in the source's own words — "while
  state-of-the-art LLMs excel at single-turn calls, memory, dynamic
  decision-making, and long-horizon reasoning remain open challenges." The
  primary genuinely carries the single-strong / multi-weak shape the sentence
  asserts. The writer also recast the subject from "An outside overview of the
  board lands on the same shape" to "The board's results show the same shape," so
  the sentence no longer claims independent corroboration it did not have. The
  claim itself is unchanged; only the subject phrase and the citation moved.

- *The secondary is now cited only for what it supports.* Emergent Mind (now s4,
  secondary) is cited in the grading section for the five single-turn category
  types. I opened its href as printed
  (`https://www.emergentmind.com/topics/berkeley-function-calling-leaderboard-v4-bfclv4`):
  it lands on the source and lists exactly those five — Simple, Multiple,
  Parallel, Parallel Multiple, Relevance Detection. The same read confirms the
  page describes multi-turn work as improving ("now improved significantly"), not
  as a stumble, which is precisely why moving it off the framing claim and onto
  the category-structure claim is the honest fix. The primary v1 blog (s3) owns
  the five types and is cited alongside; the secondary corroborates a fact the
  primary owns, which is a legitimate secondary use.

**data-nb-kind honesty and the composition floor.** Eight sources: s1 s2 s3 s5
s6 s7 s8 primary, s4 secondary. Seven primary, one secondary. Each label matches
the source's authorship-and-stake. Emergent Mind is a third-party aggregator, not
the Gorilla/UC Berkeley owner, so "secondary" is correct. The single secondary is
used once, for a claim it supports, and the >=1-secondary composition floor holds
with exactly one legitimate secondary. No label hides a missing independent
source.

**First-citation order preserved.** The renumbering (Emergent Mind moved earlier,
to s4; the v2-Live blog became s5) keeps body first-citations strictly ascending:
s1 (orientation, 66.4%), s2 (live-board note), s3 (three grading ways), s4 (five
single-turn shapes), s5 (2,251 live set, AST-only), s6 (tau-bench), s7 (v3/V4),
s8 (metric overhaul / changelog). No out-of-order first citation.

**Citation placement on the changed paragraph.** The chaining paragraph now cites
s1 on both the memory-collapse sentence (s1 Table 1 owns the near-zero agentic
memory cells) and the framing sentence (s1 abstract owns the paired shape). Both
sit on the primary that genuinely supports each. Correct.

No new break found. The claim set was not expanded and no figure, name, date, or
quotation was altered.

## Cut

Slop and display checks were re-run on the changed sentence and its paragraph
only, per the brief.

- **The changed framing sentence.** Placeholder test: what survives after the
  subject nouns are removed does not stand on its own — the sentence is carried by
  its specifics (one-shot questions; remember context; manage a long
  conversation; decide not to act). It reports an empirical shape, not a fillable
  pattern. It also survives the delete test: it is the only place the paragraph
  states the single-turn-strong half of the contrast plainly and enumerates three
  distinct multi-turn failure modes broader than the preceding sentence's
  "memory" alone, and it is the antecedent for "the split" in the sentence that
  follows. It stays.
- **"show the same shape."** I considered whether the recast subject reads as an
  empty self-referential transition now that the "outside overview" framing is
  gone. It does not rise to a blocking fault: the colon immediately supplies the
  shape's content, the sentence carries the paired contrast and the three named
  failure modes, and it is grammatical. It is a minor residue of the repair, not a
  new slop violation, and editing it further would risk touching a claim that is
  now correctly sourced. Left as written.
- **No new formula or leak.** The recast subject is none of the flagged molds
  (not the takeaway directive mold, not the the-instruments closer mold, not
  "number that matters most" / "worth knowing" filler, not a dek mold). It is not
  a closer or a heading. No planning label, selection rule, or
  assignment-fulfilled claim was introduced.
- **Banned terms and punctuation on the changed paragraph.** Em-dashes: 0. No
  en-dash, no "leverage" or "load-bearing," no negative-parallelism construction
  added by the repair. The grading-section sentence that gained the s4 citation
  ("The single-turn cases come in five shapes...") is an unchanged factual
  enumeration; adding the corroborating secondary did not alter its prose.
- **Display text.** No headline, dek, subhead, or caption changed in the repair.
  The dek retains editor/01's corrected "mostly reflects single calls." Display
  checks stand as in editor/01.

No sentences cut; none failed the slop test, and the changed sentence carries
weight.

## Reader

Unchanged from editor/01. The piece still gives the reader a job-by-job account
of what a function-calling number measures (one call, graded faithfully) and what
it never reaches (chaining, recovery, memory, declining to act), bound to the
tau-bench collapse and BFCL's own answer-key rewrites. The repair strengthened
the sourcing of the one sentence that carried this shape without a genuine owner:
its truth now rests on the primary the article already leaned on in the same
paragraph and in the authors'-limit note. The original-work assembly survives.
The prose sits closer to the voice-guide exemplars than to a median summary.

## Edits

None. The single-owner repair resolved the routed item cleanly; the article needs
no further editing.

## Required work

None. The blocking item from editor/01 is resolved and no new item was found.

## Decision

approve — the framing sentence's truth now rests on the primary (s1, the ICML
paper), whose abstract carries the single-strong / multi-weak shape in its own
words; the lone secondary (Emergent Mind, s4) is cited only for the five
single-turn category types it genuinely supports; both changed hrefs land on
their sources; data-nb-kind is honest (7 primary / 1 secondary), the
>=1-secondary floor holds, first-citation order is preserved, and the changed
sentence and its paragraph clear the slop and display checks with no new formula
or leak.

# Editorial review: the-instruments/superglue (editor/01)

## Skeptic

Thesis: the single SuperGLUE leaderboard number is a constructed measurement, not
a fact about ability, and the January 2021 "AI beats humans" crossing survives only
as the narrow, sourced claim its own builders made. The article stands on four
claims.

1. The leaderboard number is an equal-weight average of eight tasks scored in three
   different metrics, so "one number" hides a weighting choice. Verified against the
   owning primary (SuperGLUE paper 1905.00537). The article quotes the aggregation
   rule verbatim and proves the stakes with an honestly-invented two-task example: a
   five-point swing (75 vs 70) that traces to the averaging rule alone, before any
   task result changes. The example holds arithmetically and is labeled as invented.
   Claim stands.

2. The 89.8 human row is itself a measurement: five Mechanical Turk workers per item,
   majority vote, up to 30 practice items, $23.75/hr. Verified against 1905.00537
   Appendix C via the evidence record. The per-task table (BoolQ 89.0 to COPA/WSC
   100.0, MultiRC EM 51.9) is reproduced correctly and shows the spread the single
   label conceals. Claim stands.

3. The crossing precision. This was the load-bearing check. The article says a single
   DeBERTa model (1.5B) scored 89.9 against the 89.8 human macro-average and that its
   authors called it the first *single* model to cross, "in terms of macro-average
   score"; that a Google ensemble (T5 + Meena) at 90.2 had already cleared the row;
   and that the DeBERTa ensemble at 90.3 topped the board. It states plainly: "DeBERTa
   was the first single model over the line. It was not the first system to cross it,
   and its own authors never claimed otherwise." Every figure (human 89.8, T5 89.3,
   DeBERTa single 89.9, T5 + Meena 90.2, DeBERTa ensemble 90.3) matches the owning
   primary in the evidence record. The single-vs-ensemble distinction is exactly the
   correction the record demands and the flat "first to beat humans" is avoided. Claim
   stands.

4. The builders capped the claim in the same week the public uncapped it. The DeBERTa
   caveat ("by no means reaching the human-level intelligence of NLU") and Bowman's
   quote (the benchmark can no longer "detect further progress... beyond a small
   remaining margin") are quoted verbatim and correctly attributed. The section assigns
   the unqualified "AI beat humans" framing to the coverage step, not the builders,
   with each party's role stated first. Claim stands.

I opened all eight citation hrefs as the article prints them. Every one resolves to
its own source and the content matches what it is cited for: the three arxiv primaries
(1905.00537 SuperGLUE, 2006.03654 DeBERTa, 1910.10683 T5, 1804.07461 GLUE), the
Microsoft blog (89.9 vs 89.8, the caveat, dated 6 Jan 2021), VentureBeat (two models
named, "nearly 20-point" launch gap, the Bowman quote), and SyncedReview ("for the
first time, a new model surpassed human baseline performance," no body caveat — the
critical note is only in a comment, exactly as the article says). Source 8, the live
leaderboard, is the artifact the article deliberately examines and openly reports as
returning only a client-side shell; it is the standing exception to the resolve rule.
The two Go-deeper links (2104.02145 Bowman & Dahl; 1803.02324 Gururangan et al.) and
the internal Background link both resolve; the Background link text matches the
published GLUE lesson's exact title. GLUE is linked at first use in the body and in
Background, never re-taught. `data-nb-kind` labels are correct: the two trade-press
reports are secondary, the papers and the Microsoft announcement primary. No number,
name, date, or quotation needed routing; nothing broke against its primary.

## Cut

One dedicated slop pass over every sentence, then the edges alone, then the
cold-reader and delete tests.

The required structural fix: the body closed on a `nb-note-strong` "Verdict" block
that restated the finding (the three entries, what survives, what does not). Both
`press/editorial.md` and the paper's template make the takeaway bookend the one place
a lesson lands its judgment, and name the body Verdict block a leftover from the
paper's earlier template. The takeaway already carries this judgment in full — first
single model survives, first system does not, human-level understanding does not, plus
the three questions — so the block was pure restatement. Cut it. The section now closes
on the specific reporting sentence about coverage dropping the qualifier, which is a
stronger body ending and lands the "who is responsible" point the section builds.

Three self-reference / method-narration failures, which the body register forbids
(only the bookends address the reader or name the lesson):

- "this record does not re-run that check on each of the eight; the earlier lesson
  does" — recast to a claim about the number itself ("a single averaged number cannot
  show whether any one of them is being lifted that way"), keeping the shortcut point
  and the pointer to the GLUE lesson without narrating the article's own method.
- The sourcing paragraph's "every tool available for this lesson got back only its
  HTML shell" and its closing self-grading sentence ("it is what this record supports")
  — trimmed to a plain account of what the numbers rest on. The voice guide's
  honesty-about-the-reconstruction move survives; the newsroom narration does not.
- The builders-section opener "Assign the responsibility where the record actually
  puts it" — a reader-facing imperative plus "the record" self-reference — recast to a
  plain declarative that still sets up the caveats.

One punctuation and one grammar repair in the table caption: a semicolon where a
period is the plainer mark, and "depending which" corrected to "depending on which."

No borrowed phrasing from the voice-guide exemplars survived into the draft. No prompt
leakage: the commission's reader-situation sentences are not lifted, and the
selection-rule language stays out of the prose. Edge sentences (openers and closers of
every paragraph, section, and the article) each carry a fact or a reasoning step; none
is an empty signpost. Headline, dek, and headings break the flagged recent patterns:
the headline is a specific, defended finding in the piece's own nouns rather than
imo-gold's "same number, two readings" shape; the dek is a ", after" construction, not
the banned ", and"-twist or comma triad, and makes a claim about the world rather than
grading the article's method; the closing body heading is "What the builders said the
same week," not the recurring "Where X still Y." Furniture earns its place: the stat
strip carries the five load-bearing numbers, each cited nearby; the table shows the
per-task spread; the caveat note and position card give the builders' words their
weight.

## Reader

Read straight through as the paper's declared reader, I come away with what no single
source hands me: that the leaderboard number is an equal-weight average across eight
differently-metered tasks (shown, not asserted, by the two-task swing), that the human
row is a briefly-trained crowd's measurement spanning 51.9 to 100.0, and that the
famous crossing was precisely the first *single* model over a line an ensemble had
already cleared, capped by its own builders. I leave with three questions I can put to
any "beats human baseline" headline. The draft-handoff's original-work sentence — the
single-vs-system reconstruction and the invented worked example — is exactly what the
finished piece delivers; both answers survive. The prose sits closer to the voice-guide
exemplars than a median summary: it states constructions plainly and early, builds one
honest worked example, states each party's role before assigning the overclaim, and
stays skeptical of its own reconstruction. The headline, read as the largest claim, is
narrower than the whole lesson but is accurate, surprising, and defended in the body.

## Edits

- Cut the body-closing `nb-note-strong` "Verdict" block; the takeaway bookend already
  lands the judgment and press voice bars a body Verdict that restates the finding.
- Recast "this record does not re-run that check... the earlier lesson does" to "a
  single averaged number cannot show whether any one of them is being lifted that way."
- Trimmed the sourcing paragraph: removed "every tool available for this lesson" and
  the self-grading closer; kept the disclosure that the numbers rest on the DeBERTa
  table, Microsoft's dated reproduction, and two same-day reports.
- Recast the builders-section opener from "Assign the responsibility where the record
  actually puts it" to "The people who produced the 89.9 said themselves what it did
  not mean."
- Table caption: semicolon to period, and "depending which one you read" to "depending
  on which one you read."

## Required work

None. Every blocking item was an editor fix and is done. No evidence gap, broken
central claim, or source-policy failure to route to researcher or writer. Re-stamp and
the proof are the orchestrator's per the brief.

## Decision

approve — the crossing precision and every figure check out against their owning
primaries, all citations resolve, and the one blocking issue (a leftover body Verdict
block) plus the self-reference and punctuation faults were fixed in place.

# Editorial review: when-ai-breaks/clearview-ai (editor/01)

## Skeptic

Thesis: Clearview built a face-search engine by scraping billions of public
photos into biometric codes and selling it to police; regulators across many
countries found the practice unlawful, yet those findings have not stopped the
scraping or cost the company much, and the one point every regulator agreed on
is that nobody in the database consented to be there.

The four claims it stands on, and how each held:

1. Scale, and that the scraping never stopped. OAIC "more than three billion"
   (Nov 2021), Garante "over ten billion" (Feb 2022), UK FTT "over twenty
   billion" (Oct 2022), Dutch DPA "more than thirty billion" (2024). I opened all
   four owning sources: the OAIC page, the FTT judgment, and the Lewis Silkin and
   Hunton reports each carry their figure and date exactly as printed, and the
   chart plots the same four points against a labelled zero-based axis (see
   Chart). Company self-reports "in the forties" are correctly flagged as
   unverified. Held.

2. The same unlawfulness finding in five countries (Australia, Italy, Greece,
   France, Netherlands) on the biometric-data / no-lawful-basis / no-consent
   grounds. Verified against each owning source. Falk's quoted sentence matches
   the OAIC page verbatim; the CNIL "intrusive character... lack of awareness"
   quote and the Greek "lawfulness and transparency" quote match their sources;
   the five-row table's dates, penalties, and bases each check out. Held.

3. Found unlawful is not the same as paid or enforced. The UK £7.5m (TechCrunch,
   May 2022) set aside by the FTT on jurisdiction (Oct 2023), reinstated by the
   Upper Tribunal (Oct 2025, "erred materially in law", remitted to decide the
   merits). I opened the FTT and UT judgments: both support the article exactly,
   including the load-bearing "not because the collection was lawful but because
   [jurisdiction]" distinction. The EU fines are honestly framed as findings of
   law with little collected (no EU establishment; France's €100k/day tell), and
   the Illinois settlement as limiting sales, not deleting the database. Held —
   with one break inside it (below).

4. A verification score sold as identification. The 99%+ is Clearview's reported
   NIST FRVT 1:1 result (visa 99.81%, mugshot 99.76%, "an unmistakable
   validation"), not the 1:many identification the product performs, and no
   independent 1:many test on the scraped database exists in the record. The
   Clearview NIST page, the OAIC accuracy finding, and the Techdirt NYPD/75%
   material all support the section as written. The distinction is drawn from the
   evidence record and is the article's own synthesis. Held.

Break found (source policy). One sentence in the enforcement section — "According
to the Commissioner, Clearview has since been granted permission to appeal once
more, to the Court of Appeal" — carries citation 9 (the Upper Tribunal decision
page, gov.uk). I opened that page: it is the Oct 2025 UT judgment and contains
nothing about a later Court of Appeal permission. The evidence record attributes
this fact to the ICO, reported ~December 2025, from a page the researcher could
not open (ico.org.uk returned 403), and the draft-handoff itself records the fact
as "per the ICO." So the printed citation does not own the claim, and no source
in the record openably supports it. The claim is nonessential (the paragraph's
"the £7.5 million has never been paid... only on who holds the power to make
them" stands without it), but the brief wants the "further appeal pending" nuance
represented, so I route it for a real source rather than cutting it outright. The
right source is not at hand, so I cannot re-cite it myself.

Every other citation href was opened as printed and resolves to the source that
owns its claim (OAIC, HDPA, FTT, UT, ACLU-IL, ACLU, both Clearview press pages,
TechCrunch, Techdirt, Lewis Silkin, both Hunton reports). All `data-nb-kind`
labels match the evidence record; the party sources (Clearview, ACLU) are
correctly primary for their own statements and actions and used only for those.
Source floor met (8 primary, 5 secondary).

## Cut

Two direct cuts, both small; the draft was already clean of slop at the middles
and mostly at the edges.

- Orientation, para 3 closer: removed the hollow announcement "and one fact
  stands out:" ahead of the real claim. The signpost graded the comparison the
  chart already makes; the claim it introduced ("the scraping never paused for
  any of the rulings against it") does the work and now carries the sentence on
  its own. The voice-guide's "set the facts side by side" framing is kept.
- Regulators, defense para: "No source in this record, the company included..."
  → "No one, Clearview included..." The old phrasing leaned mildly inward ("this
  record") for a point that is stronger stated flatly, and the fact (nobody,
  Clearview included, claims consent) is exactly what the evidence record
  establishes.

Slop / formula sweep, nothing else cut. The three "not X but Y" constructions
(the FTT jurisdiction point, "not about what happened... about whether a photo
being public makes it free to take", "who Clearview may sell to, not what it may
collect") each correct a real, named misconception and are earned, not reflex.
The two lesson bookends address the reader as the template allows, and each says
something particular to this lesson: the opener poses the enforcement question,
the takeaway resolves it on "Public did not mean permitted", not on the desk's
stamped "the failure still ships" closer. No borrowed Kashmir Hill phrasing: the
draft names Hill as the originating reporter but takes none of the voice-guide's
Hill wording ("grabbed", "document the problem", "a decade of contacts"). No
prompt leakage; brief-shared facts ("largely uncollected", "found... unlawful")
appear as reported facts, not lifted framing. Headings reconstruct the argument
in the piece's own nouns and vary in construction. Grammar and punctuation clean;
no em-dash reflex.

## Reader

Reading what survives straight through, as the paper's smart newcomer: I come away
able to say that a scraped-photo face-search business was ruled unlawful in
country after country and kept operating and growing anyway, because a finding of
unlawfulness is not a collected penalty, and that its marketed "99%+" measures a
different task (1:1 verification) than the 1:many search it sells, which no
independent test has scored. Neither point is available from any single source;
the article assembles them. That matches the draft-handoff's original-work claim,
and it survives. The prose sits closer to the voice-guide exemplars than to a
median summary: plain verbs, each term of art glossed in the sentence that
introduces it, figures set side by side and verdicts held until earned. The
headline reads true as the largest claim.

## Chart

`chart-1.png` and its committed `chart-1.py`: four discrete bars (3, 10, 20, 30
billion) at Nov 2021 / Feb 2022 / Oct 2022 / May 2024, each labelled with its
owning authority (OAIC, Garante, UK tribunal, Dutch DPA). Numbers match the
evidence record and the primaries I opened. Read as a reader: zero-based
y-axis labelled "Images in the database (billions)", value labels on each bar,
x-axis names the date and the source, discrete bars (not a connected line) so the
chart asserts nothing about the dates between counts — the figcaption says as
much. Honest. One minor inconsistency to reconcile (writer): the chart dates the
Dutch fine "May 2024" (decision date) while the article's table dates the same
fine "Sep 2024" (announcement date). Both dates are real and supported, but the
same event is dated two ways across the two components.

## Edits

- Orientation para 3: cut "and one fact stands out:" so the claim "the scraping
  never paused for any of the rulings against it" carries the sentence directly.
- Regulators defense para: "No source in this record, the company included" →
  "No one, Clearview included".

## Required work

- **researcher:** Supply an openable, citable source establishing that Clearview
  was granted permission to appeal to the Court of Appeal (reported ~Dec 2025) —
  the ICO's own statement or reporting of it — or confirm it cannot be sourced.
  Citation 9 (the Upper Tribunal page) does not contain this fact.
- **writer:** Once the source is provided, re-cite the "granted permission to
  appeal... to the Court of Appeal" sentence to it and remove citation 9 from a
  fact that page does not carry; if no source can be obtained, cut the sentence
  (the paragraph stands without it). Also reconcile the Dutch-fine date between
  the chart (May 2024) and the table (Sep 2024).

## Decision: revise

A cited claim (Court of Appeal permission) is carried by a source that does not
support it and no source in the record openably does; that reaches every reader
who clicks, so it must be sourced or cut before publication.

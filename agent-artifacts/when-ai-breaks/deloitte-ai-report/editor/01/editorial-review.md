# Editorial review: when-ai-breaks/deloitte-ai-report (editor/01)

## Skeptic

Thesis: a government paid Deloitte A$439,142 for an assurance review whose whole
value was an outside firm's name on the finding, and the deliverable carried
citations a generative AI tool had fabricated -- a book that was never written, a
Federal Court quotation the court never gave, invented academic work -- because a
model builds a fake reference exactly as it builds a true one and no one opened a
single source to check. The claims it stands on: (1) the fee and the engagement,
(2) the specific fabrications in the 4 July report and what the 26 September
correction did with each, (3) the buried AI disclosure, (4) the refund and its
scope, (5) the mechanism.

I verified every figure, date, name, title, and quotation descriptor by
descriptor against the owning primary, opening each of the eleven citation hrefs
as printed plus the two Go-deeper links.

- Fee A$439,142.00: confirmed against the AusTender contract notice CN4118426
  itself (Deloitte Touche Tohmatsu, DEWR). Primary, exact.
- The dated timeline (contract Dec 2024, report dated 4 July 2025, published 14
  Aug, corrected 26 Sep / published 3 Oct, further-corrected 3 Feb 2026):
  confirmed against the DEWR resource page metadata (both Archive snapshots) and
  the report front matter. The 3 Feb 2026 line and its `data-nb-url` land on the
  Feb snapshot, which carries the matching update note.
- The Amato quotation, real vs fabricated (pushed hardest here): the article's
  `nb-note` blockquote is verbatim from the 4 July PDF -- "her Honour Justice
  Davis stated at [25]-[26]: The burden rests on the decision-maker..." I read the
  July Amato box (p.~57) and confirm the fabricated heading "[2021] FCA 1019",
  footnote 57 "[47]-[50] (Davies J)", the body misspelling "Justice Davis", and
  the "[25]-[26]" and "[30]" locators. Critically, the article asserts none of
  those paragraph numbers as real: they appear only inside the quoted fabrication.
  The real record (Victoria Legal Aid, corroborated by the corrected report's own
  re-attribution to paragraph 9 of the consent-order notes, which I read on p.~58
  of the September PDF) is consent orders of Justice Davies, VID611/2019, 27 Nov
  2019. The article says "Justice Davies, not Davis... 27 November" and claims no
  paragraph number of its own. Clean.
- Fabrications table: each row checked against both PDFs. The Burton Crawford
  "Welfare State" book, the second "Administrative Discretion" book (fn 55), the
  Adams article (fn 14, replaced with a real one), the Regnell paper (fn 66,
  removed), the "Justice Natalie Cujes Perry" speech (fn 58, replaced with Justice
  Melissa Perry's real "iDecide" speech), and the Amato re-attribution all match
  the primaries and the correction.
- AI disclosure: confirmed verbatim on p.48 (Phase 3 methodology graphic) and
  p.147 (Appendix C) of the September PDF -- "Azure OpenAI GPT-4o... licensed by
  DEWR and hosted on DEWR's Azure tenancy." Both sit inside the methodology, not a
  cover or summary page. The dek's "named only in its methodology, never on a
  cover page" holds.
- Titles: Rudge ("Lecturer in Law, Sydney Law School, University of Sydney"),
  Burton Crawford ("Professor of Public and Constitutional Law at the University
  of Sydney Law School"), Regnell ("Professor in Software Engineering... LTH, Lund
  University") all confirmed on the cited pages.

One break, fixed. The article stated in its own voice, three times (the
`fabrications` heading, the body line after the table, and the takeaway triad),
that the book was "cited ten times." The owning primary shows that book cited in
six footnotes (48, 59, 82, 89, 101, 115) and the bibliography, not ten. "Ten" is
Rudge's secondary characterisation (The Nightly, s4, does report "ten
references"); the evidence record's own Contradictions note flags scale as
contested and says explicitly not to adopt either count as neutral fact. Primary
governs. I removed the unsupported count from all three own-voice positions
(de-quantifying rather than substituting, since setting the number is the
writer's call) and left Rudge's "roughly ten / close to twenty" intact where it
is attributed to him in the scale-dispute steelman. The article's own voice no
longer adopts a contested count as fact, which tightens the steelman rather than
weakening it.

Refund sourcing (pushed hard, per brief). The figure A$97,587.11 is owned by the
evidence record, which states it was confirmed through two independent accounts
but that Hansard was not read directly. The cited source, the Greens release
(s11, correctly marked secondary), reads "$97,587 (less than a quarter) of the
$440,000 contract" -- rounded, no cents. So the .11 precision exceeds what the
single cited public source prints; it rests on the record's cross-checked
accounts. This is within tolerance: the refund figure is uncontested (all parties
agree the amount; only its adequacy is disputed), secondary sourcing is
acceptable for an uncontested figure, and the article does not overstate the
*kind* of sourcing -- it attributes the confirmation to "officials... at a Senate
estimates hearing" and cites the release, claiming no primary or Hansard. Not a
break; recorded as an observation. The stat strip rounds to A$97,587, the prose
gives A$97,587.11 -- an acceptable convention.

Dek causal claim. "The fake citations came from a generative AI tool" states the
article's earned synthesis, not admitted fact. The disclosed AI use was in the
technical/traceability workstream, and Deloitte has published no post-mortem, so
the AI-to-citations link is inference from the disclosure plus the hallmark
pattern. The body steelmans this honestly (the fourth contested question, "the
cause... asserted by others rather than admitted"), and the commission frames the
incident as AI-fabricated citations. I let the dek stand: softening it would
weaken a claim the paper earns, and the body carries the epistemic care.

`data-nb-kind` audit. Five primary (s1 DEWR page, s2 AusTender, s5/s6 the two
report PDFs, s9 Victoria Legal Aid), six secondary (s3, s4, s7, s8, s10, s11).
s9 is labelled "primary-adjacent" in the evidence record; between the only two
available labels, "primary" is the correct choice for a litigant's verbatim
reproduction of the court's own consent-order language in a case it ran, and the
same language is corroborated by the corrected report, so the label hides no
missing independent source. s3/s7/s8 are people's own or authoritative profiles
used for titles only and are honestly marked secondary. s11 is secondary for the
refund figure (it repeats Senate testimony it does not own) -- the honest label.
All links open and land on the source; the four Archive snapshots resolve to the
exact page versions the claims rest on. Distinctness links (hallucination,
mata-v-avianca, galactica, robodebt, cnet-ai-articles) all resolve in the library
and are handled as one-line links, not re-tellings.

## Cut

The prose is disciplined. Sentence-by-sentence and edge-by-edge, few sentences
failed the slop test; the edits below are the substantive ones.

- Negative parallelism, one instance, cut. "The most consequential invention was
  not a missing book but a court that never spoke" uses the banned "not X but Y"
  reflex, and its "not" clause (a missing book) is a real prior finding, not a
  named misconception, so it fails the earned-contrast test. Recast to "Worse than
  any missing book was a court that never spoke," which keeps the escalation and
  the vivid close without the mold. A second "not X but Y" survives in the
  mechanism section ("not a demo and not one careless filing, but a paid
  deliverable") because there the "not" clauses are the two named precedents just
  linked, so the contrast is earned; left alone.
- Punctuation. Two prose semicolons, both joining a name/identity clause to a
  disavowal ("...University of Sydney Law School; she did not write..."). Per the
  editorial direction the period is the default for two thoughts; converted both
  to periods.
- Grammar. Two awkward "a A$..." articles (the `why` opener and the takeaway).
  Recast the opener to move the fee into its own short sentence, and the takeaway
  to "a refund of A$97,587.11."

Edges. The `fabrications` section closer ("Real academics had their names on
books and papers they never wrote. A Federal Court judge was quoted saying words
she never said. All of it sat inside a document the Commonwealth had paid a global
firm to get right.") reads as recap, but it is the section's earned landing in the
short-declarative register the voice guide praises and it re-lands the piece's
thesis (paid for trust, delivered fabrication); it states the conclusion the
section built, so it stays. The `today` opener ("a missing step") and the article's
last body line ("the person who signs the document is the last check") are
concrete enough and carry the lesson's conclusion; kept. The takeaway closer
("Anyone who commissions or signs AI-assisted work now owns that check") names the
recurring failure in the reader's own terms, as the series prompt asks; kept.

No prompt leakage: where the article names where the failure lives ("consulting
reports, legal filings, and the submissions governments commission and publish")
it reports the reader's situation, which the commission states plainly and which
is not a leak. No planning labels, selection rules, or assignment-fulfilment
claims survive. No borrowed phrasing from the voice-guide exemplars.

Furniture. The `nb-note` carries the fabricated quotation verbatim (the evidence
itself), well labelled; the stat strip pairs two heterogeneous headline numbers,
both cited nearby; the six-row comparison table is the right form for the
fabrication mapping and carries its citations in the caption. No overload, no
stack-of-blocks feel. No missed component: the dated sequence reads cleanly in
prose and does not need a timeline. No source asset is required -- the one visual
that would test the central argument, the fabricated Amato quotation, is already
present verbatim in the note, and the corrected language is quoted in prose.

Deks/headings against the recent record. The dek breaks the desk's comma-stacked
name+number+consequence habit (it is one claim with a short tail, not a clause
triad). Headings are argument steps in the piece's own nouns; the closer "Where an
unchecked citation gets in" shares a "Where..." opener with robodebt's closer but
differs in build and nouns, not a formula worth breaking.

## Reader

Reading only this article, a reader comes away able to say why an AI-generated
citation is built exactly like a real one and therefore cannot be trusted without
opening the source -- and they have watched that play out on a named, dated, paid
government deliverable, with the fabricated court quotation set beside what the
court actually said. That is more than any single source gives: it synthesises two
report versions, the contract notice, the court record, and the Senate-disclosed
refund into one mechanism-driven lesson. The draft-handoff's original-work
sentence (staging the fabrications inside the assurance promise, teaching the
mechanism on the spot, setting the invented Amato quotation against the real
consent-order language) survives contact with the article. The prose sits closer
to the voice-guide exemplars -- White's restraint, letting the quotation carry the
verdict; Greenberg's single clean mechanism pass -- than to a median summary. The
headline is a defensible largest claim: Deloitte, the fee, and "citing books that
don't exist," all of which the piece establishes.

## Edits

- `why` opener: recast "a A$439,142 Deloitte assurance report... cited a book..."
  to end the fabrication sentence and move the fee into a following short sentence
  ("The department had paid A$439,142 for it."), removing the awkward "a A$".
- `fabrications` heading: "A book cited ten times that was never written" ->
  "A book cited repeatedly that was never written" (removed the unsupported count).
- `fabrications` body: two semicolons -> periods (Burton Crawford and Regnell
  sentences); "the book cited ten times against her name" -> "cited repeatedly."
- `fabrications`: "The most consequential invention was not a missing book but a
  court that never spoke." -> "Worse than any missing book was a court that never
  spoke." (removed negative parallelism).
- `takeaway`: "a book cited ten times that does not exist" -> "a book that does
  not exist"; "a A$97,587.11 refund" -> "a refund of A$97,587.11".

## Required work

- **writer (non-blocking, precision):** the article now says the nonexistent book
  was "cited repeatedly." The specific beats the generic, and the primary supports
  an exact count -- footnotes 48, 59, 82, 89, 101, 115 plus the bibliography. The
  writer may restore a concrete, primary-owned figure (e.g. "cited in six
  footnotes") in the heading, the body line, and the takeaway. Do NOT reinstate
  "ten" as the article's own fact: that is Rudge's secondary count and it conflicts
  with the primary. "Roughly ten," attributed to Rudge in the scale-dispute
  steelman, stays as is.
- **writer (optional):** consider whether to align the refund's cents (A$97,587.11)
  with the cited Greens release, which prints the rounded A$97,587, or to add the
  account that carries the exact figure. Not blocking -- the figure is uncontested
  and owned by the evidence record.

## Decision

approve -- every figure, date, name, title, and quotation holds against the owning
primary, the one factual break (a contested secondary count asserted as fact) was
fixable and fixed by de-quantifying, and no publication-blocking work remains; the
proof holds at BLOCK 0 / WARN 3 (the three intentional controlled long sentences),
verdict PUBLISHABLE.

Production record: run as claude-opus-4-8 (Opus 4.8), effort=high.

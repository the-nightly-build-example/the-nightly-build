# Editorial review: when-ai-breaks/chicago-heat-list (editor/01)

## Skeptic

Thesis: Chicago's Strategic Subject List, a 0-to-500 risk score built from
arrest records to predict who would be a "party to violence," raised a listed
person's chance of arrest without changing their chance of being shot, because a
score trained on arrests learns policing rather than crime, carried almost no
help behind it, and aimed at an event too rare to predict. The piece stands on
five claims.

1. RAND's null-versus-arrest result. The listed group was no more or less likely
   to be shot or killed than matched controls and was 2.88 times more likely to
   be arrested for a shooting (9 listed vs. 5 matched). I checked each table cell
   against the evidence record's Numbers block: shooting-victim 0.80 (p=0.58),
   murder-victim 1.04 (p=0.96), shooting-arrest 2.88 (p=0.01), murder-arrest 1.57
   (p=0.33). All match. The hedges the guardrail names are all present and
   correctly owned by RAND: theory-versus-implementation failure left undecided,
   no violent backfire, may have identified more genuine offenders, later
   versions improved. The result is not flattened into "this class cannot work."
   Held.

2. Composition of the released list. 398,684 people, 287,404 above the 250
   scrutiny line, 127,513 with no arrest or shooting on record (~90,000 still
   high-risk), age explaining ~89% of score variance, 153 at the maximum 500 with
   20 never arrested for guns or violence. Each figure matches its owner (Upturn
   for the whole-list figures, Sun-Times for the top-of-list figures) and each is
   cited to that owner. Held.

3. Attribution of the racial-disparity claim — the round's sharpest risk. The
   85%-African-American-men figure is cited to the Sun-Times (s6) and the
   released dataset (s4); the 56%-of-Black-men-under-thirty figure is cited to
   Richardson, Schultz, and Crawford (s8), with the "under thirty" wording the
   Contradictions section requires and not the "20 to 29" phrasing no primary
   owns. The disparity is nowhere pinned on the OIG. Reliability, training, access
   control, and the punitive-intervention finding ("may have attached negative
   consequences to arrests which did not result in convictions") are all cited to
   the OIG (s1). Owners are correct. Held.

4. The mechanism. Arrests are a record of policing, not of crime; the DOJ found
   CPD's unlawful force fell disproportionately on Black and Latino residents in
   the same years the data was generated (s9); Richardson et al. supply the
   "cannot escape the legacies" argument (s8, quoted and attributed). The quote is
   verbatim to the record. Held.

5. The base rate and the present-day close. Homicide rate ~0.7% in the year after
   the pilot; 993 of every 1,000 highest-marked not killed (arithmetic checks);
   the model caught 3 of 405 homicide victims. The close rests on the EU AI Act
   Article 5(1)(d) prohibition in force 2 Feb 2025 (s10, quote verbatim, locator
   correct) and names no specific live US deployment, as the guardrail directs.
   Held.

Two writer-flagged items, checked:

- "Highest possible charges." The article renders this as plain paraphrase
  ("a department directive urging the highest possible charges"), not as a
  verbatim OIG quote, and attributes it to the OIG exactly as the evidence
  record's Contradictions section attributes it. It is not overstated as a direct
  OIG finding. Verified against the record; no change.

- The RAND table. It shows four outcome rows and omits the fifth "any weapon" row
  the source-asset note lists, because the Numbers block supplies no Exp(b) or
  p-value for that row. Nothing is invented; the four rows carry the
  victimization-versus-arrest finding intact. The one exposure the omission
  created was in the caption's "only the arrest effect was statistically
  significant," which could be read as a claim about the unshown row and was also
  imprecise about the two arrest rows actually shown. Fixed in the edit below.

Display text audited descriptor by descriptor. Headline, dek, and all five
section headings carry claims about the world, not grades of the article. The
headline's "arrested, not shot" contrast is RAND's real finding against the
list's stated purpose, so the negative construction is earned. Wernick's title is
generalized to "engineering professor," which the IIT primary supports. All ten
`data-nb-kind` labels match the record's classifications (8 primary, 2 secondary;
policy floor of 8 sources / 4 primary / 1 secondary cleared). All ten source
hrefs match the addresses the evidence record read in full. The three Background
cross-links and the two in-prose lesson links resolve in the library checkout,
and each Background anchor's text matches the linked lesson's actual title.

## Cut

Slop pass, every sentence including furniture and display text. The prose holds
the voice guide's register: concrete case first (the OIG's speeding-arrestee /
uncounted-shooting-victim pair), exact figures scaled to something the reader
holds, the failure walked as a chain. No borrowed clause from the guide's Luu,
Angwin, or McKenzie quotations. No prompt leakage: the commission's framing
phrases ("ranks individuals for police attention," "no effective intervention")
appear only as sourced description of the system, never as planning labels or
claims the assignment was met. Edge sentences read out of order hold up; the
closer ("Any system that ranks individuals for police attention out of their
contact history inherits both faults") states the earned generalization rather
than grading the piece.

One sentence failed the delete test: "Here the gap between the stand-in and the
goal had a documented shape" is a signpost whose "documented shape" is exactly
the abstraction the following DOJ sentence supplies. Cut. The takeaway's "None of
that was a malfunction... the scores meant what the design made them mean" states
the same design-not-bug idea as the optum lesson's dek, but in the SSL's own
enumerated choices rather than echoing that dek's wording; it earns its place and
stays. The dek is built in the SSL's nouns and avoids the desk's recent
comma-and-triad mold; headings read as argument steps with no scaffolding slot.

Two grammar/clarity breaks fixed directly (below). Word count sat one word under
the ceiling, so the trims came from a middle signpost and a wordy tail, not from
truncating any section.

## Reader

Read straight through as the paper's declared reader, what do I have that the
sources alone would not give me: I can now say why a crime-risk score built on
arrests necessarily ranks the already-policed, and I hold three questions to test
the next such system — what it was trained on, how rare the event is, and what a
high score buys a person. No single source performs that synthesis; the
draft-handoff's original-work sentence claims exactly this chain, and the article
delivers it in "Why the list found the already-policed." Both answers survive.
The prose sits closer to the voice-guide exemplars than to a median summary: it
commits to specific figures and owners and reasons to its verdict instead of
asserting it.

## Edits

- Table caption: "only the arrest effect was statistically significant" ->
  "only the shooting-arrest effect was statistically significant" (precise about
  the two arrest rows shown, and closes the reading that referenced the omitted
  fifth row).
- Proxy-label paragraph: repaired the broken tail "and carries in every way the
  two differ" -> "and it carries every difference between the two."
- Cut the signpost "Here the gap between the stand-in and the goal had a
  documented shape."
- Base-rate paragraph: "an accurate model turns out far more false alarms than
  hits" -> "produces far more false alarms than hits."
- Close: "The weakness the EU wrote into its statute" -> "The weakness the EU
  named in its statute" (the statute names the weakness; it does not write one
  in).

## Required work

None. No evidence gap, broken central claim, or reporting repair remains for the
researcher or writer.

## Decision

Approve. The attribution the round turned on is correct throughout, both flagged
items check out, RAND's hedges are intact, and the remaining issues were prose
and precision fixes I made directly.

# Editorial review: what-could-go-wrong/companion-dependency (editor/01)

## Skeptic

Thesis: the public argument over AI companions is not one dispute but two
correct descriptions of different populations — the dismissal accurately
describes the typical, mostly-teen user, and the alarm accurately describes
the heaviest, most disclosive user, and neither side has shown how many
people move from one group to the other over years rather than weeks.

Claims tested, treating headline, dek, and every subhead as a claim:

- **Headline** ("the best evidence... comes from OpenAI itself," as drafted):
  true and sourced — the evidence record itself calls the OpenAI/MIT RCT the
  strongest design in the file, being the only randomized one — but the
  sentence was built on the exact template of the published deskilling
  headline ("The strongest evidence that AI deskills people is a single
  colonoscopy study"): "The [superlative] evidence that [claim] is/comes
  from [one narrow source]." That is a formula recurrence spec/slop.md and
  spec/headlines.md both require checking the library for. Rewritten (see
  Edits) to name the actor and the actual strongest finding (emotional
  dependence, beta=0.06, p<0.001, the largest and most significant of the
  RCT's four outcomes) without the borrowed shape.
- **Dek**: holds. Turkle's dates, the "decade before" framing, and the
  concentration claim all check against the evidence record and the primary
  sources I reopened (Bill Moyers excerpt, TEDx transcript — both quotes
  confirmed verbatim on refetch). No banned dek mold.
- **"Sherry Turkle's warning predates the apps by a decade"**: holds. Her
  1966/2011 dates, both quotes ("choose keyboards over the human voice...it
  is more efficient," "digitized friendships...sufficient unto the day," "the
  illusion of companionship without the demands of friendship") confirmed
  word-for-word against the live Bill Moyers excerpt and TEDx transcript.
  Caveat honored: no page-cited "Alone Together" quote beyond these two
  confirmed sources.
- **"The clearest study measured how much people used it, not which version
  they got"**: holds against the primary RCT (arXiv 2503.17473, refetched):
  sample sizes, all four betas and p-values, and the "voluntarily spent...
  relatively worse" quote all match exactly. The company-stake caveat is
  honored in prose ("best read as OpenAI's own account of its product, not a
  neutral study") rather than treated as authority.
- **Central claim under the round's specific test** — that the alarm and the
  dismissal describe different populations, not the same one, hedged: I
  pushed hardest here. The "heaviest, most disclosive users" finding comes
  from adult samples (the RCT's recruits, Zhang et al.'s "US adult
  Character.AI users"), while the "typical user" side comes only from Common
  Sense Media's teen survey. The piece's synthesis paragraph originally
  paired "the typical teenager" against "the heaviest user" without flagging
  that these are different studies of different age populations, which
  slightly overstates how directly comparable the two halves are. This is
  real but not a broken claim: the argument is a pattern-level synthesis
  across studies that separately measure usage-intensity and population
  behavior (the evidence record's own Contradictions section makes the same
  point about incommensurable measures), not a claim about identical
  cohorts. Fixed by anchoring the claim to its actual source ("the typical
  teenager in that survey") rather than routing it back — the fix needed no
  new reporting.
- **Replika section**: the Garante order's date (Feb. 2, 2023), the
  age-verification and "developmental level" quotes, the €20M/4% penalty,
  and both Kuyda quotes and the Feb. 1 legacy cutoff all confirmed against
  the primary order (refetched) and both Vice pieces (refetched).
- **Regulatory section**: APA advisory quote, Prinstein's "gas pedal and weak
  brakes" line and Senate context, SB 243's "meeting a user's social needs"
  definition and three-hour disclosure rule, the FTC's seven named companies
  and 6(b)-inquiry framing, and Common Sense Media's under-18 recommendation
  all confirmed against primary documents I reopened directly (SB 243 text,
  Garante order, FTC release) or that match the evidence record's page
  locators for sources I could not re-render as text (the OpenAI PDF,
  Prinstein's PDF — both resolve, per link-check, but returned only binary
  PDF streams to the fetch tool).
- **Grammar break found and fixed**: "The more serious case is [link], after
  months with a companion chatbot preceded a 14-year-old's death" did not
  parse — a dangling clause with no grammatical attachment to "after." Fixed
  directly (see Edits); the two facts it carries (months of chatbot
  conversation preceding the death; the judge letting the suit proceed
  treating the chatbot as a product) are unchanged.

No claim was broken outright, no citation misattributed, and no evidence gap
required a researcher request.

## Cut

- Ran the delete test and the edge-sentence pass on every paragraph, section,
  and the article as a whole. Two sentences failed as self-reference/
  signposting under spec/slop.md and were cut outright, not repaired: "told
  below" (a forward-pointing structural signpost, banned outside the
  bookends) and the empty-conclusion chassis "That shift is itself
  evidence:" (matches spec/slop.md's own banned-pattern example, "That limit
  is itself part of the design," almost exactly) — the substantive sentence
  that followed each was kept and now stands on its own.
- Found a repeated negative-parallelism tic ("X, not Y") recurring four times
  across the piece (dek, a heading, the section-5 thesis sentence, and the
  takeaway). Each instance individually corrects a real, named misconception
  the piece establishes, so none is a strawman, but the takeaway's version
  ("Which group someone falls into, not which side sounds more confident...")
  nearly duplicated the section-5 thesis sentence two paragraphs earlier in
  both construction and content. Rewrote the takeaway sentence without the
  tic and without the restatement: "How worried you should be about someone
  depends on which of those two groups they belong to."
- Compared headings and the headline against the recent record (deskilling,
  recommender-radicalization, power-seeking-ai, pulled directly from the
  library). Found two formula recurrences beyond what the review brief
  flagged: the headline copied deskilling's "The [superlative] evidence that
  X is/comes from [one source]" mold exactly, and the regulatory-section
  heading ("What today's proponents are asking regulators to require") was
  a fresh instance of the "What [X] saw" mold the brief's own recent-pattern
  notes name. Rewrote both in this argument's own nouns (see Edits). Also
  converted "The studies run for weeks; the worry is about years" — a
  semicolon-reversal heading that also echoed power-seeking-ai's own
  two-sentence contrast closer ("The estimate went up. The premises did
  not.") — to a single declarative sentence in the piece's own terms.
  Confirmed the desk's other habits (opener triad, "gap on both sides"
  heading, comma-triad/semicolon dek) do not recur here; the shown-vs-
  speculated line and the gap section both already land on this argument's
  specific state rather than a symmetry.
- Checked every sentence-density warning the proof carried (4 W-SENTENCE-
  DENSITY, not 0 as the writer's own handoff implied a clean run against —
  the writer's draft-handoff mislocated all four, describing them as in the
  "why" bookend and the Replika paragraph; the proof tool's own tokenizer
  places all four inside the measured-outcomes and the-response sections
  instead). All four split cleanly with no clause duplicated and no quote
  broken, contrary to the writer's note that they "did not split cleanly."
  Also gave the Numbers section its due: "a correlation the authors call
  negligible" became "a correlation of just 0.1," the actual figure the
  record carries.
- Punctuation: no em-dash, semicolon, or colon count issues; the one
  semicolon-reversal heading is fixed above.
- No prompt leakage found: language throughout traces to reported facts
  (Turkle's own words, the studies' own findings, the regulators' own asks),
  not to the commission's or brief's framing sentences.

## Reader

Read straight through as the declared reader — smart, widely read, new to
this specific subject. What I have that the sources alone would not give me:
a resolution of the "does this help or hurt" contradiction into a specific,
checkable claim — that the two camps are each right about a different slice
of users, that the "helps" and "harms" findings do not even measure the same
thing, and that the open question is a duration nobody has funded, not a
disagreement about whether the effect exists. None of the individual sources
states that; it is the article's own cross-read, and the original-work
sentence in draft-handoff.md matches what the finished piece actually does
after these edits.

The prose sits closer to the voice-guide exemplars than to a median AI
summary: it opens on the Reddit user's own words before naming Turkle, holds
the De Freitas/Zhang contradiction open the way Julian holds her causal
question open rather than picking a side, and anchors its numbers (deciles,
p-values, betas) to what the studies actually measured rather than
gesturing at "significant" effects. The reworked headline is now the
article's actual largest, best-earned claim rather than a borrowed shape.

## Edits

- Rewrote the headline (title tag, h1, and nb-meta) from "The best evidence
  that heavy ChatGPT use hurts wellbeing comes from OpenAI itself" to
  "OpenAI's own trial found its heaviest users grew more emotionally
  dependent" — breaks the exact mold of the published deskilling headline
  and foregrounds the RCT's strongest, most significant finding instead of
  its weakest.
- Split the why-bookend's dense sentence ("The argument that this
  reshapes...") into two sentences at the "and."
- Rewrote and split the RCT statistics sentence ("It predicted a small rise
  in loneliness...") into two shorter sentences with the same four figures.
- Replaced "a correlation the authors call negligible" with "a correlation
  of just 0.1" (the actual figure, per the Numbers standard) and split the
  surrounding sentence in two.
- Split the De Freitas sentence at its colon ("...found the opposite in one
  setting: an AI companion relieved...") into two sentences.
- Split the section's closing synthesis sentence ("Together, the studies
  support a narrower claim...") at its colon into two sentences, unchanged
  in substance — this is the sentence the round's central-claim check turns
  on, and the split does not touch its meaning.
- Fixed a dangling, unparseable clause in the regulatory section ("...after
  months with a companion chatbot preceded a 14-year-old's death") into a
  grammatical sentence carrying the same two facts.
- Rewrote the regulatory-section heading from "What today's proponents are
  asking regulators to require" (a fresh instance of the brief's own
  flagged "What [X] saw" mold) to "California and the APA want disclosure.
  Common Sense Media wants a ban."
- Split the Prinstein sentence ("...leaves them primed to over-value a
  chatbot's attention, and asked Congress...") into two sentences.
- Rewrote the study-duration heading from the semicolon-reversal "The
  studies run for weeks; the worry is about years" (which also echoed
  power-seeking-ai's two-sentence closer) to "No study has tracked what
  years of use do to a relationship."
- Anchored "The dismissal correctly describes the typical teenager" to "...
  in that survey," so the claim doesn't imply a directly comparable
  population to the adult-sample "heaviest user" studies.
- Rewrote the takeaway's closing-argument sentence to drop a repeated
  negative-parallelism construction and its near-duplication of the
  section-5 thesis sentence: "Which group someone falls into, not which side
  sounds more confident, should decide how worried you are about them" →
  "How worried you should be about someone depends on which of those two
  groups they belong to."
- Cut "told below" (a structural self-reference/signpost outside the
  bookends, where it is not permitted).
- Cut the empty-conclusion sentence "That shift is itself evidence:",
  keeping the substantive sentence it introduced on its own.

Verified after edits: `./nb check ... --series what-could-go-wrong --library
.nb-work/library` (network on) returns BLOCK: 0, WARN: 0, verdict
PUBLISHABLE — all four sentence-density warnings are resolved and no new
warning was introduced. Word count is now 2190 (was 2200), under the
template's ceiling. Re-opened every citation href directly (or confirmed it
against the evidence record's page locators where the fetch tool could not
render a PDF as text) — all land on the source itself, and all figures,
dates, and quotations I could re-check matched exactly.

## Required work

None. All fixes were direct edits within the editor's authority (prose,
structure, headings, a headline, and one grammar repair); no fact was
introduced, no number, name, date, or quotation was altered, and no citation
was recited for a different claim.

- **Orchestrator**: re-stamp (`./nb stamp`) and re-run the proof before
  preparing the PR — this review changed the headline, two headings, and
  several sentences, so the nb-meta `title`, `words`, and `reading_minutes`
  fields are now stale (title still reads the old headline; words/
  reading_minutes still read 2200/10 against an actual count of 2190).

## Decision

**Approve**, after direct cuts. The central claim holds against the cited
studies' populations with one precision fix, all four sentence-density
warnings are resolved, two formula recurrences and one grammar break are
fixed, and every citation and figure I reopened checks out. The orchestrator
must re-stamp and re-run the proof before the PR, since this review edited
the headline, headings, and body text after the writer's last stamp.

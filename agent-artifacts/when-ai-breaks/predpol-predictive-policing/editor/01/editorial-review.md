# Editorial review: when-ai-breaks/predpol-predictive-policing (editor/01)

## Skeptic

Thesis: PredPol/Geolitica's place-based predictions were close to random (Plainfield:
under 0.5% matched a later reported crime) while simultaneously biased, because the
system was trained on recorded crime — a record of past enforcement and reporting
decisions — rather than actual crime, a distinction that produces a provable
feedback loop and, independently, is compounded by how rare the predicted events are
in any one box on any one shift. Claims it stands on: (1) the Plainfield accuracy
figures and their denominators; (2) the feedback-loop mechanism, proven by Lum &
Isaac and Ensign et al.; (3) the vendor-response asymmetry (silence on accuracy,
detailed response on bias); (4) the 7.4% field-trial figure as triangulated, not
verified firsthand; (5) the generalization that a record of decisions can be
mistaken for a forecast.

I opened all twelve cited sources as the article prints their hrefs. The Markup's
two 2023 pieces, the 2021 Markup/Gizmodo piece, Route Fifty, BuzzFeed News, and
Wikipedia all confirmed their cited figures and quotes verbatim or in close
paraphrase. The Brantingham/Valasik/Mohler 2018 DOI correctly redirects to the
gated tandfonline page (a bot-block, not a wrong address — consistent with the
evidence record). The Ensign proceedings.mlr.press link is the paper's own
publisher landing page, a legitimate citation target even though it surfaces only
the abstract to an automated fetch.

One break, fixed directly: the article described Andrea Bertozzi only as "a
field-trial co-author but not one of the founders." Her own letter, which the
article already cites as source 12, discloses in its text: "I am an investor in
the company PredPol and have one publication with Brantingham related to the
implementation of its software." That is a materially relevant fact about a named
person's affiliation that the evidence record's paraphrase omitted, and it changes
how her defense of the software should be read — an investor's defense sits closer
to the company's own interest than "a researcher who happens not to be a founder"
suggests. Since the source was already open and already cited, I fixed the
sentence in place rather than routing it: it now reads "a field-trial co-author
and, by her own disclosure, an investor in the company but not a founder."

The three required corrections held under testing. (a) The asymmetry is stated
honestly: Geolitica's silence on the 2023 accuracy findings is distinct from
MacDonald's on-record, detailed response to the 2021 bias findings, which is
distinct again from the founders' narrower RCT rebuttal and Bertozzi's broader one
— four positions, kept apart, none conflated into a rebuttal the company never
gave. (b) The 7.4% figure is attributed throughout as reported by two independent
readers of a paywalled paper, never as independently verified — "The paper sits
behind a paywall... Neither substitutes for the original study." (c) The article
never commits to a single Santa Cruz date; it says only "in 2020," avoiding the
three-way date conflict in the record.

No other break survived testing. The Plainfield numerator/denominator pairs
(32/5,722; 8/10,141; 34/336) matched The Markup's methodology piece exactly. The
directional claims (recorded crime up, model reads it as confirmation; discovered
incidents converge to one neighborhood) match Lum & Isaac and Ensign et al.'s own
framing. Named people's titles checked out: MacDonald as CEO at the time of the
2021 response, Guarino as Plainfield's captain, Bertozzi's UCLA title.

## Cut

The round's priority was length: 2,388 words against a 1,200–2,200 band. I cut
from middles, targeting redundancy first: sentences that restated a fact or
reasoning step already made. Concrete redundancies removed: a sentence in the
"why this matters" bookend that re-named "PredPol, later renamed Geolitica"
immediately under a dek that had just done so; a closing line in the orientation
section's distinctness paragraph that re-stated the box/shift mechanism already
given; a sentence in the record-of-decisions section ("It folds the underlying
event and someone's past decision together...") that restated the training-data
claim one sentence after it was made; a repeated naming of "Black and Latino
neighborhoods... white ones" inside one paragraph (the demographic breakdown had
just been given in the preceding sentence); and the standalone sentence
"Plainfield dropped its contract," redundant with "already let the contract
lapse" two sentences earlier. None of these lost a fact, a disputable claim, or a
reasoning step — each cut a sentence doing work an adjacent sentence already did.
I also trimmed single words doing no work ("own," "already," "at all," "at
length") across a dozen sentences once the larger cuts were made. Total: roughly
190 words cut, landing at 2,198 — inside the band with a small margin.

I also broke a recurring pattern the brief flagged: "two-part-balance takeaway
closers." The takeaway originally read "It is close to random because... It is
biased because..." — the exact balanced-clause mold named in the round notes. I
rewrote it as one sentence joined by "and" rather than two mirrored clauses,
which also cut five words.

Heading check against `spec/headlines.md` and the recent library: the section
heading "The best case for the software, and the question no one answered" used
the "[clause], and [clause]" construction that a library-wide grep shows recurring
in roughly 45 headings across every desk in this paper — exactly the "looks
stamped" pattern the standard warns about. I rewrote it as "The question the
company's best evidence never answered," a single clause carrying the same
content without the comma-and joint, and updated the matching
`data-nb-section`/`id` (confirmed nothing else in the file anchors to the old id).
The dek and remaining headings do not use a comma-triad, semicolon reversal, or
any of the other flagged molds ("How a X becomes a Y," "Why an alert rarely
means...," a stock "where it lives now" heading); "A record of decisions can pass
for a forecast" and "Recorded crime is not crime" are both built from this
incident's own nouns.

Slop test: no sentence surviving in the final draft reduces to a placeholder
sentence that could describe any subject. The two candidates I checked most
closely — "Recorded crime is not crime" (a real, named misconception the whole
section corrects, not a strawman) and the Verdict note (documented furniture,
used for its intended purpose: a weight-of-evidence landing plus what would
settle the open question) — both earned their place. No self-reference, vague
attribution, or decorative analysis found. No prompt leakage: I compared authored
text against the commission, brief, and voice guide and found no lifted clauses.

Two of my own early edits introduced W-SENTENCE-DENSITY warnings by merging short
sentences into one 50+-word sentence with two clause joins; I reverted both to
shorter sentences (verified against the engine's own `sentence_density` function
directly, not just the proof's summary) rather than leave a density warning I had
caused. Final proof run: BLOCK 0, WARN 0.

## Reader

Reading the finished piece straight through as the declared reader — smart,
widely read, never opened a codebase — what I have that no single cited source
gives me: a single mechanism that explains why the same tool can be both
near-random and racially skewed at once (rare-event base rates account for the
first, training on recorded rather than actual crime accounts for the second),
and a transferable diagnostic in the piece's own words — "a record of decisions
can pass for a forecast" — that no one source states as a unified claim. That
matches the draft-handoff's original-work sentence, and it survives in the
trimmed version: none of the cuts touched the mechanism section, the three
corrections, or the closing generalization.

The prose sits closer to the voice-guide's exemplars than to a median AI summary.
The feedback loop is built as a causal chain before it is named ("patrols go to a
box, officers record more of whatever crime does get reported, the model reads
the rise as confirmation, and the next shift's map favors the same box again"),
matching the Yong model the guide points to. Figures are anchored to comparisons
the reader already owns (a coin flip via "twice as likely to occur," "darts at a
map") rather than left as bare percentages. The company's rebuttal is quoted at
length and then checked against what it does and doesn't address, as the guide's
ProPublica and Markup exemplars do. The headline rereads as the largest claim and
the piece defends it in full.

## Edits

- Cut a sentence in the "why this matters" bookend re-naming "PredPol, later
  renamed Geolitica," redundant with the dek immediately above it.
- Fixed Bertozzi's affiliation: added her own disclosed financial stake in the
  company (an investor, not a founder), checked against the primary source
  already cited as source 12.
- Rewrote the takeaway's "It is close to random because... It is biased
  because..." into one sentence, breaking the "two-part-balance closer" pattern
  named in the round notes.
- Retitled the section heading "The best case for the software, and the question
  no one answered" to "The question the company's best evidence never answered,"
  breaking the paper-wide comma-and heading mold; updated the matching
  `data-nb-section`/`id`.
- Cut a duplicate sentence in the orientation section's distinctness paragraph
  ("Its job was narrower: tell a patrol officer...").
- Cut "no information about any person" from a list that had already made the
  point with "no arrest records, no demographic data."
- Tightened the Plainfield contract sentence (dropped the renewal-price clause,
  which nothing later in the article references).
- Cut the standalone sentence "Plainfield dropped its contract," redundant with
  "already let the contract lapse" two sentences earlier.
- Merged two short sentences describing the LAPD OIG audit's opening into one,
  and shortened "matched each one against Plainfield's own crime reports for the
  same box, crime type, and shift" to "checked each one against Plainfield's own
  crime reports for a match" (the box/shift/type definition was already given a
  sentence earlier).
- Cut "over a year and a half" from the founders' RCT-rebuttal sentence and "on
  Indianapolis data"/the repeated "Black and Latino... white ones" naming from the
  2021-response paragraph (the demographic breakdown had just been given).
- Cut "unverified here against the original study" from the 7.4% paragraph,
  redundant with the following sentence's full paywall/triangulation statement.
- Cut roughly a dozen single words doing no work ("own," "already," "at all," "at
  length," "checkable") once the larger redundancies were gone.
- Verified all twelve citation hrefs by opening each as the article prints it;
  no miscitation found.
- Re-ran `./nb check` after edits: BLOCK 0, WARN 0, 2,198 words (band
  1,200–2,200).

## Required work

None outstanding for the researcher or writer. The `nb-meta` block still records
the pre-edit word count (2,388) and the pre-existing section id; per this round's
brief, the **orchestrator** must run `./nb stamp` and re-run `./nb check` before
the PR so the stamped counts match the edited article.

## Decision

approve — the length warning is cleared (2,198 words, BLOCK 0, WARN 0), the three
required corrections and the mechanism are intact, a real accuracy fix (Bertozzi's
disclosed financial stake) is applied, and a recurring structural pattern (the
two-part-balance closer and the comma-and heading) is broken. The orchestrator
must re-stamp and re-check before the PR.

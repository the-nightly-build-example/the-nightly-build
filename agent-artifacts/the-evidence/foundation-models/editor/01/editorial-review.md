# Editorial review: the-evidence/foundation-models (editor/01)

## Skeptic

Thesis: "On the Opportunities and Risks of Foundation Models" (2021) is a
114-author, 214-page taxonomy and research agenda with no original
experiment; the term it coined became standard usage and even reached
binding federal text, but the reliability its name implies was never the
thing the report measured, a gap its own naming section admits and its
contemporaneous critics built their case on.

Claims tested:

- **The report ran no experiment.** Verified directly: the arXiv v3 PDF's
  table of contents lists Introduction, Capabilities, Applications,
  Technology, Society, Conclusion across 26 sections, no Methods or Results
  section; the "Author Contributions" note confirms 26 sections each written
  by a subset of the 114-name byline; the report's own §1.4 calls only its
  *writing process* an experiment, never the models. Held.
- **114 authors, 214 pages.** Cross-checked against arXiv's own structured
  metadata (114 `<author>` entries) and pdfinfo page counts for v1/v2/v3.
  Held, and correctly used in place of Marcus and Davis's differently-scoped
  149 figure, which the article omits per the evidence record's caution.
- **The self-contradiction spine.** Confirmed the report's own §1.1.1
  states both "we chose the term 'foundation' to connote... architectural
  stability, safety, and security" and, a few sentences later, "we cannot
  characterize whether the foundation is trustworthy or not." The article
  juxtaposes these as the report's own back-to-back sentences and hands the
  judgment to Marcus and Davis ("but then why grandiosely call them
  foundation models at all?") and Dietterich ("does smack of flag
  planting... fundraising side") in their own words, never editorializing
  itself. Held, matches the round-focus requirement exactly.
- **EO 14110 / NIST framing.** Fetched both primary texts directly.
  Confirmed EO 14110 §3(k)'s definition verbatim, confirmed EO 14148 item
  (ggg) rescinding it (signed 2025-01-20, ~15 months after EO 14110), and
  confirmed NIST SP 800-218A is final, dated 2024-07-26. The article never
  claims EO 14110 as current law — "reached federal text once, and did not
  stay there" — while NIST alone carries "became standard usage." Held.
- **The three W-SENTENCE-DENSITY warnings.** Checked all three against
  source text: the §1.1.1 hedge, Dietterich's Wired quote, and the EO 14110
  definition are all genuine verbatim quotation (the EO one strings several
  verbatim clauses together rather than block-quoting the statute, but every
  quoted fragment matches the primary word for word). None is paraphrase
  dressed as quotation; none needed splitting.

Two breaks found and fixed directly (both fixable from evidence already in
hand, no new reporting needed):

- The draft said DALL-E, GPT-3, and BERT split into "three separate fields."
  They don't — GPT-3 and BERT are both language models; only DALL-E is a
  different field (vision). Fixed both instances (orientation and takeaway)
  to "three separate models, across two fields" / "separate stories for each
  field it drew from."
- The draft had Jitendra Malik "tell both Wired and Marcus and Davis" the
  "castles in the air" line. The evidence record shows Wired obtained the
  quote directly; Marcus and Davis instead *report* Malik saying it at a
  CRFM-organized workshop, not to Marcus and Davis personally. Fixed the
  sentence to attribute correctly to each source.

One imprecision fixed: the draft said the version critics read circulated
"three weeks after posting," but the earliest press critique (Tech Brew) ran
at 14 days and Marcus and Davis (already given their own precise "twenty-six
days" a few paragraphs later) at 26 days — neither is three weeks. Cut the
inexact clause; the underlying fact (212 pages, the version critics saw)
stands on its own.

No claim required routing to the researcher. No citation was wrong, no
`data-nb-kind` was misclassified — checked all nine against the primary/stake
test, including the UCSB-hosted EO 14148 transcript, which is still primary
by authorship even though the host isn't the government's own domain. Opened
every printed `href`: all nine resolve to the source itself (fetched EO
14110, EO 14148, NIST SP 800-218A, the Gradient essay, the CRFM
republication, and the arXiv abstract directly).

## Cut

Full sentence-by-sentence and edge pass against `spec/slop.md`. Findings:

- One overclaim softened: "is the only place in 214 pages where the authors
  explain a word choice at length" asserted a completeness no source
  verified (unlike the full-text search that did verify "no experiment
  language anywhere"). Rewrote to "is where the authors explain the word
  choice at length," which the evidence supports without the unverified
  superlative.
- One near-lift of the commission's own reader-outcome sentence, caught on
  clause-order comparison: the why-bookend's "You leave able to ask, of any
  influential AI document, what it proved and what it just called
  something" tracked the commission's "to ask of any influential AI document
  what it actually established versus what it merely named" almost clause
  for clause. The point underneath is genuinely the article's (the evidence
  record and body support it), so rewrote rather than cut: "By the end, you
  can look at a claim like this one and tell what the document actually
  found from what it merely announced."
- Two `data-nb-section` labels didn't mirror their headings the way the
  library's convention requires (checked against `the-evidence/
  stochastic-parrots`, where every flex-section id tracks its heading
  closely): `the-pushback` for "Marcus and Davis built their case on the
  report's own hedge," and `where-the-term-stands` for "The term reached
  federal regulation, then lost it." Renamed to
  `marcus-and-davis-built-their-case` and
  `reached-federal-regulation-then-lost-it`. No internal anchors referenced
  the old ids.
- Fixed one quoted search-term mismatch: the body quoted "we conducted" as
  a search term the researcher ran; the evidence record's actual term was
  "we conduct." Corrected for exact match.

Full edge pass (first/last sentence of every paragraph, section, and the
whole piece, read out of order): all held. The article's last sentence
("214 pages, no experiment, and a name that outran what any of it proved")
carries specific figures earned by the body and passes the delete test —
removing it loses the conclusion the argument built. The why-bookend and
takeaway read as a genuine setup/resolution pair, not a restated summary.

Delete test run on every sentence: nothing else failed it. No negative
parallelism found straining a strawman (the one "not text from text"
construction is a real technical distinction, not a corrected misconception
built to sound clever). No vague attribution, no puffery, no fluff openers,
no elaborate copulas. Zero em-dashes (limit 4). No banned-term or
sentence-density issues beyond the three already confirmed as genuine
quotation.

Checked against the recent `the-evidence` record (8 most recent deks) and
tonight's four sibling headlines: this dek's "then" connector doesn't repeat
the record's dominant "and" shape; the four flex-section headings are
concrete and piece-specific, not scaffolding, and don't echo a prior
article's shape. No formula found.

Checked all authored text against the commission, both briefs, the evidence
record, and the voice guide for prompt leakage (clause order, not just
wording). One catch, described above and fixed; nothing else lifted.

## Reader

What survives that no single source gives on its own: a document's full
lifecycle stitched from sources that never talk to each other — the report
doesn't discuss its own critics, Marcus and Davis don't discuss NIST or the
executive order, and NIST/the EOs don't discuss the naming fight — into one
throughline (named, contested, standardized, briefly codified, rescinded)
built entirely on primary text the piece opens directly rather than on
reputation. The original-work sentence in `draft-handoff.md` (juxtaposing
the report's own two sentences as fact, then handing the judgment to Marcus
and Davis's own words) holds up against the article as written.

Prose sits closer to the voice-guide exemplars than a median summary:
Newton's technique (evidence in the same breath as the finding) shows up
directly in "Thomas Dietterich, a former AAAI president then at Oregon
State, told Wired he suspected a motive..." and in stating CRFM's funders
right after the fundraising quote and letting it stand without comment;
Smith's technique (one worked primary example over reputation) is the
close reading of §1.1.1 with both sentences quoted and dated as adjacent.

Headline reread as the largest claim: "The report that coined 'foundation
models' ran no experiment" is fully earned — the piece explicitly
distinguishes the report's own "the writing of this report was an
experiment" line from the models it names, so the headline's claim survives
the one objection a careful reader would raise against it.

## Edits

1. Cut the imprecise "three weeks after posting" (orientation section);
   kept the underlying 212-page fact, which needed no specific day count.
2. Corrected a quoted search term from "we conducted" to "we conduct" to
   match the evidence record's actual full-text search string.
3. Rewrote the why-bookend's closing sentence to diverge from the
   commission's near-identical clause order while keeping the same payoff.
4. Softened "is the only place in 214 pages where the authors explain a
   word choice at length" to "is where the authors explain the word choice
   at length" — the completeness claim wasn't verified the way the
   no-experiment-language claim was.
5. Fixed "three separate trends in three separate fields" to "three
   separate models, across two fields" (orientation section) — GPT-3 and
   BERT are both language models; only DALL-E is a different field.
6. Fixed the matching takeaway sentence, "instead of three stories about
   three fields," to "instead of separate stories for each field it drew
   from," for the same reason.
7. Rewrote the Malik sentence to attribute the Wired quote to Wired
   directly and the CRFM-workshop remark to Marcus and Davis's reporting,
   rather than saying he told both outlets the same line.
8. Renamed `data-nb-section`/`id` on the third body section from
   `the-pushback` to `marcus-and-davis-built-their-case` to mirror its
   heading, per the library's established convention.
9. Renamed `data-nb-section`/`id` on the fourth body section from
   `where-the-term-stands` to `reached-federal-regulation-then-lost-it` to
   mirror its heading, for the same reason.

No change to the headline, dek, or `nb-meta` JSON — both stay exactly as
handed off, so no sync was needed between the rendered element and the
`nb-meta` block.

## Required work

None. No item requires the researcher, the writer, or the orchestrator; all
findings from the three reads were fixable directly from the evidence
already in the workspace and are logged above.

## Decision

**Approve.** The thesis holds against a skeptic's read of every source
directly opened, the self-contradiction spine is the report's own words
juxtaposed as fact with judgment left to named critics, the three flagged
warnings are genuine verbatim quotation, the 114/214 counts are used with
the 149 figure correctly absent, the EO 14110/NIST framing matches the
round-focus requirement exactly, and the source asset's crop, caption, and
provenance are all sound. Nine edits made directly close the remaining gaps;
none needed reporting this workspace doesn't already have.

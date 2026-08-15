# Editorial review: when-ai-breaks/google-photos-gorilla (editor/01)

## Skeptic

Thesis: Google Photos filed two Black men under a gorilla label in 2015, and the
repair Google shipped deleted the word rather than fixing the recognition, a
choice four companies still made in 2023. It stands on four claims.

1. The mislabel happened as described, and Google's response was an apology plus
   a promise to fix recognition. Held. Alciné's wording, Zunger's title and
   reply, and the "appalled and genuinely sorry" statement all match the two
   contemporaneous outlets that carry them (Forbes s1, CBC s2); I pulled both
   pages and read the passages. The tweets themselves are deleted, so the
   article correctly attributes the wording to the coverage, not to dead links.

2. The cause is training-data under-representation, taught as mechanism and not
   as a measurement of the gorilla error. Held, and this was the round's main
   risk. I read the two arXiv primaries in full. Shankar (s4) gives >32% US in
   Open Images, ~60% from six North American and European countries, China ~1%,
   India ~2%, ImageNet ~45% US, and the Hyderabad groom recognition drop — every
   figure in the article is exact to the paper. Yang (s5) gives the 6.2% average
   Dark share across the annotated person synsets and the slurs inherited from
   WordNet — both exact. The article states plainly and in three places (the
   bounding paragraph, the "In plain language" note, and the Gender Shades
   setup) that none of these studies measured Google Photos. The line holds.

3. Gender Shades measures the downstream accuracy gap. Held. I read the paper;
   its own key-findings bullets give 20.8%–34.7% error on darker-skinned women
   and 0.0% / 0.3% on lighter-skinned men for Microsoft and IBM, the 1,270-face
   balanced benchmark, and the three vendors. All exact. The article says twice
   it did not test Google Photos or animal labels. Good.

4. The non-fix was a choice, not an inability. Held. Wired (s3, read via curl;
   the WebFetch tool blocks the domain but the URL returns 200 and a real click
   lands) carries the 40,000-image test, the four blocked search terms, the
   "nowhere near perfect" quote, Cloud Vision's "western gorilla" at 94%, and
   Assistant naming one too. The article reads the 94% result correctly as proof
   the recognition existed and the block was deliberate, and never drifts into a
   blanket "Google can't recognize a gorilla" claim.

Breaks found and handled:
- The "better recognition of dark-skinned faces" quote was cited to CBC (s2)
  in two places. CBC carries no such quote — its Zunger material stops at the
  "target market / 100% Not OK" tweet. PetaPixel (s7) carries the quote verbatim
  ("image recognition itself — e.g. better recognition of dark-skinned faces").
  Right source already in the article; repointed both to s7.
- The 2023 timeline entry's multi-company claim (Apple, Microsoft OneDrive,
  Amazon) was cited only to PetaPixel (s7), which covers Google and Apple but
  not OneDrive or Amazon. The Register (s8) carries all four verbatim. Added s8
  to the entry.
- Minor, left as is: "within about two hours" is cited to Forbes, which says
  "within hours"; the two-hour figure is the researcher's tweet-ID decode
  recorded in the evidence Numbers section, so the claim is sourced, just split
  between the cite and the record.

Citation-resolution check (the round's third focus): I opened all eight printed
hrefs. All resolve to the source itself. Forbes returns 403 to a bare client but
200 and the full article to a browser, so a reader's click lands. No deleted
tweet, protected account, or paywalled NYT URL appears as a live citation; the
four readable primaries (s3 Wired, s4 Shankar, s5 Yang, s6 Gender Shades) carry
the floor. Display text checks clean: the headline, dek, subheads, and the two
named researchers' affiliations (Princeton and Stanford for Yang; Google Brain
for Shankar) all match their primaries.

Sensitivity check (fourth focus): the racist label is reported plainly and set
at the level of the facts around it, with the harm carried by Alciné's own
words and no reach for effect. It is serious and not sensationalized. One note:
"a long history as a racist slur against Black people" is a shade stronger than
CBC's "racist connotations," but the historical fact is general knowledge and
the treatment is sound; I left it rather than sand it down to the source's
softer word.

## Cut

Slop pass against `spec/slop.md`, every sentence including display text and the
prose inside the timeline, the note, and both bookends. One real failure, and it
was the one the pattern notes named.

- The "Why this matters" bookend closed on "By the end you will know what an
  image classifier is, why its accuracy is uneven ..., and why the block ...":
  the exact house catchphrase the recent-pattern notes and the commission both
  flag, and its middle clause merely restated the sentence before it. The lesson
  template still requires the opener to say what the reader will carry away, so I
  rewrote rather than deleted, dropping the catchphrase and the redundant clause
  and keeping the two live points (what a classifier is; why the block outlived
  the apology) in the incident's own nouns.

Edge sentences otherwise hold. The recurring "only as good as the examples it
was shown" is a deliberate teaching refrain that carries the mechanism each
time, not filler. The two bookends read back to back as setup and resolution.
The closing section is titled "The block that outlived the apology" — the
incident's own nouns, not the desk's "Where the weakness lives now" mold, so the
closer check passes. Headline and dek clear the negative-parallelism and
comma-triad molds; the headline states the finding with wordplay anchored in the
story's own noun (gorillas) and a plain dek beside it.

Two reflex semicolons joined independent clauses where the editorial punctuation
default wants a period (the "In plain language" note; the 2023 timeline's
multi-company line). Changed both to periods. No prompt or brief phrasing leaked
into the prose; the bookend's self-reference is the one place the template
allows it.

## Reader

Read straight through as the paper's declared reader, it gives what no single
source does: the three findings assembled into one causal chain — the mislabel,
the under-representation cause bounded honestly as mechanism, and the deletion
read as evidence the gap was never closed — landing on the four-company
persistence. That is exactly the article's stated original work, and it survives.
The prose sits close to the voice-guide exemplars: plain declaratives narrating
the incident, the mechanism built one step at a time, and figures stated with
their limits (the bounding paragraph and note do the Luu move), not a median
summary. The headline holds as the largest claim the piece defends.

## Edits

- Rewrote the "Why this matters" bookend's closing sentence to remove the
  "By the end you will know ..." catchphrase and its redundant clause, keeping
  the template-required takeaway in the incident's nouns.
- Repointed the "better recognition of dark-skinned faces" citation from s2
  (CBC, which does not carry it) to s7 (PetaPixel, which does) in the "Google's
  answer that night" section.
- Repointed the same quote's citation from s2 to s7 in the "skin-tone gap"
  section.
- Added s8 (The Register) to the 2023 timeline entry to source the Apple /
  Microsoft OneDrive / Amazon claim that s7 does not carry.
- Changed the semicolon to a period in the 2023 timeline's multi-company line.
- Changed the semicolon to a period in the "In plain language" note.

## Required work

- **orchestrator:** The commission's "Boundaries and neighbors" directs the
  piece to link and distinguish `when-ai-breaks/gemini-image-generation`
  (generation overcorrection, not classification) and to link
  `rite-aid-facial-recognition` alongside `facial-recognition-wrongful-arrest`.
  The draft links only `facial-recognition-wrongful-arrest` (plus
  `amazon-hiring-tool`, a reasonable but non-commissioned neighbor); both
  `gemini-image-generation` and `rite-aid-facial-recognition` exist in the
  published library but are absent here. Writer briefs 01 and 02 did not carry
  this requirement forward, so reconcile: confirm the narrowed scope, or route
  the addition to the **writer** (a plain in-prose link distinguishing the
  generation-overcorrection failure from this classification-from-
  under-representation one, per the house rule to link rather than re-teach — no
  new reporting beyond correctly naming gemini's mechanism).

## Decision

Revise: the substantive editorial defects (two miscitations, the flagged
catchphrase, two reflex semicolons) are fixed in place, but the commission's
mandated neighbor-links to gemini-image-generation and rite-aid-facial-
recognition are unmet and need the orchestrator to either enforce or waive.

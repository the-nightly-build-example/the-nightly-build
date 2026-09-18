# Editorial review: when-ai-breaks/sports-illustrated-ai-authors (editor/01)

## Skeptic

Thesis: a real magazine ran product reviews under invented human bylines
(stock AI headshots, fabricated biographies), which is a distinct kind of
trust failure from a real byline carrying AI-written text with a checkable
error, and the same tell — an unverifiable byline, a generic headshot, a
buried disclosure line — is still exploitable today. The piece stands on
four claims: (1) the five personas were fabricated, not pseudonyms; (2)
whether the article prose itself was AI-written is genuinely unresolved; (3)
Ross Levinsohn's firing is media inference, not a stated cause; (4) this is a
different failure mode from `cnet-ai-articles`.

I pulled and reread every cited source directly rather than trusting the
evidence record's paraphrases: both archived author pages (Drew Ortiz,
Domino Abrams), the archived volleyball review page, Futurism's original
report, Futurism's AdVon follow-up, the CBS News pieces, NPR, the FTC
release, and searched independently for the Business Wire release and for
generated.photos' own account of its technology.

- **Claim 1 (identity fabrication) held.** The archived Ortiz page's title,
  bio text, and headshot filenames match the article word for word. The
  Domino Abrams page independently confirms an October 2021 date, a year
  earlier than the Nov 2023 exposure implied elsewhere in the draft — see
  below. Arena Group's "pen or pseudo name" framing is accurately quoted and
  correctly contrasted with what the archived pages show.
- **Claim 2 (AI-text claim) held, but one internal inconsistency fixed.**
  Futurism's own report sources this to two unnamed people; the draft
  correctly declines to treat NPR's retelling as a second confirmation. But
  two sentences (in the body and again in the takeaway) then called this
  "one anonymous source," which contradicts the "two people" the same
  paragraph had just quoted. Fixed both to "one outlet's anonymous
  sourcing," which is what the "not two [confirmations]" argument actually
  needs and keeps the sentence consistent with itself.
- **Claim 3 (Levinsohn) held.** Verified independently: the board acted
  December 11, 2023 (Monday); CBS's story carries a December 12 byline
  reporting on that Monday action, which could have read as a date
  mismatch but isn't one. The press release language and the "operational
  efficiency and revenue" framing check out verbatim against multiple
  independent transcriptions (the Business Wire URL itself is bot-gated to
  automated fetches, as the evidence record already flagged, but its
  content is corroborated by CBS, and other named outlets are cited in the
  evidence record; not a new problem).
- **Claim 4 (cnet-ai-articles distinction) held.** Read the actual
  cnet-ai-articles article: real staff byline, in-house AI drafting tool,
  one checkable compound-interest error. The draft's contrast is accurate
  and the link (`cnet-ai-articles.html`, plain prose link at first use) is
  the correct, non-mirrored form.

**Breaks found and fixed directly:**

- The "Why this matters" bookend said Sports Illustrated and TheStreet
  "started running" the fabricated bylines "in late 2022." The archived
  Domino Abrams TheStreet page the piece itself cites is dated October
  2021 — a full year earlier. Fixed the opener to "starting at least as
  early as 2021," matching the article's own later, correctly-dated claim.
- The same bookend, and a sentence in the pen-name section, described the
  fabricated personas as coming with "a hometown." No persona in the
  evidence record or any archived page has a stated hometown — Ortiz's bio
  gives a farmhouse childhood, not a place name. Fixed both to "an invented
  childhood" / "a childhood," which is what the sources actually support.
- The piece asserted, uncited and unsupported by anything in the evidence
  record, that "a marketplace like generated.photos runs a diffusion
  model." I checked: generated.photos' own FAQ states it uses "generative
  adversarial networks," not diffusion, and the two existing
  the-mechanics lessons this passage linked to are diffusion-specific. This
  was an unsupported and factually incorrect technical claim, tied to a
  now-misleading internal link. Cut the specific (wrong) architecture claim
  and the link; kept the sourced point (a trained model licenses a
  synthetic photo from a catalog instead of a photo shoot), still cited to
  Futurism (source 2).
- "A dozen other publishers" (used twice, body and Go-deeper line)
  undercounts what the evidence record and Futurism's own AdVon report
  establish: the evidence record's paraphrase says "dozens of publishers,"
  and Futurism names roughly two dozen client titles. Fixed both instances
  to "dozens of."
- One factual claim ("no social media, no other byline") lacked its own
  citation marker, sitting after an unrelated citation in the same
  sentence. It is directly supported by source 2 (already cited two
  sentences earlier for the same paragraph); added the marker rather than
  leaving a display claim uncited.

No break required cutting a claim the argument depends on, and nothing here
needed new reporting: every fix used facts already in the evidence record or
in a source the record already cites.

## Cut

Ran the slop test on every sentence, both edges (paragraph, section, and
article boundaries) in and out of order, and the delete test on load-bearing
candidates. The prose was already close to clean going in — no fluff
openers, no vague attribution, no puffery words, no banned lexical terms
(checked `spec/banned-terms.yaml`: zero em-dashes, zero uses of leverage,
load-bearing, revolutionary, transformative, game-changing, AI race, or
machinery). Two borderline sentences ("Both sides have kept their story
since," "Neither company has produced the document that would settle which
of them is right") were checked against the delete test; both survived
because each carries a specific fact (the dispute is still unresolved a year
on) rather than summarizing the piece's own method.

The one structural formula caught: the heading "What Arena Group did next,
and who it blamed" is the exact comma-plus-"and" mold the recent library
already repeats twice in `meta-ad-delivery-discrimination` ("What the
advertiser chose, and what Facebook chose instead"; "What the May 2025
ruling did, and what it did not do") and once in `character-ai-lawsuit`.
Rewrote to "The firings Arena Group didn't blame on AI" — a single clause,
in the piece's own nouns, that states the section's actual point (the
firings happened; the company's own stated reason wasn't AI) instead of a
templated two-clause pairing.

Headline and dek checked against the recent-pattern notes: neither matches
"System told X that Y. It hadn't." nor "Company did X, then announced Y."
The dek is a single sentence, not a semicolon reversal, suspended question,
or comma triad. No moralizing close: the body ends on the two companies'
still-unresolved, dueling positions, and the takeaway states what a reader
now knows to check, not a verdict.

## Reader

A reader who has read only this piece comes away able to tell apart three
things that get blurred in casual retellings of this story: a fabricated
person (proven), AI-written prose under a fabricated name (unproven, one
outlet's anonymous sourcing, denied by both accused parties), and a
CEO's firing that reporting connected to the scandal but that the company's
own statement never named as the reason. They also leave with a compressed,
concrete checklist (unverifiable byline, generic stock-looking headshot,
buried third-party disclosure) built from the specific facts of this case
rather than a general warning. That is more than the sources alone give a
reader, since no single cited source holds the identity-fabrication /
AI-text-claim / firing-cause distinction in one place with the "what would
settle it" framing this piece adds. The prose sits closer to the
voice-guide's exemplars (Hill, Newton, Angwin) than to a median AI summary:
declarative sentences carrying one fact each, no adjective stacked in front
of a quote, and the ending handed to the two parties' unresolved positions
rather than a stated moral. The headline, reread as the largest claim
("Five of Sports Illustrated's product reviewers were AI-generated people"),
is a claim the body fully defends — the number is the story, matching
`spec/headlines.md`'s guidance that a figure earns its place in the
headline when it is the surprise.

## Edits

1. "Why this matters" bookend: changed "In late 2022, Sports Illustrated and
   its sister site TheStreet started running..." to "Starting at least as
   early as 2021, Sports Illustrated and its sister site TheStreet ran..." —
   the draft's own cited source (Domino Abrams' TheStreet page) is dated
   October 2021.
2. Same bookend: changed "a headshot, a hometown, and a hobby" to "a
   headshot, an invented childhood, and a hobby" — no persona has a named
   hometown in any source.
3. Orientation section: added a citation marker (source 2) to "Outside
   Sports Illustrated's own pages, Drew Ortiz leaves no trace at all: no
   social media, no other byline, nothing," which was previously uncited.
4. Pen-name section: changed "attached to a hometown, a hobby, and a
   personality" to "attached to a childhood, a hobby, and a personality" —
   same hometown fix.
5. AI-text-claim section: changed "One anonymous source, retold by a second
   outlet, is one confirmation, not two" to "One outlet's anonymous
   sourcing, retold by a second outlet, is one confirmation, not two" — the
   prior sentence in the same paragraph establishes two unnamed people, not
   one, so "one anonymous source" was internally inconsistent.
6. AI-text-claim section: changed "a dozen other publishers" to "dozens of
   other publishers" — matches the evidence record's own characterization
   and Futurism's reporting, which names roughly two dozen client titles.
7. Aftermath section: retitled the heading "What Arena Group did next, and
   who it blamed" to "The firings Arena Group didn't blame on AI" —
   breaks the comma-plus-"and" heading mold the recent library repeats.
8. Where-it-lives-now section: cut the unsupported and incorrect claim that
   generated.photos "runs a diffusion model," along with the link to
   `../the-mechanics/image-generation.html` (a diffusion-specific lesson).
   generated.photos' own published FAQ states it uses generative
   adversarial networks, not diffusion, and nothing in the evidence record
   supports the diffusion claim either way. Replaced with "trains a model
   on real photographs, then generates a photorealistic portrait nobody sat
   for and licenses it from a catalog instead of a photo shoot," still
   cited to source 2.
9. Takeaway bookend: changed "one anonymous source" to "one outlet's
   anonymous sourcing" — same fix as #5, for consistency across the piece.
10. Go-deeper band: changed "a dozen more publishers" to "dozens more
    publishers" — same fix as #6.

## Required work

None. No item needs the researcher or writer; nothing here required new
reporting, a source asset, or a redraft. The no-source-asset call from the
writer's handoff stands: the argument turns on quoted bio and statement
text a reader can check in the citations themselves, not on seeing the
page rendered, and no image would let a reader test a claim the prose
doesn't already let them test.

## Decision

Approve. The three reported-fact/contested lines are held exactly where the
commission and evidence record put them, the cnet-ai-articles distinction is
accurate and linked without mirroring its structure, no claim in the piece
outruns its sourcing after the fixes above, and the prose, structure, and
furniture meet `spec/slop.md` and `spec/headlines.md`.

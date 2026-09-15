# Editorial review: what-could-go-wrong/recommender-radicalization (editor/01)

## Skeptic

Thesis: the studies built specifically to catch a YouTube rabbit hole or a
sealed filter bubble mostly failed to find either operating on typical users,
but every null is bounded, so "the algorithm radicalizes ordinary users" and
"recommenders are harmless" both spend confidence no cited study measured. The
piece states it and defends it.

The claims it rests on, and how each held:

- **Pariser named the filter bubble in 2011 from a real observation.** Quotes
  ("edited them out," "57 signals," the Egypt-results anecdote, "your own
  personal, unique universe") match the evidence record verbatim; direction of
  the Daniel/Scott example is correct. Held.
- **Tufekci's 2018 "Great Radicalizer" argued watch-time optimization escalates
  content.** All quotes verbatim, mechanism correctly attributed to her. Held.
  The article also carries her own concession ("good data is hard to come by")
  and correctly recasts her three external supports (Chaslot, the WSJ using
  Chaslot's tool, Albright) as fresh-account audits, not real-user evidence.
  This is the article's hinge and it is drawn honestly.
- **Hosseinmardi 2021 found no population-level drift.** N=309,813, 21,385,962
  video views, 2016–2019, news ~11%, far-right 0.17%→0.30%, anti-woke
  0.31%→1.02%, entry points 41.29% external / 35.8% another video: all match the
  primary. The population-level caveat is quoted. Held.
- **Chen 2023 found rabbit holes vanishingly rare and concentrated in
  subscribers.** n=1,181, view shares 3% / 0.5% / 3.6% / 93%, subscriber shares
  60.8% / 54.7%, rabbit-hole rate 0.01% of visits among 3.0% of participants
  (called a lower bound), 2020 observation after the 2019 recommender change:
  all match. Held.
- **Bakshy 2015 found sorting substantially demand-side.** 10.1M users, 7M
  links, ranking 5%/8% vs choice 17%/6%, >20% opposing-party friends, plus the
  sample-skew and neutral-baseline criticism: all match, and the liberal figures
  (choice 6% below ranking 8%) are stated correctly rather than forced into the
  headline direction. Held.
- **Guess 2023's chronological feed did not move attitudes.** Null quoted
  verbatim; the ~23,000-per-study figure carries a `data-nb-note` marking it as
  Science's news coverage, not the paywalled body; the 63 "break glass" changes
  bound the window. Held, with the uncertainty correctly displayed.

Breaks found and fixed:

- **The dek generalized one study's finding to all four.** It read "Four studies
  of real viewing found extreme content clustered among ... resentful
  subscribers." That is Chen's finding (and loosely Hosseinmardi's entry-point
  result); Bakshy and Guess measured Facebook cross-cutting exposure and
  polarization, neither "extreme content" nor "resentful subscribers." A false
  label in the dek reaches every reader. Fixed to "Studies that tracked real
  YouTube viewing," which is accurate to the two YouTube studies the claim
  actually rests on, in both the visible dekline and the `nb-meta` block.
- **A number carried the wrong noun.** "21,385,962 individual YouTube videos"
  labels the primary's 21,385,962 *watched-video pageviews* as distinct videos.
  Fixed to "21,385,962 video views."
- **The synthesis table overstated one figure by a hair.** "far-right stayed
  under 0.3% of watch-time" contradicts the body's 0.30% in 2019. Fixed to "rose
  only to 0.30%."

No central claim broke; no evidence was missing; nothing needed new reporting.
Every fix used a figure or source already in the record, so none was routed.
Kind labels pass the authorship-and-stake test: the six primaries own their
arguments or their data, and Science's news report, the UMass release, and the
McNamee op-ed report from outside. Source floor (9 total, 6 primary, 3
secondary) clears the policy floor.

## Cut

Two sentences failed the slop test and were cut or trimmed; one furniture
component was removed; two grammar breaks were repaired.

- **A signpost previewing the conclusion.** "Set the studies next to what each
  can actually reach, and a pattern shows up on both sides" grades what the table
  is about to show. Trimmed to "Set the studies beside what each can actually
  reach," which leads into the table without announcing its verdict.
- **A redundant pull quote.** The `nb-pull` block repeated its own section's
  closing sentence, "Both claims spend confidence the studies did not bank,"
  verbatim and immediately below it, so the two stacked. Removed the block; the
  line still lands in the strongest position, the paragraph's close.
- **A run-on that could be misread.** The Chaslot/Albright paragraph ended in a
  four-comma sentence whose final clause ("the question the studies that followed
  went after directly") dangled off no clear antecedent. Split into three
  sentences carrying the same facts.
- **An opaque link anchor.** "What a feed built that way reliably rewards is its
  own subject" pointed the anchor text "its own subject" at the Myanmar lesson, a
  meta-gesture a cold reader cannot parse. Rewritten to name the reward
  (attention) and land the link on "Myanmar's feed."

The register holds to the voice guide: numbers arrive before their
interpretation (Yong/Engber), the nulls get flat sentences without adjectives
("showed no drift toward extremes either"), and the closing verdict states each
claim's ceiling and floor together the way Belluz states a treatment's. No
borrowed phrasing from the guide's exemplars, no prompt leakage, no
self-reference outside the two bookends. Headings and dek clear the recent-
pattern molds: no "What Bainbridge saw" opener, no "The floor labs stand on now"
closer, no comma-triad or semicolon-reversal dek. The negative parallelism that
survives ("real systems, not simulated ones"; "not an editor's judgment") each
corrects a misconception the piece names, so both stay.

## Reader

Read straight through, the piece hands its reader something no single source
does: the vivid engagement-optimization mechanism set against the specific tests
built to detect it, with each null's scope-limit named, so the reader can hear
"the algorithm radicalized him" or "it's a moral panic" and locate the supported
part of each. The draft-handoff's original-work sentence claims exactly that
comparative frame plus the synthesis table, and both survive the read. The prose
sits closer to the voice-guide exemplars than to a median summary: it commits to
figures, refuses to editorialize the nulls, and closes on the two-sided gap
rather than a moral. The headline, read as the largest claim, is one the body
earns, and "mostly" keeps it honest against the bounds.

## Edits

- Dekline and `nb-meta` dek: "Four studies of real viewing found" to "Studies
  that tracked real YouTube viewing found."
- Orientation: recast "What a feed built that way reliably rewards is its own
  subject" into "A feed built that way reliably rewards attention ... The same
  ranking shaped Myanmar's feed," moving the link onto concrete anchor text.
- Hosseinmardi paragraph: "21,385,962 individual YouTube videos" to
  "21,385,962 video views," and "watching" to "across" to fit the noun.
- Chaslot/Albright paragraph: split the closing four-comma run-on into three
  sentences, same facts.
- Table lead-in: "Set the studies next to what each can actually reach, and a
  pattern shows up on both sides" to "Set the studies beside what each can
  actually reach."
- Synthesis table, Hosseinmardi row: "far-right stayed under 0.3% of watch-time"
  to "far-right rose only to 0.30% of watch-time."
- Removed the `nb-pull` block that duplicated its section's closing sentence.

## Required work

- **orchestrator** — re-stamp and run the link-checked proof
  (`./nb check ... --series what-could-go-wrong`) as the normal next step; the
  edits are net word-negative against the writer's 2200, so the length band
  holds, but the stamp should confirm.

None to researcher or writer: no evidence gap, no broken claim, no reporting, no
chart or source-asset work is outstanding.

## Decision

approve — the thesis holds against its own sources, the three display-text and
numeric errors are fixed in place, and the slop and formula passes leave nothing
publication-blocking.

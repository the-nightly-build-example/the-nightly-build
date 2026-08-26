# Editorial review: the-instruments/codeforces-rating (editor/01)

## Skeptic

The thesis: a Codeforces rating is an Elo-style standing relative to whatever live
human field entered a round, so it certifies a placing and not skill in the
abstract; every AI "Codeforces rating" in circulation is an estimate fit to
simulated or reconstructed contests, condition-dependent enough that the same o1
reads as 1673 or 2214 depending on the test-time scaffolding; and the headline
glosses (o3's flat 2727, "175th best programmer") drop that qualifier. I can
state that thesis from the draft alone, and the four load-bearing claims under it
are legible: the rating is a relative standing (s1), the AI figures are scaffold-
dependent estimates (s5), AlphaCode's 1238 rode on up to a million samples
filtered to ten submissions (s4), and the o3 launch number circulated stripped of
its condition (s5 vs s8).

I tried to break each against the evidence record (researcher/02, which supersedes
01 and adds VentureBeat as s8). The spine holds and is pinned to its sources:

- Elo generalization, seed, and the 0.75/0.9 win probabilities at 200/400-point
  gaps all trace to s1, correctly attributed to the founder. Elo itself is linked
  out to `chatbot-arena-elo`, not re-taught, as the commission requires.
- AlphaCode: top 54.3%, estimated 1238, top 28% (beats 72%), >5,000 participants,
  ~1M samples averaged to 2.4 submissions per solved problem, all match s4. The
  571-vs-541 kind of arithmetic checks: 2214 − 1673 = 541, stated correctly.
- OpenAI ladder 808 / 1258 / 1673 / 2724 and the 99.8th percentile match s5. The
  "1673 or 2214 for the same base o1" framing is the evidence record's own
  synthesis (it names o1-ioi as the same base model), so it is within the record
  rather than an overstatement.
- The percentile denominator (99,832 active players, 30 May 2021) matches s3, and
  the draft correctly labels s3 secondary and never presents EbTech's bands as
  Codeforces titles, which the record's caution flags.

The two framings the record corrects are both honored. The draft does NOT claim
the ratings never faced the real judge; it states plainly that AlphaCode submitted
to the live Codeforces judge on finished contests and draws the honest split
(retroactive entry into a closed contest versus a live sitting). It makes no
Codeforces-specific contamination claim; it reports LiveCodeBench's LeetCode-only
memorization signal and Codeforces coming out smooth, and uses that against the
contamination story. The "175th best programmer" line is attributed to the launch
and its retellings, not to a primary that owns it, and the 2724/2727 discrepancy
is resolved in favor of the paper's 2724, as the record and brief direct.

Every `data-nb-kind` matches the record's primary/secondary determination (s3 and
s8 secondary; the rest primary). I opened all eight citation hrefs as printed:
the four arXiv links resolve (200); VentureBeat returned a transient 429 on a
well-formed URL; the three codeforces.com links return 403 from the documented
Cloudflare interstitial and resolve for a human browser. Both internal Background
targets exist in the library. No break found; nothing routed to the researcher.

One factual slip inside display-adjacent prose: the draft used "the exact number
that earns 'Grandmaster' depends on the year" as its example of a shifted cutoff,
but the record shows Grandmaster (2400–2599) is unchanged since 2013; what moved
were the bands above it and Master's floor. I generalized the example to "a top
title," which the record's "pushed the top bands upward" supports, rather than
introduce a current-threshold figure the article does not cite.

## Cut

A dedicated slop pass against `spec/slop.md`, every sentence including display
text and the one furniture note. Five sentences failed and were cut or recast;
the note ("In plain language") is the documented plain-language rendering for the
lesson template and stays.

- The why-bookend opener was a formula. "Every few months a lab reports that its
  newest model reached the 90th or 99th percentile" is built to the exact mold the
  last Instruments piece (bfcl) opened on: "Every few weeks a lab announces that
  its newest model is better at X, and points to a Y-score to prove it." I
  rewrote it into this lesson's own frame (a lab reaching for a Codeforces rating
  to prove its model can code) without copying bfcl's structure.
- The orientation section closed on a signpost: "That is the fact every quoted
  rating below has to be read through, and it is the one most easily dropped." It
  forward-references the article's own structure and states no new fact; the
  reasoning step ("change the field and the same performance yields a different
  number") already lands the point, so the section now ends there.
- The "175th" section opened on "Here is where a number gets away from its
  conditions," a where-the-piece-has-gone pointer the heading already carries. Cut;
  the section now opens on the concrete 2724 fact.
- "The most useful line in that paper is a comparison inside one model" graded the
  source rather than continuing the argument; recast to "The sharpest comparison
  in that paper is inside a single model."
- The dek restated the headline (the 1673/2214 swing) where `spec/headlines.md`
  requires it to add. Rewritten so it supplies what the headline omits: the source
  (OpenAI's own paper) and the generalization to every circulating figure up to
  o3's 2724, with the load-bearing "never entered live."

I checked the flagged house tics and found none present: no "doing the work," no
"It is tempting to say X. That goes too far.," no "the whole point / the catch is."
The takeaway does NOT close on the banned "Read [the number] as what it is, and
ask separately whether Y" mold; it lands in this article's own frame (treat the
figure as where the reading starts, then three concrete questions about contests,
attempts, and season). One earned negative-parallelism survives ("a rank among
recently active contestants, not among all programmers and not among all people"),
because the misconception it corrects is real and named. No prompt leakage against
the commission or brief: the reader-situation sentences are reported, not lifted.

## Reader

Read straight through as the paper's declared reader, what I have that the sources
alone would not give me: the several different "Codeforces rating" claims labs have
published are put on one title-anchored footing, with the mechanism (a rating is a
placing inside a live field) taught first, so I can see that every AI figure is a
condition-dependent estimate and that the same o1 swings 541 points on scaffolding
alone. The original-work sentence claims exactly that synthesis, and it survives:
the chart plus the title-anchored readings in prose assemble something no single
source performs. The prose sits closer to the voice-guide exemplars than a median
summary. It follows Ritchie's move of plain definition then one carried case
(1238 as Pupil, the 541-point o1 swing), and states the split flatly the way the
guide asks. The headline reads as the largest claim and is true and supported.

## Edits

- Rewrote the why-bookend opener to break bfcl's "Every few [period] a lab..."
  formula.
- Rewrote the dek to add attribution and the generalization instead of restating
  the headline's 1673/2214 swing (updated both the visible dekline and the
  nb-meta `dek` field to match).
- Changed "the exact number that earns 'Grandmaster' depends on the year" to "the
  exact number that earns a top title depends on the year"; Grandmaster's cutoffs
  are unchanged per the record.
- Cut the orientation-section signpost "That is the fact every quoted rating below
  has to be read through, and it is the one most easily dropped."
- Cut the "175th" section-opening signpost "Here is where a number gets away from
  its conditions."
- Recast "The most useful line in that paper is a comparison inside one model" to
  "The sharpest comparison in that paper is inside a single model."
- Changed "beats a named human, OpenAI's own chief scientist" to "beats a specific
  person, OpenAI's own chief scientist."
- Re-ran `nb check` (links off): BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

None. All findings were fixable by direct edit; the chart is correct (its numbers
match the script, the evidence, and the cited primaries, and its three reference
thresholds are unchanged since 2013, so dating them is honest), and no evidence
gap or source-policy failure remains for the researcher or writer. The orchestrator
stamps the edited article and the writer runs the final proof (links on) as the
normal next step.

## Decision

approve — the spine is sourced and honors both of the record's corrections, the
formula opener and restating dek are fixed, the slop edges are cut, and the chart
is honest.

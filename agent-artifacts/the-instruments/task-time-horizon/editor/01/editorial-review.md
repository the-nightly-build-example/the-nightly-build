# Editorial review: the-instruments/task-time-horizon (editor/01)

## Skeptic

Thesis: METR's task time horizon is a 50%-success task length fitted to a
software task suite, not a statement of capability; the seven-month doubling of
that length is a real measurement, but the calendar of automated work-months laid
over it is an extrapolation, one the paper's own five-year projection helped seed.
The piece states this clearly and every part of it can be read off the draft
alone.

The claims it stands on, and how each held:

- Claude 3.7 Sonnet's 50% horizon is 59 minutes; the abstract rounds to "around
  50 minutes" and METR's blog to "approximately one hour." Verified against the
  paper abstract ("50% time horizon of around 50 minutes"), the March blog
  ("approximately one hour ... where its fitted logistic curve intersects the 50%
  ... threshold"), and Ord's writeup, which gives the exact fitted 59 vs 15 minute
  pair. Held.
- The number is built from 170 timed tasks (66 SWAA, 97 HCAST, 7 RE-Bench),
  binary-scored, logistic fit of success against log human time, horizon read at
  the 0.5 crossing. Verified against the paper (Sections 3.1.1-3.1.3; abstract
  "170 tasks"). The log-difference-zero -> sigmoid-one-half derivation is correct.
  Held.
- 80% horizon is about 15 minutes, so the 50% mark is not reliability. Verified
  (paper 4.2.1; Ord). Held.
- Doubling 212 days, 95% bootstrap CI 171-249. Verified verbatim in the paper.
  Held.
- The acceleration is contested. The paper itself calls the recent speed-up
  "difficult to distinguish from noise," and METR's 2026 update moves the
  post-2023 doubling to 131 days, partly on task composition. Both verified
  (paper 4.2; Time Horizon 1.1: "post-2023 doubling-time is 131 days ... 20% more
  rapid," attributed to a "slightly different distribution of difficulty"). Held.
- Domain limit: the paper was retitled to "...Long Software Tasks"; the same
  method yields horizons 40-100x shorter on visual computer-use tasks and under
  one doubling per year on Tesla FSD. Verified (current arXiv title; domains blog
  "40-100x shorter," "Tesla FSD ... around 0.6 doublings / year"). Held.
- The over-read is partly the authors' own: the paper projects that "within 5
  years" agents may automate month-long software tasks; AI Digest turns the
  doubling into "A new Moore's Law for AI agents" with 2027/2028/2029 milestones.
  Both verified (paper abstract; AI Digest page). Held; the draft correctly does
  not frame the misread as purely external.
- Skeptic weight: Ord's constant-hazard/half-life reframing carries real weight
  and is then honestly undercut by Ord's own human-baseliner finding (humans
  above 20% at 12h where constant hazard predicts ~6%) and his concession that
  the assumption does not hold exactly. Verified (Ord writeup; his Feb 2026 update
  citing Hamilton). Held.

Pushing hardest on the claim I most wanted to keep, the "AI-written pull requests"
line: the cited review (Davis) calls them "SWE-bench pull requests," not
AI-written. I traced it to the owning METR note, which reviewed 296 AI-generated
contributions from five models, so "AI-written" is faithful to the underlying
finding and clearer for a reader who has not met SWE-bench. Left as written.

Every citation href was opened as printed and resolves to its source. Two
citation gaps found and fixed with sources already in the article: the orientation
sentence attributed the abstract's "around 50 minutes" and the 59-minute fitted
value while citing only the blog, and the direct quote "difficult to distinguish
from noise" (the paper's own words) carried no citation. Both now cite the paper.

Asset: Figure 1's in-image title reads "169 ... tasks" while the prose and record
give 170. The image is the unaltered primary artifact; the caption and alt text
make no count claim and no display text asserts a task number, so nothing
contradicts the image. The crop keeps the log axis, the release-date axis, every
point, the trend line, its band, and the dashed extrapolation past the last model,
which is exactly the evidence the argument spends. The asset earns its place; kept.

## Cut

The prose is clean and holds the plain, unhurried register the voice guide asks
for; it builds the number in front of the reader rather than summarizing it. Few
sentences failed the slop test. One filler transition, "That is what happened
next," was cut. One body sentence broke the template rule that only the bookends
refer to the lesson: "and later in this lesson it wobbles" narrated the piece's
own structure. Rewritten to "and it does not hold exactly," which keeps the
honest foreshadowing without the self-reference.

The negative-parallelism "X, not Y" figures ("not a task it can be trusted to
finish," "even, not ... safe," "a crossover, not a capability," "narrow" not
"wrong") each correct a misconception the piece actually names, so they survive
the earned-contrast test. Semicolons are confined to tight parallel pairs. No
prompt leakage: the reader-situation language in the opener is reported fact, not
a lifted instruction, and no sentence claims the article fulfilled its brief. No
borrowed phrasing from the voice-guide exemplars; the worked 59-minute-task case
emulates Ortiz-Ospina's method, not his words, as the guide intends.

Against the recent-pattern notes: the dek states this piece's own particular (170
tasks, the doubling, the calendar) and matches none of the banned molds. The
"By the end you will be able to..." bookend formula is present only in a softened
two-clause form on this lesson's own particulars and resolves in the takeaway, so
it stays. Headings are in the piece's nouns and vary in construction; only one
uses a comma-and-"and" join, not a repeated pattern. The last body section does
not close on a stamped one-liner. No shared "metric everyone misreads" framing
with the mixture-of-experts sibling.

## Reader

Read straight through as the paper's reader, what I have that the sources alone
would not give me: the number assembled mechanically, the 80% collapse to 15
minutes that shows 50% is not capability, and the seam between the measured
doubling and the drawn-in calendar traced back to the authors' own five-year
projection. The evidence record states these sit in the sources as separate facts
it does not connect, so the synthesis is the article's own; the draft-handoff's
original-work sentence matches what the piece delivers. The prose sits closer to
the voice-guide exemplars than to a median summary. The headline is the largest
claim and the piece defends it.

## Edits

- Rewrote "and later in this lesson it wobbles" to "and it does not hold exactly"
  (removed a body self-reference the template bars outside the bookends).
- Split the orientation citation so the blog's "approximately one hour" cites the
  blog [2] and the abstract's "around 50 minutes" plus the 59-minute fitted value
  cite the paper [1].
- Added citation [1] to the paper's own quoted phrase "difficult to distinguish
  from noise."
- Cut the filler transition "That is what happened next."

## Required work

None blocking. The orchestrator re-runs the proof and stamps after these edits;
the edits add no new prose that needs reporting and touch no number, name, date,
quotation, asset, or chart provenance.

## Decision: approve

The number is built honestly and in the right order, every load-bearing figure
checks out against the owning primary, the domain limit and the contested
acceleration are stated as such, the skeptic carries real weight, and the asset is
honest evidence; the remaining defects were mine to fix and are fixed.

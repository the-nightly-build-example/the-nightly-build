# Editorial review: the-instruments/gaia (editor/01)

## Skeptic

Thesis: a GAIA score means one thing on the withheld test set and another on the
public validation set, so before trusting any GAIA number you have to ask which
split produced it. The claims it stands on:

1. Deep Research's "state of the art on GAIA" 67.36 percent was a validation-set
   figure, not a leaderboard rank. Held. OpenAI's announcement owns the SOTA
   framing and date (s1, gated 403 but live and correct); the 67.36 / 47.6-on-L3
   read value and the "validation set" scope come from the Hugging Face post
   (s2), which I opened and which reports both figures verbatim, authored by a
   team including GAIA co-author Clémentine Fourrier. The article correctly cites
   the claim to s1 and the number to s2.
2. The validation set is contaminated and the leaderboard runs on the withheld
   test set only. Held. s5 (dataset card, gated but live) owns the no-reshare
   gating; s6 owns "widely available online ... might have 'memorized' them"
   (opened and matched word for word); s4 (leaderboard Space) owns the test-set-
   only scoring.
3. The cost is a cross-set comparison that does not hold: a 75 (test) and a 67
   (validation) do not rank one system over the other. Held. H2O.ai's blog (s7,
   opened) states its 75 percent is on the test set "with no known data leaks"
   and that Deep Research and Manus "were evaluated on validation data," dated 17
   March 2025 — every quoted fragment in the article is an exact substring.
   JoyAgent-JDGenie (s8, HTML read) reports validation pass@1 75.2 and test
   pass@1 67.1; the article's "eight points lower on the same system" is 75.2 −
   67.1 = 8.1, sound, and it compares like metric to like (both pass@1).
4. A high test-set score still does not show the system beats people. Held on the
   sourced facts: human 92 percent (annotator, s3) versus the highest verified
   test score of 75 percent (s7). The draft also asserted the "beats humans"
   reading is fed by "validation figures that approach or exceed 90 percent." No
   source in the record owns a 90-plus validation figure — s6 (the attached
   citation) covers only memorization, and the record's one 90-plus number
   (steel.dev 92.36) is in Discarded with "do not cite the number." I cut the
   figure (see Edits); the surrounding point survives on s6.

Display text, descriptor by descriptor. Headline: Deep Research's SOTA claim was
on the public set — matches s1/s2, and it breaks the desk's number-forward habit.
Dek: 466 tasks, most withheld because the public ones leak — 466 and the
withheld/leak mechanism are the paper's (s3) and s6's; it identifies rather than
restates the headline. Author line "led by Grégoire Mialon, with co-authors
including Clémentine Fourrier, Thomas Wolf, and Yann LeCun" — the arXiv author
order is Mialon, Fourrier, Swift, Wolf, LeCun, Scialom, so "led by Mialon" and
"including" are accurate and non-exhaustive. Levels 146 / 245 / 75 and their
step/tool definitions, 166 released / 300 withheld, the "6 to 17 minutes"
annotator time, quasi-exact match and the `YOUR FINAL ANSWER should be ...`
instruction, 92 percent / 15 percent, Level 3 solved none — all confirmed against
the paper's full HTML (s3). Dates (2 Feb 2025, 17 Mar 2025) match their primaries.

data-nb-kind audit: s1/s3/s4/s5 primary and s7/s8 primary (each owns the claim it
carries: OpenAI's announcement, the benchmark paper, the leaderboard operator, the
dataset host, H2O's own result, JD's own result); s2/s6/s9 secondary (report on
figures they do not own). Every label matches the evidence record and the
primary/secondary test. Nine sources, six primary — above the floor.

Every citation href opened as printed. s1 and s5 return gated statuses (403/401)
documented in the evidence record; both land on the real source and reach a human
who clicks, so they pass. All four internal cross-links (livecodebench, tau-bench,
swe-bench, task-time-horizon, tool-use) resolve in the library, and the neighbor
lessons are plain prose links, not sources, as the brief required. No citation
points at an endpoint standing in for the source.

The round's number cautions hold: no live-leaderboard standing is asserted, every
recent figure is anchored to its dated primary, the "highest verified test-set
score is 75 percent" is scoped "in this record," and no per-level human/model
split is stated at a precision the record does not support.

## Cut

Slop pass, every sentence including display text and furniture. Two body
sentences failed and were cut: "Those two sets are the number pair this lesson
keeps apart" and "Everything downstream turns on not letting them blur." The
first mentions "this lesson" in the body, which the template forbids outside the
two bookends; both are method signposts that report where the argument is going
rather than advancing it, and the public/withheld pair is already named by the
facts in the two sentences before them. The paragraph now closes on the withheld-
answers fact.

The edge pass caught nothing else. I tested the short concession "That is a real
and difficult thing to do" and the transition "Return to OpenAI's claim" against
the delete test; the first carries the pivot the balanced analysis turns on and
the second is a functional reorientation, not an empty edge, so both stand. The
closers of every section and the article's last sentence carry a fact or a
reasoning step. The dek was checked against the desk's flagged "concrete clause +
comma + and/while/because twist" mold: the clause after its comma opens on "most
of them," not a conjunction, so it varies the build rather than repeating it, and
it is none of the three banned dek molds. Headings are argument-step sentences in
the piece's own nouns, varied in build, none scaffolding. No borrowed phrasing
from the voice-guide exemplars and no prompt leakage: the neighbor-differentiation
sentence renders the commission's distinctness ask in the article's own reported
terms.

Furniture: the body closed with a `Verdict` note restating the finding. The press
editorial direction bans that outright — the takeaway bookend is where a lesson
lands its judgment, and a closing Verdict block is a leftover from the paper's
earlier template. Removed. Its instruction ("ask which set it came from") already
lives in the takeaway, so nothing was lost, and its s4 citation is carried
elsewhere. What remains — stat strip, level table, the quasi-exact-match note — is
varied and load-bearing, and the piece reads as a continuous article.

## Reader

Reading what survives straight through: I come away with one portable test — ask
which split a GAIA number came from — and a concrete size for the gap it guards
against, JoyAgent's eight points on a single system. No one source hands that
over; the paper, the leaderboard config, the H2O post, and the JD report each
carry a piece, and the article is what assembles them into the question to ask of
any GAIA number and shows the cost of not asking. That matches the draft
handoff's original-work statement, and the answer survives. The prose sits closer
to the voice-guide exemplars than to a median summary: it opens on the two numbers
the way Alexander opens on his IQ figures, keeps validation and test from blurring
the way Drum keeps incidence from death rate, and credits the correction to named
parties (H2O.ai, JD's own report) rather than presenting it as the writer's catch.
The headline, read as the largest claim, is one the piece defends.

## Edits

- Cut "Those two sets are the number pair this lesson keeps apart. Everything downstream turns on not letting them blur." from the orientation section (body self-reference plus method signpost).
- Cut the unsupported figure "approach or exceed 90 percent, the ones" so the sentence reads "The validation figures that feed 'assistants beat humans' sit on the set a model can memorize"; no source owns a 90-plus validation figure and the attached s6 supports only the memorization clause.
- Removed the closing `Verdict` note from the "what-it-licenses" section (press direction bans a body-closing Verdict block; the takeaway carries the judgment).
- Restored "of them" to the Background row-02 link label so it matches the tau-bench article's actual headline ("under 25% of them eight times in a row").

## Required work

- orchestrator: re-stamp the article. My cuts drop the body by roughly sixty words, so the `words` (1920) and `reading_minutes` (8) fields in the nb-meta block are now stale. `nb check` stays BLOCK: 0, WARN: 1 (the intended density warning); the stamp only needs to refresh the computed counts before the PR.
- researcher (non-blocking, future rounds only): the "beats humans" case is now supported qualitatively — no verified validation-set figure in the record reaches the 92 percent human bar. If a later round wants to quantify it, it needs a validation-set primary that resolves against a source, not a live-leaderboard aggregator.

## Decision

approve — every load-bearing figure, date, name, and quote verifies against the
opened primaries, and the two prose faults plus the banned Verdict block were
fixable directly, leaving the article at BLOCK: 0 with no reporting owed.

Production record: reviewed as claude-opus-4-8 (Opus 4.8), effort=high.

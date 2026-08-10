# Editorial review: the-instruments/alpacaeval (editor/01)

## Skeptic

Thesis: an AlpacaEval win rate is one language model's preference over a named
reference on a fixed prompt set, not an accuracy; that preference tilts toward
the longer answer; so a win rate only means something beside its version, judge,
and reference. The piece stands on five claims.

1. A win rate is the fraction of 805 fixed prompts on which a GPT-4 judge prefers
   the model's answer to a reference's, a preference share and not a measure of
   correctness. Opened the tatsu-lab README (source 2): it defines the metric as
   "the fraction of time the model's output is preferred over the reference's,"
   names the 805-example set, text-davinci-003 as the 1.0 baseline, and the GPT-4
   annotator. Confirmed. The back-out arithmetic in the how-computed section
   (0.9060 x 805, about 730) recomputes to 729.3; "about 730" holds.

2. Zephyr-7B reported 90.60% on AlpacaEval 1.0. Opened the Zephyr paper (source 1,
   arxiv abstract renders only the abstract, but the evidence record verifies
   90.60 in Table 1) and the model card (source 6), which shows "AlpacaEval (win
   rate %): 90.60" and no 2.0 or length-controlled figure, exactly as the article
   states. Confirmed.

3. The length swing: the same model's AlpacaEval 2.0 win rate moves 22.9% to 64.3%
   by changing only a verbosity instruction. Opened Dubois et al. (source 3). The
   abstract confirms the 0.94-to-0.98 correlation directly; the 22.9-to-64.3 swing
   and the 41.9-to-51.6 corrected swing sit in Section 4.1, verified in the
   evidence record against the PDF. The article labels the swing AlpacaEval 2.0,
   one model, verbosity-only. Direction correct: more verbose scores higher.

4. Length control helps but does not close the bias: a null model scores 76.9% raw
   and 86.5% length-controlled on AlpacaEval 2.0, the debiased number coming out
   higher. Opened Zheng et al. (source 5); abstract confirms the 86.5% LC figure,
   evidence record verifies the 76.9% raw. The article states plainly that length
   control makes verbosity-winning harder, not impossible. This is the brief's
   "do not present length control as a complete fix," and the draft honors it.

5. The reference sets the bar, so zephyr-7b-beta reads 90.60% under 1.0 and 13.20%
   LC / 10.99% raw under 2.0 with nothing about the model changed. Pulled the
   zephyr-7b-beta row from the raw AlpacaEval 2.0 leaderboard CSV (source 7):
   win_rate 10.992..., length_controlled_winrate 13.203..., avg_length 1444,
   n_total 805. The article's 13.20% LC and 10.99% raw are exact. The evidence
   record's own contradictions note supplies "weak reference / strong reference"
   for the two baselines, so "a weak model" is supported.

Citations opened, every href as printed. All seven land on their source: the two
arxiv abstracts (1, 3, 5), the README (2), the Moonlight review (4, confirmed a
third-party summary stating 0.98 versus 0.94, correctly labeled secondary), the
model card (6), and the leaderboard CSV blob (7, the repo's own file page). The
two internal Background links resolve to published lessons whose titles match the
printed anchor text (llm-as-a-judge, chatbot-arena-elo), and both Go-deeper
external links (the Dubois abstract and the live leaderboard) resolve.

Every `data-nb-kind` checks out: six primaries authored by the owning parties
(benchmark repo, the two arxiv method papers, the null-model paper, the model
card, the leaderboard data) and one secondary (Moonlight, an independent
retelling, not an independent author of the figure). Primary count 6 clears the
floor of 4; one secondary clears the floor of 1.

One break, fixed directly: the reference section dated text-davinci-003 to 2022,
a date the evidence record does not carry. Dates are protected, so I cut the year
and kept "a weak model," which the record supports. No central claim broke; no
routing needed from the skeptic read.

Source-count warning (W-SOURCES-MIN, 7 versus the floor of 8): the warning stands,
and the press rule justifies it. The evidence record holds eight sources. Seven
are cited as numbered sources (all six primaries other than Chatbot Arena, plus
the one secondary). The eighth, Chatbot Arena (Chiang et al.), is taught ground:
the course covers it in the-instruments/chatbot-arena-elo, and press/editorial.md
requires taught ground to be a plain prose link, never a numbered source. It is
linked in prose at "Chatbot Arena" and as a Background row. No displayed claim is
owned by an uncited primary that could lawfully become source 8: the review
brief named the 2.0 leaderboard CSV and the Zephyr model card as candidates, but
both are already cited (7 and 6). So the floor cannot be reached without either
citing taught ground (a press-rule violation) or padding. The warning is correct
to stand.

## Cut

Six sentences failed a pass; I made five prose fixes and one reorder.

The recurring pattern was body self-reference and signposting, which the lesson
template confines to the two bookend cards. Two body sentences narrated the
article instead of teaching. "That one fact carries the surprise this lesson is
about" both mentioned the lesson from inside the body and announced a surprise it
had not yet delivered; deleted, and the flanking sentences carry the point whole.
"That is the rule to carry away" gestured at the reader from the body and stated
nothing the next sentence did not; deleted, and the paragraph now opens on the
rule itself.

One puffery cut: "the clearest demonstration comes from the AlpacaEval team's own
follow-up work" graded the evidence before showing it. Rewritten to "the
AlpacaEval team's own follow-up work shows what else moves it," which keeps the
attribution and drops the superlative.

One correctness fix: the length-control section called the Spearman correlation
"a zero-to-one measure," which misstates a statistic the lesson is teaching (its
range is minus one to one). Changed to "a measure of how closely two rankings
agree, running up to one for a perfect match," which is accurate and still anchors
the 0.94-to-0.98 reading against a ceiling of one.

One tic broken: the takeaway opened on a restated definition ("An AlpacaEval win
rate tells you how often..."), the exact takeaway pattern the commission and brief
flagged. Reordered to lead with the finding, "An AlpacaEval win rate is a
preference, not a grade," folding the definition into the sentence that follows.
No content added or removed.

The remaining edge sentences survive the delete test. The takeaway closer holds
the Tim Harford balance the voice guide asks for ("Read with those questions in
hand, an AlpacaEval win rate is worth having. Read as a bare percentage, it will
mislead you") and states the earned conclusion. Negative-parallelism instances
("a preference, not an accuracy"; "not answering better") each correct a
misconception the piece names, the test-score reading, so they stay. Headline and
dek break the desk's "two measures disagree / both are true" reveal that fid,
tokens-per-second, and energy-per-query all run; the 90.60/13.20 contrast lives
mid-body as a worked case rather than the hook. No dek mold from spec/headlines.md
appears. Headings read as steps in AlpacaEval's own nouns, none matching fid's
"Where the number keeps its word." No prompt leakage: the comparability rule and
the preference framing are the article's reported findings, not lifted from the
commission's sentences. Furniture is used, not stacked: numbered steps for the
computation and one table for the two-setting Zephyr comparison, each earning its
place.

I considered whether the dek should pin the 22.9-to-64.3 swing to version 2.0.
It is accurate and not mis-attributed, the body pins it one section later, and a
version label would clutter a dek whose job is to show the size of the length
effect. Left as is. I also considered requesting the Dubois verbosity figure or
scatter as a source asset; the prose, the step list, and the table carry the
argument, so a figure is optional and I am not requiring it.

## Reader

Reading what survives straight through, what I have that the sources alone would
not give me: a single worked path that uses Zephyr's one headline number to walk
from a win rate that looks like a test score, through the judge-and-reference
computation, to the resolution of the 90.60 / 13.20 split as "the bar moved" and
a portable rule for reading any win rate by version, judge, and reference. The
sources hold these figures separately; none assembles them into that path. The
draft-handoff's original-work sentence claims exactly this assembly, and it
survives. The prose sits closer to the voice-guide exemplars than to a median
summary: it works the count in front of the reader in Julia Evans's manner
(0.9060 x 805, about 730), names the length effect in AlpacaEval's own parts as
Dan Luu names a specific cause, and lands the Harford balance in the takeaway.
The headline is the largest claim and the piece defends it.

## Edits

- Deleted body self-reference/signpost "That one fact carries the surprise this lesson is about" in the orientation section.
- Rewrote "the clearest demonstration comes from the AlpacaEval team's own follow-up work" to remove the graded superlative.
- Corrected the Spearman correlation from "a zero-to-one measure" to "a measure ... running up to one for a perfect match."
- Cut the unsupported date "from 2022" describing text-davinci-003, keeping "a weak model."
- Deleted body signpost "That is the rule to carry away" so the paragraph opens on the rule itself.
- Reordered the takeaway opener to lead with the finding ("a preference, not a grade") instead of a restated definition.

## Required work

- orchestrator: re-stamp the article and re-run the proof. My edits changed body
  prose (five cuts/rewrites and one reorder), so the stamped word count needs
  refreshing. No citations, numbers, names, dates, or claims changed, and no link
  set changed.
- orchestrator: accept the W-SOURCES-MIN warning (7 versus 8) as intentionally
  left, on the recorded press-rule ground that the eighth evidence source
  (Chatbot Arena) is taught ground and must remain a prose link, and no displayed
  claim is owned by an uncited primary. No researcher or writer work is needed for
  it.

## Decision

approve, with the source-count warning intentionally left and justified; the edits
are direct prose cuts and one reorder that need only a re-stamp and re-proof, not
another editorial round.

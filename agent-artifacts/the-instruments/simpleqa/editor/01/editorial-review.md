# Editorial review: the-instruments/simpleqa (editor/01)

## Skeptic

Thesis: GPT-4.5's reported "37% hallucination rate" is the wrong-answer share of
one SimpleQA run, and because SimpleQA keeps only questions a strong model
already missed and grades a declined answer apart from a wrong one, that share is
not a measure of how often a model fabricates. The piece stands on four claims.

Claim 1 — "62.5% correct" and "37% hallucinated" are the same GPT-4.5 run under
two names. Held. simple-evals lists GPT-4.5 at 62.5 correct; the incorrect share
is its complement; ABC restates that share as "hallucinated 37 per cent of the
time." I opened the simple-evals page (62.5 present) and the ABC report (the 37%
and 62% phrasings both present). The stat strip and orientation keep both figures
on GPT-4.5, so the identity is stated cleanly, not conflated with GPT-4o's own
~62% wrong share.

Claim 2 — adversarial selection (a question survives only if at least one of four
GPT-4-class completions was wrong). Held against the paper (s3, §2.1) as read in
the evidence record; the three numbered steps state the rule correctly and the
4,326 count, the ~94% third-trainer agreement, and the ~3% label-error estimate
all match the record.

Claim 3 — three-way grading with abstention scored apart from error. Held. The
grade definitions match Table 2. I recomputed the table: every row sums to 100
(38.2+1.0+60.8; 8.6+0.9+90.5; 28.9+35.0+36.1; 42.7+9.2+48.1), and correct-given-
attempted checks out (Claude 28.9/65.0 = 44.5; o1-preview 42.7/90.8 = 47.0). The
Claude-vs-GPT-4o reversal on attempted questions (44.5 vs 38.0) is stated in the
right direction.

Claim 4 — the "hallucination rate" name is OpenAI's own, from the o1 system card,
not the reporter's. Held. The o1 card (s4) href lands on the correct paper; the
evidence record read its "Hallucination Evaluations" table directly, and for
GPT-4o the 0.38/0.61 split confirms the "hallucination rate" is just the SimpleQA
incorrect share.

Attribution beat (the round's focus). Two of the three attributions are exactly
right: the relabel is sourced to the o1 card (s4), and the GPT-4.5 card's
hallucination table is correctly said to use PersonQA, not SimpleQA (s5 href
resolves to the real card PDF; content per the evidence record). The third was a
miscitation. The draft attributed the pairing "62.5 percent correct, 37.1 percent
wrong" to the simple-evals leaderboard (s2), but opening s2 shows only 62.5 — the
precise 37.1 appears on AIMon (s8), not simple-evals, and the evidence record
sources it there too. Fixed directly: s2 now carries only the 62.5 it owns, and
the ~37% is stated as that run's wrong-answer share (the complement of 62.5),
consistent with the orientation's own "about 37 percent." No source was dropped;
s8 and s2 both remain cited, count unchanged at 8.

Numbered-source judgment (s7 / TruthfulQA). Ruled permissible. The truthfulqa NB
lesson is linked in prose (and in Background), never as a numbered source; s7 is
the external TruthfulQA arXiv paper (href resolves; 817 questions / human
misconceptions confirmed), cited for one genuine external contrast fact, not to
re-teach taught ground. The floor of 8 holds and nothing routes to the
researcher.

Display text checked descriptor by descriptor: headline, dek, four subheads,
stat-strip labels, and table caption. All land on claims the piece defends; dates
(o1 card December 2024, GPT-4.5 card 27 February 2025, ABC March 2025) and the
one named critic (Daswin de Silva, quote verified in the ABC report) are correct.
All eight data-nb-kind labels pass the primary/secondary test: the paper, the two
system cards, simple-evals, DeepSeek-V3, and TruthfulQA each own the number cited
to them (primary); ABC and AIMon are outside reporting (secondary). Six primary,
two secondary — policy met. Every citation href was opened; all land on the
source itself and the five internal library links resolve to real, correctly
titled articles.

## Cut

Six sentences failed the slop test, all at edges, and all were cut or trimmed
rather than repaired:

- An orientation section-closer that was half thesis, half method-signpost ("...
  it helps to watch the score get built") — kept the thesis as a standalone
  claim, dropped the signpost.
- An emphasis signpost ("That last step is the one to hold onto") opening the
  analysis paragraph — cut; the substantive claim now opens it.
- An empty magnitude opener ("The gap this opens is wide") — cut; the figures
  that follow show the gap.
- A reader-directed imperative ("Return to the 37 percent") in body prose, which
  the lesson template forbids the body — cut; the section heading carries the
  transition.
- An empty topic sentence ("The confusion spreads easily") — cut; the paragraph
  opens on the PersonQA/simple-evals mix-up and its closer states the point.

No borrowed phrasing from the voice-guide exemplars survived into the draft: the
numbered-steps checklist echoes Recht's flat rhythm as a structural move, in
SimpleQA's own nouns, which the guide sanctions. No prompt leakage: the
construction terms are the subject's, not the brief's. Against the recent-pattern
notes, the dek is not a comma triad or a two-clause "and" contrast (one subject,
compound predicate, then a consequence), the opener carries no "by the end you
will know" syllabus-closer, and the four headings are built differently from one
another and reconstruct this argument in this benchmark's nouns. The two earned
negative-parallelism lines ("the design working as intended, not a verdict...";
"not a measure of how often the model invents facts... It is how often the model
guessed wrong...") both correct the exact misconception the piece names, so both
stay. Furniture — stat strip, numbered steps, table, one note — is all documented
and each piece does work no prose rearrangement would; nothing is a stack-of-
blocks filler and no component was added or removed.

## Reader

Read straight through, the piece gives a reader who has read nothing else a
single causal account: a SimpleQA percentage is accuracy on deliberately hard,
obscure-fact questions where abstaining is scored apart from error, so the
incorrect share that OpenAI's own o1 card renamed a "hallucination rate," and
that coverage carried forward, cannot be read as how often a model makes things
up. No one source carries that chain — the paper owns the construction, the o1
card owns the relabel, AIMon and ABC own the misreading — and the article is what
assembles them, which matches the writer's original-work statement. The prose
sits closer to the voice-guide exemplars than to a median summary: dated and
counted mechanisms, the abstention split shown through the Claude-vs-GPT-4o
reversal rather than asserted, the verdict landed plainly ("As a way to compare
models on that narrow skill, the number is fair. As an estimate of how much any
one of them makes up, it is a poor one"). The headline is the largest claim and
the piece earns it.

## Edits

- Reworded the s2 attribution so simple-evals carries only the 62.5 it prints;
  the ~37% is now stated as that run's wrong-answer share, dropping the "37.1
  percent" that simple-evals does not report.
- Takeaway: "a strong model had already missed one like it" changed to "had
  already gotten it wrong," matching the per-question keep rule the body teaches.
- Cut the orientation closer's method-signpost, keeping "Only the first label is
  fair to the test."
- Cut "That last step is the one to hold onto" from the selection analysis.
- Cut "The gap this opens is wide" from the grading paragraph.
- Cut "Return to the 37 percent" from the relabel section.
- Cut "The confusion spreads easily" from the PersonQA paragraph.

## Required work

None. No item routes to researcher, writer, or orchestrator. (The writer re-runs
the proof and the orchestrator stamps after these edits, per the standing flow;
the edits touch prose and one citation attribution only, not sources, furniture
markup, assets, or chart provenance.)

## Decision

Approve. The spine, the two mechanisms, and the attributions are correct after
one miscitation fix; the round's focus items all resolve, the source floor holds
at 8, and the edge slop is cut.

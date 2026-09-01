# Editorial review: the-instruments/imo-gold (editor/01)

## Skeptic

Thesis: an IMO gold is a proof scored by hand against a rubric, so the grader is
part of the number, and in 2025 two labs reported the identical 35/42 gold that
were not the same measurement because only one was graded under official IMO
coordination.

The claims it stands on, and how each held:

1. The IMO score is a human-graded proof score with year-relative cutoffs (six
   problems, seven points, 42 total; coordinators mark against a confidential
   scheme; medal lines set by that year's contestants). Verified against the
   IMO 2025 results page (s1: gold cutoff 35, 72 gold of 630) and the
   coordinator account (s2: confidential marking schemes, on-the-spot requests
   are not the real process, no formal AI rules). Held.

2. 2024 DeepMind silver: 28/42, four of six, statements hand-translated into
   Lean, up to three days, scored by two enlisted mathematicians (Gowers,
   Myers). Verified verbatim against the DeepMind 2024 blog (s3). The "one point
   under gold" reading checks against the IMO 2024 page (s4: gold 29, silver 22).
   Held.

3. The load-bearing contrast — who graded what. DeepMind 2025: 35/42, five of
   six, natural language from official statements, within 4.5 hours, officially
   graded and certified by IMO coordinators; the IMO president confirms the score
   on the page. Verified against the DeepMind 2025 blog (s5), Dolinar quote
   verbatim. OpenAI 2025: 35/42, five of six, two 4.5-hour sessions, no tools,
   graded by three former IMO medalists to unanimous consensus, outside the
   official cohort, after declining the Lean track. Verified through Willison's
   verbatim reproduction (s7) and Brown's timing account (s8). Both 35s equal the
   exact 2025 gold cutoff. Held — this is the strongest claim and it survives the
   hardest push: the three former medalists are not IMO coordinators acting
   officially, so "the IMO graded only one" is precisely true.

4. A gold certifies particular problems under particular conditions, not general
   research ability, and even the certified result carries the graders' own
   caution. Verified against Buzzard (s11: "a million miles away" from research
   mathematics; embargo "informal"; OpenAI marked by former contestants, "no
   rules") and CBS/Dolinar (s12: organizers could not verify compute or human
   involvement — carried in the draft as attributed reporting, which matches the
   source, a reporter's attribution rather than a direct quote). Held.

Every citation href was opened as printed. All resolve to the source itself. The
two X posts (s6 OpenAI/Wei, s8 Brown) serve their own pages behind a login wall
and return the content to an authenticated reader; Willison (s7) is cited
alongside s6 as the accessible transcript. These are gated, not dead. imo2025.au
(s9) bot-blocks a bare client but serves the page; the LessWrong linkpost (s2)
rate-limited once and is live. Every `data-nb-kind` label matches the
primary/secondary test: the labs' announcements, the IMO pages, the coordinator's
firsthand account, and Brown's own thread are primary; the round-ups, the
transcript, and CBS are secondary.

One break with the evidence, fixed directly: the conditions section claimed both
2025 golds "sat on the floor of the gold band, at 35, one point above the 28 that
counted as silver the year before." Thirty-five is seven points above 28, not
one; the "one point" belongs to 2024's 28-under-29, which the 2024 section
already states correctly. I cut the false comparison and reframed the sentence to
the true, non-redundant caveat the evidence's Numbers section flags — both golds
landed at the very bottom of the gold band, the lowest score the medal allowed —
supported by s1, and dropped the s4 citation the deleted clause had carried (s4
remains cited in the 2024 section).

The embargo handling is clean. The draft states OpenAI announced early relative
to what cooperating labs understood, attributes the specific July 28 date to
Samin (outside commentator) and Brown's contrary account to a party in a position
to know, and says plainly that "whether OpenAI broke any agreement is disputed,
and no one who would know has settled it." It makes no impropriety or
broken-embargo assertion. Confirmed as required by the brief.

## Cut

Six sentences failed a standard on the second read; all were fixable in place, so
nothing routed.

Clarity collision on "script." The Why bookend uses "a benchmark that a script
grades," where script means an automated program, and orientation reuses it
correctly ("a script matches it against a key"). But three later uses meant the
opposite thing — a contestant's written answer sheet — which for a new reader
collides with the program sense, and "model scripts" could even be misread as the
model's code. I reserved "script" for the program sense and renamed the answer
sheet to "solution" throughout: "A solution can land anywhere from zero to a full
seven"; "the same criteria applied to student solutions" (which also restores the
DeepMind primary's own wording); "asking coordinators to evaluate the models'
written solutions on the spot."

Two method signposts cut under the delete test: "which makes them a good place to
start" (the 2024 opener graded the article's own structure) and "and it is worth
stating carefully" (the timing opener narrated the writer's care). Both leave a
clean claim behind.

Two semicolons joining merely parallel independent clauses became periods, per
the house rule that a semicolon is for clauses a period would over-separate and
the period is the default otherwise: the GSM8K/FrontierMath contrast and the
July 19 / July 21 posting dates.

No negative-parallelism failures survived scrutiny: the three "not Y" turns ("not
a benchmark that a script grades," "not a percentage correct," "not on-the-spot
marking") each correct a misconception the lesson names and is built on, so each
is earned. No puffery, no decorative-analysis copulas, no vague attribution
(every actor named), no unearned punchline. The edge sentences hold: the body
closes on an earned thesis line, and the takeaway resolves the opener's three
questions. Against the recent-pattern notes, the piece breaks each flagged mold —
the dek states its finding with no number and no comma-triad, the openers avoid
"what X is counting," the body does not close on a bare grading assessment, and
no heading uses a comma-and join. No borrowed phrasing from the voice-guide
exemplars, and no prompt leakage: the three-question test is the writer's own
synthesis, credited in the draft handoff. The note (Dolinar certification) and the
table (three results, problem-statement to grader) each earn their place and are
not a stack.

## Reader

Read straight through, the piece gives the reader a reusable lens the sources do
not: three questions — who wrote the problem statements, how long the model had,
who graded — applied across the 2024 silver and both 2025 golds in one table, so
two identical 35/42 scores read as two different measurements. No single source
assembles that comparison; DeepMind's blogs, OpenAI's posts, and the IMO pages
each own one piece. The draft handoff's original-work sentence claims exactly this
comparison and test, and it survives. The prose sits with the voice-guide
exemplars, not a median summary: conditions are stated flat as facts and the
judgment rides on them, the way Mitchell names the two rules a score broke and
Willison holds a shipped model apart from the variants beside it. The headline is
the largest claim and the piece defends it: "the IMO graded only one" is exactly
what the grading route establishes.

## Edits

- Orientation: "A script can land anywhere from zero to a full seven" changed to
  "A solution can land..." to end the collision with the program sense of script.
- Orientation: GSM8K/FrontierMath semicolon changed to a period.
- 2024 section opener: cut the signpost "which makes them a good place to start."
- 2025 DeepMind paragraph: "the same criteria applied to student scripts" changed
  to "student solutions" (clarity, and matches the DeepMind primary).
- Coordinator paragraph: "evaluate model scripts on the spot" changed to
  "evaluate the models' written solutions on the spot."
- Timing paragraph: cut the signpost "and it is worth stating carefully"; changed
  the July 19 / July 21 semicolon to a period.
- Conditions paragraph: replaced the false "at 35, one point above the 28 that
  counted as silver the year before" with "sat at the very bottom of the gold
  band, the lowest score the medal allowed that year"; dropped the s4 citation the
  cut clause carried; cut the signpost opener "Read with everything around them."

## Required work

- writer: re-run the proof over the edited article before the orchestrator stamps
  it. All edits are prose only (no numbers, names, dates, quotations, or citation
  purposes changed; no scripts, styles, assets, or chart provenance touched), and
  each edit removes marks or words rather than adding banned lexis, so no BLOCK is
  expected — but the direct edits mean the prior proof no longer covers the file.

## Decision

approve — every central claim verified against its owning primary, the who-graded-
what contrast and both 35/42 figures confirmed, the embargo question left contested
with no impropriety asserted, and the remaining defects (one arithmetic error, a
term collision, two signposts, two semicolons) fixed in place. I made direct cuts,
so the article needs a fresh proof from the writer before stamping.

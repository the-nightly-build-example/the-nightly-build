# Editorial review: what-could-go-wrong/technological-unemployment (editor/01)

## Skeptic

Thesis: the famous 47% was never a count of jobs that would vanish, the loud
automation numbers each count a different thing (occupation risk, task
automatability, task exposure, real-system effects), and no primary anywhere
holds a measured count of a job actually lost to AI, so both the alarm and the
dismissal are surer than the evidence lets them be. The piece states this
plainly and stands on it.

Claims it rests on, and how each held:

- **47% is high-risk occupations, not a job-loss forecast.** The article scores
  it exactly as Frey-Osborne do: probability of computerisation above 0.7, whole
  occupations, 70 hand-labelled, a Gaussian-process classifier on nine O*NET
  level variables, 702 occupations, BLS 2010 weights, window "a decade or two."
  Every element matches the evidence record's primary reading. The disclaimer
  quote ("make no attempt to estimate the number of jobs that will actually be
  automated") is verbatim and load-bearing. Held.
- **9% is the same US economy scored by task.** Article ties the 9% to
  individual workers with at least 70% of their own tasks automatable, from
  PIAAC, set directly against FO for the same country. The worked examples
  (bookkeeping clerks 98% by occupation, retail salespeople 92%/4%) match AGZ's
  own examples in the record. The "high-risk occupation" (FO) and the
  "high-automatability worker" (OECD) are held as distinct objects, never
  blurred. Held.
- **Exposure is not displacement.** The 15% average, the 80%/19% beta shares,
  and the two caveat quotes are all Eloundou's, correctly attributed to the
  beta (LLM-plus-software) measure and explicitly marked as a capability
  proxy, not a job-loss figure. The word "exposed" is never swapped for "at
  risk." Held.
- **The two field studies point opposite ways and both are small.**
  Brynjolfsson (5,179 agents, ~3M chats, +14% avg, baseline 2.6, +34% for the
  least experienced, attrition down) and Hui-Reshef-Zhou (Upwork, writing and
  coding, -2% jobs, -5.2% earnings, top freelancers hit hardest) match the
  record number for number, and the piece is careful that one measures output
  per worker inside a firm and the other demand across a market. Held.
- **The historical counter, at full strength, then the reason this time might
  differ.** Autor's complementarity case (ATMs 100k->400k 1995-2010; tellers
  500k->550k 1980-2010; tellers/branch down a third; urban branches +40%; the
  tacit-knowledge/Polanyi point) is given its own section and stated as "the
  strongest reason to doubt the alarm" before it is weighed. Only then does
  Acemoglu's <=0.71% TFP (refined 0.55%), ~0.07%/yr, ~1.1% GDP, "order of
  magnitude below the boldest industry forecasts," and the easy-task/hard-task
  caveat arrive as the measured counter. The Acemoglu figure is the record's
  (<=0.71%/0.55%), not the rounded external 0.66%. Held, and steelmanned as the
  round focus requires.
- **The present rests on no study.** Amodei's ~half of entry-level white-collar
  jobs in 1-5 years and 10-20% unemployment is named as a warning from an
  interested party with no public dataset, cited to secondary reporting; ITIF's
  "it didn't happen" is shown to knock down a stronger forecast (47% "would
  likely be eliminated") than FO issued. Both held, and the mirror-image gap is
  the piece's payoff.

Display text audited descriptor by descriptor: headline, dek, every subhead,
every name/title/date/quantity. Keynes 1930; Frey "economist," Osborne
"engineer" (correct — Dept. of Engineering Science); OECD authors and year;
Eloundou author list; Autor 2015; Acemoglu 2024; Amodei "runs a leading AI
company" (no company named as an authority, round focus satisfied). No wrong
label found.

`data-nb-kind` audit: s1-s8 primary (each owns its number or argument), s9
(Fortune/Morris reporting on Amodei) and s10 (ITIF/Atkinson think-tank opinion)
secondary. Correct against the primary/secondary test: the study that owns a
number is primary, the think tank repeating a claim is secondary. No mislabel
hiding a missing independent source.

Chart: provenance in `chart-1.py` cites FO 47% and AGZ/OECD 9% for the same US
economy, matching the record exactly. Read as a reader: y-axis "Share of US
employment at high risk (%)" runs 0-55 with no truncation, bars sit on zero,
each labelled with its method and study. The two figures are honestly
comparable — same economy, different unit — and the caption cites both owning
primaries (s2, s3). The shared "high risk" axis label is defensible: AGZ
themselves benchmark their 9% against FO's high-risk share, and the body draws
the occupation-vs-task distinction the axis compresses. No correction routed.

No break found. No miscitation, no unsupported central claim, no source-policy
failure.

## Cut

One direct cut/rewrite: "the desk's other economic worry" in the Background band
became "a related economic worry." It narrated the newsroom's own coverage,
which `spec/slop.md` bans as self-reference and the round's recent-pattern notes
flag by name ("this desk" self-reference). The bookend's sanctioned
self-reference is addressing the reader and naming what the lesson covers, not
characterising the desk's back-catalogue. The required distinction it marks
(control via institutions there, jobs and wages here) is preserved intact.

Slop pass, sentence by sentence and then along the edges out of order: no
sentence failed the placeholder test. The edge fragments that could have been
slop earn their place. "Serious researchers, a real method, a specific number"
is the steelman verdict the beat and voice guide ask for before the critique,
and each noun points at something the paragraph built. The negative-parallel
constructions ("High risk meant... not that the jobs would go"; "not a fight
about facts. It is a fight about the unit you count"; "a warning from an
interested party, not a study") each correct a real, named misconception that is
the article's own subject, so they survive the rule rather than tripping it.
"This is automation as a complement / as a substitute" are analytic labels
carrying the section's frame, not decoration.

Formula check against the recent-pattern notes: the opener does not close on a
"By the end you will be able to..." promise; the takeaway does not land on a
second-person portable-question checklist; the closer does not use the dominant
"keep the demonstrated results and the projections in separate columns / which
of the two you are looking at" sort — it resolves in the lesson's own terms
(the bank teller, and Keynes's 1930 question). The dek avoids the concessive
"..., yet [undercut]" mold and the comma triad. Headings vary in construction
and avoid the desk's "Why/How the..." interrogatives. No surviving house mold.

Writer-flagged item 1 (the density WARN): I judged it, did not rubber-stamp it.
The sentence is the "Why this matters" payoff — "The payoff is a way to read
these numbers yourself: to tell a job that could be automated from a job that
was, an exposed task from a lost one, and a measured result from a forecast
dressed as one." It is a ~40-word three-part parallel, and each pair names a
distinction this lesson actually draws (occupation risk vs actual loss, exposure
vs loss, measured result vs forecast), each resolved point-for-point in the
takeaway ("None of them counts a job that was actually lost"). It is not the
banned "By the end you will be able to..." forward-promise formula in disguise:
it carries no second-person "you will be able to" future promise, and its
content is specific to this piece rather than interchangeable. The lesson
template explicitly sanctions posing the lesson's questions in the opener and
resolving them in the takeaway. This is that pairing, and a long sentence under
control per `spec/editorial.md`. It earns its length and stays; splitting it
would break the parallel the two bookends turn on. The single intentional
density WARN is acceptable.

Writer-flagged item 2 (the s6 label): confirmed honest. s6 is labelled "CESifo ·
Xiang Hui, Oren Reshef & Luofeng Zhou, Working Paper 10601 (2023)." The evidence
record supplies the authors, venue, working-paper number, and year but no exact
title. The label invents nothing and misleads no one — it names the working
paper by its real number rather than a title it does not have. The paper's real
title is not in the evidence record, so there is no fix to make here; leaving the
honest working-paper label is correct.

## Reader

Reading what survives straight through as the paper's declared reader: I come
away able to tell four different automation measurements apart — an occupation
scored as automatable, a worker most of whose tasks are, a task an LLM could
speed up, and a job actually lost — and to see that no study holds the last one,
so both the "half of all jobs" alarm and the "it never happened" dismissal
outrun their evidence. No single source gives that. FO gives 47%, OECD gives
9%, Eloundou gives exposure shares, but only this piece lays them in one frame
with the historical counter and the present claims and shows what each does and
does not count. That matches the draft handoff's original-work statement (four
measurements the public argument fuses, pulled apart), and both survive. The
prose sits closer to the voice-guide exemplars than to a median AI summary: it
says what each number counts, states the measured result plainly without
inflating it, and marks the gap where confidence runs past proof, in the calm
plain register the guide describes. The headline as the largest claim holds — the
piece defends exactly that the 47% was never a prediction jobs would vanish.

## Edits

- Background band: "the desk's other economic worry" -> "a related economic
  worry" (removes newsroom self-reference; preserves the marked distinction).

## Required work

None. No evidence gap, no broken claim, no chart correction, no source-policy
failure to route. The s6 title would require a new researcher artifact to add a
verified title; it is not required work, since the current working-paper label
is honest and the record supplies no title to use.

## Decision

approve — the argument is steelmanned at full strength and tested honestly,
every headline figure carries its denominator/period/definition with occupation
risk and worker exposure kept distinct, no primary is claimed to hold a job-loss
count, the chart is honest, and the proof holds at BLOCK: 0 with one earned
density WARN.

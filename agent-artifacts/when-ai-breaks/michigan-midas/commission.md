# Commission: when-ai-breaks/michigan-midas

## Assignment

One lesson for When AI Breaks, on the lesson template, on one incident: Michigan's
MiDAS (Michigan Integrated Data Automated System), the unemployment-insurance
system that, run in a mode that auto-adjudicated fraud with no human review from
roughly October 2013 to August 2015, issued tens of thousands of false fraud
determinations against jobless residents and imposed quadruple penalties, until a
state review found its fraud findings wrong the large majority of the time. This
is the scheduled open article for the series on 2026-08-23.

## Tell it from the record, in order

- What the system was built to do: modernize Michigan's Unemployment Insurance
  Agency (UIA) claims processing; the state paid Fast Enterprises (FAST) for the
  MiDAS platform, launched October 2013.
- What it actually did: it flagged "fraud" by automated data mismatches (for
  example, discrepancies between employer-reported and claimant-reported data, or
  crude questionnaire logic), auto-adjudicated without a human examiner,
  frequently notified claimants inadequately, and on a fraud finding imposed the
  penalty Michigan law allowed — up to four times the alleged overpayment — and
  pursued collection (wage garnishment, tax-refund seizure).
- Who it affected and the scale: get the exact figures from the primary record.
  A 2017 review by the UIA itself found that of the determinations made by the
  auto-adjudication system in the period, a large majority (report the exact
  percentage and denominator) were wrong. Report the number of people affected
  from the state's own numbers, not from loose secondary claims.
- What the operator did afterward: the state stopped the fully automated mode in
  2015, later reviewed and reversed determinations and issued refunds; litigation
  followed (notably *Cahoo v. SAS Institute / Fast Enterprises* and *Bauserman v.
  Unemployment Insurance Agency*, which reached the Michigan Supreme Court). Name
  the people, companies, agencies, and dates.

Then teach why this kind of system fails this way: automated determination plus a
reversed burden of proof plus removal of the human adjudicator turns a modest
false-positive rate into a mass harm, and a penalty multiplier makes each false
positive catastrophic. Close with where the same design still runs today, in
Michigan's own nouns — not a reused house line.

## Required contribution

The reader should be able to tell what MiDAS actually automated, why removing the
human examiner (not the data-matching itself) is what scaled the harm, how a
409%-style penalty multiplier converts a wrong flag into a life-altering debt,
and where to look for the same design in other benefits and fraud systems. Where
the cause is disputed (the state's account of what MiDAS "decided" versus the
plaintiffs' account, and how much the vendor versus the agency's configuration is
to blame), present the strongest version of each side and say what evidence would
settle it.

## Boundaries

- One incident. Do not fold in Robodebt or the Dutch childcare scandal as
  content: both are already published (`when-ai-breaks/robodebt`,
  `dutch-childcare-benefits`) and both share the *pattern* (automated benefits
  adjudication, reversed onus, mass false positives). Link them in Background as
  the same design in other jurisdictions, and make MiDAS's *distinct* mechanism
  do the teaching: data-mismatch fraud flags and a statutory quadruple penalty,
  not income-averaging (Robodebt) and not a foreign-nationality risk score
  (Dutch). Do not echo Robodebt's opener ("A debt the recipient had to disprove")
  or its closer framing ("the same bargain still runs").
- Every number, name, date, and percentage comes from the primary record (the
  UIA's own review, court opinions, the state auditor / ombudsman where
  applicable, contemporaneous reporting that held up). Do not inflate the
  affected count; two retellings of one origin count as one.
- The record's language matters: be precise about what was "fraud" (an
  allegation the system made) versus actual fraud (rare).

## Template, sources, policy

- Template: lesson. Word band 1200-2200.
- Source floor (nb source-policy when-ai-breaks): at least 8 sources, at least 4
  primary, at least 1 secondary. Primaries: the UIA's 2017 review/its reported
  findings, the federal opinions in *Cahoo v. SAS Institute*, the Michigan
  Supreme Court opinion in *Bauserman*, and any state legislative/auditor
  findings. Read the underlying documents; resolve every URL to the document's
  own page. Secondary reporting (Detroit Free Press, ProPublica, The Guardian,
  legal-press coverage) is context and labeled secondary; verify accusations
  against two independent parties in a position to know.
- Production policy (balanced): writing-coach low, researcher high, writer
  medium, editor high; "capable" tier for all, resolved to Claude Opus 4.8.
  nb-meta harness `claude-code-routine`, model `claude-opus-4-8`.
- Suggested nb-meta tags: government, automation, unemployment, false-positives.

## This edition's neighbors

`the-evidence/adam-optimizer`, `the-instruments/squad`,
`the-mechanics/false-confidence`, `what-could-go-wrong/natural-selection`. No
subject overlap; this is the only real-world-incident piece.

## Recent shapes and phrasing to break

Recent When AI Breaks pieces (itutorgroup, arup-deepfake-fraud, robodebt) share
habits to avoid:

- The Robodebt echo is the main risk. Its structure was: opener scene of one
  debt, "how dividing a year made a fortnight" mechanism section, "the check that
  used to catch it," "what it cost and how it ended," "where the same bargain
  still runs." MiDAS must not track that outline heading-for-heading. Find its
  own order and its own closer.
- The `nb-stat` / `nb-stat-strip` figure-scene opener (arup) and the
  one-person-two-applications opener (itutorgroup) are house moves; a specific
  human anchor is good, but do not reuse those exact shapes.
- Verify the affected-count and false-rate figures especially carefully: those
  are the numbers that will land in the headline and dek, where a wrong label
  reaches every reader.

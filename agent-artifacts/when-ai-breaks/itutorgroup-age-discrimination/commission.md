# Commission: when-ai-breaks/itutorgroup-age-discrimination

## Assignment

One lesson on a real incident: iTutorGroup's hiring software automatically
rejected older applicants, the U.S. Equal Employment Opportunity Commission sued,
and the case settled in 2023 (EEOC v. iTutorGroup, E.D.N.Y.). When AI Breaks tells
what happened in order — what the system was built to do, what it actually did,
who it affected, what the operator did afterward — names people, companies, and
dates, then explains why that kind of system fails that way and where the same
weakness lives in systems the reader uses. Work from the record: the EEOC filing,
the consent decree, the agency's statements. The reader is smart, widely read, new
to hiring algorithms and U.S. employment law.

## Why this incident, now

It is the EEOC's first settlement of an AI/automated-hiring discrimination case,
and it lands in the middle of the current wave of automated-hiring law (state
audit rules, the Mobley v. Workday litigation). It teaches a point most "AI hiring
bias" coverage misses.

## Angle

Tell it straight, and be honest about the technology. The specific, well-recorded
fact is that iTutorGroup's application software was configured to automatically
reject female applicants aged 55 or older and male applicants aged 60 or older,
and it rejected more than 200 qualified applicants on that basis; the EEOC found
out when an applicant reapplied with a more recent birth date and got an interview.
The teaching point: this was not an inscrutable machine that learned bias from
data. It was an explicit automated rule — a date-of-birth cutoff — and that is
exactly why the case was clean and winnable. Contrast this with the emergent,
learned bias of a system like Amazon's scrapped recruiting tool (link the library
lesson): there the model inferred a proxy for sex from historical data; here a
person wrote a rule. Both are "AI hiring" in the headlines; the mechanisms and the
legal exposure differ. Then generalize honestly to systems the reader meets:
automated applicant screening (knockout questions, resume filters, date and gap
rules) can encode illegal criteria directly, and the harder, more common problem
is the learned proxy that no one wrote down. Close on where the same weakness lives
now.

## What to teach (short, complete)

1. What happened, in order, with names and dates: iTutorGroup (the tutoring
   business and its brands), the automated age cutoffs, the ~200+ rejected
   applicants, how the EEOC discovered it (the reapplication), the 2022 suit and
   the 2023 consent decree and its terms (the $365,000 fund, the anti-discrimination
   provisions). Every figure from the primary record.
2. The relevant law in plain terms: the Age Discrimination in Employment Act (ADEA)
   protects workers 40 and older; a facially age-based automatic rejection is
   discrimination on its face. Define the term at first use.
3. The mechanism, honestly: an explicit programmed cutoff versus a learned proxy.
   Why the explicit rule made the case easy, and why the learned-proxy version
   (Amazon-style, link it) is the harder and more common failure.
4. Where it lives now: automated screening features readers encounter, and the
   current legal/audit landscape (name specific rules/cases, e.g. Mobley v.
   Workday, NYC Local Law 144), kept accurate and not overclaimed.

## Boundaries and non-overlap

- Distinct from when-ai-breaks/amazon-hiring-tool (learned gender bias in an
  internal tool that was scrapped before harming applicants). This incident is a
  deployed explicit-rule case with federal enforcement and a settlement, about age.
  Require a Background link and a one-sentence contrast; do not re-tell Amazon.
- Do not overclaim the technology as machine learning. If the record shows a simple
  automated filter, say so; the honesty is the lesson. The researcher must
  establish exactly what the system was.
- NYC Local Law 144 is covered from the regulation side in ai-in-the-world/
  nyc-hiring-bias-audits and the-levers. Reference the present landscape without
  re-teaching the audit law; link if useful.

## Source policy

Lesson in When AI Breaks: at least 8 sources, at least 4 primary and at least 1
secondary. Primary: the EEOC complaint and the consent decree (court/agency
documents), the EEOC press releases, the text of the ADEA, and primary documents
for the present-landscape points (the Workday ruling, Local Law 144 text).
Secondary: contemporaneous reporting, used for context and never as the sole basis
for a factual claim about the case. Any accusation needs the primary record plus
independent confirmation.

## Habits to avoid (break these, from the recent record)

- Recent When AI Breaks deks are vivid single sentences with specific figures and
  names ("Rite Aid scanned every shopper's face..."; "Robodebt built debts from
  averaged income..."). That is the house shape; write one in this case's own nouns
  (the age cutoff, the reapplication that exposed it, the $365,000). Do not copy a
  neighbor's construction.
- Vary orientation headings from recent openers; avoid a generic "Background" /
  "What happened" scaffold label.
- Furniture: a stat strip (applicants rejected, settlement fund, the two age
  cutoffs) or a short timeline could help; use only if it changes understanding.

## This run's neighbors

Also tonight: the-evidence/whisper, the-instruments/imagenet-top-5-accuracy,
the-mechanics/overused-words, what-could-go-wrong/value-lock-in. One paper, one
register; distinct dek shapes.

## Production record

- Harness: claude-code-routine. Writer model: claude-opus-4-8 (production policy
  asks "capable"; no pinned model, no deviation).
- Effort per balanced policy: coach low, researcher high, writer medium, editor
  high. None required. Template: lesson.

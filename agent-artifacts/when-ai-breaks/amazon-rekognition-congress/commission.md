# Commission: when-ai-breaks/amazon-rekognition-congress

## Assignment

One lesson for When AI Breaks on a single incident: the ACLU's July 2018 test in
which Amazon's Rekognition face-matching service falsely matched 28 members of
Congress to arrest mugshots. Tell what happened in order, then teach why that
kind of system fails that way, then show where the same weakness lives today.

## Tell it in order

- What the system was built to do: Rekognition is Amazon's commercial
  face-matching service, sold through AWS and pitched to police departments. Given
  a probe face, it searches a gallery of faces and returns candidates, each with
  a similarity score.
- What it actually did: in July 2018 the ACLU ran all 535 members of Congress
  against a gallery of public arrest photos using the service's default settings,
  and it returned 28 false matches, a share of them members of color out of
  proportion to Congress. Get the exact gallery size, the default threshold used,
  and the demographic breakdown from the primary.
- Who it affected and how: the harm is a false match feeding a real police
  investigation. Keep the stakes concrete and sourced.
- What Amazon did afterward: it disputed the test, arguing the ACLU used the
  default 80 percent confidence threshold while Amazon recommends 99 percent for
  law-enforcement identification, and questioned the method. In June 2020 Amazon
  announced a moratorium on police use of Rekognition. Record the dates and the
  exact wording of each Amazon statement.

## Teach why it fails that way

Three mechanisms, taught plainly with the incident's own numbers:

1. Threshold. A match is a similarity score, and whether it counts as a "match"
   is a cutoff the operator sets. A default tuned for one use is wrong for
   identification against a large gallery.
2. Gallery size. Searching thousands of photos gives many chances for a false
   match even when any single comparison is usually right; teach this
   base-rate/multiple-comparison effect with the test's real numbers.
3. Demographic error gaps. Measured differences in face-matching accuracy across
   groups mean false matches do not fall evenly. Cite the audits and the NIST
   demographic study for the measured version.

Link, do not re-teach: the library's lessons on the skin-tone gap in vision
(Google Photos), on base rates in an alerting system (ShotSpotter), and on
facial recognition and regulation (Clearview). This lesson's own teaching is the
threshold-plus-gallery-size point that the covered pieces do not make.

## The disputed cause

Amazon says the result was threshold misuse; the ACLU and auditors say the
tool's defaults and its measured demographic gaps are the problem. Present the
strongest version of each and say what evidence settles it: calibrated
thresholds, the gallery size, and measured per-group error rates from
independent testing.

## Close on the present

Face matching is deployed in policing and identity checks now, and the
threshold, gallery-size, and differential-error problems are unchanged. Point to
where a reader meets this today.

## Boundaries

- The reader is smart and widely read, not technical. Define face matching,
  gallery, threshold, similarity score, and false match in plain words at first
  use.
- Keep it to this incident and its mechanism. Do not turn it into a facial-
  recognition policy survey or a Clearview retread.

## Contribution the article must add

Make the "28 members of Congress" number mean something exact: why a matching
score with a default threshold against a large gallery produces false matches
that land unevenly, and why a public test surfaced it. The writer states the
exact original-work sentence in the handoff.

## Sources

Series/template floor: at least 8 sources total, at least 4 primary, at least 1
secondary. Primaries available: the ACLU's own July 2018 post; Amazon's/AWS's
blog responses; Amazon's June 2020 moratorium statement; the Gender Shades audit
and the follow-up that tested Rekognition; and the NIST face-recognition
demographic study. Secondary reporting for context and for the reporting that
held up.

## This edition (keep distinct from the run's other four lessons)

- the-evidence/gpt-4-bar-exam
- the-instruments/frechet-inception-distance
- the-mechanics/roleplay-jailbreaks
- what-could-go-wrong/value-specification

No subject overlap. Like the-instruments tonight this piece turns on a
misleading number, so keep it anchored in the incident and its people rather
than a general lesson about statistics.

## Habits not to inherit (from the recent library)

- Recent When AI Breaks deks name the actor and the harmed party in one loaded
  sentence; keep the dek doing that work but do not copy the recent shape.
- Vary heading construction; avoid leading every heading with a number or the
  comma-and contrast.
- The recent furniture stack is nb-note, nb-figure, and nb-stat. Plan furniture
  from the supplied catalog; the threshold/gallery-size point may earn a small
  table or figure, but do not add one by reflex.

## Production

Profile balanced. Model: capable (Claude Opus 4.8) for every role. Effort per
production policy: writing-coach low, researcher high, writer medium, editor
high. No required directive is in force. The writer records the actual writer
model in nb-meta per the library's convention (harness "claude-code").

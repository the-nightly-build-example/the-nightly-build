# editor review-brief: the-mechanics/lost-in-the-middle (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writer/01/brief.md              (the exact brief the writer worked from)
- ../../writing-coach/01/voice-guide.md
- ../../researcher/01/evidence.md
- ../../writer/01/draft-handoff.md      (original-work sentence; open in the third read)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/the-mechanics/lost-in-the-middle/library/the-mechanics/lost-in-the-middle.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-mechanics/lost-in-the-middle/.nb-context/

Output: ./editorial-review.md

Recent-pattern notes (the-mechanics back catalogue; use to catch formula and
catchphrase):
- Recent headlines are concrete demonstrations, often a paired before/after ("'No
  onions' gets onions, 'no elephant' gets an elephant"; "Give GPT-4 the same
  options in a new order and it changes its answer"). Flag the headline if it
  stamps that paired rhythm.
- Recent first body headings are a bare instance count or two-clause observation
  ("Two systems drop the same word", "One reorder, a different answer").
- The closing "where it lives now" section is required; watch its heading against
  recent closers.

This round's focus:
- press/editorial.md check: the takeaway bookend carries the judgment. If the body
  closes on a Verdict note or any block restating the finding, remove it (leftover
  from the earlier template). Confirm the body does not end on such a block.
- Do not let the effect be overstated. Verify against the evidence record: the
  magnitude is "more than twenty points" / ~22-point max gap (the ">30%" secondary
  figure must not appear), and Claude-1.3's ~4-point dip must stand as the flat
  counterexample so "models are lost in the middle" is not asserted flatly.
- Persistence in 2024-2025 frontier models is hedged to proxies (RULER, NoLiMa,
  Levy), not asserted as the specific position-of-answer U in a named current
  model. The mechanism must read as genuinely open (three candidate causes;
  RoPE-decay-alone explicitly ruled insufficient), with "not cured by a bigger
  window" as the settled point.
- There is a chart (chart-1.py/.png) built from Liu Appendix G Table 6
  (GPT-3.5-Turbo U vs Claude-1.3 near-flat). Inspect its committed provenance and
  read the rendered image: labels, scale, and the numbers must match the evidence
  record and the cited primary; the caption must be a factual cited label. Route any
  chart correction to the writer (they hold the chart tooling).
- Confirm irrelevant-context and attention are linked and the behavior is
  distinguished from distractors and from needle-in-a-haystack. If you change
  prose, a fresh writer proof is owed before PR.

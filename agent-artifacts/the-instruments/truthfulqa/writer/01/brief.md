# writer brief: the-instruments/truthfulqa (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- ../../commission.md — the measurement, the angle, source direction, nb-meta values.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only from it.
- ../../../../.nb-context/ — the effective template contract and runtime assets.
- ../../../../library/the-instruments/truthfulqa.html — the initialized article to edit in place.

Output: ./draft-handoff.md

Proof (run from repo root; iterate --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/the-instruments/truthfulqa/library/the-instruments/truthfulqa.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/53d4ed2b-ac4b-53e6-97a0-447483501c29/scratchpad/library-checkout --no-check-links`
- Final: same WITHOUT `--no-check-links`, and run `./nb stamp` first, until `BLOCK: 0`.

nb-meta: date `2026-08-11`, harness `claude-code-routine`, model `Claude Opus 4.8`,
three descriptive tags in nb-meta directly. Keep nb-meta `dek` identical to the
rendered dekline.

This round's focus: teach how the TruthfulQA number is produced, step by step, and
what it cannot support. Keep the generative score and the MC1/MC2 numbers
explicitly distinct wherever a figure appears. The misled-people beat is the
"bigger models are less truthful" reading against what the adversarial construction
actually supports. Link `the-instruments/hallucination-rate`, `the-instruments/llm-as-a-judge`,
and `the-mechanics/hallucination` in Background rather than re-teaching them. Link
only already-published library pages — do NOT link tonight's siblings. If the
evidence record preserved a clean sourced comparison worth a chart, build it only
with `nb chart` from the record's verified series and cite provenance; otherwise
no chart.

Habits not to inherit (house formulas across the last three of every desk):
- No "By the end you will be able to..." close on the opener; no "This lesson
  shows/takes apart..." lead-in.
- No second-person "when you meet a [number], ask three things" checklist as the
  takeaway. The-instruments' recent takeaways all land on exactly this move
  ("ask three things", "ask what else moved"); break it.
- No "demonstrated-vs-unproven / settled-vs-open" final sort; no "which of the two"
  or "measured, or used?" line.
- Do not open the way the desk's last three did: a frequency-adverb "Every few
  weeks/months a lab launches..." frame with a personified "single number doing
  the work." Find a different way in.
- Do not close on the two-part antithesis "Read with those questions in hand it
  is worth having; read as a bare percentage it misleads you." That parallel is a
  desk formula. Vary headings away from the desk's interrogative "How/Why the ..."
  and "From X to Y" molds; and drop the personified "the number keeps its word"
  device.
- No "this desk" self-reference.

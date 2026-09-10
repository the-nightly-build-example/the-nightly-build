# Draft handoff: the-instruments/gaia (01)

## Original-work statement

The article turns the evidence record's scattered validation-versus-test facts
into a single test the reader can apply, ask which split a GAIA number came
from, and uses JoyAgent-JDGenie's eight-point same-system gap to put a size on
the cross-set comparison the evidence only names as invalid.

## Proof result

`./nb check .nb-work/the-instruments/gaia/library/the-instruments/gaia.html --series the-instruments --library /tmp/claude-0/library-checkout`
(links included): **BLOCK: 0, WARN: 1**, verdict PUBLISHABLE.

Warning left intentionally:

- `W-SENTENCE-DENSITY` on the orientation sentence differentiating the three
  neighbor benchmarks ("SWE-bench scores an agent on fixing real repository
  bugs, tau-bench on holding to a single customer-service script..., and METR's
  task-time-horizon on..."). This is a deliberate parallel that shares one verb
  to give each neighbor a single differentiating line, which is what the
  commission asked for. Splitting it forces "scores" to repeat and breaks the
  parallel; the sentence is under control, so it stands per the editorial
  standard's allowance for a long controlled sentence.

## Number caveats (both respected)

- No live-leaderboard number was used. Every recent figure is anchored to a
  dated primary report: OpenAI's 67.36% validation (2 Feb 2025, read via the
  Hugging Face post), H2O.ai's 75% test (17 Mar 2025), JoyAgent's 75.2/67.1
  (its own report). The discarded aggregator standings were not cited.
- The per-level denominator is not overstated. Only the firm aggregates (human
  92%, GPT-4+plugins 15%) are given as figures; the Level 3 model result is
  stated as "solved none" (0% is denominator-independent). No precise per-level
  human/model split is asserted.

## Open question

None blocking. One awareness note for the editor: the claim "the highest
verified test-set score in this record is H2O.ai's 75 percent" is scoped to the
evidence record's reading date and is stated in the article as "in this record"
for exactly that reason; the record could not verify current live standings. If
a later researcher artifact establishes a higher dated test-set primary, that
sentence would need updating.

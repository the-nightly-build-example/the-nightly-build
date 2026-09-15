# Draft handoff: when-ai-breaks/apple-intelligence-summaries (writer, round 01)

## Original work

The article sorts the four false-notification cases (Netanyahu, Mangione,
Littler, Nadal) against Maynez et al.'s intrinsic/extrinsic hallucination
split, a mapping none of the sources make themselves, and finds it only
partly fits: the Netanyahu and Littler lines read as single-document
misreadings, but the Nadal case is a cross-notification identity swap that
the single-document hallucination literature was not built to measure. Naming
that third failure mode, compression across grouped notifications rather than
within one document, and tying it explicitly to the brand-attribution
aggravator (an outlet's icon on a machine's sentence) is the piece's own
analysis, presented as reasoning rather than as a source's finding.

## Proof result

`./nb stamp` then `./nb check --series when-ai-breaks`, iterated with
`--no-check-links`, then final with links:

- First `--no-check-links` pass: BLOCK 0, WARN 1 (W-SENTENCE-DENSITY, a
  57-word sentence in the mechanism section). Fixed by splitting the
  sentence; no warning was left standing.
- Final pass with link checking: **BLOCK: 0, WARN: 0**, verdict
  PUBLISHABLE. (Note printed by the tool: "library state not provided
  (--library); open-mode dedupe and commission checks skipped" — expected,
  since the brief's exact proof command omits `--library`.)

No warning was intentionally left; the proof is clean.

## Open questions routed

None. The evidence record's three load-bearing caveats were addressed
directly in the draft rather than routed back:

- Verbatim wording: only the Nadal ("Brazilian tennis player, Rafael Nadal,
  comes out as gay") and Netanyahu ("Netanyahu arrested") lines are quoted
  as literal notification text; Mangione and Littler are given only in the
  BBC's own paraphrase, attributed as such. The grouped "Luigi Mangione
  shoots himself; ..." screenshot string is not used anywhere in the piece.
- The "also affected" outlets (Sky News, NYT, Washington Post) are named
  only as the BBC's own report describes them: sourced to "reports from
  journalists and others on social media," not independently verified, and
  the November NYT case is likewise attributed to a screenshot the BBC could
  not confirm.
- The Maynez 70%/90% figures are presented as XSum-corpus findings that
  ground the mechanism, with an explicit sentence stating they describe a
  research benchmark, not Apple's feature, and that nobody has tested
  notification summaries the same way.

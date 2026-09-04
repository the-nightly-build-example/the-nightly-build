# Draft handoff: the-instruments/attack-success-rate (01)

## Original-work sentence

The article reorganizes the evidence record's separate benchmark facts and its
two contradictory "misled" directions into one four-step pipeline (a fixed list,
an attack, the model's answer, a judge) and spends that pipeline on a single
number still in circulation, Cisco's 100% for DeepSeek R1, to show the reader
how each buried choice makes the same rate mislead in opposite directions.

## Proof result

`./nb check ... --series the-instruments` (links included): **BLOCK: 0, WARN: 0,
PUBLISHABLE**. Stamped: words 1975, reading 9 min, sources 9 (7 primary, 2
secondary; meets the series floor of 8 sources / 4 primary). Word count sits
inside the lesson band (1200-2200). No warning intentionally left standing.

The only proof note is "library state not provided (--library)", which is
expected for the brief's local command: open-mode dedupe and commission checks
run in the orchestrator's PR-mode proof, not here.

## How the settled decisions were handled

- Both misleading directions are taught as failure modes of one number. The
  too-high direction lives in the judge section (the Scots Gaelic 43% on GPT-4,
  re-scored vacuous by StrongREJECT). The too-low direction lives in the
  expiration section (GCG's low Claude-2 2.1% against one 2023 attack, and the
  past-tense rewrite taking GPT-4o from 1% to 88%). The Cisco/DeepSeek case
  frames both, opening the lesson and resolving in the final body section.
- XSTest is cited once as a primary (s6) for the over-refusal counterweight; the
  mechanism itself is left to the linked over-refusal lesson
  (the-mechanics/over-refusal), not re-taught.
- Every rate is stated with its attack and its judge attached (e.g. "GCG
  transfer, non-refusing attempt, manually verified"; "past-tense rewrite, GPT-4
  judge"; "50 HarmBench prompts, one algorithmic attack, auto refusal detection").
- No company is named as an authority on which model is safest. Cisco appears
  only as the producer of the misled number; the verdict's *use* is what the
  lesson criticizes ("The verdict may even be right. But nothing in a single ASR
  can carry it.").
- Links, not re-argument: the jailbreaks lesson (what-could-go-wrong/jailbreaks)
  is linked for how an optimizer-found suffix is built; the over-refusal lesson
  is linked for the refusal mechanism. Both are plain prose/Background links, not
  numbered sources, per press editorial.

## Contradictions from the evidence record

- StrongREJECT prompt count (313 vs 346): resolved to the authors' repository
  figure of 313, cited to the repo (s4). Handled by using the resolved number.
- GCG AdvBench behavior count (500 vs 520/574): the article never states the
  AdvBench set size, so the discrepancy does not bear on any claim made here. It
  uses only GCG's transfer percentages, which are independent of the count.
- GCG's non-refusal success criterion vs StrongREJECT's critique: kept distinct
  in prose. The 2.1% is explicitly framed as "any reasonable non-refusing
  attempt ... a looser bar than StrongREJECT's," so GCG's rates and
  StrongREJECT's grading standard are not presented as the same measurement.

## Open evidence / voice needs

None blocking. One deliberate non-use for the editor's awareness: Gao
(arXiv:2606.25487, judge precision/recall and judge-flip results) is a verified
primary that was left unspent to keep the judge section from overloading; the
judge-sensitivity point is already carried by StrongREJECT's grader-vs-human
spread (table) and the three-judge swing on identical GPT-4o answers. It is
available if a later round wants the precision/recall trade in the piece.

## Furniture spent

Numbered steps for the four-choice pipeline; one table for the grader-vs-human
agreement spread (the clearest single picture of judge sensitivity). Both spend
argument the prose leans on; no chart or source asset was needed.

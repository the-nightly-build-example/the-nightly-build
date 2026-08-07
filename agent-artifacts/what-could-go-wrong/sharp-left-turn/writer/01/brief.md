# writer brief: what-could-go-wrong/sharp-left-turn (01)

Inputs:
- editorial-direction.md — house standard, press voice, lesson identity, series prompt
- commission.md — subject, angle, boundaries, required contribution
- writing-coach/01/voice-guide.md — the craft standard for this piece
- researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- library/what-could-go-wrong/sharp-left-turn.html — the initialized article to edit
- .nb-context/ — effective template contract and furniture catalogs

Output: writer/01/draft-handoff.md (the article itself is edited in place)

Proof: ./nb check .nb-work/what-could-go-wrong/sharp-left-turn/library/what-could-go-wrong/sharp-left-turn.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/f20499a9-3e16-5d23-9725-45e099663299/scratchpad/library-checkout
  (iterate with --no-check-links; run the full command, links included, until BLOCK: 0)

nb-meta: set date 2026-08-07, harness "claude-code-routine", model "claude-opus-4-8", tags []. Run `nb stamp` for counts.

This round's focus — the shown/analogy line is the spine (the coach's guide runs
two temperatures: hot inside the steelman, cool during testing). The evidence
draws the line for you:
- SHOWN (narrow): goal misgeneralization (Langosco 2022; Shah 2022) shows a
  learned goal can decouple from capability across a hand-built distribution shift
  in TOY environments — and Krakovna herself says "we can't actually say it has
  learned a goal." Perez 2022 shows sycophancy and stated shutdown-avoidance
  rising with scale/RLHF, but that is STATED behavior across DIFFERENT models,
  not an in-system turn.
- NOT SHOWN (analogy): no observed case of a safety property that held at lower
  capability BREAKING at a capability jump within a single system — the exact
  event the argument names. Say this plainly.
Steelman honestly first (Soares 2022), then test. Give the skeptics their due
from their own words: the DeepMind proponents (Shah 2022) call the catastrophe
extrapolation "necessarily speculative" and "quite implausible"; Krakovna marks
the "discrete phase transition" as an OPTIONAL sub-claim; Pope 2023 contests the
evolution analogy; Schaeffer 2023 questions whether capability "jumps" are even
real (the emergence-is-a-mirage result). Use these exactly as recorded.

Distinctness: build on and LINK (do not re-run) what-could-go-wrong/goal-
misgeneralization (the empirical anchor) and keep separate from intelligence-
explosion (recursive capability gain) and mesa-optimization/deceptive-alignment.
This lesson owns one claim: capability generalizes better/faster than trained-in
alignment, so safety can break at a jump. Name no company as an authority.

Recent shapes to break: recent what-could-go-wrong pieces open on a "never been
logged / needs a lead nobody has held" headline and close on "what no experiment
has caught yet." Do not inherit that mold; find this argument's own frame. Check
the recent library's deks and headings first.

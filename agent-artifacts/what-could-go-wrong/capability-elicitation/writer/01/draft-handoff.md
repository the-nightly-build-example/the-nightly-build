# Draft handoff: what-could-go-wrong/capability-elicitation (01)

## Original-work sentence

The evidence record is a set of separate results — a prompting gain, a
repeated-sampling gain, a scaffold gain, a lab's own hedge, a review's framing —
each living in its own paper and none framing itself as an argument; the article
assembles them into one tested claim (a safety score is a floor set by the
tester's effort, never a ceiling), draws the shown-versus-inferred line the
individual papers do not draw, and holds that claim at equal distance from
relief and alarm.

## Proof result

`./nb stamp` then `./nb check ... --series what-could-go-wrong --library <checkout>`
with links: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** 2193 words (band
1200-2200), 9 sources (8 primary, 1 secondary). No warnings intentionally left.

## Decisions worth flagging

- **Fine-tuning kept as linked ground, not re-cited.** The commission boundary
  says not to relitigate open-weights fine-tuning. So the cheap-removal-of-safety
  figures (Qi et al. $0.20; Lermen et al. under $200) are *not* used as numbered
  sources; fine-tuning appears as one elicitation lever with the demonstration
  handed to the linked `open-weights-release` lesson. The source floor is met
  without them (8 primary + 1 secondary).
- **Naptime figure.** Used the owned pair 0.05 -> 1.00 (CyberSecEval 2 baseline
  and Project Naptime@20). Did not use Barnett and Thiergart's "71% single
  attempt" rendering, per the verification note in the evidence record.
- **AISI 5x-20x** is presented as AISI's rough characterization, not a measured
  constant, as the evidence note requires.
- **Background links verified.** The evidence record flagged that
  `sandbagging.html` and `open-weights-release.html` might not be published; both
  exist and resolve in the supplied library checkout, and the links-on proof
  passed. No open question here.

## Open evidence or voice question

None. The evidence settled every claim the argument rests on, and the voice
guide's exemplars (build the mechanism slowly, verdict sized to the evidence,
both directions of overconfidence held at once) mapped cleanly onto this piece.

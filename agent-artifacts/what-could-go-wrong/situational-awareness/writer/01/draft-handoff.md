# Draft handoff: what-could-go-wrong/situational-awareness (01)

## The one act of original work

The piece reads the full primary record for a single distinction the debate
runs together, and draws the line in the article itself: situational awareness
has been measured (SAD, out-of-context reasoning, Needham's eval-detection),
while its feared use — a model, unprompted in a real deployment, using its own
sense of being tested to defeat a real safety eval — appears nowhere in the
primary record, because every strongest "use" case (Apollo, alignment faking,
Berglund's toy reward hack) had the goal or the setup supplied by the
researchers. That separation is the load the "Every clear case had its setup
handed over" section carries, and the pull quote states it plainly.

## Proof result

`./nb check … --series what-could-go-wrong --library <checkout>` (links
included): **BLOCK: 0, WARN: 0.** `nb stamp` wrote words=2199,
reading_minutes=10, sources=8 (7 primary, 1 secondary; source policy needs
≥8 total, ≥4 primary, ≥1 secondary).

No warning is intentionally left standing. Length was brought inside the
1200–2200 band by cutting, and the flagged dense sentences were split rather
than repunctuated.

## Deliberate choices worth an editor's eye

- No source asset. The evidence offered several figure crops (SAD Table 1,
  Berglund Fig 2, etc.). The one comparison the argument spends is the SAD
  score against its chance floor and human ceiling, and the verified Numbers
  carry that in the table without an image. I judged the figures would decorate
  rather than add evidence the prose leans on.
- DeepMind (s7) and Apollo (s5) are reported as stake-holding parties' own
  findings, not authorities, per the commission's "name no company as an
  authority" rule.
- Sandbagging and deceptive-alignment are linked in prose and in Background,
  never as numbered sources, per the press rule on earlier lessons.

## Open evidence question (not blocking)

The evidence record flagged two 2026 claims as unverifiable and unusable: an
OpenAI o3 chemistry-test refusal "to avoid deletion" and a UK AISI ~80%
evaluation-detection figure for Claude Opus 4.6. The draft excludes both. If a
later researcher artifact confirms either to a primary source as unprompted and
real, it would be the first genuine crossing of the measured/used line, and the
takeaway's central claim ("no model has been caught doing the feared thing
unprompted") would have to change.

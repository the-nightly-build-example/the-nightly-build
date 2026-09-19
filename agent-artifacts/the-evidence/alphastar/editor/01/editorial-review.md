# Editorial review: the-evidence/alphastar (editor/01)

## Skeptic

The thesis: AlphaStar's real achievement is narrower than the memory of it. The
Nature agent reached Grandmaster in anonymous ladder play under a moving camera
and a 22-non-duplicate-actions-per-5-seconds cap, from human-replay imitation
plus league reinforcement learning, and the paper's own ablations show those
limits cost it strength. The "AI beat the pros" story rests on a different,
looser agent, and the strongest "it only clicked faster" critique measures that
earlier agent, not the one that climbed the ladder.

The claims it stands on, and how each held:

1. **Grandmaster meant anonymous Battle.net ladder play, above 99.8% of ranked
   players, all three races.** Holds. MMR 6,275 Protoss / 6,048 Terran / 5,835
   Zerg, ~90,000 active European-server players, top 0.15% average — every figure
   matches the evidence record and its owning primaries. The percentile and
   population are correctly attributed to the Nature News framing (s3).

2. **The Nature version was constrained (camera, 22/5s cap, reaction delays) and
   the ablations show the constraints reduced performance.** Holds. The ~110 ms
   response / 370 ms observe-ahead delays match the record's Nature-version
   figures. The article correctly reports both ablation directions (camera lowers
   performance; pushing APM below *or* above the cap hurts). No January-version
   delay figure (~350 ms) leaked in.

3. **The December 2018 demonstration agent was looser (no camera / whole map,
   less restricted actions, Protoss-only, one map) and went 10-0 then 10-1.**
   Holds. The two off-race/on-race caveats (TLO played Protoss, not his
   professional Zerg; MaNa on-race) and the live loss to the 7-day camera
   prototype are all in the record.

4. **The "clicked faster" critique (Korzekwa: 14 bursts over 400 APM, 6 over 500,
   whole-map vision) describes the December agent, not the ladder agent.** Holds,
   and this is the round's central correctness point. I pushed hardest here
   because it is the claim the piece most wants to keep. The article never lets a
   January-agent fact attach to the Nature result: the burst measurements and
   whole-map vision are confined to the December game and explicitly closed with
   "None of it describes the version that later climbed the ladder." Fig 2c's
   within-human effective-action-rate point is stated without overclaiming that
   the Nature version had no bursts (the paper's Fig 2c does not resolve that, and
   the article does not pretend it does).

5. **Grandmaster on the ladder is not the claim of beating the world's best in a
   controlled series.** Holds. The paper's own words — ladder conditions "do not
   directly measure its susceptibility to exploitation under repeated play" — are
   quoted accurately, and the repeated-exploitation caveat is made legible in
   plain prose.

Named-person check, run deepest per the brief: the article stakes a framing on
"one of the paper's own authors is a professional player" (TLO). One web search
summary claimed TLO was not an author; I did not accept it. I pulled the paper's
own author list from DeepMind's hosted full text and confirmed "Dario Wünsch"
(Team Liquid, affiliation 2) is a listed co-author. The framing stands, and the
"doesn't feel superhuman" quote is correctly placed on the constrained (Nature)
version.

Display text verified descriptor by descriptor. Headline ("reached Grandmaster
while capped at 22 actions every five seconds") is the true central claim with
the surprise up front. Dek adds the anonymous-ladder measurement and the
looser-January-agent contrast without restating the headline. Every MMR, race,
percentile, date, and record in the body and table checks against the owning
primary — with one exception I fixed: the comparison table's December cell read
"looser, uncapped bursts," but the primary says only that the December agent was
"less restricted in how often it could act." "Uncapped" is a stronger absolute
than any source supports, so I changed the cell to "looser limits," which is
faithful to the paper and keeps a clean contrast against the Nature "22 per 5 s"
cell. The burst detail already lives, correctly attributed to Korzekwa, in the
prose.

Source kinds audited: three primaries (Nature paper s1, DeepMind Oct s2, DeepMind
Jan s4) and three secondaries (Nature News s3, Engadget s5, AI Impacts/Korzekwa
s6). The labels are honest — the two DeepMind posts are the team's own account,
correctly primary; the Nature News and Engadget reports and Korzekwa's outside
re-measurement are correctly secondary. No secondary is dressed as an independent
primary to hide a missing source. Citations resolved under the writer's
link-checked proof (BLOCK: 0).

## Cut

Ran the sentence-by-sentence slop pass, then the edges alone, then the
arrived-from-a-link read, then the delete test. The draft is clean: no sentence
failed the placeholder test outright, and I made no prose deletions. The prose
holds the plain-claims-with-defined-terms register the voice guide sets (APM,
league play, imperfect information, reinforcement learning, ablation, and MMR are
each defined in the sentence that first needs them, Brubaker-style; numbers carry
baselines, Luu-style). No borrowed clause from the Brubaker/Luu/Evans exemplars.
No prompt leakage — the commission's "AI crushed the pros" framing is reworked in
the article's own terms, and the only self-reference sits in the two bookends,
where the template allows it, and both bookend passages say something specific to
this lesson.

Two edge sentences sit at the soft end — "the exact constraints are the most
misremembered part of the whole story" (interface opener) and "What made the
paper famous was the claim that this recipe could reach the top of a human ladder
in a game this messy" (orientation closer). Both survive the delete test: each
commits to a claim the piece then establishes (the two-agents section proves the
misremembering; the orientation names the specific famous claim). Left as
written; tightening either would be optional polish, not a slop fix.

Furniture, against the recent-pattern notes. I removed the closing Verdict note
(the publication-blocking press rule: the takeaway bookend lands the judgment,
and the Verdict block is a leftover from the paper's earlier template). It held
no unique fact — its "controlled series ... players allowed to prepare ... which
DeepMind did not run" point is already carried by the superhuman section's first
paragraph and by the takeaway. Nothing needed folding out of it. The components
that remain each earn their place: numbered steps carry the three-stage training
pipeline (a real ordered process); the comparison table is the article's own
contribution, pinning the two agents side by side; the holds-up grid is the
grading itself, separating specific strengths from specific caveats, and it does
work the takeaway's plain prose does not. The recurring house stack
(stat-strip / figure / table / note) is not reproduced — no stat strip, no note
— so the piece does not read as the stamped furniture sequence.

## Reader

Straight through as the paper's declared reader: what I have that the sources
alone would not give me is the clean separation of the two AlphaStar agents and
what each one's record does and does not prove — the December demonstration agent
(looser, whole-map, one off-race pro, a live loss) set against the Nature ladder
agent (camera, 22/5s cap, ablations that cost it strength, anonymous Grandmaster
play). The paper is gated and technical, the DeepMind posts are promotional, and
Korzekwa's analysis covers only the January demo; none of them hands the reader
this synthesis. The original-work sentence in the handoff claims exactly this,
and it survives. The prose sits closer to the voice-guide exemplars than to a
median summary. Read as the largest claim, the headline is established by the
body.

## Edits

- Removed the closing Verdict note (`nb-note nb-note-strong`) from the "superhuman" section — publication-blocking press rule; it restated the finding and held no fact not already in the body or the takeaway.
- Changed the comparison table's December "Action limit" cell from "looser, uncapped bursts" to "looser limits" — "uncapped" overstated the primary, which says only "less restricted in how often it could act."

## Required work

- **orchestrator:** re-stamp before the PR. Removing the Verdict note dropped roughly 60 words, so the nb-meta `words`/`reading_minutes` and the header byline need the stamp to recompute (still comfortably inside the 1200–2200 band). Per the brief, I did not run `nb stamp`.

No work for the researcher or the writer. No source asset is required: the central "constraints cost strength" claim is followable in prose, and the paper's figures were gated.

## Decision

approve — the publication-blocking Verdict note is removed and the one display-text overstatement is corrected; the January-versus-Nature separation is clean throughout and every load-bearing claim, including TLO's authorship, checks against its primary.

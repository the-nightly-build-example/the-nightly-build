# writer brief: the-instruments/squad (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/editorial-direction.md — house standard, press voice, series prompt, template identity
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/commission.md — assignment, boundaries, required contribution, recent shapes/phrasing to break
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/writing-coach/01/voice-guide.md — how this piece should sound, with exemplars
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/researcher/01/evidence.md — the complete claim set
- Article to edit in place: /home/user/the-nightly-build/.nb-work/the-instruments/squad/library/the-instruments/squad.html
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/squad/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-instruments/squad/library/the-instruments/squad.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/97d053c3-1b59-5f4b-8b78-5c56b444e4a1/scratchpad/library-checkout

This round's focus — the evidence record CORRECTS two things the commission got
wrong. Follow the evidence, not the commission, on these:
- The January 2018 systems crossed the human **exact-match** score, NOT human F1.
  On EM: Microsoft 82.650 and Alibaba 82.440 vs the human 82.304. On F1 humans
  still led by about 2.6 points (human 91.221 vs the top ensembles at roughly
  88.5-89.3). Write "human exact match." The angle gets sharper, not weaker: the
  press turned an exact-match result into "machines out-read people." Do not
  assert a human-F1 crossing — the leaderboard disproves it.
- The SQuAD 1.0 human number was a **single** crowdworker's second answer scored
  against the others — one human, no vote. The "majority-vote / multi-reference"
  description belongs to SQuAD 2.0, not 1.0. Keep them straight.
- The exact Jan-2018 leaderboard scores rest on a dated third-party snapshot plus
  two corroborating primaries (the SQuAD 2.0 paper's wording and the Stanford NLP
  announcement); there is no live-URL primary for the live leaderboard state.
  Cite the resolving pages the evidence record lists; do not imply a live
  leaderboard URL shows these historical scores.

Define EM and F1 in plain words at first use (do not assume the reader knows
precision/recall). Everything else per your skill. Fill nb-meta: date 2026-08-23,
harness `claude-code-routine`, model `claude-opus-4-8`, tags per the commission
(benchmarks, reading-comprehension, evaluation, squad). Write the one-sentence
original-work statement in draft-handoff.md. Iterate with --no-check-links, then
run full `nb stamp` + `nb check` until `BLOCK: 0`, and do the display-text
self-test before handing off — the EM-vs-F1 correction must be right in the
headline, dek, and subheads especially.

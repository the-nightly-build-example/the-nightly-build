# editor review-brief: the-instruments/squad (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/commission.md
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/writer/01/brief.md — the exact writer brief (carries the two evidence corrections)
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/writer/01/draft-handoff.md
- Article: /home/user/the-nightly-build/.nb-work/the-instruments/squad/library/the-instruments/squad.html
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/squad/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/editor/01/editorial-review.md

Recent-pattern notes (catch what one article cannot show):
- Series openers to break: "one X per Y, N tries to match it" (imagenet); the
  numeric "the fall from A to B" heading. Confirm sections are in SQuAD's own
  nouns.
- Closer echo to watch: imagenet ended on "Whose vision the 5.1 percent belonged
  to." The human-baseline material is central here; make sure the closing section
  does not rhyme with that heading.
- House catchphrases / banned dek molds (spec/headlines.md): semicolon reversal,
  suspended question, comma triad. Check the dek.

Round focus — verify most skeptically:
- The load-bearing correctness fact: the January 2018 crossing was human EXACT
  MATCH, not human F1 (Microsoft 82.650 / Alibaba 82.440 vs human 82.304 EM;
  humans still led F1, best machine ~89.28 vs 91.221). This must be right in the
  headline, dek, every subhead, and any table. A slip here asserts something the
  leaderboard disproves.
- The SQuAD 1.0 human baseline was ONE crowdworker's second answer, no vote (the
  majority-vote method is SQuAD 2.0's). Confirm the draft keeps them straight.
- EM and F1 must be defined in plain words at first use (no assumed
  precision/recall).
- The historical Jan-2018 scores rest on a dated snapshot plus two corroborating
  primaries; the piece must not imply a live leaderboard URL shows them.
- Audit every data-nb-kind (7 primary + 2 secondary claimed) and open every
  citation href as printed.

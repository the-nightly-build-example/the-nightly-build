# Draft handoff: the-instruments/codeforces-rating (01)

## Original-work sentence

The article places the AI ratings that the sources report separately onto one
axis keyed to Codeforces' own 2013 title thresholds, turning figures from three
different papers into a single picture that shows the same o1 moving 541 points
on scaffolding alone and lets a reader read o3's estimated 2724 against the
"175th best programmer" gloss the launch dropped its qualifiers to reach. The
synthesis is visible in the chart (Fig. 1) and in the title-anchored readings the
prose draws against it (1238 as Pupil, 1673 as Expert), which no single source
performs.

## Proof result

`./nb check --series the-instruments --library /home/user/library-checkout ...`
(links on) → **BLOCK: 0, WARN: 0, verdict PUBLISHABLE. 8 sources.**

- Added source s8 (secondary) from the researcher's `researcher/02/evidence.md`:
  VentureBeat's o3 announcement report (David & Franzen, 20 Dec 2024), cited at
  the o3 gloss the article already critiques — it carries a flat 2727 and a human
  comparison ("achieves a Codeforces rating of 2727," beating OpenAI's chief
  scientist) with no estimated/simulated qualifier. This clears the earlier
  W-SOURCES-MIN (was 7; floor 8). The "175th best competitive programmer" framing
  stays attributed to the launch via coverage, since the record could not open a
  primary that owns it (OpenAI's 12-days livestream pages return 403).
- W-SENTENCE-DENSITY warnings (three at first pass, one introduced by the s8
  edit) were all fixed by splitting sentences. Final proof is WARN: 0.

## Open evidence question (owner: researcher) — RESOLVED

The earlier gap (needing an 8th opened source that bears on an existing claim)
is closed by the researcher's `researcher/02` VentureBeat source, now cited as
s8. No open evidence question remains. One partial limit stands and is handled in
the prose: no primary owns the "175th best competitive programmer" livestream
line (OpenAI's 12-days pages 403), so that specific gloss stays attributed to the
launch and its coverage rather than to a primary.

## Evidence caveats honored (per brief)

- No "these ratings never went through the real judge" claim. Section
  "What actually-judged runs and contamination checks show" states that AlphaCode
  did submit to the live Codeforces judge on finished contests; the honest split
  drawn is retroactive entry into a closed contest vs. a live sitting, and the
  estimate is the derived rating, not the pass/fail.
- No Codeforces-specific contamination claim. The same section reports that
  LiveCodeBench found the memorization drop on LeetCode and smooth Codeforces
  performance, and uses it to cut against the contamination story.
- Every rating is pinned to its source and conditions: AlphaCode 1238 / top 54.3%
  on ~1M samples filtered to ≤10 (s4); the OpenAI ladder 808→2724 with o1 at
  1673 vs 2214 on scaffolding (s5); o3's paper 2724 separated from the circulated
  2727 / "175th" gloss (s5 owns 2724; the gloss is attributed to the launch, not
  to a primary).
- Title thresholds are dated to the 2013 post and flagged as since-shifted.

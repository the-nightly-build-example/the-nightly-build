# review brief: the-instruments/codeforces-rating (editor/01)

Inputs (read in the order the editor skill names):
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound (read first).
- `commission.md` (artifact root) — the assignment, boundaries, and reader situation.
- `writer/01/brief.md` — the exact writer brief (so a leak is visible against it).
- `researcher/02/evidence.md` — the evidence record to audit against (02 supersedes 01;
  it adds the 8th source, VentureBeat). Leave closed until the skeptic read calls for it.
- `writer/01/draft-handoff.md` — the writer's handoff (original-work sentence closed until third read).
- The article: `.nb-work/the-instruments/codeforces-rating/library/the-instruments/codeforces-rating.html`,
  and beside it `chart-1.py` + `chart-1.png`.
- Template context under `.nb-work/the-instruments/codeforces-rating/.nb-context/`.

Output: `.nb-work/the-instruments/codeforces-rating/agent-artifacts/the-instruments/codeforces-rating/editor/01/editorial-review.md`

Round focus:
- The beat: explain where the number comes from and show one real case where it misled.
  Verify the load-bearing spine — a Codeforces rating is an Elo-style standing relative to
  a live human field, and every AI figure is an ESTIMATE from simulated participation,
  condition-dependent. Push on any sentence that overstates.
- Two framings the record explicitly corrects (honor the RECORD): AlphaCode DID submit to
  the live Codeforces judge on finished contests (so no "never went through the real judge"
  claim), and there is no Codeforces-specific contamination claim. Confirm the draft honors
  both.
- Numbers: every rating pinned to its source and conditions (the o1 1673-vs-2214 scaffolding
  swing; AlphaCode 1238 / top-28% on up to ~1M samples; o3 2724 estimated vs the 2727 launch
  gloss). The "175th best competitive programmer" line must be attributed to the launch via
  coverage (VentureBeat, s8), NOT to a primary that owns it. Audit every data-nb-kind.
- Chart: inspect `chart-1.py` provenance and compare every plotted number against the
  evidence record and cited primary; read `chart-1.png` as a reader (axes, scale, labels,
  the 2013 title thresholds dated and flagged as since-shifted). Route any chart correction
  to the writer, who holds the tooling.

Recent-pattern notes (compare edges, headings, dek, furniture against these):
- House tics forming across the paper, cut on sight if present: the takeaway mold
  "Read [the number] as what it is, and ask separately whether Y" (bfcl AND clip both closed
  on it); the why-bookend closer "By the end you will be able to say exactly what X shows and
  what it leaves untested"; the phrase "doing the work" (bfcl: "the set is doing as much of
  the work as the model is"); the device "It is tempting to say X. That goes too far."; the
  negative-parallelism reflex.
- The last Instruments piece was bfcl; it opened "Every few weeks a lab announces that its
  newest model is better at X, and points to a Y-score to prove it." If this draft's opener
  or takeaway is built to bfcl's shapes, it is a formula — break it without copying prior
  structure.

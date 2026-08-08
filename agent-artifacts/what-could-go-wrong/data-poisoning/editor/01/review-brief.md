# editor review-brief: what-could-go-wrong/data-poisoning (01)

Inputs:
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/editorial-direction.md — the standard you enforce
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writing-coach/01/voice-guide.md — read first; judge licensed forms against it
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/researcher/01/evidence.md — the claim set; open as an opponent
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writer/01/brief.md — the EXACT writer brief (instruction-leakage checks)
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writer/01/draft-handoff.md — original-work sentence + two editorial notes (third read only)
- .nb-work/what-could-go-wrong/data-poisoning/library/what-could-go-wrong/data-poisoning.html — the article
- .nb-work/what-could-go-wrong/data-poisoning/.nb-context/ — template context

Output: .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/editor/01/editorial-review.md

After any direct cuts, run `./nb stamp` (from /home/user/the-nightly-build); the
writer runs the proof. Do not edit markup, assets, or sources — route those. NOTE:
the draft is at 2198 words against a 2200 ceiling, so your cuts must not be undone
by added prose; if a fix needs new prose, route it to the writer with room to cut
elsewhere.

Round focus, hardest push (this is the whole point of the piece):
- The "does not compose" discipline must hold everywhere: "easy to install"
  (Souly, ~250 docs, NOT tested through safety training, decays under clean
  training, <=13B) and "survives safety training" (Sleeper Agents, hand-installed
  by SFT) must stay in SEPARATE frames and never be chained into a single "any model
  could already carry a safety-surviving 250-document backdoor" claim. Hunt for any
  sentence, heading, or the table that lets them compose. The writer's four-row
  table is designed so the "how the trigger got in" and "survived safety training?"
  columns never align in one row — verify that holds.
- Name the gap in BOTH directions (no in-the-wild frontier backdoor shown; but
  lab-demonstrated persistence is real). Cut doom and cut dismissal alike.
- The writer flags two source titles (OATML blog, Fortune) as descriptive, not
  verbatim published headlines. Verify each source's real title and, if wrong, route
  the exact correction to the writer (source text is markup you do not edit).
- Verify every rate against its owning primary; some Sleeper Agents per-variant
  figures live only in charts — confirm any precise figure or require the range.

Recent-pattern notes: the what-could-go-wrong shelf recently uses "Where the
evidence stops and X takes over" and nb-position; check headings are this argument's
own and furniture is chosen for the argument.

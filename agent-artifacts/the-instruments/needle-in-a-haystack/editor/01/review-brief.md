# editor review-brief: the-instruments/needle-in-a-haystack (01)

Inputs:
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/editorial-direction.md — the standard you enforce
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writing-coach/01/voice-guide.md — read first; judge licensed forms against it
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/researcher/01/evidence.md — the claim set; open as an opponent
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writer/01/brief.md — the EXACT writer brief (instruction-leakage checks)
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writer/01/draft-handoff.md — original-work sentence + asset/RULER decisions (third read only)
- .nb-work/the-instruments/needle-in-a-haystack/library/the-instruments/needle-in-a-haystack.html — the article
- .nb-work/the-instruments/needle-in-a-haystack/.nb-context/ — template context

Output: .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/editor/01/editorial-review.md

After any direct cuts, run `./nb stamp` (from /home/user/the-nightly-build); the
writer runs the proof. Do not edit markup, assets, or sources — route those.

Round focus, hardest push:
- Verify the retrieval-vs-reasoning line holds: "finding the planted fact" and
  "using the whole document" stay two clearly separate capabilities, and no
  near-perfect NIAH number is allowed to imply the second.
- The writer changed two things under pressure from the primaries: (1) the source
  asset is now the Anthropic prompt-diff (`asset-1.png`, captured via nb asset from
  the cited primary), NOT a green/red grid, because the post carries no grid;
  inspect the asset, its crop, alt text, and cited caption against the primary. (2)
  the RULER "models holding at 32K" figure was corrected against RULER's own
  effective-length table. Re-verify both against the owning primaries.
- Any verbatim quote must match its source character-for-character; the NoLiMa
  example must read as an explicit hypothetical, not a fabricated quoted needle.

Recent-pattern notes: the-instruments shelf recently opens "From <raw> to one
<number>" and leans on nb-stat-strip. Check headings are named from the eval's
construction and furniture is chosen for the argument.

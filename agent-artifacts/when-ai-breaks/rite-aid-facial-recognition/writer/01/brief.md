# writer brief: when-ai-breaks/rite-aid-facial-recognition (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/agent-artifacts/when-ai-breaks/rite-aid-facial-recognition/editorial-direction.md
  — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/agent-artifacts/when-ai-breaks/rite-aid-facial-recognition/commission.md
  — the incident, the angle, source direction, nb-meta values.
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/agent-artifacts/when-ai-breaks/rite-aid-facial-recognition/writing-coach/01/voice-guide.md
  — how this piece should sound; read before drafting and before every revision.
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/agent-artifacts/when-ai-breaks/rite-aid-facial-recognition/researcher/01/evidence.md
  — the complete claim set; cite only from it.
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/.nb-context/
  — the effective template contract, runtime assets, and furniture catalogs.
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/library/when-ai-breaks/rite-aid-facial-recognition.html
  — the initialized article to edit in place.

Output: /home/user/the-nightly-build/.nb-work/when-ai-breaks/rite-aid-facial-recognition/agent-artifacts/when-ai-breaks/rite-aid-facial-recognition/writer/01/draft-handoff.md
(the original-work sentence, the proof result with any warning intentionally left, and any open evidence/voice question).

Proof (run from repo root /home/user/the-nightly-build, iterate with --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/when-ai-breaks/rite-aid-facial-recognition/library/when-ai-breaks/rite-aid-facial-recognition.html --series when-ai-breaks --library /home/user/library-checkout --no-check-links`
- Final: the same command WITHOUT `--no-check-links`, and run `./nb stamp .nb-work/when-ai-breaks/rite-aid-facial-recognition/library/when-ai-breaks/rite-aid-facial-recognition.html` first, until `BLOCK: 0`.

nb-meta to fill: date `2026-08-12`, harness `claude-code-routine`, model
`Claude Opus 4.8`, and three descriptive tags (e.g. facial-recognition, base-rate,
ftc). Keep nb-meta `dek` identical to the rendered dekline.

This round's focus: tell the incident in order (what the system was built to do,
what it did, who it hurt, what Rite Aid did after), naming people, the company, and
dates, then teach why this kind of system fails this way, then close on where the
same weakness lives now. Keep reported fact, allegation, and analysis distinct
throughout.

Handle these from the evidence record with care; they are where this lesson is
easy to get wrong:
- Everything from the FTC is an allegation resolved by a consent order in which
  Rite Aid neither admitted nor denied the claims. Frame it that way every time,
  including the incident involving an 11-year-old, which is sourced only to the
  FTC. Give Rite Aid's own position (its statement, and any claim it makes about
  limited scope or discontinuation).
- Teach the base-rate mechanism as the lesson's own fresh work. Rite Aid never
  measured its own per-scan false-match rate (that failure is part of the charge),
  so any worked calculation must be built from clearly-labeled illustrative
  numbers, not reported ones. The NIST false-match thresholds (FMR 0.00001 and
  0.00003) are legitimate illustrative anchors; a plausible store-traffic figure
  and watchlist size are illustrative and must be marked as such. Make the reader
  feel why "usually right per scan" and "most alerts are false" are both true at
  once.
- The demographic-skew mechanism must be stated honestly, not overstated. NIST
  (NISTIR 8280) measured false-match-rate differences across demographic groups
  that are large in many algorithms but not all (some one-to-many systems, e.g.
  Idemia, showed little), on good-quality government photos. Rite Aid used
  low-quality CCTV images and unknown algorithms and never measured its own by-race
  error; the complaint's demographic claims are circumstantial (store siting,
  low-confidence-score proxies). The honest construction is: demographic
  false-positive skew is real and often large, and Rite Aid never checked which
  kind of system it had, so layering measured field-wide skew onto its base-rate
  problem is a well-grounded expectation, not a proven Rite-Aid measurement. Do not
  write that NIST proved Rite Aid misread specific groups by a 10-to-100x factor.
- If you use a NIST figure as a source asset, the evidence record's crop caution
  applies: presenting Figure 26 (skewed algorithms) without Figure 27 (uniform
  ones) misrepresents the report. Use `nb asset` only if the argument spends what
  the visual shows, and keep the caption factual.

Link `when-ai-breaks/facial-recognition-wrongful-arrest` in Background (it already
teaches face-matching misidentification and NIST demographic error) and
`when-ai-breaks/compas-recidivism` if useful; do not re-teach what they cover. This
lesson's fresh contribution is the base-rate-times-scale mechanism in a private
mass-surveillance deployment. Link only already-published library pages — do NOT
link tonight's sibling articles.

Furniture: plan prose and furniture together from the catalogs under `.nb-context`.
A component that carries the base-rate arithmetic (a worked figure, a small table,
or numbered steps) may earn its place; use documented markup only, and mark
illustrative numbers as illustrative in the prose, not only in a caption. Build a
chart only from a verified numeric series; do not invent data.

Habits not to inherit (house formulas the recent library shares across desks):
- Do not open "Why this matters" on a nostalgic or second-person recall ("You may
  remember when...", "If you have heard one thing about..."), and do not pivot the
  opener on "This lesson follows/tells...". Find a fresh way in.
- Do not close the opener on a "set the two things side by side" line, and do not
  land "The takeaway" on a "So next time you [see/meet] one..." portable rule. The
  desk's required close on where the weakness lives today is welcome; write it as
  this incident's own finding, not the stock second-person sentence.
- Do not use "this desk" or any self-reference in the body; the body narrates no
  one.
- When-ai-breaks' recent dek molds are "[the system] was doing exactly what it was
  built to do, [deflation]" and "[removing a safeguard] let [error] scale to [$big
  number] against [N] people." Write a dek built neither way. Vary section headings
  away from the "The X that Y" relative-noun-phrase mold and the "noun, the
  appositive" comma mold; each heading is a step in this incident's own nouns, no
  scaffolding slots.

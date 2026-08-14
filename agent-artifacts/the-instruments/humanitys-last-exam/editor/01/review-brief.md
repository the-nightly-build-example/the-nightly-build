# editor review-brief: the-instruments/humanitys-last-exam (01)

Inputs (under the article's agent-artifacts root unless noted):
- `editorial-direction.md` — house standard, paper voice, lesson identity, series prompt.
- `commission.md` — the assignment, boundaries, and the reader's situation.
- `writer/01/brief.md` — the exact writer brief (check for leakage against it).
- `writing-coach/01/voice-guide.md` — read first; compare distinctive phrasing against its quoted passages.
- `researcher/01/evidence.md` — the claim set the article may draw on.
- `writer/01/draft-handoff.md` — proof result and original-work sentence (open at the third read).
- Article: `.nb-work/the-instruments/humanitys-last-exam/library/the-instruments/humanitys-last-exam.html`, with `chart-1.py`/`chart-1.png` in the sibling slug directory.
- Template context: `.nb-work/the-instruments/humanitys-last-exam/.nb-context/`.

Output: `.nb-work/the-instruments/humanitys-last-exam/agent-artifacts/the-instruments/humanitys-last-exam/editor/01/editorial-review.md`

Round focus:
- Sourcing is the sharpest risk. Two OpenAI-owned figures (deep research 26.6% with tools; GPT-5 24.8% no-tool / 42.0% with tools) could not be fetched from openai.com (403) and are cited to Fortune and Vellum. Audit every `data-nb-kind` against the primary/secondary test: a source that repeats an OpenAI number is secondary. Confirm no figure is labeled primary-to-OpenAI when only a repeater was opened. The writer flags that attributing these to their OpenAI primary pages would need a new researcher pass reaching a non-blocked path — decide whether the current honest secondary attribution is acceptable or route a researcher request; do not have the writer invent a primary citation.
- Verify the chart (two dated series, no-tool vs tool-assisted) provenance against the evidence record and read the image as a reader: the claim rests on Fortune's "nearly threefold jump" being a tool-assisted point read off the no-tool line. Check the picture is honest about which series each point sits on.
- Check the misreading is framed against the benchmark's own stated scope (the authors' warning that a high HLE score would not by itself indicate autonomous research capability or AGI) and that the 18–29% answer-key error range is attributed to its owners (FutureHouse audit and the authors' recheck).
- Confirm the latest leaderboard figure is presented as a live read dated 2026-08-14, not a standing fact, and the two composition discrepancies are given as ranges.

Recent-pattern notes for this desk (the-instruments):
- The recent signature move is "you can move the score from X% to Y% with a trivial change" (rouge, alpacaeval, fid, mmmu, truthfulqa). If the piece drifts into that gameability frame instead of HLE's own story (low by construction, rises fast, tool/no-tool conflation), flag it.
- Recent deks state a single demonstration as a plain fact; check the dek is built in HLE's nouns and headings vary in construction and read as argument steps.

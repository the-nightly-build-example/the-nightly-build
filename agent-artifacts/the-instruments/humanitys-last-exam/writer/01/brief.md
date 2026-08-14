# writer brief: the-instruments/humanitys-last-exam (01)

Inputs (under the article's agent-artifacts root unless noted):
- `editorial-direction.md` — house standard, paper voice, lesson identity, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplars.
- `researcher/01/evidence.md` — the complete claim set. Draft only from it.
- Article to edit: `.nb-work/the-instruments/humanitys-last-exam/library/the-instruments/humanitys-last-exam.html` (initialized from the lesson template).
- Template context: `.nb-work/the-instruments/humanitys-last-exam/.nb-context/`.

Output: `.nb-work/the-instruments/humanitys-last-exam/agent-artifacts/the-instruments/humanitys-last-exam/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/the-instruments/humanitys-last-exam/library/the-instruments/humanitys-last-exam.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/4555dd06-1325-5643-8ae1-70035fc82956/scratchpad/library-checkout`
(Use `--no-check-links` while iterating; run the full command, links included, until `BLOCK: 0`. Run `nb stamp` before the final check.)

Sourcing constraints from the evidence record:
- Some OpenAI-owned tool/no-tool figures could not be fetched directly (host returned 403) and are carried through the HLE paper, Fortune, and a secondary that cites OpenAI. Cite each figure to the source the record actually opened, and set `data-nb-kind` by the primary/secondary test the record assigns — do not label a secondary that repeats an OpenAI number as primary.
- The current leaderboard is a live read dated 2026-08-14; present any "latest" score as of that date, not as a standing fact.
- Two minor primary-vs-primary discrepancies (multiple-choice fraction ~20% vs 24%; multimodal ~10% vs 14%) are logged with ranges; give the range, not a false precision.

Angle: teach how an HLE score is manufactured (near-1,000 expert contributors, adversarial filtering that only admits questions frontier models already fail, ~2,500 public questions, model-judge grading, calibration error), then what a low score and a fast-rising score each do and do not mean. Land the documented misreading: the tool-assisted number read as "the frontier of human knowledge," and the tool-vs-no-tool conflation (e.g. GPT-5 ~24.8% no-tool vs 42.0% with tools). The misreading is against the benchmark's own stated scope — the authors' paper explicitly warns a high HLE score would not by itself indicate autonomous research capability or AGI, and FutureHouse's audit found a large share of bio/chem answers wrong. Use these to bound what the number supports.

Recent the-instruments habits not to inherit:
- The desk's recent signature move is "you can move the score from X% to Y% with a trivial change" (rouge, alpacaeval, fid, mmmu, truthfulqa). HLE's honest story is different: scores are low by construction and climb fast, and the misread is about the name and tool/no-tool conflation. Do not force the gameability frame.
- Vary dek and heading construction; recent deks state a single demonstration as a plain fact. Build this dek in HLE's own nouns.

Original work: name in one sentence, in draft-handoff.md, what this article does to the evidence that the evidence does not do itself.

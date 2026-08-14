# writer brief: the-evidence/textbooks-are-all-you-need (01)

Inputs (all under the article's agent-artifacts root unless noted):
- `editorial-direction.md` — house standard, paper voice, lesson identity, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplars.
- `researcher/01/evidence.md` — the complete claim set. Draft only from it.
- Article to edit: `.nb-work/the-evidence/textbooks-are-all-you-need/library/the-evidence/textbooks-are-all-you-need.html` (already initialized from the lesson template).
- Template context: `.nb-work/the-evidence/textbooks-are-all-you-need/.nb-context/` (effective contract, furniture catalogs, runtime assets).
- Asset capture, if any, goes under the workspace beside the article.

Output: `.nb-work/the-evidence/textbooks-are-all-you-need/agent-artifacts/the-evidence/textbooks-are-all-you-need/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/the-evidence/textbooks-are-all-you-need/library/the-evidence/textbooks-are-all-you-need.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/4555dd06-1325-5643-8ae1-70035fc82956/scratchpad/library-checkout`
(Use `--no-check-links` while iterating; run the full command, links included, until `BLOCK: 0` before handing off. Run `nb stamp` on the article before the final check.)

This round's focus: the evidence record's guardrail is load-bearing. phi-1's headline result (50.6% HumanEval) is real, but the paper's own Section 5 decontamination shows the honest margin over a 12x-larger model shrinks to a few points on non-similar problems and reverses under the most aggressive pruning, and the training data was distilled from GPT-3.5/GPT-4. Land the defensible reading the record names: curated data bought real efficiency, not the headline magnitude. No hype, no debunk-for-sport; show the numbers and let them carry it. Keep the contamination discussion specific to phi-1's own pipeline (do not generalize into a benchmark-contamination essay). Do not present GSM1k as a verdict on phi-1 specifically; the record flags it targets phi-1.5/2/3.

Recent the-evidence habits not to inherit (break these, do not copy any prior structure):
- The desk's signature reveal — "the famous document doesn't actually say what it's cited for" / "the paper got its own explanation wrong" — has run in several recent pieces (gpt-2, batch-normalization, stochastic-parrots). This piece has a real version of that tension; make it in phi-1's own particulars, not that stock framing.
- Recent deks lean on a single headline figure plus a named-authors-reported-N-in-year clause (word2vec, grokking, emergence-loss-perspective). Vary the dek's build; do not stamp that mold.
- Vary section-heading construction; recent headings and deks recur as comma-and constructions. Headings are steps of this argument in phi-1's nouns.

Original work: name in one sentence, in draft-handoff.md, what this article does to the evidence that the evidence does not do itself.

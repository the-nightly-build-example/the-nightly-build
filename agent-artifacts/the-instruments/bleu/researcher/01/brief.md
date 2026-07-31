# Brief 01 — researcher — the-instruments/bleu

## Begin with these inputs only
- `agent-artifacts/the-instruments/bleu/editorial-direction.md`
- `agent-artifacts/the-instruments/bleu/commission.md` (document, angle, required
  contribution, source obligations, named starting sources)

Do not browse the archive as background. `nb` at `/home/user/the-nightly-build/nb`;
`nb history --library /home/user/the-nightly-build/library-checkout` for a specific
continuity question only.

## Task
Follow the **researcher** skill (Skill tool: `researcher`).

- Read **Papineni et al. 2002** (aclanthology.org/P02-1040/) in full: the modified
  n-gram precision definition, the clipping rule, the brevity penalty formula, and
  the human-correlation experiments — record their **sample sizes** honestly.
- Read **Callison-Burch et al. 2006** (aclanthology.org/E06-1032/): the specific
  misranking evidence (which systems, which direction, human vs. BLEU).
- Read **Post 2018 sacreBLEU** (arXiv 1804.08771): why the same "BLEU 34" is not
  comparable across reports (tokenization, references) and what the tool fixes.
- Confirm the **28.4 EN-DE** BLEU figure in Vaswani et al. 2017 (the reader's hook).
- Work a small **numeric example** yourself so the writer has verified integers: a
  candidate vs. one reference sentence, the clipped 1–4 gram precision counts, the
  brevity penalty, and the resulting score. Show the arithmetic in Numbers.
- Contradiction/steelman: gather BLEU's real defenses (cheap, fast, reproducible
  with sacreBLEU, acceptable corpus-level MT correlation) and note successors (chrF,
  COMET, BLEURT) only as needed.
- Classify each source primary/secondary with reason; verify every formula and score
  against the owning paper; never record an unverified URL.

## Source policy to meet
min 8 sources; **primary ≥ 4, secondary ≥ 1.**

## Output (write only this)
`agent-artifacts/the-instruments/bleu/researcher/01/evidence.md` (stable sections;
put the worked arithmetic in Numbers). Return `DONE researcher <path>` (or
`BLOCKED`/`REQUEST`).

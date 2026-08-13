# writer brief: the-instruments/rouge (01)

Inputs (all paths under this article's artifact root unless absolute):

- `editorial-direction.md` — house standard, slop, headline standard, press voice,
  lesson identity, series prompt. Binds every sentence.
- `commission.md` — the measurement, angle, neighbors, required contribution. Note:
  the evidence corrects the commission's too-clean "misled" claim; follow the
  evidence.
- `writing-coach/01/voice-guide.md` — how this piece should sound; read before
  drafting; reuse the subject's terms, never the exemplars' phrasings.
- `researcher/03/evidence.md` — THE evidence record to use (it carries rounds 01
  and 02 forward and adds the secondary). Do not use the earlier numbered records;
  03 is the complete, current one.
- Article to edit in place:
  `/home/user/the-nightly-build/.nb-work/the-instruments/rouge/library/the-instruments/rouge.html`
- Template context: `/home/user/the-nightly-build/.nb-work/the-instruments/rouge/.nb-context/`

Output: `writer/01/draft-handoff.md`.

Proof: `./nb check /home/user/the-nightly-build/.nb-work/the-instruments/rouge/library/the-instruments/rouge.html --series the-instruments --library /home/user/library-checkout`
(run from `/home/user/the-nightly-build`).

This round's focus — the evidence reframed the "misled" story; write the accurate
version, not the commission's cleaner-but-wrong one:

- Do not claim ROUGE "correlates weakly with human judgment" in general. The
  record's accurate picture: ROUGE correlates moderately-to-strongly with
  consistency (SummEval 0.53-0.71) but that is confounded by low abstractiveness;
  it is weak on coherence and relevance; ROUGE-L is weak on all four. Keep those
  dimensions distinct.
- The cleanest firsthand meaning-blindness proof is Lin 2004's own reversed-
  sentence example (ROUGE-2 = 1/3 for both a correct and a nonsensical candidate).
  Use it. Build one tiny correct worked ROUGE calculation from the record so the
  reader sees the arithmetic.
- Faithfulness is ROUGE's real blind spot: Maynez 2020 measures ROUGE-vs-
  faithfulness correlation as very weak (Spearman around 0.13-0.20), but the honest
  statement is "ROUGE does not track faithfulness," not "ROUGE rewards the
  unfaithful" (Maynez's best-ROUGE model is also its most faithful). Do not
  overstate.
- Do not miscite the meta-evaluations: Bhandari 2020 found ROUGE-2 the best metric
  on CNN/DailyMail (its real negatives are dataset-non-transfer and top-k
  de-correlation); Graham 2015 is about variant fragility (Pearson r swings
  0.293-0.786 across 192 variants; BLEU matches the best ROUGE), not weak
  correlation. The "extractive scores well, faithful abstractive poorly" clause is
  a news-structure artifact, not a universal law.
- Honest center to keep: ROUGE measures string overlap against a reference, works
  in its home setting (single-doc news, strong references, system-level, weaker
  systems), and degrades off-domain and on the dimensions overlap cannot see.
- Cite the added survey (Sai et al. 2022) as the secondary, as the field's outside
  characterization, not as a standalone correlation number.

Habits not to inherit (from the commission and the recent shelf):

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula, and do not model The Instruments' "every flagship
  ships an X score" opener. Do not land the takeaway on negative parallelism ("a
  high X score is worth what it measures ... It is not a reading of ..."). Deks:
  avoid the banned molds.

Set nb-meta `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`.
Make the display-text pass before proving, and prove to `BLOCK: 0` with links
included.

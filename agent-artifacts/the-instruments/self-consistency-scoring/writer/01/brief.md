# writer brief: the-instruments/self-consistency-scoring (01)

Inputs (artifact root is this file's grandparent directory):
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity
- ../../commission.md — the assignment and its boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete claim set; treat as evidence, not prose
- The initialized article: /home/user/the-nightly-build/.nb-work/the-instruments/self-consistency-scoring/library/the-instruments/self-consistency-scoring.html
- Template context: /home/user/the-nightly-build/.nb-work/the-instruments/self-consistency-scoring/.nb-context/

Output: draft-handoff.md (this directory)

Proof (run from /home/user/the-nightly-build; iterate with `--no-check-links`, run `nb stamp` before the final pass, then run with links until `BLOCK: 0`):

```
./nb check .nb-work/the-instruments/self-consistency-scoring/library/the-instruments/self-consistency-scoring.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/6299876f-cc26-50aa-a765-ad85a93ca3c3/scratchpad/library-checkout
```

This round's focus:
- Publication date is 2026-09-19. Set nb-meta `date` to it, `harness` to "claude-code", and the writer `model` to the exact model you run as (e.g. `claude-opus-4-8`).
- Spine correction the evidence record requires: do NOT center on labs "hiding" the compute. In all three primary cases (Minerva, o1, DeepSeek-R1-Zero) the lab reported the single-sample number beside the majority-vote number and labeled the metric. Center the misleading case on downstream circulation and cross-model comparison — a voted number quoted without its k, or set beside a rival's single-sample score. The clean in-source instance is Minerva's Table 2, where maj1@k=64 (50.3% on MATH, from 33.6% single-sample) sits one row above a single-sample prior state of the art of 6.9%.
- Use the verified numbers as recorded: Wang et al. GSM8K 56.5%→74.4% (PaLM-540B, 40 samples); Minerva MATH 33.6%→50.3% at k=64; o1 AIME 2024 pass@1 74% vs consensus@64 83%; DeepSeek-R1-Zero AIME cons@64 86.7% vs pass@1 71.0%; Large Language Monkeys (majority voting plateaus while coverage keeps scaling). Note the k× inference cost.
- Link (do not re-teach) the library's humaneval-pass-at-k (pass@k is a different rule), aime, and math-benchmark lessons in Background.

Recent shapes to break (do not inherit from the recent library):
- Deks that lead with a numeric contrast in one long sentence.
- Headings that lead with a raw number or use the comma-and contrast; vary construction.
- The recurring furniture stack (nb-stat-strip, nb-figure, nb-table, nb-note, nb-holdsup). A small table contrasting pass@1 and cons@k figures may earn its place; plan furniture from the supplied catalog rather than by reflex.

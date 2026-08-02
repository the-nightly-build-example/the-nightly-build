# Writer handoff: the-mechanics/over-refusal (round 01)

## Original work

The article builds and marks a step-by-step causal chain from the observed
behavior (a safe prompt refused) down to mechanism, and it makes each step's
epistemic status visible in the prose rather than leaving it implicit:
(1) refusal is installed by fine-tuning on labeled examples, not present in
the base model — settled, sourced to InstructGPT and Constitutional AI;
(2) it generalizes by surface features rather than intent — settled, sourced
to XSTest's own "lexical overfitting" diagnosis; (3) genuine harmful-refusal
is mediated by a single direction in the residual stream, which can be
erased or added — settled for open-weight models, sourced to Arditi et al.;
(4) whether *over*-refusal specifically rides that same direction, or a
separate, higher-dimensional, task-conditioned mechanism that only looks
identical from outside, is explicitly marked open, sourced to the genuine
split between Wollschläger et al. and Maskey et al. The section
"Is over-refusal the same switch, misfiring?" and its closing paragraph
("The chain has a floor, and an open step sits above it. Settled: ... Open:
...") is where this separation is made visible as the article's own move,
not merely reported from any one source.

## Article and asset paths changed

- `/home/user/the-nightly-build/.nb-work/the-mechanics/over-refusal/library/the-mechanics/over-refusal.html`
  (filled in place; no separate asset files — two `nb-table` components built
  directly from the evidence record's verified numbers, no `nb chart` or
  `nb asset` used).

## Proof result

```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series the-mechanics \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/the-mechanics/over-refusal/library/the-mechanics/over-refusal.html
```

Final result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.

The first full draft ran 2989 words against the lesson's 1200-2200 band and
carried 12 sentence-density warnings and an all-caps table-caption
placeholder warning. All were fixed by rewriting rather than waved off: table
headers/captions moved from the furniture doc's sample all-caps style to
normal sentence case (matching the published back-catalog's actual
convention, e.g. `what-could-go-wrong/jailbreaks.html`); dense multi-clause
sentences were split using the engine's own `sentence_density` heuristic
(read from `engine/nb/proof/prose.py`) to locate every remaining offender
precisely; and the body was cut from 2989 to 2198 words (a ~26% trim) without
dropping any cited claim, source, or contradiction — every one of the 9
sources, both tables, and all three commissioned ideas survived the cut.
`nb-meta.words` (2198) and `reading_minutes` (9) are the tool's own measured
counts, not estimates.

## Source handling

9 sources numbered in first-citation order: XSTest (1), InstructGPT (2),
Constitutional AI (3), Arditi et al. (4), Wollschläger et al. (5), Maskey et
al. (6), OR-Bench (7), Hasan & Biswas (8, `data-nb-kind="secondary"` per the
evidence record and brief), OpenAI safe-completions (9). 8 primary, 1
secondary, meeting the min-8/primary-≥4/secondary-≥1 policy. `data-nb-locator`
is set on every Sources-list entry from the evidence record's page/section/
table references; none were invented.

## Constraints held

- Banned term "machinery": 0 uses.
- Em-dash: 0 uses (rewrote around every place a draft reached for one).
- "leverage": 0 uses. "load-bearing" / revolutionary / transformative /
  game-changing: 0 uses.
- Agency verbs ("decides", "judges", "understands", "wants", "believes")
  applied to the model: 0 uses. The one permitted "not X, it's Y"-style
  correction of the "it decided this was dangerous" intuition is spent once,
  in the takeaway ("The model never decided the Minecraft question was
  dangerous. A word in it crossed a threshold...").
- The Arditi single-direction result is explicitly scoped to open-weight
  models in the prose itself ("The paper tested only openly released
  models... closed, proprietary models might not work the same way"), not
  just in a source locator.
- Headline states the finding with actors named, no colon-subtitle, no
  comma-triad, no question. Dek adds the concrete Minecraft/GPT-4 detail the
  headline omits. Headings vary in shape and do not echo
  `instructions-are-data`'s "The prompt a model actually sees" or any
  comma-triad recently used on this desk.

## Furniture used

- Two `nb-table` components, both built directly from the evidence record's
  verified figures: XSTest full+partial refusal rates (250 safe / Minecraft
  subtype / 200 unsafe, Llama-2 vs GPT-4) beside idea 1; OR-Bench Hard-1K
  rejection rate across five vendors beside idea 3. No chart was built —
  the evidence record itself flags that a table is the lower-risk choice here,
  and the OR-Bench scatter's full 32-model toxic-rejection axis isn't in the
  numbers the researcher verified in prose, only the Hard-1K column, so a
  table stays faithful to what was actually read.
- The two Arditi worked examples (defamation-under-ablation,
  yoga-under-addition) are carried in prose with verbatim before/after
  quotes rather than a separate `nb-note`, since each is a single
  self-contained contrast that reads cleanly inline and a note would have
  split the "erase it / add it" pairing the prose builds in one motion.

## Remaining evidence or voice questions

None. The evidence record's one flagged gap (no single aggregate
refusal-rate number for Arditi's ablation/addition bar charts) was handled
as the record itself recommended: the HarmBench and worked-example evidence
is what's cited for "erase it, refusal stops," not an invented aggregate
percentage.

## Return

DONE writer /home/user/the-nightly-build/.nb-work/the-mechanics/over-refusal/agent-artifacts/the-mechanics/over-refusal/writer/01/draft-handoff.md

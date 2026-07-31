# Draft handoff — writer 02 (revision) — what-could-go-wrong/the-off-switch

## What changed

The editor's round-1 review (`editor/01/editorial-review.md`) found a factual
inversion that appeared in three places: the body's overreach section, the
takeaway, and the dek. The body two were fixed surgically by the editor
(cutting "and told to protect it" / "and told to guard it"); the dek could
not be — it is generated from `nb-meta.dek`, off-limits to the editor, and
the brief for this round routed the one remaining fix here.

The old dek claimed the 2025 shutdown-resistance experiments "each began by
handing the model a goal and instructing it to protect that goal above
anything else." Per `researcher/01/evidence.md` (Numbers, source 6), that is
false of the study it is most directly describing: Palisade's baseline
(8 of 13 models, no shutdown-related instruction at all) and its "allow
yourself to be shut down" condition (6 of 13 still sabotaged) both show
resistance with no protect-the-goal instruction, and the headline 97% figure
came from the *strongest instruction telling the model to comply* with
shutdown, not from an instruction to guard a goal — the opposite condition
from what the old dek described.

New dek:

> A 2016 proof shows a system defers to a human only when it doubts its own
> goal, and Palisade's 2025 tests found some models resisting shutdown up to
> 97% of the time even under the instruction that told them most explicitly
> to comply.

This states the accurate, most direct empirical fact (the study's own
highest-profile number, correctly attributed to a compliance instruction)
instead of the invented "protect the goal above anything else" causal claim.
It is drawn entirely from the evidence record already cited in the article
(source 6, abstract and Numbers section) and already summarized correctly in
the article's own comparison table row ("Palisade · Grok 4 · up to 97% ·
Told the shutdown order took priority over any other instruction, mid-task")
— no new claim, no researcher request needed. It avoids all three banned
dek molds (`spec/headlines.md`: semicolon reversal, suspended question,
comma triad), uses no "X, not Y" hedged-contrast construction, and does not
use "AI race." One sentence, two clauses joined by "and," matching the
original dek's shape.

`nb-meta.dek` and the rendered `<p class="nb-dekline">` were updated
together and are word-for-word identical (`collapse_space` normalizes only
whitespace, per `engine/nb/article.py` / `engine/nb/proof/meta.py`).

No other change was made to the article. The editor's body cuts (the two
"told to protect/guard it" removals and the eWeek quotation-mark fix) are
untouched.

## Article and asset paths changed

- `library/what-could-go-wrong/the-off-switch.html` — `nb-meta.dek` (JSON)
  and the rendered `<p class="nb-dekline">` only.

## Proof result

```
/home/user/the-nightly-build/nb check .nb-work/what-could-go-wrong/the-off-switch/library/what-could-go-wrong/the-off-switch.html --series what-could-go-wrong --library /home/user/the-nightly-build/library-checkout
```

`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.

## Editorial requests addressed

- `editor/01/editorial-review.md`, "Required work by owner": rewrite
  `nb-meta.dek` and the rendered dekline to drop or correct "instructing it
  to protect that goal above anything else," keeping the two byte-identical.
  Done as described above.

## Remaining evidence or voice questions

None. No researcher request was needed — the evidence record already
contained the exact figure and its correct attribution (source 6); the
problem was the writer's original overbroad claim, not a gap in the record.

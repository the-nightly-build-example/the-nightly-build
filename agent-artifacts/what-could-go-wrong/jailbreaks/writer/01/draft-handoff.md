# Draft handoff — writer/01 — what-could-go-wrong/jailbreaks

## Original-work sentence
The article stitches twelve independent measurements and one mathematical
proof — none of which cites or reconciles any of the others — into a single
argument that draws the commission's exact line (optimizer-found transfer and
partial defenses are demonstrated; robust-refusal impossibility is
conjectured, not proven), while surfacing as one explicit, running thread the
"which model resists best flips by attack family" pattern that the GCG,
Jailbroken, and Adversarial Poetry papers each show independently but never
state as connected to one another.

## Paths changed
- Article: `.nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html`
- Chart + provenance: `.nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks/chart-1.py`
  and `.../jailbreaks/chart-1.png` (GCG Table 2 heatmap: attack success rate
  by target model × attack condition, from arXiv:2307.15043 Table 2).

## Proof result
Final command (with link checking):
```
./nb check .nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html --series what-could-go-wrong --repo /home/user/the-nightly-build --library /home/user/library-checkout
```
Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. No warnings left
intentionally — all W-LENGTH-HIGH, W-SENTENCE-DENSITY, W-PLACEHOLDER, and
W-SELF-COUNT warnings raised during drafting were resolved (word count
trimmed from an initial 2793 to 2197, within the lesson's 1200-2200 band;
`nb-meta` words/reading_minutes updated to the counted totals).

Also confirmed by `nb preview` + a rendered screenshot: the chart heatmap,
stat strip, and results table all render correctly in both light chrome, and
the "Previous" nav link to the prior what-could-go-wrong lesson resolves.

## Editorial requests addressed
None — this is invocation 01 (first draft); no `editorial-review.md` exists
yet for this article.

## Remaining evidence or voice questions
None. The evidence record's one flagged gap (the "dismissive" pole —
jailbreaks don't matter because the information is already public — being
thinly sourced to a discarded blog comment) was not forced into the draft;
the commission's "check confidence against proof in both directions"
requirement is instead met through the Vassilev-proof-versus-anonymous-critics
tension in the CONJECTURE/OPEN section, which the evidence record supports
directly and in full.

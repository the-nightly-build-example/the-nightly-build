# Draft handoff: the-instruments/training-cost (01)

## Original work

The article takes the single figure everyone repeated, $5.576 million, and
decomposes it into its two constructed inputs (DeepSeek's measured 2.788M
GPU-hour count and its separately stated $2/GPU-hour rental assumption) and its
scope (the final training run only, per Table 1's stage split), separates
DeepSeek's own narrow exclusion caveat (prior research and architecture
ablations) from the broader "salaries and hardware capital" framing that
belongs to SemiAnalysis and Bernstein's Rasgon, and then sets the figure
against Nvidia's $589 billion one-day loss while explicitly declining to
assert it as sole cause, a bounded synthesis the evidence supports but does
not state in prose itself. None of that decomposition, attribution split, or
bounded juxtaposition exists in the evidence record as written; the evidence
gives the facts and the contradiction, the article does the sorting.

## Proof result

`./nb stamp` then `./nb check ... --series the-instruments`, iterated with
`--no-check-links` and finished with links checked: **BLOCK: 0, WARN: 0**.
No warning was left intentionally; each one raised during drafting (cite
order, an over-length stat-strip label read as a placeholder, four dense
sentences) was fixed rather than argued down. 1,640 words, 10 sources (4
primary: DeepSeek-V3 report, SemiAnalysis, StockAnalysis.com, StatMuse; 6
secondary), all 10 source links resolve.

Furniture added beyond prose: `library/the-instruments/training-cost/asset-1.png`,
a source-asset crop of the technical report's Table 1 (all four rows, both
columns, and the $2/GPU-hour caption retained), captured with `nb asset pdf`
from the report's own PDF at the coordinates of that table; and
`chart-1.py`/`chart-1.png`, a two-bar chart of Nvidia's Friday-to-Monday close
built from the two cited price-data sources, rendered with `nb chart`. Both
inspected in the rendered preview (`nb preview` + `nb render-check`, phone
width, no overflow).

## This round's corrections, applied

- The report's caveat is quoted verbatim and states only "prior research and
  ablation experiments on architectures, algorithms, or data." The
  salaries/hardware-capital framing is attributed only to SemiAnalysis and
  Rasgon, kept in separate sentences with named owners.
- The Nvidia-loss paragraph states the $5.576M/$589B relationship as
  something coverage tied together (cited to Yahoo Finance) while explicitly
  stating "no source ties the loss to that reading alone" and citing
  Bernstein/Rasgon's contemporaneous caution as the bounding counter-read.
  No sentence claims the misreading as sole cause.
- The multiplication (2.788M GPU-hours x $2 = $5.576M) is written out once,
  on the page, with the stage breakdown following in Table 1.
- No dedicated GPU-hours lesson exists in the library, so GPU-hours are
  defined in plain words at first use (orientation) rather than linked as a
  term; the tokens-per-second lesson is linked in prose as the nearest
  throughput comparison, not as the source of the definition.
- Headline, dek, and section headings avoid both named molds ("The number is
  the model plus the effort"; "Where the same X lives" / "What a high score
  does not promise") and the banned dek constructions (no comma triad, no
  semicolon reversal, no suspended question).
- nb-meta: date 2026-09-15, harness claude-code-routine, model
  claude-sonnet-5.

## Open questions

None. No evidence gap or voice-guide ambiguity blocked drafting.

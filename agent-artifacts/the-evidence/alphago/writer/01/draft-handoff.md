# Draft handoff: the-evidence/alphago (round 01)

## Original work

The visible original work is the ledger table in "What each document actually
proved" (section `what-each-document-proved`): three rows separating what the
2016 Nature paper, the March 2016 Lee Sedol match record, and the 2017 AlphaGo
Zero paper each actually establish from the fused popular claim each now gets
cited for ("AlphaGo beat the world's best," the Lee Sedol match folded into
"the AlphaGo paper," and "AlphaGo learned Go from nothing"). This mapping does
not exist in any one cited source; it is built by cross-reading the two Nature
papers against the three independent Lee Sedol accounts and is stated nowhere
else in the piece more explicitly than in that table. The takeaway resolves the
same ledger in prose ("AlphaGo... is not one fact. It is three.").

## Paths changed

- Article (filled in place): `.nb-work/the-evidence/alphago/library/the-evidence/alphago.html`
- Chart script + provenance: `.nb-work/the-evidence/alphago/library/the-evidence/alphago/chart-1.py`
- Chart image: `.nb-work/the-evidence/alphago/library/the-evidence/alphago/chart-1.png`
  (Elo ladder: AlphaGo Fan 3,144 / AlphaGo Lee 3,739 / AlphaGo Master 4,858 /
  AlphaGo Zero 5,185, all from Silver et al. 2017, p. 12 — rendered as a line
  chart rather than a bar chart since Elo is an interval scale with no true
  zero, so a bar's baseline-at-zero convention would misrepresent it)

## Proof result

`nb check --series the-evidence --repo /home/user/the-nightly-build --library
/home/user/library-checkout` (with link-checking on, as specified in the
brief) on the final draft: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.**

Warnings encountered and resolved during drafting, none left standing:
- Citation order (Nature 2017 was first cited ahead of the Google blog source)
  — fixed by moving an inline Google-blog citation earlier, into the
  orientation section, so first-citation order matches source numbering.
- Eight sentence-density warnings (long, multi-clause sentences) — all split
  into shorter, single-purpose sentences.
- Two stat-strip labels tripped the all-caps placeholder heuristic at 4+ words
  — shortened to "TOURNAMENT WIN RATE" and "HUMAN POSITIONS FIRST."
- Word count briefly ran 23 words over the 2200 ceiling — trimmed.
- `nb-meta` words/reading_minutes were placeholder 0 — set to measured values
  (2174 words, 10 min).

One factual correction made after the proof was already clean, caught on a
final read-through rather than by the automated check: an earlier draft
implied the single-machine AlphaGo configuration (the one with the 99.8%
tournament win rate) was also the one that played Fan Hui. The evidence record
is explicit that the *distributed* version played Fan Hui. Rewrote that
paragraph to keep the two configurations distinct. Also removed an unverified
comparative claim that AlphaGo Lee trained "for months longer" than AlphaGo
Fan — the evidence supports AlphaGo Lee's own training time ("several
months") but not a direct comparison to Fan's, so the comparison was dropped.

Also self-audited against the brief's "use the 'not X, it is Y' shape at most
once" constraint: found it appearing three times in an earlier draft (twice as
scaffolding, once in the takeaway) and cut it to exactly the one instance in
the takeaway, which is the piece's real payoff.

## Editorial requests addressed

N/A — this is round 01, no prior editorial-review.md to apply.

## Remaining questions

None outstanding. All three commissioned ideas (architecture/MCTS,
training pipeline and honest scale, AlphaGo Zero plus the honest present-day
DeepSeek-R1 note) are taught in full within the word band; six sources meet
the primary/secondary composition policy; the Fan Hui/Lee Sedol/AlphaGo Lee
naming discipline the brief fixed is held throughout, including in the chart
and the ledger table.

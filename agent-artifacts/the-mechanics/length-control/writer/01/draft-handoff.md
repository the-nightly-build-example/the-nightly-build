# Writer handoff: the-mechanics/length-control (01)

## Original work

The evidence record establishes the architecture facts (no counter, tokens
are not words) and the trained-in bias fact (RLHF reward-shaping favors
length) as three separate, individually-sourced findings; the article's own
work is arguing that these three compound into the specific word-count-miss
behavior, while explicitly marking that compounding as inference rather than
a measured chain (no source in the record runs the no-instruction reward
finding and the explicit-instruction violation-rate finding on the same
model), and separately holding open, without resolving, the tension between
the hidden-state length-tracking evidence and the self-report failure
evidence.

## Proof result

`./nb check .nb-work/the-mechanics/length-control/library/the-mechanics/length-control.html --series the-mechanics`
(links included): **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.** No warnings
left in place; all W-SENTENCE-DENSITY and W-PLACEHOLDER warnings surfaced
during drafting were resolved by splitting the flagged sentences and
rewriting the stat-strip/table labels out of literal caps (the CSS applies
the uppercase styling). `nb stamp` reports words=2183 (inside the lesson
template's 1200-2200 band), sources=9 (8 primary, 1 secondary, meeting the
commission's 4-primary/1-secondary/8-minimum floor).

Note: `--library` was not supplied, so the proof's own note says open-mode
dedupe and commission checks were skipped in this run; nothing in the
findings list was suppressed as a result (findings list is empty).

## Open questions

None outstanding. Two evidence cautions from the brief were applied as
constraints rather than left open: the IFEval 76.89%/83.57% headline figures
are never cited as length-following numbers (IFEval is cited only for the
"verifiable instruction" / length-constraint-category framing); and the
RLHF reward-shaping finding (Singhal et al., no length instruction in the
prompt) is kept explicitly distinct in the prose from the explicit-instruction
miss-rate findings (Yuan et al., Zhang et al.), with the compounding stated
as the article's own reading, not a citation any one source would sign onto.

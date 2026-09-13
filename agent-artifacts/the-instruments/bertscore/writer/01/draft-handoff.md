# Draft handoff: the-instruments/bertscore (01)

## Original work

The article turns the evidence record's separate mechanism description and
scattered figures into one continuous derivation: it builds recall, precision,
and F1 out of the single greedy cosine-matching rule, walks the rescaling from a
raw 0.9-band score down to its rescaled value with the real documented numbers,
and then reads all three documented failures (function-word blindness, inherited
gender bias, mid-pack human correlation) back off that same "resemblance in the
encoder" computation, so each limit is shown to follow from the recipe rather
than listed as a standalone warning.

## Proof

- `nb stamp` then `nb check ... --series the-instruments --library <checkout>`
  (links included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE.
- stamped: words 1544 (band 1200-2200), sources 8 (7 primary, 1 secondary;
  floor 8 / 4 primary / 1 secondary met), reading 7 min.
- No warnings intentionally left. The three W-SENTENCE-DENSITY warnings from the
  first pass were fixed by splitting the stat-heavy sentences (which also cleared
  a comma-triad risk in the takeaway).
- render-check reported "no Chrome in this environment; skipped." The one
  equation uses only standard KaTeX plus the furniture's documented
  `\htmlClass{nb-mc1..3}{}` macro; typesetting should be confirmed by CI's
  render probe.

## Open evidence / voice question

- The voice guide asks for a worked token pair with stated cosine numbers so the
  reader "watches each candidate token find its partner." The evidence record
  supplies no per-token cosine values for any pair, and inventing them would
  breach the cite-only-what-was-opened rule. I carried the "watch it run" method
  two ways instead: the rescaling arithmetic runs on the record's real numbers
  (raw F1 0.959 to 0.759; corpus 0.931 to 0.576), and the token matching is shown
  qualitatively on Hanna & Bojar's tag-question pair with their reported F1s
  (0.815 vs 0.712). If a per-token worked example is wanted, it needs a new
  researcher artifact supplying the cosine values, not a writer invention.

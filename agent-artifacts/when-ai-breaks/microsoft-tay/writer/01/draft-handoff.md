# Writer draft handoff: when-ai-breaks/microsoft-tay (round 01)

## Original work

This piece separates Microsoft's "coordinated attack exploited a
vulnerability" account, and its own admission that it never named the
vulnerability, from the design-failure reading pressed by Zoe Quinn and
IEEE Spectrum, and says plainly what the record supports: the design-failure
reading has the stronger documentary support because Microsoft never
published the pre-launch testing or postmortem that would let an outsider
check whether coordination was necessary to the outcome or merely
accelerated it. The piece does the same second separation for mechanism:
dictated ("repeat after me") output versus genuinely generated output (the
Gervais/Hitler reply), marking Davi Ottenheimer's rival claim as a real,
if uncorroborated, doubt rather than resolving it either way. Both
separations are visible in the article's own sections ("Microsoft never
named the vulnerability it blamed" and the mechanism section's handling of
Ottenheimer), not asserted only in this handoff.

## Files changed

- Article: `/home/user/the-nightly-build/.nb-work/when-ai-breaks/microsoft-tay/library/when-ai-breaks/microsoft-tay.html`
  (filled in place from the initialized skeleton; no new assets — the brief
  and evidence record confirmed no image/screenshot clears the sourcing bar,
  so the piece is prose plus furniture only: one `nb-timeline` for the five
  dated beats, one `nb-note` for Microsoft's first, neutral statement, and
  one `nb-stat-strip` contrasting Tay's ~16-hour run with XiaoIce's 40
  million filtered users).
- No asset files added.

## Proof result

`nb check --series when-ai-breaks ... microsoft-tay.html` → **BLOCK: 0**,
1 WARN, verdict PUBLISHABLE.

Remaining WARN, left as-is:
- `W-PLACEHOLDER`: "HITLER DID NOTHING WRONG" survives as an all-caps run.
  This is a verbatim quoted tweet (Guardian, source #4), not a placeholder;
  it is one of only two offensive-tweet quotes kept in the piece (the other
  is the targeted tweet at Zoe Quinn) and is the piece's only direct textual
  support for "antisemitic" in the headline/dek. Rewriting its case would
  misquote it, so the warning is accepted rather than fixed.

Warnings surfaced and fixed during drafting (not left open): four
`W-SENTENCE-DENSITY` findings (traced to the engine's actual sentence
splitter, which does not skip citation-superscript text, then split and
shortened), one `W-CITE-DENSITY` on the "today" section (added a citation
to Peter Lee's own closing line), and the stat-strip's all-caps labels
(rewritten to sentence case; the furniture doc's ALL-CAPS samples are
placeholders, not a style to copy, confirmed against how published articles
actually render `nb-stat-l`).

nb-meta filled with measured values: 15 sources, 2,184 words, 9 min reading
time (matching the engine's own `Article.word_count`), harness
`claude-code-routine`, model `claude-sonnet-5`.

## Editorial requests addressed

None — this is round 01, no prior `editorial-review.md` exists yet.

## Remaining evidence or voice questions

None outstanding. Two evidence-record judgment calls were followed exactly
as instructed: Peter Lee is described as "then corporate vice president of
Microsoft Research" throughout (not the blog's current Healthcare byline),
and the piece says "about sixteen hours" everywhere, noting once that
Microsoft's own post (and one BBC piece) rounded it to "24 hours," without
quoting the researcher's derived 16h05m47s as if it were a stated figure.

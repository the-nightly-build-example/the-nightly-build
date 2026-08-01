# Draft handoff — writer 01 — when-ai-breaks/google-flu-trends

## Original-work sentence
The article reconciles Google's own account of the 2012-2013 overestimation
(media-driven query spikes, per Copeland et al. 2013) with Lazer et al.'s
outside critique (algorithm dynamics) by placing both against the exact
timeline each primary supplies: Google's spike-detector story fits the acute
peak Copeland's team dates to the week of January 13, 2013, but Lazer's own
figure shows the overshoot streak beginning August 21, 2011, a year and a
half earlier, which the single-season media-panic account cannot reach on
its own — so the piece reads the two accounts as describing different
stretches of one timeline (a two-year algorithm-driven baseline shift, with
a media-driven spike landing on top of it in the reported season) rather
than treating them as a dispute the record can't settle. Neither primary
states this reconciliation; it is built here from the dates and figures each
one independently supplies.

## Paths changed
- `.nb-work/when-ai-breaks/google-flu-trends/library/when-ai-breaks/google-flu-trends.html`
  (filled in place; no new assets or chart provenance files created — no
  source asset or verified numeric series in the evidence record justified
  one).

## Proof result
Both required commands run to `BLOCK: 0`, verdict `PUBLISHABLE`:
- `--no-check-links`: `BLOCK: 0`, 1 warning.
- Final proof (with link checking): `BLOCK: 0`, 1 warning (same one — link
  checking changed nothing).

Warning left standing, with reason:
- **W-SOURCES-MIN — 7 sources; series floor is 8.** The evidence record
  supplies 7 sources with a resolvable or honestly reconstructable URL:
  Ginsberg 2009, Cook 2011, Lazer 2014, Copeland et al. 2013, the Google
  2015 shutdown post, Yang/Santillana/Kou (ARGO) 2015, and Declan Butler's
  Nature News piece (cited only for its confirmed title/date, since its
  substantive numbers were never read past the paywall). An 8th candidate
  source in the record, Bryan Walsh's Time piece (13 March 2014), was read
  in full by the researcher but the evidence record captures no URL for it
  at all — no domain, no path fragment, nothing to clean up or reconstruct.
  Per the brief's instruction to never invent a URL, I dropped it rather
  than guess one, and the piece does not depend on its one exclusive
  contribution (a Dewey-beats-Truman quote from Lazer) for any claim the
  argument needs. Primary count is 6 (Ginsberg, Cook, Lazer, Copeland,
  Google's shutdown post, ARGO), secondary count is 1 (Butler); both clear
  the commission's per-kind floors (primary >=4, secondary >=1) even though
  the raw total sits one below the series floor of 8.

All reconstructed URLs (the two static.googleusercontent.com PDFs, the PLOS
DOI-based link, the sciencemag.org/content path built from the
supplementary-materials path the evidence record gives, research.google's
blog post, arxiv, and nature.com/articles/494155a) were independently
curl-verified to return 200 or, for the Science mirror, a 403 that the
engine's own link checker (`engine/nb/links.py`) treats as non-blocking
(only 404/410/DNS failure count as dead).

Word count 2199 (band 1200-2200), 7 sources, reading_minutes 10 — all
measured via the engine's own `Article` parser and written into `nb-meta`
and the byline as the actual counted values, not estimates.

## Editorial requests addressed
None — this is the first draft (invocation 01), no prior editorial-review.md
exists yet.

## Remaining evidence or voice questions
None outstanding. The evidence record's own note that the closing "where
this lives today" turn is the writer's connective work, not a new sourcing
obligation, was followed: that section cites source 4 (Lazer) for the
general failure-mode claim it extends, and names three concrete systems
(recommender systems, fraud/predictive-policing scores, and — reusing the
already-linked knowledge-cutoff concept rather than re-linking it — large
language models) without asserting any new fact requiring its own citation.

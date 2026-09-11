# writer brief: the-mechanics/hallucinated-packages (01)

Inputs:
- editorial-direction.md (house standard, slop/headline rules, press voice, lesson identity, The Mechanics prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; read before drafting)
- researcher/01/evidence.md (the complete claim set; use its Numbers section exactly; address its Contradictions)
- commission.md (the assignment, boundaries, and the original-contribution target)
- the initialized article at library/the-mechanics/hallucinated-packages.html (edit in place; keep chrome exact)
- effective template contract and furniture catalogs under .nb-context/

Output: writer/01/draft-handoff.md (the article itself is the HTML above)

Proof (run from /home/user/the-nightly-build):
  ./nb stamp .nb-work/the-mechanics/hallucinated-packages/library/the-mechanics/hallucinated-packages.html
  ./nb check --series the-mechanics --library /home/user/library-checkout .nb-work/the-mechanics/hallucinated-packages/library/the-mechanics/hallucinated-packages.html
(iterate with --no-check-links; final proof with links, to BLOCK: 0)

This round's focus (from the researcher's report; the evidence file has the detail):
- Lead with the repeatability mechanism, not the headline rate. The "~20%" figure is an
  average dominated by older open-source models and is falling (frontier models ~4.6-6.1%
  in 2026 work); present rates honestly as era- and model-dependent. The load-bearing,
  durable finding is that the same invented name recurs across runs (58% recur across
  runs, 43% in all ten; and cross-model names persist into 2026).
- The threat is demonstrated-plausible, not realized: no malicious slopsquatting attack is
  documented in the wild as of the sources; the one real upload was a harmless researcher
  proof of concept. Say so plainly; do not imply a live epidemic.
- Attribute "slopsquatting" as the evidence supports (security-firm/press coinage), not to a
  named person's own post unless the evidence record confirms it.
- Mark settled vs open: the recurrence is established empirically; the token-level "why this
  exact name is a stable attractor" is synthesis resting on the hallucination lesson, not a
  proven mechanism. Keep that line honest.
- Link, do not re-teach: the-mechanics/hallucination (base mechanism), /tool-use, /retrieval.
  Spend the lesson on what hallucination did not cover: repeatability + the supply-chain risk.
- No reproducible attack recipe and no live malicious package name presented as installable.

Recent library shapes to break (habits, not rules; keep required content):
- Dek: avoid the two-clause "claim, and/so the twist" mold, the comma-triad, and the
  "The [thing] that..." opener.
- Closing body heading: recent mechanics pieces end on a terse limit/verdict heading
  ("A self-report is no proof of who built it"). Vary the build of your where-it-lives /
  what-fixes-it heading.
- Orientation heading is its own concrete step, not a paraphrase of the headline.
- Furniture: nb-note and nb-table recur by reflex. A table of rates by ecosystem/model may be
  genuine; an nb-note is not owed. Earn each.

nb-meta: set harness to "claude-code" and model to the model you are actually running as
(report it). No charts or source assets unless the evidence record names an exact visual the
argument spends.

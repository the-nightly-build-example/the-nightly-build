# Draft handoff: when-ai-breaks/cnet-ai-articles (01)

## Original-work sentence

The article turns the evidence record's separate facts into one taught
argument: it uses the verified $10,000-at-3-percent error as the worked example
that shows why next-word prediction produces prose exactly as fluent when it is
wrong as when it is right, and it separates this failure (a publisher passing AI
copy off as its own vetted editorial) from the chatbot-answering-a-user failures
the reader already associates with AI.

## Proof result

`./nb check .nb-work/when-ai-breaks/cnet-ai-articles/library/when-ai-breaks/cnet-ai-articles.html --series when-ai-breaks`
(links included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE.

No warnings left standing. The one W-SENTENCE-DENSITY warning in the first pass
(the Kalai sentence) was fixed by splitting it into three sentences, not
suppressed.

The proof prints one note: "library state not provided (--library); open-mode
dedupe and commission checks skipped." This is expected in local mode from this
checkout; the PR/CI proof runs those against the library branch.

## Open questions for the editor / orchestrator

- **Two internal cross-links could not be verified from this checkout.** The
  Background band and the mechanism section link
  `../the-mechanics/hallucination.html` (named in the brief) and
  `../when-ai-breaks/air-canada-chatbot.html` (named in the commission as a
  published neighbor to differentiate from). The proof does not probe internal
  library cross-links, and the published library is on the `library` branch,
  which is not checked out here (and git was out of scope for this role). Please
  confirm both slugs exist and resolve on the published library; if the
  arithmetic/confidence lesson the brief mentions has a stable slug, it could
  replace or join the hallucination Background row.

- **Two Futurism source titles are descriptive, not verbatim.** The evidence
  record gave URLs and authors but not exact headlines for
  `futurism.com/the-byte/cnet-publishing-articles-by-ai` and
  `futurism.com/cnet-ai-errors` / `cnet-ai-plagiarism`. I used faithful,
  content-accurate titles; the URLs (which the link check verified) are the
  load-bearing part. Swap to the exact published headlines if the editor has
  them.

- The Washington Post "Go deeper" row is access-gated (returns 403) and is
  offered as further reading, not cited as a claim, consistent with the evidence
  record noting its body could not be read.

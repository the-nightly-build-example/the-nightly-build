# Editorial review: what-could-go-wrong/ai-moral-status (editor/02)

Second read of a revision. This is the focused re-check the brief scopes: confirm
the single publication-blocking item from editor/01 — the source 6 (Birch, gaming
problem) sourcing block — is resolved, and that the revision broke nothing new. I
did not re-litigate the argument, the evenhandedness, the company-as-authority
handling, the other seven citations, or the prose; editor/01 confirmed those and
the brief instructs me not to reopen them.

## Skeptic

The one routed break in editor/01 was that s6 cited Birch's *The Edge of
Sentience* — a source no one had opened — for the gaming problem, with the s6
href landing only on an OUP marketing product page rather than the chapter that
owns the claim. Two things had to become true for that to resolve: the concept
had to be read firsthand from Birch's own chapter, and the printed href had to
land on that chapter.

Both hold now.

- **The href resolves to the chapter itself.** I opened the s6 href exactly as
  printed, `https://doi.org/10.1093/9780191966729.003.0017`. It returns a 302 to
  `https://academic.oup.com/book/57949/chapter/475705460` — a chapter-scoped
  Oxford Academic URL (chapter 16, per the DOI's `.003.0017` suffix), inside *The
  Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI*
  (Oxford University Press), which the page confirms. This is the canonical
  chapter DOI, not the old `global.oup.com/academic/product/...` marketing page.
  The chapter's running body text is behind Oxford Academic's Cloudflare
  bot-verification wall to automated fetch — the exact limitation the evidence
  record's CAUTION documents — but the link lands a human reader on the chapter,
  which is what editor/01 required. The endpoint is the source itself, not a
  proxy that merely returns the text.

- **The citation is concept-only, matching what was read firsthand.** The lone
  [6] marker attaches to one clause — "Birch calls it the gaming problem." The
  sentences that unpack it ("a language model has read most of what people have
  written... produce the words, and the behavior, of a suffering thing because it
  learned the pattern from us, not because it feels") state the gaming-problem
  concept the chapter's own published abstract establishes, which the researcher
  read verbatim from the Crossref chapter-DOI record. There is no direct Birch
  quotation anywhere in the piece, and no page-specific body passage is
  attributed to him. The remedy the abstract also carries (deep computational
  markers over behavioral ones) is not over-claimed in the prose. So the
  concept-level citation is fully covered by what was read firsthand, and nothing
  reaches past the abstract wording — consistent with the record's instruction
  not to attribute any body-specific quote to Birch.

- **The whole-book further-reading row is correctly left alone.** The unnumbered
  "Go deeper" row still points at the OUP product page for the book "at book
  length." That is appropriate: it references the entire book, not the single
  chapter s6 cites, so the chapter-DOI fix does not force a change there.

The source count stays at 8 with no recitation, which was the honest outcome
editor/01 asked for. The 8-source floor holds legitimately.

**One new break, introduced this round, fixed directly.** Editing the s6 href
mangled the entry's closing anchor tag: it read `</` + newline + `>` instead of
`</a>`, unlike every other source in the list. A malformed close leaves the
anchor element un-terminated in the parser — a syntactic break in furniture
markup, which is mine to repair. Fixed directly to `</a>`, matching s1–s5, s7,
s8. This was the only regression the URL change introduced; the prose and
claim-set are otherwise byte-for-byte the editor/01-approved text, including the
two direct edits I made last round (both intact and verified in place).

## Cut

No new prose entered this round — the writer changed only the s6 href — so there
was no fresh slop surface to walk, and re-running the full cut pass would
re-litigate settled work the brief forbids. Zero sentences failed on this read.
The one change I made is a markup correction, not a prose change: it removes no
fact, claim, or reasoning step and alters no wording.

## Reader

Unchanged from editor/01 and re-confirmed against the fix: the piece still gives
the reader a way to locate which kind of claim "the AI said it was suffering" is
— a demonstrated behavior or an unfalsified analogy — and to see that the field's
loudest proponent and its sharpest skeptic argue over which error to fear, not
over what today's systems have been shown to do. The Birch citation now rests on
a source read firsthand and a link that lands on it, so the one seam that made
the eighth source dishonest is closed. The prose still sits closer to the
voice-guide exemplars than to a median summary; nothing in the URL change touched
that.

## Edits

- Fixed the malformed closing tag on source 6 in the sources list: `</` (an
  un-terminated close) corrected to `</a>`, matching every other source entry.

## Required work

None. The single publication-blocking item from editor/01 is resolved, and the
one regression the revision introduced was a markup break within my authority,
which I fixed directly. No item outstanding for researcher, writer, or
orchestrator.

## Decision

approve — the s6 citation now reads firsthand from Birch's own chapter abstract
and its printed href resolves to that chapter (not the marketing page), so the
8-source floor holds honestly; the lone new break, a mangled `</a>` closing tag,
is fixed directly, and nothing else in the piece changed.

# Draft handoff: the-instruments/mmmu (writer, round 01)

## Original-work sentence

The article isolates the image as a single variable across the evidence's
scattered figures: it turns GPT-4's image-off/image-on pair, the four makers'
own headline scores, and the MMMU-Pro table into one worked reading that
quantifies, model by model, how many headline points survive when the picture
is forced, and separates that vision gap from the distinct protocol-mixing gap
the same numbers carry. (Visible in the "34.9%" section's one-variable
comparison, the per-model chart, and the Maj@32-vs-pass@1 paragraph.)

## Proof result

`./nb stamp` then `./nb check ... --series the-instruments --library
/home/user/library-checkout` (links included): **BLOCK: 0, WARN: 0,
PUBLISHABLE.** No warning intentionally left. Stamped words=1905,
reading_minutes=8, sources=8 (7 primary, 1 secondary; series floor is >=8 total,
>=4 primary, >=1 secondary). One chart built via `nb chart`
(`mmmu/chart-1.py` -> `chart-1.png`), MMMU-Pro Table 1, protocol constant across
every bar. No source asset captured; the text-answerable worked example is
taught in prose rather than as a captured figure.

## Boundaries held

- "Meaningful share is text-answerable," not "most of the score is text": the
  vision-blind section states vision adds ~22 points on top of the ~35% text
  ceiling and that the majority of a 68% score is not text.
- The MMMU authors' defense (OCR/captions do not lift text-only models; MMMU
  "necessitates deeper joint interpretation") is reported fairly in the
  builders'-defense note and the paragraph after it.
- The "% answerable without the image" is attributed as triangulated (MMMU
  baseline + MMStar's direct 42.9% / 43.6%), not as one reported figure.
- Protocol mixing (Gemini Ultra Maj@32 62.4% vs GPT-4V pass@1 56.8%) is named as
  a protocol difference, not a capability gap. The chart uses one table so every
  bar shares a protocol.

## Open questions for the orchestrator/editor

- GPT-4o's 69.1% is OpenAI-owned but was bot-blocked on OpenAI's own page (per
  the evidence record). I cited it only where I actually read it (MMMU-Pro
  Table 1, source 6) and worded orientation as "listed at 69.1% in the follow-up
  study's results table," not as a claim read on OpenAI's page. Flagging in case
  the editor wants a cleaner OpenAI primary or different wording.
- Headline "answers a third of MMMU" rounds the 34.9% text-only validation
  figure (MMMU Table 2) to "a third"; the body carries the exact 34.9%. Confirm
  the rounding reads honestly for display text.

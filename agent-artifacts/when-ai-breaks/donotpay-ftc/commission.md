# Commission: when-ai-breaks/donotpay-ftc

## The incident

DoNotPay, marketed for years as "the world's first robot lawyer," sold
consumers AI-generated legal help: letters, contested parking tickets, and
document generation, and in 2023 promoted an AI that would feed a defendant
arguments through an earpiece in a live courtroom (dropped after bar-association
and unauthorized-practice-of-law warnings). In September 2024 the US Federal
Trade Commission named DoNotPay in its "Operation AI Comply" sweep; the
finalized order required the company to pay and to warn customers, on findings
that it never tested whether its service performed like a human lawyer and made
claims it could not back.

## Why this lesson, now

The course has taught why a language model produces fluent, confident text with
no guarantee it is correct (the-mechanics/hallucination), and has one incident
where AI-invented case law reached a court (when-ai-breaks/mata-v-avianca). It
has not taught the failure one step upstream: a product sold as competent legal
work on the strength of that fluency, and the regulator that treated the gap
between the marketing and the tested reality as the harm. This is the shape of
the wider "AI-washing" the reader now meets on every product page.

## The angle to test

Tell it in order, with names and dates: what DoNotPay was built and sold to do,
what it actually did (documents not reviewed by a lawyer, the abandoned
in-court stunt), who it affected (paying subscribers), and what the operator did
(settled with the FTC, the amount and the terms). Then explain why that kind of
system fails that way, using what the course taught: an LLM generates
legal-sounding prose whose fluency is not evidence of legal correctness, and
DoNotPay, per the FTC, never measured its output against a lawyer's, so a
confident wrong answer looked exactly like a right one. Close on where the same
weakness lives now: the FTC's broader Operation AI Comply actions and the
pattern of selling capability that was never tested.

The researcher must work from the record: the FTC's complaint, proposed/finalized
order, and press release; DoNotPay's own marketing claims as quoted in the
filings; and contemporaneous reporting for context. Verify the settlement amount
and terms, the exact FTC findings (what was unsubstantiated), the dates, and the
in-court-AI episode from primary accounts. Where a claim is the FTC's allegation
rather than an admitted fact, mark it as such; note DoNotPay's response if the
record carries one.

## Boundaries

Do not re-teach why models hallucinate or how retrieval works; link hallucination
and mata-v-avianca in Background. Keep the piece on DoNotPay and the tested-versus-
marketed gap, distinct from mata-v-avianca (a lawyer's court filing) and
air-canada-chatbot (a company bound by its bot's promise). This is one of five
lessons tonight; no overlap with a fine-tuning paper, an embedding benchmark,
format-constrained decoding, or an AI-safety argument.

## Source policy

Series floor: 8 sources, at least 4 primary and at least 1 secondary. The FTC
complaint, order, and release, and DoNotPay's own quoted claims, are primary to
their own facts. Reporting is secondary for context. Meet the floor with sources
that carry the argument, not padding.

## Production

Profile balanced; no stage required. This run: writing-coach and researcher on
the strong model, researcher at high effort; writer at medium effort; editor at
high effort.

## Recent habits not to inherit

- The two-clause "and/but" dek is the current house default; build the dek
  another way and avoid the three banned molds in `spec/headlines.md`.
- The desk opens many pieces on a single named victim and closes on a "Where the
  same pattern lives today" section. The present-day close is series-required;
  vary its phrasing and heading, and do not force a single-victim cold open where
  the spine here is a regulator's finding about a product.

# researcher brief: when-ai-breaks/chatgpt-data-leak (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the subject, angle, required contribution, and source floor
Output: ./evidence.md

This round's focus, from the commission: nail the timeline and scope from the
primaries, and source the mechanism. Establish (1) exactly what was exposed
(chat titles/first messages; the payment-data subset and which fields) and to
whom, with dates, from OpenAI's postmortem and any security note; (2) the
technical cause from the postmortem and the open-source client library's own bug
report and fix — enough to explain the cancelled-request / pooled-connection
mechanism accurately; (3) what the Garante ordered, on what dates, and on what
grounds, quoted from the order itself, plus any later decision. Record where
OpenAI's public account developed or where scope figures differ across sources,
and note it in Contradictions. A partial-payment-data claim or a user count must
come from the party in a position to know.

Run-environment note: outbound HTTPS is proxied; OpenAI's blog, GitHub, and the
Garante's site are reachable. The Garante order may be in Italian — record its
canonical page and translate the quoted passage faithfully, noting it is a
translation. A 403 or paywall is gated, not dead.

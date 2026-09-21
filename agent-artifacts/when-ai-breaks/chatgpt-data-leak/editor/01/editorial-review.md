# Editorial review: when-ai-breaks/chatgpt-data-leak (editor/01)

## Skeptic

Thesis: the March 2023 ChatGPT exposure was ordinary web plumbing, not the
model. A cancelled request left a pooled connection holding one user's reply and
the next request read it as its own; and Italy's Garante acted on grounds of its
own, with the later fine annulled. The piece stands on four claims.

Claim 1 — the mechanism (cancelled request + pooled connection returns another
request's data). Held. OpenAI's postmortem owns it and the redis-py issue #2624
corroborates it from the library side. I opened #2624: title "Off by 1," opened
by drago-balto on 17 March 2023, and the quoted line ("the following redis
operation on the same connection will send the command, and then promptly
continue to read the response from the previous, canceled command") is verbatim.
PR #2641 (merged 22 March, shielding) and issue #2665 (25 March, shielding
covered pipelines only) both resolve and match the article's account of an
incomplete first fix. The postmortem page (s1) returns 403 to an automated
fetch, which the brief and evidence record predicted; the researcher verified it
resolves for a human, so I did not treat the interstitial as a failure. The
postmortem's two quoted passages match the evidence record's transcription word
for word.

Claim 2 — the exposed-data scope. Held and precise. Chat titles to some users;
payment information for at most 1.2% of ChatGPT Plus subscribers active in the
nine-hour window (1 a.m.–10 a.m. Pacific); fields differ by vector
(confirmation-email vector carries card type and last four digits, the account
page adds name, email, payment address, and expiration date); full card numbers
never exposed. The article correctly frames 1.2% as a ceiling on potential
visibility, not a count, and carries OpenAI's separate statement that the number
actually seen was extremely low. The record's four cautions (four-day scope
growth, the 1.2% ceiling, fields-by-vector, incomplete first fix) are all
honored.

Claim 3 — the two commission corrections. Both held; I verified each against the
Garante primaries directly (curl reached each page at HTTP 200 with full body;
WebFetch hit a transient 503). The 30 March 2023 order (doc-web 9870832) sets out
its grounds as RILEVATO/RITENUTO: no information notice, no adequate legal basis
for mass collection to train ("assenza di idonea base giuridica in relazione
alla raccolta dei dati personali"), inaccurate outputs, and no age verification
for a service reserved to those 13+. The strings "data breach," "perdita di
dati," and "20 marzo" appear nowhere in the order — the breach is not a ground,
exactly as the article states. The breach enters as context in the 31 March
press release (9870847): "A data breach affecting ChatGPT users' conversations
and information on payments by subscribers to the service" — the article quotes
this verbatim from the Garante's own English. The 20 December 2024 release
(10085432) carries the €15M fine, the failure-to-notify finding, and the
asterisked annulment note: judgment No. 4153/2026 of the Court of Rome, published
18 March 2026, upheld OpenAI's appeal and the decision was removed from the site.
The article's "That fine no longer stands" is accurate as of 2026-09-21.

Claim 4 — the same pattern lives in ordinary cached services. Earned analysis
built from the mechanism, not an unsupported leap; the article names concrete
kinds of service (chat window, inbox, bank account, checkout) as the voice guide
directs.

Display text, descriptor by descriptor. One label was wrong and I fixed it. The
headline read "showed ChatGPT users other people's chats." The record supports
chat *titles* in the sidebar (plus, narrowly, the first message of a new
conversation) — not readable conversations. "Chats" in the largest type on the
page tells a scanning reader that conversations were exposed, which overstates
the scope the body itself claims. I retitled to "...other people's chat titles,"
which matches the body, the orientation heading ("A stranger's chat titles in
your sidebar"), and the eyebrow, and updated the `<title>` and `nb-meta.title` to
match. The dek is accurate and untouched: "card details" fairly covers card
type, last four digits, and expiration date, and the body states full numbers
were never exposed. Dates, the 1.2% figure, the nine-hour window, and every
named actor (OpenAI, Sam Altman as chief executive, the Garante, the Court of
Rome, drago-balto as the outside reporter) check out against their owning
primaries.

`data-nb-kind` audit. All ten correct: s1 (OpenAI postmortem), s2–s4 (redis-py
issue/PR/issue), s6/s8/s9/s10 (Garante order and press releases) are primary —
each owns its claim; s5 (BleepingComputer) and s7 (TechCrunch) are secondary
reporting from outside the authoring party. No label hides a missing independent
source. Composition is 8 primary / 2 secondary against a floor of 8 / 4 / 1.

Citations opened. Every href resolves to the source itself: s2/s3/s4 to the named
GitHub issue/PR, s5 to the BleepingComputer report (Lawrence Abrams, 24 March
2023, with the Altman quote), s6/s8/s9/s10 to the correct Garante documents, and
the two bookend links to Luu's cache-incidents piece and Orosz's outage piece.
s1's interstitial is the documented exception.

## Cut

Sentence-by-sentence and edge passes: the prose is clean and mechanism-first,
close to the voice-guide register. Few sentences failed the slop test. The
apparent negative-parallelism edges ("Neither problem was in the model... Both
were in the layer that stores them"; "That 1.2% is a ceiling, not a count"; "Much
of the coverage said the regulator acted over the breach. The order's own text
does not") each correct a real, named misconception and carry a reasoning step,
so they stay — these are the article's earned contrasts, not invented straw men.

One repetition failed the test. The shared-caches close restated the mechanism
generalization in generic terms ("The pattern behind 20 March, a per-user cache
reached through pooled, cancellable connections, sits behind the ordinary
services a reader signs into every day") — it duplicated the named-services
sentence in the same section's first paragraph and repeated the takeaway's
distinctive phrase verbatim, while reaching for the generic ("ordinary
services") where the piece had already named the services. I cut it. The section
now closes on the thesis line the argument built to ("None of it needs a model to
hand one person another's data"), which the delete test keeps.

I split the 49-word / 2-join grounds sentence into two, which the proof's
warning invited and which reads clearer; all four grounds and their wording are
preserved. The remaining W-SENTENCE-DENSITY warning (43 words) wraps the verbatim
redis-py #2624 quotation and cannot be altered — I left it for the orchestrator's
re-stamp.

No prompt leakage: the commission's framings ("web service first," "regulators
treat these as data-protection events") appear only as the article's own
reworded, sourced conclusions, not as lifted clauses. No banned-term, caps-run,
or self-reference failure. The bookends address the reader as the lesson template
allows, and each sentence there says something specific to this lesson. Headline,
dek, and headings do not match the recent When AI Breaks build (figure-headline →
score-and-cutoff → who-it-hit → where-it-runs); this piece leads on the
cancelled-request surprise and closes on the plumbing, not a dollar-figure dek or
a "where it runs after the pause" line.

Furniture. The two nb-note quotations earn their place: one gives OpenAI's own
words for the bug, the other its own words for the payment-field scope — both are
the operator speaking on the two facts a reader would most want from the source
directly. The nb-timeline earns its place too: it carries the 28 April
reinstatement measures the prose does not spell out and gives a scannable spine
for a confusing three-year regulatory arc. I removed the redundant "Go deeper"
row that pointed back to redis-py issue #2624, which is already source 2 — a
further-reading pointer to an already-cited source adds nothing; the Orosz row
remains as genuine onward reading.

## Reader

What the piece gives beyond its sources: a reader who has read only this article
can explain why connection pooling plus request cancellation is a general
cross-user leak pattern in any cached web service, and can separate what the
Garante actually ordered (training legal basis, transparency, accuracy, age) from
the widely-repeated claim that the breach grounded the block — and knows the fine
was annulled. No single source hands you both the taught mechanism and the
disentangled regulatory record; the article synthesizes ten. The writer's
original-work sentence claims exactly these two moves, and both survive the read.
The prose sits closer to the voice-guide exemplars than to a median summary: the
causal chain is written out step to step in the sentences, and the services are
named as kinds (inbox, bank account, checkout) rather than folded into a
category. The headline, now "A cancelled request showed ChatGPT users other
people's chat titles," is a claim the piece defends.

## Edits

- Headline: "...other people's chats" → "...other people's chat titles"
  (`<h1>`), to match the body's sourced scope; a scanning reader took "chats" as
  readable conversations.
- `<title>` element: same change, for consistency with the headline.
- `nb-meta` "title": same change, for consistency with the headline.
- Mechanism prose: "holds outgoing commands in one queue and incoming replies in
  another" → "holds commands it sends in one queue and replies it receives in
  another," so the prose's queue description does not clash with the inverse
  "incoming/outgoing" labels in the verbatim OpenAI quote that immediately
  follows.
- Italy-block grounds sentence: split the 49-word sentence into two ("...to train
  the model. It processed inaccurate data because..."), clearing the density
  warning while keeping all four grounds and their wording.
- Shared-caches: cut the redundant generic restatement sentence ("The pattern
  behind 20 March... signs into every day"), which duplicated the section's own
  named-services sentence and the takeaway's phrasing.
- Shared-caches: added a citation to source 9 alongside source 6 on "a regulator
  will treat a leak from it as a data-protection event," so the leak-as-DP-event
  claim is anchored to the failure-to-notify finding that owns it, not only to
  the order that did not rest on the breach.
- Go deeper bookend: removed the redis-py issue #2624 row, redundant with
  source 2.

## Required work

None blocking. For the orchestrator's re-stamp: one W-SENTENCE-DENSITY warning
remains by necessity (the 43-word sentence wraps the verbatim redis-py #2624
quotation and must not be altered); word count and reading time will have shifted
slightly with the cuts and should be recomputed. The links proof passes as run;
source 1's automated-fetch interstitial is the documented exception the brief
named.

## Decision

Approve — the two commission corrections and the exposed-data scope are accurate
against the primaries, the one wrong display label is fixed, and the proof
verdict is PUBLISHABLE with only the unavoidable quotation-density warning
remaining.

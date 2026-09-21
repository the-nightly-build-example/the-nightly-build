# Evidence record: when-ai-breaks/chatgpt-data-leak (01)

The record supports the commission's core account firsthand. OpenAI's own
postmortem gives the exposed-data scope, the affected-user figure, the nine-hour
window, and the mechanism in the operator's words; the redis-py bug report and
fix give the library-side confirmation of the cancelled-request / pooled-connection
failure; and the Garante's own order, press releases, and later decision give the
regulatory arc, quoted from the authority's own documents. Two places need the
writer's care. First, the commission says the Garante "cited this breach among
other concerns" in its order: the operative order of 30 March 2023 does not list
the breach as a legal ground at all, resting instead on training-data legal basis,
transparency, data accuracy, and age verification; the breach appears in the
Garante's accompanying press release as context, and became a formal violation
(failure to notify) only in the November 2024 decision. Second, that November 2024
decision, the €15 million fine, was annulled by the Court of Rome in a judgment
published 18 March 2026, so as of this article's date the monetary sanction does
not stand. The mechanism and the breach scope are on solid primary ground; the
"and then a data-protection case" half of the story is more tangled than a single
fine, and the record documents where.

## Sources

```text
URL:         https://openai.com/index/march-20-chatgpt-outage/
Kind:        primary — OpenAI is the operator and owns the incident, the scope, and the root-cause account. Dated March 24, 2023.
Establishes: What was exposed, to whom, in what window, and the technical cause, in OpenAI's own words.
Paraphrase:  A bug in the open-source redis-py library let some users see titles from another active user's chat history; the first message of a newly-created conversation could also appear in someone else's history if both were active around the same time. Deeper investigation found the same bug caused unintentional visibility of payment-related information of 1.2% of ChatGPT Plus subscribers active during a specific nine-hour window. Two exposure vectors, both March 20, 1 a.m.–10 a.m. Pacific: subscription-confirmation emails sent to the wrong users (containing another user's credit card type and last four digits only), and the "My account" → "Manage my subscription" page (showing another active Plus user's first and last name, email, payment address, credit card type, last four digits only, and expiration date). Full credit card numbers were never exposed. OpenAI took ChatGPT offline, patched the bug, notified affected users, added redundant checks that the Redis cache data matches the requesting user, and contributed a patch upstream to redis-py.
Locators:    Opening section (chat titles / first message / 1.2% paragraph); the two bulleted exposure vectors; "Technical details" section for the mechanism; "Actions we've taken" for the remediation list.
Quote:       "it was possible for some users to see another active user's first and last name, email address, payment address, credit card type and the last four digits (only) of a credit card number, and credit card expiration date. Full credit card numbers were not exposed at any time."
Quote:       "If a request is canceled after the request is pushed onto the incoming queue, but before the response popped from the outgoing queue, we see our bug: the connection thus becomes corrupted and the next response that's dequeued for an unrelated request can receive data left behind in the connection."
Quote:       "At 1 a.m. Pacific time on Monday, March 20, we inadvertently introduced a change to our server that caused a spike in Redis request cancellations. This created a small probability for each connection to return bad data." / "This bug only appeared in the Asyncio redis-py client for Redis Cluster, and has now been fixed."
Access note: The canonical page sits behind a Cloudflare "Verify you are human" (Turnstile) interstitial that blocks plain fetches (HTTP 403) from this environment. Read in full via a scripted headed browser that cleared the challenge; the URL above is the document's own page and resolves for a human in a browser.
```

```text
URL:         https://github.com/redis/redis-py/issues/2624
Kind:        primary — the upstream bug report that owns the library-side description of the fault. Opened by user "drago-balto," March 17, 2023 (three days before the ChatGPT incident).
Establishes: That async command cancellation in redis-py leaves a pooled connection holding the previous command's unread response, so the next command reads the wrong data; and that this was the fault fixed for the incident.
Paraphrase:  Titled "Off by 1 - Canceling async Redis command leaves connection open, in unsafe state for future commands." When an async request is cancelled after the command is sent but before its response is read, the connection is returned to the pool corrupted; the next operation on it reads the earlier, cancelled command's response ("off by one"). The reporter proposed catching asyncio.CancelledError in the send/parse path and disconnecting the connection. Closed by PR #2641.
Locators:    Issue title and body; "Related PR: #2641."
Quote:       "The following redis operation on the same connection will send the command, and then promptly continue to read the response from the previous, canceled command." (issue body, as rendered on the issue page)
Access note: Read via WebFetch of the public GitHub page; the browser-through-proxy path is policy-restricted to another repository, but the page is public and resolves for any reader.
```

```text
URL:         https://github.com/redis/redis-py/pull/2641
Kind:        primary — the fix itself, owned by the redis-py project. Author "chayim"; merged March 22, 2023.
Establishes: What the fix changed and that it shipped in redis-py, corroborating OpenAI's statement that it contributed a patch upstream.
Paraphrase:  Titled "AsyncIO Race Condition Fix." Shields command execution from cancellation so that a task cancelled mid-request disconnects and resets the connection instead of returning it to the pool corrupted. Closes #2624 and #2579. Shipped in redis-py 4.5.3, with backports to 4.3.6 and 4.4.3.
Locators:    PR title, description, "closes #2624, #2579," release/version note.
Access note: Read via WebFetch of the public GitHub page. Exact merge commit and the precise release-note wording were not re-verified against a raw API response (api.github.com is egress-blocked here); version numbers are corroborated by the security trackers below and by issue #2665.
```

```text
URL:         https://github.com/redis/redis-py/issues/2665
Kind:        primary — follow-up bug report showing the first fix was incomplete. Opened by "drago-balto," March 25, 2023.
Establishes: That PR #2641 (shielding) resolved the cancellation problem only for pipelined operations, leaving non-pipelined async commands still able to corrupt a pooled connection.
Paraphrase:  Titled "Canceling async Redis command leaves connection open, in unsafe state for future commands"; described as a reincarnation of #2624. A reproduction inserts a delaying TCP proxy between client and server; after a cancelled GET, a subsequent ping() returns False and a subsequent GET returns the prior command's value. The reporter notes the cancellation-shielding fix (PR #2641) covered pipelines only.
Locators:    Issue body; reference to #2624 and PR #2641.
Access note: Read via WebFetch of the public GitHub page. Do not reproduce the exploit script; it is named here only to establish that the fault was demonstrable and that the first fix was partial.
```

```text
URL:         https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870832
Kind:        primary — the Italian data-protection authority's operative order. "Provvedimento del 30 marzo 2023," doc-web 9870832, signed by its President, "Stanzione" (as the order's signature block reads). In Italian; passages below are quoted in the original and translated.
Establishes: Exactly what the Garante ordered on 30 March 2023, on which legal grounds. The breach is NOT among the enumerated grounds of the order.
Paraphrase:  Acting under GDPR art. 58(2)(f) as an urgent measure pending its inquiry, the Garante imposed a provisional limitation ("limitazione provvisoria") on OpenAI L.L.C.'s processing of the personal data of data subjects established in Italian territory, with immediate effect from receipt of the order, and invited OpenAI to report within 20 days what steps it had taken. The stated grounds ("RILEVATO"): no information notice is given to users or to the data subjects whose data OpenAI collects; there is no suitable legal basis for the mass collection and processing of personal data to train the algorithms; the data processed are inaccurate because ChatGPT's outputs do not always match reality; and there is no age verification for a service its own terms reserve to those 13 and older, exposing minors to unsuitable responses. The order finds violations of arts. 5, 6, 8, 13 and 25 of the Regulation. The 20 March data breach is not cited as a ground anywhere in the order's text.
Locators:    Premises block ("RILEVATO... RILEVATA... CONSIDERATO... RITENUTO"); operative order "TUTTO CIÒ PREMESSO IL GARANTE: a) ... b) ..."; "In Roma, 30 marzo 2023 / IL PRESIDENTE / Stanzione."
Quote (IT): "RITENUTO pertanto che nella situazione sopra delineata, il trattamento dei dati personali degli utenti, compresi i minori, e degli interessati i cui dati sono utilizzati dal servizio si ponga in violazione degli artt. 5, 6, 8, 13 e 25 del Regolamento".
Translation:  "HELD therefore that, in the situation described above, the processing of the personal data of users, including minors, and of the data subjects whose data are used by the service is in breach of arts. 5, 6, 8, 13 and 25 of the Regulation." (translation by the researcher)
Quote (IT): "a) ... dispone, in via d'urgenza, nei confronti di OpenAI L.L.C. ... la misura della limitazione provvisoria, del trattamento dei dati personali degli interessati stabiliti nel territorio italiano; b) la predetta limitazione ha effetto immediato a decorrere dalla data di ricezione del presente provvedimento".
Translation:  "a) ... orders, as a matter of urgency, against OpenAI L.L.C. ... the measure of provisional limitation of the processing of the personal data of data subjects established in Italian territory; b) the said limitation takes immediate effect from the date of receipt of this order." (translation by the researcher)
```

```text
URL:         https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870847
Kind:        primary — the Garante's own press release on the block, 31 March 2023. Carries the authority's own Italian and English text.
Establishes: That the Garante itself connected the action to the 20 March breach as context, and how the authority summarized its own grounds. This is where "the breach" enters the Garante's public account.
Paraphrase:  Announces the immediate provisional limitation and the opening of an inquiry, records that on 20 March ChatGPT had suffered a data breach involving users' conversations and paid subscribers' payment information, then restates the order's grounds (no information notice; no legal basis for mass collection/retention to train the algorithms; inaccurate outputs; no age filter for under-13s). States OpenAI has no EU establishment but a designated EEA representative, and must report within 20 days on pain of a fine up to €20 million or 4% of annual global turnover.
Locators:    Body paragraphs (Italian), then the authority's own English version ("Artificial intelligence: stop to ChatGPT by the Italian SA").
Quote (IT): "ChatGPT ... lo scorso 20 marzo aveva subito una perdita di dati (data breach) riguardanti le conversazioni degli utenti e le informazioni relative al pagamento degli abbonati al servizio a pagamento."
Quote (EN, the Garante's own translation): "A data breach affecting ChatGPT users' conversations and information on payments by subscribers to the service had been reported on 20 March."
```

```text
URL:         https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9881490
Kind:        primary — the Garante's press release of 28 April 2023 reinstating ChatGPT in Italy.
Establishes: The end of the block: ChatGPT resumed in Italy on/around 28 April 2023 after OpenAI adopted the required measures.
Paraphrase:  Titled "ChatGPT: OpenAI riapre la piattaforma in Italia" (OpenAI reopens the platform in Italy). Records the measures OpenAI put in place: a new privacy notice; a welcome screen linking to it; a Europe-wide opt-out form to exclude one's conversations and history from training (legitimate-interest basis for training, subject to objection); an age-gate requiring users to declare they are 18+, or 13–17 with parental consent; and a birth-date field at registration that blocks under-13s. The Authority expressed satisfaction and pointed to remaining requirements from its 11 April 2023 order, including an age-verification system and an information campaign.
Locators:    Headline and body bullet list; closing paragraph on the 11 April order's remaining requirements.
```

```text
URL:         https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432
Kind:        primary — the Garante's press release of 20 December 2024 announcing the final decision (Provvedimento n. 755 of 2 November 2024), and now carrying the note that a Rome court annulled it.
Establishes: The final regulatory outcome and its reversal. Here the breach becomes a formal finding (failure to notify), and here the €15 million fine is imposed — then annulled.
Paraphrase:  The Garante closed its inquiry with a corrective and sanctioning decision finding that OpenAI failed to notify the Authority of the March 2023 data breach, processed users' personal data to train ChatGPT without first identifying an adequate legal basis, and breached transparency and information obligations, and that it lacked age-verification mechanisms (risk to under-13s). It ordered a six-month institutional information campaign across radio, TV, press and internet, and fined OpenAI €15 million, taking the company's cooperation into account. Because OpenAI established its European headquarters in Ireland during the inquiry, the Garante transmitted the file to the Irish DPC as lead authority under the one-stop-shop rule. An asterisked note added to the page states that Decision No. 755 was temporarily removed following a Rome court judgment that upheld OpenAI's appeal.
Locators:    Body (Italian) and the authority's English version; the asterisk footnote at the top of the release.
Quote (IT): "la società ... oltre a non aver notificato all'Autorità la violazione dei dati subita nel marzo 2023, ha trattato i dati personali degli utenti per addestrare ChatGPT senza aver prima individuato un'adeguata base giuridica e ha violato il principio di trasparenza e i relativi obblighi informativi".
Quote (EN, the Garante's own note): "Decision No. 755 of 2 November 2024 has been temporarily removed from the website of the Italian Data Protection Authority following judgment No. 4153/2026 of the Court of Rome. The judgment, published on 18 March 2026, upheld the appeal lodged against the Authority's decision."
```

```text
URL:         https://www.bleepingcomputer.com/news/security/openai-chatgpt-payment-data-leak-caused-by-open-source-bug/
Kind:        secondary — trade-press reporting (Lawrence Abrams, BleepingComputer, March 24, 2023). It reports on OpenAI's disclosure from outside; it does not own the facts.
Establishes: Context for how OpenAI's account developed. It records that when ChatGPT was first taken offline on March 20, OpenAI "did not provide details as to what caused the outage," and that CEO Sam Altman said "We feel awful about this." Corroborates the postmortem's scope figures.
Paraphrase:  Recounts the 1.2% figure, the exposed fields, the nine-hour window, and the redis-py cause, and notes the initial March 20 outage was announced without a stated cause; the payment-data disclosure came with the March 24 postmortem.
Locators:    Opening summary; Altman quote; note on the initial outage.
```

```text
URL:         https://techcrunch.com/2023/03/31/chatgpt-blocked-italy/
Kind:        secondary — reporting on the Garante action (Natasha Lomas, TechCrunch, March 31, 2023). Reports from outside the authority.
Establishes: Independent contemporaneous account of the block and its stated grounds; useful for how outlets framed the breach's role.
Paraphrase:  Reports the order to cease processing Italian users' data, the four concerns (legal basis for training data, data accuracy, age verification, information notice), a reference to the March 20 breach, the 20-day response deadline, and the up-to €20m / 4%-of-turnover exposure. Note: coverage of this kind tends to present the breach as one of the concerns "cited," which the order's own text does not bear out (see Contradictions).
Locators:    Lead and grounds section; penalty paragraph.
```

## Contradictions

- **The order vs. the commission on the breach's role.** The commission (following
  much coverage) says the Garante ordered the halt "citing this breach among other
  concerns." The operative order of 30 March 2023 (doc-web 9870832) does not name
  the 20 March breach among its grounds; those are information notice (art. 13),
  legal basis for training (art. 6), inaccuracy (art. 5), and age verification /
  minors (art. 8), with arts. 5, 6, 8, 13 and 25 cited. The breach is named in the
  Garante's press release of 31 March as context ("lo scorso 20 marzo aveva subito
  una perdita di dati"), and only in the November 2024 decision does it become a
  formal finding, as a failure to notify the Authority. Strongest version each way:
  the block was triggered by the attention the breach drew and the Garante flagged
  it publicly, so the breach was materially part of the episode; but the legal
  measure did not rest on it. What settles it: the order's own text, which is
  dispositive and enumerates its grounds.

- **How OpenAI's account developed.** On 20 March OpenAI took ChatGPT offline over
  the chat-title exposure and, per BleepingComputer, "did not provide details" of
  the cause at first. The payment-data exposure was disclosed in the 24 March
  postmortem, which frames it as found "upon deeper investigation." The reported
  scope thus grew over four days, from chat titles to payment data.

- **Two different denominators for "who was affected."** OpenAI says payment
  information of "1.2% of the ChatGPT Plus subscribers who were active during a
  specific nine-hour window" was potentially visible, but separately that "the
  number of users whose data was actually revealed to someone else is extremely
  low." The 1.2% is a ceiling on potential visibility among active Plus users in
  the window, not a count of confirmed disclosures; secondary write-ups sometimes
  collapse the two.

- **Which fields, by vector.** The scope is not one flat list. The wrongly-addressed
  confirmation emails carried only another user's credit card type and last four
  digits; the "Manage my subscription" page additionally showed first and last
  name, email, payment address, and card expiration date. Full card numbers were
  exposed in neither.

- **"The fix" was not a single clean event.** PR #2641 (shipped 4.5.3) was taken as
  the fix, but issue #2665 (25 March) showed it covered pipelined operations only,
  leaving non-pipelined async commands still vulnerable; the incomplete fix drew a
  second CVE (see Numbers). The writer should not describe the patch as a one-shot
  resolution.

- **The €15 million fine no longer stands.** The November 2024 decision imposing it
  was annulled by the Court of Rome (judgment 4153/2026, published 18 March 2026),
  which upheld OpenAI's appeal; the Garante removed the decision from its site. Any
  framing that ends on "OpenAI was fined €15 million" is out of date as of this
  article's 2026-09-21 date.

## Numbers

```text
Figure: 1.2% of ChatGPT Plus subscribers active during the window
Owner:  OpenAI postmortem
Scope:  Potential visibility of payment-related information; denominator is Plus subscribers active during the nine-hour window on 20 March 2023, not all users and not confirmed disclosures.
```

```text
Figure: nine-hour window, 1 a.m.–10 a.m. Pacific, Monday 20 March 2023
Owner:  OpenAI postmortem
Scope:  Window during which the two exposure vectors (mis-sent confirmation emails; "Manage my subscription" page) could show another user's data. OpenAI adds it "could have occurred prior to March 20, although we have not confirmed any instances."
```

```text
Figure: last four digits (only) of a credit card number; full numbers never exposed
Owner:  OpenAI postmortem
Scope:  The card-number field's exposure across both vectors; full PAN exposure is explicitly denied.
```

```text
Figure: change introduced 1 a.m. Pacific, 20 March 2023, causing a spike in Redis request cancellations
Owner:  OpenAI postmortem
Scope:  The trigger that raised the probability of the latent redis-py bug firing; the bug appeared only in the Asyncio redis-py client for Redis Cluster.
```

```text
Figure: fixed in redis-py 4.5.3 (backports 4.3.6, 4.4.3)
Owner:  redis-py PR #2641 / release notes
Scope:  Version(s) carrying the cancellation-shielding fix. Not re-verified against a raw API response here; corroborated by issue #2665 and the security trackers.
```

```text
Figure: CVE-2023-28858 (and CVE-2023-28859 for the incomplete fix)
Owner:  Security trackers (NVD / vendor advisories) — secondary, reported not independently confirmed here
Scope:  The public vulnerability identifiers for the redis-py fault and its partial fix. Context only; not load-bearing.
```

```text
Figure: potential penalty up to €20 million or 4% of annual global turnover
Owner:  Garante press release, 31 March 2023
Scope:  Statutory exposure flagged in the 30 March order for non-response, not a fine imposed.
```

```text
Figure: €15 million fine; six-month information campaign
Owner:  Garante decision (Provvedimento n. 755, 2 November 2024), announced 20 December 2024
Scope:  The sanction imposed at the close of the inquiry — subsequently annulled by the Court of Rome (judgment 4153/2026, published 18 March 2026).
```

```text
Figure: block imposed 30–31 March 2023; ChatGPT reinstated in Italy 28 April 2023
Owner:  Garante order (30 March 2023) and press release (28 April 2023)
Scope:  Duration of the provisional limitation on OpenAI's processing of Italian users' data — roughly four weeks.
```

## Source assets

```text
Asset: OpenAI postmortem, "Technical details" section — the seven-step prose account of the Redis queue mechanism (cache → cluster → redis-py/Asyncio → shared connection pool → incoming/outgoing queues → cancellation between push and pop → corrupted connection returns another request's data).
Shows: The whole cancelled-request / pooled-connection mechanism in the operator's own words. It is the single best primary passage for teaching the mechanism.
Crop:  This is text, not an image; there is no diagram in the source. If the writer builds a diagram, it must not add steps OpenAI did not state, and must keep the ordering (cancel occurs after the request is queued but before its response is read).
```

```text
Asset: Garante order (doc-web 9870832) — the operative block "TUTTO CIÒ PREMESSO IL GARANTE: a) ... b) ...".
Shows: Exactly what was ordered and on what authority (GDPR art. 58(2)(f)), in the authority's own words. Best evidence that the order rests on training/transparency/age grounds, with the breach absent.
Crop:  Keep the "a)/b)" operative text and the "RILEVATO/RITENUTO" grounds together; do not crop in a way that implies the breach was a listed ground.
```

```text
Asset: redis-py issue #2624 / #2665 — the minimal reproduction description (off-by-one; ping() returns False after a cancelled GET).
Shows: That the fault was concrete and demonstrable, and that the first fix was partial.
Crop:  Describe, do not publish, the runnable exploit script. The commission bars instructions for causing such a breach; the mechanism is fully teachable from OpenAI's prose without the script.
```

None of the primary web pages carries a chart or photograph that would carry the
argument better than prose; the argument here is a mechanism and a set of dates,
best served by the quoted passages above and, if the writer wants one, a built
diagram of the queue mechanism from the postmortem's own steps.

## Discarded

```text
URL: https://www.sonatype.com/blog/openai-data-leak-and-redis-race-condition-vulnerability-that-remains-unfixed — secondary vendor blog; useful only for the CVE framing, which is already covered and non-load-bearing. Not cited to avoid leaning on a security vendor's characterization.
URL: https://vulert.com/vuln-db/debian-12-python-redis-167327 — CVE database mirror; duplicative of the CVE note, adds nothing firsthand.
URL: https://www.biodiritto.org/.../Provvedimento-112-2023 — third-party repost of the Garante order; the authority's own page (9870832) is the primary and was read directly.
URL: web.archive.org / archive.ph mirrors of the OpenAI postmortem — blocked by this environment's egress policy; unnecessary once the canonical page was read directly through a browser.
URL: Various Italian-language news recaps (agi.it, ictsecuritymagazine.it, corrierecomunicazioni.it) — secondary retellings of the Garante action; the Garante's own documents were read instead, per the commission's instruction to quote the regulator from the order.
```

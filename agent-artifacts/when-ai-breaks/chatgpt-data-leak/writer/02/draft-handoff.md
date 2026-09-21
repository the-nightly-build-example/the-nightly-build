# Draft handoff: when-ai-breaks/chatgpt-data-leak (02) — CI link-resolution repair

Scope of this invocation: link-resolution only. No prose, claim, structure,
heading, dek, source kind, or cited document changed. All four Garante sources
remain `data-nb-kind="primary"` (an archived copy of the authority's own page is
the same primary source) with their citation labels untouched. Only the four
`href` values were swapped; none of these sources carried a `data-nb-url`, so
nothing else was edited.

## The four address swaps (docweb ID → Wayback snapshot)

- **s6 · 9870832** (Provvedimento del 30 marzo 2023 — the operative order)
  `https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870832`
  → `https://web.archive.org/web/20241222150723/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870832`
- **s8 · 9870847** (press release, 31 March 2023 — stop to ChatGPT)
  → `https://web.archive.org/web/20260904190957/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870847`
- **s9 · 10085432** (press release, 20 December 2024 — final decision + Rome annulment note)
  → `https://web.archive.org/web/20260917130924/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432`
- **s10 · 9881490** (press release, 28 April 2023 — reopening in Italy)
  → `https://web.archive.org/web/20260831071752/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9881490`

I used the `https://` form of each snapshot (the brief listed three as `http://`).
Both resolve on the open internet; `https://` is what verifies cleanly here and
is the canonical replay form. Same timestamps as the brief for s8/s9/s10.

## docweb 9870832 — snapshot resolution

The brief said the availability API found no snapshot for 9870832 and asked me to
create one via web.archive.org/save. Save-Page-Now was down in this environment
throughout the attempt: every save (including a control save of example.com)
returned 5xx (502 "upstream request failed", then 523 Cloudflare origin-
unreachable), i.e. an SPN backend outage, not a Garante-specific bot block. So I
went back to the working replay endpoint, which found that a genuine capture of
9870832 already exists — `web/20241222150723/` (captured 22 Dec 2024). The
availability API had simply missed it. No new save was needed, and no other
document was substituted.

## Confirmation each snapshot shows the right document (opened in-browser)

- **9870832** — title "Provvedimento del 30 marzo 2023 [9870832] - Garante Privacy".
  Body carries the real order: "la misura della limitazione provvisoria del
  trattamento"; art. "58, par. 2, lett. f)"; the four grounds — no legal basis
  for training-data collection ("l'assenza di idonea base giuridica in relazione
  alla raccolta dei dati personali e al loro trattamento per scopo di
  addestramento degli algoritmi"), data inaccuracy ("il trattamento ... risulta
  inesatto in quanto le informazioni fornite da ChatGPT non sempre corrispondono
  al dato reale"), no age verification for under-13s ("l'assenza di filtri per i
  minori di età di 13 anni"), and the missing information notice; signature "In
  Roma, 30 marzo 2023 IL PRESIDENTE Stanzione", "Doc-Web 9870832". Not a bot/404.
- **9870847** — title "Intelligenza artificiale: il Garante blocca ChatGPT.
  Raccolta illecita di... - Garante Privacy" (the 31 March 2023 block release).
- **10085432** — title "COMUNICATO STAMPA - ChatGPT, il Garante privacy chiude
  l'istruttoria... - Garante Privacy"; body confirms "una sanzione di 15 milioni
  di euro" and the note that "il provvedimento n. 755 del 2 novembre 2024 è stato
  temporaneamente rimosso ... a seguito della sentenza del Tribunale di Roma n.
  4153/2026, pubbl. il 18/03/2026" — matching the article's fine and annulment.
- **9881490** — title "ChatGPT: OpenAI riapre la piattaforma in Italia
  garantendo più... - Garante Privacy" (the 28 April 2023 reopening release).

## Non-404 verification

Each replacement URL returns 200 both by browser navigation (above) and by a
direct curl probe (all four: HTTP 200). None returns 404/410, so CI's link
checker reaches a resolvable address. (Note: plain garanteprivacy.it is what CI
404s on for script clients; the Wayback replay copies do not.)

## Proof result

`./nb check .../when-ai-breaks/chatgpt-data-leak.html --series when-ai-breaks --repo /home/user/the-nightly-build`
(links included) — **BLOCK: 0**, verdict PUBLISHABLE. WARN: 1, the single
non-blocking `W-SENTENCE-DENSITY` (43 words, 2 clause joins) on the verbatim
quotation, left intentionally as expected. `nb stamp` reported the article
already stamped (words=1993, reading_minutes=9, sources=10) — link swaps changed
no counts.

Note on local vs CI: the local link checker reaches these Wayback URLs directly
(no garanteprivacy.it TLS timeout), so BLOCK: 0 here plus the confirmed non-404
status of each snapshot together evidence the CI 404s are resolved.

## Original-work sentence (carried from 01, unchanged)

The article turns a "ChatGPT broke" story into a lesson about ordinary web
plumbing — teaching the cancelled-request / pooled-connection fault as a general
cross-user leak pattern, not an AI-specific one — and separates what the Garante
actually ordered on 30 March 2023 from the widely-repeated claim that the breach
grounded the block.

## Open questions

None. This was a bounded link repair; content was already approved in round 01.

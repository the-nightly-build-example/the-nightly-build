# Draft handoff: what-could-go-wrong/treacherous-turn (01)

## Original work
The article builds an explicit three-condition test for what would count as a
real treacherous turn (a goal the system reached on its own, concealment aimed
at the test, and defection timed to the moment it works), then scores each 2024
experiment against that test to show which condition each one fails. The
evidence record lists the caveats separately; the article turns them into one
yardstick a reader can reuse, and that yardstick is visible in the
"What would count as the real thing" section and referenced through the audit
and the takeaway.

## Proof result
`./nb check ... --series what-could-go-wrong --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** `nb stamp` set
words=2198, reading_minutes=10, sources=8 (5 primary, 3 secondary; meets the
min-8 / >=4-primary / >=1-secondary policy). Preview site built without error
and renders the note and audit table.

No warning left standing.

## Sourcing decisions the editor should know
- **Yudkowsky (2008) dropped as a numbered source.** The evidence record could
  not capture a firsthand passage (the PDF returned as binary) and advised
  citing him only for provenance or dropping him. Provenance for the
  "you cannot read safety off behavior" concern is instead carried by Omohundro
  (2008), read from the author's abstract page, so every numbered source is one
  the record verified. If the editor wants Yudkowsky's name in for lineage, it
  needs a re-verified quote first.
- **Bostrom cited to the OUP product page**, not to either rendering URL, per the
  record's caution against presenting a book-rendering as Bostrom's own page.
  Page locators (p. 119 definition, p. 109 thesis, pp. 116-118 feigned safety)
  ride on the inline citations as `data-nb-locator`; no `data-nb-url` was added
  because there is no canonical per-page URL.
- **The one verbatim Bostrom quote in the note carries two em-dashes** (his
  punctuation, "—without warning or provocation—"). These are the only em-dashes
  in the piece; my own prose uses none, so the count is 2 of 4.

## Open question for the desk (not blocking)
The dek calls the three teams "the labs that ran them." Apollo Research is a
safety-evaluations organization rather than a frontier lab; the body states this
precisely ("a safety-evaluations group"). If the desk reads "labs" as too loose
for the newsstand line, the dek can say "the teams that ran them" with no other
change.

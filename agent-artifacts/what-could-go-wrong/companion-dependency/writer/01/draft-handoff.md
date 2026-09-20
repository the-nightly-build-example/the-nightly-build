# Writer draft handoff: what-could-go-wrong/companion-dependency (01)

## Original-work sentence

The article takes four evidentiary threads the researcher gathered separately
(Turkle's decade-old origin claim, the company-run RCT, the independent
Character.AI study, and the population-scale Common Sense Media survey) and
does something none of them individually does: it cross-reads them to show
they are measuring different slices of the same population (a small heavy-use
group versus the median user), which resolves the commission's "some benefit,
some harm" tension into a specific, falsifiable claim — that the two sides of
the public argument are each accurately describing a different group of
users, not disagreeing about the same one — rather than reporting the
tension as an open question or a symmetric hedge.

## Proof result

`./nb stamp` then
`./nb check .nb-work/what-could-go-wrong/companion-dependency/library/what-could-go-wrong/companion-dependency.html --series what-could-go-wrong --library .nb-work/library`
(links checked, network reachable): **BLOCK: 0**, verdict PUBLISHABLE.

Warnings intentionally left (4, all W-SENTENCE-DENSITY):
- One sentence in the "why this matters" bookend (46 words, 1 clause join).
- One sentence in the Replika/Kuyda paragraph (49 words, 2 clause joins).
- One sentence in the OpenAI/MIT study paragraph (40 words, 2 clause joins).
- One sentence in the population-data paragraph (52 words, 1 clause join).

Each carries one complete, necessary thought (a study's design plus its
headline finding, or a quote plus its context) that did not split cleanly
without either duplicating a clause or breaking a quotation across two
sentences. Word budget was also at the template's 2200-word ceiling
(landed at 2200 exactly after several rounds of trimming), which limited
how much connective tissue could be added for further splits. These read as
controlled, single-purpose-per-clause sentences rather than run-ons, per
`spec/editorial.md`'s "a long sentence under control is good writing."

## Evidence/voice notes

- Followed the evidence record's three flagged caveats exactly: no
  page-cited Turkle book quote beyond the Bill Moyers excerpt and TEDx
  transcript; the OpenAI/MIT studies are named with their producer and
  stake in the prose itself (never cited as neutral); the two independent
  wellbeing studies are cited via their arXiv preprint URLs, with De
  Freitas et al. explicitly flagged as abstract-only.
- Broke both named recent habits: the opener does not use a "By the end
  you will know" triad (opens on the Replika user's Reddit post instead),
  and the closing gap section is headed "The studies run for weeks; the
  worry is about years" rather than a "gap on both sides" mold, landing on
  this argument's specific state (which of two real, distinct user
  populations someone belongs to) rather than a symmetric hedge.
- character-ai-lawsuit, deskilling, and ai-persuasion are linked, not
  retold: character-ai-lawsuit inline in the regulatory-response section
  plus in the Background reading list; deskilling and ai-persuasion in the
  Background reading list only, as pure scope-boundary pointers.
- No open evidence gap: nothing in the brief's research request list was
  needed beyond what the evidence record supplied.

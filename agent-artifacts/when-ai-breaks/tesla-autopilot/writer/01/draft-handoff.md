# Draft handoff: when-ai-breaks/tesla-autopilot (01)

## Original work

The piece sets Tesla's own "the driver was warned" defense beside each crash's
logged final seconds — where no warning fired — and then shows that the December
2023 recall strengthened exactly those warning controls, so Tesla's remedy
conceded the driver-monitoring gap its statements had denied. That alignment of
three documents the evidence keeps separate (the NTSB's 2017 design finding, the
two crashes' final-seconds monitoring silence, and the recall's own defect
language) is the article's synthesis, and it is visible where the disputed-cause
section lands: "the controls it recalled were the controls that had let Brown and
Huang stop watching the road."

## Proof result

`./nb check … --series when-ai-breaks --library <library-checkout>` (links
included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** No warning left standing.

Stamp: 2199 words (band 1200–2200), 10 min read, 11 sources (8 primary,
3 secondary).

## Link-resolution decisions (per the brief's caveat)

Tesla removed both blog posts from its live site, so neither `tesla.com` href
would resolve.

- **"A Tragic Loss" (2016):** cited to an Internet Archive capture of Tesla's own
  page (`web.archive.org/web/20160722055534/…/blog/tragic-loss`), kept as
  **primary** — it is Tesla's own page, archived. Verified resolving via the
  Wayback availability API (status 200).
- **"An Update on Last Week's Accident" (2018):** not cited directly. Tesla's
  Mountain View account is carried by the **NBC News reproduction** (secondary,
  S6), which the evidence records as the confirming source and which resolves.

Both choices matched the label honesty the brief required, and the full
link-checked proof passed.

## Interpretation flagged for the editor

The brief said to set `model` to `claude-opus-4-8`, "matching the library's
convention." The published shelf (e.g. `the-mechanics/sycophancy.html`) writes
that field as **`Claude Opus 4.8`**. I used the shelf's form so the paper stays
consistent; `nb check` accepts it. If the pipeline expects the literal
`claude-opus-4-8`, this is the one field to change. `harness` is
`claude-code-routine`, which matches the shelf exactly.

## Furniture

One `nb-note` labeled "The defect, in Tesla's words" carries the recall's defect
sentence verbatim — the point the whole dispute turns on. Considered the NTSB
gore diagram (HAR-20/01 Fig. 2) as a source asset; the prose narrates that
mechanism concretely (Autosteer turning 5.6° into the gore where SR-85 splits),
so I left it to the prose rather than add a figure the argument did not need.

## Open questions

None blocking. The two prior AV lessons the brief mentions as a contrast are not
in the published library (`nb history` returns none; the checkout holds only
`the-mechanics`), so Background/Go-deeper rows point beyond the paper rather than
to sibling slugs I cannot resolve. If those lessons publish, a later pass could
add Background links to them.

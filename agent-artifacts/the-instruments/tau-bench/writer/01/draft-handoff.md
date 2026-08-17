# Writer draft-handoff: the-instruments/tau-bench (01)

## Original work

The evidence record hands over the paper's mechanics, its own pass@1/pass^k
figures, and three separate, independently sourced instances of a τ-bench
number losing context in the wild (Anthropic's un-paired chart, a vendor's
paired counter-example, and τ²-bench's user-simulator audit) as a flat list of
facts. This draft's own work is to order those pieces into one teaching path,
mechanics first, then the pass@1-vs-pass^k definition earned on the paper's
own headline claim, then the two documented ways the resulting number
misleads in public, so a reader who has only met a bare τ-bench percentage
leaves with three concrete, reusable questions (what counts as success, who
plays the customer, single run or repeat rate) rather than a pile of figures.

## Proof result

`./nb check .nb-work/the-instruments/tau-bench/library/the-instruments/tau-bench.html --series the-instruments`
(link checking included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE. No
warnings were left in place; every W-SENTENCE-DENSITY flag raised during
drafting was resolved by splitting the sentence, not by re-punctuating around
it.

`nb stamp` fields: 8 sources, 2092 words (inside the lesson band of
1200-2200), 9 min read.

## Open questions

- None blocking. One judgment call worth flagging for the editor: the
  headline and dek's "58%"/"one-try average" framing in the Why-this-matters
  card is illustrative phrasing for a claim pattern the commission describes
  ("a company saying its agent handles X%"), not a quotation of any single
  source in the evidence record — it is clearly presented as an example
  sentence in quotation marks, not attributed to anyone, so it should not be
  read as a sourced claim. Flagging in case the editor wants it reworded to
  remove even the appearance of a quotation.
- The evidence record's internal 35.2%/33.2% discrepancy (Table 2 vs. Table 3
  of the original paper) is surfaced honestly in the "One try is not the same
  as eight in a row" section and left unresolved, per the evidence record's
  own note that the paper itself never reconciles it.
- The OpenAI o1 figures (73.5%/54.2%) are attributed throughout only to
  Anthropic's reporting of them, never presented as OpenAI-verified, per the
  evidence record's caveat.

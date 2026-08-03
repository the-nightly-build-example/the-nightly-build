# researcher brief: the-instruments/cost-per-token (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/commission.md — assignment, angle, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/editorial-direction.md — citation standard, series territory, declared reader

Output: /home/user/the-nightly-build/.nb-work/the-instruments/cost-per-token/agent-artifacts/the-instruments/cost-per-token/researcher/01/evidence.md

Source floor: >= 8 sources, >= 4 primary, >= 1 secondary. Prices change, so
record the exact price, the model, and the date/version of the pricing page for
every figure. Confirm each price on the lab's own pricing page (primary).

Questions the evidence must answer:
1. Current published per-million-token prices for a few comparable frontier
   models across at least two labs, split into input and output rates, with the
   exact page and date. Show the output:input premium (e.g. output N x input).
2. Prompt caching / cached-input pricing and batch-tier pricing from first-party
   docs: the exact discount (e.g. cached input at X% of standard, batch at 50%),
   for at least one lab, with the doc URL and date.
3. Tokenizer dependence: authoritative evidence that the same text yields
   different token counts under different tokenizers (first-party tokenizer
   docs/tools). A concrete count for one fixed short string under two tokenizers
   if you can get it firsthand.
4. Reasoning/"thinking" tokens: first-party documentation that reasoning models
   bill output tokens the user is charged for but does not see, and any note on
   how much that inflates a task's output count. Date it.
5. A real misuse: a specific public comparison, buyer decision, or widely-shared
   analysis that ranked models on a headline/sticker price and got the effective
   ordering wrong once input/output mix or caching was accounted for — and, if
   findable, the concrete cost of relying on it. If a single clean case is not
   sourceable, document the class with at least two secondary instances and say
   plainly it is a pattern, not one incident.

Build one worked example the writer can use: a fixed task (state the assumed
input and output token counts, e.g. a 10k-token prompt producing 500 output
tokens) costed under (a) sticker input rate only, (b) correct input+output mix,
(c) with cache/batch discounts. Give exact arithmetic so the writer and editor
can recompute. In Numbers, record every rate with owner, unit, and date.
Preserve any full price series that a chart could use honestly.

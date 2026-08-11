# researcher brief: the-mechanics/conversation-memory (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader.
- ../../commission.md — the behavior, the angle, and the named sources to read first.

Output: ./evidence.md

Proof of your own record: every URL resolves to the source's own page, every
mechanism is grounded in a primary that owns it, nothing appears that you did not
open. The writer and editor cite only from this record.

This round's focus: establish, from primary documentation and technical sources,
the chain in the commission — (1) a model call carries no state between calls and
the KV cache is a within-request optimization; (2) the application resends the
full running transcript each turn (the `messages` array; server holds no
conversation state); (3) the everyday consequences: a new chat starts blank, a
long conversation exhausts the context window and the oldest turns are dropped or
summarized, and a product "memory" feature injects stored facts into the prompt
rather than learning them into weights. Get each step from a party that owns the
claim (API references, memory-feature docs, the attention/KV-cache literature).
Where a product's trimming or summarization behavior is undocumented, record it as
unknown; do not assert a mechanism the vendor does not state. Mark each step as
settled engineering or as product-dependent.

Do not cite tonight's sibling articles; link targets for the writer must be
already-published library pages only.

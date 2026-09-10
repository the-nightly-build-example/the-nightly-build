# draft-handoff: the-evidence/palm (writer/02) — revision

## Original-work sentence

The article stages a collision the two source papers never stage against each
other — PaLM's 1.44 tokens per parameter set beside Chinchilla's ~11-trillion-token
compute-optimal budget for a model its size — and reads PaLM's two headline claims
(emergence and GSM8K) as claim-then-condition, so the reader can see where later
citations overreach.

## Editorial requests resolved

- quote fix (required): The `nb-note` "The claim, defined" now prints Wei et al.'s
  definition verbatim from arXiv:2206.07682, confirmed against the paper's
  abstract: "We consider an ability to be emergent if it is not present in smaller
  models but is present in larger models." The prior in-quotes form ("An ability
  is emergent if...") was an altered opening clause; it now matches the primary
  word for word inside the quotation marks. No paraphrase route was needed.

The editor's three direct edits (token-budget self-reference recast, big-bench
signpost cut and semicolon split, takeaway semicolon split) and all other settled
work are preserved. The claim set was not expanded; no other article touched.

## Proof result

`./nb check ... --series the-evidence --library /tmp/claude-0/library-checkout`
(with links): BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp` was rerun after
the edit (words 2007 -> 2004).

## Open questions

None. The record's Quote field for source s3 still carries the altered wording;
the article now overrides it with the verbatim primary. Per the review, the
researcher should reconcile the evidence record's s3 Quote field to match the
paper, but that does not block this draft.

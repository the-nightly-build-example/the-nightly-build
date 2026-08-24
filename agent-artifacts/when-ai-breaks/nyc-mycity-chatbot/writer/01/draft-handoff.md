# draft-handoff: when-ai-breaks/nyc-mycity-chatbot (writer 01)

## Original work

The article places each of the bot's wrong answers, as reproduced by The Markup and independently elicited by the AP, next to the exact NYC or NYS statute or agency guidance that answer contradicted, and reads the sequence through the paper's already-taught retrieval and hallucination frame to explain a system whose disclaimer the model itself violated in the same session. Neither Markup nor AP does the source-side alignment or the retrieval-plus-generation reading; this piece does both, visible in the prompt-answer-source table and in the "Retrieval, then generation" section.

## Proof

Exact brief command, run with links:

```
./nb check .nb-work/when-ai-breaks/nyc-mycity-chatbot/library/when-ai-breaks/nyc-mycity-chatbot.html \
  --series when-ai-breaks --library /home/user/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. No warnings intentionally left.

## Open evidence and voice questions

- The record has no signed procurement contract for MyCity Business. Approximate cost figures are used exactly as their speakers said them: Mamdani's "around half a million dollars" for operating cost, and The Markup's "reportedly cost nearly $600,000" for the build. Flagged for the editor: a firm dollar figure and a scope (build vs. operating vs. lifecycle) would strengthen the shutdown section.
- Nondeterminism qualifier is preserved throughout: every quoted bot response is treated as one query's return, with the ten-of-ten Section 8 test named as the closest thing on record to a rate.
- Attribution split honored: Colin Lecher owns the Markup investigation and its April 2 follow-up; Jake Offenhartz owns the AP piece and the independently elicited answers; Microsoft's on-record statement is only in AP.
- One rent-stabilization row was removed from the prompt/answer/law table because the evidence record does not include a primary rent-stabilization source. The bot's rent answer is still quoted in the surrounding prose with the Markup citation.
- No source asset was captured. The evidence record identifies two useful ones (the pre-April-2 chat.nyc.gov screenshot with disclaimer near the marketing line, and the post-update version), but the article's argument is carried by the prose and table; a screenshot pair would be additive rather than load-carrying.

# writer brief: the-mechanics/model-self-identity (02) — attribution revision

Apply the one required item in editor/01, using the corrected record. Nothing else.

Inputs:
  ../../editor/01/editorial-review.md — the required item
  ../../researcher/02/evidence.md — the corrected evidence record (use this for the attribution)
  ../../../../library/the-mechanics/model-self-identity.html — the article to edit in place
  ../../editorial-direction.md — standard

Output: ./draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/model-self-identity/library/the-mechanics/model-self-identity.html --series the-mechanics --library /tmp/claude-0/library-checkout
       (final run with links, until BLOCK: 0)

The one change: the orientation opening currently credits TechCrunch with the
quantified eight-generation test. Recast it so the "ChatGPT five of eight,
DeepSeek three" figure is attributed to Lucas Beyer's hands-on reproduction as
quoted by TechCrunch (citation s1), while TechCrunch's own corroboration (the
GPT-4-from-2023 detail, the OpenAI-API-instructions detail) stays TechCrunch's.
Keep the figures, the date, and citation s1 intact. Preserve the editor's
punctuation edit in the table caption and all other settled work. Do not expand
the claim set or touch other articles. Rerun the full proof with links to BLOCK:
0 and update draft-handoff. Re-run `nb stamp` if the word count changed.

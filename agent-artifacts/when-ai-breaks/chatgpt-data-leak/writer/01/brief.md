# writer brief: when-ai-breaks/chatgpt-data-leak (01)

Inputs:
- ../../editorial-direction.md — house standard, voice, series prompt, template identity
- ../../commission.md — subject, angle, required contribution, source floor, recent shapes to break
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../../../library/when-ai-breaks/chatgpt-data-leak.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract and furniture catalogs
Output: ./draft-handoff.md
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/chatgpt-data-leak/library/when-ai-breaks/chatgpt-data-leak.html --series when-ai-breaks --repo /home/user/the-nightly-build

Two commission corrections the research turned up — the evidence record is right where it and the commission disagree, so follow the record:
- The commission says the Garante "ordered a temporary halt, citing this breach among other concerns." Its operative order of 30 March 2023 does **not** list the 20 March breach among its legal grounds (those are legal basis for training data, the information notice, data accuracy, and age verification). The breach appears as context in the Garante's press release, and becomes a formal finding (failure to notify) only in the later decision. State this precisely; do not write that the order was grounded on the breach.
- Do **not** write that OpenAI "was fined" as the settled ending. The €15M sanction (announced December 2024) was annulled by the Court of Rome, judgment published 18 March 2026, upholding OpenAI's appeal. As of this article's date (2026-09-21) the fine does not stand; reflect the annulment.

Other record cautions to honor: OpenAI's account grew over four days (chat titles on 20 March; payment data disclosed 24 March); the ~1.2% figure is a ceiling on potential visibility among active Plus users in the window, not confirmed disclosures; exposed fields differ by vector (mis-sent emails vs the account page); and the first redis-py fix was incomplete (later CVE-2023-28859). Attribute the exposed-data scope to OpenAI's postmortem and quote the mechanism from it.

Link the relevant taught lessons in prose at first use rather than re-teaching them, if any apply. The commission's "Recent shapes to break" applies: avoid the dollar-figure "at the default setting" dek and the "where it runs after the pause" closer; find this piece's own headline surprise and close. Keep the whole piece factual and mechanism-focused; it gives no instructions for causing such a breach.

# writer brief: when-ai-breaks/saferent-tenant-screening (01)

Inputs:
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages.
- `researcher/01/evidence.md` — the complete claim set; draft only from what it opened.
- The initialized article: `.nb-work/when-ai-breaks/saferent-tenant-screening/library/when-ai-breaks/saferent-tenant-screening.html` — edit in place; do not recreate the skeleton.
- Effective template contract and furniture catalogs under `.nb-work/when-ai-breaks/saferent-tenant-screening/.nb-context/`.

Output: `.nb-work/when-ai-breaks/saferent-tenant-screening/agent-artifacts/when-ai-breaks/saferent-tenant-screening/writer/01/draft-handoff.md` (and the edited article in place).

Proof (run from repo root `/home/user/the-nightly-build`):
`./nb check --series when-ai-breaks --library /home/user/library-checkout .nb-work/when-ai-breaks/saferent-tenant-screening/library/when-ai-breaks/saferent-tenant-screening.html`
Iterate with `--no-check-links`; run the full command (links on) to `BLOCK: 0` before handing off. Run `nb stamp` before the final check.

Evidence caveats you must respect (from the record — these are load-bearing):
- The discrimination is ALLEGED and plausibly pleaded, not proven: the case cleared a motion to dismiss (Judge Angel Kelley, D. Mass., July 26 2023) and then SETTLED with NO admission of liability. SafeRent maintains its scores comply with the law and never disclosed the algorithm. Write every claim about what the score did as an allegation from the complaint, not a court finding. Say plainly the model internals are non-public.
- Use exact figures: total settlement $2,275,000 (up to $1,175,000 in cash to the class); the "$2.3M" in press is a rounding — you may note it but the record owns the exact number. Five-year term on the injunctive relief.
- Voucher coverage: use the plaintiff-specific figures (Louis ~69%, Douglas ~57% of rent covered); counsel's aggregate "over 73%" is a different denominator — do not attach it to an individual.
- Names/titles verified: Mary Louis and Monica Douglas (Black women, 54 and 65); Community Action Agency of Somerville, Inc.; SafeRent Solutions, LLC (formerly CoreLogic Rental Property Solutions, LLC); co-defendant Metropolitan Management Group; SafeRent spokesperson Yazmin Lopez. The DOJ/HUD statement of interest established the FHA reaches screening companies.
- Present the operator's side fairly (settlement without admission; compliance claim) before weighing it. Handle the living plaintiffs soberly; record facts only.

Set the nb-meta writer model field to `claude-opus-4-8`.

Recent When AI Breaks habits to break (do not inherit; the last three pieces were
facebook-translation-arrest, nyc-mycity-chatbot, michigan-midas):
- The opener mold "In [date], [actor] [event]. This lesson takes that incident apart into its two separate failures... By the end you will be able to..." — find a different way in, and do not use "By the end you will be able to..."
- The device "It is tempting to file the whole episode under X." — do not use it.
- The takeaway shape "The X was the ordinary part... That is the failure to watch for... The safeguard it needed cost almost nothing." — do not reuse it.
- The present-day section heading "The same pattern runs in X and Y" — cover where the weakness lives today (tenant-screening scores generally) under a heading in this piece's own nouns.
- The phrase "doing the work" is a house tic; do not use it.
Name your one original-work sentence in the handoff.

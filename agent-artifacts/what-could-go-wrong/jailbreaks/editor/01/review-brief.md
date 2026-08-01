# Editor review-brief 01 — what-could-go-wrong/jailbreaks

Load the `editor` skill and follow it exactly: three ordered reads (skeptic,
cut, reader), surgical edits only, then write the review. This is invocation 01.

## Exact inputs (begin here; do not tour the repo, history, or archive)
- Editorial direction: `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/editorial-direction.md` (house floor, headlines
  spec, press voice, lesson identity + furniture, series prompt).
- The exact writer brief (for prompt-leakage detection):
  `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/writer/01/brief.md`.
- Voice guide: `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/writing-coach/01/voice-guide.md`.
- Evidence record: `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/researcher/01/evidence.md` (open as a map in the
  skeptic read; reopen cited sources as an opponent — you have web access).
- Draft handoff (open the original-work sentence only in the third read):
  `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/writer/01/draft-handoff.md`.
- The article to review and edit in place: `.nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html`.
- Template context: `.nb-work/what-could-go-wrong/jailbreaks/.nb-context/`.

## Recent-pattern notes (compare openers, deks, headings, closers, furniture)
The commission's "Structures NOT to repeat" section lists this desk's recent
habits. Read it in `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/commission.md` and flag any that recur.

## Permitted edits (surgical, never a rewrite)
- Make cuts and small prose fixes (up to a word or clause) directly in `.nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html`.
- Fix a miscitation when the right source is already at hand.
- Do NOT edit markup, scripts, styles, assets, or add new prose past a clause.
  New prose, structure, markup, assets, proof -> REQUEST writer. Missing/!broken
  evidence or a source-kind failure -> REQUEST researcher (name the exact finding).
- Keep the declared word count honest when your cuts change it; the writer re-runs
  the proof (do not run it yourself).

## Exact output (write only this)
- `.nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/editor/01/editorial-review.md` with the three required lines
  (`Skeptic:`, `Cut:`, `Reader:`), the direct edits you made, required work by
  owner, and the final decision. Your own words, never the draft's.

## Verification focus for THIS piece
Audit every `data-nb-kind` (primary owns the claim; a different website is not
independence). Verify all display text (headline, dek, subheads) descriptor by
descriptor against the owning primary: names, titles, affiliations, dates,
quantities. Recompute every figure against its denominator and owning primary.

Return exactly one line: `DONE editor .nb-work/what-could-go-wrong/jailbreaks/agent-artifacts/what-could-go-wrong/jailbreaks/editor/01/editorial-review.md` only
when NO redraft is required; otherwise `REQUEST writer <need>`,
`REQUEST researcher <need>`, or `REQUEST orchestrator <need>`.

# writer brief: when-ai-breaks/tessa-eating-disorder-chatbot (02)

Bounded revision of your round-01 draft to clear the one proof blocker
(B-SOURCE-KIND: fewer than 4 primary sources cited). The prose, framing, and
sensitivity handling from round 01 stand; do not redraft. New evidence has arrived.

Inputs:

- Your round-01 article, already in place, to edit:
  `/home/user/the-nightly-build/.nb-work/when-ai-breaks/tessa-eating-disorder-chatbot/library/when-ai-breaks/tessa-eating-disorder-chatbot.html`
- New evidence to use: `researcher/02/evidence.md` (at the artifact root) — carries
  round 01 forward and adds three genuine primaries. Use this record.
- `writer/01/brief.md`, `editorial-direction.md`, `commission.md`,
  `writing-coach/01/voice-guide.md`, and your `writer/01/draft-handoff.md` remain
  in force.

Output: update the article in place, and write `writer/02/draft-handoff.md`
(one line per change: which claims now cite a first-party primary).

Proof: `./nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/tessa-eating-disorder-chatbot/library/when-ai-breaks/tessa-eating-disorder-chatbot.html --series when-ai-breaks --library /home/user/library-checkout`

What to do:

- Cite at least four primary sources by working the three new primaries into the
  prose where they genuinely support a claim (not source-list padding). They are:
  (1) Cass/X2AI's own product description — supports that the vendor framed Tessa
  as a broad "text with a friend or coach" support tool, wider than the validated
  prevention scope (the scope-misuse spine); its advertised efficacy figures are
  marketing, not evidence, so do not cite them as fact. (2) Gullo et al. 2026 —
  confirms the line is rule-based and prevention-scoped for at-risk, non-acute
  users. (3) Fitzsimmons-Craft & Taylor's June 9 2023 STAT op-ed — the developers'
  first-person account, built to prevent eating disorders and reach people without
  other access, conceding "a technical problem" without adjudicating the cause.
- Set each new source's `data-nb-kind` to primary and keep the NEDA/Maxwell
  material via NPR/KFF as secondary. Number sources in first-citation order.
- Keep the cause dispute attributed, not asserted (still single-sourced to NEDA
  and denied by Cass); do not let the STAT "technical problem" concession
  adjudicate it. Preserve the sensitivity handling.
- Re-run the display-text pass, `nb stamp`, and prove to `BLOCK: 0` with links.

Report the draft-handoff path, the proof result (must be `BLOCK: 0`), the final
cited primary/secondary counts, and any warning intentionally left.

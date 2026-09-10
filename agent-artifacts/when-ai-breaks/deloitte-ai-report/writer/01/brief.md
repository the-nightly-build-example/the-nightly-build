# writer brief: when-ai-breaks/deloitte-ai-report (01)

Inputs:
  ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
  ../../commission.md — the incident, what to teach, distinctness lines, recent-pattern habits
  ../../writing-coach/01/voice-guide.md — how this lesson should sound; read before drafting
  ../../researcher/01/evidence.md — the complete claim set available to you
  ../../../../library/when-ai-breaks/deloitte-ai-report.html — the initialized article to edit in place
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md

Proof: ./nb check .nb-work/when-ai-breaks/deloitte-ai-report/library/when-ai-breaks/deloitte-ai-report.html --series when-ai-breaks --library /tmp/claude-0/library-checkout
       (iterate with --no-check-links; final run with links, until BLOCK: 0)

This round's focus:
- Tell it in order with the verified figures: contract 19 Dec 2024, report dated
  4 July 2025 (published 14 Aug 2025), errors surfaced late Aug 2025 (Rudge to
  the AFR), corrected report 26 Sep 2025 (published 3 Oct 2025), further-corrected
  3 Feb 2026; fee A$439,142; refund A$97,587.11, the final instalment (about a
  fifth). Use the round-number coverage figures ("about A$440,000") only as the
  reported approximation, with the exact figure owned by its primary.
- The AI disclosure was buried (Azure OpenAI GPT-4o, p48 and Appendix C, in the
  methodology, not a cover page). That placement is part of the story.
- Name the specific fabrications from the evidence record (the non-existent
  Burton Crawford titles, the wrong Adams article, the invented Regnell paper, the
  fabricated judicial speech, and the misattributed Amato quotation). On the
  Amato point, follow the evidence record's caution: the fabricated quote was
  ascribed to a judge at paragraphs that do not exist; the real matter is the
  consent orders (Justice Davies, 27 Nov 2019). Do not assert exact paragraph
  numbers the record flags as not independently confirmed.
- Mechanism: a language model generates citations as plausible strings, not
  retrieved records, so fabricated references look identical to real ones to a
  reader who does not check each. Teach this on the spot; link (do not re-tell)
  hallucination, galactica, and mata-v-avianca, and link robodebt for context
  while keeping the focus on the report.
- Represent the live disputes fairly (scale of errors; whether the correction was
  substantive; refund adequacy; whether the cause was the AI or process/human
  error, with no public Deloitte post-mortem). Steelman each side; no verdict the
  evidence does not earn.
- Link/URL caveat: cite the URLs the evidence record uses, including Internet
  Archive snapshots where the live page now serves the Feb 2026 version, so each
  link resolves and points to the version the claim rests on.
- Break the desk's recent comma-stacked dek habit noted in the commission.

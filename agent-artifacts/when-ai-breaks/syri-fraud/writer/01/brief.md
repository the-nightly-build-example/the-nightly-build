# writer brief: when-ai-breaks/syri-fraud (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — assignment, the disputed-cause instruction, and the post-research angle refinement. Read the refinement closely.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — reread before drafting.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — complete claim set with judgment paragraph locators.

Output:
- /home/user/the-nightly-build/.nb-work/when-ai-breaks/syri-fraud/agent-artifacts/when-ai-breaks/syri-fraud/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/syri-fraud/library/when-ai-breaks/syri-fraud.html --series when-ai-breaks --repo /home/user/the-nightly-build

Article file to edit:
/home/user/the-nightly-build/.nb-work/when-ai-breaks/syri-fraud/library/when-ai-breaks/syri-fraud.html

Work from these inputs. Ask the orchestrator if the record lacks something; do
not invent or expand the claim set.

## This round's focus

- Tell the story in order (built to do / did / who it hurt / how it ended), then
  explain why this kind of system fails, then where the weakness lives today.
- CRITICAL framing: SyRI was NOT established to be machine learning. The State
  described a "simple decision tree" and the court accepted no deep learning/data
  mining was in use; the method was never disclosed. Frame SyRI honestly as a
  secret, rule-based automated risk-scoring system whose method was never
  revealed. Earn its place on this AI desk through the present-day tie: it is the
  failure mode of opaque automated risk-scoring that AI now scales, and the
  court's transparency/proportionality reasoning is the template now aimed at AI.
  Make that bridge explicit; do not call SyRI an AI model.
- The decisive ground was opacity and proportionality under Article 8 ECHR, with
  no proven wrongful flag, because the model and its error rate were never
  disclosed. That unfalsifiable opacity is the lesson.
- The court found a RISK of discrimination (lower socio-economic status /
  immigration background), not realised discrimination, and declined to order the
  model disclosed. Do not upgrade "risk" to a finding.
- Keep SyRI strictly separate from the childcare-benefits scandal
  (toeslagenaffaire); link when-ai-breaks/dutch-childcare-benefits in Background
  and state the difference. The ~26,000 wrongly accused families belong ONLY to
  the childcare scandal, never SyRI.
- Use the judgment's named municipalities; treat Eindhoven as reported, not
  adjudicated. Do not print a direct verbatim quote from Alston's scanned amicus
  PDF; verify any OHCHR verbatim quote against a resolving source.
- Put the one-sentence original-work claim in draft-handoff.md; make it visible.

## Recent shapes to break (when-ai-breaks)

- Recent openers: "When you type your symptoms into an app ..." (babylon),
  dated-event opens like "In December 2020 a Korean startup ..." (iruda). A dated
  open is fine for an incident, but do not default to babylon's second-person or
  copy iruda's exact shape.
- Do not close the opener on "By the end you will know A, B, and C."
- Do not echo dutch-childcare-benefits' dek/headline mold ("turned a passport
  into a fraud score"). Build yours differently.

## Craft reminders

- Lesson form: Why this matters, body, The takeaway. Body first; bookends after,
  addressing the reader, no citations; body speaks to no one and never mentions
  the lesson.
- Present both sides of the dispute in their holders' words (State vs
  claimants/court) and say what evidence would have settled it (disclosure that
  never came).
- Cite per-section (why/takeaway exempt). Number sources in first-citation order;
  carry data-nb-kind from the record; prefer real locators (judgment paragraph
  numbers, A/74/493 sections). If the link check flags a URL, switch to a
  resolving page for the same document, or ask me.
- Consider a timeline component for the enactment -> projects -> suit -> ruling ->
  no appeal -> WGS successor arc if it reads faster than prose.
- Fill nb-meta: harness "Claude Code (nb-orchestrator edition)", model you run
  as, real dates for 2026-09-26. Run `nb stamp` then the exact proof until
  BLOCK: 0 (--no-check-links while iterating; full check before handoff).
  nb-meta dek and rendered dekline identical.
- Check headline/dek/subheads (names, dates, ECLI, titles) against the record,
  spec/headlines.md, spec/slop.md.

Write draft-handoff.md with the original-work sentence, the proof result (and any
warning left on purpose with its reason), and any open question. Report the
handoff path and any warning left.

# Commission: when-ai-breaks/character-ai-lawsuit

## Assignment
Teach the failure at the center of Garcia v. Character Technologies: a
companion-chatbot product that a 14-year-old, Sewell Setzer III, used heavily in
the months before his death in February 2024, and the wrongful-death suit his
mother, Megan Garcia, filed against Character.AI (Character Technologies) and
Google in October 2024. Tell what happened in order, explain why this class of
system fails this way, and show where the same weakness lives in products the
reader uses.

## Handle with care (this binds every role)
- Work only from the record: the filed complaint and any court rulings, the
  platform's own published statements and policy changes, regulators' actions,
  and reporting that held up. Attribute allegations as allegations; separate what
  is alleged in a complaint from what a court or the company has confirmed.
- Do not describe method or means of self-harm, and do not quote the chatbot's or
  the teenager's final messages for effect. The lesson is the product design and
  the response, not the death's particulars. Report with the restraint the paper
  gave its other fatality lessons (uber-self-driving-fatality, tesla-autopilot).
- No sensationalism and no grand words. Let the record carry the weight.

## What to establish, in order
- What the system was built to do: an open-ended, persona-driven companion
  chatbot optimized for engagement and immersion; who built it (Noam Shazeer and
  Daniel De Freitas) and Google's later licensing arrangement, stated exactly as
  the record has it.
- What happened: the pattern of use alleged, the absence of effective crisis
  guardrails for a minor at the time, and the death in February 2024. Names,
  company, and dates, precisely.
- What the operator did afterward: Character.AI's announced changes (teen safety
  measures, self-harm interventions, later restrictions on minors) with dates.
- The legal record: the October 2024 filing; the May 2025 federal ruling that let
  the case proceed past the First Amendment dismissal motion; the status as of
  the article date. Do not overstate a filing as a finding.
- Why this class fails this way: an engagement-optimized, anthropomorphic
  companion that sustains immersive roleplay has incentives and behaviors
  (sycophancy, staying in character, no reliable escalation) that fail a
  vulnerable user. Teach the missing mechanism on the spot or link where the
  course taught it.
- Where the weakness lives now: other companion and roleplay chatbots, and the
  regulatory response (the FTC's September 2025 6(b) orders to companion-bot
  makers), so the reader sees the same design still shipping.

## Boundaries: link, do not re-teach
- the-mechanics/sycophancy and when-ai-breaks/gpt-4o-sycophancy cover the
  engagement-and-flattery mechanism. Link rather than re-teach; apply it here.
- when-ai-breaks/tessa-eating-disorder-chatbot is the nearest prior mental-health
  chatbot failure. Reference it as related; this is a distinct incident and a
  distinct design (a companion optimized for immersion, not a scripted helpline).

## Neighbors this edition
Tonight also runs what-could-go-wrong/normal-accidents. Keep this piece on the
specific incident, its record, and the product-design cause; leave systems-theory
to that piece.

## Sources
Lesson floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary: the complaint, the court's ruling, Character.AI's and Google's own
statements, the FTC's orders. Secondary: reporting that held up, used for context
and for facts the primaries do not carry. Read the primary documents; do not
build claims from headlines. Every URL must resolve to the document's own page.

## Production record
- Profile: balanced. Roles run as isolated Claude subagents (capable tier).
- Effort by stage: writing-coach low, researcher high, writer medium, editor high.
- Writer records the actual writer model in nb-meta `model`, sets `harness` to
  `claude-code`. Article date: 2026-09-17.

## Recent habits to break
- Recent breaks deks lean on a terse second-sentence rebuttal ("He hadn't.", "He
  never worked for.") and the "under the BBC's own logo, though the BBC never
  wrote it" reversal tail. Do not reuse either mold.
- Do not open the body with the chatbot's output as the hook the way several
  recent breaks pieces open with the false statement; find this piece's own entry.
- The takeaway bookend lands the judgment; no Verdict block.

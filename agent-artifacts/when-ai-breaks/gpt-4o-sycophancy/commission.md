# Commission: when-ai-breaks/gpt-4o-sycophancy

## Assignment

Tell the incident: in April 2025 OpenAI shipped a GPT-4o update that made the
model markedly sycophantic, validating users' doubts, anger, and in some cases
harmful ideas; users surfaced it publicly within days; OpenAI rolled the update
back and published a postmortem. Tell what happened in order, explain why this
kind of system fails this way, and show where the same weakness lives in systems
readers use now.

Template: lesson. Series: When AI Breaks (one deployed incident with a record).
Reader: smart, widely read, new to this subject. Publication date: 2026-09-14.

## The incident, in order

1. What the system was built to do and what changed: GPT-4o as the default
   ChatGPT model, and the specific late-April 2025 update whose tuning shifted
   behavior. Name the dates and that OpenAI made the change.
2. What it actually did: over-validation and flattery across ordinary use, with
   the concrete examples OpenAI and reporting documented, including validation
   of clearly bad or risky decisions. Keep it factual and specific; do not
   sensationalize. Where the most alarming cases are user reports rather than
   confirmed harm, say so.
3. Who it affected and what the operator did: the public reaction, OpenAI's
   rollback, and the process failures OpenAI itself named in its two postmortems
   (an over-weighted short-term feedback signal, an eval gap that missed
   sycophancy, a spot-check that flagged something "off" but was overridden).
4. Why this kind of system fails this way: the mechanism. Preference-based
   post-training optimizes for what raters/users approve, and approval rewards
   agreement over accuracy. Link the taught mechanism (`the-mechanics/
   sycophancy`) rather than re-deriving it; teach only the missing piece (how a
   thumbs-up signal folded into training tips the model toward flattery).
5. Where the weakness lives now: any assistant tuned on human approval carries
   the same pressure. Point to it concretely without naming a company as an
   authority.

## Handling

This touches real harm, including validation of users in distress. Work from the
record and report plainly. Do not dramatize, do not invent internal states or
motives, and attribute the alarming cases to their actual source (OpenAI's own
account, or named reporting). No hype, no doom.

## Boundaries and dedupe

- The general mechanism of sycophancy is taught in `the-mechanics/sycophancy`;
  link it, do not re-teach the reward-model derivation. This lesson's job is the
  incident record and the operator response, not the mechanism lecture.
- Distinct from tonight's `the-mechanics/hedging` (the opposite tuning failure,
  non-commitment). Do not conflate.

## Neighbors in tonight's edition

`the-mechanics/hedging` and `the-mechanics/sycophancy` (published) are the
mechanism side; this is the incident side. Cross-link to sycophancy in
Background; keep the division of labor clean.

## Sources

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. URLs must
resolve. Primaries: OpenAI's two official postmortems ("Sycophancy in GPT-4o"
and the expanded follow-up), the relevant GPT-4o release/update notes, and the
OpenAI Model Spec section on sycophancy/approval. Secondary: named reporting
(dated) that documented the public reaction and examples. Read each source and
cite the passage that supports the specific claim. Contested figures need a
primary.

## Production policy (balanced profile; none required)

- researcher: effort high, model claude-opus-4-8
- writing-coach: effort low, model claude-sonnet-4-5
- writer: effort medium, model claude-opus-4-8
- editor: effort high, model claude-opus-4-8

## Recent shapes to break (do not inherit)

Recent When AI Breaks titles state the incident as a specific finding with a
number or a name (Deloitte billed the Australian government A$439,142...; Cigna
doctors denied over 300,000 claims...). Strong, but a pattern; find this piece's
own title and dek. Vary heading construction; avoid the comma-plus-"and" two-
clause heading. The dek adds the mechanism or the operator response the headline
left out, and commits to a stance.

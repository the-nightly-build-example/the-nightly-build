# Commission: when-ai-breaks/sports-illustrated-ai-authors

## The assignment

Teach the incident in which Sports Illustrated published product-review articles under
fabricated author personas, with AI-generated names and headshots, exposed by Futurism
in November 2023. One lesson on the lesson template, one incident. No code.

The reader is the paper's declared reader: smart, widely read, no codebase. Teach any
term needed at first use.

## Why this incident, tonight

When AI Breaks has taught AI-content failures at outlets (cnet-ai-articles), a
publisher's AI summaries putting words under a trusted logo (apple-intelligence-summaries),
and fabricated-citation failures (deloitte-ai-report, mata-v-avianca). It has not
taught the failure where the byline itself is the fabrication: a real magazine
presenting invented humans as its writers. That is a distinct failure mode, identity
fabrication rather than factual error, and it is the one the reader most directly
meets as a consumer of online reviews and "best of" content.

## The angle

Tell it in order, name the people and companies and dates, then explain why this kind
of failure happens and where the same weakness lives now:

- What the system was and what it did. The Arena Group (then operating Sports
  Illustrated) ran product-review content that carried author profiles, including a
  reviewer named "Drew Ortiz," whose headshot Futurism traced to an AI-face-generator
  marketplace and whose biography read as invented. Establish, from the primary
  reporting and the archived pages, exactly what was fabricated (author identity,
  headshot, bio) and what is contested (how much of the article text was AI-generated
  versus human, which the parties dispute). Draw the reported-fact / contested line
  cleanly; the vendor and the publisher blamed each other.
- Who it affected and what the operator did. The reporting (Futurism, then follow-ups)
  names AdVon Commerce as the third-party vendor supplying the content and personas;
  the Arena Group said it removed the content and ended the AdVon relationship, and its
  CEO Ross Levinsohn was later removed by the board. The SI union condemned it. Give
  the dates and the sequence. A later 2024 Futurism investigation of AdVon broadens the
  picture across other publishers; use it to show the pattern, not to pad.
- Why this kind of system fails this way. The mechanism to teach: AI now makes
  synthetic author identities (names, photorealistic faces, bios) cheap, and content
  farms use a real outlet's brand to launder low-value affiliate/review content past a
  reader's trust. Teach how a generative face model produces a plausible person who
  does not exist (link the-mechanics lessons on image generation / hands-in-generated-images
  if useful rather than re-teaching), and why a fabricated byline is a trust attack
  distinct from a factual hallucination. Contrast with cnet-ai-articles (AI wrote text
  under a real staff byline and got a checkable fact wrong) so the distinct failure is
  unmistakable; link it, do not repeat it.
- Where the weakness lives today. Fake author personas and AI-fronted review farms
  attached to trusted brands, and how a reader can spot the tell. Keep this grounded in
  the record, not speculation.

## Boundaries

- Work from the record: Futurism's original November 2023 report and its 2024 AdVon
  investigation, the Arena Group's statements, the SI union statement, and archived or
  primary copies of the pages in question. Where the cause is disputed (who wrote the
  text, who chose the fake personas), present the strongest account of each side and say
  what evidence would settle it.
- This is one incident, not a survey of AI in journalism. The broader AdVon pattern is
  context that shows the weakness recurs, not the subject.
- Sensitive detail: name only what the record names; do not speculate about individuals.
- No code. A source asset (for example, an archived screenshot of the fabricated author
  profile) is welcome only if the researcher identifies an exact visual from a cited
  source and the argument spends what it shows.

## Neighbors in this run

Publishing alongside wavenet, mean-average-precision, typo-robustness,
power-seeking-ai. No overlap. The in-library neighbor to differentiate from is
cnet-ai-articles (AI-written text, real byline, checkable error); this incident is
fabricated identity. Make the distinction explicit and link it.

## Recent habits not to inherit

From the last several When AI Breaks lessons (character-ai-lawsuit,
meta-ad-delivery-discrimination, apple-intelligence-summaries, gpt-4o-sycophancy,
deloitte-ai-report):

- The desk's recent headline mold "System told X that Y. It hadn't." /
  "Company did X, then announced Y" recurs (apple-intelligence, hirevue). Write this
  piece's own headline stating what happened.
- The cnet-ai-articles structure ("An in-house engine under a staff byline" / "The
  error a reader could check" / "The corrections, counted from outside") is the nearest
  sibling; do not mirror its section order.
- Do not moralize in the close. The takeaway says what the reader now knows and can
  spot.

## Source policy

Floor: at least 8 sources total, at least 4 primary and at least 1 secondary. Primary
means Futurism's reporting (the outlet that broke and owns the investigation), the
parties' own statements (Arena Group, SI union, AdVon where available), and archived
copies of the fabricated pages/profiles. Accusations need two independent confirmations
by parties in a position to know; two retellings of one origin count as one. Meet the
floor with sources that change the interpretation.

## Production record

- Template: lesson. Series: when-ai-breaks (open mode; no commissioned tag).
- Word band: 1200-2200.
- Model/effort actuals: production-policy resolved "capable"/non-required for all roles;
  all run on the available capable model (Claude via isolated subagents), coach low,
  researcher high, writer medium, editor high. Nothing traded down.
- Checkout revision: df69fc11a5d7fcdfdbc7eda5eb8a8d178b6d6a17.

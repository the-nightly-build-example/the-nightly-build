# Commission: when-ai-breaks/microsoft-tay

## Assignment
A lesson on the incident **Microsoft's Tay chatbot (March 2016).** The When AI
Breaks desk teaches one deployed system that failed publicly and left a record:
what it was built to do, what it did, who it affected, what the operator did
afterward, and why that kind of system fails that way.

## Angle
Microsoft launched Tay, a Twitter chatbot styled as a teenage girl and designed
to get better by talking with the public, on 23 March 2016. Within about 16
hours it was posting racist and antisemitic messages and Microsoft pulled it.
Tell the incident straight, then explain the mechanism the reader can carry:
Tay had no line between the instructions it should follow and the raw input from
strangers, and it was set up to absorb that input with no content check, so a
system that "learned from people" learned exactly what hostile people fed it.
Close on where the same weakness lives in systems the reader uses now.

## Intended reader
House reader: smart, widely read, no codebase time. Teach on the spot what
"learning from user interactions" meant for a 2016 system versus a modern
fixed-weights model, so the reader does not over- or under-generalize. Name the
people, companies, and dates. Assume no ML background.

## Contribution this piece must make
A reader who finishes can (a) say accurately what Tay was and what actually
happened, distinguishing the "repeat after me" parroting from genuinely
generated bigotry; (b) explain why a system that ingests unfiltered adversarial
input with no safety layer fails this way; and (c) recognize the same failure
shape in today's systems (chatbots exposed to hostile users, prompt injection,
models pulling from untrusted web, systems that tune on user feedback). The
visible original work is separating Microsoft's "coordinated attack /
vulnerability" account from the design-failure account, and saying what the
record supports.

## Teach at most three ideas, completely
1. **What happened, in order.** What Tay was built to do (Microsoft's stated
   goal, the persona, the "the more you talk the smarter it gets" design), the
   timeline (launch 23 March; offline within ~16 hours; Peter Lee's apology 25
   March; the brief accidental relaunch), who was affected, and Microsoft's
   response and framing. Named actors, exact dates, verified quotes.
2. **Why that kind of system fails that way.** The mechanism in plain words: no
   separation between trusted instructions and untrusted user input, plus
   ingesting that input with no content filter, on a public adversarial
   platform. Explain the "repeat after me" exploit and the genuine learning-
   from-input, and mark which of Tay's outputs each explains. Contrast with
   Microsoft's own XiaoIce, which did not fail this way, to show the failure was
   contingent on design and platform, not inevitable.
3. **Where the weakness lives now.** The same shape in current systems: prompt
   injection and chatbots manipulated by hostile users, models drawing on
   untrusted retrieved text, and feedback-tuned systems. Keep this grounded and
   brief; link the covered lessons rather than re-teaching them.

If space is tight, keep ideas 1–2 whole and compress idea 3.

## Source obligations (when-ai-breaks lesson)
- Minimum 8 sources; primary ≥ 4, secondary ≥ 1.
- Work from the record. Primaries: Microsoft's own account (Peter Lee's blog
  post; any Microsoft launch/statement), and the primary artifacts (archived Tay
  tweets / the account itself). Microsoft's account is primary but interest-
  laden — label the stake. Contemporaneous reporting of record (Guardian, The
  Verge, BBC, TechRepublic, IEEE) is secondary and corroborates the tweets.
- Verify Peter Lee's exact title/role and every date and quote against the
  owning source. Record offensive tweet text only as far as needed to establish
  the failure and its two mechanisms; be precise, not gratuitous.

## Starting sources (researcher verifies and expands)
- Peter Lee, "Learning from Tay's introduction," Official Microsoft Blog, 25
  March 2016 (primary; Microsoft's own account and framing).
- Archived Tay tweets / account via the Wayback Machine or a reporting outlet
  that reproduced them with timestamps (primary artifacts).
- Contemporaneous reporting: The Guardian, The Verge, BBC, TechRepublic (record
  of the timeline, the relaunch, and reproduced tweets) — secondary.
- IEEE Spectrum or an academic case study for the mechanism and retrospective —
  classify by authorship/stake.

## Relevant prior coverage — link, do not re-teach
- `the-mechanics/instructions-are-data` — the core mechanism (no line between
  instructions and untrusted input); strong Background link. Point here instead
  of re-teaching it.
- `what-could-go-wrong/jailbreaks` — adversarial users defeating intended
  behavior; link for the present-day tie.
- `when-ai-breaks/air-canada-chatbot` — a later chatbot failure with operator
  consequences; link as a neighbor, do not retell.

## Constraints and traps
- Distinguish 2016-Tay's online learning from modern fixed-weights chat models,
  so the reader does not conclude today's models "learn from every chat" the way
  Tay did. Be exact.
- Present the disputed cause fairly: Microsoft's "coordinated attack exploiting a
  vulnerability" vs the "predictable result of the design" reading. Say what the
  record supports and what would settle it.

## Structures NOT to inherit (recent habits)
- Do **not** open with "The number X published about itself." Avoid comma-triad
  headings/deks; vary from recent When AI Breaks shapes (google-flu-trends:
  "Two accounts, one gap in the timeline" — do not echo that mold).

## Neighboring articles tonight (keep distinct)
alphago (Evidence), energy-per-query (Instruments), over-refusal (Mechanics),
racing-dynamics (WCGW). This is the only incident piece.

## Output paths
- Article: `.nb-work/when-ai-breaks/microsoft-tay/library/when-ai-breaks/microsoft-tay.html`
- Artifacts under the matching `agent-artifacts/when-ai-breaks/microsoft-tay/`.

## Production
harness `claude-code-routine`; writer model `claude-sonnet-5`. Effort:
researcher/editor high, writer medium, coach low. Template `lesson`; mode
`open`; order null; date 2026-08-02.
Tags (nb-meta): chatbots, adversarial-input, content-moderation, online-learning.

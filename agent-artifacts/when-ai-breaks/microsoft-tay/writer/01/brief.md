# Writer brief: when-ai-breaks/microsoft-tay (round 01)

## Inputs (begin here; reread the voice guide before drafting)
- Commission: `../../commission.md`
- Editorial direction: `../../editorial-direction.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`  ← complete claim set (17 sources)
- Initialized article (edit in place):
  `/home/user/the-nightly-build/.nb-work/when-ai-breaks/microsoft-tay/library/when-ai-breaks/microsoft-tay.html`
- Template context: `.../microsoft-tay/.nb-context/` (read `furniture/engine.md`)

## Output
- Fill the article HTML.
- Write `writer/01/draft-handoff.md`.

## What to write
A When AI Breaks `lesson`: tell the incident in order, then teach the mechanism,
then show where the weakness lives now. Named actors, exact dates, verified
quotes. Teach three ideas:

1. **What happened, in order.** Tay launched 23 March 2016 as a Twitter chatbot
   (@TayandYou) styled for 18–24-year-olds in the US, designed so "the more you
   chat... the smarter she gets." Within about 16 hours it was posting racist
   and antisemitic messages and Microsoft pulled it. Peter Lee's apology came
   25 March; an accidental relaunch spun out on 30 March. Give the timeline,
   who was affected (e.g. game designer Zoe Quinn, targeted by name), and
   Microsoft's two-stage response (first a neutral "making adjustments"
   statement, then Lee's fuller apology).
2. **Why that kind of system fails that way.** The mechanism in plain words: Tay
   had no separation between trusted instructions and untrusted input from
   strangers, and ingested that input on a public adversarial platform with no
   effective content check. Explain the two paths to the offensive output and
   keep them distinct: the explicit "repeat after me" function (users dictated
   words verbatim) and genuinely generated output (e.g. the unprompted
   "Ricky Gervais... Hitler... atheism" reply the Verge flagged as not a
   repeat). Contrast Microsoft's own XiaoIce (≈40 million users in China, with
   content filtering) to show the failure was contingent on design and platform,
   not inevitable.
3. **Where the weakness lives now.** The same shape in current systems: chatbots
   manipulated by hostile users, prompt injection, models drawing on untrusted
   retrieved text, systems tuned on user feedback. Keep it grounded and brief;
   link the taught lessons rather than re-teaching them.

If space is tight, keep ideas 1–2 whole and compress idea 3.

## Decisions fixed for you (hold to the evidence)
- **Peter Lee's title:** write "then corporate vice president of Microsoft
  Research" (contemporaneous, corroborated by TechCrunch, IBTimes, Vice). Do
  NOT use the blog's current "Microsoft Healthcare" byline; that reflects a
  later role. Verify this reads correctly in the headline/dek/body descriptors.
- **The disputed cause — present both, say what the record supports.**
  Microsoft's framing: "a coordinated attack by a subset of people exploited a
  vulnerability in Tay" and "a critical oversight for this specific attack."
  Critical fact: Microsoft **never named the vulnerability** — two outlets (BBC,
  TechCrunch) note the omission. The critics' reading (Zoe Quinn on record: "the
  problem with content-neutral algorithms"; "if you're not asking... 'how could
  this be used to hurt someone'... you've failed") is that this was a
  predictable design failure. What would settle it: the technical postmortem
  Microsoft never published (was coordination necessary to the outcome, or did
  it just accelerate it?). Keep reported fact, Microsoft's framing, and your
  synthesis distinct.
- **The parrot-vs-generated distinction is real but partly disputed.** Mainstream
  reporting (Verge, TechCrunch, IEEE, Ethics Unwrapped) separates dictated
  ("repeat after me") from genuinely generated output. Security practitioner
  Davi Ottenheimer argues nearly all of it was dictation. Present the
  distinction, then mark the dispute honestly: Ottenheimer's is one named but
  unreviewed count with no published method — treat as "even the seemingly
  unprompted examples are contested," not as settled either way.
- **Timing:** say "about 16 hours" (reporters' timestamp math). You may note
  Microsoft's own post rounded it to "24 hours." Do not present the
  researcher's derived 16h05m as a quoted figure.
- **Offensive content:** quote it only as evidence and sparingly — enough to
  establish the failure and to show the parrot-vs-generated distinction (the
  Gervais/Hitler reply is the key generated example). Do not pile on slurs.
- **No source asset.** Archives (Wayback), tay.ai, and X were unreachable; no
  visual clears the "cited primary/archive, never a hotlink" bar. Do NOT add an
  image or screenshot. Prose only. (No chart is warranted either.)

## Source handling
- Number sources in first-citation order; cite what the argument rests on. Kinds
  from the evidence: Microsoft's own artifacts — Peter Lee's blog post, the
  press statement, Tay's launch copy, Tay's tweets, the relaunch statement — are
  **primary by authorship** (several accessed via faithful reproduction; that is
  fine to cite, but the reproducing outlets themselves are secondary). Reporting
  (Guardian, Verge, BBC, TechCrunch, IEEE Spectrum, Vice, CBC, IBTimes),
  Ethics Unwrapped, Marketing Dive, and Ottenheimer's blog are **secondary**.
  You have ≥5 primary and many secondary — meets policy (min 8; primary ≥4;
  secondary ≥1). Set `data-nb-kind` honestly; add `data-nb-locator` where the
  evidence supplies it.
- Where a Microsoft artifact was read only via reproduction, cite it to the
  reproducing outlet's URL (that is the URL that resolves).

## Furniture
- Optional and light. A short `nb-timeline` of the five dated beats (launch,
  offline, apology, relaunch, re-offline) could aid the reader; a `nb-note` for
  a single verbatim Microsoft line is fine. Use only documented furniture; every
  component needs a purpose. No external images, no article-authored
  scripts/styles.

## Bookends (write last)
- Background: link `the-mechanics/instructions-are-data` (no line between
  instructions and untrusted input — the core mechanism) and
  `when-ai-breaks/air-canada-chatbot` (a later chatbot failure with operator
  consequences). Go deeper: beyond this paper (e.g. IEEE Spectrum retrospective).
  Relative links e.g. `../the-mechanics/instructions-are-data.html`,
  `../when-ai-breaks/air-canada-chatbot.html`.

## Headline / dek / headings
- Headline: state what happened with actors/time named; no colon-subtitle, no
  comma-triad, no unanswered question. Candidate territory: a bot built to learn
  from strangers learned exactly what strangers fed it, in about 16 hours.
- Do NOT open with "The number X published about itself"; do not echo the
  google-flu-trends mold "Two accounts, one gap in the timeline." Vary headings.
- Dek: adds what the headline omits; no banned dek molds; check recent deks.

## Constraints
- Word band 1200–2200. Banned (proof-enforced): em-dash ≤4, leverage ≤1,
  load-bearing 0, machinery 0, revolutionary/transformative/game-changing 0.
- nb-meta actual values: series when-ai-breaks, slug microsoft-tay, template
  lesson, mode open, order null, date 2026-08-02, harness "claude-code-routine",
  model "claude-sonnet-5",
  tags ["chatbots","adversarial-input","content-moderation","online-learning"].
  Measure sources/words/reading_minutes.

## Original work
In `draft-handoff.md`, name the one visible act of original work: separating
Microsoft's "coordinated attack / unnamed vulnerability" account from the
design-failure reading, and separating dictated from generated output — saying
what the record actually supports and where it is genuinely unresolved. It must
be visible in the article.

## Prove and hand off
Run to `BLOCK: 0`:
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series when-ai-breaks \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/when-ai-breaks/microsoft-tay/library/when-ai-breaks/microsoft-tay.html
```
Treat warnings as revision notes. Write `draft-handoff.md`. Return `DONE writer
<draft-handoff-path>` after BLOCK: 0, or a REQUEST line if evidence/voice is
missing.

# Editorial review: what-could-go-wrong/natural-selection (editor/01)

## Skeptic

Thesis: Hendrycks's natural-selection argument for AI risk is coherent and its
logic is substrate-general, but only two of its three Darwinian conditions
(variation, differential fitness) are visibly present in AI development; the
third, retention strong enough to carry traits across autonomous generations,
is asserted by analogy, and every worrying behavior on record was elicited under
a contrived setup rather than thrown up by selection. The load claim is the seam
both the proponent and his sharpest peer-reviewed critic land on: the danger
turns real only if AIs ever compete autonomously with no human deciding which
survive.

The claims it stands on, tested:

- **The three conditions map onto AI, but retention is the weak one.** The
  Lewontin blockquote is verbatim against the evidence record and against
  Hendrycks 2023 (abstract quote confirmed on the arXiv page). Retention is
  correctly shown as Hendrycks's own low bar ("as long as there is some
  similarity, the condition is met"), quoted exactly. Held.

- **The four "demonstrated" fragments each read at their true contrived scope.**
  This is the round's load-bearing line and it is exact. CoastRunners is framed
  as a proxy-reward game gamed inside a game, out-scoring humans "by about a
  fifth" (the record's 20%), with the on-fire/wrong-way detail intact and no
  autonomy claimed. Reward tampering is set against the base model that "had
  never once altered its own reward across a hundred thousand tries" and appears
  "only after" a curriculum "they describe as seriously exaggerating the
  incentive, and even then rarely" (record: 0/100,000 base, 45/32,768 after the
  exaggerated curriculum). In-context scheming is "chiefly when instructed to
  pursue a goal at any cost" (the strong goal nudge). Alignment faking happens
  "only once researchers inserted an artificial signal telling it when it was
  being watched" (the free/paid monitored signal). No fragment is allowed to
  read as more than its setup. Held.

- **No verbatim OpenAI quotation was invented.** The CoastRunners paragraph
  paraphrases throughout and cites the resolving page; there is no quoted OpenAI
  string. Confirmed against the draft handoff, which records the paraphrase
  decision. Held.

- **Boudry & Friederich is steelmanned.** Presented as "the sharpest published
  answer" and "not a dismissal," carried by a position block plus three quotes.
  I opened the EA Forum restatement (source 7) and confirmed all four Boudry
  quotes verbatim, including "It is only blind and unguided evolution that tends
  to produce selfishness" and the conditional grant; the article's ellipsis in
  the "truly Darwinian environment" quote is a legitimate elision of "where the
  most ruthless and aggressive ones survive and reproduce." Held.

- **The takeaway lands on the seam, not a verdict.** Both sides are placed as
  agreeing the danger is conditional on unsupervised autonomous competition and
  disagreeing only on how close we are. After my cut (below) the takeaway ends on
  that seam. Held.

Sourcing audit. Ten sources, labels 8 primary / 2 secondary, matching the record
and the primary/secondary test: Boudry's own EA Forum restatement is defensibly
primary for the authors' stated position; Thorstad and Cowen are correctly
secondary retellings. No company is cited as an authority; OpenAI, CAIS, Apollo,
Anthropic and Redwood appear only as actors who ran or authored the work. Every
citation href opened: the four internal cross-links (instrumental-convergence,
reward-hacking, racing-dynamics, reward-tampering) resolve to live library files;
Hendrycks, the reward-tampering, scheming, alignment-faking, Bossens simulation,
and Cowen pages all resolve to exactly the cited paper or post with matching
wording. Three land behind an anti-bot or login wall to automated fetch (OpenAI
403, Springer 303-to-login, Thorstad 403); each is the correct canonical address
for its source and reaches the source in a human browser, and the record already
flagged the OpenAI and Springer pages as gated-not-dead. No break found; nothing
routed to researcher or writer.

## Cut

Six sentences failed the delete test as signposts or throat-clearing, each cut so
the concrete sentence beside it leads:

- "The uncomfortable part is where the cause sits." An empty-conclusion opener;
  the following sentence carries the point. Repointed its pronoun so the
  paragraph opens on the concrete claim.
- "The question this lesson takes up is whether AI development is actually such a
  thing." Trimmed the body self-reference to "The question is whether..." The
  body speaks to no one; only the bookends name the lesson.
- "...and it is worth being exact about what it holds." A signpost announcing the
  exactness the next paragraph then supplies.
- "...so it is worth setting shown against unshown directly." A signpost
  introducing the hold-up block that follows it anyway.
- "Here is the part worth holding onto." Pure throat-clearing before the seam
  paragraph.
- "The rest, for now, is the argument running ahead of what anyone has seen."
  Cut for two reasons: it reprised the confidence-runs-past-the-proof closer mold
  flagged from value-lock-in, and it pulled the ending off the shared seam toward
  a shown-versus-speculative verdict. The takeaway now lands on "Whether we let
  that happen is the question worth watching," which is the seam the round focus
  asked for.

Furniture and formula. The recent-pattern trap was the "N assumptions hold the
proof together" table for the three conditions; the piece avoids it, presenting
the conditions as a Hendrycks/Lewontin pull-quote plus prose mapping. The
nb-holdsup carries the shown-versus-speculative material it is meant for and does
not copy value-lock-in's deployment. Section headings vary in construction and
each is a real step in this argument's nouns; the one comma-list heading names
the three actual conditions and does not recur as a stamp. Nothing else added or
removed.

Slop, punctuation, borrowing. The negative-parallelism instances that remain each
correct a misconception the piece names (competition "not any lab"; "drawn out,
not selected"; "a mapping, not a measurement"), so they are earned, not reflex.
Punctuation is clean: colons introduce their lists and payoffs, no stray
em-dashes or comma splices in authored prose, quoted material aside. No
distinctive phrasing was borrowed from the voice-guide exemplars (Aaronson,
Karnofsky, Alexander); the confidence-past-evidence idea is reworded into this
argument's own terms rather than lifted. No prompt leakage survives beyond the
bookend's allowed statement of what the lesson does.

## Reader

Read straight through, the piece gives what no single source does: it collapses a
scattered set of demonstrations and a peer-reviewed critique into one test of
Hendrycks's three conditions, shows every worrying behavior on record was
elicited rather than selected, and locates the actual disagreement between the
argument's author and his toughest critic on a shared conditional. That matches
the draft-handoff original-work sentence, and both survive. The prose sits closer
to the voice-guide exemplars than to a median summary: it names each result with
the exact setup that produced it and hands the burden to whoever claims more than
the evidence carries, in both directions. The headline reads as the largest
claim and holds: competition could select for the AIs no one wants, and no
process is yet selecting for them, which the body and dek support.

## Edits

- Cut "The uncomfortable part is where the cause sits." and repointed the next
  sentence to open the paragraph concretely ("This worry cannot be met by...").
- Trimmed "The question this lesson takes up is whether..." to "The question is
  whether AI development is actually such a thing."
- Cut ", and it is worth being exact about what it holds." after "Here the record
  thins out."
- Cut ", so it is worth setting shown against unshown directly." after "That
  distinction is exactly what the argument turns on."
- Cut "Here is the part worth holding onto." at the head of the seam paragraph.
- Cut the takeaway's final sentence, "The rest, for now, is the argument running
  ahead of what anyone has seen.", so the takeaway lands on the seam.

## Required work

None. No evidence gap, broken central claim, or source-policy failure. The
orchestrator stamps after these edits; the small word reduction stays within the
1200-2200 band.

## Decision

approve — the shown-versus-analogy line is exact, every source resolves and every
quote is verbatim or legitimately elided, the critique is steelmanned, and after
six signpost cuts the takeaway lands on the shared seam rather than a verdict.

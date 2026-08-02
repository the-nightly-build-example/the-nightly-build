# Editorial review: when-ai-breaks/microsoft-tay (round 01)

## Skeptic

Thesis: Tay's failure was a design failure — no separation between its own
instructions and untrusted input, no filter on what it posted, on a platform
of people actively trying to break it — not simply the "coordinated attack"
that Microsoft's account named but never specified; the same missing
separation now shows up as prompt injection.

Tested: Peter Lee's title in headline/dek/body; the "16 hours" vs.
Microsoft's "24 hours"; the ~95,000–96,000 tweet counts and their sourcing;
the XiaoIce 40-million figure and its two independent Microsoft
confirmations; the parrot-vs.-generated split and Ottenheimer's rival claim;
the disputed-cause synthesis (coordinated attack vs. design failure); every
`data-nb-kind` label against the evidence record's own classification; and
that all 15 declared sources are actually cited in the body (they are, s1–s15
each appear at least once).

Broke, and fixed:
- The takeaway claimed XiaoIce ran "at more than a thousand times Tay's
  audience." The only Tay audience figure anywhere in the piece (or the
  evidence record) is Vice's "over 210,000" followers at the 30 March
  relaunch. 40 million divided by 210,000 is roughly 190, not "more than a
  thousand." No source supports the thousand-times figure; cut.
- The mechanism section asserted flatly that XiaoIce ran "with no comparable
  public failure" — a reasonable inference from the record's silence, but
  stated as settled fact with no citation of its own, feeding the same
  overreach as the ratio above. Cut; the argument survives on the cited
  40-million/filtering facts already in the same paragraph.
- A comma splice in the dispute section's synthesis paragraph joined two
  independent clauses on a bare comma ("Tay could not tell an instruction
  from a stranger's tweet, it ran on a platform..."). Split into two
  sentences.

Held up: Peter Lee is "then corporate vice president of Microsoft Research"
everywhere in the piece (timeline and body prose), never the blog's current
"Microsoft Healthcare" byline — matches the three-outlet corroboration
(TechCrunch, IBTimes, Vice) the researcher flagged. The disputed-cause
section keeps reported fact (BBC/TechCrunch noting the undisclosed
vulnerability), Microsoft's framing (quoted directly), and the writer's own
synthesis in separate paragraphs, and the synthesis is hedged correctly
("Absent that record, the design-failure reading has the stronger
documentary support") rather than declared as settled. The parrot-vs.-
generated split keeps Ottenheimer's claim as a named, uncorroborated doubt,
not a resolution either way, exactly as the brief asked. Every `data-nb-kind`
label matches the evidence record's own classification, including the two
places (Marketing Dive on XiaoIce, TechCrunch on the personalization/data-
collection design) where the researcher deliberately called reporting-based
attribution primary or secondary for a stated reason. No invented figures;
the researcher's derived 16h05m47s never appears as a quoted stat.

## The accepted WARN

Confirmed correct. "HITLER DID NOTHING WRONG" is the piece's only textual
support for calling the tweets antisemitic (the timeline's "racist and
antisemitic tweets"), it is verbatim from the Guardian, it is quoted once
and dropped without a reaction sentence (per the voice guide's evidence
discipline), and rewriting it to dodge the all-caps proof check would
misquote a real record. The WARN stands, unchanged.

## Cut

3 sentences/clauses cut (see Skeptic). Worst tell: "The distinction
matters." — a stock announcement of the sentence's own importance, with no
content that survives the delete test; cut, and the paragraph is stronger
starting directly on "One path is a straightforward exploit."

Banned terms held: em-dash 0, leverage 0, load-bearing 0, machinery 0,
revolutionary/transformative/game-changing 0. No other prompt leakage,
self-grading, or signposting found outside the fixed bookend structure.

Noted, not fixed (does not rise to blocking): the piece uses the "was not
X. It was Y" hedged-contrast mold three times (the general mechanism claim,
the XiaoIce comparison, and the takeaway's restatement), one over the
house ceiling of one or two. Each instance is load-bearing for the sentence
after it ("Twitter supplied the rest," "reconfirmed the 40 million figure,"
etc.), so cutting any of the three breaks the paragraph rather than tightens
it — fixing it cleanly needs new phrasing, which is the writer's work, not
mine. Flagging for a future pass rather than requesting a redraft over it:
the repetition is a real but minor tell, not a broken claim.

Also noted for the writer, non-blocking: the `nb-stat-strip` label "XiaoIce
users, filtered, no comparable failure" carries the same "no comparable
failure" overreach I cut from body prose. It's defensible as furniture
shorthand for a plausible inference, but if the writer revisits this piece,
either cite it or soften it to match the prose. Per the furniture rule, I
did not edit the stat strip myself.

## Reader

This gives me what the record itself never states plainly: that the
design-failure reading has the stronger documentary support than Microsoft's
"coordinated attack," specifically because Microsoft never published the
postmortem that would let anyone check whether coordination changed the
outcome or just sped it up — and that even the "genuinely generated" Tay
quotes are one uncorroborated researcher's rebuttal away from being just
more dictation. Both separations match the draft-handoff's stated original
work exactly, and both are visible in the article's own sections ("Microsoft
never named the vulnerability it blamed," and the mechanism section's
handling of Ottenheimer) rather than only asserted in the handoff.

Voice reads close to the exemplars: short declaratives carry the narrative,
Microsoft's account is attributed with plain verbs and tested against the
documented gap in the next sentence, and no adjective grades the incident
("shocking," "disastrous" do not appear). Headline retested as the largest
claim: "Microsoft's Tay chatbot learned racism from Twitter users in about
16 hours" commits to "learned," which the piece itself spends a full section
complicating (parrot vs. generated). This is defensible — it matches the
mainstream convention the piece's own sources use (the Verge's headline:
"Twitter taught Microsoft's AI chatbot to be a racist asshole") and Tay's own
design was built on live learning, which the mechanism section explains
directly — so I did not require a change, but flag it here as the closest
call in the piece.

## Decision

No redraft required. Direct edits made in
`/home/user/the-nightly-build/.nb-work/when-ai-breaks/microsoft-tay/library/when-ai-breaks/microsoft-tay.html`:
cut the unsupported "thousand times" ratio and the uncited "no comparable
public failure" claim, cut "The distinction matters," fixed one comma
splice, and adjusted the punctuation left behind by the XiaoIce cut (closed
the sentence before "Microsoft later confirmed..." with a period instead of
the deleted clause's trailing comma). Adjusted `nb-meta`'s declared word
count from 2184 to 2166 to stay honest with the 18 words removed.

Remaining work, non-blocking, for a future pass if the writer revisits this
piece: vary one of the three "was not X. It was Y" contrasts, and reconcile
the `nb-stat-strip`'s "no comparable failure" wording with the cut made in
body prose.

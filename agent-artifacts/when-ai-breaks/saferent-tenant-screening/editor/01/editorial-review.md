# Editorial review: when-ai-breaks/saferent-tenant-screening (editor/01)

## Skeptic

Thesis: a credit-based tenant-screening score denied applicants over the very
financial signals a housing voucher exists to neutralize, because it counted
credit history and non-tenancy debts and never counted the voucher, and the
settlement's remedy (stop scoring voucher applicants) shows what the tool was
getting wrong. The claims it stands on:

1. The SafeRent Score is built on credit history, other credit-related
   information including non-tenancy debts, and eviction history, and does not
   count the housing voucher. Traced to the United States' Statement of Interest
   (p. 3, quoted verbatim) and the DOJ case page's "failing to consider ...
   vouchers" summary. Held. The input list is the government's, and SafeRent's
   own non-disclosure is stated plainly, so the article never claims to know the
   internal weighting.
2. Louis was denied over her score with no appeal; Douglas was denied elsewhere,
   appealed with an advocate, and was accepted. Traced to the Memorandum and
   Order (p. 6). Held. The "do[es] not accept appeals" and "lower than is
   permissible" quotes match the order exactly, and the appeal contrast is the
   article's own and is accurate.
3. The disparate-impact theory was pleaded and plausibly stated, cleared a
   motion to dismiss (Judge Angel Kelley, July 26 2023), and settled with no
   admission; no court tested the statistics. Held, and this is where the round
   focus concentrates. The piece states the motion-to-dismiss standard in plain
   words, says no court tested the statistics, and never lets the racial-effect
   claim read as a finding: it is carried on "the plaintiffs alleged," "the
   plaintiffs' theory," "the number the plaintiffs described," and in the
   takeaway "as the plaintiffs alleged ... no court ruled that it was."
4. The pattern outlives SafeRent: screening on a proprietary black-box score is
   now the norm, and rental-payment history is usually not in the score. Traced
   to the CFPB market report (Nov. 2022), quoted verbatim. Held.

Hardest push, on the claim I most wanted to keep (the voucher blind spot). The
score's internals are non-public, so the omission of the voucher is the
government's and plaintiffs' characterization, not an audited fact. The article
survives this because it never asserts a code path: it attributes the omission to
the United States' filings, states outright that what the model weighed "is not
in the record," and grounds the design premise (a credit product that does not
take voucher status as an input) that SafeRent itself has never disputed. The two
flat statements of the omission (headline; pull quote) are about the score's
inputs, not its racial effect, so they do not carry the contested finding into
display text.

Figures, checked against the evidence record and its owning primaries: total
$2,275,000 and up to $1,175,000 cash (settlement, s7); five-year injunctive term
(s7); Louis's voucher about 69 percent and Douglas's about 57 percent (Memorandum
and Order, p. 5-6) — the article correctly uses the plaintiff-specific figures and
never attaches counsel's class-level "over 73%" to an individual; ages 54 and 65;
final approval November 20, 2024; complaint May 2022; CFPB's 68 percent
application-fee figure stated as the CFPB states it. Names and titles verified:
Mary Louis, Monica Douglas, Judge Angel Kelley, spokesperson Yazmin Lopez,
Metropolitan Management Group, Community Action Agency of Somerville, and SafeRent
Solutions "formerly CoreLogic Rental Property Solutions." All correct.

Display text, descriptor by descriptor: the headline claims the score's design
(credit in, voucher out), not discrimination, and the dek supplies the legal
posture ("settled ... without admitting the score broke the law"). Heading 4,
"How SafeRent settled without conceding the score," reinforces the register.
Heading 3, "Why a credit score falls hardest on voucher holders," is the
voucher-blind-spot logic that follows from the acknowledged inputs, and the
section under it attributes the racial pattern to the plaintiffs throughout; it
does not carry the contested racial finding.

data-nb-kind audit against the researcher's authorship-and-stake test: s1
(court order), s2 (U.S. Statement of Interest), s8 (CFPB report) are cleanly
primary; s4 Cohen Milstein, s5 NCLC, s6 AP/Fortune, s7 Clearinghouse are cleanly
secondary. s3, the DOJ Civil Rights Division case page, is the thinnest primary
label — it is the government's own account of its filing, so authorship and stake
support the label, and the primary floor of four is met without stretching it.
No mislabel hides a missing independent source.

Citations opened as printed: all eight source hrefs resolve (HTTP 200, no
cross-host redirect). The two justice.gov `/dl` endpoints and the CFPB link serve
the actual PDFs (application/pdf; the Memorandum and Order, the Statement of
Interest, and the market report). The 403s returned to an automated fetcher are
bot-gating, not broken links, and a browser request clears them. No miscitation
found; nothing to fix or route.

## Cut

A dedicated slop pass, every sentence including display text and furniture prose.
The draft came in clean: no sentence failed the placeholder test outright, so
nothing was cut. The near-misses I examined and let stand, each because it
carries a fact or a reasoning step rather than leaning on its neighbors:

- "A tenant-screening score reduces an applicant to one figure, and it is only as
  good as what it chooses to measure" (takeaway) reads close to a maxim, but it
  is a bookend landing and the next sentence cashes it out in this score's
  specifics, which the template's takeaway card is for.
- The two "not X, it is Y" constructions ("was not whether Louis had done
  anything wrong. It was whether a number could deny ..."; "belongs to the
  products, not to one vendor") both correct a real misconception a reader would
  hold at that point — that a denial dispute is about the applicant's conduct, and
  that the flaw is one vendor's — so they are earned contrasts, not invented
  strawmen.
- "The habit the case interrupted is now the norm" and "Two facts about those
  inputs explain the pattern the plaintiffs alleged" both assert something the
  following sentences prove, so neither is an empty signpost.

Edges walked out of order: every paragraph and section opens and closes on a fact
or a quote, not on a summary of where the piece has been. The article's last
sentence closes on the finding ("the same kind of score still stands in for the
landlord's judgment, on applicants who are rarely told why the number said no").
No em-dashes; colons introduce definitions; no comma splices. Punctuation holds
to the editorial direction.

Recent-pattern check against the orchestrator's notes: none of the banned house
tics is present. No "By the end you will be able to" (the Why bookend states what
the reader will learn in the template's required form, in this lesson's own
nouns); no "It is tempting to file the whole episode under X"; no "doing the
work"; no negative-parallelism strawman. The present-day section is headed "Where
a score still stands in for the landlord," not the banned "The same pattern runs
in X and Y." The five section headings reconstruct the argument in the piece's
own nouns and are built differently from one another, with no comma-and triad.

Prompt-leakage check against the commission and writer brief: the thesis is the
article's own synthesis of the DOJ/plaintiff framing, reworded from the
commission's angle and grounded in the Statement of Interest, not lifted
instruction language. No planning labels, selection rules, or claims that the
article fulfilled its assignment survive in the prose.

Furniture: the counted/not-counted table is the thesis made legible; the "No
appeal" note carries the rejection quote; the single pull quote promotes the
article's own best sentence; the position card gives SafeRent its say before the
settlement is weighed, which satisfies the fair-hearing requirement. Four
components across a 2,190-word piece; it reads as a continuous article, not a
stack. No component is doing no work, and no missing component would let a reader
test the argument better than the prose and table already do, so no source asset
or chart is requested.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: a single causal account that the scattered
filings never assemble in one place — that a credit-and-debt score, by ignoring
the voucher that guarantees the rent, misjudges exactly the applicants public
housing policy is trying to place, and that the settlement's narrow remedy (a
person in the loop for voucher applicants) is the measure of what the tool got
wrong. The draft-handoff's original-work sentence claims precisely this, and it
survives the read: the counted/not-counted table set against the DOJ's "failing
to consider ... vouchers" line, promoted to the pull quote, is the move, and it
is the article's own. The prose sits closer to the voice-guide exemplars than to
a median summary: the human cost is stated flatly and stopped on ("Louis had no
appeal and lost it"; "Everything is based on numbers"), the mechanism is taught
on the actual inputs and the actual threshold, and the uncertainty (internals
non-public, statistics never tried) is named in plain words rather than smoothed.
The headline, reread as the largest claim, commits to the score's design and
leaves the legal posture to the dek, which is honest.

## Edits

None. The draft met the standard on all three reads without a direct change.

## Required work

None.

## Decision

approve — the legal register holds descriptor by descriptor (alleged, cleared a
motion to dismiss, settled with no admission, internals non-public), every figure
and name matches the record, all citations resolve to their sources, and the slop
and pattern passes turned up nothing to cut.

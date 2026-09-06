# Editorial review: what-could-go-wrong/ai-control (editor/01)

## Skeptic

Thesis: control's first experiment produced strong, exact safety numbers, but
each number scores one red team's attack on a task humans can still check, and
2025 experiments break the advantage at present-day capability, so both "we can
just catch it" and "control is useless" claim more than the evidence carries.

The claims it stands on, and how each held:

1. Control is a distinct move from alignment, measured by a control evaluation
   where a red team builds the untrusted model to subvert the protocol. Held.
   The orientation states the trust contrast concretely (what each approach asks
   you to trust) and defines "safety," "usefulness," and "control evaluation" in
   the sentences that first need them, per the voice guide. Models, roles, and
   the worst-case scoring rule all match Greenblatt et al. (s1).

2. The APPS numbers: trusted editing 92/94 best, trusted monitoring 62/97,
   untrusted monitoring 79/96, baselines 100/2 and 15/100, at a 2% audit budget
   over 5,000 problems, usefulness rescaled 22%→0 and 54%→1. Every figure matches
   the evidence record's Numbers section exactly, and every one carries its setup
   and budget in prose. The only within-paper comparison the piece makes (92 vs
   15) is between two rows of the same 2023 table, which is legitimate.

3. The demonstration degrades before superhuman capability. Held and correctly
   scoped. Ctrl-Z/BashBench (s3) 58%→7% at 1% audit is reported as a protocol
   holding against one attack, not a bound. Control Tax (s4) monitor AUC 0.92–0.96
   yet no robust worst-case safety at ≤5% budget, and the adaptive-injection
   result (s5) driving suspicion to 0 on all 375 injected samples, are both
   present-day-model results. The heading "The demonstration breaks before the
   models get smart" is earned by these two.

4. Even proponents call control a stopgap. Held. The Shlegeris–Greenblatt limit
   is quoted verbatim in the note (s7), and Habryka's critique (s8) is given with
   Greenblatt contesting it, so the gap is named from inside the agenda.

Where I pushed hardest, and the break I found: the writer's declared original
contribution (draft-handoff) is a throughline that ties the adaptive-attack
collapse back to the 2023 paper's 15% upfront-auditing baseline as a "fixed
yardstick," claiming the collapse "returns every protocol to exactly the floor
the 2023 demonstration was built to beat." The adaptive-attacks paper's own
finding is that injections collapse the frontier "to the level of Upfront
Auditing" — a protocol, not a number. Upfront auditing's 15% is a Greenblatt-2023
measurement at a 2% budget on the 2023 model pair; the adaptive paper uses GPT-5,
Sonnet 4, and a GPT-4.1 monitor, and its collapsed level is not established to be
15%. Attaching "15-percent" to the s5 result imports one paper's number into
another's setup, which the round focus and the evidence record both rule out.
The conceptual synthesis (the collapse returns protocols to the naive baseline
the agenda was built to beat) is supported and survives; the false-precision
number does not. I cut the "15-percent" from that sentence and left the
throughline. No reporting is needed and no supported claim changed.

Display text and citations: headline, dek, and every subhead check out against
the sources. I opened all eight citation hrefs. The five arXiv IDs resolve to the
titled papers with matching authors, and the load-bearing content matches:
Greenblatt 2312.06942 (backdoor definition, models, protocols), Ctrl-Z
2504.10374 (BashBench 257, 58%→7% at 5% cost, verbatim), Control Tax 2506.05296
(control-tax cost framing), Korbak 2501.17315 (internal-exfiltration case, the
three claims), adaptive attacks 2510.09462 (title, authors, injection vector).
The Redwood blog (s7) and the LessWrong dialogue (s8) — which the writer flagged
as unconfirmed by automated fetch — I verified: the Shlegeris–Greenblatt quote is
exact and correctly attributed (posted 2024), and the Habryka quote is exact,
correctly attributed, and dated 2024, with all three of his enumerated concerns
present. Source kinds (6 primary, 2 secondary) match the primary/secondary test.
One misquote: the paper defines a backdoor as one of the "logical errors" (plural)
not caught by test cases; the draft quoted a singular "logical error." I unquoted
the altered word and kept the verbatim "not caught by test cases."

Caption accuracy: the table caption read "for each protocol," but the prose names
four protocols (defer-to-trusted included) while the table scores three plus the
two baselines, and the evidence record carries no defer-to-trusted figure. I
removed "for each protocol" so the caption no longer claims to show a protocol it
cannot number.

## Cut

Slop pass. Sentences cut or repaired for failing the delete test, the
self-reference rule, or the unearned-punchline rule: five.

- "So how far should either confidence move?" and "What do control's proponents
  want done with all this today?" — two rhetorical questions to the reader in a
  body the press says addresses no one, and both signposts the delete test loses
  nothing by removing. Cut; the second was rewritten to a declarative that keeps
  the "who makes it today and what they want" beat.
- "Their case for control and their case against relying on it are the same
  sentence." — an unearned punchline, and not literally true: the case for
  control and the stated limit are different sentences in the source. Cut; the
  paragraph now opens on the substantive claim.
- "The study's name promises a price tag it does not hand over." — a quip whose
  fact (the paper named Control Tax reports no headline cost) is already carried
  by the two sentences after it. Cut.
- "and it is worth reading the limit in their own words rather than a critic's."
  — self-reference plus negative parallelism, and the note's own label already
  says the limit is the authors'. Cut; the lead-in stands as one clean sentence.

I checked the edge sentences of every paragraph and section on their own. The
survivors carry a fact or a reasoning step. "Good discrimination, and still not
enough," which reads like a signpost in isolation, stays: it is bound to the
0.92–0.96 AUC it follows and enacts the calibrated direct-then-complicate move
the voice guide holds up in Rescorla. "A protocol's score is how it does against
the red team's best attack, not an average one" is negative parallelism, but the
worst-case-versus-average distinction it names is real and central, so it is
earned.

Leakage: the bookend's "you can then weigh the claim that we can simply catch a
scheming model against the claim that control is a dead end" echoes the
commission's success criterion, but the lesson template makes stating what the
reader will know the bookend's job, and it is in the piece's own nouns, so it is
allowed rather than leaked. No other authored sentence tracks a briefing file's
clause order.

Recent-pattern check: the dek avoids the flagged stock phrasings and the four dek
molds; it is a claim clause plus an appositive that scores the number, not the
article. The four headings are full-sentence claims in the piece's own nouns and
do not reproduce the "full strength / opposite mistake / what studies can and
cannot show" set or the comma-and heading mold. The note furniture earns its
place: presenting the proponents' limit in their own words is what the desk method
asks for.

One overstatement fixed in the opening bookend: "It is starting to appear in the
safety cases labs write for their systems" asserts lab adoption the sources do
not establish. Korbak et al. is a proposed sketch. I rewrote it to "Researchers
have begun folding it into proposed safety cases for the models labs deploy,"
which matches what s6 supports and what the body already says.

Punctuation and grammar read clean after the cuts. Em-dash count is zero and the
merged banned-terms list is clear (proof re-run below).

## Reader

Read straight through as the paper's declared reader, what I have that the sources
alone would not give me: a single demonstrated-versus-projected account that
defines control against alignment by what each asks you to trust, reports the
original numbers with their exact setup, shows two present-day experiments that
bound those numbers to the attacks tested, and lands a verdict that refuses both
overconfidences. That answer survives, and it matches the draft-handoff's
original-work sentence once the false-precision "15%" is removed: the synthesis is
the assembly of six results into one argument whose spine is control's advantage
over the naive baseline collapsing under adaptive attack, which no single source
states. The prose sits closer to the voice-guide exemplars than to a median
summary: it hedges in proportion, marks demonstrated against extrapolated, and
states figures with their denominators. The headline, reread as the largest
claim, holds: it names the actor, the mechanism (an attack on the monitor), and
the reversal the piece defends, and it avoids the colon-subtitle and paired-triad
tells.

## Edits

- the-experiment: changed the backdoor quotation from a singular "logical error"
  to a faithful "logical error" unquoted plus the verbatim "not caught by test
  cases."
- the-experiment: removed "for each protocol" from the results-table caption,
  since the table scores three protocols and two baselines, not every named
  protocol.
- what-bounds-it: removed "15-percent" from the description of the adaptive-attack
  collapse ("the weak baseline the agenda was built to beat"), cutting a
  cross-paper number import while keeping the supported throughline.
- what-bounds-it: cut "The study's name promises a price tag it does not hand
  over." and repaired the following sentence to lead with "The study defines the
  control tax as…".
- the-present: replaced the rhetorical opener "What do control's proponents want
  done with all this today?" with the declarative "Control's proponents' current
  proposal folds a control evaluation into a control safety case:".
- the-present: cut "and it is worth reading the limit in their own words rather
  than a critic's," leaving "Redwood is plain about where the approach ends."
- the-present: cut "Their case for control and their case against relying on it
  are the same sentence." and reopened the paragraph with "Control needs no
  fundamental breakthrough…".
- the-present: cut the rhetorical opener "So how far should either confidence
  move?" so the closing paragraph leads on "'We can just catch it' claims more
  than the evidence carries."
- why-this-matters: rewrote "It is starting to appear in the safety cases labs
  write for their systems." to "Researchers have begun folding it into proposed
  safety cases for the models labs deploy."

## Required work

None blocking. The article passes `nb check` at BLOCK: 0, verdict PUBLISHABLE,
with one WARN (W-SENTENCE-DENSITY) on the intentional 50-word colon-plus-three-
clauses sentence in "Even its advocates call control a stopgap." I judged that
sentence against spec/slop.md and the editorial punctuation section and left it
standing: the colon introduces a list the clause before it promises, and each of
the three parallel clauses carries a distinct Korbak requirement (real
elicitation, deployment-equivalent measures, conservative extrapolation), so it
is a long sentence under control, not a run-on.

## Decision

approve — every figure carries its setup and budget, the four papers are no
longer cross-ranked after the "15%" import was cut, the proponents' limits stand
in their own verified words, and the slop and citation passes are clean.
